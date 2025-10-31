#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 17:14:48 2025

@author: aakash-tiwari
"""

import calendar

# print(calendar.weekday(1947, 8, 15)) # 4 # Thursday


def check_leap(year):
    if year%400==0 or (year%100 and year%4==0):
        return True
    return False 

def check_valid_date(date, month, year, leap):
    if month == 2:
        if leap:
            return date<=29
        else:
            return date<=28
    else:
        if month<8:
            if month%2:
                return date<=31
            else:
                return date<=30
        else:
            if month%2:
                return date<=30
            else:
                return date<=31 
    
def get_day(index):
     list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
     return list_of_days[index] 

while 1:
    year = int(input("Enter the year (1970-2025): "))
    if year<1970 and year>2025:
        print("Enter the year between 1970-2025")
    else:
        break
    
    
while 1:
    month = int(input("Enter the month (1-12): "))
    if month<0 or month>12:
        print("Enter the month between 1-1 2")
    else:
        break 
    
    
leap = check_leap(year)

while 1:
    date = int(input("Enter date: "))
    if date>0 and check_valid_date(date, month, year, leap):
        break
    else:
        print("Enter a valid date")
        
day_index = calendar.weekday(year, month, date)
day = get_day(day_index)

print(date, "/" , month, "/", year, "falls on", day)