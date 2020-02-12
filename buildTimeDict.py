# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:28:56 2020

@author: willi
"""
import pickle

timeEncodingDict={}

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
        
f = open("timeEncodingDict.pk1",'wb')
pickle.dump(timeEncodingDict,f)
f.close()
        