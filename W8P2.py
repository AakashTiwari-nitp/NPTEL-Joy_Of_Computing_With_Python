#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 23:16:32 2025

@author: aakash-tiwari
"""

"""
Week 8: Programming Assignment 2
Collatz Function
The Collatz function is defined for any positive integer n as:
                       
                       f(n)  =       3n + 1 , if n is odd
                                        n / 2    , if n is even
We repeatedly apply the function f starting from an integer n, producing a sequence:
                                   f(n), f(f(n)), f(f(f(n))), . . .

It is believed (but not proven) that no matter which positive number you start with, this sequence will always eventually reach 1.

Example:
If n = 10, the sequence is:

10 → 5 → 16 → 8 → 4 → 2 → 1
Starting at n = 10, we must apply the function f six times to reach 1.

Your Task
Write a recursive function named collatz that:

Accepts a positive integer n such that: 1 < n ≤ 32,000

Returns the number of times the function f needs to be applied to reach 1.

Requirements
Do not print anything or take input from the user.

Only write the function definition.

Use recursion in your solution.
"""

def collatz(n):
    if n==1:
        return 0
    elif n%2:
        return 1+collatz(3*n + 1)
    else:
        return 1+collatz(n//2)
    
print(collatz(19)) # 20