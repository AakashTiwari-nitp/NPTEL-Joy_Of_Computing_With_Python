#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 07:43:01 2025

@author: aakash-tiwari
"""

"""
Problem Statement
You are working on a text analysis tool that groups words based on their frequency in a given list. For example, you might want to find all words that appear exactly once, all words that appear twice, and so on.

Write a function freq_to_words that accepts a list of lowercase words as input and returns a dictionary with the following structure:

Key: Frequency (positive integer) of the words

Value: List of all words that occur exactly that many times in the input

You do not need to accept any input from the user or print anything to the console. Just write the function definition.
"""

"""
def freq_to_words(words):
    # Step 1: Count frequency of each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Step 2: Group words by their frequency
    freq_to_words_dict = {}
    for word, count in word_count.items():
        if count not in freq_to_words_dict:
            freq_to_words_dict[count] = []
        freq_to_words_dict[count].append(word)
    
    return freq_to_words_dict
"""

def words_to_frequency(words):
    freq_dict = dict()
    for word in words:
        if word not in freq_dict:
            freq_dict[word] = 0
        freq_dict[word] += 1
    return freq_dict

def freq_to_words(words):
    freq_dict = words_to_frequency(words)
    result = dict()
    for word in freq_dict:
        freq = freq_dict[word]
        if freq not in result:
            result[freq] = []
        result[freq].append(word)
    return result