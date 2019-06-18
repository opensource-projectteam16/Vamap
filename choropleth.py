import folium
import pandas as pd
from branca.colormap import linear
import os
import main

def choropleth(Map_Object):
    path = os.getcwd()
    states = path + "/data/json/skorea-municipalities-2018-geo.json"
    print(states)

    folium.GeoJson(
        states,
        style_function=lambda feature: {
            'fillColor': '#ffff00',
            'color': 'black',
            'weight': 2,
            'dashArray': '5,5'
        }
    ).add_to(Map_Object)



if __name__ == "__main__":
    choropleth()