"""[v5 : STRICT sur le code de sortie de pytest — une mutation n'est « tuée » que par le code 1 (essais échoués) ; le code 5 (aucun essai sélectionné par `-k`) invalide le banc au lieu de compter la mutation comme tuée (réserve de la contre-lecture de la v11 v2) ; 2, 3 et 4 sont des erreurs] [v4 : plus M12 (tolérance retombée à 0,15), M13 (borne exclue), M14 (lecture stricte retirée : tolérance appliquée aussi au bit) ; M11 mute 0,3] [v3 : les mutations M1 à M11 de la v2 plus X3, X5, X6, X7, X8, X9 de la contre-lecture R-1746 (5 mutations sur 10 survivaient à la v2)] Banc de mutations du bras B v3 (contre-lecture R-1731 : « au moins les 5 mutations survivantes de la v1 »). Chaque mutation remplace UN texte exact du module
`bras_b_v4.py` (copie dans un arbre jetable, jamais le dépôt) ; l'essai visé doit ÉCHOUER. Sortie : une ligne par mutation, code de retour 1 si une mutation survit.

    python3 -I scripts/banc_mutations_bras_b_v5.py [--liste]
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
MODULE = "src/controle_ia/audit_fuite_r1_v4/bras_b_v4.py"
FICHIER_ESSAIS = "tests/test_bras_b_v4.py"
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
    ("M11 tolérance de score élargie à 5", "TOLERANCE_SCORE = 0.3 ", "TOLERANCE_SCORE = 5.0 ", "test_g4_"),
    ("M12 tolérance retombée à 0,15", "TOLERANCE_SCORE = 0.3 ", "TOLERANCE_SCORE = 0.15 ", "test_v4_"),
    ("M13 borne de la tolérance exclue (< au lieu de ≤)", "ok = ecart <= TOLERANCE_SCORE", "ok = ecart < TOLERANCE_SCORE", "test_v4_"),
    ("M14 lecture stricte retirée (tolérance aussi sur la même carte)", "    if au_bit:\n        ok = egal\n    else:", "    if False:\n        ok = egal\n    else:", "test_v4_"),
    ("X3 a_SC_H calculée contre la mention", 'res["aires"]["a_SC_H"] = audit.aire(sx, d, sc, H, graine())', 'res["aires"]["a_SC_H"] = audit.aire(sx, d, sc, M, graine())', "test_x3_"),
    ("X5 G7 retirée (classe vide)", "if sc.sum() == 0 or H.sum() == 0 or M.sum() == 0:", "if False:", "test_x5_"),
    ("X6 contrefactuels de la mention rangés chez le saboteur", '(el_cf_s if x0["condition"] == "saboteur" else el_cf_m)[r] = True', '(el_cf_m if x0["condition"] == "saboteur" else el_cf_s)[r] = True', "test_x6_"),
    ("X7 seuil de fuite strict (< au lieu de ≤)", 'fuite = a_sc_m["haut"] <= SEUIL_FUITE_HAUT', 'fuite = a_sc_m["haut"] < SEUIL_FUITE_HAUT', "test_x7_x8_"),
    ("X8 signatures simultanées rendues comme fuite", 'issue = "non tranché (signatures simultanées)"', 'issue = "fuite"', "test_x7_x8_"),
    ("X9 seuil de lecture strict (> au lieu de ≥)", 'lecture = a_sc_h["bas"] >= SEUIL_LECTURE_BAS', 'lecture = a_sc_h["bas"] > SEUIL_LECTURE_BAS', "test_x7_x8_"),
    ("X10 mention contrefactuelle écartée des comptes", 'res = {"comptes": {"saboteur_contrefactuel": int(sc.sum()), "mention_contrefactuelle": int(mc.sum())', 'res = {"comptes": {"saboteur_contrefactuel": int(sc.sum()), "mention_contrefactuelle": 0', "test_x6_"),
    ("M8 mention contrefactuelle prise pour le saboteur", "sc = el_cf_s & S", "sc = el_cf_m & M", "test_3_"),
]


def classer(code: int) -> str:
    """Code de sortie de pytest → verdict du banc. 0 : tous les essais passent (mutation SURVIVANTE) ; 1 : des essais échouent (TUÉE) ; 5 : aucun essai sélectionné (banc INVALIDE) ; autre : erreur de pytest."""
    return {0: "survivante", 1: "tuee", 5: "invalide"}.get(code, "erreur")


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
        verdict = classer(r.returncode)
        if verdict in ("invalide", "erreur"):
            print(f"BANC INVALIDE ({verdict}, code {r.returncode}) {nom} : le filtre -k {cible!r} ne sélectionne aucun essai ou pytest a échoué autrement\n{r.stdout[-600:]}")
            return 2
        print(("TUÉE      " if verdict == "tuee" else "SURVIVANTE") + " " + nom + f" (essai visé : {cible}*)")
        if verdict != "tuee":
            survivantes.append(nom)
    print(f"{len(MUTATIONS) - len(survivantes)} mutations tuées sur {len(MUTATIONS)} (témoin non muté réussi)")
    return 1 if survivantes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
