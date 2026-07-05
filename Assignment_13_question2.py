def AreaCircle(Radius,Pi=3.14):
    return Radius * Radius * 3.14
def main():
    value = int(input("Enter a number : "))
    
    ret = AreaCircle(value)

    print("Area of circle  : ",ret)

if __name__=="__main__":
    main()