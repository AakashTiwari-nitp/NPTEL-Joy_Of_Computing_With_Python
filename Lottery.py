#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 18:41:20 2025

@author: aakash-tiwari
"""

import random

bet = int(input("Enter your bet from 1 to 10: "))
lucky_draw = random.randint(1, 10)
print(lucky_draw)

account = 0

if bet == lucky_draw:
    account+= 900 - 100
else:
    account-=100
    
print(account)

