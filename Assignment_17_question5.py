def ChkPrime(No):
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def main():
    Value = int(input("Enter a number : "))
    Ret =ChkPrime(Value)
    if Ret:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()