import yfinance as yf
import time
from datetime import datetime


UPDATE_INTERVAL_SECONDS = 5  # Aktualisierungsintervall in Sekunden
STOCK_TICKER="LMND"

while True:
    # 1. Daten abrufen
    # hole die Aktie
    stock = yf.Ticker(STOCK_TICKER)
    info = stock.info

    # Preis extrahieren
    current_price = info.get('currentPrice', 'N/A')
    
    # Zeitstempel 
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time,"| Aktueller Preis: ", current_price)
    time.sleep(UPDATE_INTERVAL_SECONDS)

