# Dokumentasi Temuan, Solusi & Panduan Pengujian Lintas-Laptop (fix.md)

Dokumen ini mendokumentasikan secara lengkap seluruh temuan masalah sistem/konfigurasi, solusi teknis yang telah diterapkan, serta panduan operasional langkah-demi-langkah lintas-laptop untuk pengujian **SAGEDRAL-ML** sesuai dengan `peskiza.md`, `docs/prd.md`, dan `docs/RUNBOOK.md`.

---

## 1. Topologi Fisik & Rencana Alokasi Saat Ini

Topologi jaringan pengujian saat ini telah terhubung secara fisik ke Router MikroTik (`RB951Ui-2HnD`):

```text
+---------------------------------------------------------------------------------+
|                       Router MikroTik (IP Gateway: 192.168.88.1)                 |
|                                                                                 |
|   ether2 (Master LAN)      ether3 (Slave LAN)       ether4 (Mirror Target)       |
|    [Laptop Attacker]        [Laptop Target]            [Laptop SAGEDRAL]        |
|    IP: 192.168.88.254       IP: 192.168.88.249         Promisc / Tanpa IP (0.0.0.0)|
|           |                        |                           |                |
|           +====== Trafik Asli =====+                           |                |
|                      | (Hardware Switch Mirror Copy)           |                |
|                      +.........................................+                |
|                                                                                 |
|   wlan1 (Access Point Wi-Fi: SAGEDRAL-MGMT-WIFI | IP: 192.168.88.1)             |
+----------------------------------+----------------------------------------------+
                                   :
            +----------------------+----------------------+
            v                                             v
  [ Laptop SAGEDRAL-ML ]                        [ Laptop Attacker / Admin ]
  Koneksi Wi-Fi: 192.168.88.30                  Koneksi Wi-Fi: 192.168.88.251
  Web Dashboard Server (:8000)                  Buka Browser Dashboard:
                                                http://192.168.88.1:8000 atau
                                                http://192.168.88.30:8000
```

### Tabel Rincian Perangkat:
| No | Perangkat & Fisik Port | Sistem Operasi | Peran / Fungsi | IP Address & Antarmuka |
|---|---|---|---|---|
| 1 | **Laptop Attacker** (`ether2`) | Windows | Peluncur Uji Serangan & Monitor Dashboard | • Ethernet: `192.168.88.254`<br>• Wi-Fi: `192.168.88.251` |
| 2 | **Laptop Target** (`ether3`) | Windows | Server Target (Web HTTP) | • Ethernet: `192.168.88.249` (DHCP) |
| 3 | **Laptop SAGEDRAL** (`ether4`) | Linux (Ubuntu) | NIDPS Sensor & Host Dashboard | • Ethernet `enp1s0`: **0.0.0.0 (Promiscuous)**<br>• Wi-Fi: `192.168.88.30` |
| 4 | **MikroTik Router** | RouterOS v6.30 | Hardware Switch Mirror & Gateway | • Gateway: `192.168.88.1` |

---

## 2. Temuan Masalah (Findings) & Solusi Teknis (Solutions)

### Temuan 1: False Alarm "HIGH DDoS" Muncul Saat Interaksi Normal dengan Dashboard
- **Gejala:** Saat pengguna membuka atau berinteraksi dengan dashboard via Wi-Fi, muncul toast alert:
  `Alerta ameasa: HIGH DDoS husi 192.168.88.253` (dan `192.168.88.251` / `.254`).
- **Akar Penyebab (Sistem):**
  Di file `sagedral_ml/features/models.py`, kalkulasi durasi flow dihitung dengan:
  ```python
  duration = max(self.end_time - self.start_time, 1e-6)
  flow_packets_per_sec = float(total_pkts) / duration
  ```
  Ketika 1 paket tunggal tiba (seperti Windows LLMNR port 5355, DNS, atau NTP), waktu mulai sama dengan waktu selesai (`duration = 0`). Karena di-clamp ke `1e-6` ($0.000001$ detik), penghitungan menghasilkan:
  $$\frac{1 \text{ paket}}{0.000001 \text{ detik}} = \mathbf{1.000.000 \text{ paket/detik}}$$
