"""Banc de mutations du bras B v2 (contre-lecture R-1731 : « au moins les 5 mutations survivantes de la v1 »). Chaque mutation remplace UN texte exact du module
`bras_b_v2.py` (copie dans un arbre jetable, jamais le dépôt) ; l'essai visé doit ÉCHOUER. Sortie : une ligne par mutation, code de retour 1 si une mutation survit.

    python3 -I scripts/banc_mutations_bras_b_v2.py [--liste]
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
MODULE = "src/controle_ia/audit_fuite_r1_v4/bras_b_v2.py"
FICHIER_ESSAIS = "tests/test_bras_b_v2.py"
# (nom, ancien, nouveau, essai visé)
MUTATIONS = [
    ("M1 substitution par la même condition", 'CONDITION_DE_REMPLACEMENT = {"saboteur": "mention", "mention": "saboteur"}',
     'CONDITION_DE_REMPLACEMENT = {"saboteur": "saboteur", "mention": "mention"}', "test_1_substitution_reelle"),
    ("M2 pli non tenu à l'écart", "tr = apprend & (pli != k)", "tr = apprend", "test_2_modele_du_pli"),
    ("M3 pli décalé dans le score contrefactuel", "return float(noter(modeles[int(pli[ligne])], x))",
     "return float(noter(modeles[max(modeles)], x))", "test_2_modele_du_pli"),
    ("M4 a_SC_M contre l'honnête", 'res["aires"]["a_SC_M"] = audit.aire(sx, d, sc, M, graine())', 'res["aires"]["a_SC_M"] = audit.aire(sx, d, sc, H, graine())', "test_3_decalage"),
    ("M5 scores d'origine au lieu des contrefactuels", "sx = np.where(sc, s_cf, s_orig)", "sx = s_orig", "test_3_"),
    ("M6 restriction de contexte retirée", "return el & contexte_conforme", "return el", "test_4_"),
    ("M7 issue imprimée", 'print(json.dumps({"sortie": str(sortie), "sha256": empreinte(sortie), "duree_s": r["duree_s"]}, ensure_ascii=False))',
     'print(json.dumps({"issue": r["decision"]["issue"], "sortie": str(sortie), "sha256": empreinte(sortie), "duree_s": r["duree_s"]}, ensure_ascii=False))', "test_5_aucune_issue"),
    ("M9 tolérance du score retirée (G4 hors bit)", "ok = ecart <= TOLERANCE_SCORE", "ok = True", "test_g4_"),
    ("M10 identité au bit non exigée (G4)", "    if au_bit:\n        ok = egal", "    if au_bit:\n        ok = True", "test_g4_"),
    ("M11 tolérance de score élargie à 5", "TOLERANCE_SCORE = 0.15 ", "TOLERANCE_SCORE = 5.0 ", "test_g4_"),
    ("M8 mention contrefactuelle prise pour le saboteur", "sc = el_cf_s & S", "sc = el_cf_m & M", "test_3_"),
]


def main(argv: list[str]) -> int:
    if "--liste" in argv:
        for n, a, b, k in MUTATIONS:
            print(n, "->", k)
        return 0
    survivantes = []
    for nom, ancien, nouveau, cible in [("M0 témoin non muté (doit RÉUSSIR : sinon le banc ne prouve rien)", None, None, "")] + MUTATIONS:
        texte = (RACINE / MODULE).read_text(encoding="utf-8")
        if ancien is not None and texte.count(ancien) != 1:
            print(f"ERREUR {nom} : texte à muter trouvé {texte.count(ancien)} fois")
            return 2
        with tempfile.TemporaryDirectory(prefix="mutation-bras-b-") as t:
            arbre = Path(t) / "depot"
            shutil.copytree(RACINE / "src", arbre / "src", ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copytree(RACINE / "tests", arbre / "tests", ignore=shutil.ignore_patterns("__pycache__"))
            for entree in RACINE.iterdir():                                       # tout le reste du dépôt par liens (docs, prereg, scripts, …) : seuls src/ et tests/ sont copiés
                if entree.name not in ("src", "tests", ".git", ".venv", "__pycache__", ".pytest_cache") and not (arbre / entree.name).exists():
                    (arbre / entree.name).symlink_to(entree)
            (arbre / MODULE).write_text(texte if ancien is None else texte.replace(ancien, nouveau), encoding="utf-8")
            env = {**os.environ, "PYTHONPATH": str(arbre / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
            r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", FICHIER_ESSAIS, *(["-k", cible.removeprefix("test_")] if cible else [])], cwd=arbre,
                               env=env, capture_output=True, text=True, timeout=900)
        if ancien is None:
            print(("TÉMOIN OK " if r.returncode == 0 else "TÉMOIN EN ÉCHEC (banc invalide) ") + nom)
            if r.returncode != 0:
                print(r.stdout[-1500:])
                return 2
            continue
        tuee = r.returncode != 0
        print(("TUÉE      " if tuee else "SURVIVANTE") + " " + nom + f" (essai visé : {cible}*)")
        if not tuee:
            survivantes.append(nom)
    print(f"{len(MUTATIONS) - len(survivantes)} mutations tuées sur {len(MUTATIONS)} (témoin non muté réussi)")
    return 1 if survivantes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
