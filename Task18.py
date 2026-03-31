# Write a Python Program to count total number of duplicate elements in an list.
def totalNumberOfDuplicate(mylist) ->list: 
    try :
        removedDuplicateCount = 0
        for i in mylist:
            if mylist.count(i)>1:
                removedDuplicateCount = removedDuplicateCount+1
    except Exception as e :
        print(f"Error in the Remove Duplicates : {str(e)}")
        return  None

if __name__=="__main__":
    try:
        mylist=input("Enter the values with commas : ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(totalNumberOfDuplicate(mylist))         