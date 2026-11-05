"""Contre-lecture v3, artefacts complémentaires (entrées synthétiques seulement).
  S1 une sonde non principale renommée (enjeux-attention-c23 → enjeux-attention-c11) : 16 sondes, mauvais ensemble ;
  C1 copie du script avec N_ISO_MAX = 15 (garde des constantes) ;
  N1 fichier de poids des sondes d'un autre jeu (empreinte ≠ sondes_legeres_sha256 du JSON).
Usage : python -I -B artefacts_cl_v3_b.py --dossier <neuf> --essai <essai_factice_comparaison_jlens_v3.py>
"""
import argparse, importlib.util, json, subprocess, sys
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("--dossier", required=True); ap.add_argument("--essai", required=True)
a = ap.parse_args()
D = Path(a.dossier).resolve()
if D.exists():
    sys.exit(f"{D} existe déjà")
spec = importlib.util.spec_from_file_location("essai_v3", a.essai)
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
e, s, alt = D / "entrees", D / "sortie", D / "altere"
concepts = json.loads(E.CONCEPTS.read_text(encoding="utf-8"))
com = E.construire_commun(e, concepts)
code = E.code_du_depot(Path(a.essai).resolve().parents[5])
plan_A = {"tromperie-lineaire-c7": "J", "enjeux-attention-c7": "sortie", "enjeux-difference_moyennes-c15": "sortie",
          "tromperie-attention-c15": "J", "tromperie-difference_moyennes-c23": "sortie"}
pl_A = {"tromperie": "concentre", "enjeux": "alea"}
E.ecrire_jeu(e / "A-sain", code, com, plan_A, pl_A, "cl-A")
E.ecrire_jeu(e / "S1", code, com, plan_A, pl_A, "cl-S1", retirer=("enjeux-attention-c23",), ajouter=("enjeux-attention-c11",))
alt.mkdir(); s.mkdir()
t = E.SCRIPT.read_text(encoding="utf-8")
assert t.count("N_ISO_MAX = 14 ") == 1
C1 = alt / "C1" / E.SCRIPT.name; C1.parent.mkdir(); C1.write_text(t.replace("N_ISO_MAX = 14 ", "N_ISO_MAX = 15 "), encoding="utf-8")
m = e / "modele"
def base(jeu, sortie, npz=None):
    j = e / jeu
    return ["comparer", "--sondes", "non-principales-lineaires", "--sondes-json", str(j / "sondes-figees.json"),
            "--sondes-npz", str(npz or j / "sondes-figees-legeres.npz"), "--lentille", str(e / "lentille-factice.npz"),
            "--lentille-config", str(e / "lentille-config.yaml"),
            "--desembedding", f"{m / 'model.safetensors.index.json'}:lm_head.weight",
            "--norme-finale", f"{m / 'model.safetensors.index.json'}:model.norm.weight",
            "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(E.CONCEPTS), "--enonce-regle", str(E.ENONCE),
            "--empreintes-attendues", str(e / "empreintes-entrees-factices.txt"), "--essai-factice", "--sortie", str(s / sortie)]
for nom, sc, args in (("S1 sonde non principale renommée", E.SCRIPT, base("S1", "S1.json")),
                      ("C1 N_ISO_MAX = 15", C1, base("A-sain", "C1.json")),
                      ("N1 poids des sondes d'un autre jeu", E.SCRIPT, base("A-sain", "N1.json", e / "S1" / "sondes-figees-legeres.npz"))):
    r = subprocess.run([sys.executable, "-I", "-B", str(sc), *args], capture_output=True, text=True)
    out = Path(args[args.index("--sortie") + 1])
    print(f"[{nom}] code {r.returncode} ; sortie écrite : {out.exists()}\n    {(r.stderr.strip().splitlines() or [''])[-1][:240]}")
