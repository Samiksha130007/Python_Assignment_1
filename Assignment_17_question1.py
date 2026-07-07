import ArithMetic_Module
def main():
    value1 = int(input("Enter a 1st Number :"))
    value2 = int(input("Enter a 2nd Number :"))

    Result1 = ArithMetic_Module.Add(value1 ,value2)
    print("Addition is : ",Result1)

    Result2 = ArithMetic_Module.Sub(value1 ,value2)
    print("Subtraction is : ",Result2)

    Result3 = ArithMetic_Module.Mult(value1 ,value2)
    print("Multiplication is : ",Result3)

    Result4 = ArithMetic_Module.Div(value1 ,value2)
    print("Division is : ",Result4)

if __name__=="__main__":
    main()
