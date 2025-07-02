from fastapi import FastAPI
from typing import Optional
import sqlite3
import pandas as pd

app = FastAPI(
    title="API di prova per allenamento",
    description="Prove di API per allenamento.",
    version="1.0.0",
    contact={
        "name": "Prette Lorenzo",
        "email": "lorenzo.prette@edu.itspiemonte.it",
    }
)

def query_db(query:str,params: tuple = ()):
    conn = sqlite3.connect("prova.db")
    df = pd.read_sql_query(query,conn,params=params)
    conn.close()
    return df


@app.get("/getProva")
def prova_get(da_anno:Optional[int]=None, a_anno:Optional[int]=None):
    query = "SELECT geo,TIME_PERIOD, OBS_VALUE ,species FROM prova "
    params=[]
    if da_anno and a_anno:
        query += "WHERE TIME_PERIOD BETWEEN ? and ?"
        params.extend([da_anno,a_anno])
        df = query_db(query,tuple(params))
        return df.to_dict(orient='records')