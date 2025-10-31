#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 22:14:39 2025

@author: aakash-tiwari
"""

def checkNum(num):
    iterations = 1
    while(num!=1):
        if num%2:
            num = 3*num + 1
        else:
            num = num//2
        iterations+= 1 
        
    print(num, iterations)
    
print(checkNum(7))