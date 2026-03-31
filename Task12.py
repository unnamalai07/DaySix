def maximini(mylist)->int:
    mylist.reverse()
    return mylist

if __name__=="__main__":
    try:
        mylist=input("Enter the commas ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(maximini(mylist))

