from functools import reduce

maximum = lambda No1, No2: No1 if No1 > No2 else No2

def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))
          
    for i in range(n):
        value = int(input("Enter a numbers :"))
        Data.append(value)
    print("List : ",Data)

    RData=reduce(maximum,Data)

    print("Data After reduce : ",RData)

if __name__=="__main__":
    main()