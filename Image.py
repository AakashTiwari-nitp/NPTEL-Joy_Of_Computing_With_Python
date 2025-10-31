#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 09:18:31 2025

@author: aakash-tiwari
"""

"""
An image constits of matrix of pixels. A pixel is basically a color. A color is defined by 3 attributes

Attributes are: 1. Amount of Red, 2. Amount of Blue, 3. Amount of Green
"""

import numpy as np
from PIL import Image

width = 5
height = 4

array = np.zeros([height, width,  3], dtype = np.uint8)

img = Image.fromarray(array)

img.save('test.png')

array1 = np.zeros([100, 200, 3], dtype = np.uint8)

array1[:,:100] = [255, 128, 0] # orange color
array1[:,100:] = [0, 0, 255] # blue color 

img2 = Image.fromarray(array1)

img2.save("test2.png")
 