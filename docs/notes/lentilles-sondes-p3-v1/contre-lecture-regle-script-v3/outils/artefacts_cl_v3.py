"""Contre-lecture v3 : artefacts ajoutés à l'essai factice (entrées synthétiques seulement, aucune entrée réelle).

Réutilise les fonctions de l'essai factice v3 (construire_commun, code_du_depot, ecrire_jeu) pour fabriquer :
  G1 copie du script avec GRAINE = 20261030 (seule modification) ;
  G2 copie du script avec ETIQUETTE_ISOTROPES = "isotropes-v2/c{couche}" ;
  P1 principale enjeux-lineaire-c15 renommée enjeux-lineairebis-c15, principales du fichier inchangées ;
  P2 la même, principales du fichier mises à jour sur le nouveau nom ;
  F1 --essai-factice sur un jeu au run réel simulé (20261019-230011-p3-reel) ;
  H1 planchers de « tromperie » à la couche 14 au lieu de 15 ;
  Z1 copie du script où le score z « direct » est décalé de 1e-3 (garde des scores z sur un artefact).
Usage : python -I -B artefacts_cl_v3.py --dossier <neuf> --essai <essai_factice_comparaison_jlens_v3.py>
"""
import argparse, importlib.util, inspect, json, subprocess, sys, hashlib
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("--dossier", required=True); ap.add_argument("--essai", required=True)
a = ap.parse_args()
D = Path(a.dossier).resolve()
if D.exists():
    sys.exit(f"{D} existe déjà")
spec = importlib.util.spec_from_file_location("essai_v3", a.essai)
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
SCRIPT = E.SCRIPT
e, s, alt = D / "entrees", D / "sortie", D / "altere"
concepts = json.loads(E.CONCEPTS.read_text(encoding="utf-8"))
com = E.construire_commun(e, concepts)
code = E.code_du_depot(Path(a.essai).resolve().parents[5])
plan_A = {"tromperie-lineaire-c7": "J", "enjeux-attention-c7": "sortie", "enjeux-difference_moyennes-c15": "sortie",
          "tromperie-attention-c15": "J", "tromperie-difference_moyennes-c23": "sortie"}
pl_A = {"tromperie": "concentre", "enjeux": "alea"}
E.ecrire_jeu(e / "A-sain", code, com, plan_A, pl_A, "essai-factice-jlens-v3-A")
E.ecrire_jeu(e / "P1", code, com, plan_A, pl_A, "cl-P1", retirer=("enjeux-lineaire-c15",), ajouter=("enjeux-lineairebis-c15",))
E.ecrire_jeu(e / "P2", code, com, plan_A, pl_A, "cl-P2", princ={"tromperie": E.PRINC["tromperie"], "enjeux": "enjeux-lineairebis-c15"},
             retirer=("enjeux-lineaire-c15",), ajouter=("enjeux-lineairebis-c15",))
E.ecrire_jeu(e / "F1", code, com, plan_A, pl_A, E.RUN_REEL)
# H1 : planchers à la couche 14 (copie de ecrire_jeu, deux remplacements contrôlés)
src = inspect.getsource(E.ecrire_jeu)
a1 = 's = S(nom, 15, "max", w, 0.0, None, "plancher")'
a2 = '"couche": 15,\n                                 "empreinte": s.empreinte(), "famille": "plancher"'
assert src.count(a1) == 1 and src.count(a2) == 1
src = src.replace(a1, 's = S(nom, 14 if concept == "tromperie" else 15, "max", w, 0.0, None, "plancher")')
src = src.replace(a2, '"couche": 14 if concept == "tromperie" else 15,\n                                 "empreinte": s.empreinte(), "famille": "plancher"')
esp = dict(E.__dict__); exec(compile(src, "ecrire_jeu_h1", "exec"), esp)
esp["ecrire_jeu"](e / "H1", code, com, plan_A, pl_A, "cl-H1")
alt.mkdir(); s.mkdir()
texte = SCRIPT.read_text(encoding="utf-8")
def copie(nom, avant, apres):
    assert texte.count(avant) == 1, avant
    p = alt / nom / SCRIPT.name; p.parent.mkdir()
    p.write_text(texte.replace(avant, apres), encoding="utf-8"); return p
