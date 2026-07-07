def ChkNum(No):
    return No % 2 ==0
def main():
    Value = int(input("Enter a number : "))

    Ret = ChkNum(Value)

    if Ret :
        print("Even number ")

    else:
        print("Odd number")

if __name__=="__main__":
    main()
    