# Find the odd or even in the list 
def oddOrEven(mylist) -> int:
    evenlist=0
    oddlist=0
    for x in range(0,len(mylist)):
        if mylist[x]%2 == 0:
            evenlist=evenlist+1
        else:
            oddlist=oddlist
    return evenlist,oddlist

if __name__ == "__main__":
    try:
        mylist = input("Enter numbers separated by commas: ")
        mylist = list(map(int, mylist.split(',')))
    except Exception as e :
        print(f"Error in the Getting the user input : {str(e)}")
    print(oddOrEven(mylist))

