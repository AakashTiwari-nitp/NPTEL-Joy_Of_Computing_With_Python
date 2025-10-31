#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 11:57:27 2025

@author: aakash-tiwari
"""

import numpy as np

from PIL import Image

im = Image.open('enhanced.jpg')

pixelMap = im.load()

im.show()

I = np.asanyarray(Image.open('enhanced.jpg'))
print(I)

img = Image.new(im.mode, im.size)
pixelNew = img.load()

"""
2^8 = 256 -> 2^3 = 8

divide it by 2^5 = 32 

0-31 = 0
32-63 = 1
64-95 = 2
95-127 = 3
128-159 = 4
160-191 = 5
192-223 = 6
224-256 = 7
"""


for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelNew[i, j] = pixelMap[i, j]//32
        
img.save("compressed1.jpg")

J = np.asanyarray(Image.open("compressed1.jpg"))
print(J)