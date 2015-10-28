__author__ = 'ChrisPOConnell'
'''
Lab 6 - Exceptions
Project: Lab6-V3
'''

# DEFINITIONS

class MyException(Exception):
    #Intent:  Return a string indicating that no #'s are allowed.
    #Precondition:  Must be called in an except.
    #Postcondition: Shows error message.
    error_description = "No #'s Please!"
    #def __init__(self):
    def __str__(self):
        return repr(self.value)
        
def get_name():
    #Intent: Collects name and checks for #'s.
    #Postcondition 1:  If no #'s are found returns name.
    #Postcondition 2:  If #'s are found throws MyException.
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if name_input.find('#') == -1:
        return(name_input)
    else:
        raise MyException()

# EXECUTION
def demo_exception_handling():
    #Intent:  Tries get_name().  
    #Postcondition 1: Prints returned name_input.
    #Postcondition 2: Displays exception text. 
    try:
        print(get_name())
    except MyException:
        print(MyException.error_description)

#Simply calls function.
demo_exception_handling()