G1 = copie("G1", "GRAINE = 20261029 ", "GRAINE = 20261030 ")
G2 = copie("G2", 'ETIQUETTE_ISOTROPES = "isotropes-v3/c{couche}"', 'ETIQUETTE_ISOTROPES = "isotropes-v2/c{couche}"')
Z1 = copie("Z1", "z_direct = float((lg[ids].mean() - lg.mean()) / lg.std())",
           "z_direct = float((lg[ids].mean() - lg.mean()) / lg.std()) + 1e-3")
m = e / "modele"
def base(jeu, sortie, factice=True):
    j = e / jeu
    return (["comparer", "--sondes", "non-principales-lineaires", "--sondes-json", str(j / "sondes-figees.json"),
             "--sondes-npz", str(j / "sondes-figees-legeres.npz"), "--lentille", str(e / "lentille-factice.npz"),
             "--lentille-config", str(e / "lentille-config.yaml"),
             "--desembedding", f"{m / 'model.safetensors.index.json'}:lm_head.weight",
             "--norme-finale", f"{m / 'model.safetensors.index.json'}:model.norm.weight",
             "--vocabulaire", str(m / "tokenizer.json"), "--concepts", str(E.CONCEPTS), "--enonce-regle", str(E.ENONCE),
             "--empreintes-attendues", str(e / "empreintes-entrees-factices.txt"), "--sortie", str(s / sortie)]
            + (["--essai-factice"] if factice else []))
cas = [("A témoin (script livré)", SCRIPT, base("A-sain", "A.json"), 0, None),
       ("G1 graine 20261030", G1, base("A-sain", "G1.json"), 2, None),
       ("G2 étiquette isotropes-v2", G2, base("A-sain", "G2.json"), 2, None),
       ("P1 principale renommée, principales inchangées", SCRIPT, base("P1", "P1.json"), 2, None),
       ("P2 principale renommée, principales mises à jour", SCRIPT, base("P2", "P2.json"), 2, None),
       ("F1 --essai-factice sur run réel simulé", SCRIPT, base("F1", "F1.json"), 2, None),
       ("H1 planchers tromperie à la couche 14", SCRIPT, base("H1", "H1.json"), 2, None),
       ("Z1 score z direct décalé de 1e-3", Z1, base("A-sain", "Z1.json"), 2, None)]
lignes = []
for nom, sc, args, attendu, _ in cas:
    r = subprocess.run([sys.executable, "-I", "-B", str(sc), *args], capture_output=True, text=True)
    sortie = Path(args[args.index("--sortie") + 1])
    det = (r.stderr.strip().splitlines() or [""])[-1][:260]
    extra = ""
    if r.returncode == 0:
        o = json.loads(sortie.read_text(encoding="utf-8"))
        rp = o["regle_primaire"]
        coh = sorted(f"{c['sonde']}/{c['lentille']}" for c in rp["cases"] if c["verdict"] == "cohérent")
        niso = {f"{c['sonde']}/{c['lentille']}": c["n_iso"] for c in rp["cases"] if c["S"] >= 2}
        man = json.loads(sortie.with_name(sortie.stem + "-manifeste.json").read_text(encoding="utf-8"))
        gr = {k: v for k, v in man["graines"].items() if k != "mode"}
        extra = (f" | X J={rp['verdict_ensemble']['jacobienne']['X']} L={rp['verdict_ensemble']['logits']['X']} ;"
                 f" cohérentes {coh} ; n_iso (S≥2) {niso} ; essai_factice={o['essai_factice']} ; run={o['run_sondes']} ;"
                 f" graines manifeste {json.dumps(gr)[:200]}")
    verdict = "REFUSÉ" if r.returncode == 2 else ("ACCEPTÉ" if r.returncode == 0 else f"code {r.returncode}")
    conforme = "attendu" if r.returncode == attendu else "NON attendu"
    lignes.append(f"[{nom}] code {r.returncode} → {verdict} ({conforme} : {attendu}) ; sortie écrite : {sortie.exists()}"
                  f"\n    {det}{extra}")
print("\n".join(lignes))
