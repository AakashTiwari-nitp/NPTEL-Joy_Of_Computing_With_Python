#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 20:28:05 2025

@author: aakash-tiwari
"""

conv_factor = {}
conv_factor["dollar"] = 60

print(conv_factor)

conv_factor["euro"] = 80

print(conv_factor)

print(conv_factor["euro"])

print(conv_factor.keys()) 

print(list(conv_factor.keys()))

print(list(conv_factor.values()))

print(conv_factor.items())

conv_factor["dollar"] = 65

print(list(conv_factor.items()))

conv_factor["yen"] = 50

print(conv_factor) 

del conv_factor["yen"]

print(conv_factor)

e = 30

r = e*conv_factor["euro"]
print(r)