from fastapi import FastAPI
from typing import Optional
import sqlite3
import pandas as pd

app = FastAPI(
    title="API di prova su DB generato",
    version="1.0.0",
)

def query_db(query: str, params: tuple = ()):
    conn = sqlite3.connect('prova.db')
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

@app.get("/values_between")
def getValuesBetweenIds(da_id: Optional[int] = None, a_id: Optional[int] = None):
    query = "SELECT * FROM prova"
    params = []
    if da_id and a_id:
        query += " WHERE id BETWEEN ? AND ?"
        params.extend([da_id, a_id])
    df = query_db(query, tuple(params))
    return df.to_dict(orient='records')

@app.get("/specie")
def getValuesFromSpecie(specie: Optional[str] = None):
    query = "SELECT * FROM prova"
    params = []
    if specie:
        query += " WHERE species = ?"
        params.extend([specie])
    df = query_db(query, tuple(params))
    return df.to_dict(orient='records')


"""
@app.get("/produttivita_totale_aree")
def get_produttivita_totale_aree(da_anno: Optional[int] = None, a_anno: Optional[int] = None):
    query = "SELECT * FROM produttivita_totale_aree"
    params = []
    if da_anno and a_anno:
        query += " WHERE anno BETWEEN ? AND ?"
        params.extend([da_anno, a_anno])
    df = query_db(query, tuple(params))
    return df.to_dict(orient='records')
"""
