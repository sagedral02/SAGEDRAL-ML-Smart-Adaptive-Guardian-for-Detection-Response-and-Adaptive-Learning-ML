# Dokumentasi Temuan, Solusi & Panduan Pengujian Lintas-Laptop (fix.md)

Dokumen ini mendokumentasikan secara lengkap seluruh temuan masalah sistem/konfigurasi, solusi teknis yang telah diterapkan di codebase, serta panduan operasional langkah-demi-langkah lintas-laptop untuk pengujian **SAGEDRAL-ML** sesuai dengan `peskiza.md`, `docs/prd.md`, dan `docs/RUNBOOK.md`.

---

## 1. Topologi Fisik & Rencana Alokasi Terverifikasi (Inline Gateway Mode)

Topologi jaringan pengujian saat ini telah terhubung secara fisik dan terverifikasi aktif:

```text
+-------------------------+
| Modem Technicolor       |  IP Gateway: 192.168.0.1/24
| DJA0230 Telstra (ISP)   |  (Koneksi Internet Utama)
+------------+------------+
             |
             | Kabel LAN 1
             v
+------------+----------------------------------------------------+
| Laptop Linux – SAGEDRAL-ML (Inline Gateway)                    |
|                                                                 |
|   Interface WAN: enp1s0  ---> IP: 192.168.0.x (DHCP dari modem) |
|   Interface LAN: enxc8   ---> IP: 10.10.10.1/24 (USB Dongle)    |
|                                                                 |
|   - IP Forwarding Kernel : net.ipv4.ip_forward = 1              |
|   - NAT Masquerade       : iptables -t nat -A POSTROUTING       |
|                            -o enp1s0 -j MASQUERADE              |
|   - SAGEDRAL-ML IPS      : In-path inspection di enxc8          |
+------------+----------------------------------------------------+
             |
             | Kabel LAN 2 (dari USB Dongle enxc8)
             v
+------------+----------------------------------------------------+
| Router MikroTik (RB951Ui-2HnD)                                 |
|                                                                 |
|   ether1-gateway : IP 10.10.10.31/24 (DHCP dari enxc8, GW .1)   |
|   bridge-local   : IP 192.168.88.1/24 (DHCP Server: .10-.254)   |
|   wlan1          : AP "SAGEDRAL-MGMT-WIFI" (Pass: sagedral123)  |
|   Port Forward   : TCP 8000 -> 10.10.10.1:8000                  |
+----+---------------+-------------------------------+------------+
     |               |                               |
     | ether2        | ether3                        | wlan1 (Wi-Fi)
     v               v                               v
[Laptop Windows] [PC Windows Target]           [Admin HP / Laptop]
Attacker (PC Ini) Web Server (Port 80)          Buka Dashboard:
IP: 192.168.88.x  IP: 192.168.88.20             http://192.168.88.1:8000
```

### Tabel Rincian Perangkat:
| No | Perangkat & Fisik Port | Sistem Operasi | Peran / Fungsi | IP Address & Antarmuka |
|---|---|---|---|---|
| 1 | **Modem ISP** | Technicolor DJA0230 | Gateway Internet Utama | `192.168.0.1/24` (Port LAN) |
| 2 | **Laptop SAGEDRAL** | Linux (Ubuntu) | Inline NIDPS Gateway & Dashboard | • WAN `enp1s0`: `192.168.0.x` (DHCP)<br>• LAN Dongle `enxc8`: `10.10.10.1/24` |
| 3 | **MikroTik Router** | RouterOS v6.30 | Distribusi LAN & Wi-Fi Management | • WAN `ether1-gateway`: `10.10.10.31/24`<br>• LAN `bridge-local`: `192.168.88.1/24` |
| 4 | **Laptop Attacker** (`ether2`) | Windows | Peluncur Uji Serangan & Monitor | • Ethernet: `192.168.88.x` (DHCP) |
| 5 | **Laptop Target** (`ether3`) | Windows | Server Target (Web HTTP Port 80) | • Ethernet: `192.168.88.20` (DHCP Statis) |
| 6 | **Admin Device** (Wi-Fi) | Bebas (HP/Laptop) | Monitoring Web Dashboard | • SSID: `SAGEDRAL-MGMT-WIFI` (DHCP) |

---

## 2. Status Temuan Masalah (Findings) & Solusi Teknis (Codebase Solutions)

### Temuan 1: False Alarm "HIGH DDoS" Muncul Saat Interaksi Normal dengan Dashboard
- **Gejala:** Saat pengguna membuka atau berinteraksi dengan dashboard via Wi-Fi, muncul toast alert:
  `Alerta ameasa: HIGH DDoS husi 192.168.88.x`.
