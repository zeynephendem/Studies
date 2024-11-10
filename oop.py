#Object Oriented Programming (OOP)
"""
#class

class Person:
    pass #yer tutucu
    address="no information"
    #constructor (yapıcı metod)
    def __init__(self,name,year):
        #class/object attributes

        self.name=name
        self.year=year
    
    #methods
    def intro(self):
        print("Hello There. I am " + self.name)
    def calculateAge(self):
        return 2024-self.year


#instance(object)
p1=Person(name="Ali",year=1990)
p2=Person(name="Yağmur",year=1995)
p1.intro()
p2.intro()
print(f"Yaşım:{p1.calculateAge()}")
print(f"Yaşım:{p2.calculateAge()}")
print(p1)
print(p2)
"""
"""
class Circle:
    #Class object attribute
    pi=3.14
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    #Methods
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1=Circle() #yaricap=1
c2=Circle(5)

print(f"c1:alan={c1.alan_hesapla()} çevre={c1.cevre_hesapla}")
print(f"c1:alan={c2.alan_hesapla()} çevre={c2.cevre_hesapla}")
"""
"""
#İnheritance(Katılım):Miras Alma
#Person=>name,lastname,age,eat(),run(),drink()
#Student(Person), Teacher(Person)

class Person():
    def __init__(self, fname, lname):
        self.firstName=fname
        self.lastName=lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person.")

class Student():
    def __init__(self):
        Person.__init__(self)
        print("Student Created")
p1=Person("Ali","Yılmaz")
s1=Student("Çınar","Turan")

print(p1.firstName+''+p1.lastName)
print(s1.firstName+''+s1.lastName)

p1.who_am_i()
s1.who_am_i()
"""
"""
myList=[1,2,3]
myString="my string"

print(len(myList))
print(len(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("Movie objesi oluşturuldu.")
m=Movie("film adı","yönetmen adı","filmin süresi")
print(myList)
"""

#Uygulama
class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer
q1=Question("En iyi programlama dili hangisidir?",["C^#","python","javascript","java"],"python")
q2=Question("En popüler programalama dili hangisidir?",["C^#","python","javascript","java"],"python")
q3=Question("En çok kazandıran programlama dili hangisidir?",["C^#","python","javascript","java"],"python")


# print(q1.checkAnswer("python"))
# print(q2.checkAnswer("C#"))
# print(q3.checkAnswer("C#"))


class Quiz:
    def __init__(self, questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
q1=Question("En iyi programlama dili hangisidir?",["C^#","python","javascript","java"],"python")
q2=Question("En popüler programalama dili hangisidir?",["C^#","python","javascript","java"],"python")
q3=Question("En çok kazandıran programlama dili hangisidir?",["C^#","python","javascript","java"],"python")
questions=[q1,q2,q3]

quiz=Quiz(questions)
question=quiz.getQuestion
print(question)