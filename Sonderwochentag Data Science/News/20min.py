import feedparser

def lese_20min_feed(feed_url, anzahl_artikel):
    print("Lese RSS-Feed von: ", feed_url)
    
    # einlesen
    feed = feedparser.parse(feed_url)
    
    # Überprüfen, ob der Feed erfolgreich geparst wurde
    if feed.bozo:
        print("❗️ FEHLER beim Parsen des Feeds. Die URL ist möglicherweise ungültig oder der Feed hat ein Problem.")
        print("Fehlerdetails: ", feed.bozo_exception)
        return

    # Informationen zum Feed ausgeben
    feed_titel = feed.feed.get('title', 'Unbekannter Feed')
    print("Feed-Titel: ", feed_titel)
    print("-" * 50)

    # Die Artikel (Entries) verarbeiten
    artikel_zaehler = 0
    for entry in feed.entries:
        if artikel_zaehler >= anzahl_artikel:
            break
        
        # Titel (title)
        titel = entry.get('title', 'Kein Titel vorhanden')
        
        # Link (link)
        link = entry.get('link', 'Kein Link vorhanden')
        
        # 1. Im Originalformat des Feeds (oft ein String)
        pubdate_str = entry.get('published', 'Kein Datum vorhanden (String)')
        
        # 2. Als geparstes Datumstempel-Tupel (zur Formatierung empfohlen)
        pubdate_parsed = entry.get('published_parsed')
        
        # Optional: Umwandlung des Tupels in einen lesbaren String
        if pubdate_parsed:
            import time
            # Hier formatieren wir das Datum lesbar, z.B. 'Freitag, 31. Oktober 2025 - 15:42'
            pubdate_formatiert = time.strftime('%A, %d.%m.%Y - %H:%M', pubdate_parsed)
        else:
            pubdate_formatiert = pubdate_str # Fallback auf den String, falls das Parsen fehlschlägt
        
        
        # Zusammenfassung (summary oder description, hier summary bevorzugt)
        # Wir entfernen HTML-Tags für eine saubere Konsolenausgabe
        summary = entry.get('summary', 'Keine Zusammenfassung vorhanden')
        
        # Einfache Entfernung von HTML-Tags (kann für komplexere Fälle verbessert werden)
        saubere_summary = summary.replace('<p>', '').replace('</p>', '').replace('<b>', '').replace('</b>', '').strip()
        
        print("Artikel: ", artikel_zaehler + 1)
        print("  Titel: ", titel)
        print("  Link:  ", link)
        print("  Datum: ", pubdate_formatiert)
        print("  Zusammenfassung: ", saubere_summary)
        print("-" * 50)
        
        artikel_zaehler += 1

    if not feed.entries:
        print("Keine Artikel im Feed gefunden.")

# --- Hauptprogramm ---
FEED_URL = "https://partner-feeds.beta.20min.ch/rss/20minuten/schweiz"
ANZAHL = 500 # Anzahl der anzuzeigenden Artikel

# Funktion aufrufen
lese_20min_feed(FEED_URL, ANZAHL)