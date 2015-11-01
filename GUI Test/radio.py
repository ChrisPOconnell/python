__author__ = 'ebraude'
# Copied or adapted from
# http://www.python-course.eu/tkinter_radiobuttons.php
from tkinter import *

root = Tk()

# Selection text at beginning of UI
Label(root,
        text='Choose your language:',
        justify=LEFT,
        padx=20).pack()

language_selection = [
    ("English", 0),
    ("French", 1),
    ("Italian", 2),
    ("Spanish", 3),
    ("Chinese", 4),
]

integer_representing_language = IntVar()  # Ed: defined in tkinter
integer_representing_language.set(0)  # initializing choice, i.e. English


def display_choice():
    # Post: thank you message is on console corresponding to language_selection

    thank_you_message = ["Thanks for choosing English",
            "Merci d'avoir choisi Francais",
            "Grazie per aver scelto italiane",
            "Gracias por haber elegido Espanol",
            "Ni Hao Ma"]
    print('--->' +
          thank_you_message[integer_representing_language.get()] + '<---')


# Radiobuttons for each element of languages are in UI
for txt, val in language_selection:
    Radiobutton(root,
            text=txt,  # begins with "English"
            padx=20,
            variable=integer_representing_language,
            value=val,  # begins with 0
            command=display_choice).pack(anchor=W) #called with val of intVar

mainloop()
