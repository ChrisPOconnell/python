__author__ = 'Chris Local'
__author__ = 'ChrisPOConnell'
'''
Assignment 5
thread.py
'''

import sys
def print_there(m):
     sys.stdout.write("Download progress: %s  \r" % m)
     sys.stdout.flush()
import os

os.times()

i = 0
'''while(i < 100000000):
     i = i + 1
     m = str(os.times())
     print_there(m)
'''
import os
#print(os.times())
m = str(os.times())
#>>> print os.times.__doc__
#times() -> (utime, stime, cutime, cstime, elapsed_time)#
#Return a tuple of floating point numbers indicating process times.

import time, sys

def cpu_counter():
     while (1 > 0):
          m = str(os.times())
          sys.stdout.write(m + " \r")
          sys.stdout.flush()