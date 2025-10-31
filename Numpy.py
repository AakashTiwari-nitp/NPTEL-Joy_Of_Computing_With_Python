#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:24:53 2025

@author: aakash-tiwari
"""

import numpy as np

l = [1, 2, 3]
print(l) # [1, 2, 3]

a = np.array([1, 2, 3])
print(a) # [1 2 3] # seperated by space not comma


print(type(l)) # <class 'list'>
print(type(a)) # <class 'numpy.ndarray'>

print(a.shape) # (3,)
print(a[0], a[1], a[2]) # 1 2 3

a[1] = 6
print(a) # 1 6 3

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape) # (2, 3)

a = np.zeros((2, 2))
print(a) # [[0. 0.]
         #  [0. 0.]]
         
b = np.ones((2, 3))
print(b) # [[1. 1. 1.]
         #  [1. 1. 1.]]
         
c = np.full((2, 3), 6)
print(c) # [[6 6 6]
         #  [6 6 6]]
         
d = np.random.random((2,3))
print(d) # [[0.21055169 0.85369346 0.87075439]
         #  [0.03326483 0.62161622 0.87426721]]