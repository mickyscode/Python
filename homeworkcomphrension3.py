"""
list=map(int,input("Please enter a list of numbers seperated by space").split())
list2=[r for r in list if r%2==0]
print(list2)

list3=input("please enter some words seperated by space").split()
list4=[i[0] for i in list3]
list5=[a[::-1] for a in list3]
print(list4)
print(list5)
list6=[b*b for  b in range(1,101)]
print(list6)
"""
list7=input('Please enter list of words').split()
list8=[c for c in list7 if len(c)>=3]
print(list8)
