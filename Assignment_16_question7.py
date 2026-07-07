def Divisible(No):
    return No % 5 == 0
def main():
    value = int(input("Enter number : "))

    Ret = Divisible(value)

    print(Ret) 
if __name__=="__main__":
    main()
