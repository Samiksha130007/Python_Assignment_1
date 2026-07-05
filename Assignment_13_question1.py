def AreaRectangle(length , width):
    return length * width
def main():
    value1 = int(input("Enter a Length : "))
    value2 = int(input("Enter a Width : "))

    ret = AreaRectangle(value1 ,value2)

    print("Area of Rectangle : ",ret)

if __name__=="__main__":
    main()