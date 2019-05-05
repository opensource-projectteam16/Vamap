import numpy as np
import os
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string
import csv
from io import StringIO
import pandas as pd
import numpy.lib.recfunctions as npfunc
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
    def __init__(self,fileroute,columnname=['x','y','value'],sheetname='',mode=0,):
        """ 
        fileroute={[list of datapath],a datapath}, columnname=['x_columnname','y_columnname','x"_columnname','y"_columnname','value_columnname'], sheet=sheet name(if different)
        if it is road or double coordinate data road=true
        mode means recall from ready made data. 0==no csv file 1==have csv file
        """
        if mode==0:
            datamanager=excelmanager(fileroute,columnname,sheetname)
            self.maindata=datamanager.getdata()
            self.datalabel=datamanager.getdatalabel()
           # print (self.maindata)
           # print (self.datalabel)
            self.savedata()
        if mode==1:
            self.datalabel=[]
            with open("datalabel.csv", 'r') as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    if row != []:
                        self.datalabel.append(''.join(row))
                csvFile.close()
            self.maindata=[]
            for difile in os.listdir(fileroute):
               # print(difile)
                if difile.split(".")[-1]=='npy' and difile!='datalabel.csv':
                    data = np.load(difile)
                    #print(data)
                    self.maindata.append(data)
                    csvFile.close()
        
    def changecolumnname(self,columnname):
        if len(columnname):
            pass
            
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
    
    def savedata(self):
        writer = csv.writer(open("datalabel.csv", 'w'))
        for row in self.datalabel:
            writer.writerow(row)
        for datpage, datlabel in zip(self.maindata,self.datalabel):
            filename=datlabel+'.csv'
            np.save(filename,datpage)           
    def getdatalabel(self):
        return self.datalabel
    def getdata(self):
        return self.maindata

class excelmanager:
    def __init__(self,datafile,columnname,sheetname=''): 
        self.resultlist=[]
        self.datalabel=[]
        if type(datafile)==list:
            for afile in datafile:
                load_exs = load_workbook(filename=afile, data_only=True)
                print("loaded "+str(afile))

                for sheet in load_exs: #several sheets
                    self.resultlist.append(self.extractdata(sheet,columnname))
                    self.datalabel.append(sheet.title)

        else:
            load_exl = load_workbook(filename=datafile, data_only=True)
            print("loaded "+str(datafile))

            for sheet in load_exl: #several sheets
                self.resultlist.append(self.extractdata(sheet,columnname))
                self.datalabel.append(sheet.title)
        
    
    def extractdata(self,load_sheet,columnname):
        result=np.zeros((load_sheet.max_row-1,1))
        namelist=[]
        typelist=[]
        listtype=0
        for p,r in zip(load_sheet[2],load_sheet[1]):
            for name in columnname:
                if r.value==name:
                    if isinstance(p.value,str):
                        typelist.append(np.dtype('U30'))
                    else:
                        typelist.append(np.float64)
            
        for name in columnname:
            add=False
            for r in load_sheet[1]:
                if r.value==name:
                    add=True
                    namelist.append(r.value)
                    dtype=0
                    dat=np.array([row[r.column-1].value for row in load_sheet.iter_rows(min_row=2)],order='K')
                    dat[dat==None]=0
                    dat=dat.astype(typelist[listtype])
                    dat=dat[:,np.newaxis]
                    print(dat.dtype)
                    listtype=listtype+1
            if add==True:
                result=np.concatenate((result,dat),1)
        
        result=np.delete(result,0,1)

        #print(namelist)
        #print(typelist)
        print(result)
        dt={'names':namelist,'formats':typelist}#, 'formats':typelist
        #result=npfunc.repack_fields(result).view(dt)
        result.dtype=dt
        print(result)
    
        return result

    def getdata(self):
        return self.resultlist
    def getdatalabel(self):
        return self.datalabel
