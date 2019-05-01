import numpy as np
import os
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string

# Seokcheon Ju is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''

class Coordinate:
    def __init__(self,xcor,ycor):
        self.x=xcor
        self.y=ycor

class dataproc: 
    def __init__(self,datafile,columnx='x',columny='y',value='value',sheetname=''):
        """ 
        datafile={[list of datapath],a datapath}, columnx=name of x axis, columny=name of y axis, 
        value= column which will be major comparator, sheet=sheet name(if different)
        """
        datamanager=excelmanager(datafile,columnx,columny,value,sheetname)
        self.maindata=datamanager.getdata()
        print (self.maindata)

    def getcoordsortedata(self,coord1,coord2,coord3,coord4):
        """
        starts from right top coordinate, rotate into CW
        """
        resultlist=[]
        for datpage in self.maindata:
            idx = np.zeros((1,))
            for row in range(0,np.size(datpage,0)):
                tmp=np.where(np.logical_and(datpage[row][0] > coord2.y , datpage[row][0] <= coord1.y))[0]
                if tmp.size>0:
                    idx=np.concatenate((idx,[1]))
                else:
                    idx=np.concatenate((idx,[0]))
                
            idx=np.delete(idx,0,0)        
            xindex=list()
            for r in range(0,np.size(idx,0)):
                if idx[r]!=0:
                    xindex.append(r)
            #extracted x < x> coordinate        
            idx = np.zeros((1,))
            for row in xindex:
                tmp=np.where(np.logical_and(datpage[row][1] >coord3.x,datpage[row][1] <=coord2.x))[0]
                if tmp.size>0:
                    idx=np.concatenate((idx,[1]))
                else:
                    idx=np.concatenate((idx,[0]))
            idx=np.delete(idx,0,0)            
            xyindex=list()
            for r in range(0,np.size(idx,0)):
                if idx[r]!=0:
                    xyindex.append(xindex[r])    
            resultlist.append(datpage[np.array(np.asarray(xyindex))])      
        
        return resultlist
    
    def getdata(self):
        return self.maindata

class excelmanager:
    def __init__(self,datafile,columnx,columny,value,sheetname=''): 
        columnname=[columnx,columny,value]
        self.resultlist=[]
        if type(datafile)==list:
            for afile in datafile:
                load_exs = load_workbook(filename=afile, data_only=True)
                print("loaded "+str(afile))
                if sheetname!='':
                    load_ws = load_exs[sheetname]
                    self.resultlist=extractdata(load_exs[sheetname],columnname)

                for sheet in load_exs: #several sheets
                    self.resultlist.append(self.extractdata(sheet,columnname))
        else:
            load_exl = load_workbook(filename=datafile, data_only=True)
            print("loaded "+str(datafile))
        
            if sheetname!='':
                load_ws = load_exl[sheetname]
                self.resultlist=extractdata(load_ws[sheetname],columnname)

            for sheet in load_exl: #several sheets
                self.resultlist.append(self.extractdata(sheet,columnname))
    
    def extractdata(self,load_sheet,columnname):
        result=np.zeros((load_sheet.max_row-1,1))
        for name in columnname:
            for r in load_sheet[1]:
                if r.value==name:
                    dat=np.array([row[r.column-1].value for row in load_sheet.iter_rows(min_row=2)],order='K')
                    dat=dat[:,np.newaxis]
            result=np.concatenate((result,dat),1)

        result=np.delete(result,0,1)
        return result

    def getdata(self):
        return self.resultlist
