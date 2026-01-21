import socket

name = "www.hurni.org"
port = 80

# Funktion zum Abrufen der Webseite
def get_website():
    # Erstellen eines TCP-Sockets
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((name, port))
    
    # HTTP-GET-Anfrage erstellen (für HTTP/1.0, da einfacher)
    # Wichtig: Die Zeile muss mit \r\n enden, und der Header muss mit einer leeren \r\n-Zeile abgeschlossen werden.
    request = f"GET / HTTP/1.0\r\nHost: {name}\r\n\r\n"
    
    # Anfrage als Bytes an den Server senden
    client_socket.sendall(request.encode('utf-8'))

    # Daten vom Server empfangen (Byte-weise)
    response = b""
    while True:
        # Empfange maximal 4096 Bytes
        chunk = client_socket.recv(4096)
        if not chunk:
            # Keine Daten mehr, Schleife beenden
            break
        response += chunk

    # Verbindung schliessen
    client_socket.close()

    # Ausgabe der empfangenen Daten (dekodiert)
    print("--- EMPFANGENE DATEN VOM SERVER ---")
    print(response.decode('latin-1')) # latin-1 oder iso-8859-1 ist oft sicherer für Header

# Funktion aufrufen, um die Webseite abzurufen
while True:
    get_website()