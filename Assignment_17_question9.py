def count_digits(no):
    count = 0

    while no > 0:
        count += 1
        no = no // 10

    return count

def main():
    value = int(input("Enter a number: "))
    ret = count_digits(value)
    print("Number of digits:", ret)

if __name__ == "__main__":
    main()