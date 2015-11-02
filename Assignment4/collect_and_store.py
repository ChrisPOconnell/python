__author__ = 'ChrisPOConnell'
'''
Assignment 4
collect_and_store.py
Intent:  This file contains code to collect data and read/write files.
from test.test_univnewlines import DATA_CR
'''
import time
import xlrd
import xlwt
from classes import Province
#import test
from test import test_province_count
#Used for set_data_file_location()
from os import listdir
from os.path import isfile, join



#from classes import TestProvince

def collectprovinces():
    #intent: collect provinces and perform basic quality assurance.
    #Feature 7 found in assignment 2, turn collection into function.
    provnum = 0
    provlist = list()
    while provnum < 3 or provnum > 10:
        #Feature 9 found in assignment 2, correct error where invalid input causes
        #program to cease operations.
        #Feature 10 found in assignment 2, trap errors.
        try:
            provnum=eval(input("How many Provinces are in this year's catalog?  "))
            if provnum < 3 or provnum > 10:
                print("Please enter a single digit number between 3 and 10 ")
        except (SyntaxError,NameError):
            print("Please enter a single digit number between 3 and 10  ")
    
    print("\nGreat, you have",provnum,"Provinces to work with this year.  That should be easy :)\n")
    print("Next let's collect the 3 letter Province abbreviations.")
    indx = 0
    while (indx< provnum):
        prov = input("Please enter the three digit Province abbreviation, then press ENTER:  ")
        if len(prov) != 3:
            print("Sorry, the Province abbreviation must be 3 letters!")
        elif len(prov) == 3:
            location = input("Lovely, what's the location for that office? ")
            comment = input("What comments do you have about this office? ")
            #feature 4 found in assignment 2, convert to upper.
            provlist.append(prov.upper())
            pr = Province(provlist[indx],location,comment)
            #I'm replacing the simple value of province abbreviation with the enter collected
            #string in the provlist here.  The value of the objects will replace the abbreviation.
            provlist[indx] = str(pr)
            #Feature 17, Assignment 3, use of a class method to update a class variable.
            Province.increment_master_province_count()
            indx= indx+1
    #Feature 5 found in assignment 2, sort provinces alphabetically
    provlist.sort()
    print("\nThe provinces you entered are:\n")
    for index in range(len(provlist)):
            print(provlist[index])
    a = test_province_count()
    input("\nPress ENTER to continue...")
      
    #TestProvince.testcount(provnum=provnum)
    #Feature 6, write provinces to file
    fileW = open('LogFile.txt', 'w')
    #Feature 11, Assignment 3 (also related to feature 6 of assignment 1)
    now = time.strftime("%c")
    fileW.write("Province Entry Date:\n")
    fileW.write(now)
    fileW.write('\nProvinces:\n')
    for index in range(len(provlist)):
        fileW.write(provlist[index])
        fileW.write("\n")
    fileW.close();

def readlog():
    #Intent: Read contents of log file and display them
    #Feature 8 found in assignment 2, read file and display
    #Feature 10 found in assignment 2, trap errors.
    try:
        fileR = open('LogFile.txt')
        log = fileR.read()
        print("\nHere's what you've got so far:\n")
        print(log)
    except FileNotFoundError:
        print("\nLooks like the file you need hasn't been built yet.\n")
        print("Please enter the provinces again.")
    input("\nPress ENTER to continue...")

def copy_spreadsheet():
    #Opens file and reads some data out:
    path="C:/Users/Chris Local/OneDrive/Github/python/Assignment4/"
    xl_read = xlrd.open_workbook(path+"data_files/Book1.xls")
    print(xl_read.sheet_names()[0])
    xlr_sheet = xl_read.sheet_by_index(0)
    xlr_nrows = xlr_sheet.nrows
    xlr_ncols = xlr_sheet.ncols
    print(xlr_sheet)
    print("Rows " + str(xlr_nrows))
    print("Columns " + str(xlr_ncols))
    
    #Creates files and copies data over
    xl_write = xlwt.Workbook()
    xl_sheet = xl_write.add_sheet(xl_read.sheet_names()[0])
    input("\nPress ENTER to continue...")
    
# Feature 22 Assignment 4
def set_data_file_location():
    valid = 'NO'
    data_file_location = ""
    # Adapted directory pull from:
    # http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
            
    while(valid == 'NO'):
        print("Enter the folder name that your data set is in. (Note, dataset must be found in data_files/ folder) (Q to quit):")
        data_file_location = input("")
        if(data_file_location != 'Q'):
            data_file_location = "data_files/" + data_file_location
            # Feature 22.1 Assignment 4
            try:    
                file_list = [  f for f in listdir(data_file_location) if isfile(join(data_file_location,f)) ]
                valid = 'YES'
            except (FileNotFoundError):
                print("\nThis directory doesn't seem to exist...\n")
                valid = 'NO'
                
        if(data_file_location != 'Q' and valid != 'NO'):              
            file_list = [  f for f in listdir(data_file_location) if isfile(join(data_file_location,f)) ]
            valid = 'YES'
            print("\nOK, the location is: " + data_file_location)
            print("This folder contains: " + str(len(file_list)) + " files.\n")
            print("Do you want to save path to the log file? (Y/N)\n")
            save_to_file = input("")
            if(save_to_file == 'Y'):
                fileW = open('LogFile.txt', 'a')
                fileW.write("\ndata_file_location:\n" + data_file_location)
                fileW.close()
                    
        if(data_file_location != 'Q'):
            if(valid != 'NO'):
                input("\nPress ENTER to continue...\n")
        else:
            valid = 'YES'