# Sangmin Lee is in charge

import dataproc
import numpy as np
import math


''' 
<How to work>

<Usage> 
 Input example  : Numpy
 Output example : Numpy

'''

'''
roads = [start[coorx, coory], end[coorx, coory], width]
buildings = [coorx, coory, floors, address]
subways = [coorx, coory, name of the subway]
user_data = [coorx, coory, value]
'''

#distance between Road & user_data
def distanRoad(road, user_data) :
    #least distance between road & user_data
    x = [(road.start.coorx - user_data.coorx),(road.start.coory - user_data.coory),0]
    y = [(road.end.coorx - user_data.coorx),(road.end.coory - user_data.coory),0]
    area = abs((x[0]*y[1])-(x[1]*y[0]))

    AB = ((road.start.x-road.end.x)**2 + (road.start.y-road.end.y)**2)**(1/2)
    disR = (area/AB)

    return disR


#distance between Building & user_data
def distanBuild(building, user_data) :
    #z^ = x^ + y^
    x = building.coorx - user_data.coorx
    y = building.coory - user_data.coory

    disB = math.sqrt((x * x) + (y * y))

    return disB


#distance between Subway & user_data
def distanSubway(subway, user_data) :
    ##z^ = x^ + y^
    x = subway.coorx - user_data.coorx
    y = subway.coory - user_data.coory

    disS = math.sqrt((x * x) + (y * y))

    return disS


#value 연산 방법 1 : 군집화
#value 연산 방법 2 : 주성분 분석

def valueScore(roads, buildings, subways, user_data) :
    #다른 유저데이터!!

    valRoad = np.array([])
    valBuild = np.array([])
    valSubway = np.array([])

    #임시
    sumR = 0
    sumB = 0
    sumS = 0
    value = 0

    for i in roads :
        np.append(valRoad,distanRoad(i, user_data))
        sumR += distanRoad(i, user_data)
    for i in buildings:
        np.append(valBuild, distanBuild(i, user_data))
        sumB += distanRoad(i, user_data)
    for i in subways:
        np.append(valSubway, distanSubway(i, user_data))
        sumS += distanRoad(i, user_data)

    disValue = np.array([valRoad],[valBuild],[valSubway])

    #임시
    value = sumR + sumB + sumS

    user_data.value = value

    return user_data


class Scoring:
    def __init__(self, *args, **kwargs):
        pass
