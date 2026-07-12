def Frequency(Data, No):
    count = 0

    for i in Data:
        if i == No:
            count = count + 1

    return count


def main():
    Data = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        value = int(input("Enter a number: "))
        Data.append(value)

    print("List:", Data)

    Search = int(input("Enter number to search: "))

    Ret = Frequency(Data, Search)

    print("Frequency is:", Ret)


if __name__ == "__main__":
    main()