"""
x=int(input("Please enter a number"))
y=int(input("please enter a number"))
list1=[r*r*r for r in range(x,y+1)]
set1={i*i*i for i in range(x,y+1)}
print(list1)
print(set1)
"""
sentence=input("Please enter a sentence")
list2=[a for a in sentence]
list3=[b.upper() for b in sentence]
print(list2)
print(list3)