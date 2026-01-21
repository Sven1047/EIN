from textblob_de import TextBlobDE as TextBlob
import matplotlib.pyplot as plt

text = "Liebe G25s. Ich muss euch dringendst auffordern, beim Betreten des Zimmers 010 mehr Vorsicht walten zu lassen. Es ist nun bereits zum x-ten mal passiert, dass Schüler aus eurer Klasse während meines Unterrichts (und notabene vor dem Klingeln) auf mitunter tolpatschige Art und Weise die Türe geöffnet haben und ins Zimmer gelaufen sind, um dann festzustellen, dass ich am unterrichten bin. Das ist seit Beginn dieses Semesters gefühlt jede 2.Woche passiert. Meine bisher in Grenzen gehaltene Verärgerung darüber habe ich jeweils kundgetan, leider mit begrenzter Wirkung. Ich muss hier protestieren, das geht so nicht. Ich will euch darauf hinweisen, dass ihr Schulzimmer nicht einfach aufreissen und reinplatzen dürft. Schon gar nicht, wenn die Schulstunden noch nicht zu Ende sind. In dem Sinne, ich hoffe auf Einsicht. Ich schätze eure Klasse sehr, ihr habt viel Energie und seid begeisterungsfähig. Aber ihr müsst hier besser aufpassen und mehr Rücksicht walten lassen."
x_achse =  []
y_achse = []

blob = TextBlob(text)
sentences = blob.sentences

for i in range(len(sentences)):
    print("Satz ", i , ":", sentences[i])
    print("Sentiment: ", sentences[i].sentiment.polarity)
    x_achse.append(i)
    y_achse.append(sentences[i].sentiment.polarity)

print("Gesamt-Sentiment:",  blob.sentiment.polarity)

plt.plot(x_achse, y_achse, color='green')

plt.ylim(-1,1)
plt.xlim(0, len(sentences)-1)

plt.show()

