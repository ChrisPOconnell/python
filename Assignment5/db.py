import sqlite3
import os.path

# Feature 25 Assignment 5
def create_db():
    # Intent:  Check if database exists.
    # Postcondition 1: If database doesn't exist create it.
    # Postcondition 2: If database exists notify user.
    exists = os.path.isfile("data_files/results.db")
    if(exists == False):    
        conn = sqlite3.connect("data_files/results.db")
        cursor = conn.cursor()
        #return conn, cursor
        a_num_fields = 3
        a_table_name = 'FILE_RESULTS'
        creation_str = 'CREATE TABLE ' + a_table_name + '(file_name, column_num_match, headers_match, date_time)'
        print(creation_str)
        cursor.execute(creation_str)
        conn.commit() # save changes
        print('table ' + a_table_name + ' created')
    else:
        print("Database is existing already")

create_db()
