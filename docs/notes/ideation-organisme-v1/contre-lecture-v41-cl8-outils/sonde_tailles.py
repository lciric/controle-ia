"""CL8 : taille du contrôle d'Argon (course) et de la consigne du juge (bras) aux tailles du devis ; coût au barème haut
du code (BAREME_INCONNU de relais_reel : 10 $/M jetons d'entrée, 50 $/M de sortie) et au taux implicite du devis
(2,5 $ pour ≈ 1,1 million de caractères). Usage : python3 -B sonde_tailles.py ARBRE DOSSIER"""
import json, os, sys
ARBRE, D = sys.argv[1], sys.argv[2]
sys.path.insert(0, ARBRE)
from pole import ideation as idn
from pole.relais_reel import BAREME_INCONNU
os.makedirs(D, exist_ok=False)

def ecrire(nom, t):
    p = os.path.join(D, nom)
    open(p, "w", encoding="utf-8").write(t)
    return p

def cout(car, cpj, sortie_j=0):
    return car / cpj * BAREME_INCONNU[0] / 1e6 + sortie_j * BAREME_INCONNU[1] / 1e6

TAUX_DEVIS = 2.5 / 1.1e6
res = {"bareme_inconnu": BAREME_INCONNU, "taux_devis_usd_par_caractere": TAUX_DEVIS}
fm = idn.fiche_maximale()
res["fiche_maximale_json_indent1"] = len(json.dumps(fm, ensure_ascii=False, indent=1))
q = ecrire("q.md", "Quelles questions ?")
FICHE = {"nom": "Sobre fort", "type": "question", "enonce": "Le transfert suit-il une courbe prédite ?",
         "loi_predictive": {"espace_instances": "familles", "prediction": "rappel décroît", "signe": "-", "metrique": "rappel"},
         "perte_traduction": "pente", "questions_servies": ["Q4"],
         "avantage": {"source": "programme", "texte": "théorie", "incopiable_parce_que": "carte"},
         "originalite": {"niveau": "transposition", "texte": "rupture"},
         "demande_organisme": {"nature": "ajout", "texte": "générateur"},
         "cout": {"nature": "processeur", "ordre_de_grandeur": "jours"}, "piege": "artefact", "cosmetique_si": "plates",
         "anteriorite": [{"reference": "réf", "statut": "RAPPORTE"}]}
tm_ = ecrire("temoins.json", json.dumps({"temoins": [
        {"fiche": dict(FICHE), "attendu": "eligible", "classe": "vrai"},
        {"fiche": dict(FICHE, nom="Verbeux vide", enonce="Long " * 50), "attendu": "ineligible",
         "note_max": {"falsifiabilite": 1}, "classe": "faux_falsifiabilite"},
        {"fiche": dict(FICHE, nom="Assuré occupé", originalite={"niveau": "inedite", "texte": "jamais vu"}),
         "attendu": "ineligible", "note_max": {"originalite": 1}, "classe": "faux_anteriorite"},
        {"fiche": dict(FICHE, nom="Jumeau"), "attendu": "eligible", "jumeau_de": "Sobre fort", "classe": "jumeau"}]}, ensure_ascii=False))
