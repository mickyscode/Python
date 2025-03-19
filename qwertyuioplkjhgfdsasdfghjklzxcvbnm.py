
def SumtoLimit(limit):1
    sum=0
    for r in range(1,limit+1,1):
        sum=sum+r
    return sum
x=int(input("Please enter limit"))
sum=SumtoLimit(x)
print(sum)