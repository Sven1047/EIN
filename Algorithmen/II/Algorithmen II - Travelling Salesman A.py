cities = ["A", "B", "C"]

# gehe mit der Variable city_I durch die ganze Liste cities
for city_I in cities:
    cities_I = cities.copy()
    cities_I.remove(city_I)
    
    # gehe mit der Variable city_III durch die ganze Liste cities,
    # aber city_III darf nicht city_I oder city_II sein (weil ist ja schon gewählt)   
    for city_II in cities_I:
        cities_II = cities_I.copy()
        cities_II.remove(city_II)
        
        # gehe mit der Variable city_III durch die ganze Liste cities,
        # aber city_III darf nicht city_I oder city_II sein (weil ist ja schon gewählt)
        for city_III in cities_II:
            cities_III = cities_II.copy()
            cities_III.remove(city_III)
            print(city_I,",", city_II,",", city_III,",", city_I)