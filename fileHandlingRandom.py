#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 17:18:39 2025

@author: aakash-tiwari
"""

import random

def evolve(x):
    ind = random.randrange(0, 100)
    p = random.randint(0, 100)
    
    if(p==1):
        if(x[ind]=='0'):
            x[ind] = '1'
        else:
            x[ind] = '0'
    

with open("RandomText.txt", "r+") as myFile:
    #print(myFile.read())
    x = myFile.read()
    x = list(x)
    print(x)
    
for i in range(1, 100):
    evolve(x)
    
print(x)