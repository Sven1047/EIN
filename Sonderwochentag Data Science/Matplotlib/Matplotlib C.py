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
country_HDI = []
country_gini = []

for row in reader:
    name = row["Country"]
    literacy = row["Literacy"]
    gdppercapita = row["GDP per capita"]
    population = row["Population"]
    HDI = row["Human Development Index"]
    gini = row["Gini Index"]
        
    literacy = float(literacy)
    gdppercapita = float(gdppercapita)
    population = float(population)
    HDI = float(HDI)
    gini = float(gini)
    
    country_name.append(name)
    country_literacy.append(literacy)
    country_gdppercapita.append(gdppercapita)
    country_population.append(population)
    country_HDI.append(HDI)
    country_gini.append(gini)

# Scatterplot
plt.scatter(country_gini, country_HDI)

plt.xlim(0, 60)
plt.ylim(0, 1)

# Titel für den Graph
plt.title("Gini vs HDI")

# Labels für die Länder
for i in range(len(country_literacy)):
    plt.text(country_gini[i], country_HDI[i], country_name[i], fontsize = 5)

  
# Plotten bitte
plt.show()