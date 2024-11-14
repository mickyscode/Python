d1={"a":1,"b":2,"c":3}
print(max(d1.values()))
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[i*i for i in l1]
print(l2)
x={"A":100,"b":90,"C":80,"d":70,"E":70,"f":60,"G":50}
x1={}
keys=x.keys()
values=x.values()
print(max(values))
for a in x.keys():
    b=a.upper()
    print(b)
    x1[b]=x[a]
print(x)
print(x1)
