# Sangmin Lee is in charge

from preprocessing.dataproc import dataproc
from preprocessing.dataproc import excelmanager
import numpy as np
import math
from math import radians, cos, sin, asin, sqrt
from geopy.distance import vincenty


''' 
<How to work>   
<Usage> 
 Input example  : Numpy
 Output example : list according below
 
    roads = [[x,y,start,end,가중치], ... ]
    others = [[x,y,가중치], ... ]
    userSet = [x, y, value]
 '''


class Scoring:
    def __init__(self, coverage,userSet, roadsSet,othersSet ):
        self.coverage = coverage
        self.userSet = userSet
        self.roadsSet = roadsSet
        self.othersSet = othersSet

    '''

    #coverage 범위
    #범위에 따른 패킹
    # 벨류값 연산
    #리턴

    roadsSet = {0.5 : [csv,sheet1,x,y,start,end,width,5], 가중치 :  [csv,sheet2,x,y,st,fn]}
    othersSet = { 가중치 : [csv, sheet, x,y]}
    userSet = [sheet,x, y, value]

    '''

    def packingList(self, predata):
        predata = predata[0]
        predata = predata[0]




        setindex = []
        sx = []
        sy = []
        st = []
        ed = []
        va = []
        for data, index in zip(predata, range(0, len(predata))):
            ps = data.dtype
            if ps.names[0] == 'x':
                sx.append(predata[index])
            elif ps.names[0] == 'y':
                sy.append(predata[index])
            elif ps.names[0] == 'start':
                st.append(predata[index])
            elif ps.names[0] == 'end':
                ed.append(predata[index])
            elif ps.names[0] == 'value':
                va.append(predata[index])


        sx = sx[0]
        sy = sy[0]
        st = st[0]
        ed = ed[0]
        va = va[0]
        data = []

        if st == list():
            for i,j,k,l in zip(sx,sy,st,ed):
                data.append([float(i[0][0]),float(j[0][0]),float(k[0][0]),float(l[0][0]),predata[0]])

        else :
            for i, j, k in zip(sx, sy, va):
                data.append([float(i[0][0]), float(j[0][0]),predata[0]])

        return data



    def callObj(self):
        allOf = dataproc()

        label = allOf.getdatalabel()
        count = len(label)
        Rcount = len(self.roadsSet)
        Ocount = len(self.ohtersSet)
        Ucount = len(self.UserSet)
        r_value = []
        o_value = []
        u_value = []
        for i,j in zip(self.roadsSet.keys(),self.roadsSet.values()):
            r_value.append(i,j)
        for i,j in zip(self.othersSet.keys(),self.othersSet.values()):
            o_value.append(i,j)
        for i, j in zip(self.userSet.keys(), self.userSet.values()):
            u_value.append(i, j)

        userPack = []
        roadsPack = []
        othersPack = []

        for i in range(0, Rcount):
            a = []
            roadsPack.append(a)

        for i in range(0, Ocount):
            a = []
            othersPack.append(a)

        for i in range(0, Ucount):
            a = []
            userPack.append(a)

        for i in range(0, count):
            for u in range(0,Ucount):
                if label[i] == self.userSet[u]:
                    userPack.append([u_value[0],allOf.getdata()[i]])
            else:
                for r in range(0, Rcount):
                    if label[i] == self.r_value[r]:
                        roadsPack[r].append([r_value[0],allOf.getdata()[i]])

                    else:
                        for o in range(0, Ocount):
                            if label[i] == self.o_value[o]:
                                othersPack[o].append([o_value[0],allOf.getdata()[i]])


        userPack = [userPack]
        userPack = self.packingList(userPack)
        roadsPack = self.packingList(roadsPack)
        othersPack = self.packingList(othersPack)

        return userPack, roadsPack, othersPack




#newCoverage -> inCoverage -> converDis -> cal



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

        incover = []
        for i in range(0,len(data)):
            if data[i][0] > upPoint[0] and data[i][0] < downPoint[0] :
                incover.append(data[i])
            elif data[i][0] > downPoint[0]:
                break;

        for i in range(0,len(incover)):
            if data[i][1] > upPoint[1] or data[i][1] < downPoint[1] :
                del data[i]

        return data


#    roadsSet = {0.5 : [x,y,start,end], 가중치 :  [csv,sheet2,x,y,st,fn]}

    def inCoverageR(self,data):
        upPoint, downPoint = self.newCoverage(data)

        incover = []
        for i in range(0,len(data)):
            if (data[i][0] > upPoint[0] and data[i][0] < downPoint[0])\
                    or (data[i][2][0] > upPoint[0] and data[i][2][0]<downPoint[0])\
                    or (data[i][3][0] > upPoint[0] and data[i][3][0]<downPoint[0]):
                incover.append(data[i])

        for i in range(0,len(incover)):
            if data[i][1] > upPoint[1] or data[i][1] < downPoint[1] \
                    or (data[i][2][1] > upPoint[1] and data[i][2][1] < downPoint[0]) \
                    or (data[i][3][1] > upPoint[1] and data[i][3][1] < downPoint[0]):
                del data[i]

        return data




    def convertDis(self, data, userdata):
        # convert decimal degrees to radians

        # user data간의 비교 판단
        dislist = []

        # 위도경도 -> m(거리)
        for i in data:
            lon1, lat1, lon2, lat2 = map(radians, [i[1], i[0], userdata[1], userdata[0]])
            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            m = (6367 * c) * 1000

            dislist.append(m)

        return dislist



## 가중치 매개변수 맞추기
    def cal_(self, user, data, coverage, weight):
        # value = weight*(distance/coverage)
        sum = 0;
        data = self.inCoverage(data)

        pre = self.convertDis(user, data)

        for i in pre:
                x = data[i][2] * (i / coverage)
                sum += x


        return sum



    def cal_roads(self, user, data, coverage, weight):
        # value = weight*(distance/coverage)

        sum = 0;
        i=0
        middle = []
        start = []
        end = []
        for i in range(0,len(data)):
            middle.append([data[i][0],data[i][1]])
            start.append(data[i][2])
            end.append(data[i][3])

        middleD = self.convertDis(user, middle, coverage)
        startD = self.convertDis(user, start, coverage)
        endD = self.convertDis(user, end, coverage)


        distantList = []
        pre=[]
        for i in range(0,len(data)):
            pre.append(middleD[i],startD[i],endD[i])
            pre[i].sort()
            distantList.append([pre[i][0],data[i][4]])


        for i in distantList:
            x =  data[i][4]* (i / coverage)
            sum += x
            i+=1

        return sum



    def valueScore(self):


        allOf = dataproc('test.xlsx')
        label=allOf.getdatalabel()
        count = len(label)


        user_data, roads_data, others_data = self.callObj()

        resultUser = user_data
        count = 0

        for user in user_data:
            x = self.cal_roads(user, roads_data)
            y = self.cal_(user, others_data, self.coverage)
            z = self.cal_(user, user_data, self.coverage)


            resultUser[count][2] = x + z + y
            count +=1

        return roads_data, others_data, resultUser

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