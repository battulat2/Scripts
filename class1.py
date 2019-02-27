# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello")

val=10
b=2.3
c=val+b
print("c")

name ="Unix Shell Scripting"

print(name)

#syntax: name [start:stop:step]

print(name[0])
print(name[5])
print(name[0:5])
print(name[3:8])
print(name[-1])
print(name[0:12:2])
print(name[::])
print(name[::-1]) #reverse

## Concatination

first ="python"
second ="programming"

final = first + " "+second

print(final)

#list - set of numbers or set of strings or combinamtion. List elements are defined in []

alist = [10,20,30]
blist = ["unix","scala","spark", "hadoop"]
clist = [10,20,"unix","scala", 4000,56.44]

print(alist[0])

  #10
print(alist[1])

  #20
  
  alist[1]=100
  
  print(alist)
  print(alist +blist)
  
  #Single line comments
  
  '''
  This multiline comments
  Hi raa
  how are you?
  '''
  
  #Tuple - 
  #Tuple is defined in () whereas list is defined in []
  #Elements insertable cannot be modiifed which is basic differ b/w tuple and list
 
  atup = (10,20,30)
  btup = ("per1","java")
  
  atup[0] = 3000
  
  print("updated tuble:", atup)
  
  #Dictionary
  book = {"chap1": 10, "chap2": 20, "chap3" :30}
  data = {10:20,30:40, 50:60}

  book = {"chap1": 10, "chap2": 20, "chap3" :30, "chap1": 50}
print(book["chap1"])  


#adding key- value to the dictionary

book["chap4"] = 40

print("Updated dictionary :", book) 

book["chap5"] = (50,60, 70.77)

print("Updated dictionary :", book) 

alist = [[10,20],[30,50],[60,70]]
print(alist)
print(alist[0])
print(alist[0][0])




















