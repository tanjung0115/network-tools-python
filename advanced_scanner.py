import socket
import sys
from datetime import datetime

# Target IP (Bisa diganti nanti)
target = "127.0.0.1" 

# Fungsi untuk mengambil Banner (Versi Aplikasi)
def grab_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        
        # --- TAMBAHAN BARU ---
        # Jika port adalah layanan Web (80, 8080, 9000), kita harus kirim "pancingan"
        # Kirim request HTTP GET sederhana
        pancingan = b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        s.send(pancingan)
        # ---------------------

        banner = s.recv(1024) # Baca respon server
        return banner.decode('utf-8', errors='ignore').strip() # decode biar jadi teks
    except Exception as e:
        return f"Tidak bisa ambil banner ({e})"
    finally:
        s.close()
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            # Jika port terbuka, ambil bannernya!
            banner = grab_banner(target, port)
            print(f"[+] Port {port} TERBUKA : {banner}")
        s.close()
    except KeyboardInterrupt:
        print("\nKeluar program...")
        sys.exit()
    except socket.gaierror:
        print("Hostname tidak bisa di-resolve.")
        sys.exit()
    except socket.error:
        print("Server tidak merespon.")
        sys.exit()

# Program Utama
print("-" * 50)
print(f"Scanning Target: {target}")
print("Waktu mulai: " + str(datetime.now()))
print("-" * 50)

# Scan port penting saja (SSH, HTTP, HTTPS, FTP, Telnet)
ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 3306, 8080, 9000]

for port in ports_to_scan:
    scan_port(port)

print("-" * 50)
print("Scanning Selesai.")
