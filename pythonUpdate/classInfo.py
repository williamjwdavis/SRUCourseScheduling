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
data = pd.read_excel(cwd+"\SampleInput.xlsx",sheet_name="Classes")
column=data["Class"]

class Class():
    department = None
    number = None
    numCredits = 0
    MWF_nonTimes = []
    TR_nonTimes = []
    nonRooms = []
    nonClasses = []
    
    num_sections = 0
    
    def __init__(self, department, number):
        self.department = department
        self.number = number
        self.numCredits = 0
        self.MWF_nonTimes = []
        self.TR_nonTimes = []
        self.nonRooms = []
        self.nonClasses = []
        
    #Set functions including MWF and TR times that are correctly evaluated and
    #handled using handleTime.py
    def setNumCredits(self, numCredits):
        self.numCredits=numCredits
    def setMWF_nonTimes(self, nonTimes):
        #self.MWF_nonTimes = ht.handleTime(MWF_list)
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        #self.TH_nonTimes = ht.handleTime(TH_list)
        self.TR_nonTimes = nonTimes
    def setNumSections(self, numSections):
        self.numSections = numSections
    def setNonClasses(self, nonClasses):
        self.nonClasses = nonClasses
    def setNonRooms(self, nonRooms):
        self.nonRooms = nonRooms
        
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
    
    def printClass(self):
        print("Class: " + self.department + " "+ str(self.number))
        print("Credits: " + str(self.numCredits))
        print("Number of Setions " + str(self.numSections))
        print("NonRooms: " + str(self.nonRooms))
        print("MWF_NonTimes: " + str(self.MWF_nonTimes))
        print("TTH_NonTimes: " + str(self.TR_nonTimes))
    
def getClasses(classDf):
    classDict={}
    
    MWF_times = classDf["MWF_Room-Time_Exceptions"]
    TR_times = classDf["TTh_Room-Time_Exceptions"]
    
    MWF_times = ht.handleTime(MWF_times)
    TR_times = ht.handleTime(TR_times)
    count = 0
    for row in classDf.iterrows():
        tempClass = Class(row[1][0][0:4], row[1][0][5:])
        tempClass.setNumCredits(row[1][1])
        tempClass.setNonClasses(row[1][2])
        tempClass.setMWF_nonTimes(MWF_times[count])
        tempClass.setTR_nonTimes(TR_times[count])
        tempClass.setNonRooms(row[1][5])
        tempClass.setNumSections(row[1][6])        
        tempClass.printClass()
        classDict[tempClass.getClass()]=count
        
        count+=1
        
        break
getClasses(data)
    