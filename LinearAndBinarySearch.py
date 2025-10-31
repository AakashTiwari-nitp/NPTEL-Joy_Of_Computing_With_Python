#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 22:19:09 2025

@author: aakash-tiwari
"""

def linear_search(a, target):
    n = len(a)
    flag = 0
    count = 0
    for i in range(n):
        count+=1
        if(a[i]==target):
            flag = 1
            print("The number found at position: ", i+1)
            break
        
    if(flag == 0 ):
        print("Number is not present in the array")
        
    print("Number of iterations: ", count)
    
def binary_search(a, target):
    n = len(a)
    flag = 0 # flag = 0 means element has been not fount yet
    
    count = 0
    low = 0
    high = n - 1
    while(low<=high and flag == 0):
        count+= 1
        mid = (low + high)//2
        if(a[mid] == target):
            flag = 1
            print("The number found at position: ", mid+1)
            break
        elif(a[mid]<target):
            low = mid + 1
        elif(a[mid]>target):
            high = mid - 1
        
    if(flag == 0 ):
        print("Number is not present in the array")
        
    print("Number of iterations: ", count)
            

elements = []
for i in range(1, 1001):
    elements.append(i)

#print(elements)

target = int(input("Enter the number you want to search in the array: "))
linear_search(elements, target)
binary_search(elements, target)