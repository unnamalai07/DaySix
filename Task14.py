mylist=["Unna","Thiru"]
def findelements(value)->bool:
    for x in range(0,len(mylist)):
        if mylist[x].lower()==value.lower():
            return True
    return False

if __name__=="__main__":
    try:
        value=str(input("Enter the values "))
    except Exception as e:
        print(str(e))
    print(findelements(value))