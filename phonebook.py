import tkinter as tk
from tkinter import messagebox
phonebook={}


def AddContact():
    global phonebook
    name=nameTextBox.get()
    contact=ContactTextBox.get()
    phonebook[name]=contact
    messagebox.showinfo("phonebook",phonebook)
    nameTextBox.delete(0,tk.END)
    ContactTextBox.delete(0,tk.END)
def Cancel():
    nameTextBox.delete(0,tk.END)
    ContactTextBox.delete(0,tk.END)
def SearchContact():
    global phonebook


    Input=(NameTextBox2.get())
    Input2=phonebook[Input]
    ContactTextBox2.delete(0,tk.END)
    ContactTextBox2.insert(0,Input2)
    if Input not in phonebook:
        Response=("User Invalid")
        ContactTextBox2.insert(0,Response)
    else:
        Input = (NameTextBox2.get())
        Input2 = phonebook[Input]
        ContactTextBox2.delete(0, tk.END)
        ContactTextBox2.insert(0, Input2)





root=tk.Tk()
geometry=("500x400")
root.title("Phonebook")
nameLabel=tk.Label(root,text="Name")
nameTextBox=tk.Entry(root,width=40)
ContactLabel=tk.Label(root,text="Contact")
ContactTextBox=tk.Entry(root,width=40)
AddButton=tk.Button(root,text="ADD",command=AddContact)
CancelButton=tk.Button(root,text="Cancel",command=Cancel)
Namelabel2=tk.Label(root,text="Name")
NameTextBox2=tk.Entry(root,width=40)
SearchButton=tk.Button(root,text="Search",command=SearchContact)
ContactLabel2=tk.Label(root,text="Contact")
ContactTextBox2=tk.Entry(root,width=40)
ExitButton=tk.Button(text="Exit")
nameLabel.grid(row=1,column=1)
nameTextBox.grid(row=1,column=2)
ContactLabel.grid(row=2,column=1)
ContactTextBox.grid(row=2,column=2)
AddButton.grid(row=3,column=2)
CancelButton.grid(row=3,column=3)
Namelabel2.grid(row=4,column=1)
NameTextBox2.grid(row=4,column=2)
SearchButton.grid(row=4,column=3)
ContactLabel2.grid(row=5,column=1)
ContactTextBox2.grid(row=5,column=2)
ExitButton.grid(row=5,column=3)
root.mainloop()