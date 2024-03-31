thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']
thislist.sort()
print(thislist) #['Kiwi', 'Orange', 'banana', 'cherry']

thislist_1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist_1.reverse()
print(thislist_1)
l=[]
for ele in thislist_1:
    l.insert(0,ele)
print(l)

# Reversing a list using slicing technique
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
 
 
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))