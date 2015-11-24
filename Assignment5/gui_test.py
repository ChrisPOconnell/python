__author__ = 'Chris Local'
from tkinter import *

def tutorial1():
    root = Tk() #main window
    theLabel = Label(root, text="Chris P. OConnell - Assignment 5")
    theLabel.pack()
    root.mainloop() #in infinite loop until close button is pressed

def buttonpacking():
    root = Tk() #main window
    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    button1 = Button(topFrame, text="Button1", fg="red")
    button2 = Button(topFrame, text="Button1", fg="red")
    button3 = Button(topFrame, text="Button1", fg="red")
    button1.pack()
    button2.pack()
    button3.pack()
    button4 = Button(bottomFrame, text="Button1", fg="purple")
    button4.pack()
    root.mainloop() #in infinite loop until close button is pressed

def sizes():
    root = Tk()
    label1 = Label(root,text="Name")
    label2 = Label(root,text="Password")
    entry_1 = Entry(root)
    entry_2 = Entry(root)

    label1.grid(row=0,column=0, sticky=E)
    label2.grid(row=1,column=0, sticky=E)
    entry_1.grid(row=0,column=1)
    entry_2.grid(row=1,column=1)
    root.mainloop()

sizes()
