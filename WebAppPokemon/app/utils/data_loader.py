import pandas as pd
from .. import create_app, db
from ..models import PartecipazioneLavoro

app = create_app()
with app.app_context():
    # Cancella eventuali dati preesistenti
    PartecipazioneLavoro.query.delete()
    db.session.commit()

    # Set di dati di esempio: anni 2018–2022 per tre regioni
    records = [
        {"anno": 2018, "regione": "Piemonte", "valore": 64.0},
        {"anno": 2019, "regione": "Piemonte", "valore": 65.2},
        {"anno": 2020, "regione": "Piemonte", "valore": 63.8},
        {"anno": 2021, "regione": "Piemonte", "valore": 64.5},
        {"anno": 2022, "regione": "Piemonte", "valore": 65.0},

        {"anno": 2018, "regione": "Lombardia", "valore": 68.1},
        {"anno": 2019, "regione": "Lombardia", "valore": 68.7},
        {"anno": 2020, "regione": "Lombardia", "valore": 67.0},
        {"anno": 2021, "regione": "Lombardia", "valore": 67.8},
        {"anno": 2022, "regione": "Lombardia", "valore": 68.2},

        {"anno": 2018, "regione": "Lazio", "valore": 62.5},
        {"anno": 2019, "regione": "Lazio", "valore": 63.0},
        {"anno": 2020, "regione": "Lazio", "valore": 61.9},
        {"anno": 2021, "regione": "Lazio", "valore": 62.7},
        {"anno": 2022, "regione": "Lazio", "valore": 63.3},
    ]

    # Inserisci nel DB
    for r in records:
        db.session.add(PartecipazioneLavoro(**r))
    db.session.commit()

    print(f"✅ Inseriti {len(records)} record di prova.")