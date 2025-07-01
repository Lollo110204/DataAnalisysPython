import sqlite3
import pandas as pd



def query_db(query: str, params: tuple = ()):
    conn = sqlite3.connect('prova.db')
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


#connessione al db
conn = sqlite3.connect('prova.db')
cursor = conn.cursor()


cursor.execute('''

    CREATE TABLE IF NOT EXISTS  prova_calculate_series (
        TIME_PERIOD TEXT,
        species TEXT,
        media_OBS_VALUE_species FLOAT,
        PRIMARY KEY (TIME_PERIOD, species)
               )
''')




# Query per ottenere i dati necessari
query_prova = "SELECT * FROM prova"

df_occupazione = query_db(query_prova)

# Calcolo della produttività totale per area geografica
prova_calculate_series  = df_occupazione.groupby(['species','TIME_PERIOD'])['OBS_VALUE'].mean().reset_index()

# Inserimento dei dati calcolati nel database
prova_calculate_series.to_sql('prova_calculate_series',conn,if_exists='replace',index=False)


conn.close()