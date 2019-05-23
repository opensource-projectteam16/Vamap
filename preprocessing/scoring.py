# Sangmin Lee is in charge

from preprocessing.dataproc import dataproc
from math import radians, cos, sin, asin, sqrt

''' 
<How to work>
<Usage>
 Input example  : Scoring(coverage, userSet, roadsSet, othersSet)

                roadsSet = {0.5 : [csv,sheet1,x,y,x1,y1,x2,y2,idth,5],...}
                othersSet = { 가중치 : [csv, sheet, x,y],...}
                userSet = [csv, sheet,x, y, value]


 Output example : list according below 

                roadsSet = [[x,y],...]
                othersSet = [[x,y],...]
                userSet = [[x, y, value],...]


 import dataproc : dataproc(Pack, mode)

                Pack : values() of Set

'''
class Scoring:
    def __init__(self, coverage, userSet, roadsSet, othersSet):
        self.coverage = coverage
        self.userSet = userSet
        self.roadsSet = roadsSet
        self.othersSet = othersSet

    # 2개 들어갈때 Weight 조정하기
    def packingList(self, predata, Weight, mode):
        result = []
        for x in range(0, len(predata)):
            data = []
            pre = predata[x]
            pre = pre[0]

            setindex = []
            sx = []
            sy = []
            st_x = []
            st_y = []
            ed_x = []
            ed_y = []
            va = []
            for data, index in zip(pre, range(0, len(pre))):
                ps = data.dtype
                if ps.names[0] == 'x':
                    sx.append(pre[index])
                elif ps.names[0] == 'y':
                    sy.append(pre[index])
                elif ps.names[0] == 'x1':
                    st_x.append(pre[index])
                elif ps.names[0] == 'y1':
                    st_y.append(pre[index])
                elif ps.names[0] == 'x2':
                    ed_x.append(pre[index])
                elif ps.names[0] == 'y2':
                    ed_y.append(pre[index])
                elif ps.names[0] == 'value':
                    va.append(pre[index])
            sx = sx[0]
            sy = sy[0]
            if mode == 0:
                for i, j in zip(sx, sy):
                    result.append([float(i[0][0]), float(j[0][0]), 1.0])
            if mode == 2 :
                va = va[0]
                for i, j, k in zip(sx, sy, va):
                    pre = pre[0]
                    result.append([float(i[0][0]), float(j[0][0]), Weight[x]])
            if mode == 1:
                st_x = st_x[0]
                st_y = st_y[0]
                ed_x = ed_x[0]
                ed_y = ed_y[0]
                for i, j, k, l, m, n in zip(sx, sy, st_x, st_y, ed_x, ed_y):
                    result.append([float(i[0][0]), float(j[0][0]), float(k[0][0]), float(l[0][0]), float(m[0][0]), float(n[0][0]),Weight[x]])

        return result

    '''

     #coverage 범위
     #범위에 따른 패킹
     # 벨류값 연산
     #리턴

     roadsSet = {0.5 : [csv,sheet1,x,y,start,end,idth,5], 가중치 :  [csv,sheet2,위도,y,st,fn]}
     dataproc(csv, sheet1, 위도, 경도)
     =>

     othersSet = { 가중치 : [csv, sheet, x,y]}
     userSet = [csv, sheet,x, y, value]

     '''

    def callObj(self):
        #        Rcount = len(self.roadsSet)
        #        Ocount = len(self.othersSet)
        #        Ucount = len(self.userSet)

        userSetting = self.userSet
        roadsSetting = []
        othersSetting = []

        roadsPack = []
        userPack = []
        othersPack = []

        preroadW = list(self.roadsSet.keys())
        preotherW = list(self.othersSet.keys())
        roadWeight = []
        otherWeight = []
        uservalue = []

        rpack =[]
        opack = []


        for i in preroadW:
            a = i[2:]
            a = float(a)
            roadWeight.append(a)
        for i in preotherW:
            a = i[2:]
            a = float(a)
            otherWeight.append(a)

        k=0
        if self.roadsSet != {}:
            for i in zip(self.roadsSet.values()):
                a = i
                roadsSetting.append([a])
        if self.othersSet != {}:
            for i in zip(self.othersSet.values()):
                a = i
                othersSetting.append([a])
        mode = 0

        print("\n===============Load Excel====================================================================================================================================================\n")
        if userSetting != []:
            allU = dataproc(userSetting, mode=0)
            labelU = allU.getdatalabel()
            #            userPack = [userPack]
            userPack.append(allU.getdata())
            userPack = self.packingList(userPack, uservalue, 0)

        if roadsSetting != []:
            for i in range(0,len(roadsSetting)):
                roadSheet = roadsSetting[i]
                roadSheet = roadSheet[0]
                roadSheet = roadSheet[0]
                allR = dataproc(roadSheet, mode=1)
                labelR = allR.getdatalabel()
                for j in range(0, len(labelR)):
                    roadsPack.append(allR.getdata())
            rpack.append(self.packingList(roadsPack, roadWeight, 1))

        if othersSetting != []:
            for i in range(0,len(othersSetting)):
                otherSheet = othersSetting[i]
                otherSheet = otherSheet[0]
                allO = dataproc(otherSheet, mode=2)
                labelO = allO.getdatalabel()
                for j in range(0, len(labelO)):
                    othersPack.append(allO.getdata())
            opack.append(self.packingList(othersPack, otherWeight, 0))
        print("\n====================================================================================================================================================================================================\n")

        return userPack, rpack, opack
    '''
        userPack = userPack[0]
        if userPack != []:
            userPack = self.packingList(userPack, uservalue, 0)
        if rpack != []:
            roadsPack = self.packingList(rpack, roadWeight, 1)
        if opack != []:
            othersPack = self.packingList(opack, otherWeight, 2)
    '''

    # newCoverage -> inCoverage -> converDis -> cal

    def newCoverage(self, userone):
        x1 = userone[0] - self.coverage / 133330
        y1 = userone[1] + self.coverage / (133330 * cos(userone[0]))
        upPoint = [x1, y1]
        x2 = userone[0] + self.coverage / 133330
        y2 = userone[1] - self.coverage / (133330 * cos(userone[0]))
        downPoint = [x2, y2]

        return upPoint, downPoint

    def inCoverage(self, user, data):
        upPoint, downPoint = self.newCoverage(user)

        incover = []
        for i in range(0, len(data)):
            if data[i][0] > upPoint[0] and data[i][0] < downPoint[0]:
                incover.append(data[i])
            elif data[i][0] > downPoint[0]:
                break;

        x = []
        for i in range(0, len(incover)):
            if incover[i][1] > upPoint[1] or incover[i][1] < downPoint[1]:
                x.append(incover[i])
        for i in x:
            incover.remove(i)

        return incover

    #    roadsSet = {0.5 : [x,y,start,end], 가중치 :  [csv,sheet2,x,y,st,fn]}

    def inCoverageR(self, user, data):
        upPoint, downPoint = self.newCoverage(user)

        incover = []
        for i in range(0, len(data)):
            if (data[i][0] > upPoint[0] and data[i][0] < downPoint[0]) \
                    or (data[i][2][0] > upPoint[0] and data[i][2][0] < downPoint[0]) \
                    or (data[i][3][0] > upPoint[0] and data[i][3][0] < downPoint[0]):
                incover.append(data[i])

        x = []
        for i in range(0, len(incover)):
            if incover[i][1] > upPoint[1] or incover[i][1] < downPoint[1] \
                    or (incover[i][2][1] > upPoint[1] and incover[i][2][1] < downPoint[0]) \
                    or (incover[i][3][1] > upPoint[1] and incover[i][3][1] < downPoint[0]):
                x.append(incover[i])
        for i in x:
            incover.remove(i)

        return incover

    def convertDis(self, userdata, data):
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
    def cal_(self, user, data, coverage):
        # value = weight*(distance/coverage)
        sum = 0;
        data = self.inCoverage(user, data)

        pre = self.convertDis(user, data)

        for i in range(0, len(pre)):
            x = data[i][2] * (pre[i] / coverage)
            sum += x

        return sum

    def cal_roads(self, user, data, coverage):
        # value = weight*(distance/coverage)

        sum = 0;
        i = 0
        middle = []
        start = []
        end = []
        for i in range(0, len(data)):
            middle.append([data[i][0], data[i][1]])
            start.append([data[i][2],data[i][3]])
            end.append([data[i][4],data[i][5]])

        middleD = self.convertDis(user, middle)
        startD = self.convertDis(user, start)
        endD = self.convertDis(user, end)

        distantList = []
        pre = []
        for i in range(0, len(data)):
            pre.append([middleD[i], startD[i], endD[i]])
            pre[i].sort()
            distantList.append([pre[i][0], data[i][6]])

        for i in range(0,len(distantList)):
            x = data[i][6] * (distantList[i][0] / coverage)
            sum += x
            i += 1

        return sum

    def valueScore(self):
        user_data, roads_data, others_data = self.callObj()
#        print('351',user_data)
#        print('352',roads_data)
#        print('353',others_data)
        roads_data = roads_data[0]
        others_data = others_data[0]


        resultUser = user_data
        count = 0

        for user in user_data:
            x = self.cal_roads(user, roads_data, self.coverage)
            y = self.cal_(user, others_data, self.coverage)
            z = self.cal_(user, user_data, self.coverage)

            resultUser[count][2] = x + z + y
            count += 1

        roads = []
        others = []
        for i in range(0, len(roads_data)):
                roads.append([roads_data[i][0],roads_data[i][1]])

        for i in range(0, len(others_data)):
            del others_data[i][2]

        print('\n===============Scored UserData=======================================================================================================================================\n')
        print("[Latitude,  Longitude,  Value  ]")
        for i in range(0, len(resultUser)):
            if (2*(i+1)) > len(resultUser):
                break
            print(resultUser[int(len(resultUser)/(2*(i+1)))])
        print("\n================================================================================================================================================================\n")

        return resultUser, roads, others_data
