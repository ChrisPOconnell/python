__author__ = 'ChrisPOConnell'
'''
Assignment 3
Feature 16, Assignment 3, completed 10/18/2015
'''

class Province:
        def __init__(self,name="",office_location="DEFAULT",comments="Default Comment"):
            self.name = name
            self.office_location = office_location
            self.comments = comments
        def __str__(self):
            return(self.name + ":" + self.office_location + ":" +self.comments)