import matplotlib.pyplot as plt
from random import *
import csv



filename = "countries.csv"
csvfile = open(filename, newline='')
reader = csv.DictReader(csvfile)
country_name = []
country_literacy = []
country_gdppercapita = []
country_population = []

print(country_gdppercapita)

for row in reader:
    name = row["Country"]
    literacy = float(row["Literacy"])
    gdppercapita = float(row["GDP per capita"])
    population = float(row["Population"])
    country_name.append(name)
    country_literacy.append(literacy)
    country_gdppercapita.append(gdppercapita)
    country_population.append(population)

# Scatterplot
plt.scatter(country_gdppercapita, country_literacy)

plt.xlim(0)
plt.ylim(0)

# Titel für den Graph
plt.title("literacy vs gdp per capita")

# Labels für die Länder
for i in range(len(country_literacy)):
    plt.text(country_gdppercapita[i], country_literacy[i], country_name[i], fontsize = 8) 

  
# Plotten bitte
plt.show()



    
    
    