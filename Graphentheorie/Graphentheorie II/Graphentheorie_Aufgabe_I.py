import matplotlib.pyplot as plt
import networkx as nx
import numpy
import pandas

matrix = [[0,5,7,4,0,0,0],
          [5,0,3,0,9,0,0],
          [7,3,0,5,0,8,1],
          [4,0,5,0,0,3,0],
          [0,9,0,0,0,0,4],
          [0,0,8,3,0,0,1],
          [0,0,1,0,4,1,0]]

A=numpy.matrix(matrix)
G=nx.from_numpy_array(A)
mapping = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G"}
G= nx.relabel_nodes(G, mapping)
pos=nx.spring_layout(G) 
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

edges_MST = []

while len(edges_MST) > len(matrix):
    for index in range(len(matrix)):
        if index in edges_MST:



T = nx.minimum_spanning_tree(G)
print("The minimum spanning tree edges:")
print(T.edges())
plt.show()


