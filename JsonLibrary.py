import json
Filename=input("Please enter a filename")
fp=open(Filename,"w")
Name=input("Please enter a book name")
Price=int(input("Please enter a  book price"))
contents={"Name":Name,"Price":Price}
json.dump(contents,fp)
fp.close()
