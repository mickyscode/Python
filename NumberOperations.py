"""
def Factorial(num):
    product=1
    for n in range(1,num+1):
        product=product*n
    return product

def createBooks():
    bookdict={}
    while True:
        name=input("Please enter a book name")
        author=input("Please enter the book's author")
        bookdict[name]=author
        choice=input("Do you want to continue n for no and y for yes")
        if choice=="n":
            break
    return bookdict
def updateBooks(dictionary):
    name2=input("Please enter a book name")
    if name2 not in dictionary.keys():
        print("Given book title is not present in library")
    else:
        author=input("Please enter the book's author")
        dictionary[name2]=author
    return dictionary
result=createBooks()
print(result)
result2=updateBooks(result)
print(result2)
"""
def removeList(list):
    item=input("Enter an item you want to remove")
    if item not in list:
        print("Item given is not in list")
    else:
        list.remove(item)
    return list
list=input("Please enter a sentence seperated by spaces").split()
result=removeList(list)
print(result)
