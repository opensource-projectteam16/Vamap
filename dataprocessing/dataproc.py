import numpy as np
import os
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string

class Coordinate:
    def __init__(self):
        pass
    def __init__(xcor,ycor):
        self.x=xcor
        self.y=ycor

class dataproc:
    def __init__(self,datafile,columnx='x',columny='y',value='value',sheet=''):
            datamanager=excelmanager(datafile,columnx,columny,value,sheet)
            self.maindata=datamanager.getdata()
            print (self.maindata)
            print(self.maindata.shape())

class excelmanager:
    def __init__(self,datafile,columnx,columny,value,sheet=''):
        load_exl = load_workbook(filename='test.xlsx', data_only=True)
        columnname=[columnx,columny,value]
        print("loaded "+str(datafile))
        self.resultlist=[]
        if sheet!='':
            load_ws = load_exl[sheet]
            self.resultlist=extractdata(load_ex1[sheet],columnname)

        for sheet in load_exl:
            self.resultlist.add(self.extractdata(sheet,columnname))
    
    def extractdata(self,load_sheet,columnname):
        result=np.zeros((load_sheet.max_row-1,1))
        for name in columnname:
            for r in load_sheet[1]:
                if r.value==name:
                    dat=np.array([row[r.column-1] for row in load_sheet.iter_rows(min_row=2)],order='K')
                    dat=dat[:,np.newaxis]
            result=np.concatenate((result,dat),1)

        result=np.delete(result,0,1)
        return result

    def getdata(self):
        return self.resultlist
