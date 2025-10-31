#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 17:55:38 2025

@author: aakash-tiwari
"""

"""
Problem 1: Image Noise Isolation in Data Analysis
At a medical research lab, image preprocessing involves working with square matrices that represent pixel intensity grids extracted from medical images.

Sometimes, due to faulty sensor data, certain rows and columns must be eliminated to isolate sub-regions of the matrix.

Your task is to implement a function that removes a specified row and column from a square matrix to produce a minor matrix.

Requirements
Function Name: minor_matrix

Parameters:

M: A square matrix (list of lists).

i: Index of the row to remove (0-based).

j: Index of the column to remove (0-based).

Return Value:

A new matrix with the i-th row and j-th column removed.

Constraints:

The matrix M is always square (n × n).

M has at least 3 rows and columns.

Indexing is zero-based.

No input/output required — just define the function.
"""

"""
def minor_matrix(M, i, j):
    newM = M[:i] + M[i+1:]
    minor = [row[:j] + row[j+1:] for row in newM]
    return minor
"""

def minor_matrix(M, i, j):
    newM = []
    for row in range(len(M)):
        l = []
        if (row == i):
            continue
        for col in range(len(M)):
            if (col == j):
                continue
            else:
                l.append(M[i][j])
        newM.append(l)
    return newM


        
    