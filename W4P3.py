#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 12:24:44 2025

@author: aakash-tiwari
"""

"""
In the year 2525, the Galactic Registry maintains records of citizens from various planets. Each citizen is registered with:

A name, and A birthdate, represented by a number from 1 to 365, indicating the day of the year they were born.

The Interstellar Census Department is looking to identify "Birthday Twins" — citizens who share the same day of birth.

Input:
The function will take the following two inputs:

A string of comma-separated names (e.g., "alice,bob,charlie"),

A string of comma-separated integers (each from 1 to 365), representing the birthdates corresponding to the names above.

Task:
Identify all unique pairs of names where both individuals share the same birthday.

For each such pair, create a list in the form: [name1, name2], where name1 comes before name2 alphabetically.

Store all such pairs in a list called common.

Notes:
Only the order within each pair matters — the overall order of pairs in common is not important.

You can assume that at least one birthday twin pair will exist in any test case.
"""

"""
names = input("Enter the names seperated by comma: ").split(",")
print(names)
birthdates = input("Enter the birthdates seperated by comma: ").split(",")
birthdates = [int(x) for x in birthdates]
print(birthdates)

zipped_list = list(zip(birthdates, names))
print(zipped_list)

zipped_list.sort()
print(zipped_list)

common = []
for i in range(0, len(zipped_list)):
    for j in range(i+1, len(zipped_list)):
        if(zipped_list[i][0] == zipped_list[j][0]):
            common.append([zipped_list[i][1], zipped_list[j][1]])
        
print(len(common))
common.sort()

for i in range(0, len(common)):
    if(i!=len(common)-1):
        print(",".join(common[i]), end="\n")
    else:
        print(",".join(common[i]), end="")
"""

names = input("Enter the name seperated by comma: ").split(",")
birthdates = list(map(int, input("Enter the birthdates seperated by comma: ").split(",")))

n = len(names)
common = []

for i in range(n):
    for j in range(i+1, n):
        if(birthdates[i]==birthdates[j]):
            pair = sorted([names[i], names[j]])
            common.append(pair)

common.sort()

for pair in common:
    print(','.join(pair))