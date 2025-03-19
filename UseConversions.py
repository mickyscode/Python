
import fileOperations
filename=input("Please enter a file name")
result=fileOperations.fileReader(filename)
print(result)

sentence=input("Please enter a sentence")
list=fileOperations.convertToList(sentence)
print(list)

sentence2=input("Please enter another sentence")
result2=fileOperations.wordCount(sentence2)
print(result2)

list=input("Please enter a sentence").split()
dict={}
for r in list:
    count=list.count(r)
    dict[r]=count
fileOperations.mostFrequent(dict)

string2=input("Please enter something")
result3=fileOperations.letterCount(string2)
print(result3)