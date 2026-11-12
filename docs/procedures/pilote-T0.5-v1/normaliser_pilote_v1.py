"""Normalisation du préenregistrement du pilote de T0.5 (v1) : les champs que fixe le scellement (date, commit du code,
entropie, tests attendus et leur rappel, rapports de la relecture R2, décision de Lazar sur N-019 : GO et ligne du
registre) sont masqués ; le reste se compare au candidat
relu. Partagée par le générateur (remplir_pilote_v1.py) et les contrôles avant dépense, qui la chargent par son chemin.
Usage : python -I normaliser_pilote_v1.py FICHIER|-   (écrit l'empreinte sha256 du texte normalisé)"""
import hashlib
import re
import sys


def normaliser(texte: str) -> str:
    x = re.sub(r"version scellée le \d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC", "version scellée le <DATE>", texte)
    x = re.sub(r"- Date \(UTC\) : \d{4}-\d{2}-\d{2} \d{2}:\d{2}", "- Date (UTC) : <DATE>", x)
    x = re.sub(r"(- Commit du code d'analyse : )`[0-9a-f]{40}`", r"\1<COMMIT>", x)
    x = re.sub(r"(- Entropie : )`\d+`", r"\1<ENTROPIE>", x)
    x = re.sub(r"(- Décision de Lazar sur N-019 : )`GO-[0-9-]+` \(R-[0-9]+\)", r"\1<GO>", x)
    x = re.sub(r"(- Tests attendus : )`\d+`", r"\1<TESTS>", x)
    x = re.sub(r"au commit cité, \d+ tests\)", "au commit cité, <TESTS> tests)", x)
    x = re.sub(r"(Relecture R2 du brouillon 8 .*?: rapports ).*$", r"\1<RAPPORTS>", x, flags=re.M)
    return x


def empreinte(texte: str) -> str:
    return hashlib.sha256(normaliser(texte).encode("utf-8")).hexdigest()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage : normaliser_pilote_v1.py FICHIER|-")
    texte = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    print(empreinte(texte))
