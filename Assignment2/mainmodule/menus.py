__author__ = 'chris'
'''
Assignment 2
I'm having a problem where I try to modularize this program by putting the mainmenu()
function into a file called menus.py.  The function is imported in __init__.py.
For some odd reason this causes the mainmenu() function to run repeatedly, even after it
should exit.

While I was hoping to have this working at the time Assignment 2 was submitted
I wasn't able to get it working.
'''


def mainmenu():
    #Intent:  To serve as a main menu for the user to select options from.
    #Definitions:
    selection = '*' #priming
    valid = 'NO'     #Used to determine if selection is valid
    valid_selection=['1','2','?','Q'] #populates a valid inputs list
    index = 0
    print("\nWelcome to the Catalog Staging Program (Version 2)\n")
    while (valid != 'OK'):
        print("\n1   Enter provinces (from scratch)")
        print("2   View provinces (from file)")
        print("?   View log of progress so far.")
        print("Q   to quit\n\n")
        selection=input("Enter your value and then press enter: ")
        for index in range(len(valid_selection)):
            #print("Valid?", valid, "Selection: ",selection)
            if selection==valid_selection[index]:
                valid='OK'
            index = index+1
        if valid!='OK':
            selection='*'
            print("\nYour selection isn't valid.  Please try again.\n")
        #print("OUT OF LOOP Valid?", valid, "Selection: ",selection)
    return(selection)

def collectprovinces():
    #intent: collect provinces and perform basic quality assurance.
    #Feature 7 found in assignment 2, turn collection into function.
    provnum=0
    provlist=list()
    while provnum < 3 or provnum >10:
        #Feature 9 found in assignment 2, correct error where invalid input causes
        #program to cease operations.
        try:
            provnum=eval(input("How many Provinces are in this year's catalog?  "))
            if provnum < 3 or provnum > 10:
                print("Great, you have",provnum,"Provinces to work with this year.  That should be easy :)\n")
        except SyntaxError:
            print("Please enter a single digit number between 3 and 10  ")
            #print("Please enter a single digit number between 3 and 10  ")
        except NameError:
            print("Please enter a single digit number between 3 and 10  ")
            #print("Please enter a single digit number between 3 and 10  ")

    print("Next let's collect the 3 letter Province abbreviations.")
    indx=0
    while (indx< provnum):
        prov=input("Please enter the three digit Province abbreviation, then press ENTER:  ")
        if len(prov)!=3:
            print("Sorry, the Province abbreviation must be 3 letters!")
        elif len(prov)==3:
            #feature 4 found in assignment 2, convert to upper.
            provlist.append(prov.upper())
            indx= indx+1
    #Feature 5 found in assignment 2, sort provinces alphabetically
    provlist.sort()
    print(provlist)
    #Feature 6, write provinces to file
    fileW = open('LogFile.txt', 'w')
    fileW.write('Provinces:\n')
    for index in range(len(provlist)):
        fileW.write(provlist[index])
        fileW.write("\n")
    fileW.close();

result=mainmenu()
if result == '1':
    collectprovinces()
elif result == '2':
    print("this function is not yet working.")
elif result =='?':
    print("this function is not yet working.")
elif result =='Q':
    print("this function is not yet working.")


