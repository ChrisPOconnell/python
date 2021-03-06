__author__ = 'ChrisPOConnell'
'''
Assignment 4
start.py
Intent:  The main code had to be split from __init__.py because importing
         __init__ (which I tried in gui.py in an effort to make a start button)
         actually launched the code but not the GUI.
'''

#import Assignment3.mainmodule.menus
from menus import mainmenu
from collect_and_store import *
from under_development import *
def start():
    result = '*'
    while(result != 'Q'):
        result = mainmenu()  
        if result == '1':
            collectprovinces()
        elif result == '2':
            set_data_file_location()
        elif result == '3':
            copy_spreadsheet()
        elif result == '4': 
            get_data_file_location()
        elif result == '?':
            readlog()
        #Feature 15, assignment 3
    if(result == 'Q'):
        print("\nCome back soon!")