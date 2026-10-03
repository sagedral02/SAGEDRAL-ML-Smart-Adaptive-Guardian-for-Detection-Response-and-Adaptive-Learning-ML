#!/usr/bin/env bash
# ==============================================================================
# SAGEDRAL-ML Comprehensive Diagnostics & System Health Collector
# Dumps full system, network, firewall, database, ML models, logs, and service
# state into a single unified file in $HOME for complete end-to-end debugging.
# ==============================================================================
set -u

# Ensure running with root privileges for complete log & firewall visibility
if [[ $EUID -ne 0 ]]; then
    echo "[!] Please run this script with sudo: sudo bash scripts/collect_full_diagnostics.sh"
    exit 1
fi

REAL_USER="${SUDO_USER:-$USER}"
USER_HOME=$(getent passwd "$REAL_USER" | cut -d: -f6)
if [[ -z "$USER_HOME" || ! -d "$USER_HOME" ]]; then
    USER_HOME="/root"
fi

OUTPUT_FILE="${USER_HOME}/sagedral_full_debug.log"
rm -f "$OUTPUT_FILE"

log_section() {
    local title="$1"
    echo "" >> "$OUTPUT_FILE"
    echo "================================================================================" >> "$OUTPUT_FILE"
    echo "  $title" >> "$OUTPUT_FILE"
    echo "================================================================================" >> "$OUTPUT_FILE"
}

echo "Collecting SAGEDRAL-ML full system diagnostics..."
echo "Output will be saved to: $OUTPUT_FILE"

# 1. System Information
log_section "1. SYSTEM & HOST INFORMATION"
echo "Timestamp: $(date -u '+%Y-%m-%d %H:%M:%S UTC') / Local: $(date)" >> "$OUTPUT_FILE"
echo "Hostname : $(hostname)" >> "$OUTPUT_FILE"
echo "Kernel   : $(uname -a)" >> "$OUTPUT_FILE"
if [[ -f /etc/os-release ]]; then
    cat /etc/os-release >> "$OUTPUT_FILE"
fi
echo -e "\n--- CPU Info ---" >> "$OUTPUT_FILE"
lscpu 2>/dev/null | grep -E "Model name|Architecture|CPU\(s\):|Thread|Core" >> "$OUTPUT_FILE" || true
echo -e "\n--- Memory & Disk ---" >> "$OUTPUT_FILE"
free -h >> "$OUTPUT_FILE"
df -h / /var/lib /var/log 2>/dev/null >> "$OUTPUT_FILE" || df -h / >> "$OUTPUT_FILE"

# 2. Network & Routing Configuration
log_section "2. NETWORK INTERFACES & ROUTING"
echo "--- IPv4 Forwarding Status ---" >> "$OUTPUT_FILE"
sysctl net.ipv4.ip_forward >> "$OUTPUT_FILE" 2>&1
echo -e "\n--- Network Interfaces (Brief) ---" >> "$OUTPUT_FILE"
ip -br addr >> "$OUTPUT_FILE" 2>&1
echo -e "\n--- Network Interfaces (Detailed) ---" >> "$OUTPUT_FILE"
ip addr show >> "$OUTPUT_FILE" 2>&1
echo -e "\n--- Routing Table ---" >> "$OUTPUT_FILE"
ip route show >> "$OUTPUT_FILE" 2>&1

# 3. Netfilter / NFTables / IPTables Firewall
log_section "3. FIREWALL & NETFILTER STATUS"
echo "--- NFTables Sagedral Table ---" >> "$OUTPUT_FILE"
if command -v nft &>/dev/null; then
    nft list table inet sagedral >> "$OUTPUT_FILE" 2>&1 || echo "Table inet sagedral not found" >> "$OUTPUT_FILE"
    echo -e "\n--- NFTables Sagedral Blocklist Elements ---" >> "$OUTPUT_FILE"
    nft list set inet sagedral blocklist >> "$OUTPUT_FILE" 2>&1 || echo "Set inet sagedral blocklist not found" >> "$OUTPUT_FILE"
    echo -e "\n--- NFTables Sagedral Blocknets Elements ---" >> "$OUTPUT_FILE"
    nft list set inet sagedral blocknets >> "$OUTPUT_FILE" 2>&1 || echo "Set inet sagedral blocknets not found" >> "$OUTPUT_FILE"
else
    echo "nft command not available" >> "$OUTPUT_FILE"
