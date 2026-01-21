import pkgutil
import subprocess
import sys
        
def install_textblob():
    required_version = "textblob==0.15.2"
    
    try:
        print(f"--- Starting installation of {required_version} ---")
        install_command = [sys.executable, "-m", "pip", "install", required_version]
        subprocess.check_call(install_command)
        print(f"\n✅ Successfully installed {required_version}.")
        print("\n--- Starting TextBlob corpus data download ---")
        download_command = [sys.executable, "-m", "textblob.download_corpora"]
        subprocess.check_call(download_command)
        print("\n✅ Successfully downloaded all necessary corpora.")

    except subprocess.CalledProcessError as e:
        print(f"\n🚨 ERROR: Installation or corpus download failed.")
        print(f"The command '{' '.join(e.cmd)}' returned an error code: {e.returncode}.")
        print("Please check your environment setup.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


pakete = ['textblob', 'textblob_de', 'SpeechRecognition', 'PyAudio', 'vaderSentiment']

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
        
install_textblob()

import nltk
nltk.download('punkt_tab')