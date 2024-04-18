first_Num= int(input("Enter First Num:- "))
second_Num= int(input("Enter Second Num:- "))
third_Num= int(input("Enter Third Num:- "))

if(first_Num >= second_Num and first_Num >= third_Num):
    print("Greatest 1st !!",first_Num)
elif(second_Num >= third_Num):
    print("Greatest 2nd !!",second_Num)
else:
    print("Greatest 3rd !!",third_Num)
