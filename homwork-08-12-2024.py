import tkinter as tk
username="Kean"
password="Kean123"
def LoginVerification():
    if username==inputUsername.get():
        resultlbl.config(text="Username Valid")



    else:
        resultlbl.config(text="Username Invalid")
def LoginVerification2():
    if password==inputPassword.get():
        resultlbl2.config(text="Password Valid")
    else:
        resultlbl2.config(text="Password Invalid")




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
btnSubmit=tk.Button(root,text="Submit",command=lambda:[LoginVerification(),LoginVerification2()])
btnCancel=tk.Button(root,text="Cancel",command=LoginCancel)
btnClose=tk.Button(root,text="Close",command=root.destroy)
resultlbl=tk.Label(root,text=" ")
resultlbl2=tk.Label(root,text=" ")
lbllogin.grid(row=1,column=1,)
lblUsername.grid(row=2,column=1)
inputUsername.grid(row=2,column=2)
lblPassword.grid(row=3,column=1)
inputPassword.grid(row=3,column=2)
btnSubmit.grid(row=4,column=2)
btnCancel.grid(row=4,column=3)
btnClose.grid(row=5,column=2)
resultlbl.grid(row=6,column=1)
resultlbl2.grid(row=6,column=2)
root.mainloop()
