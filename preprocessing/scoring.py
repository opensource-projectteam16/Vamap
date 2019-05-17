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
    def __init__(self, coverage, userSet, roadsSet, othersSet ):
        self.coverage = coverage
        self.userSet = userSet
        self.roadsSet = roadsSet
        self.othersSet = othersSet


    def packingList(self, predata, Set):
        print('40',predata)
        predata = predata[0]
#        predata = predata[0]

        setindex = []
        sx = []
        sy = []
        st_x = []
        st_y = []
        ed_x = []
        ed_y = []
        va = []
        for data, index in zip(predata, range(0, len(predata))):
            ps = data.dtype
            if ps.names[0] == 'x':
                sx.append(predata[index])
            elif ps.names[0] == 'y':
                sy.append(predata[index])
            elif ps.names[0] == 'x1':
                st_x.append(predata[index])
            elif ps.names[0] == 'y1':
                st_y.append(predata[index])
            elif ps.names[0] == 'x2':
                ed_x.append(predata[index])
            elif ps.names[0] == 'y2':
                ed_y.append(predata[index])
            elif ps.names[0] == 'value':
                va.append(predata[index])

        print('69',sx)
        sx = sx[0]
        sy = sy[0]
        st_x = st_x[0]
        st_y = st_y[0]
        ed_x = ed_x[0]
        ed_y = ed_y[0]
        va = va[0]

        data = []

        if st_x != list():
            for i,j,k,l,m,n in zip(sx,sy,st_x,st_y,ed_x,ed_y):
                data.append([float(i[0][0]),float(j[0][0]),float(k[0][0]),float(l[0][0]),float(m[0][0]),float(n[0][0]),predata[0]])

        else :
            for i, j, k in zip(sx, sy, va):
                data.append([float(i[0][0]), float(j[0][0]),predata[0]])

        return data

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

        userPack = self.userSet
        roadsPack = [self.roadsSet]
        othersPack = [self.othersSet]

        '''
        for i in self.roadsSet.values():
            a = i
            roadsPack.append(a)

        for i in self.othersSet.values():
            a = i
            othersPack.append(a)

        for i in self.userSet.values():
            a = i
            userPack.append(a)
        '''

        allR = dataproc(roadsPack, mode = 1)
        allO = dataproc(othersPack, mode = 2)
        allU = dataproc(userPack, mode = 0)

        labelR = allR.getdatalabel()
        labelO = allO.getdatalabel()
        labelU = allU.getdatalabel()

        print('102',allU.getdata())

        for i in range(0, len(labelR)):
            roadsPack[i].append(allR.getdata())
        for i in range(0, len(labelO)):
            othersPack[i].append(allO.getdata())

        userPack.append(allU.getdata())

        print('145',othersPack)
        print('146', userPack)

        userPack = self.packingList(userPack,self.userSet)
        roadsPack = self.packingList(roadsPack,self.roadsSet)
        othersPack = self.packingList(othersPack,self.othersSet)

        return userPack,roadsPack, othersPack


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
        user_data, roads_data, others_data = self.callObj()

        resultUser = user_data
        count = 0

        for user in user_data:
            x = self.cal_roads(user, roads_data)
            y = self.cal_(user, others_data, self.coverage)
            z = self.cal_(user, user_data, self.coverage)


            resultUser[count][2] = x + z + y
            count +=1

        for i in range(0,len(roads_data)):
            for j in range(2,7):
                del roads_data[i][j]

        for i in range(0,len(others_data)):
            del others_data[i][2]

        print("roads" + roads_data)
        print("other" + others_data)
        print("user" + resultUser)

        return roads_data, others_data, resultUser
