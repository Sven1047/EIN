import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()  # Graph Objekt (Behälter)

# Definiere Node IDs
nodes = ["C1", "C2", "C3", "C4", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"]

# Definiere Kanten
edges = [ ("C1", "C2"), ("C2", "C3"), ("C3", "C4"),\
          ("C1", "H1"), ("C1", "H2"), ("C1", "H3"),\
          ("C2", "H4"), ("C2", "H5"),\
          ("C3", "H6"), ("C3", "H7"),\
          ("C4", "H8"), ("C4", "H9"), ("C4", "H10")]

# füge Knoten und Kanten zu G
G.add_nodes_from(nodes)
G.add_edges_from(edges)

plt.figure(figsize=(5, 5))
plt.xlim(0, 1)
plt.ylim(0, 1)

pos = {
    # C-Kette
    "C1": (0.2, 0.5),
    "C2": (0.4, 0.5),
    "C3": (0.6, 0.5),
    "C4": (0.8, 0.5),

    # Hydrogens for C1
    "H1": (0.1, 0.5),   
    "H2": (0.2, 0.6),  
    "H3": (0.2, 0.4),
    
    # Hydrogens for C2
    "H4": (0.4, 0.6),  
    "H5": (0.4, 0.4),
    
    # Hydrogens for C3
    "H6": (0.6, 0.6),  
    "H7": (0.6, 0.4),
    
    # Hydrogens for C3
    "H8": (0.8, 0.6),  
    "H9": (0.8, 0.4),
    "H10": (0.9, 0.5)

}


# gib mir die Adjazenz-Matrix
A = nx.adjacency_matrix(G).todense()

print(A)

invalid_molecule = False

for i in range(len(nodes)):
    line = A[i]
    counter = 0
    if "C" in nodes[i]:
        print("Index:", i , " this is a H atom")
        print("This is a C atom")
        if sum(line) == 4:
            print("it has 4 connections. good!")
        else:
            invalid_molecule = True
            print("this C atom does not have 4 connections. There's something wrong!")
    
    if "H" in nodes[i]:
        print("Index:", i , " this is a H atom")
        if sum(line) == 1:
            print("it has 1 connection. good!")
        else:
            invalid_molecule = True
            print("this C atom does not have 1 connection. There's something wrong!")

if(invalid_molecule):
    print("INVALID MOLECULE")
else:
    print("VALID MOLECULE")
    

# Zeichne den Graph
nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
plt.show()



