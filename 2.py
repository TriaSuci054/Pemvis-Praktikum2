'''
Nama    : Tria Suci Cahyani
NIM     : 20051397054
Kelas   : 2020B
Progam mencari volume bangun ruang menggunakan OOP (Object Oriented Programming) dengan menggunakan bahasa 
pemrograman python. Volume bangun ruang yang dapat dicari adalah :

1. Balok
2. Prisma
3. Tabung
'''

class BangunRuang:
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name

   
    def volume(self, order):
        
      
        if order == 1 :
            panjang=float(input("masukkan nilai panjang bangun: "))
            lebar=float(input("masukkan nilai lebar bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = panjang*lebar*tinggi
            
        
        elif order == 2 :
            alas_segitiga=float(input("masukkan nilai alas segitiga alas bangun: "))
            tinggi_segitiga=float(input("masukkan nilai tinggi segitiga alas bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = alas_segitiga*tinggi_segitiga*tinggi/2
       
        
        elif order == 3 :
            jari_jari=float(input("masukkan nilai jari -jari bangun: "))
            tinggi=float(input("masukkan nilai tinggi bangun: "))
            volume = (3.14*jari_jari*jari_jari)*tinggi
      

        return volume
       


bangun_item1 = BangunRuang('Balok')
bangun_item2 = BangunRuang('Prisma')
bangun_item3 = BangunRuang('Tabung')



bangun_items = [bangun_item1, bangun_item2, bangun_item3]

index = 1

for bangun_item in bangun_items:
    print(str(index) + '. ' + bangun_item.info())
    index += 1

print('--------------------')

order = int(input('Masukkan nomor bangun yang dipilih: '))
selected_bangun = bangun_items[order]
print('bangun yang di pilih adalah: ', selected_bangun.name)

print('--------------------')

result = selected_bangun.volume(order)

print('volume bangun datar ',selected_bangun.name,' adalah: ',str(result))
