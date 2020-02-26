# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:00:49 2020

@author: willi
"""
import os
import pickle
import pandas as pd
import handleTime as ht

cwd = os.getcwd()
data = pd.read_excel("SampleInput.xlsx",sheet_name='Rooms')

class Room():
    roomName = ''
    MWF_nonTimes = []
    TR_nonTimes = []
    all_nonTimes = [] #All_nonTimes should only contain the double encoded times
    
    def __init__(self, roomName):
        self.roomName = roomName
    
    def setMWF_nonTimes(self, nonTimes):
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        self.TR_nonTimes = nonTimes
    def setAll_nonTimes(self):
        self.all_nonTimes = self.MWF_nonTimes + self.TR_nonTimes
    
    def getRoom(self):
        return self.roomName
    def getAllTimeConflicts(self):
        return self.all_nonTimes    
    
    def printRoom(self):
        print("Room: " + self.roomName)
        print("MWF NonTimes: " + str(self.MWF_nonTimes))
        print("TTh NonTimes: " + str(self.TR_nonTimes))
    
def makeRooms(roomDf):
    roomDict = {}
    
    MWF_nonTimes = roomDf["MWF_Room-Time_Exceptions"]
    TR_nonTimes = roomDf["TTh_Room-Time_Exceptions"]
    
    MWF_nonTimes = ht.handleTimeAll(MWF_nonTimes)
    TR_nonTimes = ht.handleTimeAll(TR_nonTimes)
    count = 1
    
    for row in roomDf.iterrows():
        tempRoom = Room(row[1][0])
        tempRoom.setMWF_nonTimes(MWF_nonTimes[count-1])
        tempRoom.setTR_nonTimes(TR_nonTimes[count-1])
        tempRoom.setAll_nonTimes()
        #tempRoom.printRoom()
        roomDict[count] = tempRoom
        
        count+=1
        
    return roomDict

roomDict = makeRooms(data)
f = open('dictionaries/roomDict.pk1','wb')
pickle.dump(roomDict,f)
f.close()
    