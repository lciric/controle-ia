#!/usr/bin/env python3
"""Rejeu des bancs des contre-lectures n° 5 et n° 6 avec l'analyse v7 (lignée « session-depot », 27 octobre 2026 ;
CLU-01). Non décisif. Pour chaque ligne des bancs de cl5 (`banc-cl5-lot1.jsonl`, `-lot2`, `-lot3`) et de cl6
(`banc-cl6-cas.jsonl`, `-d256.jsonl`, `-d256-suite.jsonl`, `-d256-n2000.jsonl`, `-d64-oppose.jsonl` ; le rejeu partiel
de cl6 reprend six lignes de cl5 et n'est pas rejoué), mêmes scénario et graine, mêmes activations : le générateur de
cl6 (`banc_cl6.py`, qui recopie à l'identique celui de cl5 et porte les scénarios des deux), même entropie (la graine),
même nombre de tirages que le banc (300, ou 2 000 pour `-d256-n2000`) ; seule l'analyse change. `banc_cl6.py` est
exécuté depuis son texte versé, la seule ligne `ARBRE = …` remplacée par l'arbre des outils v6 de cette session (même
commit b8b7665, autre bloc-notes), puisque le module charge l'analyse v6 à l'import ; la ligne remplacée est écrite en
sortie. Contrôle : les intervalles de λ du rejeu sont comparés à ceux que le banc a consignés (calcul de λ inchangé
depuis la v5). Lecture v6 de référence : celle du banc de cl6, ou, pour les bancs de cl5, celle du rejeu v6
(`v6/rejeu-bancs-cl5/rejeu-bancs-cl5-v6.jsonl`).
    python -I -B rejeu_bancs_cl5_cl6_v7.py NOTES ARBRE_V6 ANALYSE_V7 SORTIE_JSONL PROCESSUS
      NOTES : docs/notes/echelle-conscience-eval ; ARBRE_V6 : <arbre des outils>/echelle-v6 ;
      ANALYSE_V7 : <arbre des outils>/echelle-v7/scripts/analyser_echelle_v7.py
"""
import collections
import hashlib
import importlib.util
import json
import multiprocessing
import pathlib
import sys
import tempfile

NOTES, ARBRE_V6, ANALYSE, SORTIE, PROCESSUS = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]),
                                               pathlib.Path(sys.argv[3]), pathlib.Path(sys.argv[4]), int(sys.argv[5]))
CL5 = NOTES / "v6" / "contre-lecture-cl5" / "banc"
CL6 = NOTES / "v7" / "contre-lecture-cl6"
BANCS = [CL5 / f"banc-cl5-lot{i}.jsonl" for i in (1, 2, 3)] + [
    CL6 / "banc" / f"banc-cl6-{n}.jsonl" for n in ("cas", "d256", "d256-suite", "d256-n2000", "d64-oppose")]
texte = (CL6 / "scripts" / "banc_cl6.py").read_text(encoding="utf-8")
ancienne = [l for l in texte.splitlines() if l.startswith("ARBRE = ")]
assert len(ancienne) == 1
nouvelle = f"ARBRE = pathlib.Path({str(ARBRE_V6)!r})"
B = type(sys)("banc_cl6")
B.__file__ = str(CL6 / "scripts" / "banc_cl6.py")
exec(compile(texte.replace(ancienne[0], nouvelle), B.__file__, "exec"), B.__dict__)
spec = importlib.util.spec_from_file_location("an7", ANALYSE)
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)
V6_CL5 = {(d["scenario"], d["graine"]): d for d in map(json.loads, (NOTES / "v6" / "rejeu-bancs-cl5" /
                                                                 "rejeu-bancs-cl5-v6.jsonl").read_text().splitlines())}


def un_travail(t):
    banc, nom, g, n_boot, v6, ic_banc = t
    AN.N_BOOT = n_boot
    st = json.loads(B.STIMULI.read_text(encoding="utf-8"))["stimuli"]
    a8, a70, o8, o70 = B.SCENARIOS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp) / f"{nom}-{g}"
        B.fabriquer(base / "p", st, a8, g, **o8)
        B.fabriquer(base / "g", st, a70, g + 1, **o70)
        code = AN.principal([str(B.STIMULI), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"banc": banc, "scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v7.json").read_text(encoding="utf-8"))
    ic = {f"{s}_{m}": [round(x, 3) for x in r[m][s]["lambda_ic"]] for s in ("ab", "ba") for m in ("petit", "grand")}
    return {"banc": banc, "scenario": nom, "graine": g, "n_boot": n_boot, "lecture_v6": v6,
            "intervalles_identiques_au_banc": ic == ic_banc,
            "lecture_v7": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
            "reserves_v7": r["reserves"], "issues_tenues_v7": r["issues_tenues_par_sens"],
            "ecart_sens": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
            "ecart_sens_ic": {k: [round(x, 3) for x in v] for k, v in r["ecart_sens_ic"].items()},
            "conditions_manquantes_v7": r["conditions_manquantes"], "lambda_ic": ic}


def principal():
    if SORTIE.exists():
        sys.exit(f"{SORTIE} existe déjà (R12)")
    travaux = []
    for banc in BANCS:
        for ligne in banc.read_text(encoding="utf-8").splitlines():
            d = json.loads(ligne)
            ic = {f"{s}_{m}": d[f"lambda_{s}_{m}_ic"] for s in ("ab", "ba") for m in ("petit", "grand")}
            if banc.parent == CL5:
                v = V6_CL5[(d["scenario"], d["graine"])]
                v6 = v["lecture_v6"] + (f" ({len(v['reserves_v6'])} réserve(s))" if v["reserves_v6"] else "")
            else:
                v6 = d["lecture"] + (f" ({len(d['reserves'])} réserve(s))" if d["reserves"] else "")
            travaux.append((banc.name, d["scenario"], d["graine"], 2000 if banc.name.endswith("n2000.jsonl") else 300,
                            v6, ic))
    with multiprocessing.get_context("fork").Pool(PROCESSUS) as pool:
        lignes = pool.map(un_travail, travaux, chunksize=1)
    with open(SORTIE, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"ligne remplacée dans banc_cl6.py : « {ancienne[0]} » → « {nouvelle} »")
    print(f"analyse v7 : {ANALYSE.name} sha256 {hashlib.sha256(ANALYSE.read_bytes()).hexdigest()} ; {len(lignes)} analyses")
    print(f"intervalles de λ identiques à ceux des bancs : "
          f"{sum(bool(l.get('intervalles_identiques_au_banc')) for l in lignes)} sur {len(lignes)}")
    resume = collections.defaultdict(collections.Counter)
    for l in lignes:
        n = len(l.get("reserves_v7") or [])
        lu = l.get("lecture_v7", f"code {l.get('code')}") + (f" ({n} réserve(s))" if n else "")
        resume[(l["banc"], l["scenario"])][(l.get("lecture_v6"), lu)] += 1
    for (banc, nom), c in resume.items():
        print(f"{banc} : {nom}")
        for (v6, v7), n in sorted(c.items()):
            marque = "" if v6 == v7 else "   ← change"
            print(f"  v6 « {v6} » → v7 « {v7} » : {n}{marque}")


if __name__ == "__main__":
    principal()
