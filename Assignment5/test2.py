__author__ = 'ChrisPOConnell'
'''
Assignment 4
test2.py
This file is not used as part of the running code, it's just for testing.
I don't find Tkinter very useful as sometimes the output is put into the
console behind the GUI.  Not a very useful integration.

Intent:  This file contains a unit test to check if the
         Province.total_provinces = provnum.  This is a
         simple check but is useful because it confirms
         that the class method ncrement_master_province_count
         matches the provnum (the input entered by a user when
         asked how many provinces there are this year).
'''
from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()