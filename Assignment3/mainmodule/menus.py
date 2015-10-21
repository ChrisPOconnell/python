__author__ = 'ChrisPOConnell'
'''
Assignment 3
menus.py
'''
import time
#import unittest
def mainmenu():
    #Intent:  To serve as a main menu for the user to select options from.
    #Definitions:
    selection = '*' #priming
    valid = 'NO'     #Used to determine if selection is valid
    valid_selection=['1', '2', '?', 'Q'] #populates a valid inputs list
    print("\nWelcome to the Catalog Staging Program (Version 3)\n")
    while (valid != 'OK'):
        print("1   Enter provinces (from scratch)")
        print("2   View provinces (from file)")
        print("?   View log of progress so far.")
        print("Q   to quit\n")
        selection = input("Enter your value and then press enter: ")
        for index in range(len(valid_selection)):
            if selection == valid_selection[index]:
                valid = 'OK'
        if valid != 'OK':
            selection = '*'
            print("\nYour selection isn't valid.  Please try again.\n")
    return(selection)



