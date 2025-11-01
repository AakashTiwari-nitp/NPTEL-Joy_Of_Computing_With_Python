#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 07:49:42 2025

@author: aakash-tiwari
"""

"""
Goldbach’s Conjecture
Problem Statement:
Goldbach’s conjecture is one of the oldest and best-known unsolved problems in number theory. It states that every even number greater than 2 is the sum of two prime numbers.

Your Task:
Write a function Goldbach(n) where n is a positive even number (n > 2) that returns a list of tuples. Each tuple (a, b) should satisfy:

a ≤ b

Both a and b are prime numbers

a + b = n

The tuples should be returned in sorted order.

Notes:

n will always be an even integer greater than 2.

Both numbers in a tuple must be prime.

Return the tuples in sorted order.

You need to take the input n from the user.

Print the output.      
"""

def prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def Goldbach(n):
    Res = []
    for i in range((n // 2) + 1):
        if prime(i) and prime(n - i):
            Res.append((i, n - i))
    return Res

print(Goldbach(100)) # [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]