fi
echo -e "\n--- IPTables Rules (IPv4) ---" >> "$OUTPUT_FILE"
iptables -L -n -v --line-numbers 2>&1 >> "$OUTPUT_FILE" || true
echo -e "\n--- IPTables NAT Table ---" >> "$OUTPUT_FILE"
iptables -t nat -L -n -v --line-numbers 2>&1 >> "$OUTPUT_FILE" || true

# 4. Service & Process State
log_section "4. SERVICE & PROCESS STATE"
echo "--- Systemd Service Status (sagedral-ml) ---" >> "$OUTPUT_FILE"
systemctl status sagedral-ml --no-pager -l >> "$OUTPUT_FILE" 2>&1 || echo "Service not registered in systemd" >> "$OUTPUT_FILE"
echo -e "\n--- Running Processes (sagedral / uvicorn / scapy) ---" >> "$OUTPUT_FILE"
ps aux | grep -E "sagedral|uvicorn" | grep -v grep >> "$OUTPUT_FILE" || echo "No sagedral processes currently running" >> "$OUTPUT_FILE"
echo -e "\n--- Listening Ports (TCP/UDP) ---" >> "$OUTPUT_FILE"
ss -tulpn | grep -E "8000|sagedral|uvicorn" >> "$OUTPUT_FILE" 2>&1 || ss -tulpn >> "$OUTPUT_FILE" 2>&1

# 5. Database Verification
log_section "5. DATABASE HEALTH & TABLE ROW COUNTS"
DB_PATH="/var/lib/sagedral-ml/sagedral.db"
echo "Database path: $DB_PATH" >> "$OUTPUT_FILE"
if [[ -f "$DB_PATH" ]]; then
    ls -lh "$DB_PATH"* >> "$OUTPUT_FILE" 2>&1
    if command -v sqlite3 &>/dev/null; then
        echo -e "\n--- SQLite Tables ---" >> "$OUTPUT_FILE"
        sqlite3 "$DB_PATH" ".tables" >> "$OUTPUT_FILE" 2>&1
        echo -e "\n--- Table Counts ---" >> "$OUTPUT_FILE"
        for tbl in alerts blocked_ips signature_rules users traffic_stats audit_logs system_events alembic_version; do
            cnt=$(sqlite3 "$DB_PATH" "SELECT count(*) FROM $tbl;" 2>/dev/null || echo "N/A")
            echo "  $tbl: $cnt" >> "$OUTPUT_FILE"
        done
        echo -e "\n--- Latest 5 Alerts Recorded ---" >> "$OUTPUT_FILE"
        sqlite3 -header -column "$DB_PATH" "SELECT id, datetime(timestamp, 'unixepoch', 'localtime') as time, src_ip, dst_ip, attack_type, severity, action_taken, final_score FROM alerts ORDER BY id DESC LIMIT 5;" >> "$OUTPUT_FILE" 2>&1 || true
        echo -e "\n--- Currently Active Blocked IPs ---" >> "$OUTPUT_FILE"
        sqlite3 -header -column "$DB_PATH" "SELECT id, ip, reason, datetime(blocked_at, 'unixepoch', 'localtime') as blocked_at, is_active FROM blocked_ips WHERE is_active=1 ORDER BY id DESC LIMIT 10;" >> "$OUTPUT_FILE" 2>&1 || true
    else
        echo "sqlite3 CLI utility not installed; file size: $(stat -c%s "$DB_PATH") bytes" >> "$OUTPUT_FILE"
    fi
else
    echo "Database file $DB_PATH does not exist yet." >> "$OUTPUT_FILE"
fi

# 6. Machine Learning Models & Metadata
log_section "6. MACHINE LEARNING MODELS & DRIFT METADATA"
MODEL_DIR="/var/lib/sagedral-ml/models"
echo "Model Directory: $MODEL_DIR" >> "$OUTPUT_FILE"
if [[ -d "$MODEL_DIR" ]]; then
    ls -la "$MODEL_DIR" >> "$OUTPUT_FILE" 2>&1
    if [[ -f "$MODEL_DIR/metadata.json" ]]; then
        echo -e "\n--- metadata.json ---" >> "$OUTPUT_FILE"
        cat "$MODEL_DIR/metadata.json" >> "$OUTPUT_FILE" 2>&1
    fi
    if [[ -f "$MODEL_DIR/feature_names.json" ]]; then
        echo -e "\n--- Feature Count ---" >> "$OUTPUT_FILE"
        grep -o '"' "$MODEL_DIR/feature_names.json" | wc -l >> "$OUTPUT_FILE" 2>&1 || true
    fi
else
    echo "Directory $MODEL_DIR does not exist." >> "$OUTPUT_FILE"
