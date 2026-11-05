"""Candidat 2 de l'addendum 2 de P3, écrit en entier par ce script à partir du candidat 1.

Usage : python -I -B ecrire_candidat2_addendum2_v1.py CANDIDAT1 LIGNE_CANDIDAT2 SORTIE
  CANDIDAT1 : le candidat 1 (sha256 9900a721…, vérifié avant toute lecture).
  LIGNE_CANDIDAT2 : l'élément « Candidat 2 » de l'en-tête (fichier `ligne-candidat2-addendum2-v1.md`, versé à côté) ;
    il est inséré tel quel juste avant l'élément « Date (UTC) ».
  SORTIE : le candidat 2, écrit en entier ; son empreinte est imprimée et écrite dans SORTIE.sha256.
Corrections : constats VC1-01 à VC1-05 de la vérification du candidat 1 (contre-lecture 6, rapport
`verification-candidat1-addendum2-P3-v1.md`, sha256 3f0dce9b…), en mots exacts du rapport ; seuls les retours à la ligne
sont choisis ici. Chaque ancien texte doit se trouver une seule fois. N'importe rien du dépôt.
"""
import hashlib
import sys
from pathlib import Path

CANDIDAT1 = "9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e"
ANCRE_DATE = "- Date (UTC) : celle du commit de scellement, qui fait foi.\n"

PAIRES = [
    # VC1-02 : heure de la ligne « Candidat 1 »
    ("(2026-10-20 vers 21:45 UTC)", "(2026-10-20 vers 21:21 UTC)"),
    # VC1-04, point 1 : comptes de la ligne « Candidat 1 »
    ("les trois tests proposés et éprouvés par la lentille « code »\n"
     "  (VV3-code-01 à 03), ajoutés sans changement (128 tests)",
     "les trois fonctions de test proposées et éprouvées par la lentille\n"
     "  « code » (VV3-code-01 à 03), ajoutées sans changement (7 tests de plus, 128 en tout)"),
    # VC1-01, point 1 : script cité par son chemin versé et son empreinte
    ("script\n  `…/addendum2-p3/candidat/ecrire_candidat1_addendum2_v1.py` ;",
     "script\n  `prereg/contre-lectures/brouillons-addendum2-P3-v1/ecrire_candidat1_addendum2_v1.py` (sha256\n"
     "  `94560a3b690facfc8a68a39d34f069afba44771156387f7978fcdc7877078593`), qui écrit tout le candidat 1 sauf cette ligne,\n"
     "  ajoutée ensuite ;"),
    # VC1-04, point 2 ; VC1-03, points 1 et 2 ; VC1-05 : fin de l'entrée 5 et entrée 6
    ("(30 mutants neufs\n"
     "  sur les points changés, 24 tués, 2 équivalents ; trois tests proposés). Tests v4 : les 121 tests relus et les trois\n"
     "  tests proposés et éprouvés par la lentille « code » (VV3-code-01 à 03), ajoutés sans changement, soit 128 tests\n"
     "  (sha256 `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07`), passés sous la garde R1 (0 refus). "
     "Constats traités dans le texte\n"
     "  (ce candidat) ; le module relu est le module cité en tête.\n",
     "(30 mutants neufs\n"
     "  sur les points changés : 24 tués, 6 survivants dont 2 équivalents ; les 4 autres, VV-G6-02, VV-F-01, VV-F-02 et\n"
     "  VV-D3-04, sont tués par les trois fonctions de test proposées). Tests v4 : les 121 tests relus et les trois fonctions\n"
     "  de test proposées et éprouvées par la lentille « code » (VV3-code-01 à 03), ajoutées sans changement, soit 7 tests\n"
     "  de plus (le test de la garde 7 compte une fois par forme) et 128 tests (sha256\n"
     "  `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07`), passés sous la garde R1 (128 passés,\n"
     "  0 refus ; journaux `prereg/contre-lectures/tests-v4-addendum2-P3-v1/pytest-suite-v4-garde-r1.log`, sha256\n"
     "  `cb24c899aa490bfa98e00b370c0ad388f13ddfbce6f277b21bd368a24ba12c36`, et\n"
     "  `prereg/contre-lectures/tests-v4-addendum2-P3-v1/r1-suite-v4.jsonl`, sha256\n"
     "  `f2a4be52af0304831d77abeb36d78c46bb073f1a606f7eb56e3b0e3f576b3edd`). Constats traités : VV3-texte-01 à 07 et\n"
     "  VV3-code-05 dans le texte (ce candidat) ; VV3-code-01 à 03 par les trois fonctions de test ; VV3-code-04 par les\n"
     "  mots de VV3-texte-02 (précision 14), sans le test facultatif ; VV3-code-01, point 3 (notes) : notes v3 laissées\n"
     "  telles quelles, G6-02 étant désormais tué par `test_garde_6_au_lancement_exception_du_chargeur_convertie` ; le\n"
     "  module relu est le module cité en tête.\n"
     "- **Contre-lecture 6** — vérification mécanique du candidat 1 (sha256\n"
     "  `9900a721560c87361efcf60660863727644e8fdc3ab88e4fd1f325a613306b0e`) et des tests v4 (sha256\n"
     "  `f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07`) par un sous-agent neuf, qui n'a écrit ni le\n"
     "  texte, ni aucune version du module ou de ses tests, ni aucune contre-lecture antérieure : rapport\n"
     "  `prereg/contre-lectures/verification-candidat1-addendum2-P3-v1.md` (sha256\n"
     "  `3f0dce9ba99ab692b2d47660457a28b969ac3b0ac04b43f931f0101f05283f04`), « scellable après corrections » ; suite v4\n"
     "  relancée sous la garde R1 (128 passés, 0 refus) ; chaque test ajouté tue le mutant qu'il vise. Constats VC1-01 à\n"
     "  VC1-05 traités dans ce candidat.\n"),
]


def main(argv):
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    source, ligne, sortie = Path(argv[1]), Path(argv[2]), Path(argv[3])
    octets = source.read_bytes()
    if hashlib.sha256(octets).hexdigest() != CANDIDAT1:
        raise SystemExit("candidat 1 : empreinte inattendue")
    t = octets.decode("utf-8")
    for ancien, nouveau in PAIRES:
        if t.count(ancien) != 1:
            raise SystemExit(f"trouvé {t.count(ancien)} fois (une attendue) : {ancien[:70]!r}")
        t = t.replace(ancien, nouveau)
    element = ligne.read_text(encoding="utf-8")
    if not element.startswith("- Candidat 2 : ") or not element.endswith("\n") or t.count(ANCRE_DATE) != 1:
        raise SystemExit("élément « Candidat 2 » mal formé, ou ancre « Date (UTC) » absente ou en double")
    t = t.replace(ANCRE_DATE, element + ANCRE_DATE)
    sortie.write_text(t, encoding="utf-8")
    e = hashlib.sha256(sortie.read_bytes()).hexdigest()
    Path(str(sortie) + ".sha256").write_text(f"{e}  {sortie.name}\n", encoding="utf-8")
    print(e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
