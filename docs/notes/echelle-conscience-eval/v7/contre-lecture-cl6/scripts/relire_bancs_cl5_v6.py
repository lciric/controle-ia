"""cl6 : applique `lire()` de `analyser_echelle_v6.py` (telle quelle) aux intervalles que cl5 a consignés dans ses trois
bancs (106 analyses, deux couches : aucun drapeau de profondeur), et compare au rejeu versé par l'auteur
(`docs/notes/echelle-conscience-eval/v6/rejeu-bancs-cl5/rejeu-bancs-cl5-v6.jsonl`). Contrôle indépendant du calcul :
si les lectures concordent, le rejeu versé est ce que la lecture v6 rend sur les intervalles de cl5.
Usage : python -I -B relire_bancs_cl5_v6.py
"""
import collections
import importlib.util
import json
import pathlib

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v6")
DOCS = pathlib.Path("/home/user/controle-ia-travail/docs/notes/echelle-conscience-eval/v6")
spec = importlib.util.spec_from_file_location("an", ARBRE / "scripts" / "analyser_echelle_v6.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)


def r_depuis_banc(d):
    r = {"delta_lambda_ic": {}, "specificite_ic": {}, "specificite_signe_inverse_ic": {"petit": {}, "grand": {}},
         "profondeur_contraire": {x: {"ab": False, "ba": False} for x in AN.ISSUES}}
    for m in ("petit", "grand"):
        r[m] = {}
        for s in ("ab", "ba"):
            r[m][s] = {"lambda_ic": d[f"lambda_{s}_{m}_ic"], "A_ctx_fixe_ic": [d[f"Afixe_{s}_{m}_bas"], 1.0]}
            r["specificite_signe_inverse_ic"][m][s] = d[f"ssi_{s}_{m}_ic"]
    for s in ("ab", "ba"):
        r["delta_lambda_ic"][s] = d[f"dl_{s}_ic"]
        r["specificite_ic"][s] = d[f"spec_{s}_ic"]
    return r


def principal():
    verse = {(l["scenario"], l["graine"]): l for l in
             map(json.loads, (DOCS / "rejeu-bancs-cl5" / "rejeu-bancs-cl5-v6.jsonl").read_text().splitlines())}
    n = accord = 0
    ecarts = []
    resume = collections.Counter()
    for lot in ("banc-cl5-lot1.jsonl", "banc-cl5-lot2.jsonl", "banc-cl5-lot3.jsonl"):
        for ligne in (DOCS / "contre-lecture-cl5" / "banc" / lot).read_text().splitlines():
            d = json.loads(ligne)
            lecture, reserves, detail = AN.lire(r_depuis_banc(d))
            v = verse[(d["scenario"], d["graine"])]
            ok = (lecture == v["lecture_v6"] and reserves == v["reserves_v6"]
                  and detail["issues_tenues_par_sens"] == v["issues_tenues_v6"])
            n += 1
            accord += ok
            resume[(d["scenario"], d["lecture"], lecture)] += 1
            if not ok:
                ecarts.append((d["scenario"], d["graine"], lecture, reserves, v["lecture_v6"], v["reserves_v6"]))
    print(f"{n} analyses de cl5 relues par lire() v6 ; lecture, réserves et issues tenues identiques au rejeu versé : "
          f"{accord} sur {n}")
    for e in ecarts:
        print("écart :", e)
    changes = {k: c for k, c in resume.items() if k[1] != k[2]}
    print("lectures v5 (cl5) → v6 qui changent :")
    for (sc, v5, v6), c in sorted(changes.items()):
        print(f"  {sc} : « {v5} » → « {v6} » : {c}")


if __name__ == "__main__":
    principal()
