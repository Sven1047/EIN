from textblob_de import TextBlobDE as TextBlob 
import matplotlib.pyplot as plt


text = "Liebe G25s. "
text += "Ich muss euch dringendst auffordern, beim Betreten des Zimmers 010 mehr Vorsicht walten zu lassen. "
text += "Es ist nun bereits zum x-ten mal passiert, dass Schüler aus eurer Klasse während meines Unterrichts"
text += " (und notabene vor dem Klingeln) auf mitunter toplatschige Art und Weise die Türe geöffnet haben "
text += " und ins Zimmer gelaufen sind, um dann festzustellen, dass ich am unterrichten bin. Das ist seit Beginn "
text += " dieses Semesters gefühlt jede zweite Woche passiert. Meine bisher in Grenzen gehaltene Verärgerung darüber "
text += " habe ich jeweils kundgetan, leider mit begrenzter Wirkung."
text += " Ich musste meine Stunde abbrechen, es ging so nicht mehr."
text += " Ich muss hier protestieren, das geht so nicht. Ich will euch darauf hinweisen, dass ihr Schulzimmer nicht "
text += " einfach aufreissen und reinplatzen dürft. Schon gar nicht, wenn die Schulstunden noch nicht zu Ende sind."
text += " In dem Sinne, ich hoffe auf Einsicht. Ich schätze eure Klasse sehr, ihr habt viel Energie und seid "
text += " begeisterungsfähig. Aber ihr müsst hier besser aufpassen und mehr Rücksicht walten lassen. "


blob = TextBlob(text)
sentences = blob.sentences


x_plot=[]
y_plot=[]

for i in range(len(sentences)):
    print("Satz ", i , ":", sentences[i])
    print("Sentiment: ", sentences[i].sentiment.polarity)
    
    x_plot.append(i)
    y_plot.append(sentences[i].sentiment.polarity)

print("Gesamt-Sentiment:",  blob.sentiment.polarity)



    

# jetzt haben wir alle Tupel (x,y) für x zwischen 0 bis und mit 100
        
# Das wollen wir jetzt plotten. Aber wir müssen zuerst einiges definieren
plt.plot(x_plot, y_plot, color ='green')
  
# Grafik soll bei (0,0) beginnen
plt.ylim(-1)
plt.xlim(0, len(sentences)-1)

  
# Wir setzen einen Namen für die x Achse 
plt.xlabel("Satz") 
# Wir setzen einen Namen für die y Achse
plt.ylabel("Sentiment") 

# Wir definieren wie viele Einheiten wir wollen auf den Achsen (nbins)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
  
# Wir setzen den Titel für den Graph
plt.title("Stimmungsverlauf des analysierten Textes") 
  
# Nun plotten bitte, los!
plt.show() 