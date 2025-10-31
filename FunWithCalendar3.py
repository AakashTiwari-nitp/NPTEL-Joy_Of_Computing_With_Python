#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 17:47:20 2025

@author: aakash-tiwari
"""

from datetime import datetime as dt
import pytz
 
timezones = pytz.all_timezones

for i in range(len(timezones)):
    zone = timezones[i]
    tz = pytz.timezone(zone)
    print("Current time at zone: ", zone, "is:", dt.now(tz))