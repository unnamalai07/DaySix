mylist=[0,1,2,3]
def newvalue(value)->list:
        mylist.append(value)
        return mylist

if __name__=="__main__":
    try:
        num=int(input("Enter the value "))
    except Exception as e:
        print (str(e))
    print(newvalue(num))
    

    
        