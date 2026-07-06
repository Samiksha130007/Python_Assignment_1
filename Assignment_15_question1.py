Square = lambda No : No **2 
def main():
    Data = [12,30,25,11,20]

    print("Input Data : ",Data)
    
    MData=list(map(Square,Data))

    print("Data after Map: ",MData)

if __name__=="__main__":
    main()
    