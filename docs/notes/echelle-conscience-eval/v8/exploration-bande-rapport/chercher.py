"""Recherche de graines pour les tests d'intégration v8 (voisins de cl7) : générateur des tests, analyse v8."""
import importlib.util, json, multiprocessing, pathlib, subprocess, sys, tempfile
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
spec = importlib.util.spec_from_file_location("t", ARBRE / "tests/test_analyser_echelle_v8.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
CAS = {
    "B_pos": (0.6, 0.4, {"signature": 0.6}, {"signature_b": -0.6}),
    "B_inv": (0.4, 0.6, {"signature": -0.6}, {"signature_b": 0.6}),
    "D_k133": (0.7, 0.7, {"signature_b": -1.2, "contexte_b": 1.333}, {"signature": 1.2, "contexte_b": 1.333}),
}
def un(t):
    nom, g = t
    T.AN.N_BOOT = 300
    T.AN.ATTENDUS = {k: {**v, "dimension": 256} for k, v in T.PETITS.items()}
    T.AN.etat_scripts = lambda: (T.COMMIT_ESSAI, True)
    a8, a70, o8, o70 = CAS[nom]
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        stim = d / "stim"
        subprocess.run([sys.executable, "-I", "-B", str(ARBRE / "scripts/construire_echelle_v2.py"), str(stim)], check=True, capture_output=True)
        s = stim / "echelle-v2.json"
        p = T.fabriquer(d / "p", s, a8, g, d=256, **o8); q = T.fabriquer(d / "g", s, a70, g + 1, nom="grand", d=256, **o70)
        code, r = T.analyser(d, s, p, q, repetition=True)
    if code != 0: return nom, g, "arrêt"
    return nom, g, r["lecture"], [x[:45] for x in r["reserves"]], {k: round(v, 3) for k, v in r["ecart_sens"].items()}, r["rapport_Ec"]
if __name__ == "__main__":
    travaux = [(n, g) for n in CAS for g in range(1000, 1024, 2)]
    with multiprocessing.get_context("fork").Pool(3) as pool:
        for x in pool.imap(un, travaux):
            print(json.dumps(x, ensure_ascii=False), flush=True)
