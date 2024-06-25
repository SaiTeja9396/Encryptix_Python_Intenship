from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Password Generator")
root.geometry("600x400")
root.config(background="#f0f0f0") 

def gen():
    global sc1
    sc1.set("")
    passw = ""
    length = int(c1.get())
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + lowercase
    mixs = '0123456789' + lowercase + uppercase + '!@#$%^&*()-=_+,./?><;:"[]\\|}{'
    if c2.get() == 'Low Strength':
        for i in range(length):
            passw = passw + random.choice(lowercase)
        sc1.set(passw)
    elif c2.get() == 'Medium Strength':
        for i in range(length):
            passw = passw + random.choice(uppercase)
        sc1.set(passw)
    elif c2.get() == 'High Strength':
        for i in range(length):
            passw = passw + random.choice(mixs)
        sc1.set(passw)

sc1 = StringVar(root)

t1 = Label(root, text="Python Password Generator", font=("Arial", 18, "bold"), fg="#333", bg="#f0f0f0")
t1.place(x=140, y=20)

t2 = Label(root, text="Password:", font="Arial")
t2.place(x=145, y=250)
i1 = Entry(root, font=("Arial", 14), textvariable=sc1, width=25)
i1.place(x=250, y=250)

t3 = Label(root, text="Length:", font="Arial")
t3.place(x=145, y=90)
c1 = Entry(root, font=("Arial", 14), width=10)
c1.place(x=220, y=90)

t4 = Label(root, text="Strength:", font="Arial")
t4.place(x=145, y=150)
c2 = ttk.Combobox(root, font=("Arial", 14), width=15)
c2['values'] = ('Low Strength', 'Medium Strength', 'High Strength')
c2.current(1)
c2.place(x=235, y=150)

b = Button(root, text="Generate", font=("Arial", 14, "bold"), fg="white", bg="#4CAF50", command=gen)
b.place(x=290, y=200)

root.mainloop()
