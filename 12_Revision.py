import random

print(random.randrange(1,11))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

str=""
for x in "ASWATH_NAGAR":
  str+=x
  print(x)
print(str)   

txt="The best things in life are free!"
print("free" in txt) #True
print("expensive" not in txt) #True

b="Mumbai Indians🏏🏏"
print(b[2:5]) #mba
print(b[:5]) #Mumba
print(b[-5:-2]) #ans
# print(b[-5:-1]) #Error will come because of emoji
# print(b[-5:]) #Error will come because of emoji

# Python Modify Strngs
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.split(",")) #['Hello', ' World!']

# Escape Character
txt_1 = "We are the so-called \"Vikings\" from the north."
print(txt_1)

print(bool("abc"))
x = 200
print(isinstance(x, int))

# List
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:0]) #[]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']
thislist.insert(3,"Avocado")
print(thislist) #['apple', 'banana', 'cherry', 'Avocado', 'orange', 'kiwi', 'melon', 'mango']
thislist.append("orange")
print(thislist) #It will Add One more Orange

# Extend List
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist) ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']
thislist.clear()
print(thislist)