def perfect(No):
    sum = 0

    for i in range(1, No):
        if No % i == 0:
            sum = sum + i
    return sum

def main():
    value = int(input("Enter a number: "))
    ret = perfect(value)

    
    if ret==value:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()