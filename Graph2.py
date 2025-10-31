#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 19:23:27 2025

@author: aakash-tiwari
"""

import networkx as nx

U = nx.Graph() # Undirected Graph

G = nx.DiGraph() # Directed Graph

print(G.nodes()) # [] 

G.add_nodes_from([i for i in range(5)])

print(G.nodes()) # [0, 1, 2, 3, 4]

print(G.edges()) # []
print(G.out_edges()) # []
print(G.in_edges()) # []

G.add_edge(1, 2)

print(G.edges()) # [(1, 2)]
print(G.out_edges()) # [(1, 2)]
print(G.in_edges()) # [(1, 2)]

print(G.out_edges(1)) # [(1, 2)]

print(G.in_edges(1)) # []

G.add_edge(0, 3)
G.add_edge(2, 3)
G.add_edge(3, 2)
G.add_edge(3, 4)
G.add_edge(4, 1)

print(G.out_edges(2)) # [(2, 3)]

print(G.out_edges(3)) # [(3, 2), (3, 4)]

print(G.in_edges(3)) # [(0, 3), (2, 3)]
