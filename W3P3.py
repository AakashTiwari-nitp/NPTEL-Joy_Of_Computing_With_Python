#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 07:13:06 2025

@author: aakash-tiwari
"""

"""
At Orbital Station Vega, mission control systems rely heavily on matrix-based data to process flight paths, control modules, and compute system interactions. Two key matrices, A and B, represent critical control parameters: one for navigation weights and another for response modifiers. Before any launch, the control AI must compute the product matrix AB, which defines the final control grid used during takeoff. The engineers receive the data from satellite input systems in the following format:

The first line contains the integer n, representing the size of the square matrices.

The next n lines each contain a row of matrix A, represented as comma-separated
integers.
The following n lines each contain a row of matrix B, again as comma-separated
integers.

Your task is to help the AI compute the matrix product AB, and output it in the
correct format:
n lines, each containing a row of the resulting matrix, as comma-separated integers.

Write a program that:
(a) Accepts an integer n followed by 2n lines as input.
(b) Each of the first n lines contains a row of matrix A (comma-separated integers).
(c) Each of the next n lines contains a row of matrix B (comma-separated integers).
(d) Computes the matrix product AB.
(e) Outputs the resulting matrix as n lines, with each line showing a row of the
product as comma-separated integers.
"""

n = int(input("Enter the size of the matrix: "))

A = []

for i in range(n):
    row = []
    for x in input().split(","):
        row.append(int(x))
    A.append(row)
print(A)

B = []

for i in range(n):
    row = []
    for x in input().split(","):
        row.append(int(x))
    B.append(row)
print(B)
        
C = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    C.append(row)
    
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
            
for i in range(n):
    for j in range(n):
        if(j!=n-1):
            print(C[i][j], end = ",") 
        else:
            print(C[i][j], end = "")
    print()

            
    