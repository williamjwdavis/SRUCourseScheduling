# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:34:48 2020

@author: willi
"""
import os
import re
import pickle

cwd = os.getcwd()


#temp = pd.read_excel(cwd+"\SampleInput.xlsx")
#final=temp["MWF_Unavailable_Times"]
#final=temp["TTh_Unavailable_Times"]
#Load in our time encoding dictionary
f = open('timeEncodingDict.pk1','rb')
timeEncodingDict = pickle.load(f)

def handleTime(final):
    """handleTime is expecting to be passed a dataFrame that is
    just a collection of times.  The function will output a similar 
    array that is just the corresponding encoded time labels"""
    finalSeries = []
    
    #This handles columns that correspond to MWF times
    if (re.match("^MWF",final.name)):
        for cellNum in range(len(final)):            
            tempInnerSeries=[]
            try:
                for char1 in final[cellNum].split(','):
                #Takes 
                    tempInnerSeries.append(char1+'M')
                    tempInnerSeries.append(char1+'W')
                    tempInnerSeries.append(char1+'F')
            except AttributeError:
                tempInnerSeries.append(str(final[cellNum])+'M')
                tempInnerSeries.append(str(final[cellNum])+'W')
                tempInnerSeries.append(str(final[cellNum])+'F')
            finalSeries.append(tempInnerSeries)
            #final series is a series of the encoded times , i.e. 8M or 12W
    
    #This handles columns that correspond to TTh times
    elif (re.match("^TTh",final.name)):
        for cellNum in range(len(final)):            
            tempInnerSeries=[]
            try:
                for char1 in final[cellNum].split(','):
                    tempInnerSeries.append(char1+'T')
                    tempInnerSeries.append(char1+'R')
                    if(char1==8):
                        tempInnerSeries.append(char1+'TL')
                        tempInnerSeries.append(char1+'RL')
                    elif(char1==9):
                        tempInnerSeries.append('8TL')
                        tempInnerSeries.append('930TL')
                        tempInnerSeries.append('8RL')
                        tempInnerSeries.append('930RL')
                    elif(char1==10):
                        tempInnerSeries.append('930TL')
                        tempInnerSeries.append('930RL')
                    elif(char1==11):
                        tempInnerSeries.append(char1+'TL')
                        tempInnerSeries.append(char1+'RL')
                    elif(char1==12):
                        tempInnerSeries.append('11TL')
                        tempInnerSeries.append('11RL')
                    elif(char1==1):
                        pass
                    elif(char1==2):
                        tempInnerSeries.append(char1+'TL')
                        tempInnerSeries.append(char1+'RL')
                    elif(char1==3):
                        tempInnerSeries.append('2TL')
                        tempInnerSeries.append('2RL')
                        tempInnerSeries.append('330TL')
                        tempInnerSeries.append('330RL')
                    elif(char1==4):
                        tempInnerSeries.append('330TL')
                        tempInnerSeries.append('330RL') 
            except AttributeError:
                tempInnerSeries.append(str(final[cellNum])+'T')
                tempInnerSeries.append(str(final[cellNum])+'R')
                if(final[cellNum]==8):
                    tempInnerSeries.append(str(final[cellNum])+'TL')
                    tempInnerSeries.append(str(final[cellNum])+'RL')
                elif(final[cellNum]==9):
                    tempInnerSeries.append('8TL')
                    tempInnerSeries.append('930TL')
                    tempInnerSeries.append('8RL')
                    tempInnerSeries.append('930RL')
                elif(final[cellNum]==10):
                    tempInnerSeries.append('930TL')
                    tempInnerSeries.append('930RL')
                elif(final[cellNum]==11):
                    tempInnerSeries.append(str(final[cellNum])+'TL')
                    tempInnerSeries.append(str(final[cellNum])+'RL')
                elif(final[cellNum]==12):
                    tempInnerSeries.append('11TL')
                    tempInnerSeries.append('11RL')
                elif(final[cellNum]==1):
                    pass
                elif(final[cellNum]==2):
                    tempInnerSeries.append(str(final[cellNum])+'TL')
                    tempInnerSeries.append(str(final[cellNum])+'RL')
                elif(final[cellNum]==3):
                    tempInnerSeries.append('2TL')
                    tempInnerSeries.append('2RL')
                    tempInnerSeries.append('330TL')
                    tempInnerSeries.append('330RL')
                elif(final[cellNum]==4):
                    tempInnerSeries.append('330TL')
                    tempInnerSeries.append('330RL') 
            finalSeries.append(tempInnerSeries)
    else:
        print("Column Title Error - No MWF or TTh Detected")
    
    decodedFinalSeries=[]
    for series in finalSeries:
        decodedSeries=[]
        for ele in series:
            decodedTime=timeEncodingDict[ele]
            decodedSeries.append(decodedTime)
        decodedFinalSeries.append(decodedSeries)
            
    return decodedFinalSeries