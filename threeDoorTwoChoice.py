#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 20:10:43 2025

@author: aakash-tiwari
"""

import random

doors = [0]*3
goatDoor = [0]*2
swap = 0 # Number of swap wins
dont_swap = 0 # Number of no swap wins
j = 0
while(j<10):
    
    x = random.randint(0, 2) # xth door will compromise of BMW
    
    doors[x] = "BMW"
    for i in range(0,3):
        if (i==x):
            continue
        else:
            doors[i] = "Goat"
            goatDoor.append(i)
    
    choice = int(input("Enter your choice: "))
    door_open = random.choice(goatDoor)  # open a door that comprises of goat
    
    while(door_open==choice):
        door_open = random.choice(goatDoor)
        
    ch = input("Do you want to swap? y/n: ")
    if(ch == "y"):
        if(doors[choice]=="Goat"):
            print("Player wins")
            swap+= 1
        else:
            print("Player lost")
    else:
        if(doors[choice]=="Goat"):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap+= 1
            
    j+=1;

print(swap)
 print(dont_swap)

