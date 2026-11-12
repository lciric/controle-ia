"""Révision 9 de T0.6 candidat 12 : révision 8 + couples C6-1 à C6-8 de la contre-lecture 6 + marqueur
EMPREINTE_RAPPORT_CL6_T06. Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 10 novembre 2026. Chaque « ancien » une fois,
sinon arrêt sans rien écrire (R5) ; texte intermédiaire égal à celui du contre-lecteur ; sortie neuve (R12)."""
import hashlib, json, sys
from pathlib import Path

ENTREE = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r8.md")
COUPLES = Path("prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r8-cl6-couples-v1.json")
SORTIE = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r9.md")
EMPREINTE_ENTREE = "8b4b2341b70ecd5a5c717675c04dbaa5c8d2e83c43b6e3fb9689800fd926e0a8"
EMPREINTE_COUPLES = "2765682b757995542a72ec1fbb6d5cd9ad56794ddc4ff7d18de5e67ec175ad0a"
EMPREINTE_INTERMEDIAIRE = "f7fd518f06307997e4054199287a09c9aea6589c77a6e12ea61551a64531c2d9"
MARQUEUR = "<<EMPREINTE_RAPPORT_CL6_T06>>"
RAPPORT_CL6 = "8d1421839a76904732f1219cc22ea3cb10c5b1a7992048a34f37bc189b0dc176"

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def main() -> int:
    b = ENTREE.read_bytes()
    if sha(b) != EMPREINTE_ENTREE:
        sys.exit("empreinte de la révision 8 inattendue")
    if sha(COUPLES.read_bytes()) != EMPREINTE_COUPLES:
        sys.exit("empreinte des couples inattendue")
    t = b.decode("utf-8")
    for c in json.loads(COUPLES.read_text(encoding="utf-8")):
        n = t.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : ancien trouvé {n} fois (1 exigé) ; rien n'est écrit")
        t = t.replace(c["ancien"], c["nouveau"])
    if sha(t.encode("utf-8")) != EMPREINTE_INTERMEDIAIRE:
        sys.exit("texte intermédiaire différent de celui du contre-lecteur")
    if t.count(MARQUEUR) != 1:
        sys.exit("marqueur EMPREINTE_RAPPORT_CL6_T06 : une occurrence exigée")
    t = t.replace(MARQUEUR, RAPPORT_CL6)
    if SORTIE.exists():
        sys.exit(f"{SORTIE} existe déjà (R12)")
    SORTIE.write_text(t, encoding="utf-8")
    print(sha(SORTIE.read_bytes()), SORTIE)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
