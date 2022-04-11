# Program 2. Create a program to produce the interface: (Hint: After typing your full name in the first entry field widget, the bottom entry field will show your full name after clicking the button - 50 points)
from tkinter import *

midterm=Tk()
midterm.title("Midterms in OOP")
label = Label( text="Enter your Full Name :", fg="blue", font=40)
label.grid(row=0, column=0)
label = Label( text="", font=40)
label.grid(row=1, column=0)

text = Entry(midterm)
text.grid(row=0, column=1)

def process():
    text.insert(0, "")
    magic = Label(label2, text=text.get())
    magic.pack()


button = Button(midterm, text="Click to Display Full Name :", fg="blue", font=40, command=process)
button.grid(row=1, column=0)

label2 = Label(midterm)
label2.grid(row=1, column=1)

midterm.mainloop()