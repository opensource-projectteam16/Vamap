import folium
import os

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

    print('roadIcon is loaded from {}'.format(os.path.join(path, 'roadIcon')))

    roadIcon = folium.features.CustomIcon(
        os.path.join(path, 'roadIcon'), icon_size=(28, 30))

    for eachRoad in scored_roads:
        folium.Marker([eachRoad[0], eachRoad[1]],
                      icon=folium.Icon(icon=roadIcon)
                      ).add_to(MapObject)

    # Mark others marker ::
    # eachObject[0] = coorx,
    # eachObject[1] = coory,

    print('othersIcon is loaded from {}'.format(
        os.path.join(path, 'othersIcon')))
    othersIcon = folium.features.CustomIcon(url, icon_size=(28, 30))

    for eachObject in scored_others:
        folium.Marker([eachObject[0], eachObject[1]],
                      icon=folium.Icon(icon=othersIcon)
                      ).add_to(MapObject)


# Load value markers and circlemarker based on user input
# (calculated by 'scroing')


def Make_Value_Markers(MapObject, user_data, coverage, path):

    userIcon = folium.features.CustomIcon(
        os.path.join(path, 'vamap_logo'), icon_size=(28, 30))

    for data in user_data:

        loc = [data[0], data[1]]

        if data[2] >= 50:
            color = '#FD1801'
        elif data[2] < 50 and data[2] > 25:
            color = '#FD7301'
        else:
            color = '#F7BC05'

        folium.Marker(loc,
                      icon=folium.Icon(icon=userIcon)).add_to(MapObject)

        folium.Circle(
            loc,
            radius=coverage,
            # popup=''
            color=color,
            fill=False,
            fill_color=color
        ).add_to(MapObject)
