from flask import Blueprint, jsonify
from .models import PartecipazioneLavoro, Pokemon
from collections import Counter, defaultdict

api = Blueprint('api', __name__)

@api.route('/serie')
def get_serie():
    dati = PartecipazioneLavoro.query.order_by(PartecipazioneLavoro.anno).all()
    anni = []
    valori = []

    for record in dati:
        anni.append(record.anno)
        valori.append(record.valore)

    return jsonify({"anni": anni, "valori": valori})

@api.route('/all')
def get_all():
    dati = PartecipazioneLavoro.query.all()
    records = [{"anno": d.anno, "regione": d.regione, "valore": d.valore} for d in dati]
    return jsonify(records)

@api.route('/pokemon/type1')
def pokemon_type1():
    # Conta i Pokémon per ogni tipo1
    tipi = [p.type1 for p in Pokemon.query.all()]
    counter = Counter(tipi)
    return jsonify({"labels": list(counter.keys()), "counts": list(counter.values())})

@api.route('/pokemon/hp')
def pokemon_hp():
    # Restituisce nome e hp di ogni Pokémon
    pokemons = Pokemon.query.order_by(Pokemon.hp.desc()).all()
    labels = [p.name for p in pokemons]
    hps = [p.hp for p in pokemons]
    return jsonify({"labels": labels, "hps": hps})

@api.route('/pokemon/hp_media_type1')
def pokemon_hp_media_type1():
    hp_sum = defaultdict(int)
    hp_count = defaultdict(int)
    for p in Pokemon.query.all():
        if p.type1:
            hp_sum[p.type1] += p.hp
            hp_count[p.type1] += 1
    # Calcolo la media e ordino per media decrescente
    stats = [(t, hp_sum[t]/hp_count[t]) for t in hp_sum.keys()]
    stats.sort(key=lambda x: x[1], reverse=True)
    labels = [t for t, _ in stats]
    media = [m for _, m in stats]
    return jsonify({"labels": labels, "media": media})


@api.route('/pokemon/attack_media_type1')
def pokemon_attack_media_type1():
    attack_sum = defaultdict(int)
    attack_count = defaultdict(int)
    for p in Pokemon.query.all():
        if p.type1:
            attack_sum[p.type1] += p.attack
            attack_count[p.type1] += 1
    # Calcolo la media e ordino per media decrescente
    stats = [(t, attack_sum[t]/attack_count[t]) for t in attack_sum.keys()]
    stats.sort(key=lambda x: x[1], reverse=True)
    labels = [t for t, _ in stats]
    media = [m for _, m in stats]
    return jsonify({"labels": labels, "media": media})