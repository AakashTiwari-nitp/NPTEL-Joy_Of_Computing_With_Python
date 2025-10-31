#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 22:26:01 2025

@author: aakash-tiwari
"""

"""

Pandas provides easy to use data structure for data analysis

nltk library is used to process Human language
It provides sentimental analysis of human data
Sentimental analysis involves working out whether a piece of text is positive,negative or neutral

VADER is the Valance Aware Dictionary and Sentiment Reasoner.
It takes into account the intensity of the sentiment

A data frame is two dimensional structure in the form of the Table

ord function converts character into its ASCII Notation

"""

import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')
file = 'data_file.xlsx'
xl = pd.ExcelFile(file) # Read from the Excel
dfs = xl.parse(xl.sheet_names[0]) # Parsing the excel sheet to data frame

dfs = list(dfs['Timeline']) # Removes the blank rows from the dataframe
print(dfs)
sid = SentimentIntensityAnalyzer()

str1 = "UTC+05:30"

for data in dfs:
    a = data.find(str1) # -1 if not found
    if(a==-1):
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])


 
