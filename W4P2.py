#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 12:08:15 2025

@author: aakash-tiwari
"""

"""
In the mystical realm of Numbertown, numbers are not just mathematical entities — they possess personalities. Among them, Perfect Numbers are considered rare and noble.

A perfect number is one whose value is equal to the sum of all its proper divisors (excluding itself).
For example:

6 = 1 + 2 + 3

Function Requirements
Write a Python function named is_perfect that:

Accepts a positive integer n as input.

Returns True if n is a perfect number.

Returns False otherwise.
"""

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if (num%i==0):
            sum+=i
            
    return sum==num

print(is_perfect(8128))
print(is_perfect(14))
print(is_perfect(100))
print(is_perfect(128))