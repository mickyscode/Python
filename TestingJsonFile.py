import json
def GetContents():
    Filename=input("Please enter a filename")
    fp=open(Filename,"r")
    contents=json.load(fp)
    Keys1=list((contents[0]).keys())
    print(Keys1[0], "    ",Keys1[1])
    for i in contents:
        print(i["rno"], "    ",i["Name"])
    return contents
def AddDictionary(contents):
    RollNumber=input("Please enter a roll Number")
    Name=input("Please enter a name")
    dictionary={"rno":RollNumber,"Name":Name}
    Filename=input("Please enter a filename")
    fp=open(Filename,"w")
    contents.append(dictionary)
    json.dump(contents,fp)
    fp.close()




result=GetContents()
AddDictionary(result)