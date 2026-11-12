"""Banc cl8, générateur dérivé : `fabriquer` de la simulation v8 (copie, mêmes tirages pour une même graine), plus une
composante COMMUNE aux cadrages « eval » de toutes les paires d'un jeu (norme `commun_a` ou `commun_b`, direction
aléatoire tirée d'un générateur à part), comme une asymétrie lexicale propre à un jeu (« how » 4 contre 0 dans a).
Analyse v8 du commit TELLE QUELLE (mode répétition, 300 tirages).
    python -I -B banc_cl8_commun.py SORTIE_JSONL PROCESSUS SCENARIO:GRAINE0:N [...]"""
import importlib.util, json, multiprocessing, pathlib, sys, tempfile
import numpy as np
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
spec = importlib.util.spec_from_file_location("sim8", ARBRE / "scripts" / "simuler_atteignabilite_v8.py")
SIM = importlib.util.module_from_spec(spec); spec.loader.exec_module(SIM)
AN = SIM.AN
STIM = ARBRE / "stimuli" / "echelle-v2.json"

def fabriquer(dossier, stimuli, st, alpha, graine, tau, force_c=4.0, signature=0.0, signature_b=0.0, contexte_b=1.0,
              d=64, commun_a=0.0, commun_b=0.0):
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 3)))[0].T
    C, Fp = base[0] * force_c, base[1] * 2.0
    contenus = rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        k = (s["jeu"], s["paire"], s["classe"])
        if k not in cadrage:
            cadrage[k] = rng.normal(size=d) * tau
    r2 = np.random.default_rng(graine + 777777)               # composante commune : générateur à part
    for jeu, norme in (("a", commun_a), ("b", commun_b)):
        if norme:
            z = r2.normal(size=d); z -= (z @ base[0]) * base[0]; z = z / np.linalg.norm(z) * norme
            for j in range(6):
                cadrage[(jeu, j, "eval")] = cadrage[(jeu, j, "eval")] + z
    sig = {}
    for jeu in ("a", "b"):
        v = sum(cadrage[(jeu, j, "eval")] - cadrage[(jeu, j, "reel")] for j in range(6)) / 6
        sig[jeu] = v / np.linalg.norm(v) * 4.0
    dossier.mkdir(parents=True)
    bruit = rng.normal(size=(len(st), d))
    sorties = {}
    for c in (4, 6):
        ech = 0.5 if c == 4 else 1.0
        F = alpha * C * ech + Fp + signature * sig["a"] + signature_b * sig["b"]
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = 0.5 if s["classe"] == "eval" else -0.5
            kb = contexte_b if s["jeu"] == "b" else 1.0
            X[i] = contenus[s["contenu"]] + sf * F + sc * kb * C * ech + cadrage[(s["jeu"], s["paire"], s["classe"])] + bruit[i]
        f = dossier / f"activations-L{c}.npy"
        np.save(f, X.astype(np.float16)); SIM.sceller(f); sorties[f.name] = SIM.sha(f)
    f = dossier / "ids.json"
    f.write_text(json.dumps([s["id"] for s in st]) + "\n", encoding="utf-8"); SIM.sceller(f); sorties["ids.json"] = SIM.sha(f)
    m = {"modele": "synthetique", "revision": None, "couches": [4, 6], "dimension": d, "type_nombre": "bfloat16",
         "limite": None, "sha256_stimuli": SIM.sha(stimuli), "rendu_premier": "<gabarit>", "dernier_jeton": "<fin>",
         "sha256_sorties": sorties}
    (dossier / "manifeste-mesure.json").write_text(json.dumps(m), encoding="utf-8"); SIM.sceller(dossier / "manifeste-mesure.json")

