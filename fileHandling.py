#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 17:02:12 2025

@author: aakash-tiwari
"""

with open("file1.txt", "r+") as myFile:
    print(myFile.read())
    myFile.write("I am fine.")
myFile.close()