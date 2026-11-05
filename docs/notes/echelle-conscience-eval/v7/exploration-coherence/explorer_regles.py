"""Exploration (non décisive) de trois formes de la cohérence des deux sens (CLU-01) sur des activations synthétiques
(fabriquer des tests v7) : « rencontre » (intervalle de e(m) rencontre [−δ ; δ]), « ponctuel » (|e(m)| ≤ δ),
« inclus » (intervalle de e(m) inclus dans [−δ ; δ]). Une analyse v7 par cas ; les trois règles relues sur sa sortie.
Usage : python -B explorer_regles.py ARBRE_V7 STIMULI SORTIE_JSONL"""
import importlib.util, json, pathlib, sys, tempfile, time, multiprocessing
T = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("t", T / "tests" / "test_analyser_echelle_v7.py")
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
AN = M.AN
AN.N_BOOT = 300; AN.ATTENDUS = M.PETITS; AN.etat_scripts = lambda: (M.COMMIT_ESSAI, True)
STIM = pathlib.Path(sys.argv[2])
D = 0.25
CAS = {}
for s in (0.7, 0.9, 1.1, 1.3):
    CAS[f"H0_pos_8a_70b_{s}_d256"] = (0.5, 0.5, {"signature": s}, {"signature_b": -s}, 256, 0.15)
    CAS[f"H0_inv_8a_70b_{s}_d256"] = (0.5, 0.5, {"signature": -s}, {"signature_b": s}, 256, 0.15)
CAS["HA_d256"] = (1.0, 0.2, {}, {}, 256, 0.15)
CAS["HA_d64_t015"] = (1.0, 0.2, {}, {}, 64, 0.15)
CAS["HA_d64_t04"] = (1.0, 0.2, {}, {}, 64, 0.4)
CAS["HA_ctxb06_d256"] = (1.0, 0.2, {"contexte_b": 0.6}, {"contexte_b": 0.6}, 256, 0.15)
CAS["HA_ctxb08_d256"] = (1.0, 0.2, {"contexte_b": 0.8}, {"contexte_b": 0.8}, 256, 0.15)
CAS["HA_sig_a_neg_8_d256"] = (1.0, 0.2, {"signature": -1.0}, {}, 256, 0.15)
CAS["H0_egal_d256"] = (0.5, 0.5, {}, {}, 256, 0.15)
def un(t):
    nom, g = t
    a8, a70, o8, o70, d, tau = CAS[nom]
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        p = M.fabriquer(tmp / "p", STIM, a8, g, tau=tau, d=d, **o8)
        q = M.fabriquer(tmp / "g", STIM, a70, g + 1, nom="grand", tau=tau, d=d, **o70)
        code, r = M.analyser(tmp, STIM, p, q, repetition=True)
    ten = r["issues_tenues_par_sens"]
    deux = [x for x in ("positif", "inverse", "nul") if x in ten["a→b"] and x in ten["b→a"]]
    e, ei = r["ecart_sens"], r["ecart_sens_ic"]
    regles = {"rencontre": all(ei[k][0] <= D and ei[k][1] >= -D for k in e),
              "ponctuel": all(abs(e[k]) <= D for k in e),
              "inclus": all(-D <= ei[k][0] and ei[k][1] <= D for k in e)}
    return {"cas": nom, "graine": g, "lecture_v7": r["lecture"].removeprefix("répétition, non décisive (").removesuffix(")"),
            "tenues": ten, "deux_sens": deux, "ecart": {k: round(v, 3) for k, v in e.items()},
            "ecart_ic": {k: [round(x, 3) for x in v] for k, v in ei.items()},
            "dl_ic": {s: [round(x, 3) for x in r["delta_lambda_ic"][s]] for s in ("ab", "ba")},
            "prononce_sans_regle": deux[:1], "regles": regles}
if __name__ == "__main__":
    sortie = pathlib.Path(sys.argv[3])
    if sortie.exists(): sys.exit("existe")
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    travaux = [(nom, 900 + 2 * k) for nom in CAS for k in range(n)]
    with multiprocessing.get_context("fork").Pool(3) as pool, open(sortie, "w") as f:
        for x in pool.imap(un, travaux):
            f.write(json.dumps(x, ensure_ascii=False) + "\n"); f.flush()
