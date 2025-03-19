import math
x=math.sqrt(25)
print(x)
def squareroot(lowerlimit,upperlimit):
    for r in range(lowerlimit,upperlimit+1,1):
        x=math.sqrt(r)
        print(r,"=",round(x,2))
lowerlimit=int(input("Enter first number"))
upperlimit=int(input("Enter limit"))
squareroot(lowerlimit,upperlimit)

def kmM_conversion(km):
