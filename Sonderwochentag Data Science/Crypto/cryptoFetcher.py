import ccxt
import time
from datetime import datetime


UPDATE_INTERVAL_SECONDS = 1  # Aktualisierungsintervall in Sekunden 
CRYPTO_PAIR = 'BTC/USDT'
EXCHANGE_ID = 'binance'

while True:
    # Daten abrufen
    exchange = getattr(ccxt, EXCHANGE_ID)()
    exchange.load_markets()
    
    ticker = exchange.fetch_ticker(CRYPTO_PAIR)
    current_price = ticker['last']
            
    # Zeitstempel 
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time,"| Aktueller Preis: ", current_price)
    time.sleep(UPDATE_INTERVAL_SECONDS)

