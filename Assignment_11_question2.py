def Count(No):
    count=0
    while No>0:
        count=count+1
        No=No//10
    return count
def main():
    value  =int(input("Enter a number : "))
    ret = Count(value)
    print("count is : ",ret)

if __name__=="__main__":
    main()
