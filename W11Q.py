#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 00:46:11 2025

@author: aakash-tiwari
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # To launch a Chrome browser instance

driver.get("https://www.sales-dashboard.com") # opens a given URL in the browser

# Suppose the login form has two input fields:
# Username with id="username"
# Password with id="password"

# Enter the credentials:
driver.find_element(By.ID, "username").send_keys("user123")
driver.find_element(By.ID, "password").send_keys("mypassword")
driver.find_element(By.ID, "password").send_keys(Keys.ENTER) # Submit the form by simulating the Enter key
time.sleep(5) # Since the page may take time to load, pause execution briefly
driver.quit() # close the browser entire window

"""

"""
1. The datetime Module

The datetime module contains several classes, such as:
date – Represents a calendar date (year, month, day).
time – Represents a time of day (hours, minutes, seconds, microseconds).
datetime – Combines both date and time into one object.
timedelta – Represents the difference between two dates or times.
"""

import datetime
now = datetime.datetime.now() # To get the current date and time

"""
d = datetime.date(2025,8,10) # To create a specific date:
print(now.day ,now.month, now.year) # 1 11 2025
"""

"""
You can also format dates using strftime:
Here:
%A → Full weekday name
%d → Day of month (zero-padded)
%B → Full month name
%Y → Year with century
"""

import calendar
print(calendar.month(2025, 8))
#     August 2025
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

print(calendar.isleap(2024)) # True

print(calendar.weekday(2025, 11, 1)) # 5 -Saturday

print(datetime.date.today()) # 2025-11-01

print(datetime.date.today().strftime("%B")) # November

# from datetime import date, time, datetime # allows direct use of date, time, and datetime without module prefix

# datetime.timedelta(days=10) # A time duration of 10 days

print(datetime.datetime.now().strftime("%H")) # 01 # 1 AM # 24-hour format

print(datetime.date.today().weekday()) # 5 - Saturday