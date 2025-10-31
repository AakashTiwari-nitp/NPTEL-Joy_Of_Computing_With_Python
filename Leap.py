#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 21:23:44 2025

@author: aakash-tiwari
"""

import random

year = random.randint(2000, 2015)

if(year%400==0 or year%100!=0 and year%4==0 ):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")