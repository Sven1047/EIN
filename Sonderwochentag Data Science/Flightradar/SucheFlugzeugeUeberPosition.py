from FlightRadar24 import FlightRadar24API
from FlightRadar24.entities import Entity
import time
import os
import math

# ABFRAGEBEREICH
BREITENGRAD = 47.1786  # Breitengrad Sursee
LAENGENGRAD = 8.1064   # Längengrad Sursee

#BREITENGRAD = 47.4496  # Breitengrad Kloten
#LAENGENGRAD = 8.5822   # Längengrad Kloten

RADIUS_KILOMETER = 20  # Radius in KM
AKTUALISIERUNGS_INTERVALL_SEKUNDEN = 3 # Wie oft wird geprüft welche Flugzeuge da sind?   

def main():
    # Zugang zur FlightRadar-Schnittstelle
    flugradar_api = FlightRadar24API()
    # Begrenzung berechnen mit der API
    begrenzung_str = flugradar_api.get_bounds_by_point(BREITENGRAD, LAENGENGRAD, int(RADIUS_KILOMETER * 1000))

    # Prüfe intervallweise
    while True:

        # hier holen wir die Flüge und speichern sie in der Liste "fluege"
        fluege = flugradar_api.get_flights(bounds=begrenzung_str)
        # wir gehen nun durch alle Flüge durch und drucken diese als Tabelle
        if len(fluege) > 0:
            
            # Tabellentitel
            print(f"{'Flugnr':<10} | {'Flugzeugtyp':<12} | {'Flug Start':<18} | {'Flug Ziel':<18} | {'Breite':<10} | {'Länge':<10} | {'Höhe (ft)':<10} | {'Distanz (km)':<8}")
            print("-" * 105)
            
            for flug in fluege:
                if flug.callsign:
                    rufzeichen = flug.callsign
                else:
                    rufzeichen = 'N/A'
                    
                if hasattr(flug, 'aircraft_code') and flug.aircraft_code:
                    flugzeug_typ = flug.aircraft_code
                else:
                    flugzeug_typ = 'N/A'
                    
                if flug.origin_airport_iata:
                    start_iata = flug.origin_airport_iata
                else:
                    start_iata = 'unknown'
                    
                if flug.destination_airport_iata:
                    ziel_iata = flug.destination_airport_iata
                else:
                    ziel_iata = 'unknown'
                    
                # Hole hoehe, breitengrad, laengengrad    
                hoehe = flug.altitude
                breiten_ebene = flug.latitude
                laengen_ebene = flug.longitude
                
                # berechne die Distanz
                distanz = berechne_distanz_km(BREITENGRAD, LAENGENGRAD, breiten_ebene, laengen_ebene)
                # drucke den Flug
                drucke_flug(rufzeichen, flugzeug_typ, start_iata, ziel_iata, breiten_ebene, laengen_ebene, hoehe, distanz)
            
            print(len(fluege), "Flugzeuge gefunden")
            print()
        else:
            print("Keine Flüge im Radius ", RADIUS_KILOMETER, "km um Sursee gefunden.")
            
        time.sleep(AKTUALISIERUNGS_INTERVALL_SEKUNDEN)

def drucke_flug(rufzeichen, flugzeug_typ, start_iata, ziel_iata, breiten_ebene, laengen_ebene, hoehe, distanz_anzeige):
    start_iata = flughafencode_zu_stadt(start_iata)
    ziel_iata = flughafencode_zu_stadt(ziel_iata)
    print(f"{rufzeichen:<10} | {flugzeug_typ:<12} | {start_iata:<18} | {ziel_iata:<18} | {breiten_ebene:<10.5f} | {laengen_ebene:<10.5f} | {hoehe:<10} | {distanz_anzeige:<8}")

# Berechne die Distanz zwischen 2 Punkten mit 2 Koordinaten
def berechne_distanz_km(lat1, lon1, lat2, lon2):
    ERDE_RADIUS = 6371 # der Radius der Erde
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distanz = ERDE_RADIUS * c
    return round(distanz, 2)

