def studentList():
    dlist=[]
    while True:
        r=int(input("please enter a roll number"))
        n=input("Please enter name")
        m=int(input('Please enter mark'))
        d1={"rno":r,"Name":n,"Mark":m}
        dlist.append(d1)
        YNoption=input('Please enter yes or no if you want to continue').lower()
        if YNoption=="no":
            break
    return dlist
result=studentList()
print(result)
print("RNO   NAME   MARK")
print("==================")
for i in result:
    print(i["rno"],"   ",i["Name"],"   ",i["Mark"])
