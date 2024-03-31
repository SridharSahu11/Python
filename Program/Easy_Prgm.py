# WAP to input 2 numbers and print sum.
# num1= int(input("Enter First No: "))
# num2= int(input("Enter Second No: "))
# print("The Sum is:-",num1+num2)

# WAP to calculate square area
# num1= int(input("Enter Value : "))
# num2= float(input("Enter Side : "))
# print(num1*num1)
# print(num2**2)

# WAP to calculate average of floats value
# num1= float(input("Enter float number: "))
# num2= float(input("enter float number: "))
# print("Average of",num1,"and",num2,"is : ",(num1+num2)/2)

# WAP to input user's first name and print it's length
# sent= input("Enter your Name:- ")
# print("Your Ulta Name is:- ",sent[::-1])
# print("Your name length is:- ", len(sent))

# WAP to take the user input of a student and print grade.
# marks= int(input("Enter Your Mark:- "))
# if(marks >=90):
#      print("Your Score is:- 'A'")
# elif(marks >= 80 and marks <=90):
#     print("Your Score is 'B'")    
# else:
#  print("YOur Score is 'C'")

# WAP to find the greatest of 3 numbers entered by the user.
# f_Num= int(input("Enter 1st Number:- "))
# s_Num= int(input("Enter Second Number:- "))
# t_Num= int(input("Enter Third Num:- "))
# if(f_Num >= s_Num and f_Num >= t_Num):
#     print("Highest No is:-",f_Num)
# elif(s_Num >= t_Num):
#     print("Highest Number is:-",s_Num)
# else:
#     print("Greatest Number is:-",t_Num)  
# ----------------------------------------------

# WAP to ask the user to enter name of their 3 favorites movies and store them in list
# F_mv= input("Enter Your First Movie:- ")
# list=[]
# list.append(F_mv)
# S_mv= input("Enter Your Second Movie:- ")
# list.append(S_mv)
# T_mv= input("Enter Your Third Movie:- ")
# list.append(T_mv)
# print("Your Favorites Three Movies are:",list)


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Starts with an empty dictionary and add one by one. Use subject name as key and marks as value.
# len= int(input("Enter a length below 5: "))
# dict={}
# for i in range(len):
#     sub= input("Enter Subject:- ")
#     mark= int(input("Enter Sub Mark:- "))
#     dict[sub]=mark   
# print(dict)   

# <------------- While Loops Questions ------------>
# WAP for mulitiplication table of number n:
# t_Num= int(input("Which Number Table You want:- "))
# i=1
# while i<=10:
#     print(t_Num,"x",i,t_Num*i)
#     i=i+1

# WAP Print Elements of Following list.
# [1,4,9,16,25,36,49,64,81,100]
# list=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i <=len(list)-1:
#     if(i==5):
#         break;
#     print(list[i])
#     i=i+1
# else:
#     print("it is end")    

# <------------- For loop -------------->
# Print the ele. of the following list using a loops
# f_list=[1,4,9,16,25,36,49,64,81,100]

# for ele in f_list:
#     print("Lists elements is",ele)

# Print index no of given element in a tuple:
# tuple=(1,4,8,16,25,36,63,69,36)
# x=36
# i=0
# flag=0
# for ele in tuple:   
#     if(x == ele and flag == 0):
#         print("index value of",x,"is:",i)
#         flag=1;
#     i=i+1    
# else:
#     print("There are two repeated numbers with ",x)

# WAP to find the sum of first n numbers.(using while)
# num= int(input("Enter a Number:- "))
# pre_val=num
# sum=0
# while num:
#     sum=sum+num
#     num-=1

# print("Sum of Till Number",pre_val,"is:-",sum)


# Function Program.
# WAF to print the length of a list.
def lenOfList(lst):
    counter=0
    for item in lst:
      counter+=1
    return counter
print(lenOfList([1, 4, 5, 7, 8]))
   
