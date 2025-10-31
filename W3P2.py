#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 23:15:24 2025

@author: aakash-tiwari
"""

"""
At AeroPort-X, a futuristic logistics hub, drones are used to transport cargo based on weight. A team of engineers is working on a system that reads incoming weight values for parcels — often given as real numbers due to sensitive sensors. However,to fit them into standardized cargo containers, each weight must be rounded down to the nearest whole number — in other words, converted to the greatest integer less than or equal to it. Once converted, the numbers are displayed on a screen, separated by commas, for the loading team to arrange parcels efficiently.You are asked to build the logic for this conversion process.
Write a program that:
(a) Accepts a space-separated sequence of positive real numbers representing parcel
weights.
(b) Converts each number to the greatest integer less than or equal to it.
(c) Outputs the resulting integers, separated by commas.

"""

L = input("Enter the number sepearted by space: ").split(" ")
print(L)
for i in range(len(L)):
    L[i]= int(float(L[i]))

print(L)
"""    
L = ",".join(L)
print(L)
"""    

"""
for i in range(len(L)):
    if(i!=len(L)-1):
        print(L[i], end = ",")
    else:
        print(L[i])
"""

