# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:42:10 2019

@author: TBattula
"""
'''
Write a program to check the validity of password input by user.
Following are the criteria for checking the password:

1. At least 1 character from [$#@]
2. Minimum length of transaction password: 6
3. Maximum length of transaction password: 12


display "Valid password" if all the conditions are 
satisfied or "Invalid password"

'''

pwd=input("Enter the pwd")
len1=len(pwd)
print(len1)
char1=list(pwd.split())
print(char1)

if (('$' in pwd or '#' in pwd or '@' in pwd) and (len1>=6 or len1<=12)):
     print("Password is valid:",pwd)
     '''
else
print("Password is Invalid)