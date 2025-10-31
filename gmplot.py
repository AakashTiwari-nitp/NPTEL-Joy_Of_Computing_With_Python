#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:00:42 2025

@author: aakash-tiwari
"""

from gmplot import gmplot
import csv

gmap = gmplot.GoogleMapPlotter(28.691658, 77.582363, 17)

gmap.coloricon = "http://www.googlemapsmakers.com/v1/%s"

with open("gps.csv", "r") as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        
        if(k==0):
            gmap.marker(lat, long, "yellow")
            k = 1
        else:
            gmap.marker(lat, long, "blue")
gmap.marker(lat, long, "red")

gmap.draw("mymap.html")