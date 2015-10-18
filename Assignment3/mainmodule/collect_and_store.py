__author__ = 'ChrisPOConnell'
'''
Assignment 3
'''
import time
from classes import Province

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
                print("Great, you have",provnum,"Provinces to work with this year.  That should be easy :)\n")
        except (SyntaxError,NameError):
            print("Please enter a single digit number between 3 and 10  ")

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
            provlist[indx] = str(pr)
            indx= indx+1
    #Feature 5 found in assignment 2, sort provinces alphabetically
    #provlist.sort()
    print("\nThe provinces you entered are:\n")
    for index in range(len(provlist)):
            print(provlist[index])
    input("\nPress ENTER to continue...")
    
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

