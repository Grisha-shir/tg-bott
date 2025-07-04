import sqlite3
from idlelib.colorizer import prog_group_name_to_tag

conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    genre TEXT,
    years INTEGER,
    love_music TEXT,
    artist TEXT
)
''')
conn.commit()

def add_user(user_id, genre, years, love_music, artist):
    cursor.execute('''
            INSERT INTO users (id, genre, years, love_music, artist)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                genre = excluded.genre,
                years = excluded.years,
                love_music = excluded.love_music,
                artist = excluded.artist
        ''', (user_id, genre, years, love_music, artist))
    conn.commit()

def show_table():
    res = cursor.execute('''
        SELECT * FROM users 
    ''')
    return res.fetchall()

print(show_table())










