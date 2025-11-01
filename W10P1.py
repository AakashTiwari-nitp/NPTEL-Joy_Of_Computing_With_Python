#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 07:46:20 2025

@author: aakash-tiwari
"""

"""
Problem Statement: Run-Length Encoding for Hostel Notice Board
The hostel manager at IIT Ropar maintains a digital notice board accessible to all students. Notices are uploaded as plain text, but as the number of notices grows, server space usage increases.

To reduce storage, the IT admin wants a basic compression algorithm that can shrink repetitive characters in each notice.

Compression Logic
The admin proposes using a simple form of Run-Length Encoding (RLE):

Consecutive repetitions of a character are replaced with the character followed by the count of its occurrences.

If a character appears only once consecutively, it remains unchanged.

Example:

"aaabbc" → "a3b2c"
Task
Write a function compress that accepts a string notice and returns its compressed form using the above RLE logic.

Function Signature:

def compress(notice):
    
    Instructions
You do not need to accept input from the user or print output to the console.

All characters in the string will be lowercase letters.

The length of the string will be between 1 and 1000.


"""


def compress(notice):
    if not notice:
        return ""
    result = []
    count = 1
    for i in range(1, len(notice)):
        if notice[i] == notice[i - 1]:
            count += 1
        else:
            result.append(notice[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    # Handle the last character group
    result.append(notice[-1])
    if count > 1:
        result.append(str(count))
    print(result) # [' ', 'e', '7', 't', '6', 'a', ' ']
    return ''.join(result) #  e7t6a 

print(compress(" eeeeeeetttttta ")) #  e7t6a 