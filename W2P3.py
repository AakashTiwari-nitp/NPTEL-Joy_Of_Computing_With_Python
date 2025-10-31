#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 19:03:14 2025

@author: aakash-tiwari
"""

"""
Due on 2025-08-07, 23:59 IST
While analysing intercepted communications, TASC officer Srikant Tiwari suspects that some messages might be carrying hidden signals. One of the red flags used by the agency is the density of vowels in a message — unusually high vowel counts may indicate a coded alert.
To assist in screening these messages quickly, a script is needed to count the number of vowels in any given string.
Write a Python program that:
Takes a message as input.
Counts the number of vowels (a, e, i, o, u — both uppercase and lowercase).
Prints the vowel count.
"""

str = input("Enter the string you want to test:")
str.lower()

cnt = 0

# for ch in str:
#   if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#        cnt+= 1

vowels = "aeiouAEIOU"

for ch in str:
    if(ch in vowels):
        cnt+= 1
        
print(cnt)
        