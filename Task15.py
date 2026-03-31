def ascending(mylist)->int:
    mylist.sort()
    mylist.reverse()
    return mylist

if __name__=="__main__":
    try:
        mylist=input("Enter the values with commas ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(ascending(mylist))

