#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 23:53:34 2025

@author: aakash-tiwari
"""

import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph()

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)

# l = [1, 2, 3]
# G.add_nodes_from(l)
 

# G.add_edge(1, 2)
# G.add_edge(2, 3)
# G.add_edge(1, 3)

# print(G.nodes()) # [1, 2, 3]
# print(G.edges()) # [(1, 2), (1, 3), (2, 3)] 

# G = nx.complete_graph(10)

G =nx.gnp_random_graph(20, 0.5)

nx.draw(G)
plt.show()

