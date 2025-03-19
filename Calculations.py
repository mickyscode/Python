def converTodict(string):
    dict={}
    listOfstrings=string.split()
    for item in listOfstrings:
        if item in dict.keys():
            dict[item]=dict[item]+1
        else:
            dict[item]=1
    return dict
def vowelDict(string2):
    vowelDictionary={}
    listOfstrings2=string2.split()
    for item2 in string2:
        if item2 in "aeiouAEIOU":
            if item2 in vowelDictionary.keys():
                vowelDictionary[item2]=vowelDictionary[item2]+1
            else:
                vowelDictionary[item2]=1

    return vowelDictionary

