import math

def main():    
    
    matrix =    [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0],
                 [0, 1, 0, 1, 0, 1],
                 [0, 1, 1, 0, 1, 0],
                 [0, 0, 0, 1, 0, 1],
                 [0, 0, 1, 0, 1, 0]]
    
    # Programm beurteilt, ob ein Graph zyklisch 
    druckeMatrix(matrix)
      
    start = 0
    besucht = [0]
    besucht_index = 0
    
    duplikat_gefunden = False
    waechst = True
    
    while(duplikat_gefunden == False and waechst == True):
        waechst = False
        letzter = start
        start = besucht[besucht_index]
        besucht_index = besucht_index+1
        neighbors = getNeighborsOf(start, matrix)
        if len(neighbors)>0:
            for n in neighbors:
                if(not n in besucht and n!=letzter):
                    besucht.append(n)
                    waechst = True
                else:
                    if n==letzter:
                        duplikat_gefunden = False
                    else:
                        duplikat_gefunden = True

    print("besuchte Knoten: ", len(besucht))
    if(duplikat_gefunden):
        print("Graph ist zyklisch")
    else:
        print("Graph ist nicht zyklisch")

def getNeighborsOf(start, matrix):
    neighbors = []
    for i in range(0, len(matrix)):
        if(matrix[start][i] != 0):
            neighbors.append(i)
    return neighbors
         
def druckeMatrix(matrix):
    for zeile in matrix:
        z = ""
        for element in zeile:
            z += str(element) + " "
        print(z)

main()


