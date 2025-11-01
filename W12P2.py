#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 08:00:11 2025

@author: aakash-tiwari
"""

"""
Week 12 : Programming Assignment 2
Due on 2025-10-16, 23:59 IST
Secure Sensor Data Analysis
In a secure data monitoring system, a network of sensors records values periodically. The values are stored in a list L, where each position in the list corresponds to a time slot.

To ensure data integrity, a special check is performed:
We identify all prime-numbered time slots (based on zero-indexing) and then count how many of those slots contain prime numbers themselves.

Your Task
Write a function:

def primes_galore(L)
that:

Accepts a list L of non-negative integers.

Finds all indices in L that are prime numbers (considering zero-based indexing).

Counts how many of those prime indices store prime numbers.

Returns this count.

 You may define and use helper functions (e.g., to check whether a number is prime).

Input Format
You do not need to take input from the user.

The function primes_galore(L) will be called directly with a list of integers.

Output Format
The function should return an integer: the count of prime indices that store prime numbers.

Constraints
Zero-based indexing is used.

An index and the number stored in it are considered separately for primality.

The list L may contain zero or more elements.
"""

def is_prime(x):
    if x <= 1:
        return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


def primes_galore(L):
    count = 0
    for i in range(len(L)):
        if is_prime(i) and is_prime(L[i]):
            count += 1
    return count