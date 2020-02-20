# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:39:01 2020

@author: willi
"""
import os
import pandas as pd
import numpy as np
import pickle

classes = pd.read_excel("SampleInput.xlsx",sheet_name = 'Classes')
profs = pd.read_excel("SampleInput.xlsx",sheet_name = 'Prof')
rooms = pd.read_excel("SampleInput.xlsx",sheet_name = 'Rooms')


f = open('dictionaries\classDict.pk1','rb')
classDict = pickle.load(f)
f.close()
f = open('dictionaries\profDict.pk1','rb')
profDict = pickle.load(f)
f.close()
f = open('dictionaries\roomDict.pk1','rb')
roomDict = pickle.load(f)
f.close()
f = open('dictionaries\timeEncodingDictFinal.pk1','rb')
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
    
File = open('matlabInput1.txt','a')
File.truncate(0)
inputs = ["nclasses = " + str(nclasses) + "\n",
          "ngroups = " + str(ngroups) + "\n",
          "nprofs = " + str(nprofs) + "\n",
          "ntimes = " + str(ntimes) + "\n",
          "nrooms = " + str(nrooms) + "\n",
          "forbidden_rooms_for_course = " + str(forbidden_rooms_for_course) + "\n",
          "forbidden_times_for_room = " + str(forbidden_times_for_room) + "\n",
          "forbidden_times_for_class = " + str(forbidden_times_for_class) + "\n",
          "forbidden_times_for_faculty = " + str(forbidden_times_for_faculty) + "\n",
          "forbidden_class_for_faculty = " + str(forbidden_class_for_faculty) + "\n",
          "forbidden_rooms_for_faculty = " + str(forbidden_rooms_for_faculty) + "\n",
          "c = " + str(c) + "\n",
          "required_courses_faculty = " + str(required_courses_faculty) + "\n",
          "forbidden_pairs = " + str(forbiddenPairs)]
File.writelines(inputs)
File.close()

FileIn = open('matlabInput1.txt','rt')
FileOut = open('matlabInput2.txt','wt')
for line in FileIn:
    FileOut.write(line.replace('None',''))
FileIn.close()
FileOut.close()

os.unlink('matlabInput1.txt')

FileIn = open('matlabInput2.txt','rt')
FileOut = open('matlabInput1.txt','wt')
for line in FileIn:
    FileOut.write(line.replace('[[','{['))
FileIn.close()
FileOut.close()

os.unlink('matlabInput2.txt')

FileIn = open('matlabInput1.txt','rt')
FileOut = open('matlabInput2.txt','wt')
for line in FileIn:
    FileOut.write(line.replace(',',''))
FileIn.close()
FileOut.close()

os.unlink('matlabInput1.txt')

FileIn = open('matlabInput2.txt','rt')
FileOut = open('matlabInputFinal.m','wt')
for line in FileIn:
    FileOut.write(line.replace(']]',']}'))
FileIn.close()
FileOut.close()
    
os.unlink('matlabInput2.txt')




    