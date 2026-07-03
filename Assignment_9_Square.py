def square(No):
    return No * No
def main():
    value = int(input("Enter a number :"))

    ret= square(value)

    print("Square is : ",ret)

if __name__=="__main__":
    main()