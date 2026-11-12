"""Valeurs des couples proposés (règle (a') de P3-bis) au commit du code proposé : ajouts de l'arbre gelé depuis `a1de3915`,
identité avec P3 (règle de l'en-tête), empreintes des fichiers neufs, sortie de l'essai de fermeture v3, résumés.

    python -I calculer_valeurs_couples_v1.py ARBRE COMMIT DOSSIER_RAPPORT VALEURS.json IDENTITE.txt
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

GELES = [".", ":(exclude)prereg", ":(exclude)brouillons", ":(exclude)registres", ":(exclude)docs", ":(exclude)diag",
         ":(exclude)runs", ":(exclude)donnees", ":(exclude)livrables", ":(exclude)papiers", ":(exclude)traces",
         ":(exclude)CLAUDE.md"]                       # `harnais.validation_reelle.CHEMINS_GELES`
IDENTITE = ["src/controle_ia/premier_test_ia", "src/controle_ia/sondes", "src/controle_ia/harnais",
            "src/controle_ia/environnements", "src/controle_ia/organismes", "src/controle_ia/bases",
            "src/controle_ia/manifeste.py", "src/controle_ia/gardes.py", "src/controle_ia/scellement.py",
            "src/controle_ia/prereg.py", "requirements-gpu.txt", "requirements-cpu.txt", "requirements-donnees.txt"]
P3 = "7a54d431d89745839220f882b41b13e8c62ecfdd"
A1 = "a1de39151ebae29138a389829751397074239615"
RAPPORT = "docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/rapport-code-p3bis-regle-a-v1.md"


def git(arbre, *a) -> bytes:
    return subprocess.run(["git", "-C", str(arbre), *a], check=True, capture_output=True).stdout


def main(argv) -> int:
    arbre, commit, dossier, sortie, identite = Path(argv[0]), argv[1], Path(argv[2]), Path(argv[3]), Path(argv[4])
    ajouts = git(arbre, "diff", "--name-status", "--no-renames", A1, commit, "--", *GELES).decode().splitlines()
    if not ajouts or any(not x.startswith("A\t") for x in ajouts):
        raise SystemExit(f"arbre gelé : changements autres que des ajouts depuis a1de3915 : {ajouts}")
    chemins = [x.split("\t", 1)[1] for x in ajouts]
    ident = git(arbre, "diff", "--name-status", "--no-renames", P3, commit, "--", *IDENTITE)
    identite.write_bytes(ident)
    lignes_id = ident.decode().splitlines()
    if any(not x.startswith("A\t") for x in lignes_id):
        raise SystemExit("identité avec P3 : une ligne autre que « A »")
    neufs = [c for c in chemins if not c.endswith(".sha256")]
    empreintes = []
    for c in neufs:
        h = hashlib.sha256(git(arbre, "show", f"{commit}:{c}")).hexdigest()
        comp = f"{c}.sha256"
        if comp in chemins and git(arbre, "show", f"{commit}:{comp}").decode().split()[0] != h:
            raise SystemExit(f"{c} : compagnon ≠ empreinte")
        empreintes.append(f"`{c}` (`{h}`)")
    essai = dossier / "essai-fermeture-p3bis-v3-sortie-v1.txt"
    texte_essai = essai.read_text(encoding="utf-8")
    m = re.search(r"commit ([0-9a-f]{40})", (dossier / "essai-fermeture-p3bis-v3-lancement-v1.txt").read_text(encoding="utf-8"))
    conformes = sum(1 for x in texte_essai.splitlines() if x.startswith("CONFORME — "))
    non = sum(1 for x in texte_essai.splitlines() if x.startswith("NON CONFORME"))
    m1 = re.search(r"MUTATIONS : (\d+) tuées sur (\d+)", (dossier / "mutations-p3bis-regle-a-v1.txt").read_text(encoding="utf-8"))
    m2 = re.search(r"MUTATIONS : (\d+) tuées sur (\d+)", (dossier / "mutations-survivantes-rejouees-v1.txt").read_text(encoding="utf-8"))
    tuees, total = int(m1.group(1)) + int(m2.group(1)), int(m1.group(2))
    mut = (f"{tuees} tuées sur {total} ({m1.group(1)} en première passe ; les {m2.group(2)} survivantes, m05, m06 et m17, tuées "
           "après les essais de frontière et de PB-9 renforcés), import tracé sous la copie, témoin conforme")
    suite = (dossier / "suite-essais-p3bis-regle-a-v1.txt").read_text(encoding="utf-8")
    passes = re.findall(r"^(\d+ passed[^\n]*)$", suite, re.M)
    reprise = (dossier / "essais-lecture-p3bis-v2-au-commit-du-code-v1.txt").read_text(encoding="utf-8")
    passes_reprise = re.findall(r"^(\d+ passed[^\n]*)$", reprise, re.M)
    v = {
        "commit": commit, "rapport": RAPPORT,
        "n_ajouts_geles": len(chemins), "ajouts_geles": ", ".join(f"`{c}`" for c in chemins),
        "n_identite": len(lignes_id), "sha_identite": hashlib.sha256(ident).hexdigest(),
        "empreintes_neuves": " ; ".join(empreintes),
        "config_b2": "brouillons/P3-bis-temoin-positif-v1/P3-bis-temoin-positif-config-v1-brouillon2.json",
        "sha_essai_script": hashlib.sha256(git(arbre, "show", f"{commit}:scripts/essai_fermeture_p3bis_v3.py")).hexdigest(),
        "chemin_essai": "docs/notes/g0-deux-semaines-v1/p3bis-regle-plancher-v1/essai-fermeture-p3bis-v3-sortie-v1.txt",
        "sha_essai": hashlib.sha256(essai.read_bytes()).hexdigest(), "commit_essai": m.group(1),
        "essai_resume": (f"dernière ligne « {texte_essai.strip().splitlines()[-1]} », {conformes} lignes conformes, {non} non "
                         "conforme : quatre passages par issue, issue lue égale à l'issue plantée sous la règle (a'), taille "
                         "fixe, règle des plages, durée, sept contrôles positifs détectés, second paquet"),
        "essais_neufs": ("31 dans `tests/` — `test_premier_test_ia_lecture_p3bis_v2.py` 21, "
                         "`test_premier_test_ia_notation_plancher_800_v1.py` 3, `test_premier_test_ia_ouverture_p3bis_v3.py` 5, "
                         "`test_essai_fermeture_p3bis_v3.py` 2 —, plus 3 dans le banc du module commun v2 ; suite des essais de "
                         f"P3-bis de l'arbre (liste v2, deux fichiers hors liste d'`a1de3915`, quatre neufs) : {passes[-1] if passes else 'voir le journal'} "
                         f"; fichier des essais de la lecture v2, renforcé, rejoué au commit du code : {passes_reprise[-1] if passes_reprise else 'voir le journal'}"),
        "essais_neufs_court": "31 essais neufs, quatre fichiers, hors de la liste v2",
        "mutations": mut,
        "generateur": ("`docs/procedures/P3-bis-temoin-positif-v1/journaux-developpeur-v4/generer_chaine_v2.py` et "
                       "`ecarts-chaine-v2-a-v1.txt`"),
        "bancs": ("module commun 147 essais passés ; lanceur 58 cas, surveillance 99, récupération 46, contrôles 42, 0 non "
                  "conforme ; répétition jouet de bout en bout conforme (574 s ; paquet ouvert : `lecture_p3bis_v2`, 800 et 200 "
                  "directions, « vu ») ; journaux `journaux-developpeur-v4/*-dev.log`"),
        "devis": ("temps d'instance ajouté ≈ 1 à 2 min (tirage de 1 200 directions ≤ 8,4 s ; notation en ligne sur la carte ≈ 1 à 2 s, "
                  "estimée : +4,4 Gflop par action ; garde d'identité +32 à +51 s sur 30 lots ; fichiers et second paquet "
                  "+101,7 Mo, un ou deux morceaux de 90 Mo de plus) ; pire cas ≈ 4 min ; coût +0,02 à +0,04 USD attendu, "
                  "+0,15 USD au pire, téléchargement ≤ 0,005 USD : attendu inchangé à l'arrondi (≈ 4,5 à 7,5 USD), pire cas "
                  "d'une tentative ≈ 22,2 USD, course au pire ≈ 41,2 USD, sous le plafond de 80 USD ; lectures (session, "
                  "processeur, 0 USD) : lecture de P3 +3,2 s, lecture complémentaire v2 ≈ 12 s."),
    }
    sortie.write_text(json.dumps(v, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v[k] for k in ("commit", "n_ajouts_geles", "n_identite", "sha_identite", "sha_essai", "commit_essai",
                                        "mutations")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
