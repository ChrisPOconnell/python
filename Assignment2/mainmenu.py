__author__ = 'chris'

def mainmenu():
    #Intent:  To serve as a main menu for the user to select options from.
    #Definitions:
    selection = '*' #priming
    valid = 'NO'     #Used to determine if selection is valid
    valid_selection=['1','2','H','Q'] #populates a valid inputs list
    index = 0

    print("\nWelcome to the Catalog Staging Program (Version 2)\n")
    while (valid != 'OK'):
        print("\n1   Enter provinces (from scratch)")
        print("2   View provinces (from file)")
        print("H   View log of progress so far.")
        print("Q   to quit\n\n")
        selection=input("Enter your value and then press enter: ")
        for index in range(len(valid_selection)):
            print("Valid?", valid, "Selection: ",selection)
            if selection==valid_selection[index]:
                valid='OK'
            index = index+1
        if valid!='OK':
            selection='*'
            print("\nYour selection isn't valid.  Please try again.\n")
        print("OUT OF LOOP Valid?", valid, "Selection: ",selection)
    return(selection)
