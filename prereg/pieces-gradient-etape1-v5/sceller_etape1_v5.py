"""Scellement de la v5 de l'étape 1 (lignée « session-depot ») : remplit les marqueurs `<<…>>` laissés pour le
scellement, inscrit l'entrée « Contre-lecture 5 » (texte relu, rapport, verdict), tire l'entropie E
(`secrets.randbits(128)`) et inscrit les graines au format littéral (CE3-16), puis exige que le validateur du dépôt ne
relève plus rien et scelle par `controle_ia.prereg.sceller_prereg`. Refuse si le texte relu par la contre-lecture n° 4
n'est pas, au remplissage près, celui qu'on scelle (empreinte du brouillon relu vérifiée sur une copie) ; refuse toute
sortie existante (R12). Décliné de `sceller_etape1_v4.py` sous un nom nouveau (R12).

Usage : python -I -B sceller_etape1_v5.py CONFIG.json
CONFIG : {"brouillon", "sortie", "depot_src", "heure", "texte_relu_sha256", "rapport_chemin", "rapport_sha256",
          "verdict_cl5", "traitement_cl5", "vivier_commit", "vivier_chemin", "vivier_sha256", "vivier_message"}
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
        print("refus : le brouillon n'est pas le texte relu par la contre-lecture n° 5", file=sys.stderr)
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
    ancienne = ("- **Contre-lecture 5** — sous-agent neuf, revérification limitée aux corrections RV-01 à RV-16 et CE4-01 à CE4-13 (texte v5,\n"
                "  diff du code de `ed3ce0e` à `44cd936`, lanceur v3) ; son rapport, l'entropie E (Plan d'analyse, point 5) et les graines\n"
                "  sont inscrits ici au scellement.")
    if texte.count(ancienne) != 1:
        print("refus : entrée « Contre-lecture 5 » introuvable", file=sys.stderr)
        return 2
    nouvelle = (f"- **Contre-lecture 5** — sous-agent neuf, revérification limitée aux corrections RV-01 à RV-16 et CE4-01 à CE4-13 (texte v5,\n"
                f"  diff du code de `ed3ce0e` à `44cd936`, lanceur v3).\n"
                f"  Texte relu : `gradient-etape1-sondes-v5.md` (avant remplissage des marqueurs de scellement) `{c['texte_relu_sha256']}`.\n"
                f"  Rapport : `{c['rapport_chemin']}` `{c['rapport_sha256']}`. Verdict : {c['verdict_cl5']}. Traitement : {c['traitement_cl5']}\n"
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
