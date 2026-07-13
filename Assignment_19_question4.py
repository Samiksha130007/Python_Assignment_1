from functools import reduce

def CheckEven(No):
    return No % 2 == 0

def Square(No):
    return No ** 2

def  Addition(No1 , No2):
    return No1 + No2

def main():
    Data =[]
    n=int(input("How many number you want to insert : "))

    for i in range(n):
        value =int(input("Enter a number : "))
        Data.append(value)
    print("List : ",Data)

    FData=list(filter(CheckEven , Data))
    print("List after filter : ",FData)

    MData=list(map(Square ,FData ))
    print("List After map : ",MData)

    RData=reduce(Addition , MData)
    print("List after reduce : ",RData)

if __name__=="__main__":
    main()