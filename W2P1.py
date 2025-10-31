#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 17:58:13 2025

@author: aakash-tiwari
"""

num = int(input("Enter the number of Over: "))
sum = 0
for i in range(1, num+1):
    if (i%2):
        sum = sum + i
    
print(sum)