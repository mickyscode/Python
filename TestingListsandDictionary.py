import ListandDictionary
stringlist=input("Please enter words").split()
result=ListandDictionary.converTodict(stringlist)
print(result)

dict={}


while True:
    key=input("Please enter  key")
    value=input('Please enter a value')
    dict[key]=value
    yn=input("Do you want to continue?").lower()
    if yn=="n":
        break
result2=ListandDictionary.converTolist(dict)
print(result2)

list2=input("Please enter some words").split()
result3=ListandDictionary.convertDistinctlist(list2)
print(result3)