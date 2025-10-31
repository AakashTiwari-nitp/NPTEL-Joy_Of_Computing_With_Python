#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 09:32:44 2025

@author: aakash-tiwari
"""

import numpy as np
from PIL import Image

im = Image.open('test2.png')

rgb_im = im.convert('RGB')

r, g, b = im.getpixel((1,1))
print(r,g,b) # 255 128 0

r, g, b = im.getpixel((150,1))
print(r,g,b) # 0 0 255