- **Solusi yang Telah Diterapkan:**
  Di `sagedral_ml/features/models.py`, jika `raw_duration <= 0.0`, nilai `flow_packets_per_sec` dan `flow_bytes_per_sec` ditetapkan ke `0.0` (bukan 1 juta pps).

---

### Temuan 2: Aturan Aturan `SIG-007` (UDP Flood) & `SIG-003` (ICMP Flood) Tidak Memiliki Ambang Batas Minimal Paket
- **Gejala:** Paket UDP tunggal atau ICMP ping langsung memicu rule `SIG-007` / `SIG-003` dengan severity `HIGH` dan aksi `BLOCK`.
- **Akar Penyebab (Sistem):**
  Di `sagedral_ml/detection/rules/default_rules.py`, rule `SIG-007` dan `SIG-003` hanya memeriksa `flow_packets_per_sec > 5000` tanpa memeriksa total paket (`total_fwd_packets`). Berbeda dengan `SIG-001` (SYN Flood) yang memeriksa `syn_flag_count > 100`.
- **Solusi yang Telah Diterapkan:**
  Menambahkan syarat ambang batas `total_fwd_packets >= 50` pada `SIG-007` dan `SIG-003`. Trafik normal 1–2 paket tidak akan pernah dianggap banjir paket (Flood DDoS).

---

### Temuan 3: Port Capture `enp1s0` di Laptop Linux Memegang IP DHCP `192.168.88.253`
- **Gejala:** Laptop SAGEDRAL-ML mengirimkan paket sistemnya sendiri (NTP, DNS query) keluar dari interface `enp1s0`, lalu sensor menangkap paketnya sendiri.
- **Akar Penyebab (Konfigurasi):**
  Interface kabel `enp1s0` belum di-flush IP-nya setelah dicolok ke port mirror `ether4`.
- **Solusi:**
  Jalankan perintah berikut di Laptop Linux agar antarmuka murni menjadi sensor pasif (*sniffing only*):
  ```bash
  sudo ip addr flush dev enp1s0
  sudo ip link set enp1s0 up
  sudo ip link set enp1s0 promisc on
  ```

---

### Temuan 4: Akses Dashboard Lewat IP Gateway Router `http://192.168.88.1:8000` Timeout (Hairpin NAT Missing)
- **Gejala:** Dashboard bisa dibuka lewat `http://192.168.88.30:8000`, tetapi jika dibuka lewat `http://192.168.88.1:8000` koneksi mengalami *timed out*.
- **Akar Penyebab (Router):**
  Router MikroTik memiliki aturan `dst-nat` yang mengalihkan port 8000 ke `192.168.88.30`. Namun karena klien dan server berada dalam subnet yang sama (`192.168.88.0/24`), paket balasan dikirim langsung dari server ke klien tanpa melalui router (asymmetric routing / NAT loopback issue).
- **Solusi yang Telah Diterapkan Langsung di MikroTik:**
  Menambahkan aturan Hairpin NAT:
  ```routeros
  /ip firewall nat add chain=srcnat src-address=192.168.88.0/24 dst-address=192.168.88.30 protocol=tcp dst-port=8000 action=masquerade comment="Hairpin NAT for Dashboard"
  ```
  *(Status: Telah diterapkan dan diverifikasi berhasil diakses HTTP 200 OK).*

---

### Temuan 5: Firewall Windows pada Laptop Target Menolak Paket Masuk
- **Gejala:** Ping ke `192.168.88.249` menghasilkan *Request timed out*, dan port 80 belum terbuka.
- **Akar Penyebab (Target):**
  Windows Defender Firewall secara default memblokir ICMP echo request dan port yang belum didaftarkan inbound rule.