def flughafencode_zu_stadt(code):
    datenbank = {
        # SCHWEIZ 
        "ZRH": "Zürich", "GVA": "Genf", "BSL": "Basel", "MLH": "Mulhouse", "BRN": "Bern","SMV": "Sion",
        "LUG": "Lugano","ACH": "St. Gallen","EML": "Emmen", "QYE":"Fribourg E.", "BXO":"Buochs",
        # DACH
        "FRA": "Frankfurt", "MUC": "München", "BER": "Berlin", "DUS": "Düsseldorf", "HAM": "Hamburg", "STR": "Stuttgart",
        "CGN": "Köln", "BRE": "Bremen", "NUE": "Nürnberg", "HAJ": "Hannover","LEJ": "Leipzig", "DRS": "Dresden", "FKB": "Karlsruhe",
        "FMO": "Münster/Osnabrück", "PAD": "Paderborn","VIE": "Wien", "QCF":"Freiburg im Brsg.","INN": "Innsbruck", "OBF": "Oberpfaffenhofen",
        # EUROPA
        "AMS": "Amsterdam", "CDG": "Paris", "ORY": "Paris", "NCE": "Nizza","FCO": "Rom", "CIA": "Rom", "MXP": "Mailand", "VCE": "Venedig", "BCN": "Barcelona",
        "MAD": "Madrid", "AGP": "Málaga", "LIS": "Lissabon", "OPO": "Porto","LHR": "London", "LGW": "London", "STN": "London", "MAN": "Manchester",
        "EDI": "Edinburgh", "IST": "Istanbul", "SAW": "Istanbul", "ATH": "Athen","SKG": "Thessaloniki", "PRG": "Prag", "WAW": "Warschau", "BUD": "Budapest",
        "DUB": "Dublin", "CPH": "Kopenhagen", "OSL": "Oslo", "ARN": "Stockholm","HEL": "Helsinki", "SVO": "Moskau", "LED": "Sankt Petersburg", 
        "BRU": "Brüssel", "LUX": "Luxemburg", "TLV": "Tel Aviv", "KBP": "Kiew","BEG": "Belgrad", "ZAG": "Zagreb", "SOF": "Sofia", "OTP": "Bukarest",
        "MLA": "Valletta (Malta)", "LCA": "Larnaka", "KEF": "Reykjavik","BHX": "Birmingham", "GLA": "Glasgow", "KRK": "Krakau", "TFS": "Teneriffa Süd",
        "PMI": "Palma de Mallorca", "CTA":"Catania", "TIA":"Tirana", "CLJ":"Cluj", "FLR": "Florenz","BLQ":"Bologna","LJU": "Ljubliana", "LTN": "London Luton", "EXT": "Exeter", "TGD":"Podgorica",
        "BOD": "Bordeaux","MMX": "Malmö, Schweden","ALC": "Alicante","BBU": "Bukarest", "PSA": "Pisa, Italien","CMF": "Chambéry","OXF": "Oxford","PVK": "Preveza/Lefkada",
        "PTY": "Panama-Stadt","BQH": "London Biggin","VXO": "Växjö","BLL": "Billund","AYT": "Antalya","ADB": "Izmir, Türkei","VRN": "Verona, Italien","MBX": "Maribor",
        "OST": "Ostende","CAT": "Catania, Italien","CDT": "Castellón","GHA": "Ghardaïa","BIA": "Bastia","BOH": "Bournemouth","LIN": "Mailand Linate",
        "LBA": "Leeds Bradford","CEG": "Chester/Hawarden", "GRQ": "Groningen","LYS": "Lyon","GDN": "Danzig, Polen","NWI": "Norwich",
        "NRN": "Weeze","LBC": "Lübeck","XRY": "Jerez de la Fronter","BFS": "Belfast","EIN": "Eindhoven","TLL": "Tallinn", "FAO":"Faro",
        "RIX": "Riga","SUF": "Lamezia Terme","TRN": "Turin","DLM": "Dalaman","CFU": "Korfu","PEG": "Perugia", "FAB":"Farnborough","LEN": "León",
        # NORDAMERIKA
        "JFK": "New York City", "EWR": "Newark", "LGA": "New York City","LAX": "Los Angeles", "ORD": "Chicago", "ATL": "Atlanta", "MIA": "Miami",
        "SFO": "San Francisco", "DFW": "Dallas/Fort Worth", "DEN": "Denver","SEA": "Seattle", "BOS": "Boston", "PHL": "Philadelphia", "IAD": "Washington D.C.",
        "CLT": "Charlotte", "PHX": "Phoenix", "DTW": "Detroit", "MCO": "Orlando","YYZ": "Toronto", "YVR": "Vancouver", "YUL": "Montreal","MEX": "Mexiko-Stadt", "CUN": "Cancún", "SAN": "San Diego, USA",
        # ASIEN & MITTLERER OSTEN
        "DXB": "Dubai", "AUH": "Abu Dhabi", "DOH": "Doha", "RUH": "Riad","PEK": "Peking", "PVG": "Shanghai", "CAN": "Guangzhou", "CTU": "Chengdu",
        "HKG": "Hongkong", "TPE": "Taipei", "NRT": "Tokio", "HND": "Tokio","ICN": "Seoul", "SIN": "Singapur", "BKK": "Bangkok", "HKT": "Phuket",
        "DEL": "Neu-Delhi", "BOM": "Mumbai", "KUL": "Kuala Lumpur", "CGK": "Jakarta","SGN": "Ho-Chi-Minh-Stadt", "MNL": "Manila", "JED": "Dschidda",
        "KHI": "Karatschi", "AMM": "Amman", "RMF":"Marsa Alam","SKD": "Samarkand", "URC": "Ürümqi, China","MIR": "Monastir","BJA": "Bejaia","DJE": "Djerba","HRG": "Hurghada",
        "ALG": "Algier","GYD": "Baku","BAH": "Manama","HYD": "Hyderabad","MAA": "Chennai (Madras)",
        # AFRIKA
        "JNB": "Johannesburg", "CPT": "Kapstadt", "CAI": "Kairo", "CMN": "Casablanca","NBO": "Nairobi", "LOS": "Lagos", "TUN": "Tunis", "ADD": "Addis Abeba",
        "MRU": "Mauritius", "SEZ": "Seychellen","PNR": "Pointe-Noire, Republik Kongo",
        # SÜDAMERIKA
        "GRU": "São Paulo", "GIG": "Rio de Janeiro", "EZE": "Buenos Aires","SCL": "Santiago", "LIM": "Lima", "BOG": "Bogotá", "UIO": "Quito","CCS": "Caracas",
        # AUSTRALIEN/OZEANIEN
        "SYD": "Sydney", "MEL": "Melbourne", "BNE": "Brisbane", "AKL": "Auckland","CHC": "Christchurch", "PER": "Perth",
    }

    # Den Code in Grossbuchstaben umwandeln
    code_gross = code.upper().strip()
    stadt = datenbank.get(code_gross)

    if stadt:
        return stadt
    else:
        return code

main()
