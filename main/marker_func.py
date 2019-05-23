import folium
import os
# import base64
# from io import BytesIO

# Hyunjae Lee is in charge

'''
<How to work>

<Usage>
 Input example  :
 Output example :

'''

# Load default markers (roads, buildings, subways)


def Make_Default_Markers(Map_Object, scored_roads, scored_others, path):

    # Mark roads
    # eachRoad[0] = coorx
    # eachRoad[1] = coory

    # print('roadIcon is loaded from {}'.format(
    #     os.path.join(os.path.join(path, 'static'), 'roadIcon.png')))

    # road_encoded = base64.b64encode(
    #     open(os.path.join(os.path.join(path, 'static'), 'roadIcon.png'), 'rb').read())
    # road_decoded = base64.b64decode(road_encoded)
    # road_icon_url = BytesIO(road_decoded)
    # roadIcon = folium.features.CustomIcon(road_icon_url, icon_size=(14, 14))

    for eachRoad in scored_roads:
        folium.Marker(location=eachRoad, icon=folium.Icon(color='green')
                      ).add_to(Map_Object)

    # Mark others marker ::
    # eachObject[0] = coorx,
    # eachObject[1] = coory,

    # print('othersIcon is loaded from {}'.format(
    #     os.path.join(os.path.join(path, 'static'), 'othersIcon.png')))

    # other_encoded = base64.b64encode(
    #     open(os.path.join(os.path.join(path, 'static'), 'othersIcon.png'), 'rb').read())
    # other_decoded = base64.b64decode(other_encoded)
    # other_icon_url = BytesIO(other_decoded)
    # othersIcon = folium.features.CustomIcon(other_icon_url, icon_size=(14, 14))

    for eachObject in scored_others:
        folium.Marker(location=eachObject,
                      icon=folium.Icon(color='blue')).add_to(Map_Object)


# Load value markers and circlemarker based on user input
# (calculated by 'scroing')


def Make_Value_Markers(MapObject, user_data, coverage, path):

    # userIcon = folium.features.CustomIcon(
    #     os.path.join(os.path.join(path, 'static'), 'vamap_logo.png'), icon_size=(14, 14))

    for data in user_data:

        loc = [data[0], data[1]]

        if data[2] >= 50:
            color = '#FD1801'
        elif data[2] < 50 and data[2] > 25:
            color = '#FD7301'
        else:
            color = '#F7BC05'

        folium.Marker(location=loc, tooltip=str(data[2]), icon=folium.Icon(
            color='red')).add_to(MapObject)

        folium.Circle(
            loc,
            radius=coverage,
            # popup=''
            color=color,
            fill=False,
            fill_color=color
        ).add_to(MapObject)
