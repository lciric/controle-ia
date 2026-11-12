"""Ligne `CODE-T07` de l'étape A — v1 (fichier neuf, R12 ; DS-3 bis accordée par Lazar, option (a), R-2104 ; brouillon 19, « Lignes de
registre », ligne `CODE-T07` : « chemin d'un fichier scellé qui porte le commit et les sha256 du module `src/controle_ia/t07/`
contre-lu et répété en jouet, et sha256 de ce fichier »).

Avec `code_t07_exige` vrai, la garde d'ouverture de l'étape A exige la ligne (`lecture_v2.ouvrir` ; absente → refus, code 2), en
vérifie le sceau et l'antériorité stricte à l'ouverture (`registre_v1.verifier_lignes`), puis, ici :

1. **forme du fichier cité** (JSON) : `{"commit": "<40 caractères hexadécimaux>", "fichiers": {"src/controle_ia/t07/<nom>.py":
   "<sha256>", …}}` ; tout autre chemin, empreinte mal formée, liste vide → refus ;
2. **antériorité à la première ouverture** : la ligne est datée strictement avant la **première** ligne `OUVERTURE-T07` de
   l'étape A de ce run au journal (relance comprise) ; une correction du code après une ouverture ne s'inscrit donc plus ;
3. **égalité à l'arbre exécuté** : dans le dépôt git qui porte le module **effectivement importé** (`dossier_du_module`), le commit
   cité existe et est la tête ou un de ses ancêtres (commit de scellement descendant du commit du code, comme la voie B de T0.6) ;
   les fichiers `*.py` de `src/controle_ia/t07/` au commit cité sont exactement ceux de la liste, chacun à l'empreinte écrite ; les
   fichiers du dossier importé sont les mêmes, aux mêmes empreintes (aucun fichier en plus, en moins ou changé) ; **DF-02** : tout
   `src/controle_ia/` de l'arbre exécuté (paquets importés compris) est égal au commit cité (`git diff` vide) et l'arbre de travail
   n'y porte aucun fichier modifié ni ajouté (`git status`). Sinon refus.

Contrôle joué par la garde de l'étape A **et de l'étape B** (`code_t07_exige` vrai : ligne exigée aux deux), par la passe à blanc
et avant le repli (DF-02).

Le contrôle ne lit que le dépôt du code et le fichier cité ; il n'ouvre rien de la course.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

from . import registre_v1 as rg

PREFIXE = "src/controle_ia/t07/"
COMMIT = re.compile(r"[0-9a-f]{40}")


def dossier_du_module() -> Path:
    return Path(__file__).resolve().parent


def _git(depot: Path, *args: str) -> tuple[int, str]:
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def _sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def _refus_arbre(statut: str) -> rg.RefusRegistre:
    lignes = statut.strip().splitlines()
    return rg.RefusRegistre(f"CODE-T07 : arbre de travail modifié sous src/controle_ia/ ({len(lignes)} entrée(s), première : "
                            f"{lignes[0].strip()[:120]!r})")


def lire_fichier_code(chemin: Path) -> dict:
    try:
        d = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise rg.RefusRegistre(f"CODE-T07 : fichier {chemin} illisible ({type(e).__name__})") from None
    if not isinstance(d, dict) or set(d) != {"commit", "fichiers"} or not isinstance(d["commit"], str) \
            or not COMMIT.fullmatch(d["commit"]) or not isinstance(d["fichiers"], dict) or not d["fichiers"]:
        raise rg.RefusRegistre('CODE-T07 : forme {"commit": <40 hexadécimaux>, "fichiers": {chemin: sha256}} attendue')
    for p, s in d["fichiers"].items():
        if not (isinstance(p, str) and p.startswith(PREFIXE) and p.endswith(".py") and "/" not in p[len(PREFIXE):]) \
                or not (isinstance(s, str) and rg.SHA.fullmatch(s)):
            raise rg.RefusRegistre(f"CODE-T07 : entrée {p!r} : chemin {PREFIXE}<nom>.py et empreinte sha256 attendus")
    return d


def controler_code(racine: Path, entree: dict, premiere_ouverture: int | None, dossier_code: Path | None = None) -> dict:
    """Contrôles 1 à 3 (docstring du module) ; `entree` : ligne vérifiée par `verifier_lignes` (chemin, instant, date). Rend le
    rapport ; tout défaut → `RefusRegistre` (refus de la garde, code 2)."""
    d = lire_fichier_code(Path(racine) / entree["chemin"])
    if premiere_ouverture is not None and not int(entree["instant"]) < int(premiere_ouverture):
        raise rg.RefusRegistre(f"CODE-T07 datée {entree['date']}, pas strictement antérieure à la première ouverture de l'étape A "
                               f"({rg.date_utc(premiere_ouverture)}) : refus")
    dossier = Path(dossier_code) if dossier_code is not None else dossier_du_module()
    c, top = _git(dossier, "rev-parse", "--show-toplevel")
    if c != 0:
        raise rg.RefusRegistre(f"CODE-T07 : le module importé ({dossier}) n'est pas dans un dépôt git : arbre non vérifiable")
    depot = Path(top.strip())
    _, tete = _git(depot, "rev-parse", "HEAD")
    tete = tete.strip()
    commit = d["commit"]
    if _git(depot, "cat-file", "-e", f"{commit}^{{commit}}")[0] != 0:
        raise rg.RefusRegistre(f"CODE-T07 : commit cité {commit[:12]}… absent du dépôt du module")
    if _git(depot, "merge-base", "--is-ancestor", commit, tete)[0] != 0:
        raise rg.RefusRegistre(f"CODE-T07 : commit cité {commit[:12]}… ni la tête ({tete[:12]}…) ni un de ses ancêtres")
    _, liste = _git(depot, "ls-tree", "--name-only", commit, "--", PREFIXE)
    au_commit = {p for p in liste.splitlines() if p.endswith(".py") and "/" not in p[len(PREFIXE):]}
    ecrits = set(d["fichiers"])
    if au_commit != ecrits:
        raise rg.RefusRegistre(f"CODE-T07 : fichiers du module au commit cité ≠ liste écrite (en plus au commit : "
                               f"{sorted(au_commit - ecrits)[:5]} ; absents du commit : {sorted(ecrits - au_commit)[:5]})")
    importes = {PREFIXE + f.name for f in dossier.glob("*.py")}
    if importes != ecrits:
        raise rg.RefusRegistre(f"CODE-T07 : fichiers du module importé ≠ liste écrite (en plus : {sorted(importes - ecrits)[:5]} ; "
                               f"absents : {sorted(ecrits - importes)[:5]})")
    # DF-02 : les paquets importés aussi (`sondes`, `harnais`, `premier_test_ia`, `manifeste`, `t06`, `organismes`…) : tout
    # `src/controle_ia/` de l'arbre exécuté égal au commit cité, aucun fichier modifié ni ajouté
    if _git(depot, "diff", "--quiet", commit, "--", "src/controle_ia")[0] != 0:
        raise rg.RefusRegistre(f"CODE-T07 : src/controle_ia/ de l'arbre exécuté ≠ commit cité {commit[:12]}… (paquets importés compris)")
    _, statut = _git(depot, "status", "--porcelain", "--untracked-files=all", "--", "src/controle_ia")
    if statut.strip():
        raise _refus_arbre(statut)
    ecarts = []
    for p, s in sorted(d["fichiers"].items()):
        blob = subprocess.run(["git", "-C", str(depot), "show", f"{commit}:{p}"], capture_output=True).stdout
        if _sha(blob) != s:
            ecarts.append(f"{p} au commit cité")
        if _sha((dossier / Path(p).name).read_bytes()) != s:
            ecarts.append(f"{p} dans l'arbre exécuté")
    if ecarts:
        raise rg.RefusRegistre(f"CODE-T07 : empreintes différentes de la liste écrite : {ecarts[:6]}")
    return {"commit": commit, "tete_du_depot": tete, "fichiers": len(ecrits), "date_ligne": entree["date"],
            "verifie": "commit ancêtre de la tête ; fichiers du module au commit et dans l'arbre importé égaux à la liste ; ligne "
                       "antérieure à la première ouverture de l'étape A"}


def ecrire_fichier_code(depot: Path, commit: str, sortie: Path) -> Path:
    """Aide (session mère, essais) : écrit le fichier de `CODE-T07` pour `commit` du dépôt `depot` (fichiers `*.py` de
    `src/controle_ia/t07/` au commit, empreintes du contenu au commit). Le scellement (`.sha256`) et la ligne restent à faire."""
    _, liste = _git(Path(depot), "ls-tree", "--name-only", commit, "--", PREFIXE)
    fichiers = {}
    for p in sorted(x for x in liste.splitlines() if x.endswith(".py") and "/" not in x[len(PREFIXE):]):
        fichiers[p] = _sha(subprocess.run(["git", "-C", str(depot), "show", f"{commit}:{p}"], capture_output=True, check=True).stdout)
    if not fichiers:
        raise rg.RefusRegistre(f"aucun fichier {PREFIXE}*.py au commit {commit}")
    sortie = Path(sortie)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(json.dumps({"commit": commit, "fichiers": fichiers}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return sortie


def main(argv: list[str]) -> int:
    """`python -m controle_ia.t07.code_t07_v1 ecrire DEPOT COMMIT SORTIE` : écrit le fichier de `CODE-T07` (aide de la session mère) ;
    `… verifier RACINE REGISTRE` : rejoue, avant toute ouverture, le contrôle de la garde (ligne présente, sceau, commit et
    empreintes égaux à l'arbre du module importé) ; code 0 conforme, 2 refus (motif imprimé). Rien n'est écrit."""
    import sys
    if len(argv) == 3 and argv[0] == "verifier":
        from .lecture_v2 import lire_lignes_actuelles
        try:
            l = lire_lignes_actuelles(Path(argv[2]), (rg.CODE_T07,)).get(rg.CODE_T07)
            if l is None:
                raise rg.RefusRegistre("CODE-T07 : ligne absente du registre")
            rg.sceau_conforme(Path(argv[1]) / l["chemin"], l["sha256"])
            r = controler_code(Path(argv[1]), l, None)
        except rg.RefusRegistre as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 2
        print(f"CODE-T07 conforme : commit {r['commit']}, {r['fichiers']} fichiers, tête du dépôt {r['tete_du_depot']}")
        return 0
    if len(argv) != 4 or argv[0] != "ecrire":
        print("usage : python -m controle_ia.t07.code_t07_v1 ecrire DEPOT COMMIT SORTIE | verifier RACINE REGISTRE", file=sys.stderr)
        return 2
    c, plein = _git(Path(argv[1]), "rev-parse", "--verify", f"{argv[2]}^{{commit}}")
    if c != 0:
        print(f"REFUS : commit {argv[2]!r} introuvable", file=sys.stderr)
        return 2
    try:
        p = ecrire_fichier_code(Path(argv[1]), plein.strip(), Path(argv[3]))
    except (rg.RefusRegistre, OSError, subprocess.CalledProcessError) as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    print(f"{p} : commit {plein.strip()}, {len(json.loads(p.read_text(encoding='utf-8'))['fichiers'])} fichiers (à sceller, puis ligne CODE-T07)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv[1:]))
