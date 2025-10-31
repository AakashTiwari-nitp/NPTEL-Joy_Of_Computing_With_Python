#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 09:12:03 2025

@author: aakash-tiwari
"""

"""
Text Analysis at LitVerse Publishing
At LitVerse, an online platform for writers and editors, the content moderation team is building tools to analyze and summarize large blocks of text.

One of the tools they’re developing aims to check whether any specific word appears an exact number of times in a paragraph.

You are part of the development team, and your task is to write a utility function to support this feature.

Task
(a) Write a Python function named exact_count that accepts the following:

para – a string containing a sequence of space-separated words, all in lowercase, with no special characters or punctuation.

n – a positive integer.

(b) The function should return True if there is at least one word in the paragraph that occurs exactly n times. It should return False otherwise.

(c) You do not need to accept input from the user or print output to the console. Simply define the function as described.
"""

"""
def exact_count(para, n):
    words = para.split(",")
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
    return n in words_count.values()
"""

def exact_count(para, n):
    D = dict()
    for word in para.split(' '):
        if word not in D:
            D[word] = 0
        D[word] += 1
    for word in D:
        if D[word] == n:
            return True
    return False

para = input("Enter the paragraph: ")
n = int(input("Enter the number: "))
print(exact_count(para, n))

        