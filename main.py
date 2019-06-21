# 3rd parties
import pandas as pd
import sys
import os
# developed modules
from main.parser import parser, checkArgument, printparser
from main.load import Load
from main.map3d import Map3d, TileLayer3d
from main.marker_func import Make_Default_Markers, Make_Value_Markers
from preprocessing.scoring import Scoring
import numpy as np
import vincent
import folium
import json

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

    arg = checkArgument(sys.argv)
    coverage, user_data, roads, others = parser(path)
    printparser(coverage, user_data, roads, others)


    # TODO Check error handling is working well.

    # Load csv, json files
    load_instance = Load(path)
    csvLists, jsonOutputs = load_instance.loadJson()
    Map_Object = load_instance.map_create_withJsons(jsonOutputs)

    # print(csvLists)
    # Data processing

    #   Sangmin Lee is in charge
    preprocessing = Scoring(coverage, user_data, roads, others)

    # #    [if you need]
    # #    //return_values  = preprocessing.function_name(...)

    scored_user_data, scored_roads, scored_others = preprocessing.valueScore()

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load custom marker icon

    # Load default markers (roads, buildings, subways)
    Make_Default_Markers(Map_Object, scored_roads, scored_others, path)

    # Load value markers and circlemarker based on user input
    # (calculated by 'scoring')
    Make_Value_Markers(Map_Object, scored_user_data, coverage, path)

    # Add choropleth
    # Map_Object.choropleth(

    # )

    #Save as html file

    Map_Object.save('MAP.html')

    incover = preprocessing.return_incover()

    k=0;
    popup = list()
    x =[]
    y =[]
    for data in incover:
        if data != list() :
            for i in data:
                x.append(i[0])
                y.append(i[1])
            npx = np.array(x)
            npy = np.array(y)

            scatter_points = {
                'x': npx,
                'y': npy,
            }

            scatter_chart = vincent.Scatter(scatter_points,
                                            iter_idx='x',
                                            width=600,
                                            height=300)

            scatter_json = scatter_chart.to_json()
            scatter_dict = json.loads(scatter_json)


            popup = folium.Popup(max_width=650)
            folium.Vega(scatter_dict, height=350, width=650).add_to(popup)
            folium.Marker([scored_user_data[k][0], scored_user_data[k][1]], popup=popup).add_to(Map_Object)
            k+=1;

        else :
            k+=1;
        Map_Object.save('MAP.html')

if __name__ == "__main__":
    main()
