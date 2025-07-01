import pandas as pd
import requests
import os
from io import StringIO
import sqlite3

# URL dei dataset
occupazione_url = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/fish_ld_it?format=SDMX-CSV'

# importanza_url = 'https://raw.githubusercontent.com/AlbertoPuggioniITS/dataset/main/Importanza-economica-del-settore-della-pesca-per-regione.csv'
# produttivita_url = 'https://raw.githubusercontent.com/AlbertoPuggioniITS/dataset/main/Produttivita-del-settore-della-pesca-per-regione.csv'

curr_dirr = os.getcwd()
csv_dir = os.path.join(curr_dirr,'csv')

def import_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content, sep=',')
        df.columns = [col.replace('�', 'à') for col in df.columns]
        return df
    else:
        print(f"Errore nell'importazione dei dati da {url}")
        return None
    
def save_df_local(df, filename):
    os.makedirs(csv_dir, exist_ok=True)
    path = os.path.join(csv_dir, filename)
    df.to_csv(path, index=False, encoding='utf-8')
    print(f"DataFrame salvato in {path}")
    

df_occupazione = import_data(occupazione_url)

save_df_local(df_occupazione,'prova.csv')

df_occupazione = df_occupazione.rename(columns={"LAST UPDATE":"LAST_UPDATE"})

# Funzione per normalizzare i dati mancanti tramite interpolazione
def interpolate_missing_data(df, columns):
    for col in columns:
        df[col] = df[col].interpolate(method='linear')
    return df

interpolate_missing_data(df_occupazione,['OBS_VALUE'])

#connessione al db 
conn = sqlite3.connect('prova.db')
cursor = conn.cursor()

# Inserimento dei dati nelle tabelle
for _, row in df_occupazione.iterrows():
    cursor.execute('INSERT INTO prova (geo, TIME_PERIOD, OBS_VALUE,species) VALUES (?, ?, ?, ?)',
                   (row['geo'], row['TIME_PERIOD'],row['OBS_VALUE'],row['species']))
    
# per controllare se i dati sono stati inseriti correttamente
#     cursor.execute("SELECT * FROM prova LIMIT 10")
# for row in cursor.fetchall():
#     print(row)
    
conn.commit()
conn.close()





