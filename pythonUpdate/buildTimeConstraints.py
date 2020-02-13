# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:55:39 2020

@author: willi
"""
import pickle

f = open('timeEncodingDict.pk1','rb')
timeEncodingDict = pickle.load(f)
f.close()

forbidden_pairs = []
allowedPairsDict = {}

"""
The first set of nested loops simply allows all of the classes that are together by a simple
pattern of matching times, and matching key lengths.  This serves as a unique identifier for 
all of the encoded times and lets us record the possible time slots for each time slot.  This
information is stored in allowedPairsDict
"""
for outerEle in timeEncodingDict.keys():
    for innerEle in timeEncodingDict.keys():
        if (outerEle == innerEle):
            pass
        else:
            if ((outerEle[0]==innerEle[0])&(len(outerEle)==len(innerEle))):
                allowedPairsDict[timeEncodingDict[outerEle] + " " + timeEncodingDict[innerEle]] = 1
                #forbidden_pairs.append([timeEncodingDict[outerEle] + " " + timeEncodingDict[innerEle]])

"""
Next the allowedPairsDict is passed to this set of nested loops where the system returns all
the forbiddenPairs.  This is simple enough, however the strings and characters are modified
a bit in order to pass nicely off to matlab
"""
for outerEle in timeEncodingDict.keys():
    for innerEle in timeEncodingDict.keys():
        if (outerEle == innerEle):
            pass
        else:
            key = timeEncodingDict[outerEle]+" "+timeEncodingDict[innerEle]
            temp1 = timeEncodingDict[outerEle]
            temp2 = timeEncodingDict[innerEle]
            
            if (int(timeEncodingDict[outerEle]))<10:
                temp1 = timeEncodingDict[outerEle][1]
            if (int(timeEncodingDict[innerEle]))<10:
                temp2 = timeEncodingDict[innerEle][1]
                
            if key in allowedPairsDict:
                pass
            else:
                forbidden_pairs.append(temp1+' '+temp2)
                
f = open("forbidden_pairs.pk1",'wb')
pickle.dump(forbidden_pairs,f)
f.close()

