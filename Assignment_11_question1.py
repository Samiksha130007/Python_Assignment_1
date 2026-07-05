def CheckPrime(No):
    if No <= 1:
         return False

    for i in range(2, No):
            if No % i == 0:
                return False
    return True
def main():
    value = int(input("Entaer a number : "))

    ret =CheckPrime(value)

    print(ret)

    if ret == True:
        print("Prime Number")
    else:
        print("Not prime number")
    
if __name__=="__main__":
    main()
