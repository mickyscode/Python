def createEmployee():
    employeeList=[]
    while True:
        name=input("please enter a name")
        salary=int(input("Please enter a salary"))
        sublist=[name,salary]
        employeeList.append(sublist)
        yesno=input("Do you want to continue?(y for yes and n for no)")
        if yesno=="n":
            return employeeList

def searchEmployee(employeeList):
    name2=input("Please enter a name")
    p=False
    for i in employeeList:
        if i[0]==name2:
            p=True
            print(i[i])
    if p==False:
        print("Name is not avalaiable")
        








#main code
finalList=createEmployee()
print(finalList)
searchEmployee(finalList)






