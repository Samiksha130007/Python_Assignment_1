Largest=lambda NO1,NO2,NO3:NO1 if NO1 > NO2 and NO1 > NO3 else (NO2 if NO2 > NO3 else NO3)

value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))
value3 = int(input("Enter third number: "))

Ret = Largest(value1,value2,value3)

print("Largest number is : ",Ret)