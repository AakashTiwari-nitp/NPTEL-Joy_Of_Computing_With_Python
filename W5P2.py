#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 02:39:49 2025

@author: aakash-tiwari
"""

"""
Managing Train Arrivals at Hogsmeade Station
The station master at Hogsmeade Station is responsible for recording details of the various magical and non-magical trains that stop there — including the number of compartments and the number of passengers in each compartment.

You have been hired as a student intern from Hogwarts School of Witchcraft and Wizardry to assist in organizing this data using Python.

(a) You have to take the following inputs:
An integer n, the number of trains that stop at the station.

For each train:

The train name (a string).

An integer m, the number of compartments in the train.

m lines of input, each containing:

The name of a compartment, and

The number of passengers in it (comma-separated).

(b) Your task is to:
Create a nested dictionary called station_dict.

The outer dictionary should use the train name as the key.

The value for each train should be another dictionary, where:

Keys are compartment names.

Values are the number of passengers in that compartment (as integers, not strings).
"""

n = int(input("Enter the number of trains: "))

station_dict = {}

for i in range(n):
    train_name = input("Enter the train name: ")
    m = int(input("Enter the number of compartments: "))
    train = {}
    for j in range(m):
        str = input("Enter the name and number of passenger seperated by comma: ")
        [compartment, passenger] = str.split(",")
        passenger = int(passenger)
        train[compartment] = passenger
    station_dict[train_name] = train
    
print(dict(sorted(station_dict.items())))
    