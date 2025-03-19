import json
Filename=input("Please enter Filename")
fp=open(Filename,"r")
contents=json.load(fp)
for n in contents:
    print(n.values())
    values=list(n.values())
    Name=values[0]
    NameBigger=Name.upper()
    print(NameBigger)
fp.close()