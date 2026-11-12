"""Banc synthétique de la contre-lecture cl3 : appelle `analyser_echelle_v3.py` TEL QUEL (mode --repetition, N_BOOT
réduit) sur des activations synthétiques à vérité connue. Générateur repris de `test_analyser_echelle_v3.py::fabriquer`,
étendu :
  - signature   : poussée du format le long de la signature (moyenne des particularités) du jeu a (signe libre) ;
  - signature_b : idem pour le jeu b ;
  - force_b     : facteur de force du contexte sur les stimuli du jeu b (1 = comme a) ;
  - kappa       : hétérogénéité de la force des paires.
Usage : python -I -B banc_v4.py NOM_SCENARIO GRAINE_DEPART N_REPETITIONS N_BOOT SORTIE_JSONL
"""
import hashlib
import importlib.util
import json
import pathlib
import sys
import tempfile

import numpy as np

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/echelle-v3")
STIMULI = ARBRE / "stimuli" / "echelle-v2.json"
spec = importlib.util.spec_from_file_location("an", ARBRE / "scripts" / "analyser_echelle_v3.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, st, alpha, graine, force_c=4.0, beta=0.0, signature=0.0, signature_b=0.0, kappa=0.0,
              tau=0.4, force_b=1.0, d=64, couches=(4, 6)):
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


# nom : (alpha petit, alpha grand, options petit, options grand)
SCENARIOS = {
    # CLY-01 rejoué : signature a positive au petit, aucun concept
    "sig_a_pos": (0.0, 0.0, {"signature": 2.0}, {}),
    # signature a NÉGATIVE au petit, aucun concept : « fuite de signe inverse » fabriquée ?
    "sig_a_neg": (0.0, 0.0, {"signature": -2.0}, {}),
    "sig_a_neg_faible": (0.0, 0.0, {"signature": -1.0}, {}),
    # signature a négative au grand
    "sig_a_neg_grand": (0.0, 0.0, {}, {"signature": -2.0}),
    # masquage : H_A vraie (1,0 ; 0,2), signature a négative au petit qui ramène λ_ab(petit) vers λ(grand)
    "masque_HA": (1.0, 0.2, {"signature": -0.9}, {}),
    "masque_HA2": (0.6, 0.0, {"signature": -0.6}, {}),
    "masque_HA_fort": (1.0, 0.2, {"signature": -2.0}, {}),
    "masque_HA_fort2": (1.0, 0.2, {"signature": -2.4}, {}),
    "masque_pasdefuite": (0.6, 0.0, {"signature": -1.4}, {}),
    "masque_HA_fort_t015": (1.0, 0.2, {"signature": -2.0, "tau": 0.15}, {"tau": 0.15}),
    "masque_pasdefuite_t015": (0.6, 0.0, {"signature": -1.4, "tau": 0.15}, {"tau": 0.15}),
    "sig_a_neg_t015": (0.0, 0.0, {"signature": -1.0, "tau": 0.15}, {"tau": 0.15}),
    # forces de paires inégales, fuite spécifique (CLY-02 rejoué)
    "HA_kappa": (1.0, 0.1, {"kappa": 0.5}, {"kappa": 0.5}),
    # signature du jeu b seul au petit : a→b propre
    "sig_b_pos": (0.0, 0.0, {"signature_b": 2.0}, {}),
    # signatures des deux jeux au petit : faux positif possible malgré le contrôle symétrique
    "sig_ab_pos": (0.0, 0.0, {"signature": 2.0, "signature_b": 2.0}, {}),
    # contexte plus faible sur le jeu b (aux deux tailles) sous H_A vraie
    "HA_force_b_faible": (1.0, 0.2, {"force_b": 0.4}, {"force_b": 0.4}),
    # contexte plus faible sur le jeu b au petit seulement, aucune fuite
    "rien_force_b_petit": (0.0, 0.0, {"force_b": 0.4}, {}),
    # témoin : H_A pure
    "HA": (1.0, 0.2, {}, {}),
}


def principal(argv):
    nom, graine0, n_rep, n_boot, sortie = argv[0], int(argv[1]), int(argv[2]), int(argv[3]), pathlib.Path(argv[4])
    AN.N_BOOT = n_boot
    st = json.loads(STIMULI.read_text(encoding="utf-8"))["stimuli"]
    a8, a70, o8, o70 = SCENARIOS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        for k in range(n_rep):
            g = graine0 + 2 * k
            base = tmp / f"{nom}-{g}"
            fabriquer(base / "p", st, a8, g, **o8)
            fabriquer(base / "g", st, a70, g + 1, **o70)
            code = AN.principal([str(STIMULI), str(base / "p"), str(base / "g"), str(g), str(base / "s"),
                                 "--repetition"])
            if code != 0:
                ligne = {"scenario": nom, "graine": g, "code": code}
            else:
                r = json.loads((base / "s" / "analyse-echelle-v3.json").read_text(encoding="utf-8"))
                ligne = {"scenario": nom, "graine": g,
                         "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
                         "reserves": r["reserves"]}
                for s in ("ab", "ba"):
                    for m in ("petit", "grand"):
                        ligne[f"lambda_{s}_{m}"] = round(r[m][s]["lambda"], 3)
                        ligne[f"lambda_{s}_{m}_ic"] = [round(x, 3) for x in r[m][s]["lambda_ic"]]
                        ligne[f"Afixe_{s}_{m}_bas"] = round(r[m][s]["A_ctx_fixe_ic"][0], 3)
                        ligne[f"nu_{s}_{m}"] = round(r[m][s]["nu"], 3)
                    ligne[f"dl_{s}_ic"] = [round(x, 3) for x in r["delta_lambda_ic"][s]]
                    ligne[f"spec_{s}_ic"] = [round(x, 3) for x in r["specificite_ic"][s]]
            with open(sortie, "a", encoding="utf-8") as f:
                f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
            print(json.dumps({k2: ligne.get(k2) for k2 in ("scenario", "graine", "lecture", "reserves", "lambda_ab_petit",
                                                            "lambda_ba_petit", "dl_ab_ic", "dl_ba_ic")},
                             ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
