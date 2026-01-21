import sys
import pkgutil
import subprocess

def main():
    # das hier managt nur den import der bibliotheken
    importiere_pakete() 
    
    W = [255, 255, 255]
    S = [0, 0, 0]      

    bitmap_daten_rgb = [
        [S, S, S, S, S, S, S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S, S, S, S, S, S, S],
        [S, S, W, W, W, W, W, W, W, W, W, W, S, S],
        [S, S, W, S, S, W, W, W, W, S, S, W, S, S],
        [S, S, W, S, S, W, W, W, W, S, S, W, S, S],
        [S, S, W, W, W, W, W, W, W, W, W, W, S, S],
        [S, S, W, W, W, W, S, S, W, W, W, W, S, S],
        [S, S, W, W, W, W, S, S, W, W, W, W, S, S],
        [S, S, W, W, W, W, W, W, W, W, W, W, S, S],
        [S, S, W, S, W, W, W, W, W, W, S, W, S, S],
        [S, S, W, W, S, S, S, S, S, S, W, W, S, S],
        [S, S, W, W, W, W, W, W, W, W, W, W, S, S],
        [S, S, S, S, S, S, S, S, S, S, S, S, S, S],
        [S, S, S, S, S, S, S, S, S, S, S, S, S, S]
    ]

    """
    Ändere das obige Bild ab - zeichne ein Schachbrettmuster (8x8 Pixel), alternierend Schwarz Weiss
    a) von Hand
    """
    
    bitmap_daten_rgb = [
        [S, W, S, W, S, W, S, W],
        [W, S, W, S, W, S, W, S],
        [S, W, S, W, S, W, S, W],
        [W, S, W, S, W, S, W, S],
        [S, W, S, W, S, W, S, W],
        [W, S, W, S, W, S, W, S],
        [S, W, S, W, S, W, S, W],
        [W, S, W, S, W, S, W, S],
    ]
    
    """
    b) mit einer Schlaufe
    """
    
    bitmap_daten_rgb = []
    for i in range(4):
        
        zeile = []
        zeile.append(S)
        zeile.append(W)
        zeile.append(S)
        zeile.append(W)
        zeile.append(S)
        zeile.append(W)
        zeile.append(S)
        zeile.append(W)
        bitmap_daten_rgb.append(zeile)
        
        zeile = []
        zeile.append(W)
        zeile.append(S)
        zeile.append(W)
        zeile.append(S)
        zeile.append(W)
        zeile.append(S)
        zeile.append(W)
        zeile.append(S)
        bitmap_daten_rgb.append(zeile)
        
    
    """
    c) Zeichne einen weissen Viertelkreis auf Schwarzem Grund - Nutze Pythagoras! Du kannst das Bild auch gerne grösser machen als 8x8 Pixel
    """
    
    bitmap_daten_rgb = []
    for y in range(100):
        zeile = []
        for x in range(100):
            zeile.append(S)
        bitmap_daten_rgb.append(zeile)
    
    for y in range(100):
        for x in range(100):
            if (x*x + y*y)**0.5 < 100:
                bitmap_daten_rgb[x][y]=W
    
    zeichne_die_bitmap(bitmap_daten_rgb)
    
    
    
    
def zeichne_die_bitmap(bitmap_daten_rgb):
    import numpy as np 
    from PIL import Image 
    np_array_rgb = np.array(bitmap_daten_rgb, dtype=np.uint8)
    img = Image.fromarray(np_array_rgb, mode='RGB')

    neue_groesse = (500, 500)
    img_skaliert = img.resize(neue_groesse, resample=Image.NEAREST)

    dateiname = "smiley_kuerzel_rgb.bmp"
    img_skaliert.save(dateiname)
    img_skaliert.show()


def importiere_pakete():
    pakete = ['numpy', 'PIL']
    for paket_name in pakete:
        if pkgutil.find_loader(paket_name):
            continue
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", paket_name],
            stdout=subprocess.PIPE, # Unterdrückt die detaillierte pip-Ausgabe
            stderr=subprocess.PIPE # Leitet Fehler in eine Variable um
        )
        if pkgutil.find_loader(paket_name):
            print(paket_name, "erfolgreich installiert und geladen.")
        else:
            raise ImportError("Installation von", paket_name, "schlug fehl, oder es kann nicht geladen werden.")
main()

