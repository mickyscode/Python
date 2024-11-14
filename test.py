import tkinter as tk
def printResult():
    fullname=("Welcome"+" "+enterbox.get().upper()+" "+enterbox2.get().upper())

    lblresult.config(text=fullname)

root=tk.Tk()
root.geometry("300x300")
root.title("Title")

lbleng=tk.Label(root,text="First Name",bg="black",fg="white",width=25)
lbleng.pack(pady=10)
enterbox=tk.Entry(root,width=25,)
enterbox.pack(row=1,column=2pady=10)
lbleng=tk.Label(root,text="Last Name",bg="black",fg="White",width=25)
lbleng.pack(pady=10)
enterbox2=tk.Entry(root,width=25,)
enterbox2.pack(pady=10)
submitButton=tk.Button(root,text="Submit",command=printResult)
submitButton.pack(pady=10)
lblresult=tk.Label(root,text=" ")
lblresult.pack(pady=10)
root.mainloop()