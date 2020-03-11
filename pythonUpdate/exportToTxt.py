# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:39:01 2020

@author: willi
"""
import classInfo
import profInfo
import roomInfo
import createInputVars as var
import os


File = open('matlabInput1.txt','a')
#deletes the previous file
File.truncate(0)

#take the inputs from createInputVars.py and plug them into
#the final that we're exporting
inputs = ["nclasses = " + str(var.nclasses) + ";\n",
          "ngroups = " + str(var.ngroups) + ";\n",
          "nprofs = " + str(var.nprofs) + ";\n",
          "ntimes = " + str(var.ntimes) + ";\n",
          "nrooms = " + str(var.nrooms) + ";\n",
          "forbidden_rooms_for_course = " + str(var.forbidden_rooms_for_course) + ";\n",
          "forbidden_times_for_room = " + str(var.forbidden_times_for_room) + ";\n",
          "forbidden_times_for_class = " + str(var.forbidden_times_for_class) + ";\n",
          "forbidden_times_for_faculty = " + str(var.forbidden_times_for_faculty) + ";\n",
          "forbidden_class_for_faculty = " + str(var.forbidden_class_for_faculty) + ";\n",
          "forbidden_rooms_for_faculty = " + str(var.forbidden_rooms_for_faculty) + ";\n",
          "c = " + str(var.c) + ";\n",
          "required_courses_faculty = " + str(var.required_courses_faculty) + ";\n",
          "forbidden_pairs_rooms = " + str(var.forbidden_pairs_rooms) + ";\n",
          "forbidden_pairs_prof = " + str(var.forbidden_pairs_prof) + ";\n",
          "restricted_pairs_of_classes = " + str(var.restricted_pairs_of_classes) + ";\n",
          "load_upper = " + str(var.load_upper) + ";\n",
          "load_lower = " + str(var.load_lower) + ";\n",
          "Monday = " + str(var.Monday) + ";\n",
          "Tuesday = " + str(var.Tuesday) + ";\n",
          "Wednesday = " +str(var.Wednesday) + ";\n",
          "Thursday = " + str(var.Thursday) + ";\n",
          "Friday = " + str(var.Friday) + ";\n",
          "groups = " + str(var.groups) + ";\n",
          "maxPreps = " + str(var.maxPreps) + ";\n",
          "longCourses = " + str(var.longCourses) + ";\n",
          "regCourses = " +str(var.regCourses) + ";\n",
          "forbidden_pairs = " + str(var.forbiddenPairs) +";"]
File.writelines(inputs)
File.close()


"""
This whole shpiel is just text organization to take the python output
and turn it into a matlab format that won't yell at me
"""
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




    