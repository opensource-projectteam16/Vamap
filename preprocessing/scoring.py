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
 
위도 1도 사이의 거리는 48,000 ÷ 360 = 133.33 km 
'''


class Scoring:
    def __init__(self, coverage,userSet, roadsSet,othersSet ):
        self.coverage = coverage
        self.userSet = userSet
        self.roadsSet = roadsSet
        self.othersSet = othersSet



        # a[0]:x
        # a[1]:y
        # a[2]:value
        # 접근 방식 : r[x][y].item()     b[x][y].item()       s[x][y].item()    a[x][y].item() //튜풀
        # q=dataproc()
        # q.getdata()[index]= data
        # q.getdatalabel()=['road','building','subway','user']

    '''

    #coverage 범위
    #범위에 따른 패킹
    # 벨류값 연산
    #리턴

    roadsSet = {0.5 : [csv,sheet1,x,y,start,end,width,5], 가중치 :  [csv,sheet2,x,y,st,fn]}
    othersSet = { 가중치 : [csv, sheet, x,y]}
    userSet = [sheet,x, y, value]

    '''

    def callObj(self):
        allOf = dataproc()

        label = allOf.getdatalabel()
        count = len(label)
        Rcount = len(self.roadsSet)
        Ocount = len(self.ohtersSet)
        r_value = []
        o_value = []
        for i in self.roadsSet.value():
            r_value.append(i)
        for i in self.othersSet.value():
            o_value.append(i)

        userPack = []
        roadsPack = []
        othersPack = []

        for i in range(0, Rcount):
            a = []
            roadsPack.append(a)

        for i in range(0, Ocount):
            a = []
            othersPack.append(a)

        for i in range(0, count):
            if label[i] == self.userSet[0]:
                userPack.append(allOf.getdata()[i])
            else:
                for r in range(0, Rcount):
                    if label[i] == self.r_value[r]:
                        roadsPack[r].append(allOf.getdata()[i])

                    else:
                        for o in range(0, Ocount):
                            if label[i] == self.o_value[o]:
                                othersPack[o].append(allOf.getdata()[i])

        userPack = userPack[0]
        roadsPack = roadsPack[0]
        othersPack = othersPack[0]



    def newCoverage(self, userone):
        x1 = userone[0] - self.coverage / 133330
        y1 = userone[1] + self.coverage / (133330 * cos(userone[0]))
        upPoint = [x1, y1]
        x2 = userone[0] + self.coverage / 133330
        y2 = userone[1] - self.coverage / (133330 * cos(userone[0]))
        downPoint = [x2, y2]

        return upPoint, downPoint



    def inCoverage(self,data):
        upPoint, downPoint = self.newCoverage(data)



        incoverU = []
        for i in range(0,len(data)):
            if data[i][0] > upPoint[0] and data[i][0] < downPoint[0] :
                incoverU.append(data[i])
            elif data[i][0] > downPoint[0]:
                break;

        for i in range(0,len(incoverU)):
            if data[i][1] > upPoint[1] or data[i][1] < downPoint[1] :
                del data[i]

        return data


    def convertDis(self, np_obj, userdata, coverage, count=0):
        # convert decimal degrees to radians

        # user data간의 비교 판단
        dislist = []

        # 위도경도 -> m(거리)
        for i in np_obj:
            lon1, lat1, lon2, lat2 = map(radians, [i[0], i[1], userdata[0], userdata[1]])
            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            m = (6367 * c) * 1000

            if coverage < m:
                m = 0
                dislist.append(m)
            else:
                dislist.append(m)

        return dislist




    def cal_(self, user, user_data, coverage, weight):
        # value = weight*(distance/coverage)
        sum = 0;

        pre = self.convertDis(user, user_data, coverage)

        for i in pre:
            if i == 0:
                continue;
            x = weight * (i / coverage)
            sum += x

        return sum



    def cal_roads(self, user, user_data, coverage, weight):
        # value = weight*(distance/coverage)
        sum = 0;
        i=0

        pre1 = self.convertDis(user, user_data, coverage)
        pre2 = self.convertDis(user, user_data, coverage)
        pre3 = self.convertDis(user, user_data, coverage)




        for i in pre1:
            if i == 0:
                continue;
            x = user[i][2]* weight * (i / coverage)
            sum += x
            i+=1

        return sum



    def valueScore(self):


        allOf = dataproc('test.xlsx')
        label=allOf.getdatalabel()
        count = len(label)


        roads = []
        user_data = []
        subways = []
        buildings = []

        for i in range(0, count):  # a[x][y] -> y
            if label(i) == 'roads':
                roads.append(allOf.getdata(i))
            elif label(i) == 'buildings':
                buildings.append(allOf.getdata(i))
            elif label(i) == 'subways':
                subways.append(allOf.getdata(i))
            else:
                user_data.append(allOf.getdata(i))


        for user in user_data:
            x = self.cal_roads(roads, user, self.coverage, self.weight[0])
            y = self.cal_(buildings, user, self.coverage, self.weight[1])
            z = self.cal_(subways, user, self.coverage, self.weight[2])
            w = self.cal_(user_data, user, self.coverage, self.weight[3])

            user[2] = x + z + y + w

        return roads, buildings, subways, user_data

    # 수정 코드 보관
    '''
    
            allOf = dataproc()



        roads = []
        sub_bul = []
        user_data = []
        subways = []
        buildings = []

        # 수정필요
        for i in allOf:
            for j in i:
                if j[2] == 'user_data':
                    user_data.append(j)
                elif j[2] == 'road':
                    roads.append(j)
                else:
                    sub_bul.append(j)
                    if j[2] == 'buildings':
                        buildings.append(j)
                    else:
                        subways.append(j)




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