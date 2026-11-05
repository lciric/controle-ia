#!/usr/bin/env python3
"""Rejeu du banc de la contre-lecture n° 7 avec l'analyse v8 (lignée « session-depot », 27 octobre 2026 ; CLT-01).
Mêmes scénarios, mêmes graines, même générateur (`fabriquer` et `SCENARIOS` de `banc_cl7.py`, versé et empreinté,
importé tel quel), même nombre de tirages que chaque ligne du banc ; seule l'analyse change (`analyser_echelle_v8.py`
de l'arbre des outils, mode répétition). Contrôle : les intervalles de λ doivent être ceux du banc, à l'arrondi près.
    python -I -B rejouer_banc_cl7_v8.py BANC_CL7_PY ARBRE_ECHELLE_V8 SORTIE_JSONL PROCESSUS BANC_JSONL [BANC_JSONL …]
"""
import hashlib, importlib.util, json, multiprocessing, pathlib, sys, tempfile

BANC = ARBRE = AN = None


def charger(banc_py, arbre):
    global BANC, ARBRE, AN
    s = importlib.util.spec_from_file_location("banc_cl7", banc_py); BANC = importlib.util.module_from_spec(s)
    s.loader.exec_module(BANC)
    ARBRE = pathlib.Path(arbre)
    s = importlib.util.spec_from_file_location("an8", ARBRE / "scripts" / "analyser_echelle_v8.py")
    AN = importlib.util.module_from_spec(s); s.loader.exec_module(AN)


def un(t):
    ligne_banc = t
    nom, g, n_boot = ligne_banc["scenario"], ligne_banc["graine"], ligne_banc.get("n_boot", 300)
    AN.N_BOOT = n_boot
    stim = ARBRE / "stimuli" / "echelle-v2.json"
    st = json.loads(stim.read_text(encoding="utf-8"))["stimuli"]
    a8, a70, o8, o70 = BANC.SCENARIOS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp) / f"{nom}-{g}"
        BANC.fabriquer(base / "p", st, a8, g, **o8)
        BANC.fabriquer(base / "g", st, a70, g + 1, **o70)
        code = AN.principal([str(stim), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v8.json").read_text(encoding="utf-8"))
    out = {"scenario": nom, "graine": g, "n_boot": n_boot,
           "lecture_v7": ligne_banc.get("lecture"), "reserves_v7": ligne_banc.get("reserves"),
           "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
           "reserves": r["reserves"], "issues_tenues": r["issues_tenues_par_sens"],
           "ecart_sens": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
           "ecart_sens_ic": {k: [round(x, 3) for x in v] for k, v in r["ecart_sens_ic"].items()},
           "rapport_Ec": {k: (None if v is None else round(v, 3)) for k, v in r["rapport_Ec"].items()},
           "rapport_Ec_ic": {k: [round(x, 3) for x in v] for k, v in r["rapport_Ec_ic"].items()}}
    ecarts = []
    for s in ("ab", "ba"):
        for m in ("petit", "grand"):
            k = f"lambda_{s}_{m}_ic"
            if k in ligne_banc:
                ecarts.append(max(abs(a - round(b, 3)) for a, b in zip(ligne_banc[k], r[m][s]["lambda_ic"])))
    out["ecart_max_lambda_ic_au_banc"] = max(ecarts) if ecarts else None
    return out


def principal(argv):
    banc_py, arbre, sortie, processus = argv[0], argv[1], pathlib.Path(argv[2]), int(argv[3])
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà (R12)")
    charger(banc_py, arbre)
    lignes = []
    for f in argv[4:]:
        lignes += [json.loads(l) for l in pathlib.Path(f).read_text(encoding="utf-8").splitlines() if l.strip()]
    entete = {"banc_cl7_py_sha256": hashlib.sha256(pathlib.Path(banc_py).read_bytes()).hexdigest(),
              "analyse_sha256": hashlib.sha256((ARBRE / "scripts" / "analyser_echelle_v8.py").read_bytes()).hexdigest(),
              "bancs": {pathlib.Path(f).name: hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest() for f in argv[4:]},
              "analyses": len(lignes)}
    with multiprocessing.get_context("fork").Pool(processus, initializer=charger, initargs=(banc_py, arbre)) as pool, \
            open(sortie, "w", encoding="utf-8") as f:
        f.write(json.dumps({"entete": entete}, ensure_ascii=False) + "\n")
        for x in pool.imap(un, lignes, chunksize=1):
            f.write(json.dumps(x, ensure_ascii=False) + "\n"); f.flush()
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
