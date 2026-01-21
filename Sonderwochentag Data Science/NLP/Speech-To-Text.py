import speech_recognition as sr
import time
from textblob_de import TextBlobDE as TextBlob
import matplotlib.pyplot as plt

# Zeit in Sekunden
TIMEWINDOW = 10

def transcribe():
    # Recognizer-Objekt
    recognizer = sr.Recognizer()

    # Verwende das Standard-Mikrofon als Audioquelle
    with sr.Microphone() as source:
        print("Kalibrierung")
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        print("Sag etwas für ", TIMEWINDOW, " Sekunden.")
        
        try:
            # record() zeichnet die gesamte festgelegte Zeit (duration) oder bis zum Timeout auf 
            audio = recognizer.record(source, duration=TIMEWINDOW) 
            print("Audio aufgezeichnet...")

        except sr.WaitTimeoutError:
            print("Nichs gefunden...")
            return

    # Umwandlung in Sprache
    try:
        # Verwende die Google Web Speech API für die Erkennung
        text = recognizer.recognize_google(audio, language="de-DE") 
        
        print("Umgewandelt in Text:")
        print("--------------------")
        print(text)
        print("--------------------")

    # Fehlerbehandlung: wenn die API die Sprache nicht versteht
    except sr.UnknownValueError:
        print("Google Speech Recognition hat nichts erkennen können")
    
    # Fehlerbehandlung: wenn die API-Anfrage fehlschlägt (z.B. keine Internetverbindung)
    except sr.RequestError as e:
        print("Fehler mit with Google Speech Recognition Service:", e)

    return(text)


def sentiment_analyse(text):
    x_achse = []
    y_achse = []

    blob = TextBlob(text)
    sentences = blob.sentences

    for i in range(len(sentences)):
        print("Satz ", i, ":", sentences[i])
        print("Sentiment: ", sentences[i].sentiment.polarity)
        x_achse.append(i)
        y_achse.append(sentences[i].sentiment.polarity)

    print("Gesamt-Sentiment:", blob.sentiment.polarity)

    plt.plot(x_achse, y_achse, color='green')

    plt.ylim(-1, 1)
    plt.xlim(0, len(sentences))

    plt.show()

if __name__ == "__main__":
    text = transcribe()
    sentiment_analyse(text)

