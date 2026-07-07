def display(No):
    for i in range(No , 0 ,-1):
        for j in range(i):
            print("*",end=" ")
        print()
def main():
    Value = int(input("Enter a number : "))
    display(Value)

if __name__ == "__main__":
    main()
