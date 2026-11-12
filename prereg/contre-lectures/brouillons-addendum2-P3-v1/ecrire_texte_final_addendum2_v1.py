"""Texte final de l'addendum 2 de P3 : le candidat 2, suivi de l'entrée « Contre-lecture 7 » (vérification de l'écart).

Usage : python -I -B ecrire_texte_final_addendum2_v1.py CANDIDAT2 ENTREE7 SORTIE
  CANDIDAT2 : le candidat 2 (sha256 5d5e5aa8…, vérifié avant toute lecture), qui finit par l'entrée « Contre-lecture 6 ».
  ENTREE7 : l'entrée « Contre-lecture 7 », dans la forme relue par les deux vérificateurs de l'écart, chevrons remplis.
  SORTIE : le texte final, écrit en entier (candidat 2, puis l'entrée 7) ; son empreinte est imprimée et écrite dans
    SORTIE.sha256. N'importe rien du dépôt.
"""
import hashlib
import re
import sys
from pathlib import Path

CANDIDAT2 = "5d5e5aa83c57d37e6406ea1d57e87bc841c8e69e22a4918324a36b2b877bc247"
FIN_ENTREE6 = "  VC1-05 traités dans ce candidat.\n"


def main(argv):
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    source, entree, sortie = Path(argv[1]), Path(argv[2]), Path(argv[3])
    octets = source.read_bytes()
    if hashlib.sha256(octets).hexdigest() != CANDIDAT2:
        raise SystemExit("candidat 2 : empreinte inattendue")
    t = octets.decode("utf-8")
    e7 = entree.read_text(encoding="utf-8")
    if not t.endswith(FIN_ENTREE6):
        raise SystemExit("le candidat 2 ne finit pas par l'entrée 6")
    if not e7.startswith("- **Contre-lecture 7** — ") or not e7.endswith("\n") or "<" in e7 or ">" in e7:
        raise SystemExit("entrée 7 mal formée ou chevrons non remplis")
    if len(re.findall(r"`[0-9a-f]{64}`", e7)) != 4:
        raise SystemExit("entrée 7 : quatre empreintes attendues (deux candidats, deux rapports)")
    sortie.write_text(t + e7, encoding="utf-8")
    e = hashlib.sha256(sortie.read_bytes()).hexdigest()
    Path(str(sortie) + ".sha256").write_text(f"{e}  {sortie.name}\n", encoding="utf-8")
    print(e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
