#sayilar=[1,3,5,7,9,12,19,21]
"""
#1- Listeyi yazdır
i=0
while i<len(sayilar):
    print(sayilar[i])
    i+=1

#2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır.
baslangic=int(input("başlangıç:"))
bitis=int(input("bitiş:"))
while baslangic<bitis:
    i=baslangic
    while i<bitis:
        i+=1
        if (i%2==1):
        print(i)
"""
"""
#3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
i=100
while i>0:
    print(i)
    i-=1
#4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı şekilde yazdırın.
numbers=[]
i=0
while i<5:
    sayi=input("sayi:")
    numbers.append(sayi)
    print(numbers)
"""
#5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın.
#   ürün sayısını kullanıcıya sor.
#   dictionary listesi yapısı (name,price) şeklinde olsun.
#   ürün ekleme işlemi bittiğinde ürünleri ekranda sırala.

urunler = []
adet = int(input("Kaç ürün eklemek istiyorsun: "))
i = 0

while i < adet:
    name = input("Ürün ismi: ")
    price = input("Ürün fiyatı: ")
    urunler.append({
        "name": name,
        "price": price
    })
    i += 1

for urun in urunler:
    print(f"Ürün adı: {urun['name']} Ürün fiyatı: {urun['price']}")
