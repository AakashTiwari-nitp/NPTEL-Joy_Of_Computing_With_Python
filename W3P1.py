#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 19:25:13 2025

@author: aakash-tiwari
"""

"""
In the land of Codeville, young programmers discover an ancient scroll containing a list of mysterious words — each one part of a secret prefix code used by the town’s old network of messengers. Legend says that hidden among these words is one with special power: the longest word in the list. But there’s a twist — if more than one word shares the longest length, the scroll reveals only the one that appears last in the list.The town’s Code Scribe, Pixel, needs your help. She wants you to write a program that will search through this list and identify the special word according to the rules.
Write a program that:

Accepts a single line of input containing a comma-separated list of words from the ancient prefix code.

Finds and prints:   (a) The longest word in the list.   (b) If multiple words share the maximum length, print the one that appears right-most in the list.
"""

"""
str = input("Enter the words seperated by comma: ")
words = str.split(',')
#print(words)
maxLength = 0
longest_word = ""
for word in words:
    if (len(word) >= maxLength):
        maxLength = len(word)
        longest_word = word
        
print(longest_word)
"""
    
def getLongestWord(str):
    words = [word.strip() for word in str.split(',')] # form a list of word after removing the empty spaces from the word
    # print(words)
    max_length = 0
    longest_word = ""
    for word in words:
        if(len(word) >= max_length):
            longest_word = word
            max_length = len(word)
    return longest_word
    
if __name__ == "__main__":
    user_input = input()
    result_word = getLongestWord(user_input)
    print(f"{result_word}", end='')