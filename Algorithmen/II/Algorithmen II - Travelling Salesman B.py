cities = ["A", "B", "C"]


def nextCity(current_path, cities_remaining):
    if len(cities_remaining) == 0:
        print(current_path)
    else:
        for i in range(len(cities_remaining)):
            new_current = current_path.copy()
            new_current.append(cities_remaining[i])
            new_cities_remaining = cities_remaining.copy()
            new_cities_remaining.pop(i)
            nextCity(new_current, new_cities_remaining)


nextCity([], cities)
