# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:00:49 2020

@author: willi
"""
import pickle
import pandas as pd
import handleTime as ht


class Room():
    #these are the attributes that we'll describe a room with
    #we can build these out in the future but that'll also 
    #require additional methods to encorporate them
    roomName = ''
    MWF_nonTimes = []
    TR_nonTimes = []
    all_nonTimes = [] #All_nonTimes should only contain the double encoded times
    
    def __init__(self, roomName):
        self.roomName = roomName
    
    #setters
    def setMWF_nonTimes(self, nonTimes):
        self.MWF_nonTimes = nonTimes
    def setTR_nonTimes(self, nonTimes):
        self.TR_nonTimes = nonTimes
    def setAll_nonTimes(self):
        self.all_nonTimes = self.MWF_nonTimes + self.TR_nonTimes
    
    #getters
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
    
    #get the time requirements from the Excel doc
    MWF_nonTimes = roomDf["MWF_Room-Time_Exceptions"]
    TR_nonTimes = roomDf["TTh_Room-Time_Exceptions"]
    
    #run the dataframes through the preprocessing from
    #handTime.py
    MWF_nonTimes = ht.handleTimeAll(MWF_nonTimes)
    TR_nonTimes = ht.handleTimeAll(TR_nonTimes)
    count = 1
    
    #iterate through the rows of the Excel doc and 
    #build an object using each cell of the row and 
    #finally add it to the array
    for row in roomDf.iterrows():
        tempRoom = Room(row[1][0])
        tempRoom.setMWF_nonTimes(MWF_nonTimes[count-1])
        tempRoom.setTR_nonTimes(TR_nonTimes[count-1])
        tempRoom.setAll_nonTimes()
        #tempRoom.printRoom()
        roomDict[count] = tempRoom
        
        count+=1
        
    return roomDict

def run(path):
    data = pd.read_excel(path + "Input.xlsx",sheet_name='Rooms')
    
    roomDict = makeRooms(data)
    f = open(path + 'dictionaries/roomDict.pk1','wb')
    pickle.dump(roomDict,f)
    f.close()
    