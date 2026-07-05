def SumDigits(No):
    sum = 0
    while No > 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
    return sum

def main():
    value = int(input("Enter a number: "))

    result = SumDigits(value)
    print("Sum of digits =", result)

if __name__ == "__main__":
    main()