#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:33:19 2025

@author: aakash-tiwari
"""

#from statistics import mean
#from scipy import stats

#Estimates = [1000, 1020, 587, 962, 145, 356, 451, 576, 768, 1230, 654,257, 150, 100,564, 869, 235, 246, 142,754]
#print("The size of the sample data is:", len(Estimates))

#Estimates.sort()

#print(Estimates)

#tv = int(0.1*len(Estimates))

#Estimates = Estimates[tv:]

#print("The size of the sample data after removing 10% smaller values: ", len(Estimates))

#Estimates = Estimates[:len(Estimates) - tv]

#print("The size of the sample data after removing 10% larger values: ", len(Estimates)) 

#print(f"The mean of the Estimates is: {mean(Estimates)}")

#m = stats.trim_mean(Estimates,0.1)
#print(m)


import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4])
#plt.plot([1, 3, 5, 7], "ro")
#plt.plot([2, 4, 6, 8], "r--")
#plt.plot([1, 4, 8, 16], "bs")
#plt.plot([1, 5, 15, 20], "g^")
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#plt.ylabel("Some values")

#Estimates = [1000, 1020, 587, 962, 145, 356, 451, 576, 768, 1230, 654,257, 150, 100,564, 869, 235, 246, 142,754]
#plt.plot(Estimates)

#y = []
#for i in range(len(Estimates)):
#    y.append(5)
    
#plt.plot(Estimates, y, "r--")

import statistics
Estimates = [1000, 1020, 587, 962, 145, 356, 451, 576, 768, 1230, 654,257, 150, 100,564, 869, 235, 246, 142,754]
Estimates.sort()
tv = int(0.1*len(Estimates))

Estimates = Estimates[tv:]
Estimates = Estimates[:len(Estimates) - tv]
y = []
for i in range(len(Estimates)):
    y.append(5)

plt.plot(Estimates, y, "r--")
m = statistics.mean(Estimates)

plt.plot(m, 5, "g^")
median1 = statistics.median(Estimates)
plt.plot(median1, 5, "bs")