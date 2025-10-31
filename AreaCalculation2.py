#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:15:36 2025

@author: aakash-tiwari
"""

from PIL import Image
import random

im = Image.open("map-01.png")
rgb_im = im.convert("RGB")

width, height = rgb_im.size  # <-- ACTUAL DIMENSIONS
print(width, height)

count_pun = 0
count_in = 0
count = 0
while(count<=10000):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    z = 0
    
    r,g,b = rgb_im.getpixel((x, y))
     
    if(r == 60):
        count_in+=1
        count+=1
    elif(r == 80):
        count_pun+=1
        count+=1
        
area_pun = (count_pun/count_in)*3287263
print(area_pun) # 205995.38713550963