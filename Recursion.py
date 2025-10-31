#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 10:11:46 2025

@author: aakash-tiwari
"""

"""
def factorial(n):
    if(n<0):
        return f"Factorial is not defined for {n}"
    product = 1
    for i in range(1, n+1):
        product*=i
    return product
"""

"""
base case or the anchor case:
    the case where the recursion stops
"""

def factorial(n):
    if(n==0):
        return 1
    elif (n>=1):
        return n*factorial(n-1)
    else:
        return f"Factorial is not defined for {n}"

print(factorial(5))