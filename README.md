#  Super Port Scanner (Python CLI Tool)

###  Author:Mija Tanjung
**Bootcamp Cybersecurity - Week 1: The Toolmaker**

---

##  Deskripsi Singkat
**Super Port Scanner** adalah alat pemindai jaringan (Network Scanner) berbasis Command Line Interface (CLI) yang dibangun menggunakan Python murni. 

Alat ini dibuat untuk memahami cara kerja pemindaian jaringan (*Reconnaissance*) di dunia Cybersecurity. Berbeda dengan scanner tradisional yang lambat, tool ini telah dioptimalkan dengan algoritma **Multithreading** untuk memindai ribuan port dalam hitungan detik.

##  Fitur Utama (Key Features)
-  **Asynchronous/Multithreading:** Menggunakan `concurrent.futures` dengan 50 *workers* untuk memindai port (1-1024) secara bersamaan (Sangat Cepat!).
-  **Dynamic Target Parsing:** Mendukung input target dinamis dari terminal (mendukung IP Address maupun resolusi Hostname/Domain).
-  **Banner Grabbing:** Tidak hanya mendeteksi port yang terbuka, tapi secara aktif mengirim *HTTP payload* untuk mengidentifikasi layanan (service) yang berjalan di baliknya.
-  **Pro UI/UX:** Dilengkapi dengan ASCII Art, ANSI Color Codes (Warna terminal), dan output log yang bersih.
-  **Graceful Error Handling:** Tahan terhadap *crash*. Mampu menangani *Timeout*, koneksi terputus, dan *Keyboard Interrupt* (Ctrl+C) dengan aman.

##  Prasyarat (Prerequisites)
- Python 3.x
- Tidak memerlukan *library* eksternal (Hanya menggunakan modul bawaan Python: `socket`, `sys`, `datetime`, `concurrent.futures`).

##  Cara Penggunaan (Usage)

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/tanjung0115/Cybersecurity-Portfolio.git](https://github.com/tanjung0115/Cybersecurity-Portfolio.git)
   cd Cybersecurity-Portfolio
