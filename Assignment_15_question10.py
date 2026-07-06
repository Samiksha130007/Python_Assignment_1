from functools import reduce
CheckEven = lambda No :(No % 2 == 0)

count = lambda No , A : (No+1)

def main():
    Data =[]
    n=int(input("enter list number :"))
          
    for i in range(n):
        value = int(input("Enter a number :"))
        Data.append(value)
    print("List : ",Data)
    
    FData=list(filter(CheckEven,Data))
    print("Data After filter : ",FData)

    RData = reduce(count , FData ,0)
    print("Data After reduce : ",RData)

if __name__=="__main__":
    main()