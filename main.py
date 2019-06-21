# 3rd parties
import pandas as pd
import sys
import os
import folium

# developed modules
from choropleth import choropleth
from main.parser import parser, checkArgument, printparser
from main.load import Load
from main.basemap3D import Map3D
from main.marker_func import Make_Default_Markers, Make_Value_Markers
from preprocessing.scoring import Scoring

''' 
How to work
Usage 
 Input example  
 Output example 
'''


# MAIN


def main():

    path = os.getcwd()

    arg = checkArgument(sys.argv)
    coverage, user_data, roads, others, executefile , userselect_coor = parser(path)
    printparser(coverage, user_data, roads, others, executefile , userselect_coor)

    # Load csv, json files
    load_instance = Load(path)
    csvLists, jsonOutputs = load_instance.loadJson()
    Map_Object = load_instance.map_create_withJsons(jsonOutputs)

    # Data processing
    preprocessing = Scoring(coverage, user_data, roads, others)
    scored_user_data, scored_roads, scored_others = preprocessing.valueScore()

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load default markers (roads, buildings, subways)
    Make_Default_Markers(Map_Object, scored_roads, scored_others, path)

    # Load value markers and circlemarker based on user input
    # (calculated by 'scoring')
    Make_Value_Markers(Map_Object, scored_user_data, coverage, path)

    # TODO 3D MAP
    #New3dMap = Map3D(scored_user_data)
    #New3dMap.draw3dMap()

    # Add choropleth
    choropleth(Map_Object)

    # Save as html file
    Map_Object.save('MAP.html')


if __name__ == "__main__":
    main()
