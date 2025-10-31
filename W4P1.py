#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 11:40:31 2025

@author: aakash-tiwari
"""

"""
At Insight Analytics, the DataOps team is responsible for maintaining data quality across real-time dashboards, reports, and AI pipelines.
To streamline data handling across various components, you are tasked with implementing a unified utility function that simplifies basic list operations. This function will be used across multiple internal scripts to ensure consistent list behavior and efficient processing.

Problem Statement
Write a single Python function named list_util that performs different operations on a list based on a specified command.

Function Signature

def list_util(L, command):

    ...

Parameters:
L: A list of elements.

command: A string representing the operation to perform. It can be one of:

"is_empty" – Check if the list is empty.

"first" – Get the first element of the list.

"last" – Get the last element of the list.

"init" – Get all elements except the last.

"rest" – Get all elements except the first.

Depending on the value of command, the function should perform one of the following:

If command is "is_empty", return True if the list is empty, and False otherwise.

If command is "first", return the first element of the list if it’s non-empty; otherwise return None.

If command is "last", return the last element of the list if it’s non-empty; otherwise return None.

If command is "rest", return a list of all elements except the first one, if the list is non-empty. If the list has only one element, return an empty list. If the list is empty, return None.
"""

"""
def list_util(L, command):
    if (command=="is_empty"):
        if(len(L)==0):
            return True
        else:
            return False
        
    elif (command=="first"):
        if(len(L)==0):
            return None
        else:
            return L[0]
    
    elif (command=="last"):
        if(len(L)==0):
            return None
        else:
            return L[-1]
    
    elif (command=="init"):
        return L[:-1] if L else None
    
    elif (command=="rest"):
        return L[1:] if L else None
    
print(list_util([],"last"))
print(list_util([99],"rest"))
print(list_util(['a','b','c','d'],"init"))
"""


def list_util(L, command):
    if command == "is_empty":
        return len(L) == 0

    if command == "first":
        return L[0] if L else None

    if command == "last":
        return L[-1] if L else None

    if command == "init":
        if not L:
            return None
        return L[:-1] if len(L) > 1 else []

    if command == "rest":
        if not L:
            return None
        return L[1:] if len(L) > 1 else []

print(list_util([],"last"))
print(list_util([99],"rest"))
print(list_util(['a','b','c','d'],"init"))