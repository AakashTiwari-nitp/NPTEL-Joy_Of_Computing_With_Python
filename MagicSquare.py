#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 18:44:39 2025

@author: aakash-tiwari
"""

n = int(input("Enter the size of the square: "))

#magicsq = []

"""
#def magicSquare(n):
    if(n%2==0):
        print("The magic square of the given number can't be formed")
        return
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicsq.append(l)
    
    p = n//2
    q = n-1
    num = 1
    m = n * (n**2+1) // 2
    #print(m)
    
    while(num<=n*n):
        magicsq[p][q] = num
        num+= 1
        if(num>n*n):
            break
        
        p-=1
        q+=1
        #print(p, q)
        
        while(p==-1 or q == n or magicsq[p][q]):
            if(p==-1 and q == n):
                p = 0
                q = n-2
            elif(p==-1):
                p = n-1
            elif(q == n):
                q = 0
            elif(magicsq[p][q]):
                p+=1
                q-=2
                
        #print(p, q)
        #if(num==4):
            #break
    
    for i in range(n):
            for j in range(n):
                print(magicsq[i][j], end=" ")
            print() 
"""

def magicSquare(n):
    magicsq = []
    
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicsq.append(l)
        
        
    i = n//2
    j = n-1
    cnt = 1
    num = n*n
    
    while(cnt<=num):
        if(i==-1 and j == n):
            i = 0
            j = n-2
            
        else:
            if(i==-1):
                i = n-1
            if(j==n):
                j = 0
                
        if(magicsq[i][j]):
            i+=1
            j-=2
            continue
        else:
            magicsq[i][j] = cnt
            cnt+=1
        
        i-=1
        j+=1
        
    for i in range(n):
        for j in range(n):
            print(magicsq[i][j], end = " ")
        print()
        
    print("The sum of each row, column or diagonal is:", n*(n**2+1)//2)        

magicSquare(n)


    