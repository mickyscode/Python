import json
list=[]
while True:
    name=input("Please enter name")
    price=input("Please enter price")
    dictionary={"Name":name,"Price":price}
    list.append(dictionary)
    choice=input("Do you want to continue")
    if choice=="N":
        break
Filename=input("Please enter Filename")
fp=open(Filename,"w")
json.dump(list,fp)
print("List has been added")
fp.close()


