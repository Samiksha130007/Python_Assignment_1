def factors(No):
    for i in range(1,No+1):
        if No%i==0:
            print(i)
def main():
    value = int(input("Enter a number : "))
    print("Factor of",value,"is : ")
    ret =factors(value)
   
if __name__=="__main__":
    main()