#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 22:14:02 2025

@author: aakash-tiwari
"""

import datetime

print(datetime.date.today())

print(datetime.date.today().strftime("%Y")) # for year only

print(datetime.date.today().strftime("%B")) # for month only

print(datetime.date.today().strftime("%d")) # for date only

print("Week Number of the month:", datetime.date.today().strftime("%W")) # for week number

print("Week day of the week: ",datetime.date.today().strftime("%w")) # for geeting week day of the week

print("Day of year:", datetime.date.today().strftime("%j")) # for day of the year

print("Day of the week:", datetime.date.today().strftime("%A")) # for getting day of the week

print(datetime.datetime.now()) # for year only