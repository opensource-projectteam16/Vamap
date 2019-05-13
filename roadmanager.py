from geopy.geocoders import Nominatim
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import sys
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

    # Execl handler
    df = pd.read_excel(your_roadfile, sheetname=sheet_name)
    if df is None:
        print("You have to follow input rule")
        print("python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>")
        quit()

    # Check columns
    if column_name not in df.columns:
        print("You have to follow input rule")
        print("python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>")
        quit()

    # Get the contents of the column
    column_contents = df[column_name]
    if column_contents is None:
        print("You have to follow input rule")
        print("python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>")
        quit()

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
        print("You have to follow input rule")
        print("python roadmanager.py <your_roadfile.csv> <sheet_name> <column_name>")
        quit()


if __name__ == "__main__":
    main()
