import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # Graph Objekt (Behälter)

# Definiere Node IDs
nodes = ["A", "B", "C", "D", "E", "F", "G"]

# Definiere Kanten
# Tupel (id_1, id_2) stellt dar, dass id_1 und id_2 miteinander durch eine Kante verbunden sind
edges = [("A", "B"), ("A", "C"),("A","D"), ("B", "C"),("B","E"), ("C","D"),("C","F"),("C","G"),("E","G"),("F","D"),("F","G")]

# füge Knoten und Kanten zu G
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Zeichne den Graph
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
print(nx.modularity_matrix(G))