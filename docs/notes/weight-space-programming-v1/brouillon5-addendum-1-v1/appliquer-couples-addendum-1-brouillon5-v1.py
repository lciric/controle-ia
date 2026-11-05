"""Brouillon 5 de l'addendum n° 1 à SPARKS-EXP7-NUL : brouillon 4 + les 8 couples de la contre-lecture du delta v4 (L1 à
L8, tous retenus : les changements de code qu'ils supposent sont faits en v5), appliqués dans l'ordre, puis M-1 à M-5 ;
même règle : chaque « ancien » doit apparaître exactement une fois au moment de son application, sinon refus. Les trois
marqueurs « À REMPLIR » restent.

    python3 -I -B appliquer-couples-addendum-1-brouillon5-v1.py RACINE_DU_DEPOT HEURE_UTC
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SHA_B4 = "925c11fe58fe157e2343d5d36b816aacbdeb0f677d63afa50a1c0818323d5f29"
SHA_COUPLES = "68230e9a6820ab994f7ae2d0e3b620703e333816392fb168ab4b0b260db0b7ec"
B4 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon4.md"
B5 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon5.md"
COUPLES = "docs/notes/weight-space-programming-v1/contre-lecture-delta-v4-v1/couples-brouillon5-v1.json"
MARQUEUR = "À REMPLIR"

LIGNES_L = [
    ("nom de l'amorce `…_v3.sh` → amorce de la version du code citée en section 2 (`…_v<N>.sh`)", "nom resté de la v3", "L1 ; contre-lecture du delta v4, point 2"),
    ("fichier `sparks-v3-detruire` → `sparks-v<N>-detruire`", "idem", "L2 ; point 2"),
    ("« Qui pose `sparks-v3-detruire` » → `sparks-v<N>-detruire`", "idem", "L3 ; point 2"),
    ("marqueur de création incertaine → aussi pour toute sortie sans identifiant avec « success » vrai, code 0 compris ; clé `VAST_API_KEY` et mandataire passés par leur nom", "R-032, R-1497, R-1506", "L4 ; points 14 et 15"),
    ("— → redémarrage ou destruction par la session tenus pour faits seulement après un inventaire filtré", "R-1506 : code 0 sur refus", "L5 ; point 16"),
    ("borne de la machine : plafonds → durée réelle consignée à la fin, plafond sans fin consignée", "plan infaisable au coin haut du devis", "L6 ; point 9"),
    ("tir réel : non écrit → commande du mode « tir », sous un GO qui le couvre ; répétition dans un espace de processus par démarrage", "points 4, 19, 20 et 23", "L7"),
    ("marqueur du commit final : `prep/sparks-exp7-nul-v2` → branche de la dernière version contre-lue", "nom resté de la v2", "L8 ; point 3"),
]
LIGNES_M = [
    ("M-1", "en-tête du brouillon 4 → brouillon 5, contre-lecture du delta v4 et empreintes", "R6", "message de la mère du 4 novembre (≈ 23:58 UTC)"),
    ("M-2", "section 2 : compléments v4 → plus les neuf changements du code v5, dont la garde de l'addendum en mode réel (lecture retenue : commit lancé **contenu dans** `origin/main`, non « descendant », une branche d'essai pouvant descendre de `main`)", "liste fermée ; contre-lecture du delta v4, point 21", "contre-lecture du delta v4, « Changements de code requis »"),
    ("M-3", "— → tir réel sous une ligne de GO à part, posée par la mère (`GO_ID` en paramètre, plafond écrit ≤ 5 USD)", "nœud du point 4 : l'extension de GO-2026-11-04-04 dit « scellé avant tout lancement »", "message de la mère"),
    ("M-4", "« Contre-lecture » : reste celle du delta v4 → faite (« à reprendre ») ; reste celle du delta v5", "état", "contre-lecture du delta v4"),
    ("M-5", "pied du brouillon 4 → pied du brouillon 5", "état", "—"),
]


def table() -> str:
    t = ["## 00000. Changements du brouillon 4 au brouillon 5 (avant → après ; raison ; source)", "",
         "L1 à L8 : les couples de la contre-lecture du delta v4 (`docs/notes/weight-space-programming-v1/"
         "contre-lecture-delta-v4-v1/couples-brouillon5-v1.json`, `68230e9a…`), tous retenus, appliqués dans l'ordre par "
         "script. M-1 à M-5 : changements demandés par la mère, appliqués ensuite par le même script, sous la même règle "
         "(`docs/notes/weight-space-programming-v1/brouillon5-addendum-1-v1/appliquer-couples-addendum-1-brouillon5-v1.py` "
         "et sa sortie, même dossier).", "",
         "| N° | Avant → après | Raison | Source |", "|---|---|---|---|"]
    t += [f"| L-{i} | {a} | {r} | {s} |" for i, (a, r, s) in enumerate(LIGNES_L, 1)]
    t += [f"| {n} | {a} | {r} | {s} |" for n, a, r, s in LIGNES_M]
    return "\n".join(t) + "\n\n---\n\n"


def changements(heure: str) -> list[tuple[str, str, str]]:
    return [
        ("M-1 titre", "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 4\n",
         "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 5\n"),
        ("M-1 date", "Brouillon 4 écrit le 4 novembre 2026 à partir de 23:05 UTC (`date -u`), toujours avant toute donnée.",
         "Brouillon 4 écrit le 4 novembre 2026 à partir de 23:05 UTC (`date -u`), toujours avant toute donnée. Brouillon 5 "
         f"écrit le 5 novembre 2026 à partir de {heure} UTC (`date -u`), toujours avant toute donnée."),
        ("M-1 auteur", "(même dossier, compagnons « OK »).\n- Décision",
         "(même dossier, compagnons « OK »).\n- Brouillon 5 : même rédacteur-développeur ; brouillon 4 (`925c11fe…`) + les 8 "
         "couples de la contre-lecture du delta v4 + M-1 à M-5 (section 00000). Contre-lecture du delta v4 : "
         "`docs/notes/weight-space-programming-v1/contre-lecture-delta-v4-v1/contre-lecture-delta-v4-v1.md`, sha256 "
         "`4bc7066e…` (verdict « à reprendre : le code et la commande du tir réel ; le texte sera scellable après les 8 "
         "couples et le tir »), couples `couples-brouillon5-v1.json` `68230e9a…` (même dossier, compagnons « OK »).\n- Décision"),
        ("M-0 table", "## 0000. Changements du brouillon 3 au brouillon 4", table() + "## 0000. Changements du brouillon 3 au brouillon 4"),
        ("M-2 et M-3 compléments v5", "Fonction par fonction : `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v4.md`.",
         "Fonction par fonction : `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v4.md`.\n\n"
         "**Compléments à la liste (contre-lecture du delta v4, « Changements de code requis »).** Code v5, branche "
         "`prep/sparks-exp7-nul-v5`, descendant du code v4 (`53d4eda6`), fichiers neufs seulement : (1) `VAST_API_KEY` "
         "transmise à `vastai` par son nom ; (2) identifiant et « success » vrai testés avant toute erreur de certificat ; "
         "`start` et `destroy` lus comme la création (refus sur la sortie d'erreur avec le code 0, R-1506), puis inventaire "
         "filtré ; (3) durée réelle de chaque démarrage consignée à sa fin et prise par la borne de la machine ; (4) en mode "
         "réel, l'amorce exige l'addendum reconnu : empreinte attendue passée à la création (`ADDENDUM_SHA256`), ou commit "
         "lancé contenu dans `origin/main` ; un démarrage dont la création n'a pas passé toutes les gardes ne peut exécuter "
         "qu'un ordre « fin » ; (5) amorce prise par `git show \"$COMMIT:…\"` ; (6) corps de la réponse au `DELETE` lu "
         "(`\"success\": false` = échec) et aucune tentative de la minuterie au-delà de sa marge ; (7) mode « tir » du "
         "lanceur, avec sa commande écrite pas à pas (machine réelle, image de la course, échéance de 20 à 30 minutes, sans "
         "modèle ni donnée, création arrêtée à la garde du code, ordre « fin », inventaires filtrés), **sous une ligne de GO à "
         "part posée par la mère, `GO_ID` en paramètre, plafond écrit au plus 5 USD**, devis contrôlé par `tir.py` ; (8) "
         "répétition jouet corrigée (`/usr/sbin` et `/sbin` dans le chemin, chaque démarrage sous `unshare -pf "
         "--mount-proc`, attendus précis) ; (9) mutations manquantes. La liste fermée v5 "
         "(`src/controle_ia/sparks_exp7_nul_v5/liste-fermee-v1.txt`) compte les fichiers v2 à v5 ; la garde de lancement lit "
         "celle-ci. Fonction par fonction : `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v5.md`."),
        ("M-4 contre-lecture", "`rapport-developpeur-addendum-1-v4.md`), par un sous-agent neuf.",
         "`rapport-developpeur-addendum-1-v4.md`), par un sous-agent neuf. Contre-lecture du delta v4 faite (`4bc7066e…`, "
         "« à reprendre ») : ses 8 couples sont appliqués ici (section 00000) et ses neuf changements sont faits en v5 ; "
         "restent la contre-lecture du delta v5 (`git diff 53d4eda6..<commit>`, `rapport-developpeur-addendum-1-v5.md`), "
         "par un sous-agent neuf, et le tir réel."),
        ("M-5 pied", "Brouillon 4 (4 novembre 2026, même rédacteur-développeur), sur le brouillon 3",
         "Brouillon 5 (5 novembre 2026, même rédacteur-développeur), sur le brouillon 4 (4 novembre 2026, même "
         "rédacteur-développeur), sur le brouillon 3"),
    ]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def appliquer(texte: str, nom: str, ancien: str, nouveau: str) -> str:
    n = texte.count(ancien)
    if n != 1:
        raise SystemExit(f"REFUS {nom} : « ancien » trouvé {n} fois (une attendue)")
    print(f"OK {nom} : 1 occurrence, {len(ancien)} → {len(nouveau)} caractères")
    return texte.replace(ancien, nouveau)


def main(argv: list[str]) -> int:
    racine, heure = Path(argv[0]), argv[1]
    b4, cp = (racine / B4).read_bytes(), (racine / COUPLES).read_bytes()
    if sha(b4) != SHA_B4 or sha(cp) != SHA_COUPLES:
        raise SystemExit("REFUS : empreinte d'entrée différente")
    print(f"entrées : brouillon 4 {sha(b4)} ; couples {sha(cp)}")
    texte = b4.decode("utf-8")
    for i, c in enumerate(json.loads(cp), 1):
        texte = appliquer(texte, f"L-{i}", c["ancien"], c["nouveau"])
    inter = sha(texte.encode("utf-8"))
    print(f"après les 8 couples : {inter} (texte d'essai du contre-lecteur : 56992343…)")
    if not inter.startswith("56992343"):
        raise SystemExit("REFUS : texte après les couples différent de celui du contre-lecteur")
    for nom, a, n in changements(heure):
        texte = appliquer(texte, nom, a, n)
    if texte.count(MARQUEUR) != 3:
        raise SystemExit(f"REFUS : {texte.count(MARQUEUR)} marqueurs (trois attendus)")
    sortie = racine / B5
    if sortie.exists():
        raise SystemExit(f"REFUS : {sortie} existe déjà (R12)")
    sortie.write_text(texte, encoding="utf-8")
    print(f"marqueurs « {MARQUEUR} » : 3")
    print(f"sortie : {B5} {sha(texte.encode('utf-8'))} ({len(texte.encode('utf-8'))} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
