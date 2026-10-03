#!/bin/bash
# SAGEDRAL-ML Automated Installer Script
# v1.0.1 — Updated for Python 3.8.10 compatibility (BackBox / Ubuntu 20.04 LTS)
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
info() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; exit 1; }

echo "================================================"
echo "  SAGEDRAL-ML Installer v1.0.1"
echo "  Smart Adaptive Guardian (NIDPS)"
echo "  Compatibility: Python >= 3.8 (tested Py3.8.10)"
echo "================================================"

# 1. Root privilege check
[[ $EUID -ne 0 ]] && error "Installer must be run as root (use: sudo bash scripts/install.sh)"

# 2. Python version pre-flight check
info "Checking Python version..."
if command -v python3 &>/dev/null; then
    PY_VER=$(python3 -c 'import sys; print("%d.%d.%d" % sys.version_info[:3])' 2>/dev/null || echo "0.0.0")
    PY_MAJ=$(python3 -c 'import sys; print(sys.version_info[0])' 2>/dev/null || echo 0)
    PY_MIN=$(python3 -c 'import sys; print(sys.version_info[1])' 2>/dev/null || echo 0)
    info "Detected python3 version: ${PY_VER}"
    if [[ "$PY_MAJ" -lt 3 ]] || [[ "$PY_MIN" -lt 8 ]]; then
        error "SAGEDRAL-ML requires Python >= 3.8. Detected ${PY_VER}. Install python3.8+ and try again."
    fi
else
    error "python3 command not found. Please install python3 first."
fi

# 3. Install system dependencies
info "Installing system dependencies (python3-dev, libpcap, nftables, build-essential)..."
if command -v apt-get &>/dev/null; then
    warn "If apt reports Temporary failure resolving, fix DNS/network access before continuing."
    if ! DEBIAN_FRONTEND=noninteractive apt-get update -qq; then
        warn "apt update failed; DNS/network diagnostic follows:"
        getent hosts archive.ubuntu.com security.ubuntu.com 2>/dev/null || true
        warn "Continuing with cached apt indexes; retry if dependency installation fails."
    fi
    # build-essential + python3-dev Wajib untuk compile lightgbm/numpy/scikit-learn C extensions di Py3.8
    apt-get install -y --no-install-recommends \
        python3-venv \
        python3-pip \
        python3-dev \
        python3-setuptools \
        build-essential \
        libpcap-dev \
        nftables \
        tcpdump \
        libgomp1 \
        ca-certificates \
        curl \
        sqlite3
elif command -v yum &>/dev/null; then
    yum install -y python3-pip python3-devel libpcap-devel nftables tcpdump gcc gcc-c++ libgomp sqlite
fi

INSTALL_ROOT=/opt/sagedral-ml
VENV_DIR=/opt/sagedral-ml/venv
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
install -d -m 0755 "${INSTALL_ROOT}"
python3 -m venv "${VENV_DIR}"
VENV_PYTHON="${VENV_DIR}/bin/python"

# 4. Upgrade pip/setuptools/wheel terlebih dahulu (kritis untuk build Py3.8 wheels)
info "Upgrading pip, setuptools, and wheel for build compatibility..."
"${VENV_PYTHON}" -m pip install --upgrade pip setuptools wheel

# 5. Install Python dependencies from requirements.txt
info "Installing Python dependencies from requirements.txt..."
"${VENV_PYTHON}" -m pip install -r "${PROJECT_DIR}/requirements.txt"

# 6. Install sagedral-ml Python package in editable mode
info "Installing sagedral-ml Python package (editable mode for continuous sync)..."
"${VENV_PYTHON}" -m pip install -e "${PROJECT_DIR}"

# 7. Verify sagedral-ml CLI accessible
SAG_CLI=/usr/local/bin/sagedral-ml
[[ ! -d "${SAG_CLI}" ]] || error "CLI destination is a directory: ${SAG_CLI}. Move it aside and re-run."
ln -sfnT "${VENV_DIR}/bin/sagedral-ml" "${SAG_CLI}"
[[ -x "${SAG_CLI}" ]] || error "Installed CLI is not executable."

# 8. Create directories
info "Creating directories..."
if ! id -u sagedral &>/dev/null; then
    useradd --system --home-dir /var/lib/sagedral-ml --shell /usr/sbin/nologin sagedral
