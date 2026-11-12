"""Banc synthétique de la contre-lecture n° 5 (cl5) : appelle `analyser_echelle_v5.py` TEL QUEL (mode --repetition,
N_BOOT réduit) sur des activations synthétiques à vérité connue. Générateur repris à l'identique de celui de cl4
(`docs/notes/echelle-conscience-eval/v5/contre-lecture-cl4/scripts/banc_v5.py`, lui-même repris de cl3), pour que les
cas rejoués aux mêmes graines donnent les mêmes activations que dans les bancs de cl4 (analyse v4) ; seuls changent
l'analyse appelée (v5) et le nom de sa sortie. Scénarios nouveaux : signatures d'un seul jeu à chacune des deux tailles,
de jeux différents (« croisées »).
Usage : python -I -B banc_cl5.py SORTIE_JSONL N_BOOT PROCESSUS NOM:GRAINE0:N [NOM:GRAINE0:N ...]
"""
import hashlib
import importlib.util
import json
import multiprocessing
import pathlib
import sys
import tempfile

import numpy as np

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v5")
STIMULI = ARBRE / "stimuli" / "echelle-v2.json"
spec = importlib.util.spec_from_file_location("an", ARBRE / "scripts" / "analyser_echelle_v5.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, st, alpha, graine, force_c=4.0, beta=0.0, signature=0.0, signature_b=0.0, kappa=0.0,
              tau=0.4, force_b=1.0, d=64, couches=(4, 6)):
    """Identique à `fabriquer` du banc de cl4 (mêmes tirages, même ordre)."""
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 4)))[0].T
    C, Fp = base[0] * force_c, base[2] * 2.0
    contenus = rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        cle = (s["jeu"], s["paire"], s["classe"])
        if cle not in cadrage:
            cadrage[cle] = rng.normal(size=d) * tau
    kap = {(j, p): 1.0 + kappa * rng.normal() for j in ("a", "b") for p in range(6)}
    diffs = [cadrage[("a", j, "eval")] - cadrage[("a", j, "reel")] for j in range(6)]
    diffs_b = [cadrage[("b", j, "eval")] - cadrage[("b", j, "reel")] for j in range(6)]
    signes = rng.choice([-1.0, 1.0], size=6)
    gen = sum(sg * dj for sg, dj in zip(signes, diffs))
    gen = gen / np.linalg.norm(gen) * force_c
    sig = sum(diffs) / 6
    sig = sig / np.linalg.norm(sig) * force_c
    sig_b = sum(diffs_b) / 6
    sig_b = sig_b / np.linalg.norm(sig_b) * force_c
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True)
    ids, sorties = [s["id"] for s in st], {}
    bruit = rng.normal(size=(len(st), d))
    for k, c in enumerate(couches):
        ech = 0.5 if k == 0 else 1.0
        F = alpha * C * ech + Fp + beta * gen + signature * sig + signature_b * sig_b
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = 0.5 if s["classe"] == "eval" else -0.5
            fb = force_b if s["jeu"] == "b" else 1.0
            X[i] = contenus[s["contenu"]] + sf * F + sc * fb * kap[(s["jeu"], s["paire"])] * C * ech \
                + cadrage[(s["jeu"], s["paire"], s["classe"])] + bruit[i]
        f = dossier / f"activations-L{c}.npy"
        np.save(f, X.astype(np.float16))
        sceller(f)
        sorties[f.name] = sha(f)
    f_ids = dossier / "ids.json"
    f_ids.write_text(json.dumps(ids) + "\n", encoding="utf-8")
    sceller(f_ids)
    sorties["ids.json"] = sha(f_ids)
    m = {"modele": "synthetique", "revision": None, "couches": list(couches), "dimension": d,
         "type_nombre": "bfloat16", "limite": None, "sha256_stimuli": sha(STIMULI), "rendu_premier": "<gabarit>",
         "dernier_jeton": "<fin>", "sha256_sorties": sorties}
    (dossier / "manifeste-mesure.json").write_text(json.dumps(m), encoding="utf-8")
    sceller(dossier / "manifeste-mesure.json")
    return dossier


