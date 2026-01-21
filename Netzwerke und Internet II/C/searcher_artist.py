import sqlite3

artist = input("Welchen Artist suchst du? ")

conn = sqlite3.connect('chinook.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

query  = "SELECT artists.Name AS artist, tracks.Name AS title "
query += "FROM tracks, genres, albums, artists "
query += "WHERE tracks.GenreId = genres.GenreId "
query += "AND tracks.AlbumId = albums.AlbumId "
query += "AND albums.ArtistId = artists.ArtistId "
query += "AND LOWER(artists.Name) LIKE LOWER('%" + artist + "%') "

print(query)

# Ausführung
results = conn.execute(query).fetchall()
conn.close()

# Ergebnisse ausgeben
if results:
    print(f"Gefundene Songs für Genre '{artist}':\n")
for row in results:
    print(f"{row['artist']} - {row['title']}")
else:
    print(f"Keine Einträge für '{artist}' gefunden.")

conn.close()
