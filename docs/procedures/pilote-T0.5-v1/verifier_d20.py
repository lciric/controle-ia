"""Contrôle D-20 sans lecture : cherche, dans des fichiers à verser, des fragments des fiches scellées de la revalidation
(textes des actions de l'agent), sans jamais afficher un contenu. Les chaînes des fiches (valeurs JSON d'au moins 80
caractères) sont découpées en fenêtres de 64 caractères aux positions multiples de 16 ; chaque fichier candidat (texte,
JSON, ou archive tar, membre par membre) est parcouru par fenêtres glissantes de 64 caractères. Un fragment commun d'au
moins 79 caractères est toujours détecté. Seuls s'affichent des comptes, des chemins de fichiers candidats et des chemins
de clés des fiches (jamais de valeur).
Usage : python3 -I verifier_d20.py FICHE.json [FICHE.json …] -- CANDIDAT [CANDIDAT …]   (code 1 si une fenêtre commune)"""
import hashlib
import json
import sys
import tarfile
from collections import Counter

L, PAS, MIN = 64, 16, 80
args = sys.argv[1:]
if "--" not in args:
    sys.exit(__doc__)
k = args.index("--")
fiches, candidats = args[:k], args[k + 1:]


def chaines(o, chemin="$"):
    if isinstance(o, str):
        yield chemin, o
    elif isinstance(o, dict):
        for c, v in o.items():
            yield from chaines(v, f"{chemin}.{c}")
    elif isinstance(o, list):
        for v in o:
            yield from chaines(v, f"{chemin}[]")


def h(s: str) -> bytes:
    return hashlib.blake2b(s.encode("utf-8"), digest_size=12).digest()


index: dict[bytes, str] = {}
for f in fiches:
    with open(f, encoding="utf-8") as fh:
        for chemin, s in chaines(json.load(fh)):
            if len(s) >= MIN:
                for i in range(0, len(s) - L + 1, PAS):
                    index.setdefault(h(s[i:i + L]), chemin)
print(f"fenêtres indexées : {len(index)} (fiches : {len(fiches)})")


def textes(nom: str, donnees: bytes):
    t = donnees.decode("utf-8", errors="replace")
    yield nom, t
    try:
        o = json.loads(t)
    except Exception:
        return
    for chemin, s in chaines(o):
        yield f"{nom}:{chemin}", s


def examiner(nom: str, donnees: bytes) -> int:
    n = 0
    vus = Counter()
    for etiquette, t in textes(nom, donnees):
        for i in range(0, len(t) - L + 1):
            c = index.get(h(t[i:i + L]))
            if c is not None:
                n += 1
                vus[c] += 1
    if n:
        print(f"COMMUN {nom} : {n} fenêtre(s) ; clés des fiches : {dict(vus)}")
    return n


total = 0
for c in candidats:
    if tarfile.is_tarfile(c):
        with tarfile.open(c) as tar:
            for m in tar.getmembers():
                if m.isfile():
                    total += examiner(f"{c}!{m.name}", tar.extractfile(m).read())
    else:
        with open(c, "rb") as fh:
            total += examiner(c, fh.read())
print(f"fenêtres communes : {total}")
sys.exit(1 if total else 0)
