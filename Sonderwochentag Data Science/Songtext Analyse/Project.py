from gtts import gTTS
import os
import csv
import tkinter as tk
import zipfile


def speech(text, lang):

    speech = gTTS(text = text, lang = lang, slow=False)
    speech.save(r"C:\Users\sveng\Downloads\speech.mp3")
    os.startfile(r"C:\Users\sveng\Downloads\speech.mp3")

def csv_reader(file_name):
    header = []
    data = []
    try:
        with open(file_name, mode='r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)
            try:
                header = next(csv_reader)
            except StopIteration:
                print(f"Warning: The file '{file_name}' is empty.")
                return [], []
            for row in csv_reader:
                data.append(row)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

    return data

def text(artist, songname):
    data = csv_reader(artist)
    text = ""
    for i in range(0,len(data)):
        if songname in data[i][2]:
            text = data[i][6]

    speech(text, 'en')

def read_csv_simple(file_obj):
    header = []
    data = []
    csv_reader = csv.reader(file_obj)
    try:
        header = next(csv_reader)
    except StopIteration:
        return [], []
    for row in csv_reader:
        data.append(row)
    return header, data

def load_artists_from_zip(zip_path):
    artists = {}

    with zipfile.ZipFile(zip_path, "r") as z:
        # Alle CSV-Dateien finden
        csv_files = [name for name in z.namelist() if name.lower().endswith(".csv")]

        for csv_file in csv_files:
            artist = os.path.splitext(os.path.basename(csv_file))[0]

            with z.open(csv_file) as file:
                header, data = read_csv_simple(
                    (line.decode("utf-8", errors="ignore") for line in file)
                )

            if not header:
                continue

            # Songtitel ist IMMER die 3. Spalte (Index 2)
            song_col_index = 2
            songs = [row[song_col_index] for row in data if len(row) > song_col_index]

            artists[artist] = songs

    return artists



def waehle_artist_und_song(artists_songs):
    def lade_songs(event):
        nonlocal artist_selected
        sel = artist_listbox.curselection()
        if not sel:
            return
        artist_selected = artist_listbox.get(sel)

        song_listbox.delete(0, tk.END)
        for s in artists_songs[artist_selected]:
            song_listbox.insert(tk.END, s)

    def song_ausgewaehlt(event):
        nonlocal song_selected
        sel = song_listbox.curselection()
        if sel:
            song_selected = song_listbox.get(sel)

    def fertig():
        root.destroy()

    artist_selected = None
    song_selected = None

    root = tk.Tk()
    root.title("Artist → Songs auswählen")

    tk.Label(root, text="Artists:").pack(anchor="w")
    artist_listbox = tk.Listbox(root, height=8, width=8)
    artist_listbox.pack(fill="x")
    artist_listbox.bind("<<ListboxSelect>>", lade_songs)

    for artist in artists_songs.keys():
        artist_listbox.insert(tk.END, artist)

    tk.Label(root, text="Songs:").pack(anchor="w")
    song_listbox = tk.Listbox(root, height=10, width=8)
    song_listbox.pack(fill="x")
    song_listbox.bind("<<ListboxSelect>>", song_ausgewaehlt)

    tk.Button(root, text="Auswahl bestätigen", command=fertig).pack(pady=10)

    root.mainloop()
    return artist_selected, song_selected


def main():
    zip_path = "archive.zip"

    artists_songs = load_artists_from_zip(zip_path)

    artist, song = waehle_artist_und_song(artists_songs)

    return artist, song

artist, song = main()

artist = artist + ".csv"

text(artist, song)
