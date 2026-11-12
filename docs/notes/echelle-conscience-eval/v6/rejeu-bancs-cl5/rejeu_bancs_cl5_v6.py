#!/usr/bin/env python3
"""Rejeu des bancs de la contre-lecture n° 5 avec l'analyse v6 (lignée « session-depot », 27 octobre 2026 ; CLV-01).
Non décisif. Pour chaque ligne des trois bancs de cl5 (`banc-cl5-lot1.jsonl`, `-lot2`, `-lot3`), mêmes scénario et
graine, mêmes activations : le générateur de cl5 (`banc_cl5.py`, importé tel quel, scénarios des lots 2 et 3 ajoutés
comme dans `banc_cl5_lot2.py` et `banc_cl5_lot3.py`), même entropie (la graine), 300 tirages ; seule l'analyse change
(`analyser_echelle_v6.py` au lieu de la v5). Sortie : une ligne JSON par analyse (lecture v5 relue dans le banc de cl5,
lecture v6, réserves, issues tenues par sens), puis un résumé par scénario ; contrôle : les intervalles de λ du rejeu
sont comparés à ceux que le banc de cl5 a consignés (même calcul depuis la v5, mêmes activations).
    python -I -B rejeu_bancs_cl5_v6.py PIECES_CL5 ANALYSE_V6 SORTIE_JSONL PROCESSUS
      PIECES_CL5 : docs/notes/echelle-conscience-eval/v6/contre-lecture-cl5 ; ANALYSE_V6 : chemin de analyser_echelle_v6.py
"""
import collections
import hashlib
import importlib.util
import json
import multiprocessing
import pathlib
import sys
import tempfile

PIECES, ANALYSE, SORTIE, PROCESSUS = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]),
                                      int(sys.argv[4]))


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


B = charger("banc_cl5", PIECES / "scripts" / "banc_cl5.py")
for lot in ("banc_cl5_lot2.py", "banc_cl5_lot3.py"):          # scénarios ajoutés, relus dans les scripts de cl5
    texte = (PIECES / "scripts" / lot).read_text(encoding="utf-8")
    debut = texte.index("B.SCENARIOS.update(")
    fin = texte.index("\n})", debut) + 3                     # fin du dictionnaire, en début de ligne
    exec(texte[debut:fin], {"B": B})
AN = charger("an6", ANALYSE)
AN.N_BOOT = 300


def un_travail(t):
    nom, g, v5, n5, ic5 = t
    st = json.loads(B.STIMULI.read_text(encoding="utf-8"))["stimuli"]
    a8, a70, o8, o70 = B.SCENARIOS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp) / f"{nom}-{g}"
        B.fabriquer(base / "p", st, a8, g, **o8)
        B.fabriquer(base / "g", st, a70, g + 1, **o70)
        code = AN.principal([str(B.STIMULI), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v6.json").read_text(encoding="utf-8"))
    ic6 = {f"{s}_{m}": [round(x, 3) for x in r[m][s]["lambda_ic"]] for s in ("ab", "ba") for m in ("petit", "grand")}
    return {"scenario": nom, "graine": g, "lecture_v5_cl5": v5, "reserves_v5_cl5": n5,
            "intervalles_identiques_a_cl5": ic6 == ic5,
            "lecture_v6": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
            "reserves_v6": r["reserves"], "issues_tenues_v6": r["issues_tenues_par_sens"],
            "lambda_ic": ic6}


def principal():
    if SORTIE.exists():
        sys.exit(f"{SORTIE} existe déjà (R12)")
    travaux = []
    for lot in ("banc-cl5-lot1.jsonl", "banc-cl5-lot2.jsonl", "banc-cl5-lot3.jsonl"):
        for ligne in (PIECES / "banc" / lot).read_text(encoding="utf-8").splitlines():
            d = json.loads(ligne)
            ic5 = {f"{s}_{m}": d[f"lambda_{s}_{m}_ic"] for s in ("ab", "ba") for m in ("petit", "grand")}
            travaux.append((d["scenario"], d["graine"], d.get("lecture"), len(d.get("reserves") or []), ic5))
    with multiprocessing.get_context("fork").Pool(PROCESSUS) as pool:
        lignes = pool.map(un_travail, travaux, chunksize=1)
    with open(SORTIE, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    resume = collections.defaultdict(collections.Counter)
    for ligne in lignes:
        lu = ligne.get("lecture_v6", f"code {ligne.get('code')}")
        n = len(ligne.get("reserves_v6") or [])
        n5 = ligne.get("reserves_v5_cl5") or 0
        resume[ligne["scenario"]][(ligne.get("lecture_v5_cl5") + (f" ({n5} réserve(s))" if n5 else ""),
                                   lu + (f" ({n} réserve(s))" if n else ""))] += 1
    print(f"analyse v6 : {ANALYSE.name} sha256 {hashlib.sha256(ANALYSE.read_bytes()).hexdigest()} ; {len(lignes)} analyses")
    print(f"intervalles de λ identiques à ceux du banc de cl5 : "
          f"{sum(bool(l.get('intervalles_identiques_a_cl5')) for l in lignes)} sur {len(lignes)}")
    for nom, c in resume.items():
        print(nom)
        for (v5, v6), n in sorted(c.items()):
            print(f"  v5 (banc de cl5) « {v5} » → v6 « {v6} » : {n}")


if __name__ == "__main__":
    principal()
