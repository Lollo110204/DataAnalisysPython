from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pandas as pd
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)
    
    from app.models import Pokemon  # Import dopo db.init_app
    from .views import main
    from .api import api
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')
    
    with app.app_context():
        db.create_all()
        importa_pokemon(Pokemon)  # Passo Pokemon come argomento
    return app

def importa_pokemon(Pokemon):  # Accetta Pokemon come argomento
    if Pokemon.query.first():
        print("✅ Pokémon già presenti. Importazione saltata.")
        return

    print("📦 Importazione Pokémon...")
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'Pokemon.csv')
    df = pd.read_csv(file_path)

    # Adatto i nomi delle colonne al CSV
    df = df.dropna(subset=["name", "type1"])
    df["type2"] = df["type2"].fillna("Unknown")
    df = df.drop_duplicates(subset=["number"])

    cols_int = ["number", "total", "hp", "attack", "defense"]
    for col in cols_int:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=cols_int)

    for _, row in df.iterrows():
        p = Pokemon(
            id=int(row["number"]),
            name=row["name"],
            type1=row["type1"],
            type2=row["type2"] if pd.notna(row["type2"]) else None,
            total=int(row["total"]),
            hp=int(row["hp"]),
            attack=int(row["attack"]),
            defense=int(row["defense"]),
            speed=int(row["speed"]) if pd.notna(row["speed"]) else None,
            generation=int(row["generation"]) if pd.notna(row["generation"]) else None,
            legendary=bool(row["legendary"]) if pd.notna(row["legendary"]) else False
        )
        db.session.add(p)

    db.session.commit()
    print(f"✅ Importati {len(df)} Pokémon.")