"""Largeur de l'intervalle du rapport des Ec (exploration, non décisive) : contextes égaux, × 1,15, × 1,333, × 0,75."""
import importlib.util, json, multiprocessing, pathlib, subprocess, sys, tempfile
ARBRE = pathlib.Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/echelle-v8")
spec = importlib.util.spec_from_file_location("t", ARBRE / "tests/test_analyser_echelle_v8.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
CAS = {"k1": 1.0, "k115": 1.15, "k133": 1.333, "k075": 0.75}
def un(t):
    nom, g = t
    T.AN.N_BOOT = 300
    T.AN.ATTENDUS = {k: {**v, "dimension": 256} for k, v in T.PETITS.items()}
    T.AN.etat_scripts = lambda: (T.COMMIT_ESSAI, True)
    k = CAS[nom]
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d); stim = d / "stim"
        subprocess.run([sys.executable, "-I", "-B", str(ARBRE / "scripts/construire_echelle_v2.py"), str(stim)], check=True, capture_output=True)
        s = stim / "echelle-v2.json"
        p = T.fabriquer(d / "p", s, 0.7, g, d=256, contexte_b=k); q = T.fabriquer(d / "g", s, 0.7, g + 1, nom="grand", d=256, contexte_b=k)
        code, r = T.analyser(d, s, p, q, repetition=True)
    return nom, g, {m: [round(r["rapport_Ec"][m], 3), [round(x, 3) for x in r["rapport_Ec_ic"][m]]] for m in ("petit", "grand")}
if __name__ == "__main__":
    with multiprocessing.get_context("fork").Pool(3) as pool:
        for x in pool.imap(un, [(n, g) for n in CAS for g in (2000, 2002, 2004)]):
            print(json.dumps(x), flush=True)
