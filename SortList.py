mylist = [1,4,3,5,2,6,9,8,10,12,14,11,13]

for i in range(len(mylist)): #12
    for j in range(len(mylist)): #12
        if mylist[i] < mylist[j]: 
            temp = mylist[i]
            mylist[i] = mylist[j]
            mylist[j] = temp

print(mylist)