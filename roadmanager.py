from geopy.geocoders import Nominatim
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
import os

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

    checkInputs(sys.args)

    # Get user inputs
    your_roadfile = sys.argv[1]
    sheet_name = sys.argv[2]
    column_name = sys.argv[3]

    geolocator = Nominatim(user_agent=" THIS IS ROAD MANAGER")

    # Change the address to (latitude, longitude)
    for each_contents in column_contents:
        location = geolocator.geocode(each_contents)

        if location is None:
            print("No (latitude, longitude) is available at the address {}".format(
                each_contents))
            quit()

        # TODO
        print((location.latitude, location.longitude))


def checkInputs(checkInput):
    if len(checkInput) not 4:
        printError()


def returnColumn(path_your_roadfile, sheet_name, column_name, returntype=0):
    '''
    returntype = 0 : return fp, sheet_name, column_name
    returntype = 1 : return fp, sheet_name, column_contents
    '''

    # <your_roadfile.csv> <sheet_name> <column_name>
    # 1st check : if your_roadfile is vaild form
    for fp in filepaths:
        # Split the extension from the path and normalise it to lowercase.
        ext = os.path.splitext(fp)[-1].lower()

        # Now we can simply use == to check for equality, no need for wildcards.
        if ext == ".csv":
            print(fp, "is an csv!")
        elif ext == ".xlsx":
            print(fp, "is a xlsx file!")
        else:
            print(fp, "is an unknown file format.")
            print(" We allow only .csv or .xlsx files ")
            quit()

    # 2nd check : if your_roadfile has the given 'sheet_name'
    # Execl handler
    df = pd.read_excel(fp, sheetname=sheet_name)
    if df is None:
        printError()

    # 3rd check : if df has the given 'column_name' in a sheet
    # Check columns
    if column_name not in df.columns:
        printError()

    # Get the contents of the column
    # TODO Use this variable if in case it needs
    column_contents = df[column_name]

    if returntype == 0:
        return fp, sheet_name, column_name
    elif returntype == 1:
        return fp, sheet_name, column_contents
    else:
        printError()


def printError():
    print("You have to follow input rule")
    print("python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>")
    quit()


if __name__ == "__main__":
    main()
