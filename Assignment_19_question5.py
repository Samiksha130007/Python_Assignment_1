from functools import reduce
def CheckPrime(No):
    if No <=1:
        return False
    for i in range(2 , No):
        if No%i == 0:
            return False
    return True

def Multiply(No):
    return No * 2

def Maximum(No1 , No2):
    if No1 > No2:
        return No1
    else:
        return No2 
    
def main():
    Data = []
    n = int(input("How many number you want to insert : "))

    for i in range(n):
        Value = int(input("Enter numbers : "))
        Data.append(Value)

    print("List : ",Data)

    fdata=list(filter(CheckPrime , Data))
    print("List after filter : ",fdata)

    mdata=list(map(Multiply , fdata))
    print("List after map : ",mdata)

    rdata=reduce(Maximum , mdata)
    print("List after reduce : ",rdata)

if __name__=="__main__":
    main()
    