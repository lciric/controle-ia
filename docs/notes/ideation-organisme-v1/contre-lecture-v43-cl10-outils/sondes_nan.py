"""Sondes « valeurs non finies » (contre-lecture CL7) : appels directs, sur l'arbre donné.

Usage : python3 -B sondes_nan.py ARBRE DOSSIER_TEMP
Pour chaque entrée : NaN, +∞, −∞, booléen (et une valeur saine). « refus » = exception levée (type), « ACCEPTÉ » = rendu."""
import importlib.util
import json
import math
import os
import sys
import tempfile

ARBRE, TMP = sys.argv[1], sys.argv[2]
sys.path.insert(0, ARBRE)
from pole import pari_apparie as pa  # noqa: E402
from pole import porte_pace as pp  # noqa: E402
from pole import ideation as idn  # noqa: E402

NAN, INF = float("nan"), float("inf")
MAUVAIS = {"NaN": NAN, "+inf": INF, "-inf": -INF, "True": True}


def essai(f):
    try:
        r = f()
        return "ACCEPTÉ → " + repr(r)[:90]
    except Exception as e:  # noqa: BLE001
        return "refus (" + type(e).__name__ + ")"


lignes = []


def sonde(nom, fabrique, sain):
    res = {k: essai(lambda v=v: fabrique(v)) for k, v in MAUVAIS.items()}
    res["sain"] = essai(lambda: fabrique(sain))
    lignes.append((nom, res))


# --- liste de CL39-09 et § 4 de CL6
sonde("verifier_coefficients(constante)", lambda x: pa.verifier_coefficients({"A": 1}, constante=x), -0.4)
sonde("contraste(constante)", lambda x: pa.contraste({"A": 0.6, "B": 0.4}, {"A": 1, "B": -1}, x), 0.0)
sonde("contraste(coefficient)", lambda x: pa.contraste({"A": 0.6, "B": 0.4}, {"A": x, "B": -1}), 1)
sonde("contraste(part)", lambda x: pa.contraste({"A": x, "B": 0.4}, {"A": 1, "B": -1}), 0.6)
sonde("contraste_plafonne(constante)", lambda x: pa.contraste_plafonne({"A": 0.2}, {"A": 1}, x, 10, 20), 0.0)
sonde("ebh_pondere(log_e)", lambda x: pa.ebh_pondere({"a": 0.0, "b": x, "c": 3.0}, {k: 0.05 / 3 for k in "abc"}, 0.05), 0.0)
sonde("ebh_pondere(alpha)", lambda x: pa.ebh_pondere({"a": 0.0, "b": 0.0}, {"a": 0.45, "b": 0.45}, x), 0.95)


def course(x):
    c = pa.Course(alpha=0.05, essai=True)
    c.entrer("g", ["a"], 0.05)
    c.ajouter_trajectoire("a", [math.log(2), x], unites={1, 2})
    return sorted(c.lire())


sonde("Course.ajouter_trajectoire", course, math.log(3))
sonde("trajectoire_log_sans_remise", lambda x: pa.trajectoire_log_sans_remise([0.1, x, -0.1])[-1], 0.2)
sonde("trajectoire_log_richesse (valeur)", lambda x: pa.trajectoire_log_richesse([0.1, x])[-1], 0.2)
sonde("borne_basse(valeur)", lambda x: pa.borne_basse([0.4, 0.0] * 100 + [x]), 0.0)
sonde("borne_basse(alpha)", lambda x: pa.borne_basse([0.4, 0.0] * 100, alpha=x), 0.05)
sonde("evaluer(alpha)", lambda x: pa.evaluer({"B": [1.0] * 30}, alpha=x)["promue"], 0.05)
sonde("evaluer(m)", lambda x: pa.evaluer({"B": [1.0] * 30}, m=x)["promue"], 1)
sonde("evaluer(valeur de contraste)", lambda x: pa.evaluer({"B": [1.0] * 6 + [x] * 6})["promue"], 1.0)
sonde("evaluer(delta)", lambda x: pa.evaluer({"B": [1.0] * 30}, ecarts_faux_positifs=[0.0] * 30, delta=x)["promue"], 0.05)
sonde("evaluer(écart de garde)", lambda x: pa.evaluer({"B": [1.0] * 30}, ecarts_faux_positifs=[0.0] * 29 + [x], delta=0.05)["promue"], 0.0)
sonde("Course.entrer(alpha_c)", lambda x: pa.Course(alpha=0.05, essai=True).entrer("g", ["a"], x), 0.05)
sonde("Course(alpha)", lambda x: pa.Course(alpha=x, essai=True).alpha, 0.05)
ref, cand = [0] * 40, [1] * 40
sonde("porte PACE : pari_apparie_binaire(delta)",
      lambda x: pp.pari_apparie_binaire(ref, cand, ecarts_faux_positifs=[0.0] * 40, delta=x)["arretee_au_seuil"], 0.05)
sonde("porte PACE : pari_apparie_binaire(alpha)", lambda x: pp.pari_apparie_binaire(ref, cand, alpha=x)["arretee_au_seuil"], 0.05)
sonde("porte PACE : porte_pace(lam)", lambda x: pp.porte_pace(ref, cand, lam=x)["validee"], 0.5)
sonde("porte PACE : porte_pace(budget)", lambda x: pp.porte_pace(ref, cand, budget=x)["validee"], 40)


def comparer_gain(x):
    import random
    s = pp.simuler_suite(random.Random(3), "gain", m=3, n_dev=40)
    s[1]["gain_reel"] = x
    return pp.comparer(s)["bras"]["pari_apparie"]["validations"]


