import math

def main():    
    
    # Programm beurteilt, ob ein Graph zusammenhängend ist
    matrix = [[0,5,7,4,0,0,0],
              [5,0,3,0,9,0,0],
              [7,3,0,5,0,8,1],
              [4,0,5,0,0,3,0],
              [0,9,0,0,0,0,4],
              [0,0,8,3,0,0,1],
              [0,0,1,0,4,1,0]]
    
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



