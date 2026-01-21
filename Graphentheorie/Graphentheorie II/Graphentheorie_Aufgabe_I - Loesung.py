import math


labels = ["A","B","C","D","E","F","G"]

matrix = [[0,5,7,4,0,0,0],
          [5,0,3,0,9,0,0],
          [7,3,0,5,0,8,1],
          [4,0,5,0,0,3,0],
          [0,9,0,0,0,0,4],
          [0,0,8,3,0,0,1],
          [0,0,1,0,4,1,0]]

def main():    
    druckeMatrix(matrix)
    N = len(matrix)
    
    # zur Vereinfachung fangen wir immer mit dem Knoten 0 an
    knoten_spanning_tree = [0]
    edges = []
    
    billigste_erweiterung_startknoten = 0
    billigste_erweiterung_zielknoten = math.inf
    billigste_erweiterung_zielknoten_kosten = math.inf
    
    while(len(knoten_spanning_tree)<N):
        # nun iterieren wir über alle Knoten 1-N
        for knoten_index in range(0,N):
            if knoten_index not in knoten_spanning_tree:
                print("Knoten: ", knoten_index , " ist noch nicht in Spanning Tree")
                print("Knoten: ", knoten_index,  " hat folgende Kanten in den Spanning Tree:")
                for i in range(0,N):
                    if matrix[knoten_index][i] > 0 and i in knoten_spanning_tree:
                        print(knoten_index, "-", i, " mit Kosten", matrix[knoten_index][i])
                        if matrix[knoten_index][i] < billigste_erweiterung_zielknoten_kosten:
                            billigste_erweiterung_startknoten = i
                            billigste_erweiterung_zielknoten_kosten = matrix[knoten_index][i]
                            billigste_erweiterung_zielknoten = knoten_index
                        
        print("nächster Schritt: neue Kante ", billigste_erweiterung_startknoten, " - ", billigste_erweiterung_zielknoten, " kosten:", billigste_erweiterung_zielknoten_kosten, " | ", labels[billigste_erweiterung_startknoten], " - ", labels[billigste_erweiterung_zielknoten])
        # füge das neue Element der knoten_spanning_tree hinzu
        knoten_spanning_tree.append(billigste_erweiterung_zielknoten)
        # füge die neue Kante hinzu
        edges.append([billigste_erweiterung_startknoten,billigste_erweiterung_zielknoten])
        
        billigste_erweiterung_zielknoten = math.inf
        billigste_erweiterung_zielknoten_kosten = math.inf
        
        print("Die folgenden Kanten sind Teil des Minimum Spanning Tree:")
        for edge in edges:
            print(edge, " |", labels[edge[0]] + "-" + labels[edge[1]])
        
    
def druckeMatrix(matrix):
    for zeile in matrix:
        z = ""
        for element in zeile:
            z += str(element) + " "
        print(z)

main()

