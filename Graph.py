#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 17:59:33 2025

@author: aakash-tiwari
"""

import networkx as nx
# G = nx.barbell_graph(4, 2)
# G = nx.barbell_graph(4, 3)
# G = nx.barbell_graph(5, 3)

# G = nx.complete_graph(5)

# G = nx.cycle_graph(6)

# G = nx.ladder_graph(5)

# G = nx.path_graph(5)

# G = nx.star_graph(5) # 5 outer node and 1 centre node 

# G = nx.wheel_graph(6)

G = nx.gnm_random_graph(5, 0.5) # number of node, probability as parameter

nx.draw(G) 