radius=float(input("Please enter a radius"))
area=2*radius*3.14
arearounded=round(area,2)
print(arearounded)

numbers=input('Please enter a list of numbers seperated by spaces').split()
print(max(numbers))
print(min(numbers))
bookd={"Chronicles of Narnia":20,"Wings of Fire":18,"Secret Garden":14,"Treasure Island":25,"Around the world in 80 days":16}
print(bookd)
print('1.Name of all books')
print('2.Search price of book when name is given')
print('3.Find total price of books')
print('4.Find name of book with minimum price')
print('5.Find name of book with maximum price')
while True:
    Menuchoice=input("Please enter the corresponding number of the choice you want on the menu").strip(".")
    if Menuchoice=="1":
        names=bookd.keys()
        print(list(names))
    elif Menuchoice=="2":
        name=input("Please enter a book's name you want the price of")
        print(bookd[name])
    elif Menuchoice=="3":
        print(sum(bookd.values()))
    elif Menuchoice=="4":
        minprice=min(bookd.values())
        for r in bookd.keys():
            if bookd[r]==minprice:
                print(r)
    elif Menuchoice=="5":
        maxprice=max(bookd.values())
        for r  in bookd.keys():
            if bookd[r]==maxprice:
                print(r)
    choice=input("Enter yes if you want to continue no if you dont").lower()
    if choice=="no":
        break




