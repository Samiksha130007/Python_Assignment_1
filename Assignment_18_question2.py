def maximum(Data):
    max =Data[0]

    for i in Data:
        if i> max:
            max=i
    return max


def main():
    Data =[]
    n=int(input("how many number do yo want to enter:"))

    for i in range(n):
        value= int(input("enter a number :"))
        Data.append(value)

    print("List : ",Data)

    ret =maximum(Data)
    print("Maximum : ", ret)
if __name__=="__main__":
    main()