"""Révision 8 de T0.6 candidat 12 : révision 7 + mots de Lazar (R-2077) + couples d'en-tête. Écrit par la session mère
`session_01QPDgKgACWyCkCN8HjqwNXy` le 10 novembre 2026. Chaque « ancien » doit apparaître exactement une fois, sinon arrêt
sans rien écrire (R5) ; la sortie ne doit pas exister (R12)."""
import hashlib, json, sys
from pathlib import Path

ENTREE = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r7.md")
SORTIE = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r8.md")
COUPLES = Path("brouillons/T0.6-organismes-v0-v1-candidat12-r8-couples-v1.json")
EMPREINTE_ENTREE = "9dd695b16695d5f85fcf09ee8dc896e8cbf8a4fd5c9523e032762849cdcdfe0c"

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
