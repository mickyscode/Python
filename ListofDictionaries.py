import json
fp=open("Contacts.json","r")
PhoneBook=json.load(fp)
print(PhoneBook)
PhoneBook.append({"Name":"Alice","Contact":"324324"})
fp.close()
fp=open("Contacts.json","w")
json.dump(PhoneBook,fp)
fp.close()