#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:48:57 2025

@author: aakash-tiwari
"""

"""
Problem: Searching Patient Records in a Health Analytics System
The hospital network MedNexus maintains a centralized database of patient record IDs.
These IDs are stored in sorted order to enable fast lookups.

You are part of the software development team tasked with optimizing the search functionality.
Since the system follows a recursive design pattern, you must implement a recursive version of the search algorithm to determine whether a given patient ID exists in the records.

Requirements
Function Name: search

Parameters:

L → A sorted list of integers (patient record IDs).

k → An integer representing the ID to search for.

Return Value:

Return True if k is present in L.

Return False if k is not present.

Constraints:

Must use recursion.

No need to accept input from the user.

No need to print output to the console. Only the function definition is required.
"""

def Search(L, K):
    if len(L)==0:
        return False
    
    left = 0
    right = len(L) -1
    mid = (left + right)//2
    
    if(L[mid]==K):
        return True
    elif(L[mid]>K):
        right = mid-1
    elif(L[mid]<K):
        left = mid+1
        
    return Search(L[left:right+1], K)

L = input("Enter the number seperated by comma: ").split(",")

for i in range(len(L)):
    L[i]  = int(L[i])
    
K = int(input("Enter the number to search: "))

print(Search(L, K))


    