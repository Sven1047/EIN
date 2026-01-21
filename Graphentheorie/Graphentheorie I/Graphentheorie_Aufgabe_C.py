import matplotlib.pyplot as plt
import pandas
import networkx as nx
import random

# funktion für zufällig 0 oder 1 - mit 40% Wahrscheinlichkeit für eine 1
def random01():
    if random.random()<0.4:
        return 1
    else:
        return 0


G = nx.Graph() # Graph Objekt (Behälter)

# hier erstellen wir einen 7x7 Graphen
AdjMatrix = [[0,1,1,1,1,1,1],
             [1,0,1,1,1,1,1],
             [1,1,0,1,1,1,1],
             [1,1,1,0,1,1,1],
             [1,1,1,1,0,1,1],
             [1,1,1,1,1,0,1],
             [1,1,1,1,1,1,0]]


# Hier: setze die Gewichte zufällig!
for i in range(len(AdjMatrix)):
    print("Zeile: ", i)

# Die Labels
labels = ["A", "B", "C", "D", "E", "F", "G"]

# wir brauchen sogenannte "Pandas"-Dataframes
AdjMatrix = pandas.DataFrame(AdjMatrix, index=labels, columns=labels)

# Zeichne den Graph
nx.draw_networkx(nx.from_pandas_adjacency(AdjMatrix))
plt.show()

