def hitung_tiket_kebun_binatang():
    total_harga = 0.0

    # Perulangan untuk menginput umur pengunjung
    while True:
        input_umur = input("masukkan umur: ")
        
        # Jika user langsung menekan Enter (kosong), loop berhenti
        if input_umur.strip() == "":
            break
            
        umur = int(input_umur)
        
        # Penentuan harga tiket berdasarkan ketentuan umur
        if umur <= 2:
            harga = 0.0
            print("Gratis")
        elif 3 <= umur <= 12:
            harga = 14.0
            print(f"Harga ${harga:.2f}")
        elif umur >= 65:
            harga = 18.0
            print(f"Harga ${harga:.2f}")
        else:  # Umur selain kategori di atas (13 - 64 tahun)
            harga = 23.0
            print(f"Harga ${harga:.2f}")
            
        # Akumulasi total pembayaran
        total_harga += harga
        print(f"Running total: {total_harga:.2f}")

    # Proses pembayaran dan pengembalian uang
    if total_harga > 0:
        uang_dibayar = float(input("masukkan jumlah uang: "))
        kembalian = uang_dibayar - total_harga
        print(f"Running kembalian: {kembalian:.2f}")
    else:
        print("Total pembayaran $0.00. Tidak ada kembalian.")

# Jalankan program
if __name__ == "__main__":
    hitung_tiket_kebun_binatang()
