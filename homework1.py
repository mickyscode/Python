import tkinter as tk
def printResult():
    mark=int(txtEng.get())
    if mark>=50:
        lblResult.config(text="Passed")
    else:
        lblResult.config(text="Failed")

root=tk.Tk()
root.geometry("300x300")
root.title("Result form")
lblEng=tk.Label(root,text="Marks of english",width=20,bg="blue",fg="White")
lblEng.pack(pady=10)
txtEng=tk.Entry(root,width=25,bg="blue",fg="white")
txtEng.pack(pady=10)
btnsubmit=tk.Button(root,text="Submit",bg="black",fg="white",command=printResult)
btnsubmit.pack(padx=10,pady=50)
lblResult=tk.Label(root,text="Result",bg="yellow",fg="red",width=20)
lblResult.pack(pady=10)
root.mainloop()