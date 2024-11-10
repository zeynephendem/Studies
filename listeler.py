"""
my_list=[1,2,3]
my_list=["bir",2,True,5.6]
print(my_list)
"""
"""
list1=["one","two"]
list2=["four","five"]
numbers=list1+list2
print(numbers)
print(len(numbers))

userA=["Sadık",36]
userB=["Çınar",2]
users=[userA,userB]
print(userA)
print(userB)
print(users)
"""

"""
#1-"Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar=["Bmw","Mercedes","Opel","Mazda"]

#2- Liste kaç elemanlıdır?
result=len(arabalar)

#3- Listenin ilk ve son elemanı nedir?
result=arabalar[0]
result=arabalar[3]

#4- Mazda değerini Toyota ile değiştirin.
arabalar[-1]="Toyota"
result=arabalar

#5- Mercedes listenin bir elemanı mıdır?
result="Mercedes" in arabalar 

#6- Listenin -2 indeksindeki değer nedir?
result=arabalar[-2]

#7- Listenin ilk 3 elemanını alın.
result=arabalar[:3]

#8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:]=["Toyota","Renault"]
result=arabalar

#9- Listenin üzerinde "Audi" ve "Nissan" değerlerini ekleyin.
result=arabalar+["Audi"+"Nissan"]

#10- Listenin son elemanını silin.
del arabalar[-1]
result=arabalar

#11- Liste elemanlarını tersten yazdırınız.
result=arabalar[::-1]

#12- Aşağıdaki verileri bir liste içinde saklayınız.
     #studentA:Yiğit Bilgi 2010, (70,60,70)
     #studentB:Sena Turan 1999, (80,80,70)
     #studentC:Ahmet Turaan 1998, (80,70,90)
studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","Turan",1999,[80,80,70]]
studentC=["Ahmet","Turan",1998,[80,70,90]]

#13- Liste elemanlarını ekrana yazdırın. 
result=studentA
print(result)
"""

"""
numbers=[1,10,5,16,4,9,10]
letters=["a","g","s","b","y","a","s"]

val=min(numbers)
val=max(numbers)

#numbers.append(49) sona eklenir
#numbers.insert(3, 78) 3.indekse 78 sayısı eklenir.

#numbers.pop() en sondaki silinir.
# numbers.pop(0) 0.indeks silinir. 
# numbers.remove(10) 10 sayısı silinir.

#numbers.sort()
#numbers.reverse() tersten sıralar
#print(len(letters))
#numbers.clear() listeyi siler.
 
print(numbers)
"""

names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

#1- "Cenk" ismini listenin sonuna ekleyin.
names.append("Cenk")

#2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")

#3- "Deniz" ismini listeden siliniz.
names.remove("Deniz")

#4- "Sena" isminin indeksi nedir?
index=names.index("Sena")
print(index)

#5- "Ali" listenin bir elemanı mıdır?
result="Ali" in names
print(result)

#6- Liste elemanlarını ters çevirin.
names.reverse()
print(names)

#7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

#8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

#9- str="Chevrolet,Dacia" karakter dizisini listeye çevirin.
str="Chevrolet,Dacia"
result=str.split(",")
print(result)

#10- years dizisinin en büyük ve en küçük elemanı nedir?
min=min(years)
max=max(years)
print(min,max)

#11- years dizisinin kaç tane 1998 değeri vardır?,
result=years.count(1998)
print(result)

#12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

#13- Kullanıcıdan alacağınız 3 markayı bir listede saklayınız.
markalar=[]
marka=input("marka:")
markalar.append(marka)
print(marka)