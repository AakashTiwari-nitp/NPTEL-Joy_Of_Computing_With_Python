#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 02:03:09 2025

@author: aakash-tiwari
"""

"""
In the ancient city of Numerya, mathematicians and scholars explore the mystical properties of numbers. The Number Lore Library holds priceless scrolls about factors, which are believed to unlock numeric harmony.

You are the newly appointed Royal Scribe of Computation, and the scholars have entrusted you with building tools to help them. You must write a program that:

Finds all factors of a given positive integer.

Finds common factors of two positive integers.

Lists the factors for all numbers from 1 up to a given integer.

Your program will work based on a mode of operation chosen by the user:

Input Format:

First line: An integer choice (1, 2, or 3) indicating the operation:

1 → Find all factors of a given number.

2 → Find common factors of two given numbers.

3 → List factors for all numbers from 1 to a given number.

Based on the choice:

If choice = 1 → Read a single integer n.

If choice = 2 →  Read two integers a and b on separate lines (first enter a, press Enter, then enter b).

If choice = 3 → Read a single integer n.
"""

def get_factors(n):
    lst = []
    for i in range(1, n):
        if(n%i==0):
            lst.append(i)
    lst.append(n)
    return lst

def common_factors(a, b):
    common=[]
    lst1 = get_factors(a)
    lst2 = get_factors(b)
    for x in lst1:
        if x in lst2:
            common.append(x)
            
    return common

def list_all_factors(n):
    dict = {}
    for i in range(1, n+1):
        dict[i] = get_factors(i)
        
    return dict

choice = int(input("Enter your choice: "))

if choice == 1:
    n = int(input("Enter the number: "))
    print(get_factors(n))
elif choice == 2:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print(common_factors(n1, n2))
elif choice==3:
    n = int(input("Enter the number: "))
    print(list_all_factors(n))
