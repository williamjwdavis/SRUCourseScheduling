# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:30:59 2020

@author: willi
"""
import os
import pandas as pd
import numpy as np
import pickle

classes = pd.read_excel("SampleInput.xlsx",sheet_name = 'Classes')
profs = pd.read_excel("SampleInput.xlsx",sheet_name = 'Prof')
rooms = pd.read_excel("SampleInput.xlsx",sheet_name = 'Rooms')


f = open('dictionaries/classDict.pk1','rb')
classDict = pickle.load(f)
f.close()
f = open('dictionaries/profDict.pk1','rb')
profDict = pickle.load(f)
f.close()
f = open('dictionaries/roomDict.pk1','rb')
roomDict = pickle.load(f)
f.close()
f = open('dictionaries/timeEncodingDict.pk1','rb')
timeEncodingDictEarly = pickle.load(f)
f.close()
f = open('dictionaries/timeEncodingDictFinal.pk1','rb')
timeEncodingDict = pickle.load(f)
f.close()
f = open('forbidden_pairs.pk1','rb')
forbiddenPairs = pickle.load(f)
f.close()

nclasses = np.sum(classes["Num_Sections"])
ngroups = len(classes)
nprofs = len(profs)
ntimes = len(timeEncodingDict)
nrooms = len(rooms)

forbidden_rooms_for_course = []
for i in range(len(classDict)):
    forbidden_rooms_for_course.append(classDict[i+1].getNonRooms())

forbidden_times_for_room = []
for i in range(len(roomDict)):
    forbidden_times_for_room.append(roomDict[i+1].getAllTimeConflicts())
    
forbidden_times_for_class = []
for i in range(len(classDict)):
    forbidden_times_for_class.append(classDict[i+1].getAllTimeConflicts())

forbidden_times_for_faculty = []
for i in range(len(profDict)):
    forbidden_times_for_faculty.append(profDict[i+1].getAllTimeConflicts())
    
forbidden_class_for_faculty = []
for i in range(len(profDict)):
    forbidden_class_for_faculty.append(profDict[i+1].getNonClasses())
    
forbidden_rooms_for_faculty = []
for i in range(len(profDict)):
    forbidden_rooms_for_faculty.append(profDict[i+1].getNonRooms())
    
c = [] #c is the number of credits of class i 
for i in range(len(classDict)):
    c.append(classDict[i+1].getNumCredits())
    
required_courses_faculty = []
for i in range(len(profDict)):
    required_courses_faculty.append(profDict[i+1].getReqClasses())
    
forbidden_pairs_rooms = []
alreadySeen={}
for i in range(nrooms):
    for j in range(nrooms):
        if i==j:
            pass
        else:
            if (str(j)+" "+str(i)) in alreadySeen.keys():
                pass
            else:
                forbidden_pairs_rooms.append([i+1,j+1])
                alreadySeen[str(i)+" "+str(j)]=1

forbidden_pairs_prof = []
alreadySeen={}
for i in range(nprofs):
    for j in range(nprofs):
        if i==j:
            pass
        else:
            if (str(j)+" "+str(i)) in alreadySeen.keys():
                pass
            else:
                forbidden_pairs_prof.append([i+1,j+1])
                alreadySeen[str(i)+" "+str(j)]=1

restricted_pairs_of_classes=[]
for i in range(len(classDict)):
    if classDict[i+1].getNonClasses() == []:
        pass
    else:
        for ele in classDict[i+1].getNonClasses():
            if ele == None:
                pass
            else:    
                restricted_pairs_of_classes.append([i+1,ele])
                
load_upper=[]
for i in range(len(profDict)):
    load_upper.append(profDict[i+1].getMaxLoad())
    
load_lower=[]
for i in range(len(profDict)):
    load_lower.append(profDict[i+1].getMinLoad())

Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []

for key in timeEncodingDictEarly.keys():
    if key[len(key)-1] == 'M':
        Monday.append(timeEncodingDict[timeEncodingDictEarly[key]])
    elif (key[len(key)-1]=="T") | (key[len(key)-2]=='TL'):
        Tuesday.append(timeEncodingDict[timeEncodingDictEarly[key]])
    elif (key[len(key)-1]=="W"):
        Wednesday.append(timeEncodingDict[timeEncodingDictEarly[key]])
    elif (key[len(key)-1]=="R") | (key[len(key)-2]=='RL'):
        Thursday.append(timeEncodingDict[timeEncodingDictEarly[key]])
    elif (key[len(key)-1]=="F"):
        Friday.append(timeEncodingDict[timeEncodingDictEarly[key]])

#FIXME fix day={Monday, Wednesday, Friday}
groups=[]
count = 1
for item in range(len(classDict)):
    temp = []
    for i in range(classDict[item+1].getNumSections()):
        temp.append(count+i)
        if classDict[item+1].getNumSections()>1:
            pass
        else:
            count+=1
    groups.append(temp)
    
maxPreps = []
for i in range(len(profDict)):
    maxPreps.append(profDict[i+1].getMaxPreps())
    
longCourses = []
regCourses = []
for key in timeEncodingDictEarly.keys():
    if key[len(key)-1]=="L":
        longCourses.append(timeEncodingDict[timeEncodingDictEarly[key]])
    else:
        regCourses.append(timeEncodingDict[timeEncodingDictEarly[key]])
