'''
Nama    : Tria Suci Cahyani
NIM     : 20051397054
Kelas   : 2020B
'''

print("### Kalkulator Bangun Datar ###")
print("Anda dapat menghitung Luas & Keliling bangun datar")
print("l = Luas")
print("k = Keliling")
jenisKalkulator = str(input("Masukkan Kode : "))

if jenisKalkulator == "l":
    print("Anda memilih untuk menghitung Luas")
    print("KODE :")
    print("1. Persegi")
    print("2. Jajar Genjang")
    print("3. Segitiga")
  
    jenisBangun = int(input("Masukkan Kode : "))

    if jenisBangun == 1:
        s = int(input("Sisi bangun : "))

        luasPersegi = (s * s)
        print("Hasil luas persegi : ", luasPersegi)


    if jenisBangun == 2:
        a = int(input("Alas bangun : "))
        t = int(input("Tinggi bangun : "))

        luasJajargenjang = (a * t)
        print("Hasil luas jajar genjang", luasJajargenjang)

    if jenisBangun == 3:
        a = int(input("Alas bangun : "))
        t = int(input("Tinggi bangun : "))

        luasSegitiga = (0.5 * a * t)
        print("Hasil luas segitiga : ", luasSegitiga)

   


if jenisKalkulator == "k":
    print("Anda memilih untuk menghitung Keliling")
    print("KODE :")
    print("1. Persegi")
    print("2. Jajar Genjang")    
    print("3. Segitiga")
   
    jenisBangun = int(input("Masukkan Kode : "))

    if jenisBangun == 1:
        s = int(input("Sisi bangun : "))

        kelPersegi = (s * s * s * s)
        print("Hasil keliling persegi : ", kelPersegi)

    if jenisBangun == 2:
        s1 = int(input("Sisi kanan : "))
        s2 = int(input("Sisi kiri : "))
        s3 = int(input("Sisi atas : "))
        s4 = int(input("Sisi bawah : "))

        kelJajargenjang = (s1 + s2 + s3 + s4)
        print("Hasil keliling jajar genjang", kelJajargenjang)

    if jenisBangun == 3:
        a = int(input("Alas bangun : "))
        t = int(input("Tinggi bangun : "))
        d = int(input("Diagonal bagun : "))

        kelSegitiga = (a + t + d)
        print("Hasil keliling segitiga : ", kelSegitiga)
