import tkinter as tk
from tkinter import messagebox
username="Kean"
password="Kean123"
def LoginVerification():
    if username==inputUsername.get() and password==inputPassword.get():
        messagebox.showinfo("login","Login Succesful")


    else:
        messagebox.showinfo("login","Failed loser now spend 10 minutes Trying to remember")





def LoginCancel():

    inputUsername.delete(0,tk.END)
    inputPassword.delete(0,tk.END)

root=tk.Tk()
root.geometry("500x300")
root.title("Login")
lbllogin=tk.Label(root,text="Login")
lblUsername=tk.Label(root,text="Username")
inputUsername=tk.Entry(root)
lblPassword=tk.Label(root,text="Password")
inputPassword=tk.Entry(root)
btnSubmit=tk.Button(root,text="Submit",command=LoginVerification)
btnCancel=tk.Button(root,text="Cancel",command=LoginCancel)
btnClose=tk.Button(root,text="Close",command=root.destroy)
lbllogin.grid(row=1,column=1,)
lblUsername.grid(row=2,column=1)
inputUsername.grid(row=2,column=2)
lblPassword.grid(row=3,column=1)
inputPassword.grid(row=3,column=2)
btnSubmit.grid(row=4,column=2)
btnCancel.grid(row=4,column=3)
btnClose.grid(row=5,column=2)
root.mainloop()
