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
    
    def calcNonClasses(self):
        pass
    
    def setMWF_nonTimes(self, nonTimes):
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        self.TR_nonTimes = nonTimes
    def setNonRooms(self, nonRooms):
        self.nonRooms = nonRooms
    def setNonClasses(self, nonClasses):
        self.nonClasses = nonClasses
        
    
        