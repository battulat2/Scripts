# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:21:20 2019

@author: TBattula
"""
'''
name = "python is general purpose and python is interactive and python is cross 	platform language"
-write a program to count all the occurences of python in the above string.
-write a program to count all the no. of words in the above string.
-convert the string to uppercase
-replace python with spark and display the output



name =input("Enter the name:")
print(name)
print(name.upper())
print(name.replace('python','spark'))


name =input("Enter the name:")
print(name.count('python'))
x=name.split()
y=len(name.split())
print("x:",x)
print("y:",y)
print(len(name.split()))



write a program to read anyfile ( employees.log ) and convert its extension to
employees.csv

Enter any filename : employees.log
new file           : employees.csv

'''

name =input("Enter any filename:")
print(name)
x=list(name.split("."))
print(x)
y=name.replace(x[1], "csv")
print(y)
