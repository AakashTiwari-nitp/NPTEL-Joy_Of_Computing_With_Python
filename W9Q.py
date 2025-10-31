#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 23:32:20 2025

@author: aakash-tiwari
"""

"""
import networkx as nx # used for creating and analyzing the graph
import matplotlib.pyplot as plt # helps us visualize the graph

G = nx.Graph() # creates an empty undirected graph named G.

G.add_node("Alice")
G.add_node("Bob")
# add two individual nodes to our graph


G.add_edge("Alice", "Bob") #  adds a connection between Alice and Bob

G.add_edges_from([("Bob", "Charlie"), ("Alice", "David")]) # add multiple edges at once

# "Charlie" or "David" weren’t added earlier, they will be automatically created.

nx.draw(G, with_labels=True) # creates a visual layout, and with_labels=True ensures that node names (like "Alice") are shown
plt.show() # displays the graph window.

print("Nodes:", G.nodes()) # Nodes: ['Alice', 'Bob', 'Charlie', 'David']
print("Edges:", G.edges()) # Edges: [('Alice', 'Bob'), ('Alice', 'David'), ('Bob', 'Charlie')]

print("Number of nodes:", G.number_of_nodes()) # Number of nodes: 4
print("Number of edges:", G.number_of_edges()) # Number of edges: 3
"""

"""
import networkx as nx
G = nx.Graph()
G.add_edge("A", "B")
print("C" in G.nodes()) # False
"""

"""
import networkx as nx
G = nx.Graph()

G.add_edges_from([("X", "Y"), ("Y", "Z")])
print (G.number_of_nodes()) # 3
"""

"""
import networkx as nx
G = nx.Graph()
G.add_node("Tom")
print(G.number_of_edges()) # 0
"""

"""
import networkx as nx
G = nx.Graph()
G.add_node("A")
G.add_node("B")
print(G.edges()) # []
"""


"""
import networkx as nx
G = nx.Graph()
G.add_edges_from([("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "David"), ("Alice", "David")])

print(G.degree("Bob")) # 2 # The degree of a node is the number of edges connected to it

print(list(G.neighbors("Charlie"))) # ['Bob', 'David'] # To get all nodes connected to a particular node (its neighbors

print(nx.has_path(G, "Alice", "Charlie")) # True # To check if there is a path between two nodes

print(nx.shortest_path(G, "Alice", "Charlie")) # ['Alice', 'Bob', 'Charlie'] # To find the shortest connection between two nodes

print(G.degree("Charlie")) # 2

print(list(G.neighbors("Bob"))) # ['Alice', 'Charlie']
"""
"""
import networkx as nx
edges = [("A", "B"), ("B", "C"), ("C", "D")]
G = nx.Graph()

G.add_edges_from(edges)
print(len(G.nodes())) # 4
"""

"""
import networkx as nx
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
degrees = {node: G.degree(node) for node in G.nodes()}
print(degrees["B"]) # 2
"""

"""
import networkx as nx
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
path = nx.shortest_path(G, "A", "C")
print(path[1]) # B
"""

"""
import networkx as nx
G = nx.Graph()

G.add_edges_from([("A", "B"), ("C", "D")])

pairs = [("A", "B"), ("A", "C")]

results = [nx.has_path(G, u, v) for u, v in pairs]
print(results) # [True, False]
"""

"""
import networkx as nx
G = nx.Graph()

G.add_edges_from([("X", "Y"), ("Y", "Z")])

nodes = ["X", "Z"]
paths = {n: nx.shortest_path(G, "X", n) for n in nodes}
print(paths) # {'X': ['X'], 'Z': ['X', 'Y', 'Z']}
"""

import networkx as nx
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D")])
high_deg = [n for n in G.nodes() if G.degree(n) > 1]
print(high_deg) # ['B', 'C']

