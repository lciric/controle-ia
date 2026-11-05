"""Banc de la contre-lecture n° 8 : générateur `fabriquer` de `simuler_atteignabilite_v8.py` (commit 9ccc383, importé
tel quel) et analyse `analyser_echelle_v8.py` TELLE QUELLE (mode répétition, 300 tirages), sur des activations
synthétiques à vérité connue. Une ligne JSON par analyse.
    python -I -B banc_cl8.py SORTIE_JSONL PROCESSUS SCENARIO:GRAINE0:N [...]"""
import importlib.util, json, multiprocessing, pathlib, sys, tempfile
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
spec = importlib.util.spec_from_file_location("sim8", ARBRE / "scripts" / "simuler_atteignabilite_v8.py")
SIM = importlib.util.module_from_spec(spec); spec.loader.exec_module(SIM)
AN = SIM.AN
STIM = ARBRE / "stimuli" / "echelle-v2.json"

def O(**k):
    return k
# nom : (alpha petit, alpha grand, options petit, options grand, tau)
SC = {}
# (1) rapport des Ec et hétérogénéité des cadrages : fuite égale 0,7, contextes k
for tau, dim in ((0.15, 256), (0.4, 256), (0.4, 64), (0.8, 64)):
    for k in (1.0, 1.15, 1.25, 1.333, 0.75):
        SC[f"Q_t{tau}_d{dim}_k{k}"] = (0.7, 0.7, O(contexte_b=k, d=dim), O(contexte_b=k, d=dim), tau)
# (2) famille B au voisinage du seuil : écart vrai 0,2 à 0,24 (H_0), signatures croisées plus petites, dimensions 64 et 256
for (a8, a70) in ((0.6, 0.4), (0.62, 0.4), (0.64, 0.4)):
    for s in (0.3, 0.4, 0.5):
        SC[f"B_{a8}_{a70}_s{s}_d256"] = (a8, a70, O(signature=s, d=256), O(signature_b=-s, d=256), 0.15)
    SC[f"Binv_{a70}_{a8}_s0.4_d256"] = (a70, a8, O(signature=-0.4, d=256), O(signature_b=0.4, d=256), 0.15)
for s in (1.0, 1.4, 1.8):     # dimension 64 : |s_jeu| plus petit, signature plus forte pour le même λ
    SC[f"B_0.6_0.4_s{s}_d64"] = (0.6, 0.4, O(signature=s, d=64), O(signature_b=-s, d=64), 0.15)
# (3) famille D, hétérogénéité plus forte : fuite égale forte, contexte d'un jeu plus fort, signatures croisées
for tau, dim, sigs in ((0.4, 256, (0.3, 0.45)), (0.8, 64, (0.3, 0.45)), (0.4, 64, (0.6, 0.9))):
    for k in (1.25, 1.333):
        for s in sigs:
            SC[f"D_t{tau}_d{dim}_k{k}_s{s}"] = (0.9, 0.9, O(signature_b=-s, contexte_b=k, d=dim),
                                                 O(signature=s, contexte_b=k, d=dim), tau)
# (4) famille D à tau 0,15 et contexte dans la bande (k 1,12) : seule la réserve « λ change » peut voir
for s in (0.8, 1.0):
    SC[f"D_t0.15_d256_k1.12_s{s}"] = (0.9, 0.9, O(signature_b=-s, contexte_b=1.12, d=256),
                                       O(signature=s, contexte_b=1.12, d=256), 0.15)
# (5) famille C (H_A compensé) en dimension 64
for s in (1.4, 1.8):
    SC[f"C_0.65_0.35_sm{s}_d64"] = (0.65, 0.35, O(signature=-s, d=64), O(signature_b=s, d=64), 0.15)

def un(t):
    nom, g = t
    AN.N_BOOT = 300
    a8, a70, o8, o70, tau = SC[nom]
    st = json.loads(STIM.read_text(encoding="utf-8"))["stimuli"]
    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)
        SIM.fabriquer(base / "p", STIM, st, a8, g, tau, **o8)
        SIM.fabriquer(base / "g", STIM, st, a70, g + 1, tau, **o70)
        code = AN.principal([str(STIM), str(base / "p"), str(base / "g"), str(g), str(base / "s"), "--repetition"])
        if code != 0:
            return {"scenario": nom, "graine": g, "code": code}
        r = json.loads((base / "s" / "analyse-echelle-v8.json").read_text(encoding="utf-8"))
    v8 = [x for x in r["reserves"] if x.startswith(("le λ du", "jeux de force"))]
    out = {"scenario": nom, "graine": g, "lecture": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
           "reserves_v8": [x[:48] for x in v8], "autres_reserves": [x[:40] for x in r["reserves"] if x not in v8],
           "lecture_par_sens": r["lecture_par_sens"], "issues_tenues": r["issues_tenues_par_sens"],
           "e": {k: round(v, 3) for k, v in r["ecart_sens"].items()},
           "e_ic": {k: [round(x, 3) for x in v] for k, v in r["ecart_sens_ic"].items()},
           "q": {k: (None if v is None else round(v, 3)) for k, v in r["rapport_Ec"].items()},
           "q_ic": {k: [round(x, 3) for x in v] for k, v in r["rapport_Ec_ic"].items()},
           "couches": {k: r[k]["couche"] for k in ("petit", "grand")}}
    for s in ("ab", "ba"):
        out[f"dl_{s}"] = [round(x, 3) for x in r["delta_lambda_ic"][s]]
        out[f"cert_{s}"] = [round(r[m][s]["A_ctx_fixe_ic"][0], 3) for m in ("petit", "grand")]
        out[f"transfert_{s}"] = [round(r[m][s]["transfert"], 3) for m in ("petit", "grand")]
        out[f"lambda_{s}"] = [round(r[m][s]["lambda"], 3) for m in ("petit", "grand")]
    return out

def principal(argv):
    sortie, processus = pathlib.Path(argv[0]), int(argv[1])
    if sortie.exists():
        sys.exit("sortie présente")
    travaux = []
    for x in argv[2:]:
        motif, g0, n = x.split(":")
        noms = [k for k in SC if k.startswith(motif)] if motif.endswith("*") is False and motif not in SC else [motif]
        if motif.endswith("*"):
            noms = [k for k in SC if k.startswith(motif[:-1])]
        for i, nom in enumerate(noms):
            travaux += [(nom, int(g0) + 1000 * i + 2 * j) for j in range(int(n))]
    with multiprocessing.get_context("fork").Pool(processus) as pool, open(sortie, "w", encoding="utf-8") as f:
        for ligne in pool.imap(un, travaux, chunksize=1):
            f.write(json.dumps(ligne, ensure_ascii=False) + "\n"); f.flush()
    return 0

if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
