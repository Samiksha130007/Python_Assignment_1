def Addition(No1 , No2):
    return No1 + No2
def Subtraction(No1 , No2):
    return No1 - No2
def Multiplication(No1 , No2):
    return No1 * No2
def Division(No1 , No2):
    return No1 / No2
def main():
    Value1= int(input("enter a 1st number :"))
    Value2= int(input("enter a 2nd number :"))

    ret1 = Addition(Value1,Value2)
    print("Addition is : ",ret1)
    
    ret2 = Subtraction(Value1,Value2)
    print("substraction is : ",ret2)

    ret3 = Multiplication(Value1,Value2)
    print("Multiplication is : ",ret3)

    ret4 = Division(Value1,Value2)
    print("division is : ",ret4)

if __name__=="__main__":
    main()