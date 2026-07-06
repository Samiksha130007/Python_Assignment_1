Divisible = lambda No : No%3==0  and No%5==0 

def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))
          
    for i in range(n):
        value = int(input("Enter a numbers :"))
        Data.append(value)
    print("List : ",Data)
    
    FData=list(filter(Divisible,Data))

    print("Data After filter : ",FData)

if __name__=="__main__":
    main()
