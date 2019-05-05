# 3rd parties
import pandas as pd

# developed modules
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

    # Default map view
    Map_Object = folium.Map(location=[37.566345, 126.977893], zoom_start=17)

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load custom marker icon

    # Load default markers (roads, buildings, subways)
    Make_Default_Markers(Map_Object, roads, buildings, subways)

    # Load value markers and circlemarker based on user input (calculated by 'scroing')
    Make_Value_Markers(MapObejct, user_data, coverage)

    # Add choropleth
    # Map_Object.choropleth(

    # )
    # Save as html file

    Map_Object.save('MAP.html')


if __name__ == "__main__":
    main()
