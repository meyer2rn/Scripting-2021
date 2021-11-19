#Python Program to convert USD to different currencies using Tkinter

from tkinter import *

#this creates a GUI Window
window = Tk()

#Function to convert USD to Euro (EUR), Yen (JPY), Pound (GBP), and Australian Dollar (AUD)
def from_usd():
    # USD to Euro (EUR)
    euro = float(e2_value.get())*.88
    # USD to Yen (JPY)
    yen = float(e2_value.get())*114.28
    # USD to Pound (GBP)
    pound = float(e2_value.get())*.74
    # USD to Australian Dollar (AUD)
    dollar = float(e2_value.get())*1.37

    #Enters converted currency to text widget
    t1.delete("1.0", END)
    t1.insert(END,euro)

    t2.delete("1.0", END)
    t2.insert(END,yen)

    t3.delete("1.0", END)
    t3.insert(END,pound)

    t4.delete("1.0", END)
    t4.insert(END,dollar)

#Creates label widgets
e1 = Label(window, text = "Enter the amount in USD", font="bold")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value, bg="yellow",)
e3 = Label(window, text = '€ Euro')
e4 = Label(window, text = '¥ Yen')
e5 = Label(window, text = '£ Pound')
e6 = Label(window, text = '$ Australian Dollar')

#Creates text widgets
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
t4 = Text(window, height = 1, width = 20)

#Creates button widgets
b1 = Button(window, text = "Convert", command = from_usd, bg='red')

#Creates table structure
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)
e6.grid(row = 1, column = 3)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)
t4.grid(row = 2, column = 3)
b1.grid(row = 0, column = 2)

#Start GUI
window.mainloop()