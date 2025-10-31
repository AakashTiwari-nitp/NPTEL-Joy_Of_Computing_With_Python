#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 22:33:10 2025

@author: aakash-tiwari
"""

"""
def are_anagrams(w1, w2):
    return sorted(w1) == sorted(w2)

print(are_anagrams("Listen", "Silent")) # False
"""

"""
def are_anagrams(w1, w2):
    w1 = w1.replace(" ", "").lower()
    w2 = w2.replace(" ", "").lower()
    return sorted(w1) == sorted(w2)

print(are_anagrams( "Dormitory", "Dirty room")) # True
"""

"""
words = ["listen", "silent", "enlist", "google", "gogole"]
anagrams = []
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if sorted(words[i]) == sorted(words[j]):
            anagrams.append((words[i], words[j]))
print (anagrams) # [('listen', 'silent'), ('listen', 'enlist'), ('silent', 'enlist'), ('google', 'gogole')]
"""

"""
def ascii_sum(word):
    total=0
    for char in word:
        total += ord(char)
        return total
print(ascii_sum("abc") == ascii_sum("acb")) # True
"""

"""
import random
print(random.randrange(0, 10)) # exclusive # not inclusive of upper bound
print(random.randint(0, 10)) # inclusive
print(random.random()) # always between 0 and 1 # [0. 1) # not inclusive of upper bound
"""

"""
import random
import matplotlib.pyplot as plt
counts = []
count = 0
for i in range(10):
    guess = random.randint(1, 10)
    pick = random.randint(1, 10)
    if guess != pick:
        count += 1
    else:
        count-=1
    counts.append(count)
plt.plot(counts)
plt.show()
"""

"""
import random
print(random.randint(10, 1)) # ValueError: empty range in randrange(10, 2)
"""

"""
# PIL— Python Imaging Library
from PIL import Image # Manipulate and view images

img = Image.open("filepath") # opens the image # To load the image into Python
img_resized = img.resize((300,300)) # Resizes the image to 300x300 pixels
print(img.format) # prints the format of the image # Ex- JPEG, PNG
print(img.mode) # prints the mode of the image # Ex - RGB or L
img_resized.show() #  to view the image on the screen
"""

"""
from PIL import Image
img = Image.open("image.jpg")
print(type(img)) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
"""


from PIL import Image
import numpy as np
img = Image.open("image.jpg")
img = img.resize((3, 3))
arr = np.array(img)
print(arr.shape) #  (3, 3, 3) for color or RGB # (3, 3) for grayscale or L

# arr[x][y] contain a list of RGB values in a colored image loaded with NumPy 
