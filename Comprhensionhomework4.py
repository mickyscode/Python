list={a for a in range(1,11)}
print(list)
list2={b*b for b in range(1,11)}
print(list2)
list3=map(int,input('Please enter numbers seperated by spaces').split())
list4={c*c*c for c in list3}
print(list4)