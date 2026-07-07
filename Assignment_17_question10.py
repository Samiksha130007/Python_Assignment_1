def sum_digits(no):
    total = 0

    while no > 0:
        digit = no % 10
        total += digit
        no = no // 10

    return total

def main():
    value = int(input("Enter a number: "))
    ret = sum_digits(value)
    print("Addition of digits:", ret)

if __name__ == "__main__":
    main()