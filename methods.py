#method
"""
list=[1,2,3]

list.append(4)
list.pop()
print(type(list))

myString="Hello"
print(myString.upper())
"""

#fonksiyon

def sayHello(name):
    print("Hello"+name)
sayHello("Zeynep")
sayHello("Ayşe")
sayHello("Ali")

def yasHesapla(dogumYili):
    return 2019-dogumYili
ageZeynep=yasHesapla(2017)
ageAyse=yasHesapla(2018)
ageAli=yasHesapla(2009)
print(ageAyse,ageAli,ageZeynep)

def EmekliligeKacYilKaldi(dogumYili,isim):
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas
    if emeklilik>0:
        print(f"emekliliğinize{emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")
EmekliligeKacYilKaldi(1980,"Zeynep")