#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 23:14:49 2025

@author: aakash-tiwari
"""

"""
Problem Statement
You have a locker containing a number of coins. Each coin has a positive integer value engraved on it, representing its worth. You are required to determine whether it is possible to withdraw a subset of these coins such that their combined value is exactly equal to a target amount.

Function Specification
Write a recursive function named subset_sum that takes the following arguments:

L – a list of positive integers, where each integer represents the value of a coin.

s – a positive integer representing the target value.

The function should return True if it is possible to choose a subset of coins from the list whose sum is exactly s, and False otherwise.
"""

"""
def subset_sum(L, s):
    if s == 0:
        return True
    
    # Base case 2: If the list is empty or the current sum is negative, it's impossible.
    if not L or s < 0:
        return False
        
    return subset_sum(L[1:], s - L[0]) or subset_sum(L[1:], s)
"""

def subset_sum(L, s):
    if s == 0:
        return True
    if len(L) == 0:
        return False
    if subset_sum(L[:-1], s - L[-1]):  # include last coin
        return True
    else:  # exclude last coin
        return subset_sum(L[:-1], s)