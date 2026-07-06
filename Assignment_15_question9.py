from functools import reduce
Multiplication= lambda No1 ,No2 : No1 * No2

def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))
          
    for i in range(n):
        value = int(input("Enter a numbers :"))
        Data.append(value)
    print("List : ",Data)
    
    RData=reduce(Multiplication,Data)

    print("Data After reduce : ",RData)

if __name__=="__main__":
    main()