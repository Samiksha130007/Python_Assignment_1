from MarvelousNum import ChkPrime

def ListPrime(Data):
    sum = 0

    for i in Data:
        if ChkPrime(i):
            sum = sum + i

    return sum


def main():
    Data = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        value = int(input("Enter a number: "))
        Data.append(value)

    print("List:", Data)

    Ret = ListPrime(Data)

    print("Addition of prime numbers is:", Ret)


if __name__ == "__main__":
    main()