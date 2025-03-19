def CreateDict():
    dict={}
    while True:
        Student=input("Enter student name")
        Score=int(input("Enter student test score"))
        dict[Student]=Score
        AddMore=input("Do you want to add a student's score and name?").lower()
        if AddMore=="no":
            break
    return dict
def CalcResult(dict):
    Scores=dict.values()
    TopMark=max(Scores)
    for key,value in dict.items():
        if value==TopMark:
            print(key)
#MainCode
Result1=CreateDict()
print(Result1)

CalcResult(Result1)
