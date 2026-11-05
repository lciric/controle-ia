"""cl6 : surveillance v6 (script du commit, telle quelle) avec PAS_S=abc dans l'environnement : que devient la boucle ?"""
import importlib.util, json, pathlib, sys
spec = importlib.util.spec_from_file_location("lat", pathlib.Path(__file__).parent / "latence_reelle_v6.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
base = pathlib.Path(sys.argv[1]); base.mkdir(parents=True)
L.cas(base, "e-pas-s-illisible", 0, 20, {"PAS_S": "abc"})
d = base / "e-pas-s-illisible"
print("arret.txt :", (d / "s" / "arret.txt").read_text() if (d / "s" / "arret.txt").exists() else "absent")
print("arrêts demandés :", (d / "arrets").read_text().split() if (d / "arrets").exists() else [])
