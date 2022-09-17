from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Hogwarts School of Witchcraft and Wizardry")

myLabel = Label(root, text = "Choose your class", bg = "Green", fg = "White", cursor = "Pirate", font = "Arial").place(x = 500, y = 120)
myLabel = Label(root, text = "Sorting Hat! I choose:", bg = "Red", fg = "White", font = "Arial").place(x = 500, y = 0)

checkBox1 = Checkbutton(root, text = "Gryffindor").place(x = 500, y = 30)
checkBox2 = Checkbutton(root, text = "Hufflepuff").place(x = 500, y = 50)
checkBox3 = Checkbutton(root, text = "Ravenclaw").place(x = 500, y = 70)
checkBox4 = Checkbutton(root, text = "Slytherin").place(x = 500, y = 90)

ll = ("Defence against dark arts", "Potions", "Herbology")
val = StringVar(root)
comboBox = ttk.Combobox(root, textvariable = val, width = 30)
comboBox['values'] = ll
comboBox['state'] = 'normal'
comboBox.place(x = 500, y = 150)

txt = StringVar(root)

def fun():
    if val.get() == "Defence against dark arts":
        txt.set("Prof. Quirrell seems weird")

    if val.get() == "Potions":
        txt.set("Prof. Snape is a Snake")

    if val.get() == "Herbology":
        txt.set("Mandrakes have matured Madam Sprout")

    return None

text = Entry(root, textvariable = txt, width = 35).place(x = 500, y = 210)
myButton = Button(root, text = "Rush to your class!", command = fun).place(x = 500, y = 180)

def on_closing():
    global app_running
    if messagebox.askokcancel("Exiting the application", "Do you wish to exit the application"):
        app_running = False
        root.destroy()

app_running = True
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()