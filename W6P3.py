#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 17:01:42 2025

@author: aakash-tiwari
"""

"""
Problem: Signal Propagation in Network Simulation
At NeuroLink Systems, researchers are developing a simulation to analyze how signals propagate in a neural network grid.

The network is represented as a square matrix A, where each entry represents the connection strength between neurons.

To study influence over multiple steps, the team must compute the matrix raised to a power m.

Each matrix multiplication represents one time step of propagation.

Your task is to implement a recursive function to compute the power of a matrix.

Requirements
Function Name: power

Parameters:

A: A square matrix (2D list of integers or floats).

m: A positive integer (exponent).

Return Value:

The matrix A^m, computed recursively.

Constraints:

Must use recursion.

No user input or console printing — only function definition required.
"""

def power(A, m):
    if m==1:
        return A
    return multiply(A, power(A, m-1))

def multiply(A, B):
    C = []
    for i in range(len(A)):
        l = [0]*len(A)
        C.append(l)
        
        
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                C[i][j]+= A[i][k]*B[k][j]
                
    return C

n = int(input("Enter the size of the matrix: "))

A = []
for i in range(n):
    l = input(f"Enter the {i}th row of the matrix seperated by comma: ").split(",")
    for j in range(len(l)):
        l[j] = int(l[j])
    A.append(l)
        
print(A)
        
m = int(input("Enter the power to be computed: "))

C = power(A, m)

print(C)        