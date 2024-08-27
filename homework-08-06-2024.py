import tkinter as tk

def ConvertResult():
    CMinput=int(lblcmInput.get())
    Mnumber=(str(CMinput/100)+" "+"Metres")
    lblresult.config(text=Mnumber)
root=tk.Tk()
root.geometry("300x300")
root.title("cm to m convertor")
lblcm=tk.Label(root,text="Centimetres")
lblcmInput=tk.Entry(root,text="Type here")
btnsubmit=tk.Button(root,text="Convert",command=ConvertResult)
lblresult=tk.Label(root,text=" ")
lblcm.grid(row=1,column=1)
lblcmInput.grid(row=1,column=2)
btnsubmit.grid(row=2,column=1)
lblresult.grid(row=3,column=1)
root.mainloop()