def O(**k): return {"d": 256, **k}
SC = {
    # contrôle : sans composante commune, ce générateur rend les activations de la simulation (même graine)
    "Z_controle_k1": (0.7, 0.7, O(), O(), 0.15),
    # rapport des Ec sous une composante commune au jeu a, contextes égaux ou inégaux, fuite égale (H_0)
    "Z_ca3_k1": (0.7, 0.7, O(commun_a=3.0), O(commun_a=3.0), 0.15),
    "Z_ca3_k1.25": (0.7, 0.7, O(commun_a=3.0, contexte_b=1.25), O(commun_a=3.0, contexte_b=1.25), 0.15),
    "Z_ca4_k1.4": (1.0, 1.0, O(commun_a=4.0, contexte_b=1.4), O(commun_a=4.0, contexte_b=1.4), 0.15),
    "Z_cb3_k1": (0.7, 0.7, O(commun_b=3.0), O(commun_b=3.0), 0.15),
    # famille D sous composante commune : fuite égale forte (1,0), contexte du jeu b × 1,4, signatures croisées
    "ZD_ca4_k1.4_s": (1.0, 1.0, O(commun_a=4.0, contexte_b=1.4, signature_b=-1.6),
                      O(commun_a=4.0, contexte_b=1.4, signature=0.55), 0.15),
    "ZD_ca4_k1.4_s2": (1.0, 1.0, O(commun_a=4.0, contexte_b=1.4, signature_b=-1.9),
                       O(commun_a=4.0, contexte_b=1.4, signature=0.65), 0.15),
    # miroir « positif » : jeu b +au petit, jeu a −au grand
    "ZD_ca4_k1.4_pos": (1.0, 1.0, O(commun_a=4.0, contexte_b=1.4, signature=0.65),
                        O(commun_a=4.0, contexte_b=1.4, signature_b=-1.9), 0.15),
}

def un(t):
    nom, g = t
    AN.N_BOOT = 300
    a8, a70, o8, o70, tau = SC[nom]
    st = json.loads(STIM.read_text(encoding="utf-8"))["stimuli"]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        fabriquer(base / "p", STIM, st, a8, g, tau, **o8)
        fabriquer(base / "g", STIM, st, a70, g + 1, tau, **o70)
        if nom == "Z_controle_k1":           # contrôle d'identité avec le générateur de la simulation
            SIM.fabriquer(base / "p0", STIM, st, a8, g, tau, **o8)
            ident = all((base / "p" / f).read_bytes() == (base / "p0" / f).read_bytes() for f in ("activations-L4.npy", "activations-L6.npy"))
        else:
            ident = None
        code = AN.principal([str(STIM), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v8.json").read_text(encoding="utf-8"))
    v8 = [x for x in r["reserves"] if x.startswith(("le λ du", "jeux de force"))]
    out = {"scenario": nom, "graine": g, "identique_simulation": ident,
           "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
           "reserves_v8": [x[:48] for x in v8], "autres_reserves": [x[:40] for x in r["reserves"] if x not in v8],
           "lecture_par_sens": r["lecture_par_sens"], "issues_tenues": r["issues_tenues_par_sens"],
           "e": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
           "e_ic": {k: [round(x, 3) for x in v] for k, v in r["ecart_sens_ic"].items()},
           "q": {k: (None if v is None else round(v, 3)) for k, v in r["rapport_Ec"].items()},
           "couches": {k: r[k]["couche"] for k in ("petit", "grand")}}
    for s in ("ab", "ba"):
        out[f"dl_{s}"] = [round(x, 3) for x in r["delta_lambda_ic"][s]]
        out[f"cert_{s}"] = [round(r[m][s]["A_ctx_fixe_ic"][0], 3) for m in ("petit", "grand")]
        out[f"transfert_{s}"] = [round(r[m][s]["transfert"], 3) for m in ("petit", "grand")]
        out[f"lambda_{s}"] = [round(r[m][s]["lambda"], 3) for m in ("petit", "grand")]
        out[f"spec_{s}"] = [round(x, 3) for x in r["specificite_ic"][s]]
    return out

def principal(argv):
    sortie, processus = pathlib.Path(argv[0]), int(argv[1])
    if sortie.exists(): sys.exit("sortie présente")
    travaux = []
    for x in argv[2:]:
        nom, g0, n = x.split(":")
        travaux += [(nom, int(g0) + 2 * j) for j in range(int(n))]
    with multiprocessing.get_context("fork").Pool(processus) as pool, open(sortie, "w", encoding="utf-8") as f:
        for ligne in pool.imap(un, travaux, chunksize=1):
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n"); f.flush()
    return 0

if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
