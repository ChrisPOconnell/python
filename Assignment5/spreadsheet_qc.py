import xlrd

def compare_spreadsheet(file, template):
    file_to_test = file
    template_to_use = template
    #  TESTs IF FILE EXISTS
    
    xl_file = xlrd.open_workbook(file)
    xl_file_sheet = xl_file.sheet_by_index(0)
    xl_file_columns = xl_file_sheet.ncols
    
    xl_template = xl_file.open_workbook(template)
    xl_template_sheet = xl_template.sheet_by_index(0)
    xl_template_columns = xl_template_sheet.ncols
    if 
 
compare_spreadsheet("data_files/templates/TEMPLATE_AbsentAwaitingSeeking", "data_files/templates/TEMPLATE_AbsentAwaitingSeeking")
        