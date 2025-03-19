import json
def medicinelist():
    list1=[]
    while True:
        name=input("Please enter a medicine name")
        price=int(input("Please enter medicine price"))
        Contents=input("Please enter medicene contents").split()
        list1.append({"Name":name,"Price":price,"Contents":Contents})
        Choice=input("Do you want to continue?")
        if Choice=="n":
            break
    return list1
def searchMedicine(list1,m1):
    present=False
    #M1 not present
    for i in list1:
        #Each i is each dictionary in list
        if m1==i["Name"]:
            print(i["Price"],i["Contents"])
            present=True
    if present==False:
        print("Name given is not present")

def searchByContents(Cname,list1):
    Medicinelist=[]
    for i in list1:
        if Cname in i["Contents"]:
            Medicinelist.append(i["Name"])
    print(Medicinelist)



    #MainCode

result=medicinelist()
print(result)
m1=input("Please enter medicine name")
searchMedicine(result,m1)
Cname=input("Please enter a content of a medicine")
searchByContents(Cname,result)

