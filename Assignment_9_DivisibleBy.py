def checkDivisible(No):
     if No % 3 == 0 and No % 5 == 0:
        return True
     else:
        return False

def main():
    value = int(input("Enter a number: "))

    ret = checkDivisible(value)

    if ret:
        print(value, "is divisible by both 3 and 5")
    else:
        print(value, "is not divisible by both 3 and 5")

if __name__ == "__main__":
    main()