#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 10:32:21 2025

@author: aakash-tiwari
"""

def binary_search(a, target, start, end): 
    if(start>= len(a) or end<0):
        return f"The {target} is not present in the list"
    if (start==end):
        if (start> 0 and a[start]==target):
            return f"The {target} found at index {start}"
        else:
            return f"The {target} is not present in the list"
    else:
        mid = (start + end)//2
        if (a[mid]==target):
            return f"The {target} found at index {mid}"
        elif (a[mid]>target):
            return binary_search(a, target, start, mid-1)
        elif (a[mid]<target):
            return binary_search(a, target, mid+1, end)
        
a = [20, 30, 50, 70, 80]
target= int(input("Enter the element to search in the list: "))
print(binary_search(a, target, 0, len(a)-1)) 
    