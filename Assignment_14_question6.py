CheckOdd=lambda No: (No % 2 !=0)

value=int(input("Enter a number : "))

Ret= CheckOdd(value)
if Ret:
    print("Odd Number")

else:
    print("it is not Odd number ")