def negativenumber(mylist)->list:
    negativelist=[]
    for x in range(0,len(mylist)):
        if mylist[x]<0:
            negativelist.append(mylist[x])
    return negativelist

if __name__=="__main__":
    try:
        mylist=input("Enter thevalues with comma : ")
        mylist=list(map(int, mylist.split(",")))
    except Exception as e:
        print (str(e))
    print(negativenumber(mylist))    