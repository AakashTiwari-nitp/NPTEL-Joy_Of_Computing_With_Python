#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 23:19:24 2025

@author: aakash-tiwari
"""

"""
Week 8: Programming Assignment 3
Problem: Twin Primes
Two numbers p and q are said to be twin primes if:

Both p and q are prime numbers, and

The absolute difference between them is 2, i.e., |p − q| = 2.

Task
Write a function twin_primes(p, q) that:

Accepts two integers p and q as arguments,

Returns True if they are twin primes, and False otherwise.

      Note:

The function should not print anything.

The function should not accept input from the user.You may use helper functions if needed.

You only need to write the function definition.  .
"""

def isPrime(n):
  if (n<=1):
    return False
  if (n<=3):
    return True
  if (n%2==0 or n%3==0):
    return False
  
  i = 5
  while(i*i<=n):
    if(n%i==0 or n%(i+2)==0):
      return False
    i = i+6
  return True  
    
def twin_prime(p, q):
    return isPrime(p) and isPrime(q) and abs(p-q)==2

print(twin_prime(5, 7)) # True