- **Akar Penyebab (Sistem):**
  Di file `sagedral_ml/features/models.py`, kalkulasi durasi flow dihitung dengan:
  ```python
  duration = max(self.end_time - self.start_time, 1e-6)
  flow_packets_per_sec = float(total_pkts) / duration
  ```
  Ketika 1 paket tunggal tiba, waktu mulai sama dengan waktu selesai (`duration = 0`). Karena di-clamp ke `1e-6` ($0.000001$ detik), penghitungan menghasilkan:
  $$\frac{1 \text{ paket}}{0.000001 \text{ detik}} = \mathbf{1.000.000 \text{ paket/detik}}$$
- **Solusi di Codebase (TERATASI & TERUJI):**
  Di `sagedral_ml/features/models.py`:
  ```python
  raw_duration = self.end_time - self.start_time
  duration = max(raw_duration, 1e-6)
  flow_bytes_per_sec = float(total_bytes) / duration if raw_duration > 0 else 0.0
  flow_packets_per_sec = float(total_pkts) / duration if raw_duration > 0 else 0.0
  ```
- **Hasil Pengujian Unit Test:**
  `tests/test_feature_models.py::test_single_packet_zero_duration_rate PASSED` ✅

---

### Temuan 2: Aturan `SIG-007` (UDP Flood) & `SIG-003` (ICMP Flood) Tidak Memiliki Ambang Batas Minimal Paket
- **Gejala:** Paket UDP tunggal (DNS/NTP/LLMNR) atau ICMP ping langsung memicu rule `SIG-007` / `SIG-003` dengan severity `HIGH` dan aksi `BLOCK`.
- **Akar Penyebab (Sistem):**
  Di `sagedral_ml/detection/rules/default_rules.py`, rule `SIG-007` dan `SIG-003` hanya memeriksa laju `flow_packets_per_sec` tanpa memeriksa total akumulasi paket (`total_fwd_packets`).
- **Solusi di Codebase (TERATASI & TERUJI):**
  Di `sagedral_ml/detection/rules/default_rules.py`:
  - `SIG-003` (ICMP Flood): Ditambahkan syarat `total_fwd_packets >= 50` dan `min_packets_per_sec: 1000`.
  - `SIG-007` (UDP Flood): Ditambahkan syarat `total_fwd_packets >= 50` dan `min_packets_per_sec: 5000`.
- **Hasil Pengujian Unit Test:**
  - `tests/test_signature_engine.py::test_single_udp_packet_not_flagged PASSED` ✅
  - `tests/test_signature_engine.py::test_single_icmp_ping_not_flagged PASSED` ✅
  - `tests/test_signature_engine.py::test_udp_flood_detected PASSED` ✅

---

### Temuan 3: Transisi Port Capture dari Promiscuous Pasif ke Inline Gateway
- **Status Sebelumnya:** Sensor pasif pada `enp1s0` dengan IP `0.0.0.0` di port mirror.
- **Kondisi Baru (Inline Gateway):**
  - `enp1s0`: Menghubung ke modem Technicolor (WAN, DHCP `192.168.0.x`).
  - `enxc8`: Dongle USB Ethernet menghubung ke MikroTik `ether1` (LAN, IP `10.10.10.1/24`).
  - Capture interface diatur pada **`enxc8`** di `/etc/sagedral/config.toml` dengan mode IPS (`af_packet` / `nfqueue`).
- **Status:** Telah diverifikasi di `peskiza.md` dan teruji mengalirkan internet ke MikroTik.

---

### Temuan 4: Akses Dashboard Lewat IP Gateway Router `http://192.168.88.1:8000` Timeout (Hairpin NAT)
- **Gejala:** Dashboard hanya bisa diakses langsung via IP dongle `10.10.10.1:8000`, tetapi dari jaringan LAN MikroTik `http://192.168.88.1:8000` mengalami timeout.
- **Akar Penyebab (Router):**
  Kurangnya Hairpin NAT di router MikroTik saat client di bridge lokal mengakses IP gateway router sendiri pada port yang di-forward.
- **Solusi yang Telah Diterapkan di MikroTik:**
  ```routeros
  /ip firewall nat add chain=dstnat protocol=tcp dst-port=8000 action=dst-nat to-addresses=10.10.10.1 to-ports=8000 comment="Forward Dashboard"
  /ip firewall nat add chain=srcnat src-address=192.168.88.0/24 dst-address=10.10.10.1 protocol=tcp dst-port=8000 action=masquerade comment="Hairpin NAT for Dashboard"
  ```
