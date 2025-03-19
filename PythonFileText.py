def PrintFirstWord(Filename):
    fp=open(Filename,"r")
    contentString=fp.read()
    ContentList=contentString.split()
    fp.close()
    print("The first letters of each word in the file")
    for item in ContentList:
        FirstLetter=item[:1]
        print(FirstLetter)
#Main Code
Filename=input("Please enter Filename")
PrintFirstWord(Filename)

def CountFile(Filename):
    count=0
    fp=open(Filename,"r")
    contents=fp.read()
    for r in contents:
        if r==" ":
            count=count+1
    print(count)

#Main Code
Filename = input("Please enter Filename")
CountFile(Filename)


def SearchWord(Filename,Word):
    fp=open(Filename,"r")
    contents=fp.read()
    contentsList=contents.split()
    present=False
    for r in contentsList:
        if Word==r:
            print("Word given is Present")
            present=True
            break
    if present==False:
        print("Given word is not present in file")

#Main Code
Filename=input('Please enter a Filename')
Word=input("Please enter a word")
SearchWord(Filename,Word)
