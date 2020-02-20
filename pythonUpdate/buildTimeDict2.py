# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:41:17 2020

@author: willi
"""
import pandas as pd 
import pickle
import os

f = open('timeEncodingDict.pk1','rb')
timeDict = pickle.load(f)
f.close()

timeDict2 = {}

count = 1
for i in range(9):
    for j in range(7):
        if (j>4):
            if(i<5):
                timeDict2[str(i)+str(j)]=count
                count+=1
            else:
                pass
        else:    
            timeDict2[str(i)+str(j)] = count
            count+=1

f = open('dictionaries\timeEncodingDictFinal.pk1','wb')
pickle.dump(timeDict2,f)
f.close()