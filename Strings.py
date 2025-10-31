#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:36:45 2025

@author: aakash-tiwari
"""

import string

s = "Raj"

print(s.lower()) # raj
print(s) # Raj

print(s.upper()) # RAJ
print(s) # Raj

sl = list(s)
print(sl) # ['R', 'a', 'j']

print(s.replace("j", "#")) # Ra#

print(s.replace("aj", "#")) # R#

print(s.replace("Ra", "#")) # #j 

print(s.replace("ra", "#")) # Raj

print(s.replace("Ra", "*#")) # *#j

print(s.replace("a", "*#")) # R*#j  

print(sl)

l = ['a', 'b', 'c', 'd', 'e', 'f']

print(l[1:4]) # ['b', 'c', 'd']

print(l[:4]) # ['a', 'b', 'c', 'd']

print(l[2:]) # ['c', 'd', 'e', 'f']

print(l[:]) # ['a', 'b', 'c', 'd', 'e', 'f']

print(l.index('d')) # 3 # return the index of first occurance only
 

