__author__ = 'ChrisPOConnell'
'''
Assignment 5
gui.py
'''

from tkinter import *
import thread
import sys
import os
from multiprocessing import Process
from tkinter import Tk, Checkbutton, Label
from tkinter import StringVar, IntVar

class MainMenu:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        # Configure label for CPU counter/thread
        self.m = StringVar()
        self.m.set("CPU COUNTER GOES HERE")
        self.label_cpu = Label(frame, textvariable = self.m)
        self.button1 = Button(frame, text = "1. Enter Provinces (from Scratch)")
        self.label_cpu.grid(row=1, sticky = W)
        self.button1.grid(row=2, sticky = W)

    def cpu_counter(self):
       while (1 > 0):
            v = str(os.times())
            print(v)
            self.m.set(v)

def cpu_counter_external(GUI):
    GUI.cpu_counter()

if __name__ == '__main__':
    root = Tk()
    menubar = Menu(root)
    menubar.option_add('*tearOff', FALSE)
    submenu = Menu(menubar)
    menubar.add_cascade(label = "File!", menu = submenu)
    menubar.add_cascade(label = "Help!", menu = submenu)
    root.config(menu=menubar)
    GUI = MainMenu(root)
    p = Process(target = GUI.cpu_counter)

    #The following line, GUI.cpu_counter() updates the label
    #but it should not be run unless in a process.
    #GUI.cpu_counter()

    p.start()
    p.join()
    root.mainloop()



