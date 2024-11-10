#key-value
#41=> kocaeli 34=> istanbul

"""
sehirler=["kocaeli","istanbul"]
plakalar=[41,34]
print(plakalar[sehirler.index("kocaeli")])

#print(plakalar["kocaeli"]) => 41
#print(plakalar["istanbul"]) => 34

plakalar={"kocaeli":41, "istanbul":34}
print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"]=6
plakalar["kocaeli"]="new value"
print(plakalar)
"""

"""
users={
    "zeynephendem":30},
{
    "zeynephendem":2,
    "address":"kocaeli",
    "phone":"1231321"
}
print(users["zeynephendem"]["address"])
"""

"""
ogrenciler={
"120": {
    "ad":"Ali",
    "soyad":"Yılmaz",
    "telefon":"532 000 00 01"
    },
    "125": {
    "ad":"Can",
    "soyad":"Korkmaz",
    "telefon":"532 000 00 02"
    },
    "128": {
    "ad":"Volkan",
    "soyad":"Yükselen",
    "telefon":"532 000 00 03"
    },
    }

1- Kullanıcıdan aldığınız bilgilerle öğrenci bilgilerini dictionary içinde saklayınız.

2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
"""

ogrenciler={}

number=input("öğrenci no:")
name=input("öğrenci adı:")
surname=input("öğrenci soyad:")
phone=input("öğrenci telefon:")

ogrenciler[number]={
    "ad":name,
    "soyad":surname,
    "telefon":phone
}
print(ogrenciler)

#update ile hepsini içinde topluyoruz.
ogrenciler={}
ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})
print(ogrenciler)

