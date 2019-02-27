# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:26:52 2019

@author: TBattula
"""
##Method1
import math
print(math.ceil(4.9))
print(math.tan(4.9))
print(math.log(4.9))



##Method2 - Accessing methods with alias name
import math as m

print(m.ceil(4.9))
print(m.tan(4.9))
print(m.log(4.9))

#Metho3 - Importing only required methods
# . is not required here
from math import ceil, log
print(m.ceil(4.9))
print(m.log(4.9))


#Metho4 - Importing all  methods
# . is not required here
from math import *
print(m.ceil(4.9))
print(m.log(4.9))

import os
# from the current path
print(os.listdir())

# from the C: path
print(os.listdir("c:\\"))

# remove the file
os.unlink("test12333.py")
