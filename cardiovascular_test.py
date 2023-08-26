from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Cardiovascular Test")
root.configure(background = "pink")

heading = Label(root, text = "Cardiovascular Test")
heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)

q1_radiobutton = StringVar(value = '0')

q1_label = Label(root, text = "Do you experience shortness of breath during routine activities?")
q1_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)
q1_radiobutton1 = Radiobutton(root, text = "yes", variable = q1_radiobutton, value = "yes")
q1_radiobutton2 = Radiobutton(root, text = "no", variable = q1_radiobutton, value = "no")
q1_radiobutton1.place(relx = 0.5, rely = 0.225, anchor = CENTER)
q1_radiobutton2.place(relx = 0.5, rely = 0.250, anchor = CENTER)


q2_radiobutton = StringVar(value = '0')

q2_label = Label(root, text = "Do you have swelling in the feet/ankles/legs or abdomen?")
q2_label.place(relx = 0.5, rely = 0.325, anchor = CENTER)
q2_radiobutton1 = Radiobutton(root, text = "yes", variable = q2_radiobutton, value = "yes")
q2_radiobutton2 = Radiobutton(root, text = "no", variable = q2_radiobutton, value = "no")
q2_radiobutton1.place(relx = 0.5, rely = 0.350, anchor = CENTER)
q2_radiobutton2.place(relx = 0.5, rely = 0.375, anchor = CENTER)

q3_radiobutton = StringVar(value = '0')

q3_label = Label(root, text = "Do you feel any of these sympotms - confusion, disorientation or loss of memory?")
q3_label.place(relx = 0.5, rely = 0.425, anchor = CENTER)
q3_radiobutton1 = Radiobutton(root, text = "yes", variable = q3_radiobutton, value = "yes")
q3_radiobutton2 = Radiobutton(root, text = "no", variable = q3_radiobutton, value = "no")
q3_radiobutton1.place(relx = 0.5, rely = 0.450, anchor = CENTER)
q3_radiobutton2.place(relx = 0.5, rely = 0.475, anchor = CENTER)

q4_radiobutton = StringVar(value = '0')

q4_label = Label(root, text = "Do you experience shortness of breath while at rest/lying down?")
q4_label.place(relx = 0.5, rely = 0.525, anchor = CENTER)
q4_radiobutton1 = Radiobutton(root, text = "yes", variable = q4_radiobutton, value = "yes")
q4_radiobutton2 = Radiobutton(root, text = "no", variable = q4_radiobutton, value = "no")
q4_radiobutton1.place(relx = 0.5, rely = 0.550, anchor = CENTER)
q4_radiobutton2.place(relx = 0.5, rely = 0.575, anchor = CENTER)

q5_radiobutton = StringVar(value = '0')

q5_label = Label(root, text = "Do you experience persistent wheezing/coughing that produces white/pink blood tinged mucus?")
q5_label.place(relx = 0.5, rely = 0.650, anchor = CENTER)
q5_radiobutton1 = Radiobutton(root, text = "yes", variable = q5_radiobutton, value = "yes")
q5_radiobutton2 = Radiobutton(root, text = "no", variable = q5_radiobutton, value = "no")
q5_radiobutton1.place(relx = 0.5, rely = 0.675, anchor = CENTER)
q5_radiobutton2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def sick():
    score = 0
    if q1_radiobutton.get() == "yes":
        score = score + 5
    if q1_radiobutton.get() == "no":
        score = score
    
    if q2_radiobutton.get() == "yes":
        score = score + 5
    if q2_radiobutton.get() == "no":
        score = score
    
    if q3_radiobutton.get() == "yes":
        score = score + 5
    if q3_radiobutton.get() == "no":
        score = score
    
    if q4_radiobutton.get() == "yes":
        score = score + 5
    if q4_radiobutton.get() == "no":
        score = score 
 
    
    if q5_radiobutton.get() == "yes":
        score = score + 5
    if q5_radiobutton.get() == "no":
        score = score
    
    if score <= 5:
        print(score)
        messagebox.showinfo("Result", "You don't need to see a doctor.")
    
    elif score <= 10 and score <=15:
        print(score)
        messagebox.showinfo("Result", "You might need to see a doctor if these symptoms get worse.")
    
    else: 
        print(score)
        messagebox.showinfo("Result", "You need to see a doctor immediately! Get well soon")
    
button_result = Button(root, text = "Result", command = sick)
button_result.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()
        
    
