import sqlite3


def get_result(name):
    genre = "боевик"
    duration = 90
    con = sqlite3.connect(database=name)
    cur = con.cursor()
    cur.execute(
        '''
        DELETE FROM films
        WHERE films.id IN (
            SELECT films.id FROM films
            INNER JOIN genres
            WHERE films.genre == (SELECT genres.id FROM genres WHERE genres.title == ?) AND films.duration >= ?
        )
        ''',
        (genre, duration)
    )
    con.commit()
    con.close()
