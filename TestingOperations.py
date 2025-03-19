import tkinter as tk
from tkinter import messagebox
import Operations
def Calculate(op):
    x=int(textbox1.get())
    y=int(textbox2.get())
    if op=="+":
        messagebox.showinfo(Operations.add(x,y))
    elif op=="-":
        messagebox.showinfo(Operations.subtract(x,y))
    elif op=="*":
        messagebox.showinfo(Operations.multiply(x,y))
    elif op=="/":
        messagebox.showinfo(Operations.division(x,y))
root=tk.Tk()
root.title("Operations")
root.geometry("500x300")

label1=tk.Label(root,text="Enter a number",width=20)
textbox1=tk.Entry(root,width=20)
label2=tk.Label(root,text="Enter a second number",width=20)
textbox2=tk.Entry(root,width=20)
AddButton=tk.Button(root,text="add",width=10)
SubtractButton=tk.Button(root,text="subtract",width=10)
MultiplyButton=tk.Button(root,text="Multiply",width=10)
DivisionButton=tk.Button(root,text="Divide",width=10)
CancelButton=tk.Button(root,text="Cancel",width=20)
label1.grid(row=2,column=1,pady=10)
textbox1.grid(row=2,column=3,pady=10)
label2.grid(row=3,column=1,pady=10)
textbox2.grid(row=3,column=3,pady=10)
AddButton.grid(row=4,column=1,pady=10,padx=10,command=Calculate("+"))
SubtractButton.grid(row=4,column=2,pady=10,padx=10,command=Calculate("-"))
MultiplyButton.grid(row=4,column=3,pady=10,padx=10,command=Calculate("*"))
DivisionButton.grid(row=4,column=4,pady=10,padx=10,command=Calculate("/"))
CancelButton.grid(row=5,column=4,pady=10)
root.mainloop()