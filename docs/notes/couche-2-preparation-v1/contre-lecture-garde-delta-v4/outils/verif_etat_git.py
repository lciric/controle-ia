"""GD3-04 : `etat_git` de la v4 contre des réponses de git simulées (aucun dépôt créé : subprocess.run est remplacé)."""
import importlib.util, json, subprocess, types
C = "/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/relecture-garde-delta-v4/cl"
spec = importlib.util.spec_from_file_location("sim4", f"{C}/outils/copie_script/sim_garde_v4.py")
sim = importlib.util.module_from_spec(spec); spec.loader.exec_module(sim)
R = lambda out, rc: types.SimpleNamespace(stdout=out, returncode=rc)
cas = {
 "hors dépôt": {"rev-parse": R("", 128), "status": R("", 128), "ls-files": R("", 128)},
 "dépôt sans commit (HEAD non né)": {"rev-parse": R("HEAD\n", 128), "status": R("?? s.py\n", 0), "ls-files": R("", 1)},
 "dépôt refusé (propriétaire douteux)": {"rev-parse": R("", 128), "status": R("", 128), "ls-files": R("", 128)},
 "non suivi": {"rev-parse": R("abc123\n", 0), "status": R("?? s.py\n", 0), "ls-files": R("", 1)},
 "ignoré": {"rev-parse": R("abc123\n", 0), "status": R("", 0), "ls-files": R("", 1)},
 "suivi propre": {"rev-parse": R("abc123\n", 0), "status": R("", 0), "ls-files": R("s.py\n", 0)},
 "suivi modifié": {"rev-parse": R("abc123\n", 0), "status": R(" M s.py\n", 0), "ls-files": R("s.py\n", 0)},
 "status en échec, suivi": {"rev-parse": R("abc123\n", 0), "status": R("", 128), "ls-files": R("s.py\n", 0)},
}
res = {}
for nom, rep in cas.items():
    def faux(args, **kw):
        return rep["rev-parse" if "rev-parse" in args else "status" if "status" in args else "ls-files"]
    sim.subprocess.run = faux
    res[nom] = sim.etat_git("/x/s.py")
    print(f"{nom:40s} -> {res[nom]}")
json.dump(res, open(f"{C}/sorties/verif_etat_git.json", "w"), indent=1, ensure_ascii=False)
