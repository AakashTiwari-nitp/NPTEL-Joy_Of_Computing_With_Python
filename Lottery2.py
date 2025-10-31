#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 18:45:10 2025

@author: aakash-tiwari
"""

import random

account = 0

for i in range(30):
    bet = random.randint(1, 10)
    lucky_draw = random.randint(1, 10)
    # print(f"Bet: {bet}")
    # print(f"Lucky Draw: {lucky_draw}")


    if bet == lucky_draw:
        account+= 900 - 100
    else:
        account-=100
    
print(f"Amount in your game account: {account}")