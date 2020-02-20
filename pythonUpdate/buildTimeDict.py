# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:28:56 2020

@author: willi
"""
import pickle

"""
This creates the timeEncodingDictionary according to the conventions listed in the documentation.
The conventions generally are: if it's a regular MWF, or MTThF course (i.e. course that is 
an hour in length even if it is 4 credits), time slot is denoted by 8M, 8W, etc. where the first
character(s) are the beginning time, and the second character(s) is the day of the week.  Next,
the 1.5 hour courses are encoded by their start time, 8, 930, etc, and then the day of the week,
T, R, followed by L, for long.  This is simply to differentiate the overlapping timeslots that 
cannot go together, but are still possibilities throughout the day.
"""

timeEncodingDict={}

#These values where manually decided upon for convention's sake.  
#While they are 'hard-coded' now, they can be referred to generally
#after this point

#This is for MTWRF classes that are 1 hour long
for i in range(9):
    for j in range(5):
        if (i==0):
            char1='8'
        elif (i==1):
            char1='9'
        elif (i==2):
            char1='10'
        elif (i==3):
            char1='11'
        elif (i==4):
            char1='12'
        elif (i==5):
            char1='1'
        elif (i==6):
            char1='2'
        elif (i==7):
            char1='3'
        elif (i==8):
            char1='4'
            
        if (j==0):
            char2='M'
        elif (j==1):
            char2='T'
        elif (j==2):
            char2='W'
        elif (j==3):
            char2='R'
        elif (j==4):
            char2='F'
        timeEncodingDict[char1+char2] = str(i)+str(j)
      
#This is for TR classes that are 1.5 hours long and thus encoded with the extra L
for i in range(5):
    for j in range(2):
        if (i==0):
            char1='8'
        elif (i==1):
            char1='930'
        elif (i==2):
            char1='11'
        elif (i==3):
            char1='2'
        elif (i==4):
            char1='330'
        if (j==0):
            char2="TL"
        elif (j==1):
            char2="RL"
        timeEncodingDict[char1+char2] = str(i)+str(j+5)
  
#Dump the dictionary into the files for us to use later      
f = open("dictionaries\timeEncodingDict.pk1",'wb')
pickle.dump(timeEncodingDict,f)
f.close()
        