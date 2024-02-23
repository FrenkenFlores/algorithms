import sqlite3
genre = input()
con = sqlite3.connect(database="music_db.sqlite")
cur = con.cursor()
m_list = cur.execute(
    '''
    SELECT DISTINCT
        Album.Title
    FROM Album
    INNER JOIN Track
    WHERE Track.AlbumId == Album.AlbumId AND Track.GenreId == (SELECT Genre.GenreId from Genre WHERE Genre.Name == ?)
    ORDER BY Album.ArtistId, Album.Title
    ''',
    (genre,)
).fetchall()
for e in m_list:
    print(*e)
con.close()
