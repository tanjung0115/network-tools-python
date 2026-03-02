import socket

print("--- Banner Grabber (Informasi Gathering) ---")
print("-" * 50)

# Meminta input target (Port wajib dijadikan integer/angka)
target_ip = input("Masukkan IP/Domain target: ")
target_port = int(input("Masukkan Port target: "))

print("-" * 50)
print(f"[*] Mengetuk target {target_ip} di port {target_port}...")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)

    # Melakukan koneksi ke target
    s.connect((target_ip, target_port))

    # Trik menyapa web server (port 80)
    if target_port == 80:
        sapaan = f"HEAD / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        s.send(sapaan.encode())

    # Menangkap balasan
    banner = s.recv(1024).decode('utf-8', errors='ignore')
        
    if banner:
        print("[+] Identitas server terbongkar!")
        print(">>>" + "=" * 40)
        print(banner.strip())
        print("=" * 40 + "<<<")
    else:
        print("[-] Server tidak memberikan identitas apa pun.")

except socket.timeout:
    print("[x] Timeout: Server terlalu lama merespon.")
except ConnectionRefusedError:
    print(f"[x] Error: Port {target_port} tertutup atau menolak koneksi.")
except Exception as e:
    print(f"[x] Error sistem: {e}")
finally:
    s.close()

print("=" * 50)
print("---- Operasi Selesai ----")
