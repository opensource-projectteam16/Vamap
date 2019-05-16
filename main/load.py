import folium
import json
import glob
import os
import os.path

# Hyunjae Lee is in charge

'''
<How to work>

<Usage>
 Input example  :
        path = os.getcwd()
        a = Load(path)
        csvLists, jsonOutputs = a.loadJson()
 Output example :
        print(csvLists)
        print(JsonLists)
'''


class Load:
    def __init__(self, path):
        self.mypath = path

    def loadJson(self):

        csvFormat = 'user_data/*.csv'
        jsonFormat = 'json/*.json'

        # Input
        csvLists = []
        jsonLists = []
        folder = []

        # Output
        csvOutputs = []
        jsonOutputs = []

        # Check root directory where 'data' folder is
        for root in os.listdir(self.mypath):

            fullPath = os.path.join(self.mypath, root)

            if not os.path.isfile(fullPath):
                folder.append(fullPath)

        # Check data directory to get .csv and .json files
        for eachDatafolder in folder:
            if eachDatafolder[-4:] == 'data':
                for filename in glob.glob(os.path.join(eachDatafolder, csvFormat)):
                    csvLists.append(filename)
                for filename in glob.glob(os.path.join(eachDatafolder, jsonFormat)):
                    jsonLists.append(filename)

        # Read .json files
        for json in jsonLists:
            readFile = open(json, 'r', encoding='utf-8').read()
            jsonOutputs.append(readFile)

        # Return path of .csv files and data of json files
        return csvLists, jsonOutputs

    def map_create_withJsons(self, jsonOutputs):
        # Default map view // need to rearrange
        Map_Object = folium.Map(
            location=[37.566345, 126.977893], zoom_start=13)

        for eachJson in jsonOutputs:
            folium.GeoJson(eachJson, name='json_data').add_to(Map_Object)

        return Map_Object

    def __str__(self):
        # For testing
        pass
