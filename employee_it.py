# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:46:40 2019

@author: TBattula
write a program to read the file and replace the lines containing "Business 

Development"  to "Information technology" and write the output to other file.

"""
'''

fobj=open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees.csv", "r")
for line in fobj:
     x=line.replace("Business Development", "Information technology")
     fobj=open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees_it.csv", "w")
     fobj.write(x)
     fobj.close()
    #if line in ("Business Development"):
fobj.close()
'''


fr=open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees.csv", "r")
fw=open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\employees_it.csv", "w")
for line in fr:
    line=line.strip()
    line=line.replace("Business Development", "Information technology")
    fw.write(line)
fw.close()
fr.close()
     