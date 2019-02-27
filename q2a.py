# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:28:09 2019

@author: TBattula
"""

'''
Write a programme to verify the file extension
'''


filename=input("Enter file name:")
ext=list(filename.split("."))
exts=ext[1]
print(type(exts))
if exts=='py':
    print('python')
elif exts=='txt':
    print("text file")
else :
    print("c file") 