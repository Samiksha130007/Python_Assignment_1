maximum = lambda no1 ,no2 : no1 if no1>no2 else no2 

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Maximum number is:", maximum(num1, num2))

if __name__ == "__main__":
    main()