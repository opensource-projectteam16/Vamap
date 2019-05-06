# 3rd parties
import pandas as pd

# developed modules
from main.load import Load
from main.parser import Parser
from main.map3d import Map3d, TileLayer3d
from main.marker_func import Make_Default_Markers, Make_Value_Markers
from dataprocessing.scoring import scoring

# Hyunjae Lee , Sungjae Min is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''

# MAIN


def main(self):

    # path
    path = os.getcwd()

    # parsing setup.txt
    '''
    Sungjae Min is in charge
    '''

    # Load csv, json files
    load_instance = Load(path)
    csvLists, jsonOutputs = load_instance.loadJson()
    Map_Object = load_instance.map_create_withJsons(jsonOutputs)

    # Data processing
    '''
    Sangmin Lee is in charge
    preprocessing = Scoring(inputs(if you need))
    
    [if you need]
    //return_values  = preprocessing.function_name(...)
    
    roads, buildings, subways, user_data = preprocessing.scoring(inputs(if you need))
    '''

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load custom marker icon

    # Load default markers (roads, buildings, subways)
    Make_Default_Markers(Map_Object, roads, buildings, subways)

    # Load value markers and circlemarker based on user input
    # (calculated by 'scoring')
    Make_Value_Markers(Map_Object, user_data, coverage)

    # Add choropleth
    # Map_Object.choropleth(

    # )

    # Save as html file

    Map_Object.save('MAP.html')


if __name__ == "__main__":
    main()
