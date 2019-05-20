# 3rd parties
import pandas as pd
import sys
import os
# developed modules
from main.parser import parser, checkArgument
from main.load import Load
from main.map3d import Map3d, TileLayer3d
from main.marker_func import Make_Default_Markers, Make_Value_Markers
from preprocessing.scoring import Scoring

# Hyunjae Lee is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''


# MAIN


def main():
    # path
    path = os.getcwd()

    # parsing setup.txt
    '''
    Sungjae Min is in charge

    when user hits 'python main.py setup.txt',
    arg = .... (read the content of setup.txt)
    coverage , weights = parser(arg, path)

    '''

    # arg = checkArgument(sys.argv)
    print(parser(path))
    # coverage, user_data, roads, others = parser(path)
    #    arg = checkArgument(sys.argv)
    coverage = 5000

    user_data = ['seoulbikeinfo_test.xlsx', 'Excel_Import_1', '위도', '경도']
#    roads = {'1) 0.3' : ['road_test.xlsx', 'road_2', 'x', 'y', 'start_x', 'start_y', 'end_x', 'end_y', 'value', 4]}
    roads = {}
    others = {'1) 0.2' : ['seoul_building_1_test.xlsx', 'building_2', 'x', 'y', 'value', 3],'2) 0.5' : ['seoul_building_1_test.xlsx', 'building_3', 'x', 'y', 'value', 4]}

    # TODO Check error handling is working well.
    print(coverage, user_data, roads, others)

    # Load csv, json files
    load_instance = Load(path)
    csvLists, jsonOutputs = load_instance.loadJson()
    Map_Object = load_instance.map_create_withJsons(jsonOutputs)

    # print(csvLists)
    # Data processing

    #   Sangmin Lee is in charge
    preprocessing = Scoring(coverage, user_data, roads, others)

    #    [if you need]
    #    //return_values  = preprocessing.function_name(...)

    scored_user_data, scored_roads, scored_others = preprocessing.valueScore()

    print('main', scored_user_data)

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load custom marker icon

    # Load default markers (roads, buildings, subways)
    # Make_Default_Markers(Map_Object, scored_roads, scored_others)

    # Load value markers and circlemarker based on user input
    # (calculated by 'scoring')
    # Make_Value_Markers(Map_Object, scored_user_data,, coverage)

    # Add choropleth
    # Map_Object.choropleth(

    # )

    # Save as html file

    # Map_Object.save('MAP.html')


if __name__ == "__main__":
    main()
