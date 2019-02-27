# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:43:36 2019

@author: TBattula
"""
'''
import os
for file in os.listdir():
    if os.path.isfile(file):
        filsize=os.path.getsize(file)
        print("Filename", file
              )
 '''
 
import os
for file in os.listdir():
    if os.path.isfile(file):
        filesize = os.path.getsize(file)
        print("Filename :", file)
        print("size     :", filesize , "bytes")
        print("----------------------")