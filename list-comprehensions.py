"""
numbers=[]
for x in range (10):
    numbers.append(x)
print(numbers)

numbers=[x for x in range(10)]
print(numbers)

for x in range(10):
    print(x**2)
numbers=[x**2 for x in range(10)]
"""

#1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalış.
# random modülünü kullan.
# Her soru 20 puan 100 üzerinden değerlendirme yap.
# Hak bilgisini kullanıcıdan al ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""
import random 
sayi=random.randint(1,100)
can=int(input("kaç hak kullanmak istersin:"))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input("tahmin:"))
    if sayi==tahmin:
        print(f"Tebrikler {sayac} defada bildiniz. Toplam puanınız:{100-(100/can)*(sayac-1)}")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")
    if hak==0:
        print(f"Hakkınız bitti. Tutulan sayi {sayi}")
print(sayi)
"""
#Girilen sayı asal mı diye kontrol et.
sayi=int(input("sayi:"))
asalmi=True
if sayi==1:
    print("1 sayısı asal değildir.")
    
for i in range(2,sayi):
    if (sayi % i==0):
        asalmi=False
        break
if asalmi:
    print("sayı asaldır.")
else:
    print("sayı asal değildir.")
    