fi
install -d -m 0755 /var/lib/sagedral-ml
install -d -m 0755 /var/lib/sagedral-ml/models
install -d -m 0755 /var/lib/sagedral-ml/backups
install -d -m 0755 /var/lib/sagedral-ml/custom-rules
install -d -m 0755 /etc/sagedral
touch /var/log/sagedral-ml.log
chmod 0666 /var/log/sagedral-ml.log

# 9. Config template
if [[ ! -f /etc/sagedral/config.toml ]]; then
    "${SAG_CLI}" config template > /etc/sagedral/config.toml
    chmod 0644 /etc/sagedral/config.toml
    info "Created default config at /etc/sagedral/config.toml"
fi

# 10. Enable Kernel IPv4 Forwarding
info "Configuring IPv4 Forwarding for Gateway Inline Mode..."
echo "net.ipv4.ip_forward = 1" > /etc/sysctl.d/99-sagedral.conf
sysctl -p /etc/sysctl.d/99-sagedral.conf 2>/dev/null || sysctl -w net.ipv4.ip_forward=1 2>/dev/null || true

# 11. Initialize nftables table (input, forward, output)
info "Initializing nftables sagedral table (input + forward inline protection)..."
nft add table inet sagedral 2>/dev/null || true
nft add set inet sagedral blocklist "{ type ipv4_addr; }" 2>/dev/null || true
nft add set inet sagedral blocknets "{ type ipv4_addr; flags interval; }" 2>/dev/null || true
nft add chain inet sagedral input "{ type filter hook input priority 0; }" 2>/dev/null || true
nft add rule inet sagedral input ip saddr @blocklist drop 2>/dev/null || true
nft add rule inet sagedral input ip saddr @blocknets drop 2>/dev/null || true
nft add chain inet sagedral forward "{ type filter hook forward priority 0; }" 2>/dev/null || true
nft add rule inet sagedral forward ip saddr @blocklist drop 2>/dev/null || true
nft add rule inet sagedral forward ip saddr @blocknets drop 2>/dev/null || true

# 12. ML Model initialization
info "Initializing ML detection models..."
"${SAG_CLI}" model init --force 2>&1 || true

# 13. Install systemd service + logrotate
info "Installing systemd service..."
cp "${PROJECT_DIR}/systemd/sagedral-ml.service" /etc/systemd/system/sagedral-ml.service

info "Installing logrotate configuration..."
if [[ -f "${PROJECT_DIR}/scripts/logrotate.conf" ]]; then
    cp "${PROJECT_DIR}/scripts/logrotate.conf" /etc/logrotate.d/sagedral-ml
    info "Logrotate config installed at /etc/logrotate.d/sagedral-ml"
fi

if [ -d /run/systemd/system ] && systemctl is-system-running &>/dev/null; then
    systemctl daemon-reload
    systemctl enable sagedral-ml
    info "Starting SAGEDRAL-ML service via systemd..."
    systemctl restart sagedral-ml
    sleep 3
    if systemctl is-active --quiet sagedral-ml; then
        info "SAGEDRAL-ML systemd service is ACTIVE and RUNNING! ✅"
    else
        warn "Service started but status is not active yet. Checking logs..."
        journalctl -u sagedral-ml -n 20 --no-pager || true
    fi
else
    warn "System is not booted with systemd as PID 1 (WSL or container environment detected)."
    info "To start SAGEDRAL-ML manually, run: sudo sagedral-ml start"
fi

# 13. Post-install status check
echo ""
info "Post-install status check..."
sleep 2
if command -v sagedral-ml &>/dev/null; then
    echo ""
    echo "=== ML Model Status (offline check) ==="
    "${SAG_CLI}" model info 2>&1 || true
    echo ""
fi

echo ""
echo -e "${GREEN}================================================${NC}"
echo -e "${GREEN}  SAGEDRAL-ML installation completed!${NC}"
echo -e "${GREEN}================================================${NC}"
echo "Supported Python: $(python3 --version) ✅"
echo ""
echo "Start service : systemctl start sagedral-ml"
echo "                (or non-systemd: sudo sagedral-ml start)"
echo "Check status  : sagedral-ml status          -> ML Model Loaded should now be True"
echo "Model details : sagedral-ml model info"
echo "Re-init model : sagedral-ml model init --force"
echo "Web Dashboard : http://localhost:8000"
echo ""
echo -e "${YELLOW}👉 NEXT STEP:${NC} Edit /etc/sagedral/config.toml and set capture.interface to your"
echo "   active Bridged/monitor interface (e.g. eth1), then restart service: systemctl restart sagedral-ml"
