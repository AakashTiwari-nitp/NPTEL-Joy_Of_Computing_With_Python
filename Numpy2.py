#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:39:44 2025

@author: aakash-tiwari
"""

import numpy as np

x = np.array([1, 2])

print(x.dtype) # int64

x = np.array([1.0, 2.0])
print(x.dtype) # float64

x = np.array([1, 3], dtype=np.int32)

print(x.dtype) # int32

x = np.array([[1, 2], [3, 4]], dtype = np.float64)

y = np.array([[5, 6], [7, 8]], dtype = np.float64)

print(x+y) # [[ 6.  8.]
           #   [10. 12.]]
           
print(np.add(x, y)) #[[ 6.  8.]
                    # [10. 12.]]

print(np.subtract(x, y)) # [[-4. -4.]
                         #  [-4. -4.]]

print(np.multiply(x, y)) # [[ 5. 12.]
                         #  [21. 32.]]
                         
print(np.divide(x, y)) # [[0.2        0.33333333]
                       #   [0.42857143 0.5       ]]
                       
print(np.sqrt(x)) # [[1.         1.41421356]
                  #   [1.73205081 2.        ]]

x = np.array([[1, 2], [3, 4]])
print(x.T) # [[1 3]
           #  [2 4]]
           
print(np.sum(x)) # 10

print(np.sum(x, axis=0)) # [4 6] # column sum
print(np.sum(x, axis=1)) # [3 7] # row sum