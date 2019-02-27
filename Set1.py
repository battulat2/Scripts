# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:36:23 2019

@author: TBattula
"""

#set - group of elements. set elements are defined in the {}. Indexing is not permitted.

aset = {10,20,30,40,10}

print(aset)

#removing duplicates - convert to the set

alist = [10,20,30,40,10,20]

print(set(alist))

#list - set conversion

print(tuple(alist))

final = tuple(alist)

print("tuple data:", final)

#string methods
#Everything is python is object
#every object contains set of methods


name = "PyThon"

print(name.upper()) #converting to upper case
print(name.casefold())
print(name.capitalize())
print(name)

name="unix, scala, spark, hadoop"

print(name.split(","))


name = "linux Programming"
print(name.strip())
print(name.replace("linux","python"))
print(name.find("in"))

a = [10,20,30,30,30]
print(a.count(30))

tuple1 = (1,2,3,4,4,4,4)

print("length of tuple",len(tuple1))

print("count of 2 in tuple",tuple1.count(4))

#how to get the list of built in functions and exceptions

print(dir(__builtin__))


alist = [10,20]

alist.append(30)
alist.append(40)

print("After appending:", alist)

alist.extend([50,60,70,10,10])

print("After extending:", alist)

print("count of 10:", alist.count(10))


#revers happends in place

alist.reverse()
c=alist.reverse()

print(alist)

print(alist.reverse())


print(c)

popitem = alist.pop(5)
print(popitem)






















