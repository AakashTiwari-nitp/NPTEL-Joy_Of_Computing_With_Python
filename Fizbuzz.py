#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 12:32:55 2025

@author: aakash-tiwari
"""

def fizzBuzz(n):
    for i in range(1,n):
        if (i%15==0):
            print(str(i) + " = FizzBuzz")
        elif (i%5==0):
            print(str(i) + " = Buzz")
        elif (i%3==0):
            print(str(i) + " = Fizz")
        else:
            print(str(i))
            
fizzBuzz(51)