# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:29:25 2019

@author: TBattula

write a program to capture any string from keyboard and write the output to the file.
"""

'''
fobj=open("demo123.txt","w")
#fobj=open("C:\\Users\\tbattula\\Desktop\\Python_class\\demo1.txt", "w")
txt=input("Enter the test")
fobj.write(txt)
fobj.close()

myinput=input("Enter string:")
fobj=open(r"C:\\Users\\tbattula\\Desktop\\Python_class\\demo1.txt",'w')
fobj.write(myinput)
fobj.close() 


----------------------------------------------
write a program to write all the odd numbers from 700 to 400 to the file and the
file name should be with today's timestamp.
Eg: 27_Feb_2019.txt
----------------------------------------------
'''
for val in range(701, 400, -2):
      print(val)
      

fobj=open("odd_numbers.txt","w")
#fobj=open("C:\\Users\\tbattula\\Desktop\\Python_class\\demo1.txt", "w")
for val in range(700, 400, -1):
    x=val
    print(val)
    
fobj.write(x)
fobj.close()