# nom : (alpha petit, alpha grand, options petit, options grand) ; les six premiers : scénarios de cl4, mêmes graines
SCENARIOS = {
    "faible_egal_t015": (0.2, 0.2, {"tau": 0.15}, {"tau": 0.15}),
    "faible_forceb06_t015": (0.15, 0.15, {"tau": 0.15, "force_b": 0.6}, {"tau": 0.15, "force_b": 0.6}),
    "sig_ab_neg": (0.0, 0.0, {"signature": -2.0, "signature_b": -2.0}, {}),
    "sig_ab_grand": (0.0, 0.0, {}, {"signature": 2.0, "signature_b": 2.0}),
    "sig_a_neg": (0.0, 0.0, {"signature": -2.0}, {}),
    "masque_double_t015": (1.0, 0.2, {"signature": -2.0, "signature_b": -2.0, "tau": 0.15}, {"tau": 0.15}),
    # cas nouveaux (cl5) : signature négative d'un seul jeu à chaque taille, jeux différents ; aucun concept
    "croise_neg_8a_70b": (0.0, 0.0, {"signature": -2.0}, {"signature_b": -2.0}),
    "croise_neg_8b_70a": (0.0, 0.0, {"signature_b": -2.0}, {"signature": -2.0}),
    "croise_pos_8a_70b": (0.0, 0.0, {"signature": 2.0}, {"signature_b": 2.0}),
    # masquage d'un écart vrai par la double signature, au tau 0,4 (CLW-02 : « peut masquer un écart vrai »)
    "masque_double_t04": (1.0, 0.2, {"signature": -2.0, "signature_b": -2.0}, {}),
}


def un_travail(t):
    nom, g, n_boot = t
    AN.N_BOOT = n_boot
    st = json.loads(STIMULI.read_text(encoding="utf-8"))["stimuli"]
    a8, a70, o8, o70 = SCENARIOS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp) / f"{nom}-{g}"
        fabriquer(base / "p", st, a8, g, **o8)
        fabriquer(base / "g", st, a70, g + 1, **o70)
        code = AN.principal([str(STIMULI), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v5.json").read_text(encoding="utf-8"))
    ligne = {"scenario": nom, "graine": g,
             "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
             "reserves": r["reserves"], "lecture_par_sens": r["lecture_par_sens"],
             "issues_tenues": r["issues_tenues_par_sens"], "conditions_manquantes": r["conditions_manquantes"],
             "couches": {k: r[k]["couche"] for k in ("petit", "grand")}}
    for s in ("ab", "ba"):
        for m in ("petit", "grand"):
            ligne[f"lambda_{s}_{m}"] = round(r[m][s]["lambda"], 3)
            ligne[f"lambda_{s}_{m}_ic"] = [round(x, 3) for x in r[m][s]["lambda_ic"]]
            ligne[f"Afixe_{s}_{m}_bas"] = round(r[m][s]["A_ctx_fixe_ic"][0], 3)
            ligne[f"nu_{s}_{m}"] = round(r[m][s]["nu"], 3)
            ligne[f"ssi_{s}_{m}_ic"] = [round(x, 3) for x in r["specificite_signe_inverse_ic"][m][s]]
        ligne[f"dl_{s}_ic"] = [round(x, 3) for x in r["delta_lambda_ic"][s]]
        ligne[f"spec_{s}_ic"] = [round(x, 3) for x in r["specificite_ic"][s]]
    return ligne


def principal(argv):
    sortie, n_boot, processus = pathlib.Path(argv[0]), int(argv[1]), int(argv[2])
    if sortie.exists():
        sys.exit(f"{sortie} existe déjà")
    travaux = []
    for spec_ in argv[3:]:
        nom, g0, n = spec_.split(":")
        travaux += [(nom, int(g0) + 2 * k, n_boot) for k in range(int(n))]
    with multiprocessing.get_context("fork").Pool(processus) as pool:
        lignes = pool.map(un_travail, travaux, chunksize=1)
    with open(sortie, "w", encoding="utf-8") as f:
        for ligne in lignes:
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    for ligne in lignes:
        print(json.dumps({k: ligne.get(k) for k in ("scenario", "graine", "lecture", "reserves", "issues_tenues")},
                         ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
