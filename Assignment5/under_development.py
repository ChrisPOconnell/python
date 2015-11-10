__author__ = 'ChrisPOConnell'
'''
Assignment 4
under_development.py
This file contains code that is not yet functional but is being worked on.
'''
#Used for get_data_file_location()
import os
import sys
import fileinput
#Used for set_data_file_location()
from os import listdir
from os.path import isfile, join


def get_data_file_location():
    # Adapted from:
    # http://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file-using-python
    # Line counter to determine what line the data_file_location: string is 
    # found on:
    line_counter = 0
    found = 0 # if this number is 1 then the value will be returned.
    
    file_to_search = 'LogFile.txt'
    temp_file = open( file_to_search, 'r+' )
    text_to_search = 'data_file_location:'

    for line in fileinput.input( file_to_search ):
        if text_to_search in line :
            #print('Match Found at line '+ str(line_counter))
            line_counter += 1
            found = 1
            break          
        else:
            #print('Match Not Found!!')
            line_counter += 1
            
    with open(file_to_search) as f:
        content = f.readlines()
        
    if(found == 1): 
        validate = validate_data_file_location(content[line_counter])
        print("validate variable" + str(validate))
        print("content[line_counter]" + content[line_counter])
        return(content[line_counter])
    else:
        return("NO")

def replace_data_file_location():
        found = get_data_file_location()
        print(found)
        if(found != 'NO'):
            print('\nAn data_file_location already exists:\n' + found + '\nDo you want to continue and replace the location? (Y/N)')
            cont = input("")
        while(cont != 'Y' and cont !='N'):
            print('Do you want to continue and replace the location? (Y/N)')
            cont = input("")
        if(cont == 'Y'):
            set_data_file_location()

def validate_data_file_location(data_file):
    data_file_location = data_file
    try:    
        file_list = [  f for f in listdir(data_file_location) if isfile(join(data_file_location,f)) ]
        valid = 'YES'
    except (FileNotFoundError):
        print("\nThis directory doesn't seem to exist...\n")
        valid = 'NO'
        
    return(valid)

