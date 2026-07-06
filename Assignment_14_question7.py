CheckDivisible=lambda No: (No % 5 ==0)

value=int(input("Enter a number : "))

Ret= CheckDivisible(value)
if Ret:
    print("Number is divisible by 5")

else:
    print("Number is not divisible by 5 ")