# WAP Print Elements of Following list.
# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i <= len(list)-1:
#     if(i==5):
#         break;
#     print(list[i])
#     i=i+1
# else:
#     print("it is end")  

# Print index no of given element of this tuple:
# tuple=(1,4,8,16,25,36,63,69,36)
# x=36
# i=0
# flag=0
# for ele in tuple:   
#     if(x == ele ):
#         print("index value of",x,"is:",i)
#         break;
#     i=i+1    
# else:
#     print("There are two repeated numbers with ",x)

# WAP to check if a list contains a palindrome of elements or not
# input:- [1,2,3,2,1]
# output:- "It is Palindrome List"   
# list1=[11,22,33,22,11]
# flag=False
# for i in range(math.floor(len(list1)/2)):
#     if(list1[i] == list1[(len(list1)-i)-1]):
#      flag=True
#     else:
#      flag=False
#      break 

# Iterate a array using Recusrion.
def Print_F(i):
  li_st=[11,12,22,23,33,34,44,45]
  if(i<len(li_st)):
    print(li_st[i])
    Print_F(i+1)
  else:
    return 0
Print_F(0)