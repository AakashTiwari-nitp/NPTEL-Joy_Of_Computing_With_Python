#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 09:47:57 2025

@author: aakash-tiwari
"""

import scipy.misc
from PIL import Image
import numpy as np
import random
import imageio.v2 as imageio
 
img = imageio.imread("map-01.png")
count_pun = 0
count_in = 0
count = 0
while(count<=100000):
    x = random.randint(0, 1055)
    y = random.randint(0, 991)
    z = 0
    if(img[x][y][z] == 60):
        count_in+=1
        count+=1
    elif(img[x][y][z] == 80):
        count_pun+=1
        count+=1
        
area_pun = (count_pun/count_in)*3287263
print(area_pun) # 205995.38713550963
    
      