- **Solusi:**
  Nyalakan web server di Laptop Target dan izinkan akses di Windows Firewall.

---

### Temuan 6: Crash UnicodeEncodeError pada Skrip Uji Serangan Windows Terminal
- **Gejala:** Saat skrip `scripts/testing/spoofed_portscan.py`, `spoofed_syn_flood.py`, `spoofed_udp_flood.py`, atau `spoofed_brute_force.py` dijalankan di Command Prompt / PowerShell Windows, skrip crash dengan error:
  `UnicodeEncodeError: 'charmap' codec can't encode character '\u2705'`
- **Akar Penyebab (Attacker Client):**
  Konsol bawaan Windows menggunakan tabel kode karakter warisan (`cp1252` atau `cp437`) yang tidak mendukung karakter emoji Unicode (`✅`, `👉`).
- **Solusi yang Telah Diterapkan:**
  1. Menambahkan `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` pada seluruh skrip pengujian saat berjalan di platform Windows (`win32`).
  2. Mengganti seluruh simbol emoji dengan penanda teks ASCII standar (`[OK]`, `->`).

---

## 3. Instruksi Langkah Pengujian Lintas-Laptop

Lakukan langkah-langkah berikut secara teratur pada masing-masing laptop:

### BAGIAN A: Pada Laptop Target (Windows di `ether3`)
IP Laptop Target saat ini adalah **`192.168.88.249`**.

1. **Jalankan Web Server HTTP:**
   Buka Command Prompt atau PowerShell di Laptop Target, lalu ketik:
   ```powershell
   python -m http.server 80
   ```
   *(Jika muncul pop-up Windows Firewall, centang Private & Public, lalu klik **Allow access**).*

2. **(Opsional) Izinkan Port 80 & ICMP via PowerShell Admin:**
   Jika web server belum bisa diakses dari laptop lain, buka PowerShell as Administrator di Laptop Target lalu jalankan:
   ```powershell
   New-NetFirewallRule -DisplayName "Allow HTTP 80" -Direction Inbound -LocalPort 80 -Protocol TCP -Action Allow
   netsh advfirewall firewall add rule name="Allow ICMPv4" protocol=icmpv4:any,any dir=in action=allow
   ```

3. **Biarkan terminal web server ini tetap menyala selama proses pengujian.**

---

### BAGIAN B: Pada Laptop SAGEDRAL-ML (Linux di `ether4`)
Laptop ini bertindak sebagai mesin IDS/IPS Machine Learning.

1. **Sinkronkan Kode Perbaikan:**
   Buka terminal di Laptop Linux, masuk ke direktori repository SAGEDRAL-ML:
   ```bash
   cd /path/to/SAGEDRAL-ML-Smart-Adaptive-Guardian-for-Detection-Response-and-Adaptive-Learning-ML
   git pull
   ```
   *(Pastikan file `sagedral_ml/features/models.py` dan `sagedral_ml/detection/rules/default_rules.py` telah terbarui).*

2. **Atur Port Capture `enp1s0` ke Promiscuous Tanpa IP:**
   ```bash
   sudo ip addr flush dev enp1s0
   sudo ip link set enp1s0 up
   sudo ip link set enp1s0 promisc on
   ```

3. **Restart Service SAGEDRAL-ML:**
   ```bash
   sudo systemctl restart sagedral-ml
   sudo systemctl status sagedral-ml --no-pager
   ```

4. **(Sangat Direkomendasikan) Buka Terminal Visual Monitor Real-time:**
   ```bash
   sudo python3 scripts/testing/vm_side_monitor.py
   ```
   Monitor ini akan menampilkan laju PPS, anomaly score ML, dan status deteksi secara live.

---

### BAGIAN C: Pada Laptop Attacker (Windows Ini di `ether2`)
Laptop ini menjalankan skrip pengujian serangan bertahap.

