import tkinter as tk
def EvenOddDecider():
    Number=int(NumberBox.get())
    if Number%2==0:
        ParityLbl.config(text="Number given is even")
    else:
        ParityLbl.config(text="Number given is odd")

root=tk.Tk()
root.title("Even odd decider")
NumberBox=tk.Entry(root,width=30)
EvenoddButton=tk.Button(root,text="Press to get number's parity",command=EvenOddDecider)
ParityLbl=tk.Label(root,text="")
NumberBox.pack(pady=60,padx=30)
EvenoddButton.pack(pady=50,padx=30)
ParityLbl.pack(pady=40,padx=30)
root.mainloop()