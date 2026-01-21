import math
import matplotlib.pyplot as plt
import pandas
import networkx as nx

G = nx.Graph() # Graph Objekt (Behälter)

    
labels = ["A","B","C","D","E","F","G"]

matrix = [[0,5,7,4,0,0,0],
          [5,0,3,0,9,0,0],
          [7,3,0,5,0,8,1],
          [4,0,5,0,0,3,0],
          [0,9,0,0,0,0,4],
          [0,0,8,3,0,0,1],
          [0,0,1,0,3,1,0]]

# wir brauchen sogenannte "Pandas"-Dataframes
AdjMatrix = pandas.DataFrame(matrix, index=labels, columns=labels)

gerichtet = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[j][i]:
            gerichtet = True
            print("matrix[", i, "][", j, "] != matrix[", i, "][", j, "]")

if gerichtet:
    print("Graph ist gerichtet")

G = nx.from_pandas_adjacency(AdjMatrix)

# Zeichne den Graph
nx.draw_networkx(nx.from_pandas_adjacency(AdjMatrix))
plt.show()