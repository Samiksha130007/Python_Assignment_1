def EvenNumbers(No):
    for i in range(2, No + 1, 2):
        print(i)

def main():
    value = int(input("Enter a number: "))
    EvenNumbers(value)

if __name__ == "__main__":
    main()