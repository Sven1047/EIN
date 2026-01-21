import requests
import json
import codecs

# Die Basis-URL für alle Ratsmitglieder
api_url_all = "https://ws-old.parlament.ch/councillors/"

def debug_councillors(url):
    raw_content = None
    try:
        print("Lade Daten von:", url)
        response = requests.get(url)
        response.raise_for_status() 
        
        raw_content = response.content
        
        # 1. Schreibe den rohen Inhalt in eine Datei zur Untersuchung
        filename = "api_response_raw.html"
        with open(filename, 'wb') as f:
            f.write(raw_content)
        print("Roher API-Inhalt in", filename, " zur manuellen Prüfung gespeichert.")
        
    except Exception as e:
        print("Ein unerwarteter Fehler ist aufgetreten:", e)

# Hauptfunktion und Aufruf
if __name__ == "__main__":
    debug_councillors(api_url_all)