# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:57:17 2019

@author: TBattula
"""
'''

Write a program to capture the string and output in terms of list

Enter any list : perl, unix, spark, scala
List Output :['perl','unix','spark', 'scala']Length of list :4

'''

alist = input("Enter any list :")

blist = alist.split(",")
print(list(blist))
print(len(blist))