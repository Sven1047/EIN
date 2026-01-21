import matplotlib.pyplot as plt
from random import *
import csv



filename = "countries_moredata.csv"
csvfile = open(filename, newline='')

reader = csv.DictReader(csvfile)
country_name = []
country_literacy = []
country_gdppercapita = []
country_population = []
country_life_expectancy = []

for row in reader:
    name = row["Country"]
    literacy = row["Literacy"]
    gdppercapita = row["GDP per capita"]
    population = row["Population"]
    life_expectancy = row["Life Expectancy"]
        
    literacy = float(literacy)
    gdppercapita = float(gdppercapita)
    population = float(population)
    life_expectancy = float(life_expectancy)
    
    country_name.append(name)
    country_literacy.append(literacy)
    country_gdppercapita.append(gdppercapita)
    country_population.append(population)
    country_life_expectancy.append(life_expectancy)

# Scatterplot
plt.scatter(country_gdppercapita, country_life_expectancy)

plt.xlim(0)
plt.ylim(0)

# Titel für den Graph
plt.title("life expectancy vs gdp per capita")

# Labels für die Länder
for i in range(len(country_literacy)):
    plt.text(country_gdppercapita[i], country_life_expectancy[i], country_name[i], fontsize = 8) 

  
# Plotten bitte
plt.show()



    
    
    