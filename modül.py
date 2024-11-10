"""
#Yöntem1
# import math
import math as islem
# value=dir(math)
# value=help(math.ceil)

# value=math.sqrt(49)
# value=math.factorial(5)
# value=math.floor(5)

value=islem.factorial(5)
print(value)
"""
"""
#Yöntem2
from math import*
def sqrt(x):
    print("x:"+str(x))

value=factorial(5)
print(value)
"""
"""
import random
#result=dir(random)

result=random.random() #0.0-0.1
result=random.random()*100
result=int(random.uniform(10,100))
result=random.randint(1,100)

greeting="hello there"
names=["ali","yağmur","deniz","cenk"]
result=names[random.randint(0,len(names))]
result=random.choice(names)
result=random.choice(greeting)
liste=list(range(10))
random.shuffle(liste)

print(result)
"""

#modül hakkında bilgilendirme
print("modül eklendi")
number=10
numbers=[1,2,3]
person={
    "name":"Ali",
    "age":"24",
    "city":"İstanbul"
}

def func(x):
    """
    fonksiyon hakkında bilgilendirme
    """
    print(f"x:{x}")

class Person:
    def speak(self):
              print("I am speaking...")