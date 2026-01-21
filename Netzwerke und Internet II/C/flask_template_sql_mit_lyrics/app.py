from flask import Flask, render_template, request
import sqlite3
import requests
from bs4 import BeautifulSoup
import urllib3

# This line suppresses the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

def scrape_azlyrics(artist, song):
    # Format names: remove spaces and non-alphanumeric characters
    artist = "".join(filter(str.isalnum, artist.lower()))
    song = "".join(filter(str.isalnum, song.lower()))
    
    url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"
    
    # Using a User-Agent is highly recommended to avoid 403 Forbidden errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        # verify=False ignores SSL certificate errors
        response = requests.get(url, headers=headers, verify=False)
        
        if response.status_code != 200:
            return f"Error: Received status code {response.status_code}. Check artist/song spelling."

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # AZLyrics usually places the lyrics in the first div that has NO class and NO id
        # but is located inside the 'main-page' container.
        all_divs = soup.find_all("div", class_=None, id=None)
        for div in all_divs:
            text = div.get_text()
            if len(text) > 100:  # Lyrics are usually the longest text block without a class
                return text.strip()
        
        return "Lyrics div not found."

    except Exception as e:
        return f"Error: {e}"

def get_db_connection():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        # wir erhalten das Genre aus dem Formular
        genre = request.form.get('genre', '').strip()
        # prüfen, ob das Genre nicht leer ist
        if genre:
            # wir erhalten eine Verbindung zur Datenbank
            conn = get_db_connection()
            
            query  = "SELECT artists.Name AS artist, tracks.Name AS title "
            query += "FROM tracks, genres, albums, artists "
            query += "WHERE tracks.GenreId = genres.GenreId "
            query += "AND tracks.AlbumId = albums.AlbumId "
            query += "AND albums.ArtistId = artists.ArtistId "
            query += "AND (LOWER(genres.Name) LIKE LOWER('%" + genre + "%') "
            query += "OR LOWER(artists.Name) LIKE LOWER('%" + genre + "%'))"
            
            results = conn.execute(query).fetchall()
            conn.close()
    return render_template('index.html', results=results)

@app.route('/lyrics')
def lyrics():
    artist = request.args.get('artist')
    title = request.args.get('title')
    if not artist or not title:
        return "Missing artist or title", 400
    lyrics_text = scrape_azlyrics(artist, title)
    return render_template('lyrics.html', artist=artist, title=title, lyrics=lyrics_text)

if __name__ == '__main__':
    app.run(debug=True, port=8086, use_reloader=False)

