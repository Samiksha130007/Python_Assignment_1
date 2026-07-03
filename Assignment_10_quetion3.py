def Factorial(No):
    fact = 1
    for i in range(1, No + 1):
        fact = fact * i
    return fact

def main():
    value = int(input("Enter a number: "))
    result = Factorial(value)
    print("Factorial =", result)

if __name__ == "__main__":
    main()