fi
if [[ -x /opt/sagedral-ml/venv/bin/sagedral-ml ]]; then
    echo -e "\n--- CLI Model Info ---" >> "$OUTPUT_FILE"
    /opt/sagedral-ml/venv/bin/sagedral-ml model info >> "$OUTPUT_FILE" 2>&1 || true
fi

# 7. Configuration Inspection
log_section "7. ACTIVE CONFIGURATION (/etc/sagedral/config.toml)"
if [[ -f /etc/sagedral/config.toml ]]; then
    cat /etc/sagedral/config.toml >> "$OUTPUT_FILE" 2>&1
else
    echo "Config file /etc/sagedral/config.toml not found" >> "$OUTPUT_FILE"
fi

# 8. Python Environment & Dependency Check
log_section "8. PYTHON VIRTUALENV & PACKAGE INTEGRITY"
VENV_PY="/opt/sagedral-ml/venv/bin/python"
if [[ -x "$VENV_PY" ]]; then
    echo "Python: $("$VENV_PY" --version)" >> "$OUTPUT_FILE"
    echo -e "\n--- Pip Package List ---" >> "$OUTPUT_FILE"
    "$VENV_PY" -m pip list >> "$OUTPUT_FILE" 2>&1
    echo -e "\n--- Core Import Sanity Test ---" >> "$OUTPUT_FILE"
    "$VENV_PY" -c '
import sys
modules = [
    "sagedral_ml",
    "sagedral_ml.config",
    "sagedral_ml.capture.sniffer",
    "sagedral_ml.features.extractor",
    "sagedral_ml.detection.signature_engine",
    "sagedral_ml.detection.ml_engine",
    "sagedral_ml.detection.decision_engine",
    "sagedral_ml.ips.response",
    "sagedral_ml.api.main",
    "scapy",
    "fastapi",
    "uvicorn",
    "alembic",
    "passlib",
    "bcrypt",
    "numpy",
]
errors = []
for m in modules:
    try:
        __import__(m)
        print(f"  [OK] {m}")
    except Exception as exc:
        errors.append((m, str(exc)))
        print(f"  [FAIL] {m}: {exc}")
if errors:
    print(f"\nTotal import errors: {len(errors)}")
    sys.exit(1)
else:
    print("\nAll core modules imported successfully without errors.")
' >> "$OUTPUT_FILE" 2>&1
else
    echo "Virtualenv python $VENV_PY not found" >> "$OUTPUT_FILE"
fi

# 9. Local API Health Check
log_section "9. LOCAL API HEALTH CHECK (http://127.0.0.1:8000)"
if command -v curl &>/dev/null; then
    echo "--- GET /api/v1/status ---" >> "$OUTPUT_FILE"
    curl -s -m 3 http://127.0.0.1:8000/api/v1/status >> "$OUTPUT_FILE" 2>&1 || echo "Could not reach /api/v1/status" >> "$OUTPUT_FILE"
    echo -e "\n\n--- GET / (Dashboard Index Header) ---" >> "$OUTPUT_FILE"
    curl -s -I -m 3 http://127.0.0.1:8000/ >> "$OUTPUT_FILE" 2>&1 || echo "Could not reach Dashboard root" >> "$OUTPUT_FILE"
else
    echo "curl command not found" >> "$OUTPUT_FILE"
fi

# 10. Systemd Journal Logs (Last 200 lines)
log_section "10. SYSTEMD JOURNAL LOGS (Last 200 lines)"
journalctl -u sagedral-ml -n 200 --no-pager >> "$OUTPUT_FILE" 2>&1 || echo "No journal entries found" >> "$OUTPUT_FILE"

# 11. Application File Log (/var/log/sagedral-ml.log)
log_section "11. FULL APPLICATION FILE LOG (/var/log/sagedral-ml.log)"
if [[ -f /var/log/sagedral-ml.log ]]; then
    cat /var/log/sagedral-ml.log >> "$OUTPUT_FILE" 2>&1
else
    echo "File /var/log/sagedral-ml.log does not exist." >> "$OUTPUT_FILE"
fi

# Fix ownership so non-root user can read/copy
chown "$REAL_USER:$REAL_USER" "$OUTPUT_FILE"
chmod 0644 "$OUTPUT_FILE"

echo ""
echo "================================================================================"
echo "  Diagnostics collection COMPLETE!"
echo "  Saved to: $OUTPUT_FILE"
echo "  File size: $(stat -c%s "$OUTPUT_FILE" 2>/dev/null || wc -c < "$OUTPUT_FILE") bytes"
echo "================================================================================"
echo "You can now view or copy it directly:"
echo "  cat ~/sagedral_full_debug.log"
echo "================================================================================"
