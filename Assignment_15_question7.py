LengthOfString = lambda String :len(String)>5 

def main():
    Data =[]
    n=int(input("enter list number :"))
          
    for i in range(n):
        value = input("Enter a String :")
        Data.append(value)
    print("List : ",Data)
    
    FData=list(filter(LengthOfString,Data))

    print("Data After filter : ",FData)

if __name__=="__main__":
    main()
