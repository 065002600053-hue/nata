print("---Program Perhitungan Diskonan Pembelanjaan USAKTIF---\n")

nama = input("Masukan Nama : ")
nim = input("Masukan Nim  : ")

# Validasi input Total Belanja agar bernilai positif/valid
try:
    total_belanja = float(input("Masukan Total Belanja anda : "))
    if total_belanja < 0:
        print("!-Masukan total belanja dengan benar-!")
        exit()
except ValueError:
    print("!-Masukan total belanja dengan benar-!")
    exit()

pakai_kupon = input("bayar pakai kupon? y/n : ").strip().lower()

diskon_persen = 0
is_gratis = False

# Pengecekan Pilihan Kupon
if pakai_kupon in ['y', 'yes']:
    kode_kupon = input("Masukan kode kupon : ").strip()
    if kode_kupon == "IKL6309":
        diskon_persen = 100
        is_gratis = True
    else:
        print("!-Maaf kode yang anda pakai salah atau expired-!")
        exit()

elif pakai_kupon in ['n', 'no']:
    # Perhitungan Diskon Berdasarkan Total Belanja
    if total_belanja >= 390000:
        diskon_persen = 80
    elif total_belanja >= 190000:
        diskon_persen = 60
    elif total_belanja >= 90000:
        diskon_persen = 40
    elif total_belanja >= 40000:
        diskon_persen = 20
    else:
        diskon_persen = 0

else:
    # Penanganan jika input pilihan kupon salah
    print("!-Masukan pilihan dengan benar-!")
    exit()

# Menampilkan Pesan Diskon
print()
if diskon_persen > 0:
    print(f"--SELAMAT ANDA MENDAPATKAN DISKON {diskon_persen}%--")
else:
    print("--ANDA TIDAK MENDAPATKAN DISKON--")

# Perhitungan Potongan Harga dan Total Pembayaran
potongan_harga = total_belanja * (diskon_persen / 100)
total_bayar = total_belanja - potongan_harga

# Menampilkan Rincian Belanja
print("\n------------Rincian Belanja ------------")
print(f"{nama} - {nim}")
print(f"Total belanja anda  : Rp.{total_belanja}")
print(f"Potongan harga      : Rp.{int(potongan_harga)}")

if is_gratis:
    print("Total Pembayaran    : GRATIS TIS TIS")
else:
    print(f"Total Pembayaran    : Rp.{int(total_bayar)}")

print("\nTerimakasih sudah belanja :)")
