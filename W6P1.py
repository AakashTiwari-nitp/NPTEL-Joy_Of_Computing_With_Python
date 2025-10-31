#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:45:54 2025

@author: aakash-tiwari
"""

"""
Problem: Robot Arithmetic Module – Engineering Constraint
At RoboCore Labs, engineers are developing an embedded system for a low-power educational robot.
Due to hardware limitations, the robot’s control unit cannot use the built-in multiplication operation.

As a member of the firmware team, your task is to implement a function that computes the product of two positive integers without using the * operator.

Requirements:
Function Name: multiply

Parameters:

a (positive integer)

b (positive integer)

Constraints:

You may only use the + (addition) and - (subtraction) operators.

The * (multiplication) operator is strictly forbidden.

Return Value:

The function should return the product of a and b.

Implementation:

The solution must be implemented using recursion.

Note:

Do not read input from the user.

Do not print output to the console.
"""

def multiply(a, b):
    if(b==1):
        return a
    return a + multiply(a, b-1)

print(multiply(5, 90))