from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Diagnose Report")
root.geometry("550x550")
root.configure(background = "medium orchid")

q1rbtn = StringVar(value="0")
q1=Label(root,text="Do You Experience Shortness Of Breath During Routine Activities?", fg="white")
q1.pack()
q1r1 = Radiobutton(root, text = "Yes", variable = q1rbtn, value = "Yes", bg = "medium orchid")
q1r1.pack()
q1r2 = Radiobutton(root, text = "No", variable = q1rbtn, value = "No", bg = "medium orchid")
q1r2.pack()

q2rbtn = StringVar(value="0")
q2=Label(root,text="Do You Have Swelling In Your Feet/Ankles/Legs (Shoes Feel Tighter) Or Abdomen?", fg="white")
q2.pack()
q2r1 = Radiobutton(root, text = "Yes", variable = q2rbtn, value = "Yes", bg = "medium orchid")
q2r1.pack()
q2r2 = Radiobutton(root, text = "No", variable = q2rbtn, value = "No", bg = "medium orchid")
q2r2.pack()

q3rbtn = StringVar(value="0")
q3=Label(root,text="Do You Feel Any Of These Symptoms - Confusion, Disorientation Or Loss Of Memory?", fg="white")
q3.pack()
q3r1 = Radiobutton(root, text = "Yes", variable = q3rbtn, value = "Yes", bg = "medium orchid")
q3r1.pack()
q3r2 = Radiobutton(root, text = "No", variable = q3rbtn, value = "No", bg = "medium orchid")
q3r2.pack()

q4rbtn = StringVar(value="0")
q4=Label(root,text="Do You Experience Shortness Of Breath While At Rest/Lying Down?", fg="white")
q4.pack()
q4r1 = Radiobutton(root, text = "Yes", variable = q4rbtn, value = "Yes", bg = "medium orchid")
q4r1.pack()
q4r2 = Radiobutton(root, text = "No", variable = q4rbtn, value = "No", bg = "medium orchid")
q4r2.pack()

q5rbtn = StringVar(value="0")
q5=Label(root,text="Do You Experience Persistent Wheezing/Coughing That Produces White Or Pink Blood Tinged Mucus?", fg="white")
q5.pack()
q5r1 = Radiobutton(root, text = "Yes", variable = q5rbtn, value = "Yes", bg = "medium orchid")
q5r1.pack()
q5r2 = Radiobutton(root, text = "No", variable = q5rbtn, value = "No", bg = "medium orchid")
q5r2.pack()

def hdscore():
    score = 0
    if(q1rbtn.get() == "Yes"):
        score = score + 10
        print(score)
    
    if(q2rbtn.get() == "Yes"):
        score = score + 10
        print(score)
    
    if(q3rbtn.get() == "Yes"):
        score = score + 10
        print(score)
    
    if(q4rbtn.get() == "Yes"):
        score = score + 10
        print(score)
    
    if(q5rbtn.get() == "Yes"):
        score = score + 10
        print(score)
    
    if(score <= 10):
        messagebox.showinfo("Report", "You Don't Need To Visit A Doctor.")
    
    elif(score > 10 and score <= 30):
        messagebox.showinfo("Report", "You Might Perhaps Have To Visit A Doctor.")
    
    else:
        messagebox.showinfo("Report", "I Strongly Advice You To Visit A Doctor.")

btn = Button(root, text = "Show Report", command = hdscore)
btn.pack()

root.mainloop()