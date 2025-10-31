#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 18:56:04 2025

@author: aakash-tiwari
"""

"""
# Flipping the image

from PIL import Image

# opening the image
img = Image.open("flipped.jpg") 

# transposing
transposed_image = img.transpose(Image.FLIP_LEFT_RIGHT)
 
# save it in a file in human understandable format

transposed_image.save("corrected.jpg")
print("Done Flipping")
"""

# Image Enhancement CLAHE

import cv2

# read the image
img = cv2.imread("image.jpg")

# preparation for CLAHE

clahe = cv2.createCLAHE()

# convert to gray scale image
 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply enhancement
enh_img = clahe.apply(gray_image)

# save it to a file

cv2.imwrite('enhanced.jpg', enh_img)

print("Done enhancement")