d1={}
print(d1)
print(type(d1))
d1[1]="Nothing"
d1[2]="Something"
print(d1)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
print(car.values())

# print("After Using Items",car.items()) #The items() method will return each item in a dictionary, as tuples in a list.
# Change Dictionary Items
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# dict2={
#   "brand": "FordA",
#   "model": "Ferari",
#   "year": 1970
# }
# dict2=thisdict
# print("Dict2",dict2)

# list_1=[1,2,3,4]
# list_2=['Sridhar','Varun',"Asutosh","Lalit"]
# data_1= dict(zip(list_1,list_2))
# print(data_1)


# Method <---->	Description
# clear()	--------> Removes all the elements from the dictionary
# copy() -------->	Returns a copy of the dictionary
# fromkeys() -------->	Returns a dictionary with the specified keys and value
# get() -------->	Returns the value of the specified key
# items()-------->	Returns a list containing a tuple for each key value pair
# keys() -------->	Returns a list containing the dictionary's keys
# pop() -------->	Removes the element with the specified key
# popitem() -------->	Removes the last inserted key-value pair
# setdefault() -------->	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() -------->	Updates the dictionary with the specified key-value pairs
# values() -------->	Returns a list of all the values in the dictionary

# Nested Dictionary.
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


for x in myfamily:
 for y in myfamily[x]:
   print(y,myfamily[x][y])