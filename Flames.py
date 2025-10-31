#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:58:25 2025

@author: aakash-tiwari
"""

import string

def remove_matching_letters(l1, l2):
    for word in l1:
        if word in l2:
             l1.remove(word)
             l2.remove(word)


name1 = input("Enter the first name: ")
name1 = name1.lower()
name1.replace(" ", "")

name2 = input("Enter the second name: ")
name2 = name2.lower()
name2.replace(" ", "")

l1 = list(name1)
l2 = list(name2)

remove_matching_letters(l1, l2)

print(l1)
print(l2)

count = len(l1) + len(l2)

result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]


while(len(result)>1):
    split_index = (count%(len(result))) - 1

    if split_index>=0:
        right = result[split_index+1:]
        left = result[:split_index]
        result = right + left
    else:
        result = result[:len(result) - 1]
        
print(result[0])