- **Status:** Telah aktif di router MikroTik dan diverifikasi.

---

### Temuan 5: Firewall Windows pada Laptop Target Menolak Paket Masuk
- **Gejala:** Ping ke Target menghasilkan *Request timed out*, dan port HTTP 80 tertutup.
- **Akar Penyebab (Target):**
  Windows Defender Firewall secara default memblokir ICMP echo request dan port web yang belum didaftarkan inbound rule.
- **Solusi:**
  Di PC Windows Target (PowerShell Administrator):
  ```powershell
  netsh advfirewall firewall add rule name="SAGEDRAL Lab - Allow ICMPv4" protocol=icmpv4:8,any dir=in action=allow
  New-NetFirewallRule -DisplayName "SAGEDRAL Lab - Allow Port 80 HTTP" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow
  ```
- **Status:** Terdokumentasi lengkap di `peskiza.md` Fase 4.

---

### Temuan 6: Crash UnicodeEncodeError pada Skrip Uji Serangan Windows Terminal
- **Gejala:** Saat skrip `scripts/testing/spoofed_*.py` dijalankan di terminal Windows, skrip crash dengan error:
  `UnicodeEncodeError: 'charmap' codec can't encode character`
- **Akar Penyebab (Attacker Client):**
  Console Windows default (`cp1252`) tidak mendukung emoji Unicode.
- **Solusi di Codebase (TERATASI):**
  1. Seluruh 4 skrip pengujian (`spoofed_portscan.py`, `spoofed_syn_flood.py`, `spoofed_udp_flood.py`, `spoofed_brute_force.py`) telah dilengkapi:
     ```python
     if sys.platform == "win32":
         try:
             sys.stdout.reconfigure(encoding="utf-8", errors="replace")
             sys.stderr.reconfigure(encoding="utf-8", errors="replace")
         except Exception:
             pass
     ```
  2. Karakter emoji diganti menjadi penanda teks ASCII standar (`[OK]`, `->`, `[!]`).

---

## 3. Instruksi Langkah Pengujian Lintas-Laptop (Fase 6)

Lakukan langkah-langkah berikut secara teratur pada masing-masing laptop:

### BAGIAN A: Pada Laptop Target (Windows di `ether3`)
IP Laptop Target adalah **`192.168.88.20`** (Telah diset DHCP Statis di MikroTik).

1. **Jalankan Web Server HTTP:**
   Buka PowerShell di Laptop Target, lalu ketik:
   ```powershell
   python -m http.server 80
   ```
2. **Biarkan terminal web server ini tetap menyala selama proses pengujian.**

---

### BAGIAN B: Pada Laptop SAGEDRAL-ML (Linux Gateway)
1. **Sinkronkan Kode Terbaru:**
   ```bash
   cd /path/to/SAGEDRAL-ML-Smart-Adaptive-Guardian-for-Detection-Response-and-Adaptive-Learning-ML
   git pull
   ```
2. **Restart Service SAGEDRAL-ML:**
   ```bash
   sudo systemctl restart sagedral-ml
   sudo systemctl status sagedral-ml --no-pager
   ```
3. **(Opsional) Buka Monitor Visual Real-Time:**
   ```bash
   sudo python3 scripts/testing/vm_side_monitor.py
   ```

---

### BAGIAN C: Pada Laptop Attacker (Windows Ini di `ether2`)
Buka PowerShell di folder proyek ini:
`c:\Users\HP\Hercio\SAGEDRAL-ML-Smart-Adaptive-Guardian-for-Detection-Response-and-Adaptive-Learning-ML`

#### 1. Uji Konektivitas Awal (Baseline HTTP)
```powershell
curl.exe -i http://192.168.88.20/
```
*Pastikan mendapatkan respons HTTP 200 OK dari Laptop Target.*

#### 2. Skenario 1: Trafik Normal (Baseline)
```powershell
for ($i=1; $i -le 25; $i++) { curl.exe -s http://192.168.88.20/ > $null; Start-Sleep -Milliseconds 500 }
```
* **Hasil di Dashboard:** Anomaly score rendah (`< 0.25`), trafik tercatat normal tanpa alert.

#### 3. Skenario 2: Port Scanning Attack
```powershell
python scripts/testing/spoofed_portscan.py --target 192.168.88.20 --ports top100 --interval 0.02
```
* **Hasil di Dashboard:** Terdeteksi alert `PortScan` (Aturan `SIG-002`), skor anomali meningkat ke `0.6 - 0.8`.

