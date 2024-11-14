import tkinter as tk
def printResult():
    fullname=("Welcome"+" "+enterbox.get().upper()+" "+enterbox2.get().upper())

    lblresult.config(text=fullname)

root=tk.Tk()
root.geometry("300x300")
root.title("Title")

lbleng=tk.Label(root,text="First Name",bg="black",fg="white",width=25)
enterbox=tk.Entry(root,width=25,)
lbleng1=tk.Label(root,text="Last Name",bg="black",fg="White",width=25)
enterbox2=tk.Entry(root,width=25,)
submitButton=tk.Button(root,text="Submit",command=printResult)
lblresult=tk.Label(root,text=" ")
lbleng.grid(row=1,column=1)
enterbox.grid(row=1,column=2)
lbleng1.grid(row=2,column=1)
enterbox2.grid(row=2,column=2)
submitButton.grid(row=3,column=2,)
lblresult.grid(row=4,column=1,padx=20)
root.mainloop()