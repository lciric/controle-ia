"""CL9 : la borne de 12 000 caractères par fiche servie — où elle mord, ce qu'elle fait (refus, troncature ?), ce que
voient les juges. Usage : python3 -B sonde_fiche_12000.py ARBRE DOSSIER"""
import copy, json, os, sys
A, D = sys.argv[1], sys.argv[2]
sys.path.insert(0, A)
from pole import ideation as idn
os.makedirs(D, exist_ok=False)
res = {}
BASE = {"nom": "Sobre fort", "type": "question", "enonce": "e",
        "loi_predictive": {"espace_instances": "familles", "prediction": "p", "signe": "-", "metrique": "m"},
        "perte_traduction": "p", "questions_servies": ["Q4"],
        "avantage": {"source": "programme", "texte": "t", "incopiable_parce_que": "c"},
        "originalite": {"niveau": "transposition", "texte": "r"},
        "demande_organisme": {"nature": "ajout", "texte": "g"},
        "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"}, "piege": "a", "cosmetique_si": "p",
        "anteriorite": [{"reference": "réf", "statut": "RAPPORTE"}]}
CHEMINS = [("enonce",), ("loi_predictive", "espace_instances"), ("loi_predictive", "prediction"), ("loi_predictive", "metrique"),
           ("perte_traduction",), ("avantage", "texte"), ("avantage", "incopiable_parce_que"), ("originalite", "texte"),
           ("demande_organisme", "texte"), ("cout", "ordre_de_grandeur"), ("piege",), ("cosmetique_si",)]


def remplir(k, motif="m", nq=1, na=1):
    f = copy.deepcopy(BASE)
    for c in CHEMINS:
        d = f
        for x in c[:-1]:
            d = d[x]
        d[c[-1]] = (motif * k)[:k]
    f["questions_servies"] = ["Q" + str(i) for i in range(nq)]
    f["anteriorite"] = [{"reference": "r" * 200, "statut": "RAPPORTE"}] * na
    return f


def essai(f):
    try:
        v = idn.valider_fiche_ideation(f, "a", 1)
        return {"accepte": True, "taille_servie": idn.taille_servie(v),
                "identique_au_brut_hors_champs_internes": idn.vue_servie(v) == f}
    except idn.FicheIdeationInvalide as e:
        return {"accepte": False, "motif": str(e)}

# 1. seuil exact : 12 textes de k caractères ; contenu « utile » (somme des textes) au seuil
for k in (800, 900, 950, 960, 1000, 1500, 3000):
    f = remplir(k)
    res[f"12 textes de {k}"] = dict(essai(f), contenu_textes=12 * k,
                                    taille_servie_brute=len(json.dumps([f], ensure_ascii=False, indent=1)))
# 2. fiche « réelle » : 3 champs de 3 000 (le maximum par champ), le reste court
f = copy.deepcopy(BASE); f["enonce"] = f["perte_traduction"] = f["piege"] = "y" * 3000
res["3 champs de 3 000"] = essai(f)
f["cosmetique_si"] = "y" * 3000
res["4 champs de 3 000"] = essai(f)
# 3. échappements : 6 000 caractères de texte avec guillemets et retours à la ligne
f = copy.deepcopy(BASE); f["enonce"] = ('a "b"\n' * 500)[:3000]; f["piege"] = ('a "b"\n' * 500)[:3000]
res["6 000 caractères dont guillemets et retours"] = dict(essai(f), contenu_textes=6000)
# 4. borne au seuil : on cherche la plus grande fiche acceptée et la plus petite refusée (une seule dimension)
lo, hi = 0, 3000
while hi - lo > 1:
    mid = (lo + hi) // 2
    (lo, hi) = (mid, hi) if essai(remplir(mid))["accepte"] else (lo, mid)
res["seuil 12 textes (1 question, 1 antériorité de 200)"] = {"k_max_accepte": lo, "taille_servie": idn.taille_servie(remplir(lo)),
                                                              "k+1": essai(remplir(lo + 1))}
# 5. un témoin de plus de 12 000 caractères : la course est-elle refusée, et quand ?
tem = {"temoins": [{"fiche": dict(BASE), "attendu": "eligible", "classe": "vrai"},
                   {"fiche": dict(remplir(1100), nom="Verbeux vide"), "attendu": "ineligible", "note_max": {"falsifiabilite": 1},
                    "classe": "faux_falsifiabilite"},
                   {"fiche": dict(BASE, nom="Assuré occupé", originalite={"niveau": "inedite", "texte": "jamais vu"}),
                    "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
                   {"fiche": dict(BASE, nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]}
pt = os.path.join(D, "temoins.json"); json.dump(tem, open(pt, "w", encoding="utf-8"), ensure_ascii=False)
lb = os.path.join(D, "lb.json"); idn.construire_liste_blanche([pt], lb)
try:
    idn.charger_temoins(pt, idn.charger_liste_blanche(lb))
    res["temoin_verbeux_12x1100"] = "accepté"
except Exception as e:  # noqa: BLE001
    res["temoin_verbeux_12x1100"] = type(e).__name__ + " : " + str(e)[:300]
res["temoin_verbeux_taille_servie"] = idn.taille_servie(remplir(1100))
# 6. ce que dit la consigne aux proposeurs
c = idn.consigne_proposeur([("p", "x", "h")], 8, "Q ?")
i = c.find("Bornes")
res["consigne_bornes"] = c[i:i + 300]
res["base_fiche_maximale_textes"] = {"k": len(idn.fiche_maximale()["enonce"]), "taille": idn.taille_servie(idn.fiche_maximale())}
print(json.dumps(res, ensure_ascii=False, indent=1))
