# <----------- list [] ------------------->
# List is a mutable data type.
# student= ["Jinendra",85,"B","Bada Bazar"]
# student[2]= 88
# print(student)
# print(student[5]) #IndexError: list index out of range
# marks=[33,54,66,78,52,92]
# print(marks[1:4])  #[54,66,78]
# print(marks[:4])  #[33,54,66,78]
# print(marks[1:])  #[54,66,78,52,92]
# print(marks[-3:])  #[78,52,92]
# print(marks[-4:-1])  #[66,78,52]
# sort="Sorting in Ascending Order using 'sort()':- "
# print(marks.sort())
# marks.sort()
# print(sort,marks)

# Print decending order of a list
# list=[11,88,45,63,19,54]
# list[4]=28
# print(list) #[11,88,45,63,28,54]
# list.insert(2,21)
# print(list)  #[11,88,21,45,63,28,54]
# list.sort(reverse=True)
# print(list)

# User input List[]
# list=[]
# n= int(input("Enter the number of list you want: "))
# for i in range(0,n):
#     ele=int(input("Enter Element:- "))
#     list.append(ele)

# for ele in list:
#     print(ele,end=" ")

# print(list)




# <----------- Tuple () ------------------>
# tuple=(22,12,45,63,(1+1),True,"hello")
# print(type(tuple))
# print(tuple)
# print(tuple[3])
# print(tuple.index(True)) #5
# print(tuple.count(2)) #[22,12]

# str=("No More")
# print(type(str)) #<class 'str'>
# str2=("Anytime",)
# print(str2,type(str2))
# str3="Anytie",
# print(str3,type(str3))

# forDel=("A","B","C","D")
# del forDel[1] #'tuple' obj don't support item deletion
# print(forDel)

tuple_ = ("Python", "Tuple", "Ordered", "Immutable", [1,2,3,4])
try:
    tuple_[2]= 'items'    
    print(tuple_)
except Exception as e:
    print(e)   #'tuple' does not support item assignment
    
tuple_[-1][2] = 10     
print(tuple_)        
