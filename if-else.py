"""
username="sadikturan"
password="1234"

isLoggedin=(username=="sadikturan") and (password=="1234")

if isLoggedin:
   print("Hoş geldiniz")
"""

"""
x=10
y=20

if x>y:
    print("x y den büyük")
elif x==y:
    print("x ye eşit")
else:
    print("y x den büyük")
"""
"""
num=int(input("sayi:"))

if num>0:
    print("sayi pozitif")
elif num<0:
    print("sayi negatif")
else:
    print("sayı sıfır")
"""

#UYGULAMALAR
"""
#1.soru
isim=input("isminiz:")
yas=int(input("yaşınız:"))
egitim=input("eğitim:")

if (yas>=18) and (egitim=="lise" or egitim=="üniversite"):
    print("ehliyet alabilirsiniz:")
else:
    print("ehliyet alamazsınız.")
"""

"""
#2.soru
yazili1=float(input("1.yazılı:"))
yazili2=float(input("2.yazılı:"))
sozlu=float(input("sözlü:"))

ortalama=(yazili1+yazili2+sozlu)/3

if(ortalama>=0) and (ortalama<25):
    print(f"ortalamanız:{ortalama} notunuz:0")
elif (ortalama>=25) and (ortalama<45):
    print(f"ortalamanız:{ortalama} notunuz:1")
elif (ortalama>=45) and (ortalama<55):
    print(f"ortalamanız:{ortalama} notunuz:2")
elif (ortalama>=55) and (ortalama<70):
    print(f"ortalamanız:{ortalama} notunuz:3")
elif (ortalama>=70) and (ortalama<85):
    print(f"ortalamanız:{ortalama} notunuz:4")
elif (ortalama>=85) and (ortalama<=100): 
    print(f"ortalamanız:{ortalama} notunuz:5")
else:
    print("yanlış bilgi girdiniz.")
"""
"""
#3.soru
import datetime

# Kullanıcıdan tarih al
tarih = input("Araçınız hangi tarihte trafiğe çıktı (YYYY/MM/DD): ")

# Tarihi ayır ve sayısal verilere dönüştür
yil, ay, gun = map(int, tarih.split("/"))

# Kullanıcının girdiği tarihi oluştur
trafigeCikis = datetime.date(yil, ay, gun)

# Bugünün tarihi
simdi = datetime.date.today()

# Tarihler arasındaki farkı hesapla
fark = (simdi - trafigeCikis).days

# Servis aralığını kontrol et
if fark <= 365:
    print("1. servis aralığı")
elif 365 < fark <= 365 * 2:
    print("2. servis aralığı")
elif 365 * 2 < fark <= 365 * 3:
    print("3. servis aralığı")
else:
    print("Hatalı süre.")
"""