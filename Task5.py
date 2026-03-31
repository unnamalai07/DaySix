def secondmaxi(mylist)->int:
    mylist.sort()
    mylist.reverse()
    maximumnun=mylist[1]
    return maximumnun



if __name__=="__main__":
    try:
        mylist=input("Enter the commas ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(secondmaxi(mylist))

