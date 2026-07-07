def ChkNumber(No):
    return No
def main():
    value = int(input("Enter a number : "))

    ret = ChkNumber(value)

    if ret == 0:
        print("Zero")

    elif ret > 0:
        print("Positive Number ")

    else:
        print("Negative Number ")

if __name__=="__main__":
    main()