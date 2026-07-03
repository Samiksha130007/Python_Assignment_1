def SumNatural(No):
    sum = 0
    for i in range(1, No + 1):
        sum = sum + i
    return sum

def main():
    value = int(input("Enter a number: "))
    result = SumNatural(value)
    print("Sum =", result)

if __name__ == "__main__":
    main()