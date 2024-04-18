Num= int(input("Enter Number:- "))
if(Num > 1):
    no=round(Num/2)
    for i in range(2,no):
        print(i)
        if(Num % i == 0):
            print("It is not a Prime Number !!",Num)
            break;
    else:
        print("It is a Prime Number !!",Num)
else:
    print("Number Must be Greater then 1")