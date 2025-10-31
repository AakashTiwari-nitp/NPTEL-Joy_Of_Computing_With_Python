#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 11:42:50 2025

@author: aakash-tiwari
"""

"""
Finbonacci Series
 0, 1, 1, 2, 3, 5, 8, 13
"""

def fibonacci(n):
    if(n<0):
        return "Not defined"
    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the Number: "))
print(f"The {n+1}th number of the fibonacci series is: {fibonacci(n)}")
    