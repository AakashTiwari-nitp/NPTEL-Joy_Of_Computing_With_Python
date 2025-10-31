#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 21:09:01 2025

@author: aakash-tiwari
"""

import string
import random
#print(string.ascii_letters)

symbols = list(string.ascii_letters)
#print(symobols)


card1 = [0]*5
card2 = [0]*5

print(f"Card1: {card1}")
print(f"Card2: {card2}")


pos1 = random.randrange(0, 5)
pos2 = random.randrange(0, 5)

sameSymbol = random.choice(symbols)

if(pos1 == pos2):
    card1[pos1] = sameSymbol
    card2[pos1] = sameSymbol
    symbols.remove(sameSymbol)
    
else:
    card1[pos1] = sameSymbol
    card2[pos2] = sameSymbol
    symbols.remove(sameSymbol)
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
    
i = 0
while(i<5):
    if(i!=pos1 and i!=pos2):
        card1[i] = random.choice(symbols)
        symbols.remove(card1[i])
        card2[i] = random.choice(symbols)
        symbols.remove(card2[i])
        
    i+=1
    
print(f"Card1: {card1}")
print(f"Card2: {card2}")

ch = input("Enter the character in the both cards: ")

if(ch == sameSymbol):
    print("You Entered Right Character")
else:
    print("You Entered Wrong Character")