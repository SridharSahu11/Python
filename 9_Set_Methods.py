import math

set_1={1,2,11,33,22,2,"Sam"}
set_2={"Jaz","Aadhya","Sam","Prateek","Golu","Jaz"}
print("set_1: ",set_1)
print("set_2: ",set_2)

# iSM= set_1.intersection(set_2) # & (intersection)
# print(iSM)
# uM= set_1.union(set_2)
# print("Union Ouput:- ",uM)

# a={"Raja","Rani"}
# b={"Raja","Rani","Mantri"}
# subSet=a.issubset(b) #if elements of A contained by B then, it will return True.
# print(subSet)

# print ("Hello Annie, I'm " + str(math.pi) + " years old!")

# We can update a list in a Set. Update dont return a new value.
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
# print(thisset)

# print(thisset)

# print(thisset.discard("apple"))
# print("After Removed",thisset)
# thisset.clear()
# print("After using Clear Method",thisset)

# Join Two Sets using union() and update()
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set11={"a", "b" , "c"}
# set22= {11, 22, 33}
# set11.update(set22)
# print(set11)

# Method <---> Description
# add() ------>	Adds an element to the set
# clear() ------>	Removes all the elements from the set
# copy()  ------>	Returns a copy of the set
# difference()  ------>	Returns a set containing the difference between two or more sets
# difference_update() ------>	Removes the items in this set that are also included in another, specified set
# discard()	------> Remove the specified item
# intersection() ------>	Returns a set, that is the intersection of two other sets
# intersection_update()	 ------> Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() ------>	Returns whether two sets have a intersection or not
# issubset() ------> Returns whether another set contains this set or not
# issuperset() ------>	Returns whether this set contains another set or not
# pop() ------>	Removes an element from the set
# remove() ------>	Removes the specified element
# symmetric_difference() ------> Returns a set with the symmetric differences of two sets
# symmetric_difference_update() ------>	inserts the symmetric differences from this set and another
# union() ------> Return a set containing the union of sets
# update() ------> Update the set with the union of this set and others
 

