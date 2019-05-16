# import pandas as pd ## IMPORT ERROR


import sys
import os
import numpy as np

from geopy.geocoders import Nominatim
from openpyxl import load_workbook


# Hyunjae Lee is in charge

'''
<How to work>

<Usage>
 Input example  :
        python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>
 Output example :
        It will return (latitude, longitude) in the address
'''


def main():

    checkInputs(sys.argv)

    # Get user inputs
    your_roadfile = sys.argv[1]
    sheet_name = sys.argv[2]
    column_name = sys.argv[3]
    start_row = sys.argv[4]

    # Change the address to (latitude, longitude)
    your_roadfile, sheet_name = returnColumn(
        your_roadfile, sheet_name, column_name, returntype=1)

    print(your_roadfile, sheet_name)


def changeAddress(geolocator, address):

    location = geolocator.geocode(address)

    if location is None:
        print("No (latitude, longitude) is available at the address {}".format(
            location))
        quit()

    return (location.latitude, location.longitude)


def checkInputs(checkInput):
    if len(checkInput) != 5:
        printError()


def returnColumn(path_your_roadfile, sheet_name,
                 column_name, startrow=1, returntype=0):
    '''
    returntype = 0 : return fp, sheet_name, column_name
    returntype = 1 : return fp, sheet_name
    '''
    # If returntype is 1
    if returntype == 1:
        geolocator = Nominatim(user_agent=" THIS IS ROAD MANAGER")

    # <your_roadfile.csv> <sheet_name> <column_name>
    # 1st check : if your_roadfile is vaild form
    if os.path.isfile(path_your_roadfile):
        print("Correct access")
    else:
        print("[ERROR] Failed to load Excel File : %s" % (path_your_roadfile))

    # for fp in path_your_roadfile:
    #     # Split the extension from the path and normalise it to lowercase.
    #     ext = os.path.splitext(fp)[-1].lower()

    #     # Now we can simply use == to check for equality, no need for wildcards.
    #     if ext == ".csv":
    #         print(fp, "is an csv!")
    #     elif ext == ".xlsx":
    #         print(fp, "is a xlsx file!")
    #     else:
    #         print(fp, "is an unknown file format.")
    #         print(" We allow only .csv or .xlsx files ")
    #         quit()

    # 2nd check : if your_roadfile has the given 'sheet_name'
    # Execl handler
    wb = load_workbook(filename=path_your_roadfile)
    if wb is None:
        printError()

    # get the worksheet
    worksheet = wb[sheet_name]
    if worksheet is None:
        printError()

    # 3rd check : if the worksheet has the given 'column_name'
    # Check columns
    list_with_values = []

    for cell in worksheet[startrow]:
        list_with_values.append(cell.value)

    print('Your column list is {}'.format(list_with_values))
    if column_name not in list_with_values:
        printError()

    if returntype == 0:
        wb.close()
        return path_your_roadfile, sheet_name, column_name

    # 4th check : Get the contents of the given column    column_num = list_with_values.index(column_name)
    column_num = list_with_values.index(column_name)
    print('{} is located at {} column'.format(column_name, column_num+1))

    column_contents = return_column_from_excel(path_your_roadfile, sheet_name,
                                               column_num, startrow+1)

    # 5th check : Write
    for eachcell in column_contents:
        # worksheet[eachcell] = changeAddress(geolocator, worksheet[eachcell])
        print(worksheet[eachcell].value)
        # print("after ", eachcell)

    if returntype == 1:
        # save data as excel file
        # wb.save(filename='converted_' + path_your_roadfile)
        print(" Finish to save !")
        return path_your_roadfile, sheet_name
    else:
        printError()


def printError():
    print("You have to follow input rule")
    print("python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>")
    quit()


def return_column_from_excel(file_name, sheet_name, column_num, first_data_row):
    wb = load_workbook(filename=file_name)
    ws = wb[sheet_name]
    min_col, min_row, max_col, max_row = (
        column_num, first_data_row, column_num, ws.max_row)
    wb.close()
    return ws.iter_cols(min_col, min_row, max_col, max_row)


if __name__ == "__main__":
    main()
