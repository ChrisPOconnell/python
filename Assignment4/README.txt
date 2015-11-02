
REQUIREMENTS:
\python35\scripts\pip install xlwt
\python35\scripts\pip install xlrd
xlutils needs to be installed, but this doesn't work well through pip.

FILE LOCATIONS:
data_files/templates:   A set of known good templates that future proofing files
                        should be compared to.

data_files/Book1.xls:   A sample file with which to test xlwt and xlrd.

data_files/Proof[X]:    Where X is the proof number and date.  For example:
                        data_files/Proof1_09162015.  Files that are being
                        compared or corrected should be placed here.

REPORTING INFORMATION:
The formula for each report should be:
provnum*2+16.  In other words, there are two reports that need to run for each
province and 16 reports to be run that cover all provinces.  

DATA_FILE_LOCATION FUNCTIONS:
From the main menu replace_data_file_location() is called
replace_data_file_location() -> get_data_file_location()
