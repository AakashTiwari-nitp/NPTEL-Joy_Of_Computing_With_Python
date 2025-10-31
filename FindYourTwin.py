#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 21:42:42 2025

@author: aakash-tiwari
"""

import random 
import datetime

birthdays = []

i = 1
while(i<=50):
    year = random.randint(1895, 2025)
    
    if(year%400==0 or year%100!=0 and year%4==0):
        leap = 1
    else:
        leap = 0
        
    month = random.randint(1, 12)
    
    if(leap and month == 2):
        day = random.randint(1, 29)
    elif(month == 2):
        day = random.randint(1, 28)
    elif(month%2 and month<=8 or month == 8):
        day = random.randint(1, 31)
    elif(month%2==0 and month>8):
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
        
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday
    birthdays.append(day_of_year)
    i+=1
    
birthdays.sort()

for i in range(len(birthdays) - 1):
    if(birthdays[i] == birthdays[i+1]):
        print(birthdays[i], birthdays[i+1])
        
    
    
    