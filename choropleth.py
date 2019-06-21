import folium
import pandas as pd
from branca.colormap import linear
import pandas as pd
import os
import main

def choropleth(Map_Object):
    path = os.getcwd()

    # path of json file
    states = path + "/data/json/skorea-municipalities-2018-geo.json"

    # path of sample unemployment csv file
    unemployment = path + "/data/unemployment.csv"
    unemployment_file = pd.read_csv(unemployment)
    print(unemployment_file.head)

    unemployment_dict = unemployment_file.set_index('State')['Unemployment']
    colormap = linear.YlGn_09.scale(
        unemployment_file['Unemployment'].max(),
        unemployment_file['Unemployment'].min())
    color_dict = {key: colormap(unemployment_dict[key]) for key in unemployment_dict.keys()}

    folium.GeoJson(
        states,
        style_function=lambda feature: {
            'fillColor': '#ffff00',#color_dict[feature['id']],
            'color': 'black',
            'weight': 1,
            'dashArray': '5,5',
            'fill0pacity': 0.9,
        }
    ).add_to(Map_Object)

    # Navigation button
    folium.LayerControl().add_to(Map_Object)

    # Color bar
    colormap.caption = 'Unemployment color scale'
    colormap.add_to(Map_Object)


if __name__ == "__main__":
    choropleth()