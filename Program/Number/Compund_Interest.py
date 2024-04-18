Principle_Amt= int(input("Enter Amount:- "))
R_O_I= int(input("Rate Of Interest:- "))
Time= int(input("Time Period in Years:- "))
CI= (Principle_Amt * (1 + (R_O_I/100))) ** Time - Principle_Amt
print("Compound Interest of your amount is:- ",CI)