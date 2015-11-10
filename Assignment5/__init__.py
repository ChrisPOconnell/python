__author__ = 'ChrisPOConnell'
'''
Assignment 4
__init__.py
'''

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
        
start()