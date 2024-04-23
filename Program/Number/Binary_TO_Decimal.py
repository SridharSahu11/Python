# First take Binary Number
# Then Convert in to a List
# Reverse the list
# then Do decimal process.


Num= input("Enter A Binary Number:- ")
Num_list= list(Num)
Rev_List= Num_list.reverse()
print(Num_list)
x=0
for i in range(len(Num_list)):
    print(Num_list[i])
    x=x+int(Num_list[i])*pow(2,i)

print(x)
