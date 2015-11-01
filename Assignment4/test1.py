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