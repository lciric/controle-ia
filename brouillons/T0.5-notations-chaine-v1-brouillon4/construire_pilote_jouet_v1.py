"""Pilote jouet arrêté pendant ses notations décisives, et préenregistrement jouet des notations refaites, pour la
répétition jouet de la chaîne des notations (N-021, option (a)) ; v1.

Dans le dépôt jetable DEPOT (au commit du code relu C, arbre propre) :
1. tâches jouet (deux tâches des tests du pilote, cibles de test), scellées, ajoutées de force (donnees/ est ignoré) ;
2. pilote jouet joué par le vrai lanceur du pilote (`lancer_pilote_a.executer`, mode jouet, sans préenregistrement),
   comme le fabriquent les tests (`tests/test_noter_pilote_a.py`, `_pilote_arrete`) : ensembles rendus non vides et
   notations arrêtées à l'échéance, donc arrêt consigné à l'étape « notations decisives par jouet-8B », épisodes et
   appariement écrits, aucune notation ;
3. configuration jouet des notations (paramètres des juges recopiés du manifeste du pilote jouet), scellée, au chemin
   réel `prereg/T0.5-pilote-notations-config-v1.json` ;
4. préenregistrement jouet au chemin réel `prereg/T0.5-pilote-notations-v1.md` : le candidat relu CANDIDAT, dont
   chaque citation lue par le script de l'instance, par le lanceur et par la récupération est remplacée par sa valeur
   jouet ; chaque remplacement doit toucher exactement une ligne (le texte relu est ainsi éprouvé : citations uniques) ;
   scellé par `sceller_prereg` (problemes() vide).
Deux commits (tâches et pilote ; configuration et préenregistrement). Écrit sur la sortie standard un JSON : commit,
run du pilote jouet, empreintes. Ne touche à rien hors de DEPOT ; aucun réseau.
Usage : construire_pilote_jouet_v1.py DEPOT CANDIDAT TESTS_ATTENDUS
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


def git(depot: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True, text=True).stdout.strip()


def remplacer_une_fois(texte: str, motif: str, valeur: str) -> str:
    """Remplace la valeur entre accents graves après l'intitulé `motif` ; exactement une occurrence de l'intitulé."""
    rx = re.compile(rf"({re.escape(motif)} : `)([^`]*)(`)")
    n = len(rx.findall(texte))
    if n != 1:
        raise SystemExit(f"intitulé « {motif} » trouvé {n} fois dans le candidat (une seule attendue)")
    return rx.sub(lambda m: m.group(1) + valeur + m.group(3), texte)


def main(argv: list[str]) -> int:
    depot, candidat, tests = Path(argv[1]).resolve(), Path(argv[2]).resolve(), int(argv[3])
    sys.path[:0] = [str(depot / "src"), str(depot / "tests")]
    from controle_ia.environnements import lancer_pilote_a as lp
    from controle_ia.environnements import noter_pilote_a as npa
    from controle_ia.environnements.lancer_pilote_a import empreinte_config
    from controle_ia.gardes import GardeArret
    from controle_ia.prereg import sceller_prereg
    from controle_ia.scellement import empreinte, sceller
    from test_pilote_a import CIBLES_TEST, TACHES, _config_lanceur

    if git(depot, "status", "--porcelain"):
        raise SystemExit("dépôt jetable non propre")
    code = git(depot, "rev-parse", "HEAD")
    pilote = "20261012-100000-t05-pilote-jouet"
    f_taches = depot / "donnees" / "t05-notations-jouet" / "taches-jouet-2-v1.json"
    f_taches.parent.mkdir(parents=True, exist_ok=True)
    f_taches.write_text(json.dumps({"taches": [dict(t, cibles=CIBLES_TEST) for t in TACHES]}, ensure_ascii=False),
                        encoding="utf-8")
    sha_taches = sceller(f_taches)
    git(depot, "add", "-f", str(f_taches), str(f_taches) + ".sha256")
    git(depot, "commit", "-qm", "essai : tâches jouet des notations")

    vrai_jouer, vrai_noter = lp.jouer_pilote, lp.noter_ensembles

    def jouer(*a, **k):
        fiches, vecteurs, cn = vrai_jouer(*a, **k)
        for f in fiches:
            f["bilan"]["ensemble"] = f"PROPOSAL 1: idée {f['episode']}"
        return fiches, vecteurs, cn

    def noter(*a, **k):
        raise GardeArret("limite de durée dépassée pendant les notations")

    lp.jouer_pilote, lp.noter_ensembles = jouer, noter
    try:
        lp.executer(_config_lanceur(), depot, pilote, None, str(f_taches))
        raise SystemExit("le pilote jouet ne s'est pas arrêté pendant ses notations")
    except GardeArret:
        pass
    finally:
        lp.jouer_pilote, lp.noter_ensembles = vrai_jouer, vrai_noter
    d = depot / "diag" / pilote
    noms = sorted(p.name for p in d.glob("*.json"))
    if noms != ["appariements.json", "arret.json", "episodes.json"]:
        raise SystemExit(f"pilote jouet : fichiers {noms}")
    arret = json.loads((d / "arret.json").read_text(encoding="utf-8"))["resultat"]
    if arret["etape"] != "notations decisives par jouet-8B":
        raise SystemExit(f"pilote jouet arrêté à l'étape {arret['etape']!r}")
    git(depot, "add", "-A", "runs", "diag")
    git(depot, "commit", "-qm", "essai : pilote jouet arrêté pendant ses notations décisives")

    manifeste = json.loads((depot / "runs" / pilote / "manifeste.json").read_text(encoding="utf-8"))
    cp = manifeste["config"]
    config = {**{k: cp[k] for k in npa.CLES_EGALES_AU_PILOTE}, "mode": "jouet", "run_pilote": pilote,
              "duree_max_juges_s": {j["nom"]: 600 for j in cp["juges"]}, "duree_globale_s": 1200,
              "notations_attendues_par_juge": 4}
    npa.exiger_config_notations(config)
    f_config = depot / "prereg" / "T0.5-pilote-notations-config-v1.json"
    f_prereg = depot / "prereg" / "T0.5-pilote-notations-v1.md"
    for f in (f_config, f_prereg):
        if f.exists():
            raise SystemExit(f"{f} existe déjà (R12)")
    f_config.write_text(json.dumps(config, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    sceller(f_config)
    entropie = next(iter(manifeste["graines"].values()))["entropie"]
    valeurs = {
        "Commit du code d'analyse": code,
        "Run du pilote noté": pilote,
        "Manifeste du pilote noté": empreinte(depot / "runs" / pilote / "manifeste.json"),
        "Épisodes du pilote noté": empreinte(d / "episodes.json"),
        "Arrêt du pilote noté": empreinte(d / "arret.json"),
        "Tâches du pilote": sha_taches,
        "Entropie": str(entropie),
        "Configuration des notations (empreinte canonique)": empreinte_config(config),
        "Chemin des tâches du pilote noté": str(f_taches.relative_to(depot)),
        "Chemin du manifeste du pilote noté": f"runs/{pilote}/manifeste.json",
        "Chemin des épisodes du pilote noté": f"diag/{pilote}/episodes.json",
        "Chemin de l'arrêt du pilote noté": f"diag/{pilote}/arret.json",
        "Chemin de la configuration des notations": str(f_config.relative_to(depot)),
        "Tests attendus": str(tests),
    }
    texte = candidat.read_text(encoding="utf-8")
    for motif, valeur in valeurs.items():
        texte = remplacer_une_fois(texte, motif, valeur)
    f_prereg.write_text(texte, encoding="utf-8")
    sha_prereg = sceller_prereg(f_prereg)
    git(depot, "add", str(f_config), str(f_config) + ".sha256", str(f_prereg), str(f_prereg) + ".sha256")
    git(depot, "commit", "-qm", "essai : configuration et préenregistrement jouets des notations")
    print(json.dumps({"commit_code": code, "commit_essai": git(depot, "rev-parse", "HEAD"), "pilote": pilote,
                      "preenregistrement": sha_prereg, "configuration": empreinte_config(config),
                      "taches": sha_taches, "entropie": str(entropie)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
