"""CL8 : interruption entre la création de SORTIE et l'écriture du manifeste de départ (fenêtre étroite du cœur).
Usage : python3 -B lanceur_fenetre.py ARBRE -- ARGS DU LANCEUR…  (moteur simulé ; contrôles Claude gratuits)
`manifeste(phase="depart")` lève KeyboardInterrupt une fois (après os.makedirs(sortie))."""
import importlib.util, os, sys
arbre = sys.argv[1]
reste = sys.argv[3:]
sys.path.insert(0, arbre)
spec = importlib.util.spec_from_file_location("ideation_v1_lanceur", os.path.join(arbre, "demonstrations", "ideation_v1.py"))
lanceur = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lanceur)
idn = lanceur.idn
orig = idn.manifeste
def manifeste(**k):
    if k.get("phase") == "depart" and os.environ.get("CL8_FENETRE") == "1":
        raise KeyboardInterrupt("signal 15 (simulé entre makedirs et manifeste de départ)")
    return orig(**k)
idn.manifeste = manifeste
raise SystemExit(lanceur.principal(reste))
