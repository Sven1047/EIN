import matplotlib.pyplot as plt
import pandas
import networkx as nx

G = nx.Graph() # Graph Objekt (Behälter)

AdjMatrix = [[0,1,1,1,0,0,0],
             [1,0,1,0,1,0,0],
             [1,1,0,1,0,1,1],
             [1,0,1,0,0,1,0],
             [0,1,0,0,0,0,1],
             [0,0,1,1,0,0,1],
             [0,0,1,0,1,1,0]]

# node labels
labels = ["A", "B", "C", "D", "E", "F", "G"]

# wir brauchen sogenannte "Pandas"-Dataframes
AdjMatrix = pandas.DataFrame(AdjMatrix, index=labels, columns=labels)

# Zeichne den Graph
nx.draw_networkx(nx.from_pandas_adjacency(AdjMatrix))
plt.show()
