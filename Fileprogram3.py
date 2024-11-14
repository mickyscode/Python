"""
fp=open("File1.txt","r")
s=fp.readlines()
print(len(s))
for i in range(len(s)):
    s[i]=s[i].strip("\n")
print(s)
fp.close()

"""
"""
def countWord(filename):
    d={}
    file1=open(filename,"r")
    l=file1.read()
    l=l.split()
    for i in l:
        a=l.count(i)
        d[i]=a
    return(d)
filename=input('Please enter a filename')
result1=countWord(filename)
print(result1)
"""
"""
filename2=input('Please enter a filename')
contents=input("Please enter what you would want to put in file")
fp=open(filename2,"a")
fp.write(contents)
fp.close()
def updateFile(file1,file2):
    fp=open(file1,"r")
    contents=fp.read()
    fp.close()
    fp=open(file2,"a")
    fp.write(contents)
    fp.close()
file1=input('Please enter a file')
file2=input('Please enter a file')
updateFile(file1,file2)

def copyFile(filename1,filename2):
    fp=open(filename1,"r")
    contents=fp.read()
    fp.close()
    fp2=open(filename2,"w")
    fp2.write(contents)
    print("File copied")
    fp2.close()
filename1=input("Please enter a filename who's contents will be copied to another file")
filename2=input('Please enter another filename')
copyFile(filename1,filename2)

def manageFile(filename):
    fp=open(filename,"r")
    contents=fp.read().split()
    fp.close()
    sum=0
    for i in contents:
        if i.startswith("A"):
            sum=sum+1
    return sum
filename=input("Please enter file name")
result1=manageFile(filename)
print("Number of words that start with A is",result1)
def MergeFile(file1,file2,file3):
    fp=open(file1,"r")
    contents=fp.read()
    fp.close()
    fp2=open(file2,"r")
    contents2=fp2.read()
    fp2.close()
    contents3=contents+" "+contents2
    fp3=open(file3,"w")
    fp3.write(contents3)
    fp3.close()
    print("File Is merged")
file1=input("Please enter a file")
file2=input("Please enter a file")
file3=input("PLease enter a file")
MergeFile(file1,file2,file3)
"""

def Movie_Genre(file):
    d={}
    fp=open(file,"r")
    contents=fp.readlines()
    fp.close()
    for r in contents:
        list=r.split("|")
        moviename=list[2].strip("\n")
        movietype=list[0]
        d[moviename]=movietype
    return d


def read_genre_movie(filename):
    d={}
    fp=open(filename,"r")
    contents1=fp.readlines()
    for i in contents1:
        list1=i.split("|")
        movieGenre=list1[0]
        movieName=list1[2].strip("\n")
        if movieGenre not in d.keys():
            d[movieGenre]=[movieName]

        else:
            d[movieGenre].append(movieName)
    return d
filename=input('Please enter a filename')
GenreMovieDict=read_genre_movie(filename)
print(GenreMovieDict)
MovieGenreDict=Movie_Genre(filename)
print(MovieGenreDict)
"""
def wordCount(filename):
    d={}
    fp=open(filename,"r")
    l=fp.read()
    l=l.split()
    for i in l:
        a=l.count(i)
        d[i]=a
    fp.close()
    print(d)

filename=input('Please enter a filename')
wordCount(filename)
"""




