"""Banc de la contre-lecture n° 7 (cl7) : analyse v7 du commit b54da1f TELLE QUELLE (mode --repetition, N_BOOT réduit),
sur des activations synthétiques à vérité connue. Générateur `fabriquer` recopié à l'identique de `banc_cl6.py` (cl6,
lui-même repris de cl5) : mêmes tirages, même ordre ; seule l'analyse change.
    python -I -B banc_cl7.py SORTIE_JSONL N_BOOT PROCESSUS NOM:GRAINE0:N [...]"""
import hashlib, json, multiprocessing, pathlib, sys, tempfile, importlib.util
import numpy as np

ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v7")
STIMULI = ARBRE / "stimuli" / "echelle-v2.json"
spec = importlib.util.spec_from_file_location("an7", ARBRE / "scripts" / "analyser_echelle_v7.py")
AN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AN)


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, st, alpha, graine, force_c=4.0, beta=0.0, signature=0.0, signature_b=0.0, kappa=0.0,
              tau=0.4, force_b=1.0, d=64, couches=(4, 6)):
    """Identique à `fabriquer` du banc de cl5 (mêmes tirages, même ordre)."""
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


def T(**k):
    return {"tau": 0.15, "d": 256, **k}


# nom : (alpha petit, alpha grand, options petit, options grand)
SCENARIOS = {
    # témoins
    "d256_H0_egal": (0.5, 0.5, T(), T()),
    "d256_HA": (1.0, 0.2, T(), T()),
    # cl6 rejoué (contrôle de l'outil : même scénario et graines que cl6, analyse v7)
    "d256_H0_croise_oppose_pos_8a_70b": (0.5, 0.5, T(signature=1.3), T(signature_b=-1.3)),
    # (A) classe de cl6, fuite égale, amplitudes et dimension nouvelles
    "A_H0_05_pos_8a_70b_s1.6": (0.5, 0.5, T(signature=1.6), T(signature_b=-1.6)),
    "A_H0_05_pos_8a_70b_s2.0": (0.5, 0.5, T(signature=2.0), T(signature_b=-2.0)),
    "A_H0_07_pos_8a_70b_s1.2": (0.7, 0.7, T(signature=1.2), T(signature_b=-1.2)),
    "A_H0_05_pos_8a_70b_s1.3_d512": (0.5, 0.5, T(signature=1.3, d=512), T(signature_b=-1.3, d=512)),
    # (B) écart vrai sous δ (H_0) et signatures croisées de signes opposés, chacune sous δ en λ
    "B_H0_d020_pos_8a_70b_s0.6": (0.6, 0.4, T(signature=0.6), T(signature_b=-0.6)),
    "B_H0_d020_pos_8a_70b_s0.7": (0.6, 0.4, T(signature=0.7), T(signature_b=-0.7)),
    "B_H0_d015_pos_8a_70b_s0.7": (0.55, 0.4, T(signature=0.7), T(signature_b=-0.7)),
    "B_H0_d020_inv_8a_70b_s0.7": (0.4, 0.6, T(signature=-0.7), T(signature_b=0.7)),
    "B_temoin_d020_sans_signature": (0.6, 0.4, T(), T()),
    # (C) écart vrai au-delà de δ (H_A) et signatures croisées qui le compensent sous δ : « nul » fabriqué ?
    "C_HA_d030_8a_70b_sm0.7": (0.65, 0.35, T(signature=-0.7), T(signature_b=0.7)),
    "C_HA_d030_temoin": (0.65, 0.35, T(), T()),
    # (D) fuite égale (H_0), contexte du jeu b plus faible, signatures croisées de signes opposés (petit : jeu b ;
    # grand : jeu a) : l'asymétrie de contexte compense l'écart de chaque modèle
    "D_H0_07_k075_8b_70a_s1.0": (0.7, 0.7, T(signature_b=1.0, force_b=0.75), T(signature=-1.0, force_b=0.75)),
    "D_H0_07_k075_8b_70a_s0.8": (0.7, 0.7, T(signature_b=0.8, force_b=0.75), T(signature=-0.8, force_b=0.75)),
    "D_H0_07_k075_temoin": (0.7, 0.7, T(force_b=0.75), T(force_b=0.75)),
    "D_H0_07_k075_inv_8a_70b_s1.0": (0.7, 0.7, T(signature=1.0, force_b=0.75), T(signature_b=-1.0, force_b=0.75)),
    # (E) prix sous H_0 : « nul » perdu sous un contexte d'un jeu plus faible
    "E_H0_05_k06": (0.5, 0.5, T(force_b=0.6), T(force_b=0.6)),
    "E_H0_05_k06_d64_t015": (0.5, 0.5, {"tau": 0.15, "force_b": 0.6}, {"tau": 0.15, "force_b": 0.6}),
    "E_H0_09_k08": (0.9, 0.9, T(force_b=0.8), T(force_b=0.8)),
    "E_H0_07_k07": (0.7, 0.7, T(force_b=0.7), T(force_b=0.7)),
    # (B') écart vrai sous δ, signatures plus faibles (chacune sous δ en λ)
    "B_H0_d020_pos_8a_70b_s0.5": (0.6, 0.4, T(signature=0.5), T(signature_b=-0.5)),
    "B_H0_d015_pos_8a_70b_s0.55": (0.55, 0.4, T(signature=0.55), T(signature_b=-0.55)),
    "B_H0_d015_pos_8b_70a_s0.55": (0.55, 0.4, T(signature_b=0.55), T(signature=-0.55)),
    "B_H0_d020_inv_8a_70b_s0.55": (0.4, 0.6, T(signature=-0.55), T(signature_b=0.55)),
    "B_H0_d010_pos_8a_70b_s0.6": (0.5, 0.4, T(signature=0.6), T(signature_b=-0.6)),
    # (C') écart vrai au-delà de δ, compensé sous δ
    "C_HA_d030_8a_70b_sm0.55": (0.65, 0.35, T(signature=-0.55), T(signature_b=0.55)),
    "C_HA_d035_8a_70b_sm0.6": (0.7, 0.35, T(signature=-0.6), T(signature_b=0.6)),
    # (D') asymétrie de contexte et signatures croisées, amplitudes plus fortes
    "D_H0_07_k075_8b_70a_s1.2": (0.7, 0.7, T(signature_b=1.2, force_b=0.75), T(signature=-1.2, force_b=0.75)),
    "D_H0_07_k075_8b_70a_s1.4": (0.7, 0.7, T(signature_b=1.4, force_b=0.75), T(signature=-1.4, force_b=0.75)),
    "D_H0_07_k075_inv_8b_70a_s1.2": (0.7, 0.7, T(signature_b=-1.2, force_b=0.75), T(signature=1.2, force_b=0.75)),
    "D_H0_07_k125_8a_70b_s1.2": (0.7, 0.7, T(signature=1.2, force_b=1.25), T(signature_b=-1.2, force_b=1.25)),
    "D_H0_07_k133_inv_8b_70a_s1.2": (0.7, 0.7, T(signature_b=-1.2, force_b=1.333), T(signature=1.2, force_b=1.333)),
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
        r = json.loads((base / "s" / "analyse-echelle-v7.json").read_text(encoding="utf-8"))
    ligne = {"scenario": nom, "graine": g, "n_boot": n_boot,
             "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
             "reserves": r["reserves"], "lecture_par_sens": r["lecture_par_sens"],
             "issues_tenues": r["issues_tenues_par_sens"], "conditions_manquantes": r["conditions_manquantes"],
             "ecart_sens": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
             "ecart_sens_ic": {k: [round(x, 3) for x in v] for k, v in r["ecart_sens_ic"].items()},
             "couches": {k: r[k]["couche"] for k in ("petit", "grand")}}
    for s in ("ab", "ba"):
        for m in ("petit", "grand"):
            ligne[f"lambda_{s}_{m}"] = round(r[m][s]["lambda"], 3)
            ligne[f"lambda_{s}_{m}_ic"] = [round(x, 3) for x in r[m][s]["lambda_ic"]]
            ligne[f"Afixe_{s}_{m}_bas"] = round(r[m][s]["A_ctx_fixe_ic"][0], 3)
            ligne[f"Ec_{s}_{m}"] = round(r[m][s]["Ec"], 3)
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
    with multiprocessing.get_context("fork").Pool(processus) as pool, open(sortie, "w", encoding="utf-8") as f:
        for ligne in pool.imap(un_travail, travaux, chunksize=1):
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
            f.flush()
            print(json.dumps({k: ligne.get(k) for k in ("scenario", "graine", "lecture", "reserves", "issues_tenues",
                                                       "ecart_sens")}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
