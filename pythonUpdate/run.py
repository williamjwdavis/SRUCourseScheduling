# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:20:28 2020

@author: willi
"""
import os
import sys

#we have to make sure the user is in the correct directory
workingPath = sys.argv[0]
workingPath = workingPath+"/../"

import buildTimeConstraints
import buildTimeDict
import buildTimeDict2
import roomInfo
import classInfo
import profInfo

#Build the null time pairs if they don't exist
if os.path.isfile(workingPath+"forbidden_pairs.pk1"):
    pass
else:
     buildTimeConstraints.run(workingPath)

#Build the time dictionaries if they don't exist
if os.path.isfile(workingPath+"dictionaries/timeEncodingDictFinal.pk1"):
    pass
elif os.path.isfile(workingPath+"dictionaries/timeEncodingDict.pk1"):
    buildTimeDict2.run(workingPath)
else:
    buildTimeDict.run(workingPath)
    buildTimeDict2.run(workingPath)

#Build room dictionary if it doesnt exist    
if os.path.isfile(workingPath+"dictionaries/roomDict.pk1"):
    pass
else:
    roomInfo.run(workingPath)
    
#Build the class dictionary if it doesnt exist
if os.path.isfile(workingPath+"dictionaries/classDict.pk1"):
    pass
else:
    classInfo.run(workingPath)
    
#Build the prof dictionaries if they don't exist
if os.path.isfile(workingPath+"dictionaries/profDict.pk1"):
    pass
else:
    profInfo.run(workingPath)

import exportToTxt as export
export.run(workingPath)