import sqlite3

# Connessione al database
conn = sqlite3.connect('prova.db')
cursor = conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS  prova (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               geo TEXT,
               TIME_PERIOD TEXT,
               OBS_VALUE FLOAT,
               species TEXT
               )

''')


conn.commit()
conn.close()