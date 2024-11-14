"""
list=list(map(int,input("Please enter a list of numbers seperated by spaces").split()))
d={i:i*i for i in list}
print(d)

list=input('Please enter a sentence').split()
d={i:len(i) for i in list}
print(d)
"""
def createListstudents():
    studentlist=[]
    while True:
        name=input('Please enter a name')
        mark=int(input("Please enter mark"))
        list=[name,mark]
        studentlist.append(list)
        yn=input("Do you want to continue(n for no and y for yes)")
        if yn=="n":
            break
    return studentlist
list1=createListstudents()
print(list1)
for i in list1:
    print(i)
