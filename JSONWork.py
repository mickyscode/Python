import json
def studentList():
    list1=[]
    while True:
        Name=input("Please give a  student name")
        Marks=list(map(int,input("Please give a list of marks seperated by spaces").split()))
        list1.append({"Name":Name,"Marks":Marks})
        AddMore=input("Do you want to continue").lower()
        if AddMore=="no":
            break
    return list1
result1=studentList()
print(result1)