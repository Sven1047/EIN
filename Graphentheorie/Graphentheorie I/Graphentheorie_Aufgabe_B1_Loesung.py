import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # Graph Objekt (Behälter)

# Definiere Node IDs
nodes = ["A", "B", "C", "D", "E", "F", "G"]

# Definiere Kanten
# Tupel (id_1, id_2) heisst dass id_1 und id_2 miteinander durch eine Kante verbunden sind
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "E"), ("E", "G"), ("G", "F"), ("F", "C"), ("C", "D"), ("D", "A"), ("C", "G"), ("F", "D")]

# füge Knoten und Kanten zu G
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# gib mir die Adjazenz-Matrix
A = nx.adjacency_matrix(G)
print(A.todense())
