
def fileReader(filename):
    fp=open(filename,"r")
    contents=fp.read()
    return contents

def convertToList(sentence):
    wordlist=sentence.split()
    return wordlist


def wordCount(words):
    dict={}
    for word in words:
        if word in dict.keys():
            dict[word]=dict[word]+1
        else:
            dict[word]=1
    return dict

def mostFrequent(dict):
    mostCount=max(list(dict.values()))
    value_to_find=mostCount
    for key,value in dict.items():
        if value==value_to_find:
            return key
def letterCount(string2):
    lettercount=len(string2)
    return lettercount
