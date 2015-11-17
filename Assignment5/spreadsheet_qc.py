import xlrd
import os.path
from db import write_filetest

files_tested = 0 #Must be present to count number of files tested.
    
def compare_spreadsheet(path, file, template):
    global files_tested
    files_tested = files_tested + 1
    file_to_test = path + file
    template_to_use = template

    #  TESTs IF FILE EXISTS
    file_exists = os.path.isfile(file_to_test)
    template_exists = os.path.isfile(template_to_use)
    if(file_exists == True and template_exists == True): 
        xl_file = xlrd.open_workbook(file_to_test)
        xl_file_sheet = xl_file.sheet_by_index(0)
        xl_file_columns = xl_file_sheet.ncols
    
        xl_template = xlrd.open_workbook(template_to_use)
        xl_template_sheet = xl_template.sheet_by_index(0)
        xl_template_columns = xl_template_sheet.ncols
    
        if (xl_file_columns == xl_template_columns):
            print("OK    - " + file + "Column numbers for match.")
            column_match = "OK"
        else:
            print("ERROR - " + file + ": Column numbers do not match.  File = " + str(xl_file_columns) + ", TEMPLATE = " + str(xl_template_columns))
            column_match = "ERROR"
            
        # Feature 25.1 Assignment 5
        write_filetest(file, column_match, "NOT BUILT YET")
    else:
        print("ERROR - " + file + ": Problem with the parameters passed for testing")


def file_count():
    print("This will count files and make sure they match!")
 
def spreadsheets_to_qc():
    global files_tested
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","AbsentAwaitingSeeking.xls", "data_files/templates/TEMPLATE_AbsentAwaitingSeeking.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","AdvisoryCommittees.xls", "data_files/templates/TEMPLATE_AdvisoryCommittees.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","AlphabeticIndex.xls", "data_files/templates/TEMPLATE_AlphabeticIndex.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","CardinalBishopPrefectApostolic.xls", "data_files/templates/TEMPLATE_CardinalBishopPrefectApostolic.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","DeceasedJesuits.xls", "data_files/templates/TEMPLATE_DeceasedJesuits.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","DepartedSociety.xls", "data_files/templates/TEMPLATE_DepartedSociety.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","FormationStatus.xls", "data_files/templates/TEMPLATE_FormationStatus.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_CDT.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_CFN.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_MAR.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_ORE.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_UCS.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_UNE.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_USA.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","IndexofHouses_WIS.xls", "data_files/templates/TEMPLATE_IndexofHouses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","Jubilarians.xls", "data_files/templates/TEMPLATE_Jubilarians.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_CDT.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_CFN.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_MAR.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_ORE.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_UCS.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")    
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_UNE.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_USA.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","MiniCatalog - GPSStreet 2016_WIS.xls", "data_files/templates/TEMPLATE_MiniCatalog - GPSStreet 2016.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","ProvCommApostolates.xls", "data_files/templates/TEMPLATE_ProvCommApostolates.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","ProvincialCommittees.xls", "data_files/templates/TEMPLATE_ProvincialCommittees.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","ProvinceAddresses.xls", "data_files/templates/TEMPLATE_ProvinceAddresses.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","ResidentsFromOtherProv.xls", "data_files/templates/TEMPLATE_ResidentsFromOtherProv.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","ResidingInOtherProvinces.xls", "data_files/templates/TEMPLATE_ResidingInOtherProvinces.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","SuperiorsByAppointment.xls", "data_files/templates/TEMPLATE_SuperiorsByAppointment.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","TranscribedInToProv.xls", "data_files/templates/TEMPLATE_TranscribedInToProv.xls")
    compare_spreadsheet("data_files/sample-reports-NOSENSITIVEINFO/","TranscribedToOther.xls", "data_files/templates/TEMPLATE_TranscribedToOther.xls")
    print(files_tested)
    files_tested = 0 #Must be at end to reset number of files tested.


