from flask import Flask, render_template, request
from random import *
from datetime import datetime

app = Flask(__name__)

# Alle Witze in einer einfachen Liste
WITZ_DATEN = [
    "Was sagt ein Genervter zu einem Taschenmesser? 'Klappe zu!'",
    "Was ist ein Keks unter einem Baum? Ein schattiges Plätzchen.",
    "Was macht ein Clown im Büro? Faxen.",
    "Wie nennt man ein Kaninchen im Fitnessstudio? Pumpernickel.",
    "Warum können Skelette so schlecht lügen? Weil sie so leicht zu durchschauen sind.",
    "Wie viele Programmierer braucht man, um eine Glühbirne zu wechseln? Keinen, das ist ein Hardware-Problem.",
    "Ein Informatiker stellt sich jeden Abend ein volles und ein leeres Glas Wasser neben sein Bett. Warum? – Das volle Glas hat er, falls er in der Nacht aufwacht und Durst hat. Und das leere Glas, falls er in der Nacht aufwacht und keinen Durst hat.",
    "Ein Informatiker schiebt einen Kinderwagen durch den Park. Kommt ein älteres Ehepaar: Junge oder Mädchen? Informatiker: Richtig!",
    "Wie trinken Programmierer den Kaffee? 0x000000 natürlich.",
    "Ich habe ein Brötchen angerufen, aber es war belegt.",
    "Die wichtigsten zwei Worte in der Gastronomie? 'Zahlen bitte!'",
    "Was ist die Lieblingsspeise von Autos? Parkplätzchen."
]

LEHRERWITZE = [
    "Lehrer : 'Nenne mir die drei Steigerungsstufen von leer.' Max: 'Leer, leerer, Lehrerzimmer.'",
    "Schüler: 'Warum ist meine Informatik-Note so schlecht?' – Lehrer: 'Du hast im Binärtest eine 2 geschrieben.'",
    "Lehrer: 'Wieso kommst du 20 Minuten zu spät?' Schüler: 'Sie haben doch gesagt, es ist nie zu spät zum Lernen!'",
    "Lehrer: 'Wo wurden die Friedensverträge des Dreissigjährigen Krieges unterschrieben?' Schüler: 'Ganz unten rechts auf der letzten Seite!'"
]

@app.route('/', methods=['GET', 'POST'])
def index_seite():
    ausgabe = None
    
    if request.method == 'POST':
        # Wir schauen, welcher Button-Wert (action) gesendet wurde
        aktion = request.form.get('action')

        if aktion == 'witz':
            zufallszahl = randint(0, len(WITZ_DATEN)-1) 
            ausgabe = WITZ_DATEN[zufallszahl]

        elif aktion == 'lehrerwitz':
            zufallszahl = randint(0, len(LEHRERWITZE)-1)
            ausgabe = LEHRERWITZE[zufallszahl]
            
        elif aktion == 'zeit':
            # Datum und Zeit ermitteln
            jetzt = datetime.now()
            ausgabe = jetzt.strftime('Heute ist der %d.%m.%Y. Es ist %H:%M Uhr.')
            
    return render_template('index.html', witz=ausgabe)

if __name__ == '__main__':
    app.run(debug=True, port=8087, use_reloader=False)