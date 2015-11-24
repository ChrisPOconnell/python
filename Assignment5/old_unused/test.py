__author__ = 'ChrisPOConnell'
'''
Assignment 4
test.py
Intent:  This file contains a unit test to check if the
         Province.total_provinces = provnum.  This is a
         simple check but is useful because it confirms
         that the class method ncrement_master_province_count
         matches the provnum (the input entered by a user when
         asked how many provinces there are this year).
'''

#Feature 14 Assignment 4, unittest.
import unittest

class test_province_count(unittest.TestCase):
    def setUp(self):
        global provnum
        self.assertEqual(Province.total_provinces,provnum)
import curses
stdscr = curses.initscr()