#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 00:49:45 2025

@author: aakash-tiwari
"""

import numpy as np
board = np.array([['-']*3]*3)
# print(board)
p1s = 'X'
p2s = 'O'

def place(symbol):
    print(np.matrix(board))
    while(1):
        row = int(input("Enter the row 1, 2 or 3: "))
        col = int(input("Enter the col 1, 2 or 3: "))
        row-=1
        col-=1
        if(row<0 or row>3):
            print("You enter the invalid row number.")
        elif(col<0 or col>3):
            print("You enter the invalid column number.")
        elif(board[row][col]!='-'):
            print("The place is already filled, please try again!")
        else:
             break
    
    board[row][col] = symbol
    
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count+=1
        if count==3:
            print(symbol, "Won")
            return True
    return False

def check_column(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if (board[r][c]==symbol):
                count+=1
        if count==3:
            print(symbol, "Won")
            return True
    return False

def check_diagonal(symbol):
    count = 0
    for r in range(3):
        if (board[r][r] == symbol):
            count+=1
    if(count==3):
        print(symbol, "Won")
        return True
    count = 0
    for r in range(3):
        if (board[2-r][r]==symbol):
            count+=1
    if(count==3):
        print(symbol, "Won")
        return True
    return False
    
    
def won(symbol):
    return check_rows(symbol) or check_column(symbol) or check_diagonal(symbol)
                 
     

def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1s)
            if won(p1s):
                break
        else:
            print("O turn")
            place(p2s)
            if won(p2s):
                break
            
    if ( not(won(p1s)) and not(won(p2s)) ):
        print("Draw")
            
    
    
play()