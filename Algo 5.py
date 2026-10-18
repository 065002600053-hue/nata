#program ini mengubah suhu dari celcius ke fahrenheit atau sebaliknya
print("ketik F untuk mengubah dari fahrenheit ke celcius")
print("ketik C mengubah dari celcius ke fahrenheit")

pilihan = input("Masukan pilihan: ")
suhu = int(input("Masukan suhu: "))

if pilihan == "F":
           c = (suhu - 32) * 5/9
           print(f"{suhu} derajat fahrenheit adlah {c} derajat celcius")
else:
    f = (suhu * 9/5) + 32
    print(f"{suhu} derajat celcius adalah {f} derajat fahrenheit")
           
           