sonde("porte PACE : comparer(gain_reel)", comparer_gain, -0.05)
sonde("porte PACE : simuler_suite(bruit_fp)",
      lambda x: len(pp.simuler_suite(__import__("random").Random(1), "honnete_garde", m=2, bruit_fp=x)), 0.1)

# --- ideation : plafonds et sommes (hors de la liste de CL6)
os.makedirs(TMP, exist_ok=True)
d = tempfile.mkdtemp(dir=TMP)


def ecrire(nom, texte):
    p = os.path.join(d, nom)
    with open(p, "w", encoding="utf-8") as f:
        f.write(texte)
    return p


fiche = {"nom": "Sobre fort", "type": "question", "enonce": "E ?",
         "loi_predictive": {"espace_instances": "x", "prediction": "y", "signe": "-", "metrique": "z"},
         "perte_traduction": "p", "questions_servies": ["Q4"],
         "avantage": {"source": "programme", "texte": "t", "incopiable_parce_que": "c"},
         "originalite": {"niveau": "transposition", "texte": "r"}, "demande_organisme": {"nature": "ajout", "texte": "g"},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "j"}, "piege": "a", "cosmetique_si": "b",
         "anteriorite": []}
p = ecrire("piece.md", "# Pièce\ntexte")
q = ecrire("question.md", "Q ?")
t = ecrire("temoins.json", json.dumps({"temoins": [
    {"fiche": fiche, "attendu": "eligible", "classe": "vrai"},
    {"fiche": dict(fiche, nom="Verbeux vide"), "attendu": "ineligible", "note_max": {"falsifiabilite": 1},
     "classe": "faux_falsifiabilite"},
    {"fiche": dict(fiche, nom="Assuré occupé"), "attendu": "ineligible", "note_max": {"originalite": 1},
     "classe": "faux_anteriorite"},
    {"fiche": dict(fiche, nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]},
    ensure_ascii=False))
lb = os.path.join(d, "lb.json")
idn.construire_liste_blanche([p, q, t], lb)
budgets = {("proposeur_ideation", "claude-opus-5-5"): 5.0, ("proposeur_ideation", "claude-fable-5-1"): 9.3,
           ("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0,
           ("proposeur_ideation", "gemini-argon"): 2.5, ("juge_ideation", "gemini-argon"): 3.5}
base = dict(liste_blanche=lb, question=q, pieces=[p], temoins=t, budgets=budgets, budget_total_usd=40.0,
            budget_externe_usd=11.6, proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
            juges=[("juge-fable", "claude-fable-5-1"), ("juge-opus", "claude-opus-5-5")],
            proposeurs_externes=[("argon", "gemini-argon")], juges_externes=[("argon-j", "gemini-argon")],
            seconde_passe=True, cout_controles_prevu_usd=0.4, cout_controles_externes_prevu_usd=2.5)
sonde("verifier_reglages(budget_controle_bras_usd)",
      lambda x: idn.verifier_reglages(**dict(base, budget_controle_bras_usd=x))["somme_externe"], 0.2)
lignes.append(("verifier_reglages(budget_controle_bras_usd = −5,0) avec total externe 6,0",
               {"−5,0": essai(lambda: idn.verifier_reglages(**dict(base, budget_externe_usd=6.0,
                                                                   budget_controle_bras_usd=-5.0))["somme_externe"]),
                "0,2 (sain)": essai(lambda: idn.verifier_reglages(**dict(base, budget_externe_usd=6.0))["somme_externe"])}))

spec = importlib.util.spec_from_file_location("lanceur", os.path.join(ARBRE, "demonstrations", "ideation_v1.py"))
lanceur = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lanceur)
bj = {("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0}
jj = [("a", "claude-opus-5-5"), ("b", "claude-fable-5-1")]
sonde("lanceur.verifier_relais(depense_usd)",
      lambda x: lanceur.verifier_relais({"plafond_usd": 40, "reserve_par_appel_usd": 4, "depense_usd": x}, 40.0, bj, jj), 0.0)
sonde("lanceur.verifier_relais(plafond_usd)",
      lambda x: lanceur.verifier_relais({"plafond_usd": x, "reserve_par_appel_usd": 4, "depense_usd": 0.0}, 40.0, bj, jj), 40)
sonde("lanceur.verifier_relais(reserve_par_appel_usd)",
      lambda x: lanceur.verifier_relais({"plafond_usd": 40, "reserve_par_appel_usd": x, "depense_usd": 0.0}, 40.0, bj, jj), 4)
lignes.append(("lanceur.verifier_relais(depense « 0.4 » en texte)",
               {"texte": essai(lambda: lanceur.verifier_relais({"plafond_usd": 40, "reserve_par_appel_usd": 4,
                                                                "depense_usd": "0.4"}, 40.0, bj, jj))}))
# tentative de contrôle au coût NaN (fichier altéré ou écrit par une autre version)
ctl = os.path.join(d, "S-controle")
os.makedirs(ctl)
with open(os.path.join(ctl, "tentative-1.json"), "w") as f:
    f.write('{"reglages": {"cout_claude_usd": NaN, "cout_externe_usd": -2.5}}')
lignes.append(("lanceur.lire_tentatives_controle (coûts NaN et −2,5, sans sceau)",
               {"lu": essai(lambda: lanceur.lire_tentatives_controle(ctl))}))

for nom, res in lignes:
    print(f"## {nom}")
    for k, v in res.items():
        print(f"   {k:>10} : {v}")
