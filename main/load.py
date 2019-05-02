import folium
import json
import os
# Yooseok Jeong is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''


'''example'''
'''
rfile1 = open('c:/Users/82102/Documents/GitHub/Team16_Development/main/skorea-provinces-2018-geo.json', 'r', encoding='utf-8').read()

rfile2= open('c:/Users/82102/Documents/GitHub/Team16_Development/main/seoul_municipalities_geo.json', 'r', encoding='utf-8').read()

jsonData1 = json.loads(rfile1)

jsonData2 = json.loads(rfile2)

folium.GeoJson(jsonData1, name='json_data').add_to(map_osm)

folium.GeoJson(jsonData2, name='json_data').add_to(map_osm)

'''


class Load:
    def __init__(self, *args, **kwargs):
        pass
