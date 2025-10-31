#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 11:48:15 2025

@author: aakash-tiwari
"""

import random
from PIL import Image

end = 100

def show_board():
    img = Image.open("image.jpg")
    img.show()
    
def check_ladder(points):
    if points == 4:
        print("Ladder")
        return 23
    elif points == 13:
        print("Ladder")
        return 46
    elif points == 33:
        print("Ladder")
        return 52
    elif points == 42:
        print("Ladder")
        return 63
    elif points == 50:
        print("Ladder")
        return 69
    elif points == 62:
        print("Ladder")
        return 81
    elif points == 74:
        print("Ladder")
        return 93
    else:
        return points
    
def check_snake(points):
    if points == 27:
        print("Snake")
        return 5
    elif points == 40:
        print("Snake")
        return 2
    elif points == 43:
        print("Snake")
        return 17
    elif points == 54:
        print("Snake")
        return 31
    elif points == 66:
        print("Snake")
        return 45
    elif points == 89:
        print("Snake")
        return 53
    elif points == 99:
        print("Snake")
        return 41
    else:
        return points
    
def reached_end(points):
    return points == end
        
    
def play():
    # taking name  
    p1_name = input("Enter the name of the first player: ")
    p2_name = input("Enter the name of the second player: ")
    
    # intial points
    pp1 = 0
    pp2 = 0
    
    turn = 0
    while(1):
        if turn%2==0:
            print(f"{p1_name} turn")
            c = int(input("Press 1 to continue, 0 to quit: "))
            if(c==0):
                print(f"{p1_name} scored {pp1}")
                print(f"{p2_name} scored {pp2}")
                print("Quitting the game")
                break
            
            dice = random.randint(1, 6)
            print(f"Dice showed {dice}")
            
            pp1 = pp1 + dice
            
            pp1 = check_ladder(pp1)
            
            pp1 = check_snake(pp1)
            
            if(pp1 > end):
                pp1 = end
                
            print(f"{p1_name} score is: {pp1}")
            
            if reached_end(pp1):
                print(f"{p1_name} won")
                break
        else:
            print(f"{p2_name} turn")
            c = int(input("Press 1 to continue, 0 to quit: "))
            if(c==0):
                print(f"{p1_name} scored {pp1}")
                print(f"{p2_name} scored {pp2}")
                print("Quitting the game")
                break
            
            dice = random.randint(1, 6)
            print(f"Dice showed {dice}")
            
            pp2 = pp2 + dice
            
            pp2 = check_ladder(pp2)
            
            pp2 = check_snake(pp2)
            
            if(pp2 > end):
                pp2 = end
                
            print(f"{p2_name} score is: {pp2}")
            
            if reached_end(pp2):
                print(f"{p2_name} won")
                break 
            
        turn+=1
         
 
show_board()

play()