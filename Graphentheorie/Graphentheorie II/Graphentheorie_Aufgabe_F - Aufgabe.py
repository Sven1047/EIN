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



