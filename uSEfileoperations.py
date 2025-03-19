import fileOperations
filename=input("Please enter filename")
contentStr=fileOperations.fileReader(filename)
print(contentStr)

wordlist=fileOperations.convertToList(contentStr)
print(wordlist)

countdict=fileOperations.wordCount(wordlist)
print(countdict)


frequentword=fileOperations.mostFrequent(countdict)
print(frequentword)