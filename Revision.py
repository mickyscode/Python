def Openfile(filename):
    fp=open(filename,"r")
    contents=fp.read()
    contents=contents.upper()
    print(contents)
    sentences=contents.count(".")
    print(sentences)
    fp.close()

def manageFiles(filename):
    count=0
    fp=open(filename,"r")
    info=fp.read()
    words=info.split()
    for a in words:
        if a.startswith("A"):
            count=count+1
    print(count)

def editFile(filename,sentence):
    fp=open(filename,"a")
    fp.write(sentence)
    print("File Updated")

def wordCount(filename):
    dict={}
    numOfWords=0
    fp=open(filename,"r")
    contents=fp.read()
    listOfWords=contents.split()
    for r in listOfWords:
        if r in dict.keys():
            dict[r]=dict[r]+1
        else:
            dict[r]=1
    print(dict)


#Maincode

filename=input("Please enter filename")

Openfile(filename)

filename=input('Please enter filename')
manageFiles(filename)

filename=input("Please enter filename")
sentence=input('Please enter a sentence')
editFile(filename,sentence)

filename=input("Please enter filename")
wordCount(filename)