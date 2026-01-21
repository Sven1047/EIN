from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    noresults = "false"
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
            query += "AND LOWER(genres.Name) LIKE LOWER('%" + genre + "%')"
            query += "OR LOWER(artists.Name) LIKE LOWER('%" + genre + "%')"
            
            results = conn.execute(query).fetchall()
            conn.close()

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port=8086, use_reloader=False)

