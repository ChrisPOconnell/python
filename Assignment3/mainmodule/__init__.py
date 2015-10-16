__author__ = 'chris'
#import Assignment3.mainmodule.menus
from menus import mainmenu
from menus import readlog
from menus import collectprovinces
import unittest

result='*'
while(result!='Q'):
    result=mainmenu()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(result,"1" or "2" or "?" or "Q")
    if result == '1':
        collectprovinces()
    elif result == '2':
        print("this function is not yet working.")
    elif result =='?':
        readlog()
print("\nCome back soon!")