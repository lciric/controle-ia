"""Contre-lecture de la garde δ : entrées du script (JSON, CSV, non finis, vides, bornes, options).

Lancement : python3 -B verif_entrees.py CHEMIN_DU_SCRIPT DOSSIER_DE_TRAVAIL
Chaque cas écrit un fichier d'entrée dans DOSSIER_DE_TRAVAIL/entrees/, lance le script en sous-processus (python3 -I -B)
avec 100 répétitions, une taille 10, sans n₈₀, et consigne : code de sortie, dernière ligne d'erreur, écarts lus.
"""
import json
import os
import subprocess
import sys

SCRIPT, TRAVAIL = sys.argv[1], sys.argv[2]
ENT = os.path.join(TRAVAIL, "entrees")
os.makedirs(ENT, exist_ok=True)

cas_fichiers = {
    "ok.json": '{"ecarts": [0.0, 0.1, -0.1, 0.0, 0.2]}',
    "ok_fa_fb.json": '{"fA": [0.1, 0.0, 0.2], "fB": [0.0, 0.0, 0.1]}',
    "ok.csv": "ecart\n0.0\n0.1\n-0.1\n",
    "ok_fa_fb.csv": "fA,fB\n0.1,0.0\n0.0,0.0\n0.2,0.1\n",
    "nan.json": '{"ecarts": [0.0, NaN, 0.1]}',
    "inf.json": '{"ecarts": [0.0, Infinity, 0.1]}',
    "null.json": '{"ecarts": [0.0, null, 0.1]}',
    "booleens.json": '{"ecarts": [true, false, true, false]}',
    "chaines.json": '{"ecarts": ["0.1", "0.0", "-0.1"]}',
    "les_deux_cles.json": '{"ecarts": [0.0, 0.0], "fA": [0.9, 0.9], "fB": [0.0, 0.0]}',
    "fa_hors_0_1.json": '{"fA": [1.5, 1.2, 1.4], "fB": [1.0, 1.0, 1.0]}',
    "fa_fb_longueurs.json": '{"fA": [0.1, 0.0], "fB": [0.0]}',
    "vide.json": "",
    "liste_vide.json": '{"ecarts": []}',
    "un_seul.json": '{"ecarts": [0.1]}',
    "liste_racine.json": "[0.0, 0.1, 0.2]",
    "imbrique.json": '{"ecarts": [[0.0, 0.1], [0.1, 0.0]]}',
    "hors_bornes.json": '{"ecarts": [0.0, 1.5]}',
    "vide.csv": "",
    "entete_seule.csv": "ecart\n",
    "nan.csv": "ecart\n0.0\nnan\n0.1\n",
    "inf.csv": "ecart\n0.0\ninf\n0.1\n",
    "case_vide.csv": "ecart\n0.0\n\n0.1\n",
    "cellule_vide.csv": "fA,fB\n0.1,\n0.0,0.0\n",
    "virgule_decimale.csv": "ecart\n0,1\n-0,2\n0,3\n0,1\n",
    "point_virgule.csv": "fA;fB\n0.1;0.0\n0.0;0.1\n",
    "entete_espace.csv": " ecart\n0.0\n0.1\n",
    "json_dans_txt.txt": '{"ecarts": [0.0, 0.1, -0.1]}',
    "bom.csv": "﻿ecart\n0.0\n0.1\n",
    "recentre_sort_de_bornes.json": json.dumps({"ecarts": [1.0] + [-1.0] * 9}),
    "moyenne_negative.json": json.dumps({"ecarts": [-0.03] * 50 + [0.0] * 50}),
}


def lancer(args):
    r = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--repetitions", "100", "--tailles", "10", "--sans-n80"] + args,
                       capture_output=True, text=True, cwd=TRAVAIL)
    err = [l for l in r.stderr.strip().splitlines() if l.strip()]
    res = {"code": r.returncode, "erreur": (err[-1] if err else "")}
    if r.returncode == 0:
        d = json.loads(r.stdout)
        res["ecarts_observes"] = d.get("ecarts_observes")
        res["avertissements_stderr"] = [l for l in err if "Warning" in l]
        res["lois"] = list(d["lois"])
    return res


resultats = {}
for nom, contenu in cas_fichiers.items():
    chemin = os.path.join(ENT, nom)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(contenu)
    resultats[nom] = lancer(["--ecarts", chemin])

resultats["fichier_absent"] = lancer(["--ecarts", os.path.join(ENT, "absent.json")])
options = {
    "tailles_0": ["--tailles", "0"], "tailles_negative": ["--tailles", "-5"], "tailles_vide": ["--tailles", ""],
    "delta_0": ["--deltas", "0"], "delta_1": ["--deltas", "1"], "delta_0.6_tricheur_tronque": ["--deltas", "0.6"],
    "m_0": ["--m", "0"], "K_0": ["--K", "0"], "taux_negatif": ["--taux", "-0.1"], "taux_2": ["--taux", "2"],
    "sigma_negatif": ["--sigma", "-0.1"], "repetitions_99": ["--repetitions", "99"],
}
for nom, args in options.items():
    resultats["option|" + nom] = lancer(args)

# cas particulier : δ = 0,6, tricheur annoncé 2δ = 1,2 ; moyenne réellement tirée ?
r = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--repetitions", "100", "--tailles", "10", "--sans-n80",
                    "--deltas", "0.6"], capture_output=True, text=True, cwd=TRAVAIL)
if r.returncode == 0:
    d = json.loads(r.stdout)
    c = d["lois"]["binomiale_K10_taux0.01"]["cellules"]["delta=0.6|n=10"]
    resultats["option|delta_0.6_tricheur_tronque"]["tricheur"] = {"biais_annonce": c["tricheur"]["biais"],
                                                                   "moyenne_g_tiree": c["tricheur"]["moyenne_g"]}

# cas particulier : recentrage qui sort des bornes → NaN silencieux ?
chemin = os.path.join(ENT, "recentre_sort_de_bornes.json")
r = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--repetitions", "100", "--tailles", "10", "--sans-n80",
                    "--ecarts", chemin], capture_output=True, text=True, cwd=TRAVAIL)
if r.returncode == 0:
    d = json.loads(r.stdout)
    c = d["lois"]["reelle_recentree"]["cellules"]["delta=0.05|n=10"]
    resultats["recentre_sort_de_bornes.json"]["cellule_recentree_delta0.05_n10"] = {
        k: {"moyenne_g": v["moyenne_g"], "part20": v["certification"]["20.0"]["part"]} for k, v in c.items()}

# cas particulier : moyenne brute négative → cellule « frontière » brute hors frontière
chemin = os.path.join(ENT, "moyenne_negative.json")
r = subprocess.run([sys.executable, "-I", "-B", SCRIPT, "--repetitions", "1000", "--tailles", "960", "--sans-n80",
                    "--deltas", "0.05", "--ecarts", chemin], capture_output=True, text=True, cwd=TRAVAIL)
if r.returncode == 0:
    d = json.loads(r.stdout)
    for loi in ("reelle_recentree", "reelle_brute"):
        c = d["lois"][loi]["cellules"]["delta=0.05|n=960"]
        resultats["moyenne_negative.json"][f"{loi}_n960"] = {
            k: {"moyenne_g": round(v["moyenne_g"], 4), "part20": v["certification"]["20.0"]["part"],
                "part160": v["certification"]["160.0"]["part"]} for k, v in c.items()}

print(json.dumps(resultats, indent=1, ensure_ascii=False))
