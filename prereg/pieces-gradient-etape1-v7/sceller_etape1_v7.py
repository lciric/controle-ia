"""Scellement de la v7 de l'étape 1 (lignée « session-depot ») : remplit les marqueurs `<<…>>` laissés pour le
scellement, inscrit l'entrée « Contre-lecture 7 » (texte relu, rapport, verdict), tire l'entropie E
(`secrets.randbits(128)`) et inscrit les graines au format littéral (CE3-16), puis exige que le validateur du dépôt ne
relève plus rien et scelle par `controle_ia.prereg.sceller_prereg`. Refuse si le texte relu par la contre-lecture n° 7
n'est pas, au remplissage près, celui qu'on scelle (empreinte du brouillon relu vérifiée sur une copie) ; refuse toute
sortie existante (R12). Décliné de `sceller_etape1_v6.py` sous un nom nouveau (R12).

Usage : python -I -B sceller_etape1_v7.py CONFIG.json
CONFIG : {"brouillon", "sortie", "depot_src", "heure", "texte_relu_sha256", "rapport_chemin", "rapport_sha256",
          "verdict_cl7", "traitement_cl7", "vivier_commit", "vivier_chemin", "vivier_sha256", "vivier_message"}
"""
import hashlib
import json
import pathlib
import secrets
import sys

import numpy as np


def principal(chemin_config: str) -> int:
    c = json.loads(pathlib.Path(chemin_config).read_text(encoding="utf-8"))
    brouillon, sortie = pathlib.Path(c["brouillon"]), pathlib.Path(c["sortie"])
    if sortie.exists() or sortie.with_name(sortie.name + ".sha256").exists():
        print(f"refus : {sortie} existe déjà (R12)", file=sys.stderr)
        return 2
    texte = brouillon.read_text(encoding="utf-8")
    if hashlib.sha256(texte.encode("utf-8")).hexdigest() != c["texte_relu_sha256"]:
        print("refus : le brouillon n'est pas le texte relu par la contre-lecture n° 7", file=sys.stderr)
        return 2
    remplacements = {
        "<<HEURE_SCELLEMENT>>": c["heure"],
        "<<VIVIER_COMMIT>>": c["vivier_commit"],
        "<<VIVIER_CHEMIN>>": c["vivier_chemin"],
        "<<VIVIER_SHA256>>": c["vivier_sha256"],
        "<<VIVIER_MESSAGE>>": c["vivier_message"],
    }
    for marque, valeur in remplacements.items():
        if texte.count(marque) != 1:
            print(f"refus : marqueur {marque} présent {texte.count(marque)} fois", file=sys.stderr)
            return 2
        texte = texte.replace(marque, valeur)
    entropie = secrets.randbits(128)
    enfants = np.random.SeedSequence(entropie).spawn(3)
    graine_1, graine_2, entropie_analyse = (int(e.generate_state(1, dtype=np.uint64)[0]) for e in enfants)
    ancienne = ("- **Contre-lecture 7** — sous-agent neuf, revérification limitée aux corrections CL6-01 à CL6-05 (texte v7, diff du code de\n"
                "  `224de13` à `bef2c2f`, lanceur v4) ; son rapport, l'entropie E (Plan d'analyse, point 5) et les graines sont\n"
                "  inscrits ici au scellement.")
    if texte.count(ancienne) != 1:
        print("refus : entrée « Contre-lecture 7 » introuvable", file=sys.stderr)
        return 2
    nouvelle = (f"- **Contre-lecture 7** — sous-agent neuf, revérification limitée aux corrections CL6-01 à CL6-05 (texte v7, diff du code de\n"
                f"  `224de13` à `bef2c2f`, lanceur v4).\n"
                f"  Texte relu : `gradient-etape1-sondes-v7.md` (avant remplissage des marqueurs de scellement) `{c['texte_relu_sha256']}`.\n"
                f"  Rapport : `{c['rapport_chemin']}` `{c['rapport_sha256']}`. Verdict : {c['verdict_cl7']}. Traitement : {c['traitement_cl7']}\n"
                f"- **Entropie et graines** (Plan d'analyse, point 5 ; `secrets.randbits(128)` au scellement, `SeedSequence(E).spawn(3)`,\n"
                f"  `generate_state(1, uint64)[0]` de chaque enfant), au format littéral lu par le lanceur :\n"
                f"  - E = {entropie}\n"
                f"  - graine_1 = {graine_1}\n"
                f"  - graine_2 = {graine_2}\n"
                f"  - entropie_analyse = {entropie_analyse}")
    texte = texte.replace(ancienne, nouvelle)
    sys.path.insert(0, c["depot_src"])
    from controle_ia import prereg
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with open(sortie, "x", encoding="utf-8", newline="\n") as f:
        f.write(texte)
    problemes = prereg.problemes(sortie)
    if problemes:
        print("refus : validateur : " + " ; ".join(problemes), file=sys.stderr)
        sortie.unlink()
        return 3
    h = prereg.sceller_prereg(sortie)
    print(json.dumps({"scelle": str(sortie), "sha256": h, "graine_1": graine_1, "graine_2": graine_2,
                      "entropie_analyse": entropie_analyse}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1]) if len(sys.argv) == 2 else 1)
