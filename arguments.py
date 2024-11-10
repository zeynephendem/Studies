"""
def changeName(n):
    n="ada"
name="yiğit"
changeName(name)
print(name)

def change(n):
    n[0]="istanbul"
sehirler=["ankara","izmir"]
n=sehirler
n[0]="istanbul"
print(sehirler)
print(n)
"""
"""
def add(a,b,c=0):
    return sum((a,b,c))
print(add(10,20))
print(add(10,20,30))

def add(*params):
    return sum(params)
print(add(10,20))
print(add(10,20,30))
"""
"""
def displayUser(**args):
    for key, value in args.items():
        print("{} is {}".format(key,value))
displayUser(name="Zeynep",age=20,city="İstanbul")
displayUser(name="Ayşe",age=21,city="Sakarya")
displayUser(name="Ali",age=19,city="Edirne")
"""
"""
#1-Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def yazdir(kelime,adet):
    print(kelime*adet)
yazdir("Merhaba\n",10)

#2-Kendine gönderilen sınırsız sayıdaki parametreyi bir listeyi çeviren fonksiyonu yazın.
def listeyeCevir(*params):
    liste=[]
    for param in params:
        liste.append(param)
    return liste
result=listeyeCevir(10,20,30,"Merhaba")
print(result)

#3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
sayi1=int(input("sayı 1:"))
sayi2=int(input("sayı 2:"))

def asalSayilariBul(sayi1,sayi2):
    for sayi in range(sayi1, sayi2):
        if sayi>1:
             for i in range(2,sayi):
                 if (sayi%i==0):
                     break
                 else:
                     print(sayi)

asalSayilariBul(sayi1,sayi2)

#4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.
def tamBolenleriBul(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if (sayi % i ==0):
            tamBolenler.append(i)
        return tamBolenler
print(tamBolenleriBul(20))
"""