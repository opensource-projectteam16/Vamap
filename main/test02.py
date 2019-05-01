import folium
import json

map_osm = folium.Map(location=[37.566345, 126.977893],zoom_start=17)

folium.Marker([37.566345, 126.977893], popup= '서울특별시청' ).add_to(map_osm)

rfile1 = open('c:/Users/82102/PycharmProjects/untitled2/skorea-provinces-2018-geo.json', 'r', encoding='utf-8').read()

rfile2= open('c:/Users/82102/PycharmProjects/untitled2/seoul_municipalities_geo.json', 'r', encoding='utf-8').read()

jsonData1 = json.loads(rfile1)

jsonData2 = json.loads(rfile2)

folium.GeoJson(jsonData1, name='json_data').add_to(map_osm)

folium.GeoJson(jsonData2, name='json_data').add_to(map_osm)

map_osm.save('c:/Users/82102/PycharmProjects/untitled2/map.html')



