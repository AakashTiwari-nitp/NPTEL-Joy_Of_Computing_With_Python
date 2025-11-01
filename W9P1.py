#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 07:38:46 2025

@author: aakash-tiwari
"""

"""
Problem Statement: Merge Two Dictionaries
Write a function named merge that merges two dictionaries D1 and D2 into a new dictionary D following these rules:

Each key-value pair in D must come from either D1 or D2.

Every key from both D1 and D2 must be present in D.

If a key appears in both D1 and D2, the value to retain depends on the argument priority:

If priority is "first", retain the value from D1.

If priority is "second", retain the value from D2.

All keys in the resulting dictionary D must be sorted in alphabetical order.

Constraints:

Do not print anything.

Do not accept input from the user. Only define the function.
"""

def merge(D1, D2, priority):
    if priority == 'second':
        return merge(D2, D1, 'first')
    
    D = dict()
    
    # Copy all key-value pairs from D1
    for key in D1:
        D[key] = D1[key]
    
    # Copy key-value pairs from D2 where key is not already in D
    for key in D2:
        if key not in D:
            D[key] = D2[key]
    
    # Return dictionary sorted by key
    return dict(sorted(D.items()))