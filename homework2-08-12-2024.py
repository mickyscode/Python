import tkinter as tk
#from tkinter import messagebox


string=""
def calculatestring(symbol):
    global string
    string=string+symbol
    textcalculator.delete(0,tk.END)
    textcalculator.insert(0,string)
def Evalstring():
    global string
    #messagebox.showinfo("string",string)
    answer=eval(string)
    textcalculator.delete(0,tk.END)
    textcalculator.insert(0,str(answer))
def ClearTextBox():
    global string
    string=""
    textcalculator.delete(0,tk.END)


root=tk.Tk()
root.geometry("175x175")
root.title("Calculator")
textcalculator=tk.Entry(root,width=20)
btnnumber1=tk.Button(root,text="1",width=5,command=lambda:calculatestring("1"))
btnnumber2=tk.Button(root,text="2",width=5,command=lambda:calculatestring("2"))
btnnumber3=tk.Button(root,text="3",width=5,command=lambda:calculatestring("3"))
btnnumber4=tk.Button(root,text="4",width=5,command=lambda:calculatestring("4"))
btnnumber5=tk.Button(root,text="5",width=5,command=lambda:calculatestring("5"))
btnnumber6=tk.Button(root,text="6",width=5,command=lambda:calculatestring("6"))
btnnumber7=tk.Button(root,text="7",width=5,command=lambda:calculatestring("7"))
btnnumber8=tk.Button(root,text="8",width=5,command=lambda:calculatestring("8"))
btnnumber9=tk.Button(root,text="9",width=5,command=lambda:calculatestring("9"))
btnnumber0=tk.Button(root,text="0",width=5,command=lambda:calculatestring("0"))
btnBracket1=tk.Button(root,text="(",width=5,command=lambda:calculatestring("("))
btnBracket2=tk.Button(root,text=")",width=5,command=lambda:calculatestring(")"))
btnnumberC=tk.Button(root,text="c",width=5,command=ClearTextBox)
btncharacter=tk.Button(root,text="=",width=5,command=Evalstring)
btncharacter1=tk.Button(root,text="+",width=5,command=lambda:calculatestring("+"))
btncharacter2=tk.Button(root,text="-",width=5,command=lambda:calculatestring("-"))
btncharacter3=tk.Button(root,text="*",width=5,command=lambda:calculatestring("*"))
btncharacter4=tk.Button(root,text="/",width=5,command=lambda:calculatestring("/"))
textcalculator.grid(row=1,column=1,columnspan=5)
btnnumber1.grid(row=2,column=1)
btnnumber2.grid(row=2,column=2)
btnnumber3.grid(row=2,column=3)
btnnumber4.grid(row=3,column=1)
btnnumber5.grid(row=3,column=2)
btnnumber6.grid(row=3,column=3)
btnnumber7.grid(row=4,column=1)
btnnumber8.grid(row=4,column=2)
btnnumber9.grid(row=4,column=3)
btnnumber0.grid(row=5,column=2)
btnBracket1.grid(row=5,column=1)
btnBracket2.grid(row=5,column=3)
btnnumberC.grid(row=6,column=2)
btncharacter.grid(row=6,column=3)
btncharacter1.grid(row=2,column=4)
btncharacter2.grid(row=3,column=4)
btncharacter3.grid(row=4,column=4)
btncharacter4.grid(row=5,column=4)
root.mainloop()