#username, password => database

a,b,c,d=5,5,10,4
password="1234"
username="Zeynep Hendem"

result=(a==b) #true
result=(a==c)
result=("zeynephendem"==username)
result=(a!=b)
result=(a!=c)

#1- Girilen 2 sayıdan hangisi büyüktür?
a=int(input("a:"))
b=int(input("b:"))
result=(a>b)
print(f"a:{a} b:{b} den büyüktür:{result}")

#2- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız, eğer ortalama 50 ve üstündeyse "geçti" değilse "kaldı" yazdırın.
vize1=float(input("vize1:"))
vize2=float(input("vize2:"))
final=float(input("final:"))

ortalama=(((vize1+vize2)/2)*0.6)+(final*0.4)
print(f"not ortalamanız:{ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

#3- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi=int(input("sayi:"))
tekcift=(sayi % 2 == 0)
print(f"girilen sayı çift olma durumu:{tekcift}")

#4- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi=int(input("sayi:"))
pozitifmi=(sayi>0)
print(f"girilen sayının pozitif olma durumu:{pozitifmi}")

#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz. 
#   (email: email@zeynephendem.com parola:abc123)

email= "email@zeynephendem.com "
password= "abc123"

email=input("email:")
password=input("parola:")

isEmail=(email==email)
isPassword=(password==password)

print(f"Email bilgisi doğrumu:{isEmail} ve Parola doğru mu:{isPassword}")




