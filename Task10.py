mylist=[7,9,6,5]
def removevenumber(num)->list:
    if len(mylist)>=num:
        mylist.pop(num)
        return mylist
    else:
        return "Invalid Input"
if __name__=="__main__":
    try:
        num=int(input("Enter the index of remove number : "))
    except Exception as e:
        print (str(e))
    print(removevenumber(num))
    