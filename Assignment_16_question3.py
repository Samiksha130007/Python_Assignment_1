def Add(No1 , No2 ):
    return No1 + No2

def main():
    value1 = int(input("Enter a 1st Number : "))
    value2 = int(input("Enter a 2nd Number : "))

    Ret = Add(value1 , value2)

    print("Addition : ",Ret)

if __name__=="__main__":
    main()