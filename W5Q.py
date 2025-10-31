#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 00:58:32 2025

@author: aakash-tiwari
"""

"""
def f(x):
    return x*3+1

print(f(1), f(2), f(3)) # 4, 7, 10
"""

"""
def weighted_sum(x, y = 2, z=3):
    return x + y*z

print(weighted_sum(1, z = 4)) # 9
"""

"""
def double(x):
    return x*2

def add_three(x):
    return x+3

def composed(x):
    return add_three(double(x))

print(composed(4)) # 11
"""

"""
import numpy as np
data = np.array([[10, 20], [30, 40]])
print(data.shape()) # It raises an error because .shape is not a function and cannot be called with ()
reshaped = data.reshape(4, 1)
print(reshaped.shape)
"""

"""
def manual_sum(lst):
    total = 0
    for i in lst:
        total = total + i
    return total

def process_list(L):
    squares = []
    for item in L:
        squares.append(item**2)
    return squares, manual_sum(squares)

result = process_list([1, 2, 3])
print(result[0][1], result[1]) # 4 14
"""

"""
def identity():
    return "Function is called"
identity_value = "Just a value"

print(identity) # <function identity at 0x7b50b7e8fc40>
print(identity()) # Function is called
print(identity_value()) # TypeError: 'str' object is not callable
""" 

"""
def message():
    return "This is a function"

message = "This is a message"

print(message()) # TypeError: 'str' object is not callable
"""

"""
def log_error(msg, log = []):
    log.append(msg)
    return log

print(log_error("E1")) 
print(log_error("E2"))
print(log_error("E3", []))

# ['E1']
# ['E1', 'E2']
# ['E3']
"""