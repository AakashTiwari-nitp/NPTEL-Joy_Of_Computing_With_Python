#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 07:41:36 2025

@author: aakash-tiwari
"""

"""
import random

def jumbled_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def guess_characters():
    characters = ["Ironman", "Elsa", "Yoda", "Moana", "Harry", "Simba"]
    #characters=[] # IndexError
    original = random.choice(characters)
    jumbled = jumbled_word(original)
    
    print(f"Guess the character from this jumbled: {jumbled}")
    
    guess = input("Your Guess: ")
    
    if guess.lower() == original.lower():
        print("Correct!")
    else:
        print(f"Oops! The correct answer was: {original}")
        
guess_characters()
"""

"""
matrix = []

for row in range(3):
    new_row = []
    for col in range(3):
        new_row.append(0)
    matrix.append(new_row)
    
for row in matrix:
    print(row)
"""

matrix = []
row = [0]*3
for i in range(3):
    matrix.append(row)

matrix[0][0] = 99
print(matrix)