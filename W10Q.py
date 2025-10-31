#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 00:10:33 2025

@author: aakash-tiwari
"""


"""
from PIL import Image
import numpy

# Step 1: Load the image in grayscale mode
im = Image.open('image.jpg').convert('L') # The image is loaded and converted to grayscale using .convert('L').
pixelMap = im.load() # It gives access to individual pixels of the image
print(pixelMap) # <PixelAccess object at 0x737a81b83b90>

# Step2: Creates a new grayscale image
img = Image.new('L', im.size) #  ensures that the output image remains in grayscale mode
pixelNew = img.load()

print(img.size) # (360, 360)
print(type(pixelMap[0,0])) # <class 'int'>

# Step 3: Quantize
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 0 <= pixelMap[i, j] <= 31:
            pixelNew[i, j] = 0
        elif 32 <= pixelMap[i, j] <= 63:
            pixelNew[i, j] = 1
        elif 64 <= pixelMap[i, j] <= 95:
            pixelNew[i, j] = 2
        elif 96 <= pixelMap[i, j] <= 127:
            pixelNew[i, j] = 3
        elif 128 <= pixelMap[i, j] <= 159:
            pixelNew[i, j] = 4
        elif 160 <= pixelMap[i, j] <= 191:
            pixelNew[i, j] = 5
        elif 191 <= pixelMap[i, j] <= 223:
            pixelNew[i, j] = 6
        elif 224 <= pixelMap[i, j] <= 255:
            pixelNew[i, j] = 7
img.save('lena_2.jpg')
J = numpy.asarray(Image.open('lena_2.jpg')) # It writes the quantized image to a file

# Uniform Quantization with 8 Quantization level


# if the input image was not converted to grayscale before quantization then The pixelMap[i, j] would return a tuple instead of a single value
"""

# Step 1: Open the file in the read mode

file = open("students.txt", "r") #  Read the file

# Step 2: Read all the lines from the files
lines = file.readlines() #  A list of lines from the file

# Step 3: Close the file after reading
file.close() # Saves memory and finishes file operations

# Step 4: Count how many student registered
count = len(lines) #  The number of lines (students) in the file
print("Total students registered:", count)

# Step 5: Open a new file to write numbered list
new_file = open("registered.txt", "w") #  It overwrites the file if it already exists # ensures that the new file is actually created

# Step 6: Write each name with a serial number
for i in range(count):
    name = lines[i].strip() # Removes newline and extra spaces from both ends
    new_file.write(f"{i+1}. {name}\n") # \n moves to a new line after each entry

# Step 7: Close the output file
new_file.close()

