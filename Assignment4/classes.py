__author__ = 'ChrisPOConnell'
'''
Assignment 4
classes.py
Feature 16, Assignment 3, completed 10/18/2015
Feature 17, Assignment 3, completed 10/19/2015
Feature 17, Assignment 3, use of a class method to update a class variable.
'''
import unittest
#from other_functions import *

class Province:
        master_province_count = 0
        total_provinces = master_province_count
        def __init__(self,name="",office_location="DEFAULT",comments="Default Comment"):
            self.name = name
            self.office_location = office_location
            self.comments = comments
        def __str__(self):
            return(self.name + ":" + self.office_location + ":" +self.comments)
  
  #Feature 18, Assignment 3, use of a class method to update a class variable.      
        @classmethod
        def increment_master_province_count(cls):
                Province.total_provinces+= 1

