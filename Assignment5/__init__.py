__author__ = 'ChrisPOConnell'
'''
Assignment 4
__init__.py
'''

from menus import mainmenu
from collect_and_store import *
from under_development import *
from spreadsheet_qc import *
from build_and_verify import compare_files
from db import *

def start():
    result = '*'
    while(result != 'Q'):
        result = mainmenu()  
        if result == '1':
            collectprovinces()
        elif result == '2':
            set_data_file_location()
        elif result == '3':
            spreadsheets_to_qc()
            input("\nPress ENTER to continue...")
        elif result == '4': 
            get_data_file_location()
        elif result == '5':
            compare_files()
            input("\nPress ENTER to continue...")
        elif result == '6':
            read_filetest()
            input("\nPress ENTER to continue...")
        elif result == '7':
            purge_filetest()
            input("\nPress ENTER to continue...")
        elif result == '?':
            readlog()
        #Feature 15, assignment 3
    if(result == 'Q'):
        print("\nCome back soon!")
        
start()