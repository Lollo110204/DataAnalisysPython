import sqlite3

# Connessione al database
conn = sqlite3.connect('prova_esame.db')
cursor = conn.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS  prova (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               geo TEXT,
               TIME_PERIOD INT,
               OBS_VALUE FLOAT,
               species TEXT
               )

''')

# Crea un indice su TIME_PERIOD per velocizzare le query che lo usano come filtro
cursor.execute('CREATE INDEX IF NOT EXISTS idx_time_period ON prova (TIME_PERIOD)')


conn.commit()
conn.close()