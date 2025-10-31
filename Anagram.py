#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 19:47:12 2025

@author: aakash-tiwari
"""

"""
x = [1, 3, 2, 4]
print(sorted(x)) # [1, 2, 3, 4]
print(sorted(x, reverse=True)) # [4, 3, 2, 1]

x = ['q', 'w', 'e', 'r', 't', 'y']
print(sorted(x)) # ['e', 'q', 'r', 't', 'w', 'y']

x = "python"
print(sorted(x)) # ['h', 'n', 'o', 'p', 't', 'y']

x = {'q': 1, 'w': 2, 'e': 4, 't': 0}
print(sorted(x)) # ['e', 'q', 't', 'w']

L = ["cccc", "aa", "ddd", "b"]
print(sorted(L, key = len)) # ['b', 'aa', 'ddd', 'cccc']
print(L) # ['cccc', 'aa', 'ddd', 'b']

L.sort()
print(L) # ['aa', 'b', 'cccc', 'ddd']
"""

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print(sorted(str1))
print(sorted(str2))

if(sorted(str1) == sorted(str2)):
    print("These are anagrams")
else:
    print("These are not Anagrams")
