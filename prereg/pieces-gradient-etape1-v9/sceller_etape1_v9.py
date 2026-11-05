"""Scellement de la v9 de l'étape 1 (lignée « session-depot ») : remplit les marqueurs `<<…>>` laissés pour le
scellement, inscrit l'entrée « Contre-lecture 9 » (texte relu, rapport, verdict), tire l'entropie E
(`secrets.randbits(128)`) et inscrit les graines au format littéral (CE3-16), puis exige que le validateur du dépôt ne
relève plus rien et scelle par `controle_ia.prereg.sceller_prereg`. Refuse si le texte relu par la contre-lecture n° 9
n'est pas, au remplissage près, celui qu'on scelle (empreinte du brouillon relu vérifiée) ; refuse toute sortie
existante (R12) ; refuse si le lanceur ne lit pas exactement le chemin scellé (`PREREG=` du lanceur, relatif au dépôt) ou
si le texte ne cite pas l'empreinte réelle du lanceur (le lanceur v4 lisait un nom qu'aucune version scellée ne portait).
Décliné de `sceller_etape1_v8.py` (relu par la contre-lecture n° 8, jamais versé) sous un nom nouveau (R12).

Usage : python -I -B sceller_etape1_v9.py CONFIG.json
CONFIG : {"brouillon", "sortie", "depot_src", "lanceur", "heure", "texte_relu_sha256", "rapport_chemin", "rapport_sha256",
          "verdict_cl9", "traitement_cl9", "vivier_commit", "vivier_chemin", "vivier_sha256", "vivier_message"}
"""
import hashlib
import json
import pathlib
import re
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
        print("refus : le brouillon n'est pas le texte relu par la contre-lecture n° 9", file=sys.stderr)
        return 2
    # le lanceur lit-il exactement ce qu'on scelle, et le texte cite-t-il le vrai lanceur ?
    depot = pathlib.Path(c["depot_src"]).resolve().parent
    lanceur = pathlib.Path(c["lanceur"])
    lignes = [l for l in lanceur.read_text(encoding="utf-8").splitlines() if l.startswith("PREREG=")]
    try:
        relatif = sortie.resolve().relative_to(depot).as_posix()
    except ValueError:
        relatif = None
    if relatif is None or lignes != [f"PREREG={relatif}"]:
        print(f"refus : le lanceur lit {lignes}, la sortie est {relatif} (chemin relatif au dépôt {depot})", file=sys.stderr)
        return 2
    e_lanceur = hashlib.sha256(lanceur.read_bytes()).hexdigest()
    if texte.count(e_lanceur) != 1:
        print(f"refus : le texte ne cite pas une fois l'empreinte du lanceur {e_lanceur}", file=sys.stderr)
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
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)))
    if restes:
        print(f"refus : marqueurs restants {restes}", file=sys.stderr)
        return 2
    entropie = secrets.randbits(128)
    enfants = np.random.SeedSequence(entropie).spawn(3)
    graine_1, graine_2, entropie_analyse = (int(e.generate_state(1, dtype=np.uint64)[0]) for e in enfants)
    ancienne = ("- **Contre-lecture 9** — sous-agent neuf, revérification limitée aux corrections CL8-01 à CL8-12 (texte v9, lanceur v6\n"
                "  et ses essais ; diff du code de `5d1d4fd` à `4de6544`) ; son rapport, l'entropie E (Plan d'analyse, point 5) et les graines sont\n"
                "  inscrits ici au scellement.")
    if texte.count(ancienne) != 1:
        print("refus : entrée « Contre-lecture 9 » introuvable", file=sys.stderr)
        return 2
    nouvelle = (f"- **Contre-lecture 9** — sous-agent neuf, revérification limitée aux corrections CL8-01 à CL8-12 (texte v9, lanceur v6\n"
                f"  et ses essais ; diff du code de `5d1d4fd` à `4de6544`).\n"
                f"  Texte relu : `gradient-etape1-sondes-v9.md` (avant remplissage des marqueurs de scellement) `{c['texte_relu_sha256']}`.\n"
                f"  Rapport : `{c['rapport_chemin']}` `{c['rapport_sha256']}`. Verdict : {c['verdict_cl9']}. Traitement : {c['traitement_cl9']}\n"
                f"- **Entropie et graines** (Plan d'analyse, point 5 ; `secrets.randbits(128)` au scellement, `SeedSequence(E).spawn(3)`,\n"
                f"  `generate_state(1, uint64)[0]` de chaque enfant), au format littéral lu par le lanceur :\n"
                f"  - E = {entropie}\n"
                f"  - graine_1 = {graine_1}\n"
                f"  - graine_2 = {graine_2}\n"
                f"  - entropie_analyse = {entropie_analyse}")
    texte = texte.replace(ancienne, nouvelle)
    for nom in ("vivier_commit", "vivier_chemin", "vivier_sha256", "question_c001_sha256", "graine_1", "graine_2", "entropie_analyse"):
        n = len(re.findall(r"(^|\s)" + nom + r" = [0-9a-zA-Z_./:-]+", texte))
        if n != 1:
            print(f"refus : « {nom} = … » présent {n} fois (une seule occurrence exigée, CE4-12)", file=sys.stderr)
            return 2
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
