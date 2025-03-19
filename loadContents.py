import json
def loadContents():
    fp=open("JsonLibrary.json","r")
    contents=json.load(fp)
    return contents
    fp.close()
def findTotals(list):
    sum=0

    for l in list:
        sum=sum+int(l["Mark"])
    print(sum)
def updateList(list):
    rollNum=int(input("Please enter a roll Number or the student who's mark you want to update"))
    NewMark=input('Please give aa new mark for the student')
    present=False
    for i in list:

        if rollNum==i["rno"]:
            i["Mark"]=NewMark
            present=True
    if present==False:
        print("given name is not present")
    return list

# Main Code
students=loadContents()
print(students)


findTotals(students)
students=updateList(students)
print(students)
