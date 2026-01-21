import time

def distance(cityX, cityY):
    return ((cityX[0]-cityY[0])**2 + (cityX[1]-cityY[1])**2)**(1/2)


final_paths = []
distances_final_paths = []

def nextCity(current_path, cities_remaining):
    if len(cities_remaining) == 0:
        dist = 0
        # Berechne immer stückweise die Distanzen
        for i in range(len(current_path)-1):                        
            dist = dist + distance(current_path[i], current_path[i+1])
        
        global final_paths
        global distances_final_paths
        
        final_paths.append(current_path)
        distances_final_paths.append(dist)
        
        print(current_path, "distance:", dist)
    else:
        for i in range(len(cities_remaining)):
            new_current = current_path.copy()
            new_current.append(cities_remaining[i])
            new_cities_remaining = cities_remaining.copy()
            new_cities_remaining.pop(i)
            nextCity(new_current, new_cities_remaining)



#         A         B          C          D         E
cities = [[0,300], [200,200], [400,300], [200,400], [5000,4500], [300,535], [400,2000]]

# we start the time
start = time.time()

# here we call the algorithm
nextCity([], cities)

shortest_path_distance = float('inf')
shortest_path = ""

for i in range(len(final_paths)):
    if distances_final_paths[i] < shortest_path_distance:
        shortest_path_distance = distances_final_paths[i]
        shortest_path = final_paths[i]

print("\n")
print("shortest_path_distance: ", shortest_path_distance)              
print("shortest_path: ", shortest_path)              

end = time.time()
elapsed = end - start

print("time elapsed for calculation (s): ", elapsed)

    
