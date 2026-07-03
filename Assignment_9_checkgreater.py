def checkGreater(No1 , No2 ):
    if No1 > No2 :
        return True
    else:
        return False

def main():
    value1 = int(input("Enter a 1st number : "))
    value2 = int(input("Enter a 2nd number : "))

    ret = checkGreater(value1,value2)
    print(ret)

    if ret == True:
        print(value1 , "number is grater")

    else :
        print(value2 , "number is grater ")

if __name__=="__main__":
    main()