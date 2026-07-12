def minimum(Data):
    min =Data[0]

    for i in Data:
        if i< min:
            min=i
    return min


def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))

    for i in range(n):
        value= int(input("enter a number :"))
        Data.append(value)

    print("List : ",Data)

    ret =minimum(Data)
    print("Minimum : ", ret)
if __name__=="__main__":
    main()