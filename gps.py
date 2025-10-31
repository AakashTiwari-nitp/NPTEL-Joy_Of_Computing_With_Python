#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:50:15 2025

@author: aakash-tiwari
"""

import csv

with open("gps.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        print(lat)
        print(long)
        print(lat+long)