"""Ordre de la course v2 (brouillon) : (1) rejoue son générateur sur le brouillon v1 (arbre jetable) et compare au commit ;
(2) pour chacun des 7 couples de la contre-lecture précédente, vérifie que « ancien » est unique dans le brouillon v1 et que
« nouveau » (adapté à la chaîne v12 par les remplacements globaux du générateur) figure une seule fois dans le brouillon v2 ;
(3) relève les points demandés par la consigne (motifs=28, borne ≈ 5 800 s, suite ≈ 68 min, garde 1914, marqueurs restants,
commandes du lanceur et sous-commandes) ; (4) cherche toute chaîne qui ressemble à une clé ou une sortie brute ;
(5) cherche si l'ordre fait vérifier le bloc d'équivalence et le nombre de pas de distillation (constats neufs).

Usage : python -I verifier_ordre_course_v2_v1.py DEPOT DOSSIER_JETABLE
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

DEPOT, JET = Path(sys.argv[1]), Path(sys.argv[2])
C = "8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63"
D2 = "docs/notes/g0-deux-semaines-v1/ordres-t06-course-v2/"
V1 = "docs/notes/g0-deux-semaines-v1/ordres-t06-course-v1/ordre-fille-6-t06-course-v1-brouillon.md"
V2 = D2 + "ordre-fille-6-t06-course-v2-brouillon.md"
GEN = D2 + "pieces/generer_ordre_course_v2.py"
CP = D2 + "pieces/couples-ordre-course-v1.json"


def show(chemin: str, commit: str = C) -> bytes:
    return subprocess.run(["git", "-C", str(DEPOT), "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout


r: dict = {}
racine = JET / "depot-ordre"
for p in (V1, GEN, CP):
    (racine / p).parent.mkdir(parents=True, exist_ok=True)
    (racine / p).write_bytes(show(p))
g = subprocess.run([sys.executable, "-I", "-B", str(racine / GEN), str(racine)], capture_output=True, text=True)
r["generateur"] = {"code": g.returncode, "sortie": g.stdout.strip(), "err": g.stderr.strip()[-300:]}
v2 = show(V2)
r["rejeu_egal_au_commit"] = (racine / V2).read_bytes() == v2 if (racine / V2).exists() else False
r["sha256_v2"] = hashlib.sha256(v2).hexdigest()
t1, t2 = show(V1).decode("utf-8"), v2.decode("utf-8")
glob = (("scripts/lancer_t06_v10.sh", "scripts/lancer_t06_v12.sh"), ("amorce v8", "amorce v10"), ("prep/t06-course-v1", "prep/t06-course-v12"),
        ("audit-fuite-r1-v4-bras-b-v1.json", "audit-fuite-r1-v4-bras-b-v4.json"))
couples = json.loads(show(CP))
etat = []
for i, c in enumerate(couples, 1):
    nouveau = c["nouveau"]
    for a, b in glob:
        nouveau = nouveau.replace(a, b)
    entier = t2.count(nouveau)
    note = ""
    if entier != 1 and i == 7:
        # le générateur remplace ensuite, dans le texte du couple 7, la phrase « bras-b.out porte l'issue » (couple « sortie bras B »)
        ancienne = "`traces/bras-b-…/bras-b.out` porte l'issue du bras B (`{\"issue\": …}`) : **ne l'ouvre pas**, ni `bras-b.err` (noms et tailles seulement)."
        reste = [x for x in nouveau.split(ancienne) if x]
        entier = min(t2.count(x) for x in reste)
        note = "sa première phrase est remplacée ensuite par le couple « sortie bras B » du générateur ; le reste est trouvé"
    etat.append({"couple": i, "ancien_dans_v1": t1.count(c["ancien"]), "nouveau_dans_v2": entier, "note": note})
r["couples_contre_lecture_precedente"] = etat
# (3) points de la consigne
r["motifs=28"] = t2.count("motifs=28")
r["motifs=27"] = len(re.findall(r"motifs=27", t2))
r["borne_5800"] = t2.count("5 800 s")
r["suite_68_min"] = t2.count("68 minutes")
r["tests_1914"] = t2.count("1914 passed")
r["garde_autre_que_1914"] = "si l'instance compte autre chose, l'amorce s'arrête avant le run" in t2
r["marqueurs"] = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t2)))
r["lanceurs_cites"] = sorted(set(re.findall(r"scripts/lancer_t06_v[0-9]+\.sh", t2)))
r["amorces_citees"] = sorted(set(re.findall(r"amorce(?:_instance_t06)? ?v?[0-9]+", t2)))
r["sous_commandes"] = sorted(set(re.findall(r"lancer_t06_v12\.sh (controles|creation auto (?:course|relance)|surveillance|apres-creation|controles-epreuve)", t2)))
r["fenetre_cite"] = "scripts/fenetre_carte_t06_v1.sh scripts/lancer_t06_v12.sh" in t2
r["t06_branche_code_course"] = t2.count("T06_BRANCHE_CODE=")
r["t06_branche"] = len(re.findall(r"T06_BRANCHE=", t2))
r["calcul_branche"] = len(re.findall(r"calcul/", t2))
# (4) clés ou sorties brutes
r["motifs_de_cle"] = {"ghp_": t2.count("ghp_"), "hf_": len(re.findall(r"\bhf_[A-Za-z0-9]{10,}", t2)), "github_pat": t2.count("github_pat"),
                       "longue_chaine_hex_64": len(re.findall(r"\b[0-9a-f]{64}\b", t2)), "json_brut_instances": t2.count('"instances"')}
# (5) constats neufs
r["equivalence_verifiee_par_l_ordre"] = {"equivalence": t2.count("equivalence"), "équivalence": t2.count("équivalence")}
r["pas_distillation_verifies_par_l_ordre"] = {"pas déclarés": t2.count("pas déclarés"), "pas_declares": t2.count("pas_declares"), "480": t2.count("480")}
r["v1_marqueurs"] = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", t1)))
print(json.dumps(r, ensure_ascii=False, indent=1))
