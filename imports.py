import pkgutil
import subprocess
import sys

# Verwenden Sie diese Liste, um die spezielle Behandlung von PyOpenGL zu ermöglichen
pakete = ['pygame', 'PyOpenGL', 'PyOpenGL_accelerate']

for i, paket_name in enumerate(pakete):
    # 1. Überspringen, wenn bereits geladen
    if pkgutil.find_loader(paket_name):
        print(f"'{paket_name}' ist bereits geladen. Überspringe Installation.")
        continue

    # 2. Installation versuchen
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
        # Hier könnten Sie die Fehlerausgabe anzeigen, wie im vorherigen Beispiel
        raise ImportError(f"Installation von '{paket_name}' schlug fehl (Rückgabecode {e.returncode}).")

    # 3. Überprüfen, ob das Paket nach der Installation geladen werden kann
    if pkgutil.find_loader(paket_name):
        print(f"✔️ '{paket_name}' erfolgreich installiert und geladen.")
    else:
        # **SPEZIELLE BEHANDLUNG FÜR PYOPENGL**
        # Wenn PyOpenGL nicht sofort geladen werden kann, aber der nächste Schritt der Accelerator ist,
        # fahren wir fort, weil der Import oft erst nach der Installation des Accelerators funktioniert.
        if paket_name == 'PyOpenGL' and i < len(pakete) - 1 and pakete[i+1] == 'PyOpenGL_accelerate':
            print(f"⚠️ Warnung: '{paket_name}' konnte nach der Installation nicht sofort geladen werden. Setze fort mit '{pakete[i+1]}'.")
            continue # Springe zur Installation von PyOpenGL_accelerate