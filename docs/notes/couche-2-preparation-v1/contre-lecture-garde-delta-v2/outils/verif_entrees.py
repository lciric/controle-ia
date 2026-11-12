"""Q5 — entrées du script v2 (`--ecarts`, `--ecarts-contraste`) et réglages : refus explicites, replis silencieux.

Écrit les fichiers d'essai dans ../sorties/essais_entrees/entrees/ et lance la copie conforme du script sur chacun.
Usage : python3 -I -B verif_entrees.py > ../sorties/verif_entrees.json
"""
import json
import os
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(ICI, "copie_script", "sim_garde_v2.py")
DOSSIER = os.path.join(ICI, "..", "sorties", "essais_entrees", "entrees")
os.makedirs(DOSSIER, exist_ok=True)
PETIT = ["--repetitions", "100", "--tailles", "5", "--deltas", "0.1", "--m", "1", "--K", "3", "--taux", "0.1",
         "--biais", "0", "--comparateurs", "1", "--sans-n80"]

FICHIERS = {
    # CSV
    "ok_point.csv": "ecart\n0.1\n-0.2\n0.3\n0.1\n",
    "ok_crlf.csv": "ecart\r\n0.1\r\n-0.2\r\n0.3\r\n",
    "ok_fafb.csv": "fA,fB\n0.1,0.0\n0.2,0.3\n0.0,0.0\n",
    "ok_unite_ecart.csv": "unite,ecart\nu1,0.1\nu2,-0.2\nu3,0\n",
    "virgule_decimale.csv": "ecart\n0,1\n-0,2\n0,3\n0,1\n",
    "virgule_decimale_fafb.csv": "fA,fB\n0,1,0,0\n0,2,0,3\n",
    "point_virgule_virgule_decimale.csv": "fA;fB\n0,1;0,0\n0,2;0,3\n",
    "virgule_decimale_guillemets.csv": 'ecart\n"0,1"\n"-0,2"\n',
    "virgule_decimale_colonne_en_trop_vide.csv": "ecart,note\n0,1\n-0,2\n0,3\n",
    "virgule_decimale_unite_note.csv": "ecart,unite\n0,1\n0,2\n",
    "ligne_vide_milieu.csv": "ecart\n0.1\n\n0.3\n",
    "ligne_vide_fin_double.csv": "ecart\n0.1\n0.3\n\n",
    "lignes_blanches_espaces.csv": "ecart\n0.1\n   \n0.3\n",
    "booleens.csv": "ecart\nTrue\nFalse\n",
    "nan.csv": "ecart\nnan\n0.1\n",
    "inf.csv": "ecart\ninf\n0.1\n",
    "texte_na.csv": "ecart\nNA\n0.1\n",
    "champ_vide.csv": "ecart\n\"\"\n0.1\n",
    "bom.csv": "﻿ecart\n0.1\n0.2\n",
    "entete_seul.csv": "ecart\n",
    "une_ligne.csv": "ecart\n0.1\n",
    "hors_bornes.csv": "ecart\n1.5\n0.1\n",
    "fafb_hors_01.csv": "fA,fB\n1.5,1.0\n0.2,0.1\n",
    "espaces.csv": "ecart\n 0.1 \n-0.2\n",
    "entete_ecart_et_fafb.csv": "ecart,fA,fB\n0.5,0.1,0.0\n0.5,0.2,0.0\n",
    "pourcentages.csv": "ecart\n10\n-20\n",
    # JSON
    "ok.json": json.dumps({"ecarts": [0.1, -0.2, 0.3, 0.0]}),
    "ok_fafb.json": json.dumps({"fA": [0.1, 0.2, 0.0], "fB": [0.0, 0.3, 0.0]}),
    "booleens.json": '{"ecarts": [true, false, 0.1]}',
    "chaines.json": '{"ecarts": ["0.1", "0.2"]}',
    "nan.json": '{"ecarts": [NaN, 0.1]}',
    "infini.json": '{"ecarts": [Infinity, 0.1]}',
    "null.json": '{"ecarts": [null, 0.1]}',
    "les_deux.json": json.dumps({"ecarts": [0.1, 0.2], "fA": [0.1, 0.2], "fB": [0.0, 0.0]}),
    "fA_seul.json": json.dumps({"fA": [0.1, 0.2]}),
    "fafb_hors_01.json": json.dumps({"fA": [1.5, 0.2], "fB": [1.0, 0.1]}),
    "fafb_longueurs.json": json.dumps({"fA": [0.1, 0.2, 0.3], "fB": [0.0, 0.1]}),
    "liste_racine.json": "[0.1, 0.2]",
    "imbrique.json": '{"ecarts": [[0.1], [0.2]]}',
    "grand_entier.json": '{"ecarts": [' + "1" + "0" * 400 + ', 0.1]}',
    "vide.json": '{"ecarts": []}',
    "cle_inconnue.json": '{"ecart": [0.1, 0.2]}',
    "cles_en_trop.json": json.dumps({"ecarts": [0.1, 0.2], "unites": ["u1"], "signe": "B-A"}),
    "json_sous_extension_txt.txt": json.dumps({"ecarts": [0.1, 0.2]}),
}