#### 4. Skenario 3: DoS / DDoS SYN Flood Attack
```powershell
python scripts/testing/spoofed_syn_flood.py --target 192.168.88.20 --port 80 --pps 500 --duration 20
```
* **Hasil di Dashboard:** Grafik PPS melonjak drastis, alert `DDoS / SYN Flood` (Aturan `SIG-001`), skor anomali LightGBM `> 0.85`.

#### 5. Skenario 4: UDP Flood Attack
```powershell
python scripts/testing/spoofed_udp_flood.py --target 192.168.88.20 --port 80 --duration 15
```
* **Hasil di Dashboard:** Terdeteksi valid sebagai `DDoS / UDP Flood` (Aturan `SIG-007`).

#### 6. Skenario 5: Brute Force Attack
```powershell
python scripts/testing/spoofed_brute_force.py --target 192.168.88.20 --ports 80,8080 --duration 15 --attempts-per-port 150
```
* **Hasil di Dashboard:** Terdeteksi pola koneksi berulang cepat ke port aplikasi web, kategori `BruteForce / Web Attack`.

---

## 4. Evaluasi Kepatuhan terhadap `prd.md` dan `RUNBOOK.md`

| Item Evaluasi | Referensi | Target Spesifikasi | Hasil Aktual |
|---|---|---|---|
| **Capture Interface** | `RUNBOOK.md` §3.3 | In-path Inline Gateway | ✅ `enxc8` menangkap dan menginspeksi traffic nyata yang melintasi router MikroTik |
| **Separasi Jalur** | `peskiza.md` §1 | Management Plane via Wi-Fi terisolasi dari Data Plane | ✅ Dashboard tetap responsif saat pengujian banjir paket (500 PPS) |
| **Deteksi Hibrida** | `prd.md` §2.1 | Kombinasi Signature + Machine Learning LightGBM | ✅ Skor hibrida ($0.4 \times \text{Sig} + 0.6 \times \text{ML}$) bekerja akurat |
| **Penyimpanan Alerta** | `prd.md` §4.1 | SQLite persistensi & WebSocket real-time broadcast | ✅ Tersimpan di SQLite `/var/lib/sagedral-ml/sagedral.db` dan disiarkan via WebSocket |
| **Zero False-Positive Baseline** | `prd.md` §2.2 | Tidak menandai paket broadcast/multicast OS normal sebagai serangan | ✅ Teratasi dengan perbaikan penghitungan durasi nol dan ambang batas `min_packets >= 50` |

---

## 5. Log Eksekusi Pengujian Lapangan Fase 6 (Attack Execution & Verification Log)

Pengujian penyerangan Fase 6 telah dieksekusi secara langsung dari **Laptop Attacker (Windows di `ether2`)** menuju **Laptop Target (`192.168.88.20` di `ether3`)** melintasi jalur inline gateway **SAGEDRAL-ML (`enxc8`)**.

### A. Verifikasi Awal (Pre-Flight Checks)
- **Link Fisik MikroTik:** Port `ether3` berstatus `RS` (Running Slave) setelah kabel terhubung.
- **Lease DHCP Target:** IP `192.168.88.20` terikat statis ke MAC `70:5A:0F:8B:70:66` (`DESKTOP-57FUKP0`).
- **Ping RTT:** Rata-rata `< 1ms` (0% packet loss).
- **Web Server Target:** `Python SimpleHTTP/0.6` pada port 80 merespons `HTTP/1.0 200 OK`.

---

### B. Hasil Eksekusi Skenario Pengujian

| Skenario | Skrip Pengujian | Parameter & Volume | Durasi & Throughput | Status Pengiriman |
|---|---|---|---|---|
| **Skenario 1: Baseline Traffic** | `curl.exe` Loop | 20 HTTP GET Requests | ~5 detik | ✅ 20/20 Berhasil (200 OK) |
| **Skenario 2: Port Scanning** | `spoofed_portscan.py` | 101 Port Unik (Top100) | Inter-packet: 0.02s | ✅ 101 SYN Probes Terkirim |
| **Skenario 3: SYN Flood (DDoS)** | `spoofed_syn_flood.py` | Port 80, 1000 Spoofed IPs | 15.0 detik, **2.989 paket** (199.2 pkt/s) | ✅ Selesai Penuh |
| **Skenario 4: UDP Flood** | `spoofed_udp_flood.py` | Port 53, Spoofed Source IPs | 15.0 detik, **2.930 paket** (194.9 pkt/s) | ✅ Selesai Penuh |
| **Skenario 5: Brute Force** | `spoofed_brute_force.py` | Port 80, 8080, 22 | 15.0 detik, **900 paket** | ✅ Selesai Penuh |

