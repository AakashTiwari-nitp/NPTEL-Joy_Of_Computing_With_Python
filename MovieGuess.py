#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:45:34 2025

@author: aakash-tiwari
"""

import random
movies = ["drishyam", "gol mall", "shaitaan", "stree", "lunchbox", "queen", "vikram", "pushpa", "taare zameen par"]

def play():
    p1 = input("Enter the name of Player 1")
    p2 = input("Enter the name of Player 2")
    pp1 = 0
    pp2 = 0
    
    willing = True
    turn = 0
    while(willing):
        if (turn%2==0):
            #player 1
            print(p1, "Your Turn: ")
            pickedMovie = random.choice(movies)
            qn  = createQuestion(pickedMovie)
            print(qn)
            modified_qn = qn
            
            not_said = True
            while(not_said):
                ch = input("Your letter: ")
                if(is_present(ch, pickedMovie)):
                    #unlock
                    modified_qn = unlock(modified_qn, pickedMovie, ch)
                    print(modified_qn)
                    
                    d = input("Press 1 to guess movie name or 2 to unlock more characters")
                    if d==1:
                        ans = input("Enter your answer: ")
                        if ans == pickedMovie:
                            print("You guessed it right")
                            pp1+= 1
                            not_said = False
                else: 
                    print(ch, " not found ")
        else:
            #player 2
        turn = turn+1
            
        
    
play()