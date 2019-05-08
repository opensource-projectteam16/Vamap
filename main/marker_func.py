import folium


# Hyunjae Lee is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''

# Load default markers (roads, buildings, subways)


def Make_Default_Markers(MapObject, roads, buildings, subways):

    # Mark roads
    # skip roads

    # Mark buildings :: building[0] = coorx, building[1] = coory, building[2] = value of the building
    for building in buildings:
        folium.Marker([building[0], building[1]],
                      tooltip=building[2]).add_to(MapObject)

    # Mark subways :: subway[0] = coorx, subway[1] = coory, subway[2] = the name of the subway station
    for subway in subways:
        folium.Marker([subway[0], subway[1]],
                      tooltip=subway[2]).add_to(MapObject)


# Load value markers and circlemarker based on user input (calculated by 'scroing')


def Make_Value_Markers(MapObject, user_data, coverage):
    for data in user_data:

        loc = [data[0], data[1]]

        if data[2] >= 50:
            color = '#FD1801'
        elif data[2] < 50 and data[2] > 25:
            color = '#FD7301'
        else:
            color = '#F7BC05'

        folium.Marker(loc,
                      tooltip=data[3]).add_to(MapObject)
                      
        folium.Circle(
            loc,
            radius=coverage,
            # popup=''
            color=color,
            fill=True,
            fill_color=color
        ).add_to(MapObject)