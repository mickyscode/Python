import tkinter as tk
def PassOrFail():
    markENG=int(lblEngMark.get())
    markMALAYALAM=int(lblMalayalamMark.get())
    if (markENG+markMALAYALAM)/2>=50:
        resultlbl.config(text="Pass")
    else:
        resultlbl.config(text="u failed hahahah")
def ClearScreen():
    lblEngMark.delete(0,tk.END)
    lblMalayalamMark.delete(0, tk.END)

root=tk.Tk()
root.title("Result")
root.geometry("800x500")
lblEng=tk.Label(root,text="Marks of English",width=30)
lblEngMark=tk.Entry(root,width=70,)
lblMalayalam=tk.Label(root,text="Marks of Malayalam",width=30)
lblMalayalamMark=tk.Entry(root,width=70)
resultlbl=tk.Label(root,text="Result......")
btnOK=tk.Button(root,text="OK",command=PassOrFail)
btnCANCEL=tk.Button(root,text="CANCEL",command=ClearScreen)
btnclose=tk.Button(root,text="close",command=root.destroy)
lblEng.grid(row=1,column=1)
lblEngMark.grid(row=1,column=2)
lblMalayalam.grid(row=2,column=1)
lblMalayalamMark.grid(row=2,column=2,pady=30)
btnOK.grid(row=3,column=2)
btnCANCEL.grid(row=3,column=3,)
resultlbl.grid(row=4,column=1)
btnclose.grid(row=5,column=3,)
root.mainloop()
