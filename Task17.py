# Write a Python Program to delete all duplicate elements from an list.
def removeDuplicate(mylist) ->list: 
    try :
        removedDuplicate = []
        for i in mylist:
            if i not in removedDuplicate:
                removedDuplicate.append(i)
        return removedDuplicate
    except Exception as e :
        print(f"Error in the Remove Duplicates : {str(e)}")
        return []

if __name__=="__main__":
    try:
        mylist=input("Enter the values with commas : ")
        mylist=list(map(int,mylist.split(",")))
    except Exception as e:
        print(str(e))
    print(removeDuplicate(mylist))