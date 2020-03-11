# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:10:05 2020

@author: willi
"""
import os
import pickle
import pandas as pd
import handleTime as ht

cwd = os.getcwd()
data = pd.read_excel("SampleInput.xlsx",sheet_name="Classes")

f = open('dictionaries/roomDict.pk1','rb')
roomDict = pickle.load(f)
f.close()

class Class():
    #These are the attributes we'll be tracking for the classes
    #additinaly attributes can be constructed with corresponding methods
    #in the future
    department = None
    number = None
    numCredits = 0
    MWF_nonTimes = []
    TR_nonTimes = []
    nonRooms = []
    nonClasses = []
    num_sections = 0
    
    #Some of these values were initialized to an empty array since there 
    #was a bug that would carry forward the last object's values
    def __init__(self, department, number):
        self.department = department
        self.number = number
        self.numCredits = 0
        self.MWF_nonTimes = []
        self.TR_nonTimes = []
        self.all_nonTimes = [] #All times should only contain the final double encoded times
        self.nonRooms = []
        self.nonClasses = []
        
    #Set functions including MWF and TR times that are correctly evaluated and
    #handled using handleTime.py
    def setNumCredits(self, numCredits):
        self.numCredits=numCredits
    def setMWF_nonTimes(self, nonTimes):
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        self.TR_nonTimes = nonTimes
    def setAll_nonTimes(self):
        self.all_nonTimes = self.MWF_nonTimes + self.TR_nonTimes
        
    def setNumSections(self, numSections):
        self.numSections = numSections
        
    #this sets the classes by calling on the class dictionary that will
    #be made and getting the appropriate encoded value of the class
    #thus adding it to the array
    def setNonClasses(self, nonClasses, classDict):
        try:
            for nonClass in nonClasses.split(','):
                for keyNum in classDict.keys():
                    if (nonClass == classDict[keyNum].getClass()):
                        self.nonClasses.append(keyNum)
        except AttributeError:
            self.nonClasses.append(None)
            
    #this sets the rooms by calling on the room dictionary that was
    #made and getting hte appropriate encoded value of the rooms
    #thus adding it to the array
    def calcNonRooms(self, nonRooms):
        try:
            for nonRoom in nonRooms.split(','):
                for keyNum in roomDict:
                    if (nonRoom == roomDict[keyNum].getRoom()):
                        self.nonRooms.append(keyNum)
        except AttributeError:
            self.nonRooms.append(None)
        
    #Get functions for the attributes
    def getNumCredits(self):
        return self.numCredits
    def getClass(self):
        return self.department + " " + str(self.number)
    def getMWFConflicts(self):
        return self.MWF_nonTimes
    def getTHConflicts(self):
        return self.TH_nonTimes
    def getNumSections(self):
        return self.numSections
    def getNonClasses(self):
        return self.nonClasses
    def getNonRooms(self):
        return self.nonRooms
    def getAllTimeConflicts(self):
        return self.all_nonTimes
    
    def printClass(self):
        print("Class: " + self.department + " " + str(self.number))
        print("Credits: " + str(self.numCredits))
        print("Number of Setions " + str(self.numSections))
        print("NonRooms: " + str(self.nonRooms))
        print("NonClasses: " + str(self.nonClasses))
        print("MWF_NonTimes: " + str(self.MWF_nonTimes))
        print("TTH_NonTimes: " + str(self.TR_nonTimes))
    
def getClasses(classDf):
    classDict={}
    
    #slot the times into dataframes
    MWF_times = classDf["MWF_Room-Time_Exceptions"]
    TR_times = classDf["TTh_Room-Time_Exceptions"]
    
    #run the preprocessing from handleTime.py
    MWF_times = ht.handleTimeAll(MWF_times)
    TR_times = ht.handleTimeAll(TR_times)
    count = 1
    
    #iteratre through the rows to build objects for each class that needs
    #to be accounted for in the Excel doc
    for row in classDf.iterrows():
        tempClass = Class(row[1][0][0:4], row[1][0][5:])
        tempClass.setNumCredits(row[1][1])
        #tempClass.setNonClasses(row[1][2])
        tempClass.setMWF_nonTimes(MWF_times[count-1])
        tempClass.setTR_nonTimes(TR_times[count-1])
        tempClass.setAll_nonTimes()
        tempClass.calcNonRooms(row[1][5])
        tempClass.setNumSections(row[1][6])        
        #tempClass.printClass()
        classDict[count]=tempClass
        
        count+=1
    return classDict

#since we can't have an attribute of the dictionary that we're building be 
#dependant on the dicitonary itself, we use this function after we create the
#dictionary so there are no issues.
def setAllNonClasses(classDict, classDf):
    for key in classDict.keys():
        classDict[key].setNonClasses(classDf.iloc[key-1][2],classDict)
    return classDict
        
classDict = getClasses(data)
classDict = setAllNonClasses(classDict,data)
f = open("dictionaries\classDict.pk1",'wb')
pickle.dump(classDict, f)
f.close()
    