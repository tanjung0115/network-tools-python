import socket
import sys
from datetime import datetime
import concurrent.futures  # INI MODUL SIHIRNYA (Untuk Multithreading)

# --- WARNA (ANSI CODES) ---
HIJAU = '\033[92m'
MERAH = '\033[91m'
KUNING = '\033[93m'
BIRU = '\033[94m'
RESET = '\033[0m'

def print_banner():
    print(BIRU + """
    ========================================
      SUPER PORT SCANNER v3.0 (TURBO) 
           Code by: Tanjung0115
    ========================================
    """ + RESET)

def grab_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        pancingan = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        s.send(pancingan)
        banner = s.recv(1024)
        return banner.decode('utf-8', errors='ignore').strip()
    except:
        return "Tidak ada banner"
    finally:
        s.close()

# Fungsi ini yang akan dikerjakan oleh para "Kloning"
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Waktu tunggu maksimal setengah detik
        result = s.connect_ex((target, port))
        
        if result == 0:
            info = grab_banner(target, port)
            print(f"{HIJAU}[+] Port {port} OPEN : {info}{RESET}")
        s.close()
    except:
        pass # Jika error (misal koneksi putus), biarkan saja, jangan matikan program

# --- PROGRAM UTAMA ---
print_banner()

if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print(f"{MERAH}[!] Hostname tidak ditemukan!{RESET}")
        sys.exit()
else:
    print(f"{KUNING}[?] Cara pakai: python3 advanced_scanner.py <TARGET IP>{RESET}")
    sys.exit()

print("-" * 50)
print(f" Target    : {target}")
print(f" Mulai     : {datetime.now()}")
print("-" * 50)

# KITA SCAN DARI PORT 1 SAMPAI 1024
ports = range(1, 1025) 

try:
    # --- PROSES MULTITHREADING DIMULAI ---
    # Kita membuat 50 Kloning (max_workers=50) untuk bekerja bersamaan
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        # Menyebarkan tugas (mengecek port) ke para pekerja
        for port in ports:
            executor.submit(scan_port, target, port)

except KeyboardInterrupt:
    print(f"\n{MERAH}[!] Dibatalkan oleh user.{RESET}")
    sys.exit()

print("-" * 50)
print(f"🏁 Selesai   : {datetime.now()}")
print(f"{BIRU}Scanning Selesai.{RESET}")
