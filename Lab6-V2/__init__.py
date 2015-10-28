# DEFINITIONS

class MyException(Exception):
    error_description = "You can't divide by 0!"
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
        
def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if name_input.find('#') > -1:
        return(name_input)
    else:
        raise MyException(input_name)

# EXECUTION

def demo_exception_handling(input_name)
    try:
        get_name()
    except MyException:
        print(MyException.error_description)

demo_exception_handling(input_name)