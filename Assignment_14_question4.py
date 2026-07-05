minimum  = lambda a, b: a if a < b else b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("minimum number is:", minimum(num1, num2))

if __name__ == "__main__":
    main()