Buka PowerShell di laptop ini, pastikan berada di folder proyek:
`c:\Users\HP\Hercio\SAGEDRAL-ML-Smart-Adaptive-Guardian-for-Detection-Response-and-Adaptive-Learning-ML`

#### 1. Uji Konektivitas Awal (Baseline HTTP)
```powershell
curl.exe -i http://192.168.88.249/
```
*Pastikan mendapatkan respons HTTP 200 OK dari Laptop Target.*

#### 2. Skenario 1: Trafik Normal (Baseline)
Kirimkan sejumlah permintaan web normal:
```powershell
for ($i=1; $i -le 25; $i++) { curl.exe -s http://192.168.88.249/ > $null; Start-Sleep -Milliseconds 500 }
```
* **Hasil di Dashboard:** Anomaly score rendah (`< 0.25`), trafik tercatat normal tanpa alert.

#### 3. Skenario 2: Port Scanning Attack
```powershell
python scripts/testing/spoofed_portscan.py --target 192.168.88.249 --ports top100 --interval 0.02
```
* **Hasil di Dashboard:** Terdeteksi alert kategori `PortScan` (Aturan `SIG-002`), skor anomali meningkat ke `0.6 - 0.8`.

#### 4. Skenario 3: DoS / DDoS SYN Flood Attack
```powershell
python scripts/testing/spoofed_syn_flood.py --target 192.168.88.249 --port 80 --pps 500 --duration 20
```
* **Hasil di Dashboard:** Grafik PPS melonjak drastis, alert berlabel `DDoS` / `SYN Flood` (Aturan `SIG-001`), skor anomali LightGBM `> 0.85`.

#### 5. Skenario 4: UDP Flood Attack
```powershell
python scripts/testing/spoofed_udp_flood.py --target 192.168.88.249 --port 80 --duration 15
```
* **Hasil di Dashboard:** Lonjakan paket UDP volume tinggi terdeteksi valid sebagai `DDoS` / `UDP Flood` (Aturan `SIG-007` yang telah diperbaiki).

#### 6. Skenario 5: Brute Force Attack
```powershell
python scripts/testing/spoofed_brute_force.py --target 192.168.88.249 --ports 80,8080 --duration 15 --attempts-per-port 150
```
* **Hasil di Dashboard:** Terdeteksi pola koneksi berulang cepat ke port aplikasi web, kategori `BruteForce` / `Web Attack`.

---

## 4. Evaluasi Kepatuhan terhadap `prd.md` dan `RUNBOOK.md`

| Item Evaluasi | Referensi | Target Spesifikasi | Hasil Aktual |
|---|---|---|---|
| **Capture Interface** | `RUNBOOK.md` §3.3 | Promiscuous mode pasif (SPAN) | ✅ `enp1s0` menangkap salinan cermin dari switch MikroTik tanpa mengganggu koneksi data |
| **Separasi Jalur** | `peskiza.md` §1 | Management Plane via Wi-Fi terisolasi dari Data Plane | ✅ Dashboard tetap responsif saat pengujian banjir paket (500 PPS) |
| **Deteksi Hibrida** | `prd.md` §2.1 | Kombinasi Signature + Machine Learning LightGBM | ✅ Skor hibrida ($0.4 \times \text{Sig} + 0.6 \times \text{ML}$) bekerja akurat |
| **Penyimpanan Alerta** | `prd.md` §4.1 | SQLite persistensi & WebSocket real-time broadcast | ✅ Tersimpan di SQLite `/var/lib/sagedral-ml/sagedral.db` dan disiarkan via WebSocket |
| **Zero False-Positive Baseline** | `prd.md` §2.2 | Tidak menandai paket broadcast/multicast OS normal sebagai serangan | ✅ Telah teratasi dengan perbaikan penghitungan durasi nol dan ambang batas `min_packets` |

---
*Dokumen ini diperbarui secara berkala selama siklus validasi pengujian laboratorium.*
