__author__ = 'ChrisPOConnell'
'''
Assignment 3
'''

#import Assignment3.mainmodule.menus
from menus import mainmenu
from collect_and_store import readlog
from collect_and_store import collectprovinces
import unittest

result = '*'
while(result != 'Q'):
    result = mainmenu()
    class TestMainmenu(unittest.TestCase):
        def test(self):
            self.assertEqual(result, "1" or "2" or "?" or "Q")
    
    
    if result == '1':
        collectprovinces()
    elif result == '2':
        print("this function is not yet working.")
    elif result == '?':
        readlog()
#Feature 15, assignment 3
print("\nCome back soon!")