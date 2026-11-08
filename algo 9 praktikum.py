def kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def hitung_hari(bulan, tahun=0):
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    elif bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    return 0

# Main Program Loop
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

while True:
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))

    # Berhenti jika user memasukkan 0
    if bulan == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break

    # Jika bulan adalah Februari (2), minta input tahun
    if bulan == 2:
        tahun = int(input("masukkan tahun (e.g., 2021): "))
        jumlah_hari = hitung_hari(bulan, tahun)
    else:
        jumlah_hari = hitung_hari(bulan)

    print(f"{jumlah_hari} hari dalam sebulan")
    
