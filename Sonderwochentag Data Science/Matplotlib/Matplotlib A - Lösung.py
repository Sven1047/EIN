import matplotlib.pyplot as plt

import math
 
x_plot=[]
y_plot=[]

logx_plot=[]
logy_plot=[]

for i in range(0,101):
    x_plot.append(i)
    y_plot.append(i**0.5)

for i in range(1,101):
    logx_plot.append(i)
    logy_plot.append(math.log10(i))
        

plt.plot(x_plot, y_plot, color ='green')
plt.plot(logx_plot, logy_plot, color ='red')
  
  
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

