"""
name="Sadık"
surname="Turan"
age=36

print("My name is " + name + " " + surname + " and I am " + str(age) + " years old.")
"""

#Format

"""
name="Çınar"
surname="Turan"

print("My name is {1} {0}".format(name,surname))  soyad başa gelir.
print("My name is {} {}".format(name,surname)) isim başta olur.
print("My name is {} {} and I'm {} years old".format(name,surname,"36"))
"""

"""
result=200/500
print("the result is {r}".format(r=result))
"""
"""
website="http://www.sadikturan.com"
course="Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1-"course" karakter dizisinde kaç karakter bulunur?
print(len(course))

#2-"website" içinden www karakterlerini al.
print(website[7:10])

#3- "website" içinden com karakterlerini alın.
print(website[22:])

#4- "course" içinden ilk 15 ve son 15 karakterleri al.
print(course[0:15])
print(course[15:])

#5- "course" ifadesindeki karakterleri tersten yazın.
print(course[::-1])

#6- Ekrana "Benim adım Bora Yılmaz, yaşım 32 ve mesleği mühendis." yaz.
name, surname, age, job="Bora","Yılmaz", 32, "mühendis"
print("Benim adım " + name + " " + surname + ", yaşım " + str(age) + " ve mesleğim mühendis.")
print("Benim adım {} {}, yaşım{} ve mesleğim {}.".format(name,surname,age,job))
print(f"Benim adım {name} {surname}, yaşım{age} ve mesleğim {job}.")

#7- "Hello world" ifadesindeki w harfini W harfiyle değiştir.
s="Hello world"
print(s.replace("w","W"))

#8- "abc" ifadesini yan yana 3 defa yazdır.
print("abc"*3)

#print(result) dersek result değişkeniyle yapılabilir.
"""

"""
message="Hello there."
message=message.upper() #büyük harfe çevirir
message=message.lower() #küçük harfe çevirir
message=message.title() #her kelimenin baş harfi büyük olur
message=message.capitalize() #sadece ilk harf büyük
message=message.strip() #baştaki boşluk gider
message=message.split() #her bilgi bölünürek karakter dizisi olur

print(message)
"""

website="http://www.sadikturan.com"
course="Python Kursu:Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1-"Hello World" karakter dizisinin baş ve sondaki boşluk karakterlerini silin
from unittest import result
result="Hello World".strip()
result="Hello World".lstrip()
result="Hello World".rstrip()
result=website.lstrip("/:pth")

#2- sadikturan bilgisi haricindeki karakterleri silin.
result="www.sadikturan.com".strip("w.moc")

#3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.
result=course.lower()

#4- "website" içinde kaç tane a karakteri var?
result=website.count("a")

#5- "website" "www" ile başlayıp "com" ile bitiyor mu?
result=website.startswith("www")
result=website.endswith("com")

#6- "website" içinde ".com" ifadesi var mı?
result=website.find("com")

#7- "course" içindeki karakterlerin hepsi alfabetik mi?
result=course.isalpha()

#8-"contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin.
result="Contents".center(50,)
result="Contents".ljust(50,)
result="Contents".rjust(50,)

#9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
result=course.replace("","-")

#10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştir.
result="Hello World".replace("World","There")

#11- "course" karakter dizisini boşluk karakterlerinden ayırın.
result=course.split(" ")
print(result)



print(result)