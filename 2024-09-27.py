def createListOfEmployees():
    list=[]
    while True:
        name=input('please enter a name')
        salary=int(input("Please enter a salary"))
        d={"ename":name,"salary":salary}
        list.append(d)
        YN=input("Do you want to continue?").lower()
        if YN=="no":
            break
    return list
result=createListOfEmployees()
print(result)
print("EMPLOYEE DETAILS")
print("=================")
print("NAME       SALARY")
print("=================")
for i in result:
    print(i["ename"],"     ",i["salary"])
    
