#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 07:42:24 2025

@author: aakash-tiwari
"""

"""
Problem Statement
You are given a 2-dimensional list mat that represents a matrix.

Write a function rotate(mat) that returns a new matrix rotated 90° clockwise.

The input mat is a list of lists, where each inner list represents a row.

You do not need to handle input/output.

Hint / Approach:

First, compute the transpose of the matrix.

Then, reverse each row of the transposed matrix.
"""


def get_column(mat, col):
    return [mat[row][col] for row in range(len(mat))]

def transpose(mat):
    return [get_column(mat, i) for i in range(len(mat[0]))]

def rotate(mat):
    mat_trans = transpose(mat)
    rotated_mat = []
    for row in mat_trans:
        rotated_mat.append(row[::-1])  # reverse each row