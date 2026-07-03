def cube(No):
    return No * No * No
def main():
    value = int(input("Enter a number :"))

    ret= cube(value)

    print("cube is : ",ret)

if __name__=="__main__":
    main()