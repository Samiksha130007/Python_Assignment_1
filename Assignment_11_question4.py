def ReverseNumber(No):
    rev = 0

    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10

    return rev

def main():
    value = int(input("Enter a number: "))

    result = ReverseNumber(value)
    print("Reverse number =", result)

if __name__ == "__main__":
    main()