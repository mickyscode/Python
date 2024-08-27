students={"Kean":99,"Aditi":87,"Janvi":76}
def DisplayNames():
    print("List of students",list((students.keys())))
DisplayNames()
def HighMark():
    print("Highest Mark is",max(students.values()))
HighMark()
def LowMark():
    print("Lowest Mark is",min(students.values()))
LowMark()
def AverageMark():
    print("Average Mark is",sum(students.values())/len(students.keys()))
AverageMark()
def NewMark():
    student=input("Enter a student name who's mark you want to change")
    mark=int(input("Enter a new Mark"))
    if student not in list(students.keys()):
        print("Student name given is Unavailable")
    else:
        students[student]=mark
        print(students)
NewMark()
def DeleteDetails():
    Name=input("Please enter a student name who's info you want to delete")
    if Name not in list(students.keys()):
        print("Student name given is Unavailable")
    else:
        del students[Name]
        print(students)
DeleteDetails()
