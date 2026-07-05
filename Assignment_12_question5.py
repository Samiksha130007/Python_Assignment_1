def PrintNumbers(No):

    for i in range(No , 0 ,-1):
        print(i , end=" ")

def main():
    value= int(input("enter a number : "))
    ret= PrintNumbers(value)
if __name__=="__main__":
    main()