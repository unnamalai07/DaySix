def maximini(mylist)->int:
    mylist.sort()
    print(mylist)
    minimumnum = mylist[0]
    mylist.reverse()
    maximumnun=mylist[0]
    return maximumnun,minimumnum



if __name__=="__main__":
    try:
        mylist=input("Enter the commas ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(maximini(mylist))

