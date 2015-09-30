__author__ = 'chris'

def mainmenu():
    #Definitions:
    selection = "*" #priming
    valid = ""     #Used to determine if selection is valid
    valid_selection='1','2','?','Q' #populates a valid inputs list

    print("\nWelcome to the Catalog Staging Program (Version 2)\n")
    while (selection == "*"):
        print("\n1   Enter provinces")
        print("2   View provinces")
        print("?   View log of progress so far.")
        print("Q   to quit\n\n")
        selection=input("Enter your value and then press enter: ")
        for index in range(len(valid_selection)):
            if selection==valid_selection[index]:
                valid="OK"
        if valid!="OK":
                selection="*"
        print("Valid?", valid, "Selection: ",selection)
    return(selection)
