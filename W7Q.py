#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 17:19:14 2025

@author: aakash-tiwari
"""

"""
Tuples are ordered, immutable, and allow duplicates.
Syntax: () (round brackets)

Sets are unordered, mutable, and store unique items.
Syntax: {} (curly braces)
"""

"""
backpack = ("map", "compass", "torch")
print(backpack[0]) # map
# backpack[0] = "magic map" # TypeError: 'tuple' object does not support item assignment

print(backpack[1]) # compass

pouch = {"coin", "potion", "coin"}
print(pouch) # {'coin', 'potion'}

pouch = {"potion"}
pouch.add("gem")
pouch.remove("potion")
print(pouch) # {'gem'}

x = ("compass")
print(type(x)) # <class 'str'>

print(type("hello")) # <class 'str'>

x = ("compass",)
print(type(x)) # <class 'tuple'>

backpack = ("map", "map", "torch")
pouch = {"map", "map", "torch"}
print(len(backpack), len(pouch)) # 3 2

items = ["map", "torch", "torch", "map"]
unique_items = set(items)

fixed_items = tuple(unique_items)
print(len(items), len(unique_items), fixed_items) # 4 2 ('torch', 'map')

backpack = ("map", "torch")
pouch = {"torch", "map"}
supply_list = ["map", "torch"]
               
print(backpack, pouch, supply_list) # ('map', 'torch') {'map', 'torch'} ['map', 'torch']
print(backpack[1], supply_list[1]) # torch torch
"""

"""
def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n - 1)

factorial(4) # 1 normal call and 4 recursive calls
"""

"""
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
print(reverse_string("a"))
"""

def reverse_string(s):
    if s:
        return reverse_string(s[1:]) + s[0]
    else:
        return ""

print(reverse_string("race"))