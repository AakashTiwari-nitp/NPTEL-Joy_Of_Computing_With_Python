#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:34:30 2025

@author: aakash-tiwari
"""

import turtle
import random

turtle.bgcolor("black")
seurat = turtle.Turtle()
 
dot_distance = 25
width = 5
height = 7
 
seurat.penup()

list_color = ["white", "yellow", "brown", "red", "blue", "green", "orange", "pink", "violet", "grey"]

 
seurat.setpos(-250, 250)


def spiral(m, n):
    k = 0
    l = 0
    f = 0
    
    col = random.randint(0, 10)
    seurat.color(list_color[col])
    
    
    """
     k = index of the starting row
     l = index of the starting column
    """
    while(k<m and l<n):
        if f==1:
            seurat.right(90)
        
        # printing the first row of the starting row
        for i in range(l, n):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[k][i], end = " ")
            
        k+=1
        f=1
        
        col = random.randint(0, 10)
        seurat.color(list_color[col])
        
        seurat.right(90)
        
        # printing the last column of the remaining
        for i in range(k, m):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(a[i][n-1], end = " ")
            
        n-=1
        
        col = random.randint(0, 10)
        seurat.color(list_color[col])
        seurat.right(90)
        
        
        if(k<m):
            # printing the last row from the remaining row
            for i in range(n-1, l-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[m-1][i], end =" ")
                
            m-=1
            
        col = random.randint(0, 10)
        seurat.color(list_color[col])
        seurat.right(90)
            
        if(l<n):
            # printing the first col for the remaining col
            for i in range(m-1, k-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                # print(a[i][l], end=" ")
            l+=1
            
        
spiral(20,20)
turtle.done()