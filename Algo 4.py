# Input tiga panjang sisi
a = float(input("Masukkan sisi 1: "))
b = float(input("Masukkan sisi 2: "))
c = float(input("Masukkan sisi 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki")
    else:
        print("Segitiga sembarang")
else:
    print("Tidak dapat membentuk segitiga")
