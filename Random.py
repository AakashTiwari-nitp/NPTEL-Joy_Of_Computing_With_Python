#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 17:10:00 2025

@author: aakash-tiwari
"""

import random

print(random.randint(1,5))
# Both 1 and 5 are inclusive here

print(random.randrange(1,5))
# Here 5 is not inclusive 

print(random.random())
# generates a number from 0 to 1

print(random.randrange(1, 10, 2))
# this will only generate odd numbers (step of 2)

print(random.randrange(2, 11, 2))
# this will generate even number from 2 to 10


print(random.choice([2, 6, 8, 45, 67, 75]))
# gives a random item from the list

myList = [11, 28, 45, 96]
print(random.choice(myList))