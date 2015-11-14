import xlrd
import os.path
from os import listdir

proof_path = "C:/Users/Chris Local/OneDrive/Github/python/Assignment5/data_files/sample-reports-NOSENSITIVEINFO"

def define_files():    
    # First range is columns, should always be 2
    # Second range is number of total reports, which should be PROVNUM * 2 + 16
    files_totest = [[[] for i in range(2)] for i in range(2)]
    files_totest.extend("AbsentAwaitingSeeking.xls")
    files_totest.extend("data_files/templates/TEMPLATE_AbsentAwaitingSeeking.xls")
    files_totest.extend("AdvisoryCommittees.xls")
    files_totest.extend("data_files/templates/TEMPLATE_AdvisoryCommittees.xls")
    
    print(files_totest)
       
    return(files_totest)

def compare_files():
    # Feature 26 Assignment 5, two sets and compare.
    files_existing = set(listdir(proof_path))
    try:
        files_totest = define_files()
    except():
        print("\nERROR - The file list build failed.")
    files_totest_list = list()
    for r, c in files_totest:
        files_totest_list.append(r)
        files_totest_set = set(files_totest_list)

    try:
        comparison = set(files_existing) == set(files_totest_set)
        if(comparison == True):
            print("\nOK    - The file names tested matches the file names in the directory.")
        else:
            print("\nERROR - The file names tested don't match the file names in the directory")
    except (TypeError):
        print("\nERROR - There's some error with the sets...")
        
    if(len(files_existing) == len(files_totest_list)):
        print("OK    - The number of files tested matches the number of existing files")
        print("        Existing: " + str(len(files_existing)) + " Tested: " + str(len(files_totest_list)))

    else:
        print("ERROR - The number of files tested doesn't match the number of existing files")
        print("        Existing: " + str(len(files_existing)) + " Tested: " + str(len((files_totest))))

compare_files()
