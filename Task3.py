def sumofnumber(mylist)->int:
    totalvalue=0
    for x in range(0,len(mylist)):
        totalvalue=mylist[x]+totalvalue
    return totalvalue

if __name__=="__main__":
    try:
        mylist=input("Enter the values with comma ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(sumofnumber(mylist))