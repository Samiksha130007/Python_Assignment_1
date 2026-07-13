from functools import reduce

def Filter(No):
    if No >=70 and No<=90:
        return No

def  IncreaseNo(No):
    return No + 10

def Product(No1 , No2):
    return No1 * No2

def main():
    Data =[]
    n=int(input("How many number you want to insert :"))
    for i in range(n):
        Value = int(input("Enter a Number : "))
        Data.append(Value)
    print("List : ",Data)

    FData= list(filter(Filter , Data))
    print("List After Filter : ",FData)

    MData = list(map(IncreaseNo , FData))
    print("List After Map : ",MData)

    RData = reduce(Product , MData)
    print("List After Reduce : ",RData)

if __name__=="__main__":
    main()