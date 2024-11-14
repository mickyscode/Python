import tkinter as tk
import random
trials=0
score=0
def Score():
    global trials
    global score
    a=random.randint(1,21)
    Number=GuessBox.get()
    MachineBox.insert(0,str(a))
    trials=trials+1
    if a==int(Number):
        score=score+1
    UserBox.insert(0,str(score))
    TrialBox.insert(0,trials)

def Cancel():
    GuessBox.delete(0,tk.END)
    MachineBox.delete(0,tk.END)
    UserBox.delete(0,tk.END)
    TrialBox.delete(0,tk.END)

root=tk.Tk()
geometry=("500x300")
root.title=("Number game")
titleLabel=tk.Label(root,text="The Number Game")
GuessLabel=tk.Label(root,text="Guess a number between 1-20")
GuessBox=tk.Entry(root)
ScoreButton=tk.Button(root,text="Score",command=Score)
MachineLabel=tk.Label(root,text="Machine Score:")
UserLabel=tk.Label(root,text="Score:")
MachineBox=tk.Entry(root)
UserBox=tk.Entry(root)
TrialLabel=tk.Label(root,text="trials")
TrialBox=tk.Entry(root)
NextButton=tk.Button(root,text="next",command=Cancel)
titleLabel.grid(row=1,column=2)
GuessLabel.grid(row=2,column=1)
GuessBox.grid(row=2,column=2)
ScoreButton.grid(row=3,column=1)
MachineLabel.grid(row=3,column=2)
UserLabel.grid(row=4,column=2)
MachineBox.grid(row=3,column=3)
UserBox.grid(row=4,column=3)
TrialLabel.grid(row=5,column=2)
TrialBox.grid(row=5,column=3)
NextButton.grid(row=5,column=1)
root.mainloop()
