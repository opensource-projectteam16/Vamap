from preprocessing.dataproc import dataproc
from preprocessing.dataproc import excelmanager
import numpy as np
import math
from math import radians, cos, sin, asin, sqrt
from geopy.distance import vincenty

# a[0]:x
# a[1]:y
# a[2]:value
# 접근 방식 : r[x][y].item()     b[x][y].item()       s[x][y].item()    a[x][y].item() //튜풀
# q=dataproc()
# q.getdata()[index]= data
# q.getdatalabel()=['road','building','subway','user']



allOf = dataproc()

label = allOf.getdatalabel()
count = len(label)

roads = []
sub_bul = []
user_data = []
subways = []
buildings = []

for i in range(0, count):
    if label[i].startswith('road'):
        roads.append(allOf.getdata()[i])
    elif label[i].startswith('building'):
        buildings.append(allOf.getdata()[i])
    elif label[i].startswith('public_bicycle'):
        subways.append(allOf.getdata()[i])
    else:
        user_data.append(allOf.getdata()[i])

print(subways)

indx= subways[0]
setindex=[]
for data,index in zip(indx,range(0,len(indx))):
    ps = data.dtype
    if ps.names[0]=='x':
        print(indx[index])
        setindex.append(index)
    if ps.names[0]=='y':
        print(indx[index])
        setindex.append(index)
#        [x,y,value]
print('hi')
finallist= [indx[column] for column in setindex]
print(finallist)
'''
a[0][0] a[1][0] a[2][0]
a[0][1] a[1][1] a[2][1]


count = 5
for i in range(0,count):
    print(i)
    print("hi")
'''