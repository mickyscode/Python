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
    if bookdict["001"]["available"].strip()=="True":
        print("Book is available")
    else:
        print("Not available >;3")


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



#main code
load_books()
load_userRecord()

