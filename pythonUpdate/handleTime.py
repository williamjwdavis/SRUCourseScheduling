# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:34:48 2020

@author: willi
"""
import pandas as pd
import os
import re
import pickle

cwd = os.getcwd()
temp = pd.read_excel(cwd+"\SampleInput.xlsx")

final=temp["MWF_Unavailable_Times"]

#Load in our time encoding dictionary
f = open('timeEncodingDict.pk1','rb')
timeEncodingDict = pickle.load(f)

def handleTime(series):
    """handleTime is expecting to be passed a dataFrame that is
    just a collection of times.  The function will output a similar 
    array that is just the corresponding time labels"""
    finalSeries=[]
    
    if (re.match("^MWF",final.name)):
        for char1 in final[0].split(','):
            finalSeries.append(char1+'M')
            finalSeries.append(char1+'W')
            finalSeries.append(char1+'F')
    elif (re.match("^TTh",final.name)):
        print("NO")
    else:
        print("Column Title Error - No MWF or TTh Detected")
        
    return

handleTime(final)