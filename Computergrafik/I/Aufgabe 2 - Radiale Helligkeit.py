import sys
import pkgutil
import subprocess

def main():
    # das hier managt nur den import der bibliotheken
    importiere_pakete() 
    
    bitmap_daten_rgb = []
    for y in range(100):
        zeile = []
        for x in range(100):
            distanz_zur_mitte = ((x-50)**2 + (y-50)**2)**0.5
            farbton = (distanz_zur_mitte / 100) * 255
            F = [farbton,farbton,farbton] 
            zeile.append(F)
        bitmap_daten_rgb.append(zeile)
    
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

