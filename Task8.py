def negativenumber(mylist)->list:
    allnumber=[]
    for x in range(0,len(mylist)):
            allnumber.append(mylist[x])
    return allnumber

if __name__=="__main__":
    try:
        mylist=input("Enter thevalues with comma : ")
        mylist=list(map(int, mylist.split(",")))
    except Exception as e:
        print (str(e))
    print(negativenumber(mylist))
    

    
        