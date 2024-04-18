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

# WAP for mulitiplication table of number n:
# t_Num= int(input("Which Number Table You want:- "))
# i=1
# while i<=10:
#     print(t_Num,"x",i,t_Num*i)
#     i=i+1

# WAP to find the sum of first n numbers.(using while)
num= int(input("Enter a Number:- "))
pre_val=num
sum=0
while num:
    sum=sum+num
    num-=1
print("Sum of Till Number",pre_val,"is:-",sum)


# Recursion
# def N_Sum(n):
#   if(n>0):
#     return n + N_Sum(n-1)
#   else:
#     return 0
# print(N_Sum(5))

# factorial of given number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
num = 5
print("Factorial of",num,"is",factorial(num))