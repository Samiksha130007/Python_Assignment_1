def multiply(a, b):
    return a * b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = multiply(a,b)
    print("Multiplication is:", result)

if __name__ == "__main__":
    main()
