#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 07:53:23 2025

@author: aakash-tiwari
"""

"""
Week 11 : Programming Assignment 3
Due on 2025-10-09, 23:59 IST
Problem: Secure Communication for Disaster Response Teams
During emergency situations such as natural disasters, communication between rescue teams must remain confidential to prevent misuse of critical information.
To achieve this, messages are encrypted using a Caesar Cipher before transmission.

The Caesar Cipher works by shifting each letter in the message by a fixed number of positions in the alphabet.

Example (Shift = 3):
ATTACK → DWWDFN
Here, A → D, T → W, Z → C (letters wrap around).

Only uppercase alphabets (A–Z) are encrypted.

Spaces and punctuation remain unchanged.

Task
Write a program to encrypt a given message using Caesar Cipher.

You must define the function:

def encrypt_message(message, shift):
    # Your code here
Input Format
The first line of input contains the message (string, may include spaces).

The second line contains the shift value (integer).

Output Format
Print the encrypted message after applying the Caesar Cipher.


"""

def encrypt_message(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

print(encrypt_message("MISSION IMPOSSIBLE", 3)) # PLVVLRQ LPSRVVLEOH