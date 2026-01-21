import math

import matplotlib.pyplot as plt

x_plot=[]
y_plot=[]
y2_plot=[]

# wir generieren zahlen von 0 bis und mit 100
for x in range(1,102):
    x_plot.append(x)
    
    y = (x-1)**0.5
    y_plot.append(y)

    y2_plot.append(math.log10(x))

# jetzt haben wir alle Tupel (x,y) für x zwischen 0 bis und mit 100
        
# Das wollen wir jetzt plotten. Aber wir müssen zuerst einiges definieren
plt.plot(x_plot, y_plot, color ='green')
plt.plot(x_plot,y2_plot, color='blue')
  
# Grafik soll bei (0,0) beginnen
plt.ylim(0,10)
plt.xlim(0,100)
  
# Wir setzen einen Namen für die x Achse 
plt.xlabel("x-Achse") 
# Wir setzen einen Namen für die y Achse
plt.ylabel("y-Achse") 

# Wir definieren wie viele Einheiten wir wollen auf den Achsen (nbins)
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)
  
# Wir setzen den Titel für den Graph
plt.title("die Wurzelfunktion") 
  
# Nun plotten bitte, los!
plt.show() 