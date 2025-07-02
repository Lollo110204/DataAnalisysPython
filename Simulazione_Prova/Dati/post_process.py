import sqlite3
import pandas as pd

conn = sqlite3.connect("prova.db")


# Funzione per interpolare i dati mancanti
def interpoazione_dati_mancanti(df,columns):
        for col in columns:
            df[col] = df[col].interpolate(method='linear')
        return df

# Interpolazione dei dati mancanti

for table, column in [('prova','OBS_VALUE'),
                       ('prova_calculate_series','media_OBS_VALUE_species')]:
      df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
      df = interpoazione_dati_mancanti(df,[column])
      df.to_sql(table,conn,if_exists='replace',index=False)
    

conn.close()