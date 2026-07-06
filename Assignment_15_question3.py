CheckOdd= lambda No : (No % 2 != 0)

def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))
          
    for i in range(n):
        value = int(input("Enter a numbers :"))
        Data.append(value)
    print("List : ",Data)
    
    FData=list(filter(CheckOdd,Data))

    print("Data After filter : ",FData)

if __name__=="__main__":
    main()
