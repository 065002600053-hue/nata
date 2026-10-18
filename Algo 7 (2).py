while True:
    bulan = int(input("Bulan (1-12): "))
    tahun = int(input("Tahun: "))
    
    if bulan in [1, 3, 5, 7, 8, 10, 12]: hari = 31
    elif bulan in [4, 6, 9, 11]: hari = 30
    elif bulan == 2:
        hari = 29 if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0) else 28
    else:
        print("Bulan tidak valid!")
        continue
        
    print(f"Jumlah hari: {hari}")
    if input("Lagi? (y/t): ") != 'y': break
