"""
def sumUptoN(limit):
    sum=0
    for r in range(1,limit+1,1):
        sum=sum+r
    return sum
limit=int(input("Please enter a limit"))
limit2=int(input("Please enter another limit"))
answer1=sumUptoN(limit)
answer2=sumUptoN(limit2)
answer3=answer1/answer2
print(answer3)

def multiTable(value):
    for r in range(1,12+1,1):
        answer=value*r
        print(answer)
value=int(input("Please enter a number to find its table"))
multiTable(value)
"""
def isPassed():
    sciencemarks=int(input("Please enter science marks"))
    mathsmarks=int(input("Please enter maths marks"))
    englishmarks=int(input("Please enter english marks"))
    if (sciencemarks+mathsmarks+englishmarks/3)>=40:
        print("passed")
    else:
        print("FAILED XD")
isPassed()
