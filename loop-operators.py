"""
for item in range(1,10):
    print(item)
print(list(range(1,10)))
"""
"""
#enumerate
index=0
greeting="Hello There"

for letter in greeting:
    print(f"letter:{letter} index:{index}")
    index +=1
"""
#zip
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)
