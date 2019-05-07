# Sangmin Lee is in charge

from preprocessing.dataproc import dataproc
from preprocessing.dataproc import excelmanager
import numpy as np
import math
from math import radians, cos, sin, asin, sqrt
from geopy.distance import vincenty


'''
넘어오는 데이터 가정
array[[도로1],[도로2]],[빌딩],[지하철],[유저데이터]]
'''

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

class Scoring:
    def __init__(self, coverage, weight) :
        self.coverage = coverage
        self.weight = weight


    #center road that is least distance point
    def center_road(self, pre_roads) :

        roads = np.array()

        roads[0] = (pre_roads[0][0] + pre_roads[1][0])/2
        roads[1] = (pre_roads[0][1] + pre_roads[1][2])/2


        return roads


    def convertDis(self, np_obj, userdata, coverage, count=0):
        # convert decimal degrees to radians


        #user data간의 비교 판단
        dislist = []

        #위도경도 -> m(거리)
        for i in np_obj :
            lon1, lat1, lon2, lat2 = map(radians, [i[0],i[1] , userdata[0], userdata[1]])
            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            m = (6367 * c)*1000

            if coverage < m :
                m =0
                dislist.append(m)
            else :
                dislist.append(m)


        return dislist


    def cal_(self, user, user_data, coverage,weight):
        #value = weight*(distance/coverage)
        sum = 0;

        pre = self.convertDis(user,user_data,coverage)

        for i in pre:
            if i == 0:
                continue;
            x = weight*(i/coverage)
            sum += x

        return sum


    #a[0]:x
    #a[1]:y
    #a[2]:value
    #접근 방식 : r[x][y].item()     b[x][y].item()       s[x][y].item()    a[x][y].item() //튜풀
    #q=dataproc().
    # q.getdata()[index]= data
    #q.getdatalabel()=['road','building','subway','user']

    #value 연산 방법 1 : 군집화
    #value 연산 방법 2 : 주성분 분석

    def valueScore(self) :

        nallOf = np.array()
        nallOf = dataproc()


        allOf = nallOf

        roads = []
        sub_bul = []
        user_data=[]
        subways = []
        buildings = []


        #수정필요
        for i in allOf:
            for j in i:
                if j[2] == 'user_data':
                    user_data.append(j)
                elif j[2] == 'road' :
                    roads.append(j)
                else:
                    sub_bul.append(j)
                    if j[2] == 'buildings':
                        buildings.append(j)
                    else:
                        subways.append(j)


        for user in user_data :
            x = self.cal_(roads, user, self.coverage,self.weight[0])
            y = self.cal_(buildings, user, self.coverage,self.weight[1])
            z = self.cal_(subways, user, self.coverage,self.weight[2])
            w = self.cal_(user_data, user, self.coverage,self.weight[3])

            user[2] =x+z+y+w

        return roads,buildings,subways,user_data




    #수정 코드 보관
    '''
    
    
    
        #distance between Road & user_data
    def distanRoad(self, road, user_data) :
        #least distance between road & user_data
        x = [(road.start.coorx - user_data.coorx),(road.start.coory - user_data.coory),0]
        y = [(road.end.coorx - user_data.coorx),(road.end.coory - user_data.coory),0]
        area = abs((x[0]*y[1])-(x[1]*y[0]))

        AB = ((road.start.x-road.end.x)**2 + (road.start.y-road.end.y)**2)**(1/2)
        disR = (area/AB)

        return disR
        
        
        #distance between Building & user_data
        def distanBuild(self, building, user_data) :
            #z^ = x^ + y^
            x = building.coorx - user_data.coorx
            y = building.coory - user_data.coory

            disB = math.sqrt((x * x) + (y * y))

            return disB


        #distance between Subway & user_data
        def distanSubway(self, subway, user_data) :
            ##z^ = x^ + y^
            x = subway.coorx - user_data.coorx
            y = subway.coory - user_data.coory

            disS = math.sqrt((x * x) + (y * y))

            return disS
            
        def addDis_other(self, basicNp, coverage):

            sum = 0;
    
            for i in basicNp:
                x = coverage/i[2]
                sum += x
    
            return sum
            
            
            
            
            
    def cal_other(self, other, user_data, coverage):
        sum = 0;
        print(other)

        pre = self.convertDis(other,user_data,coverage)

        for i in pre:
            if i == 0:
                continue;
            x = coverage/i
            sum += x


        return sum
    '''