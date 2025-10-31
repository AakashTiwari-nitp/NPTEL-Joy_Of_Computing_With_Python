#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 01:12:07 2025

@author: aakash-tiwari
"""

import networkx as nx #  used to handle the graph
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes = list(G.nodes())
    
    for s in nodes:
        for t in nodes:
            if s!=t: # ensures no self-loop is added
                r = random.random()
                if r<=0.5: # probability that an edge will be added between two distinct nodes
                    G.add_edge(s, t)
    return G

def assign_points(G): # assigns the starting points to nodes
    nodes = list(G.nodes)
    p = []
    for each in nodes:
        p.append(100)
    return p # List
     
def distribute_points(G, points):
    nodes = list(G.nodes())
    new_points =  []
    for i in range(len(nodes)):
         new_points.append(0)
    
    for n in nodes:
        out = list(G.out_edges(n))
        if (len(out)==0):
            new_points[n]+= points[n]
        else:
            share = points[n]/len(out)
            for src, target in out:
                new_points[target]+= share
    return new_points

def keep_distributing(points, G): # handles the repeated redistribution of points
    while 1:
        new_points = distribute_points(G, points)
        print(new_points)
        points = new_points
        stop = input("Enter # to stop or any other key to continue: ")
        if stop == "#":
            break
    return new_points
             
def rank_by_points(points): # ranks nodes by their final point values
    d = {} #  {node: points}
    for i in range(len(points)):
        d[i] = points[i]
    print(sorted(d.items(), key=lambda f:f[1]))
         

# create a directed graph
G = nx.DiGraph()

G.add_nodes_from([i for i in range(10)])

G=add_edges()

# Visualize the graph

nx.draw(G, with_labels=True) # Displays the graph visually
plt.show()
 
# assign initial points


points = assign_points(G)


# keep distributing

final_points = keep_distributing(points, G)

# rank by points
rank_by_points(final_points)

# default network function

result = nx.pagerank(G) # built-in function is used to calculate actual PageRank values
print(sorted(result .items(), key=lambda f:f[1]))

