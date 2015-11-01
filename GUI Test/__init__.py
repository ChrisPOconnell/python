# adapted from https://docs.python.org/2/library/tkinter.html

from tkinter import *

class FirstGUIDemo(Frame):  # Ed: inherits from Frame 

    def __init__(self, master=None):  #Ed: master refers to the inherited (i.e., Frame's) constructor
        Frame.__init__(self, master)  #Ed: parent's constructor; "master" is GUI framework to be used
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.HELLO_BUTTON = Button(self, text="Hello", command=self.greet)
        self.HELLO_BUTTON.pack({"side": "left"})

        self.QUIT_BUTTON = \
            Button(self, text="QUIT", fg="red", bg="blue1", command=self.quit)
        self.QUIT_BUTTON.pack({"side": "right"})

    def greet(self):  # Simple console message
        print('\n------The application has been requested to say "hello."------')


tk = Tk()  # Ed: a Tk object
app = FirstGUIDemo(master=tk)  # Ed: Frame object bound to the Tk object
