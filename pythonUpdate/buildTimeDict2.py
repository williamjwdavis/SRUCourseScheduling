# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:41:17 2020

@author: willi
"""
import pandas as pd 
import pickle
import os
import directories as d

"""
buildTimeDict2 takes the dictionary created from the buildTimeDict.py 
and condenses it.  The purpose of having these two separate dicitonaries
is that in the first dictionary, we still understand what the keys and values mean,
and there is a predicatable relationship between the two.  During this round of 
encoding, the relationship is lost, as this dictionary is used purely for input
purposes in matlab.
"""
f = open(d.mainDirectory + 'dictionaries/timeEncodingDict.pk1','rb')
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

f = open(d.mainDirectory + 'dictionaries/timeEncodingDictFinal.pk1','wb')
pickle.dump(timeDict2,f)
f.close()