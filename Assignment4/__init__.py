__author__ = 'ChrisPOConnell'
'''
Assignment 4
__init__.py
'''

#import Assignment3.mainmodule.menus
from menus import mainmenu
from collect_and_store import readlog, copy_spreadsheet
from collect_and_store import collectprovinces
import unittest

result = '*'
while(result != 'Q'):
    result = mainmenu()  
    if result == '1':
        collectprovinces()
    elif result == '2':
        print("this function is not yet working.")
    elif result == '3':
        copy_spreadsheet()
    elif result == '?':
        readlog()
#Feature 15, assignment 3
print("\nCome back soon!")