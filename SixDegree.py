#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 09:08:42 2025

@author: aakash-tiwari
"""

import networkx as nx
import numpy as np

G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes())

spll = []

for u in N:
    for v in N:
        if u!=v:
            l = nx.shortest_path_length(G, u, v)
            # print(f"Shortest path between {u} and {v} is of length: {l}",)
            spll.append(l)
         
min_spl = min(spll)
max_spl= max(spll)
average_spl =  np.average(spll)
 
print("Minimum Shortest Path Length:", min_spl)
print("Maximum Shortest Path Length:", max_spl)
print("Average Shortest Path Length:", average_spl)
