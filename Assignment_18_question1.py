def Addition(Data):
    sum= 0

    for i in Data:
        sum = i+sum
    return sum

def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))
          
    for i in range(n):
        value = int(input("Enter a numbers :"))
        Data.append(value)
    print("List : ",Data)

    Ret = Addition(Data)
    print("Addition is : ",Ret)

if __name__=="__main__":
    main()