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
data = pd.read_excel(cwd + "\SampleInput.xlsx",sheet_name='Prof')

#import the dictionaries we've built already
f = open('dictionaries/classDict.pk1',"rb")
classDict = pickle.load(f)
f.close()
f = open('dictionaries/roomDict.pk1','rb')
roomDict = pickle.load(f)
f.close()

class Prof():
    #these are the current attributes that describe a professor
    #we can build these out further in the future, but that
    #would also need further implementation of corresponding methods
    name = None
    minLoad = 6 #Default Values if none are given
    maxLoad = 15 #Default Values if none are given
    nonClasses = []
    reqClasses = []
    MWF_nonTimes = []
    TR_nonTimes = []
    all_nonTimes = [] #All_nonTimes should only contain the double encoded times 
    nonRooms = []
    maxPreps = 0
    
    def __init__(self, name):
        self.name = name
        self.nonClasses = []
        self.nonRooms = []
        self.reqClasses = []
        
    #setters
    def setMinLoad(self, minLoad):
        self.minLoad = minLoad
    def setMaxLoad(self, maxLoad):
        self.maxLoad = maxLoad
    def setMaxPreps(self, maxPreps):
        self.maxPreps = maxPreps
    def setMWF_nonTimes(self, nonTimes):
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        self.TR_nonTimes = nonTimes
    def setNonRooms(self, nonRooms):
        self.nonRooms = nonRooms
    def setAll_nonTimes(self):
        self.all_nonTimes = self.MWF_nonTimes + self.TR_nonTimes
        
    #build the classes from the class dictionary and add it to 
    #the array that we'll be exporting
    def calcNonClasses(self, nonClasses):
        try:
            for nonClass in nonClasses.split(','):
                for keyNum in classDict:
                    if (nonClass == classDict[keyNum].getClass()):
                        self.nonClasses.append(keyNum)
        except AttributeError:
            self.nonClasses.append(None)
    
    #build the rooms from the room dicitonary and add it to 
    #the array that we'll be exporting
    def calcNonRooms(self, nonRooms):
        try:
            for nonRoom in nonRooms.split(','):
                for keyNum in roomDict:
                    if (nonRoom == roomDict[keyNum].getRoom()):
                        self.nonRooms.append(keyNum)
        except AttributeError:
            self.nonRooms.append(None)
        
    #required classes is a bit more complicated since we have
    #to split the string and treat it separatley and then find
    #it in the class dictionary that we've created, finally
    #adding it to the array that we'll export
    def calcReqClasses(self, reqClasses):
        try:
            for reqClass in reqClasses.split(','):
                for keyNum in classDict:
                    if (reqClass == classDict[keyNum].getClass()):
                        self.reqClasses.append(keyNum)
        except AttributeError:
            self.reqClasses.append(None)
            
    #getters
    def getAllTimeConflicts(self):
        return self.all_nonTimes
    def getNonRooms(self):
        return self.nonRooms
    def getNonClasses(self):
        return self.nonClasses
    def getReqClasses(self):
        return self.reqClasses
    def getMaxLoad(self):
        return self.maxLoad
    def getMinLoad(self):
        return self.minLoad
    def getMaxPreps(self):
        return self.maxPreps
        
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
    
    #grab the times from the Excel doc
    MWF_times = profDf["MWF_Unavailable_Times"]
    TR_times = profDf["TTh_Unavailable_Times"]
    
    #take the times and put them through the preprocessing 
    #in handleTime.py script
    MWF_times = ht.handleTimeAll(MWF_times)
    TR_times = ht.handleTimeAll(TR_times)
    count = 1
    
    #iterate through each row in the excel doc and 
    #load each row into a new object and finally 
    #add it to an object array
    for row in profDf.iterrows():
        tempProf = Prof(row[1][0])
        tempProf.calcReqClasses(row[1][1])
        tempProf.calcNonClasses(row[1][2])
        tempProf.setMWF_nonTimes(MWF_times[count-1])
        tempProf.setTR_nonTimes(TR_times[count-1])
        tempProf.setAll_nonTimes()
        tempProf.calcNonRooms(row[1][5])
        tempProf.setMinLoad(row[1][6])
        tempProf.setMaxLoad(row[1][7])
        tempProf.setMaxPreps(row[1][8])
        #tempProf.printClass()
        
        profDict[count] = tempProf
        count+=1
    
    return profDict
    
profDict = getProfs(data)
f = open("dictionaries\profDict.pk1","wb")
pickle.dump(profDict,f)
f.close()

        