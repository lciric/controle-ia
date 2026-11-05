"""Essai de `etat_scripts()` réel (non remplacé par un faux) sur un clone jetable du commit c08a5b2 :
propre ; __pycache__ ignoré ; fichier non suivi dans echelle-v3 ; script modifié."""
import importlib.util, pathlib, subprocess, sys
CL = pathlib.Path(sys.argv[1])
def etat():
    spec = importlib.util.spec_from_file_location("an", CL / "echelle-v3/scripts/analyser_echelle_v3.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.etat_scripts()
print("propre :", etat())
(CL / "echelle-v3/scripts/__pycache__").mkdir(exist_ok=True)
(CL / "echelle-v3/scripts/__pycache__/x.pyc").write_bytes(b"x")
print("avec __pycache__ :", etat())
(CL / "echelle-v3/resultats-locaux").mkdir()
(CL / "echelle-v3/resultats-locaux/a.json").write_text("{}")
print("fichier non suivi dans echelle-v3 :", etat())
(CL / "echelle-v3/resultats-locaux/a.json").unlink(); (CL / "echelle-v3/resultats-locaux").rmdir()
p = CL / "echelle-v3/scripts/analyser_echelle_v3.py"
t = p.read_text(); p.write_text(t.replace('"delta": 0.25', '"delta": 0.20'))
print("script modifié :", etat())
subprocess.run(["git", "-C", str(CL), "checkout", "-q", "--", "echelle-v3/scripts/analyser_echelle_v3.py"])
(CL / "autre-dossier").mkdir(); (CL / "autre-dossier/b.txt").write_text("x")
print("fichier non suivi hors de echelle-v3 :", etat())
