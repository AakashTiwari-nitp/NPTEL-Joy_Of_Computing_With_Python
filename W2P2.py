#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 18:08:22 2025

@author: aakash-tiwari
"""
"""
A high-security vault uses a custom PIN authentication mechanism. 
To reduce the chances of brute-force attacks, the system only allows PINs that are Neon Numbers.
The rule is:
A PIN is valid if the sum of the digits of its square equals the PIN itself.
Your Task: Write a Python program that reads a numeric PIN input by the user and validates whether it is a Neon Number or not.

"""
num = int(input("Enter the number to test: "))

sq = num*num

sum = 0
while (sq>0):
    rem = sq%10
    sum = sum + rem
    sq = sq//10
    
print(sum)
    
if(sum==num):
    print("The given number is a Neon Number.")
else:
    print("The given number is not a Neon Number.")