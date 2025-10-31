#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 17:47:47 2025

@author: aakash-tiwari
"""

c = 1
n = 0
while(c==1):
    n = n+1
    print("The patient with token number", n, "may come in")
    c = int(input("Do you wish to continue: "))
    
print("This is end of the day, you have examined", n, "patient today.")