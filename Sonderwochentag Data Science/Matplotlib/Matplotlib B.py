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

for row in reader:
    name = row["Country"]
    literacy = float(row["Literacy"])
    gdppercapita = float(row["GDP per capita"])
    population = float(row["Population"])
    country_name.append(name)
    country_literacy.append(literacy)
    country_gdppercapita.append(gdppercapita)
    country_population.append(population)


#########################################################

x_plot=[]
y_plot=[]

for i in range(100):
    x_plot.append(randint(0,100))
    y_plot.append(randint(0,100))
    
        
plt.scatter(country_gdppercapita, country_literacy)
plt.xlabel("GDP per capita")
plt.ylabel("Literacy")

plt.xlim(0,70000)
plt.ylim(0,1)

# definieren wieviele Einheiten man will auf den Achsen
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)
  
# Titel für den Graph
plt.title("Literacy vs. GDP per capita")

for i in range(0,len(country_name)):
    plt.text(country_gdppercapita[i], country_literacy[i], country_name[i], fontsize = 5)

# Plotten bitte
plt.show()



    
    
    