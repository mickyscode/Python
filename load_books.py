def load_books():
    bookdict={}
    fp=open("Books.txt","r")
    contents=fp.readlines()
    for line in contents:
        col=line.split(",")
        Id=col[0]
        Name=col[1]
        Author=col[2]
        Available=col[3].strip("\n")
        bookdict[Id]={"title":Name,"author":Author,"available":Available}
    for i,j in bookdict.items():
        print(i,j)
    return bookdict
#   if bookdict["001"]["available"].strip()=="True":
#       print("Book is available")
#   else:
#        print("Not available >;3")
#
#
def load_userRecord():
    userdict = {}
    fp = open("userRecord.txt", "r")
    contents = fp.readlines()
    for line in contents:
        col = line.split(",")
        userID= col[0]
        bookId = col[1]
        BorrowDate = col[2]
        DueDate = col[3].strip("\n")
        userdict[userID] = {"bookId": bookId, "BorrowDate": BorrowDate, "DueDate": DueDate}
    for i,j in userdict.items():
        print(i,j)
    return userdict
bookdict={}
def add_book(bookdict):
    id=input("Please enter book id")
    title=input("Please enter book title")
    author=input("Please enter book author")
    available="True"
    bookdict[id]={"title":title,"author":author,"available":available}
    print(bookdict)
=


#main code
books=load_books()
print(books)
records=load_userRecord()
print(records)
add_book(books)