import requests

print("Fuzzer Direktori & Ekstensi Sederhana")
print("-" * 50)

# 1. Meminta input dari pengguna
url_dasar = input("Masukkan URL dasar (contoh: http://127.0.0.1:8080/config.): ")
nama_file_wordlist = input("Masukkan nama file wordlist (contoh: wordlist.txt): ")

print("-" * 50)

try:
    # 2. Membaca isi file teks (wordlist)
    with open(nama_file_wordlist, "r") as file:
        daftar_tebakan = file.read().splitlines()
        
    print(f" Berhasil memuat {len(daftar_tebakan)} kata dari file {nama_file_wordlist}.")
    print(" Memulai proses pemindaian (fuzzing)...\n")
    
    # 3. Proses pengiriman HTTP Request (Looping)
    for kata in daftar_tebakan:
        if kata == "":  # Abaikan jika ada baris kosong di dalam file
            continue
            
        # Menggabungkan URL dasar dengan kata dari wordlist
        url_lengkap = url_dasar + kata
        
        try:
            # Mengirim HTTP GET request
            respon = requests.get(url_lengkap)
            
            # Memeriksa HTTP Status Code
            if respon.status_code == 200:
                print(f" Ditemukan (200 OK) : {url_lengkap}")
            else:
                print(f" Gagal ({respon.status_code})     : {url_lengkap}")
                
        except requests.exceptions.RequestException:
            print(f"[x] Error: Tidak dapat terhubung ke server. Pemindaian dihentikan.")
            break # Menghentikan proses jika server tidak bisa dihubungi
            
except FileNotFoundError:
    print(f" Error: File '{nama_file_wordlist}' tidak ditemukan di dalam folder ini!")

print("-" * 50)
print("--- Proses Selesai ---")
