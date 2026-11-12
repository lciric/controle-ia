"""Révision 10 de T0.6 candidat 12 : révision 9 + couples R10-1 à R10-3 (contenu de S, R-2080). Écrit par la session mère
`session_01QPDgKgACWyCkCN8HjqwNXy` le 10 novembre 2026. Chaque « ancien » doit apparaître exactement une fois, sinon arrêt
sans rien écrire (R5) ; la sortie ne doit pas exister (R12)."""
import hashlib, json, sys
from pathlib import Path

ENTREE = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r9.md")
SORTIE = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r10.md")
COUPLES = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r10-couples-v1.json")
EMPREINTE_ENTREE = "e800c4dfe45d6acaa332f9bb91bcc3877cf87af16086406dfe8c193bea1c3071"

def main() -> int:
    b = ENTREE.read_bytes()
    if hashlib.sha256(b).hexdigest() != EMPREINTE_ENTREE:
        sys.exit(f"empreinte de {ENTREE} inattendue")
    t = b.decode("utf-8")
    couples = json.loads(COUPLES.read_text(encoding="utf-8"))
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            sys.exit(f"couple {c['id']} : ancien trouvé {n} fois (1 exigé) ; rien n'est écrit")
        t = t.replace(c["ancien"], c["nouveau"])
    if SORTIE.exists():
        sys.exit(f"{SORTIE} existe déjà (R12)")
    SORTIE.write_text(t, encoding="utf-8")
    print(hashlib.sha256(SORTIE.read_bytes()).hexdigest(), SORTIE)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
