# info={
#     "name":"Sridhar Sahu",
#     "subjects":"Pyhton",
#     "age":23,
#     "is_adult":"Yes",
#     "tuple":('a',"b",'23',25)
# }
# print(info)

# info["name"]="Allen Walker"
# keysR= info.keys()
# print(type(keysR))  #<class 'dict_keys'>
# print(keysR)   # dict_keys(['name','subjects','age','is_adult','tuple'])

# print(info.values())    # dict_keys(['Allen Walker','Pyhton',23,('a',"b",'23',25)])
# print(type(info.values()))  #<class 'dict_values'>

# print(info.items()) #returns all keys and value as a tuples
# print(type(info.items())) #<class 'dict_items'>

# print(info.get("name"))  #Allen Walker


# Set in Python
# set_collection= {11,22,11,"World","bye","Bye"}
# print(set_collection)
# print(len(set_collection))
# empty_set= set() #empty set: syntax
# print(type(empty_set))
# empty_set.add(1)
# empty_set.add(2)
# empty_set.add(2)
# empty_set.add("buna")
# print(empty_set)
# print("After Noon explore set methods.")

# It can contain any type of element such as integer, float, tuple etc. But mutable elements (list, dictionary, set) can't be a member of set. Consider the following example.
set_1={1,22,33,"Hello EveryOne"}
print(type(set_1))
set_2 = {["Javatpoint",4],[2,5]}  
print(set_2)