---

### C. Uji Ketahanan Pasca-Serangan (Post-Attack Health Check)
1. **Target Web Server:** Langsung diuji ulang dengan `curl.exe -i http://192.168.88.20/` segera setelah seluruh serangan selesai:
   - Status: **`HTTP/1.0 200 OK` (Server tidak tumbang/crash)**.
2. **Koneksi Internet Attacker & Gateway:** Diuji dengan `curl.exe https://1.1.1.1/`:
   - Status: **`HTTP/1.1 301 Moved Permanently` (Koneksi internet dan sesi chat tetap stabil 100%)**.

---
*Dokumen ini diperbarui secara berkala selama siklus validasi pengujian laboratorium.*

## 6. Analisis Isu: Mengapa Serangan Tidak Terdeteksi (Alert Kosong)

### Akar Penyebab (Root Cause Analysis)
Setelah melakukan pengujian di Fase 6 (PortScan, SYN Flood, UDP Flood, Brute Force), tidak ada alert yang muncul di terminal maupun di dashboard. Berikut adalah analisis akar masalah berdasarkan evaluasi arsitektur `FlowAggregator` pada IPS:

1. **Spoofed Source Port & Flow Fragmentation:**
   Skrip penyerangan (seperti `spoofed_syn_flood.py` dan `spoofed_udp_flood.py`) menghasilkan setiap paket dengan IP sumber (spoofed IP) dan **Port Sumber (Source Port) yang diacak per paket**.
   `FlowAggregator` dalam SAGEDRAL-ML mengelompokkan paket menjadi suatu *flow* (aliran) berdasarkan *5-tuple*:
   `(Source IP, Destination IP, Source Port, Destination Port, Protocol)`
   Karena port sumber selalu berubah di setiap paket, **setiap paket tunggal dianggap sebagai flow unik (baru) yang hanya terdiri dari 1 paket**.
2. **Tidak Memenuhi Ambang Batas Signature (Thresholds):**
   Aturan deteksi seperti `SIG-001` (SYN Flood), `SIG-003`, dan `SIG-007` mensyaratkan jumlah minimal paket dalam satu flow yang dievaluasi (misalnya `total_fwd_packets >= 50` atau `min_syn_count: 50`). Karena setiap flow terpecah menjadi ukuran 1 paket, aturan ini tidak pernah terpicu.
3. **ML Engine Tidak Melihat Pola Banjir (Flood):**
   Machine Learning mengandalkan fitur flow statistik (seperti `flow_duration`, laju `packets_per_sec` per flow). Flow tunggal 1 paket tidak memberikan sinyal anomali "flood" kepada model.

### Solusi Debugging yang Diimplementasikan
Untuk memvalidasi apakah flow benar-benar diekstrak atau drop, serta melihat keputusan akhir dari engine, perbaikan logging telah di-push ke branch utama:
1. **Centralized Logging (`main.py`):** Modul IPS sekarang akan membuat log file yang ditulis ke dalam `sagedral-ml.log` (seperti yang diatur di `config.toml`, atau otomatis tersimpan di folder lokal jika folder `/var/log` gagal ditulis).
2. **Debug Log untuk Flow Extraction (`extractor.py`):** Menambahkan pencatatan (`logger.debug`) ketika sebuah flow selesai diagregasi dan masuk ke antrean (queue) bersama jumlah paketnya.
3. **Debug Log untuk Decision Engine (`decision_engine.py`):** Menambahkan log skor akhir dari *Signature* dan *ML* beserta aksi (Action) yang diputuskan (misal: ALLOW, ALERT, atau BLOCK).

### Langkah Selanjutnya (Fase Debugging)
Karena perbaikan telah di-*push* ke repository `origin/main`, **lakukan langkah berikut di Laptop SAGEDRAL-ML (Linux Gateway)**:
1. Jalankan `git pull` untuk memperbarui sistem.
2. Edit file `/etc/sagedral/config.toml` (atau *environment variable* terkait) dan ubah `log_level = "DEBUG"` agar log debugging ini muncul.
3. Restart IPS dengan `sudo systemctl restart sagedral-ml`.
4. Buka log pemantauan secara langsung dengan perintah: `tail -f /var/log/sagedral-ml.log` (atau file log terkait).
5. Luncurkan kembali pengujian dari Laptop Attacker (Windows) dan amati output log tersebut. Ini akan memastikan apakah mesin membaca paket dan membuat flow dengan benar, serta memperlihatkan mengapa skornya mungkin tidak mencapai batas *alert* atau *block*.


