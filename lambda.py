def square(num):
    return num**3
numbers=[1,3,5,9]
result=list(map(square,numbers))
for item in map(square,numbers):
    print (item)
print(result)

#SCOPE 
name="global string"
def greeting():
    name="Çınar"
    def hello():
        print("hello"+name)
    hello()
greeting()


x=50
def test():
    global x
    print(f"x: {x}")

    x=100
    print(f"changed x to: {x}")

test()
print(x)