#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 22:09:17 2025

@author: aakash-tiwari
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("facebook_combined.txt", create_using=nx.DiGraph(), nodetype=int)

nx.draw(G, with_labels=True)
plt.show()
