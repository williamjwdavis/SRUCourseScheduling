# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:10:03 2020

@author: willi
"""
import os
import pickle
import pandas as pd
import handleTime as ht

cwd = os.getcwd()
data = pd.read_excel(cwd + "\SampleInput.xlsx",sheet_name='Teacher')

f = open(cwd + '\classDict.pk1',"rb")
classDict = pickle.load(f)
f.close()

class Prof():
    name = None
    minLoad = 0
    maxLoad = 0
    nonClasses = []
    MWF_nonTimes = []
    TR_nonTimes = []
    nonRooms = []
    
    def __init__(self, name):
        self.name = name
        
    def setMinLoad(self, minLoad):
        self.minLoad = minLoad
    def setMaxLoad(self, maxLoad):
        self.maxLoad = maxLoad
    
    def calcNonClasses(self, nonClasses):
        pass
    
    def setMWF_nonTimes(self, nonTimes):
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        self.TR_nonTimes = nonTimes
    def setNonRooms(self, nonRooms):
        self.nonRooms = nonRooms
    def setNonClasses(self, nonClasses):
        self.nonClasses = nonClasses
        
    def printClass(self):
        print("Name: " + self.name)
        print("Min Load: " + str(self.minLoad))
        print("Max Load: " + str(self.maxLoad))
        print("nonClasses: " + str(self.nonClasses))
        print("nonRooms: " + str(self.nonRooms))
        print("MWF NonTimes: " + str(self.MWF_nonTimes))
        print("TR NonTimes: " + str(self.TR_nonTimes))
        
                                
    
def getProfs(profDf):
    profDict = {}
    
    MWF_times = profDf["MWF_Unavailable_Times"]
    TR_times = profDf["TTh_Unavailable_Times"]
    
    MWF_times = ht.handleTime(MWF_times)
    TR_times = ht.handleTime(TR_times)
    count = 0
    
    for row in profDf.iterrows():
        tempProf = Prof(row[1][0])
        tempProf.setNonClasses(row[1][1])
        tempProf.setMWF_nonTimes(MWF_times[count])
        tempProf.setTR_nonTimes(TR_times[count])
        tempProf.setMinLoad(row[1][5])
        tempProf.setMaxLoad(row[1][6])
        tempProf.printClass()
        
        profDict[count] = tempProf
        count+=1
        break
    
    return profDict
    
profDict = getProfs(data)
f = open("profDict.pk1","wb")
pickle.dump(profDict,f)
f.close()

        