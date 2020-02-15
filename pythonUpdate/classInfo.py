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
    nonClasses = []
    
    num_sections = 0
    
    def __init__(self, department, number):
        self.department = department
        self.number = number
        
    #Set functions including MWF and TR times that are correctly evaluated and
    #handled using handleTime.py
    def setNumCredits(self, numCredits):
        self.numCredits=numCredits
    def setMWF_nonclasses(self, MWF_list):
        self.MWF_nonTimes = ht.handleTime(MWF_list)
    def setTR_nonclasses(self, TH_list):
        self.TH_nonTimes = ht.handleTime(TH_list)
    def setNumSections(self, numSections):
        self.numSections = numSections
    def setNonClasses(self, nonClasses):
        self.nonClasses = nonClasses
        
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
    
def getClasses(classDf):
    classDict={}
    for row in classDf.iterrows():
        tempClass = Class(row[1][0][0:4], row[1][0][5:])
        tempClass.setNumCredits(row[1][1])
        tempClass.setNonClasses(row[1][2])
        tempClass.setMWF_nonclasses(row[1][3])
        tempClass.setTR_nonclasses(row[1][4])
        tempClass.setNumSections(row[1][5])
        
        print(row[1][0][0:4])
        print(row[1][1])
        print(row[1][2])
        print(row[1][3])
        break
getClasses(data)
    