def lancer(args):
    p = subprocess.run([sys.executable, "-I", "-B", SCRIPT] + args, capture_output=True, text=True, timeout=300)
    res = {"code": p.returncode, "erreur_derniere_ligne": (p.stderr.strip().splitlines() or [""])[-1][:300]}
    if p.returncode == 0:
        try:
            s = json.loads(p.stdout)
            res["ecarts_observes"] = s.get("ecarts_observes")
            res["ecarts_contraste_observes"] = s.get("ecarts_contraste_observes")
            res["avertissements_stderr"] = p.stderr.strip()[:300]
            res["lois_garde"] = list(s.get("lois_garde", {}))
        except Exception as e:
            res["sortie_illisible"] = str(e)
    return res


sortie = {"script": SCRIPT, "commande_commune": PETIT, "garde": {}, "contraste": {}, "reglages": {}}
for nom, contenu in FICHIERS.items():
    chemin = os.path.join(DOSSIER, nom)
    with open(chemin, "w", encoding="utf-8", newline="") as f:
        f.write(contenu)
    sortie["garde"][nom] = lancer(PETIT + ["--ecarts", chemin])
for nom in ["ok_fafb.csv", "fafb_hors_01.csv", "fafb_hors_01.json", "virgule_decimale.csv", "nan.json", "ok.json"]:
    sortie["contraste"][nom] = lancer(PETIT + ["--ecarts-contraste", os.path.join(DOSSIER, nom)])
sortie["garde"]["absent"] = lancer(PETIT + ["--ecarts", os.path.join(DOSSIER, "nexiste_pas.csv")])

# Réglages : bords
REG = {
    "delta_0.5_taux_0.1": ["--deltas", "0.5"],
    "delta_0.6": ["--deltas", "0.6"],
    "taux_0.95_delta_0.1": ["--taux", "0.95"],
    "taux_1": ["--taux", "1"],
    "taux_0.45_biais_0.025_delta_0.3": ["--taux", "0.45", "--deltas", "0.3", "--biais", "0.025"],
    "K_0": ["--K", "0"],
    "m_0": ["--m", "0"],
    "graine_negative": ["--graine", "-1"],
    "tailles_vide": ["--tailles", ""],
    "tailles_virgule_fin": ["--tailles", "5,"],
    "biais_negatif": ["--biais", "-0.01"],
    "ecart_contraste_0.6": ["--ecart-contraste", "0.6"],
    "deltas_nan": ["--deltas", "nan"],
    "taux_nan": ["--taux", "nan"],
    "biais_nan": ["--biais", "nan"],
}
for nom, extra in REG.items():
    args = list(PETIT)
    for i in range(0, len(extra), 2):
        j = args.index(extra[i]) if extra[i] in args else None
        if j is None:
            args += [extra[i], extra[i + 1]]
        else:
            args[j + 1] = extra[i + 1]
    r = subprocess.run([sys.executable, "-I", "-B", SCRIPT] + args, capture_output=True, text=True, timeout=300)
    res = {"code": r.returncode, "erreur_derniere_ligne": (r.stderr.strip().splitlines() or [""])[-1][:300]}
    if r.returncode == 0:
        s = json.loads(r.stdout)
        cel = next(iter(s["cellules"].values()))
        res["exemple_cellule"] = {k: v for k, v in cel.items() if k not in ("etiquette",)}
        res["reglages_lus"] = {k: s["reglages"][k] for k in ("deltas", "taux", "biais", "seuils")}
    sortie["reglages"][nom] = res
json.dump(sortie, sys.stdout, indent=1, ensure_ascii=False)
print()
