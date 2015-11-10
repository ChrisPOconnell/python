__author__ = 'ChrisPOConnell'
'''
Assignment 4
test1.py
This file is not used as part of the running code, it's just for testing.

Intent:  This is an exact cut and paste from StackOverflow used to generate
         one pass and one fail for a unittest.  I used to his to see if a green 
         pass bar would be generated in either PyCharm or PyDev.  In  neither
         environment does a green bar appear.
'''

from unittest.case import TestCase
import unittest
from io import StringIO
class MyTestCase(TestCase):
    def testTrue(self):
        '''
        Always true
        '''
        assert True

    def testFail(self):
        '''
        Always fails
        '''
        assert False

from pprint import pprint
stream = StringIO()
runner = unittest.TextTestRunner(stream=stream)
result = runner.run(unittest.makeSuite(MyTestCase))
print('Tests run ' + str(result.testsRun))
print('Errors ' + str(result.errors))
pprint(result.failures)
stream.seek(0)
print('Test output\n'+ stream.read())