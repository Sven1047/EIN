import pkgutil
import subprocess
import sys
        

pakete = ['yfinance']

for i, paket_name in enumerate(pakete):
    if pkgutil.find_loader(paket_name):
        print(f"'{paket_name}' ist bereits geladen. Überspringe Installation.")
        continue
    
    print(f"Versuche Installation von '{paket_name}'...")
    try:
        process = subprocess.run(
            [sys.executable, "-m", "pip", "install", paket_name],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Installation von '{paket_name}' erfolgreich abgeschlossen.")
    except subprocess.CalledProcessError as e:
        raise ImportError(f"Installation von '{paket_name}' schlug fehl (Rückgabecode {e.returncode}).")

    if pkgutil.find_loader(paket_name):
        print(f"✔️ '{paket_name}' erfolgreich installiert und geladen.")
    else:
        if paket_name == 'PyOpenGL' and i < len(pakete) - 1 and pakete[i+1] == 'PyOpenGL_accelerate':
            print(f"⚠️ Warnung: '{paket_name}' konnte nach der Installation nicht sofort geladen werden. Setze fort mit '{pakete[i+1]}'.")
            continue # Springe zur Installation von PyOpenGL_accelerate
        