for nom, tp, tm in (("devis-1.1M", 750_000, 350_000), ("maximum", 750_000, 750_000), ("petit-S1", 2000, 2000)):
    p = ecrire(f"p-{nom}.md", ("Texte de contexte. " * 50000)[:tp])
    m = ecrire(f"m-{nom}.md", ("Tour interne. " * 60000)[:tm])
    lb = os.path.join(D, f"lb-{nom}.json")
    idn.construire_liste_blanche([p, q, m, tm_], lb)
    att = os.path.join(D, f"att-{nom}.json")
    idn.ecrire_json_scelle(att, {"lecteur": "x", "lu_le": "x", "materiau_sha256": {os.path.basename(m): idn.sha256_fichier(m)}})
    budgets = {("proposeur_ideation", "claude-opus-5-5"): 5.0, ("proposeur_ideation", "claude-fable-5-1"): 9.3,
               ("juge_ideation", "claude-opus-5-5"): 4.0, ("juge_ideation", "claude-fable-5-1"): 7.0,
               ("proposeur_ideation", "gemini-argon"): 2.5, ("juge_ideation", "gemini-argon"): 3.5}
    v = idn.verifier_reglages(liste_blanche=lb, question=q, temoins=tm_, pieces=[p], materiau=[m], attestation_materiau=att,
                              budgets=budgets, budget_total_usd=40.0, budget_externe_usd=11.6,
                              proposeurs=[("opus", "claude-opus-5-5"), ("fable", "claude-fable-5-1")],
                              juges=[("juge-opus", "claude-opus-5-5"), ("juge-fable", "claude-fable-5-1")],
                              proposeurs_externes=[("argon", "gemini-argon")], juges_externes=[("argon", "gemini-argon")],
                              seconde_passe=True, cout_controles_prevu_usd=0.4, cout_controles_externes_prevu_usd=2.5,
                              taille_max_pieces=750_000)
    t41 = len(idn.consigne_de_controle(v["texte_controle_externe"]))
    t40 = len(idn.consigne_de_controle(v["texte_pieces"] + "\n\n" + f"### m\n{open(m).read()}" + "\n\n" + ("x" * 4000 + "\n") * 8))
    res[nom] = {"pieces": tp, "materiau": tm, "controle_v41": t41, "controle_v40_formule": t40,
                "cout_v41_4c": round(cout(t41, 4), 3), "cout_v41_3c_2000s": round(cout(t41, 3, 2000), 3),
                "cout_v41_taux_devis": round(t41 * TAUX_DEVIS, 3), "cout_v40_4c": round(cout(t40, 4), 3),
                "depasse_2_5_au_bareme_4c": cout(t41, 4) > 2.5}
# consigne du juge : pièces de juge + fiches servies (2 passes × 8 × 3 proposeurs) + 4 témoins
for nom, pj, taille_fiche in (("petit-0-pj-fiches-1k", 0, 1000), ("realiste-48-fiches-3k-pj-100k", 100_000, 3000),
                              ("pj-750k-48-fiches-3k", 750_000, 3000), ("maximum-48-fiches-max-pj-750k", 750_000, "max")):
    if taille_fiche == "max":
        f = dict(fm)
    else:
        f = {k: v for k, v in fm.items()}
        t = "y" * (taille_fiche // 12)
        f = json.loads(json.dumps(fm).replace("x" * 3000, t).replace("x" * 500, "r" * 100))
    fiches = [dict(f, identifiant=f"T{i:02d}") for i in range(1, 53)]
    pieces_j = [("pj.md", "z" * pj, "h")] if pj else []
    c = idn.consigne_juge(fiches, "Quelles questions ?", pieces_j)
    t = len(idn.consigne_de_controle(c))
    res["juge-" + nom] = {"taille_controle_du_bras": t, "cout_4c": round(cout(t, 4), 3), "cout_3c_2000s": round(cout(t, 3, 2000), 3),
                          "cout_taux_devis": round(t * TAUX_DEVIS, 3), "depasse_0_2_4c": cout(t, 4) > 0.2}
for t in (22_000, 243_000):
    res[f"controle_du_bras_{t}"] = {"cout_4c_entree": round(cout(t, 4), 4), "cout_3c_2000s": round(cout(t, 3, 2000), 4),
                                    "cout_taux_devis": round(t * TAUX_DEVIS, 4), "seuil_0_2_en_caracteres_4c": int(0.2 / (10 / 1e6) * 4),
                                    "seuil_0_2_en_caracteres_3c_2000s": int((0.2 - 2000 * 50 / 1e6) / (10 / 1e6) * 3)}
print(json.dumps(res, ensure_ascii=False, indent=1))
