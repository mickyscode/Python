
list=[1,2,3,4,5,6,7,8,9,10]
list2=[i for i in list]
print(list2)
list3=[l*l for l in range(1,11)]
print(list3)
list4=[a*a*a for a in list]
print(list4)
dict={}
n=int(input("Please enter a number"))
listnum=[h for h in range(1,n+1)]
for r in listnum:
    value=r*r
    dict[r]=value
print(dict)
import math
list5=[2**b for b in range(1,6)]
print(list5)
x=int(input("Please enter number"))
y=int(input("Please enter number"))
list6=[round(math.sqrt(c),2) for c in range(x,y+1)]
print(list6)
n=int(input('Please enter number'))
list7=[6*d for d in range(1,n+1)]
print(list7)

l1=list(map(int,input("Please enter a list of numbers seperated by space...OR ELSE").split()))
l2=[x for x in l1 if x%2!=0]
print(l2)
l3=[y for y in l1 if y%2==0]
print(l3)
l4=[p for p in l1 if p>=0]
print(l4)
l5=[n for n in l1 if n<0]
print(l5)
l6=[x for x in l1 if x%5==0]
print(l6)

names=input("Please enter list of names").split()
listnames=[x for x in names if len(x)>=3]
listreverse=[y[::-1] for y in names]
print(listnames)
print(listreverse)

y={y for y in range(1,11)}
print(y)


