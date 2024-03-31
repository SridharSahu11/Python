fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList=[]

for x in fruits:
    print(x)
    if "a" in x:
        newList.append(x)
print(newList)

list= [x for x in range(11)]
print(list)

list= [x for x in range(11) if x<6]
print(list)
