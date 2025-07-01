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

@api.route('/pokemon/legendary/top_stats')
def legendary_top_stats():
    from .models import Pokemon
    legendaries = [p for p in Pokemon.query.all() if hasattr(p, 'legendary') and (str(p.legendary).lower() == 'true' or str(p.legendary) == 'TRUE' or str(p.legendary) == 'True' or p.name.lower() in ['mewtwo','mew','articuno','zapdos','moltres','raikou','entei','suicune','lugia','ho-oh','regirock','regice','registeel','latias','latios','kyogre','groudon','rayquaza','jirachi','deoxys','uxie','mesprit','azelf','dialga','palkia','heatran','regigigas','giratina','cresselia','phione','manaphy','darkrai','shaymin','arceus','victini','cobalion','terrakion','virizion','tornadus','thundurus','reshiram','zekrom','landorus','kyurem','keldeo','meloetta','genesect','xerneas','yveltal','zygarde','diancie','hoopa','volcanion','tapu koko','tapu lele','tapu bulu','tapu fini','cosmog','cosmoem','solgaleo','lunala','nihilego','buzzwole','pheromosa','xurkitree','celesteela','kartana','guzzlord','necrozma','magearna','marshadow','poipole','naganadel','stakataka','blacephalon','zeraora','meltan','melmetal','zacian','zamazenta','eternatus','kubfu','urshifu','zarude','regieleki','regidrago','glastrier','spectrier','calyrex'])]
    if not legendaries:
        return jsonify({"max_attack": None, "max_defense": None})
    max_attack = max(legendaries, key=lambda p: p.attack)
    max_defense = max(legendaries, key=lambda p: p.defense)
    return jsonify({
        "max_attack": {"name": max_attack.name, "attack": max_attack.attack, "type1": max_attack.type1, "type2": max_attack.type2},
        "max_defense": {"name": max_defense.name, "defense": max_defense.defense, "type1": max_defense.type1, "type2": max_defense.type2}
    })

@api.route('/pokemon/legendary/type1_distribution')
def legendary_type1_distribution():
    from .models import Pokemon
    from collections import Counter
    legendaries = [p for p in Pokemon.query.all() if hasattr(p, 'legendary') and (str(p.legendary).lower() == 'true' or str(p.legendary) == 'TRUE' or str(p.legendary) == 'True' or p.name.lower() in ['mewtwo','mew','articuno','zapdos','moltres','raikou','entei','suicune','lugia','ho-oh','regirock','regice','registeel','latias','latios','kyogre','groudon','rayquaza','jirachi','deoxys','uxie','mesprit','azelf','dialga','palkia','heatran','regigigas','giratina','cresselia','phione','manaphy','darkrai','shaymin','arceus','victini','cobalion','terrakion','virizion','tornadus','thundurus','reshiram','zekrom','landorus','kyurem','keldeo','meloetta','genesect','xerneas','yveltal','zygarde','diancie','hoopa','volcanion','tapu koko','tapu lele','tapu bulu','tapu fini','cosmog','cosmoem','solgaleo','lunala','nihilego','buzzwole','pheromosa','xurkitree','celesteela','kartana','guzzlord','necrozma','magearna','marshadow','poipole','naganadel','stakataka','blacephalon','zeraora','meltan','melmetal','zacian','zamazenta','eternatus','kubfu','urshifu','zarude','regieleki','regidrago','glastrier','spectrier','calyrex'])]
    tipi = [p.type1 for p in legendaries]
    counter = Counter(tipi)
    return jsonify({"labels": list(counter.keys()), "counts": list(counter.values())})
