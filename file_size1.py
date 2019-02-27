# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:37:48 2019

@author: TBattula
"""
'''
import csv
with open("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets", "r") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)


import os
for file in os.listdir("C:\\Users\\tbattula\\Desktop\\Python_class\\datasets\\"):
    if file.endswith(".csv"):
        print(os.path.join("File name", file))
        
        '''
import os
for filename in os.listdir("C:\\Users\\tbattula\\Desktop\\Python_class\\"):
    os.rename(employees.csv, employees123.txt)