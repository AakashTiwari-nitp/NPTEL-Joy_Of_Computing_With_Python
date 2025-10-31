#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 00:28:28 2025

@author: aakash-tiwari
"""

import networkx as nx
import matplotlib.pyplot as plt

# G = nx.gnp_random_graph(50, 0.3)
G = nx.barabasi_albert_graph(50, 2)

nx.draw(G)
plt.show()

print(G.nodes) 
print(G.edges())
print(G.degree(0))

nx.write_gexf(G, "analysis.gexf")