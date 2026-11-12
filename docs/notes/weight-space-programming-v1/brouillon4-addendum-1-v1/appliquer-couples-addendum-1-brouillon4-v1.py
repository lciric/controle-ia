"""Brouillon 4 de l'addendum n° 1 à SPARKS-EXP7-NUL : brouillon 3 + les 10 couples de la contre-lecture du delta v3 (K1 à
K10, tous retenus : les huit changements de code qu'ils supposent sont faits en v4), appliqués dans l'ordre, puis H-1 à
H-6 ; même règle : chaque « ancien » doit apparaître exactement une fois au moment de son application, sinon refus. Les
trois marqueurs « À REMPLIR » restent.

    python3 -I -B appliquer-couples-addendum-1-brouillon4-v1.py RACINE_DU_DEPOT HEURE_UTC
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SHA_B3 = "12e47e51525e0d820e8bbf599167ac49be12dbc1768b5635569ac027656ac424"
SHA_COUPLES = "838882eb938a5e0fb2de50527e7df9a3eddec7e6d5973539c7e1bc64893d5d8d"
B3 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon3.md"
B4 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon4.md"
COUPLES = "docs/notes/weight-space-programming-v1/contre-lecture-delta-v3-v1/couples-brouillon4-v1.json"
MARQUEUR = "À REMPLIR"

LIGNES_K = [
    ("contrôle causal : branche `calcul/sparks-exp7-nul-causal-v1` → branche neuve liée au commit et à l'ordre, sur ordre écrit", "texte resté de la v1 ; phase causale rejouable", "K1 ; contre-lecture du delta v3, points 2 et 15"),
    ("borne de la carte : « `timeout` de l'amorce » → `timeout` sur chaque étape, repli `vastai` compris", "aucune étape n'était bornée", "K2 ; point 3 et Q3"),
    ("attente du principal : non précisée → minuterie de ce démarrage, par son numéro au lancement, au plus 32 minutes ; délais de chaque étape écrits", "démonstration dans un espace de processus", "K3 ; Q3"),
    ("branche des ordres `calcul/sparks-exp7-nul-v3-ordres` → `ordres/sparks-exp7-nul-v4-<commit court>`", "la session n'écrit pas sous `calcul/` ; répétition isolée", "K4 ; point 10"),
    ("ordre : champ `instance` = `CONTAINER_ID` exigé", "ordre lié à une instance", "K5 ; point 11"),
    ("consignation de l'ordre : non contrôlée → impossible = refus", "disque plein", "K6 ; point 13"),
    ("`deja_usd` : cru → ne baisse jamais ; borne = max(`deja_usd`, borne propre de la machine)", "R-1481", "K7 ; point 14"),
    ("stockage non borné par la machine → risque accepté par Lazar (R-1488, option (b)), borné par l'échéance du GO", "décision de Lazar", "K8 (indépendant du code)"),
    ("épreuves : « cas sain et artefact » → chacune mutée au banc, minuterie et attente jouées sous `unshare -pf` ; liste du tir réel détaillée", "Q5, Q6", "K9 ; points 17 et 24"),
    ("création par la session : non dite → `vastai create` sous `timeout`, sortie non affichée, marqueur de création incertaine", "R-1480 ; point 6 de la liste", "K10 ; Q3"),
]
LIGNES_H = [
    ("H-1", "en-tête du brouillon 3 → brouillon 4, contre-lecture du delta v3 et empreintes", "R6", "message de la mère du 4 novembre (≈ 22:55 UTC)"),
    ("H-2", "épreuves (K9) : « chacune mutée » → exception déclarée pour les gardes du script d'instance, jouées seulement à la répétition", "exactitude", "rapport du développeur v4, section 4"),
    ("H-3", "— → leçon R-1497 : variables du mandataire transmises à `vastai` par le lanceur, erreur de certificat = « non parvenu », sans marqueur", "leçon du jour", "message de la mère ; R-1497"),
    ("H-4", "section 2 : compléments de la liste de code v3 → plus les huit changements du code v4", "liste fermée", "contre-lecture du delta v3, « Changements de code requis »"),
    ("H-5", "« Contre-lecture » : reste celle du delta v3 → faite (« à reprendre ») ; reste celle du delta v4", "état", "contre-lecture du delta v3"),
    ("H-6", "pied du brouillon 3 → pied du brouillon 4", "état", "—"),
]


def table_0000() -> str:
    t = ["## 0000. Changements du brouillon 3 au brouillon 4 (avant → après ; raison ; source)", "",
         "K1 à K10 : les couples de la contre-lecture du delta v3 (`docs/notes/weight-space-programming-v1/"
         "contre-lecture-delta-v3-v1/couples-brouillon4-v1.json`, `838882eb…`), tous retenus (les changements de code qu'ils "
         "supposent sont faits en v4), appliqués dans l'ordre par script. H-1 à H-6 : changements demandés par la mère, "
         "appliqués ensuite par le même script, sous la même règle (`docs/notes/weight-space-programming-v1/"
         "brouillon4-addendum-1-v1/appliquer-couples-addendum-1-brouillon4-v1.py` et sa sortie, même dossier).", "",
         "| N° | Avant → après | Raison | Source |", "|---|---|---|---|"]
    t += [f"| K-{i} | {a} | {r} | {s} |" for i, (a, r, s) in enumerate(LIGNES_K, 1)]
    t += [f"| {n} | {a} | {r} | {s} |" for n, a, r, s in LIGNES_H]
    return "\n".join(t) + "\n\n---\n\n"


def changements_h(heure: str) -> list[tuple[str, str, str]]:
    return [
        ("H-1 titre", "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 3\n",
         "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 4\n"),
        ("H-1 date", "écrit le 4 novembre 2026 à partir de 22:28 UTC (`date -u`), toujours avant toute donnée.",
         "écrit le 4 novembre 2026 à partir de 22:28 UTC (`date -u`), toujours avant toute donnée. Brouillon 4 écrit le "
         f"4 novembre 2026 à partir de {heure} UTC (`date -u`), toujours avant toute donnée."),
        ("H-1 auteur", "(même dossier, compagnons « OK »).\n- Décision",
         "(même dossier, compagnons « OK »).\n- Brouillon 4 : même rédacteur-développeur ; brouillon 3 (`12e47e51…`) + les 10 "
         "couples de la contre-lecture du delta v3 + H-1 à H-6 (section 0000). Contre-lecture du delta v3 : "
         "`docs/notes/weight-space-programming-v1/contre-lecture-delta-v3-v1/contre-lecture-delta-v3-v1.md`, sha256 "
         "`cf2ffcb0…` (verdict « à reprendre : le code et la commande de répétition ; le texte est scellable après les 10 "
         "couples »), couples `couples-brouillon4-v1.json` `838882eb…` (même dossier, compagnons « OK »).\n- Décision"),
        ("H-0 table", "## 000. Changements du brouillon 2 au brouillon 3", table_0000() + "## 000. Changements du brouillon 2 au brouillon 3"),
        ("H-2 exception", "comme dans un conteneur).",
         "comme dans un conteneur ; exception déclarée : les gardes du script d'instance, `POUSSEE-VERIFIEE` et préfixe de la "
         "branche des sorties, ne se jouent qu'à la répétition jouet et ne sont pas mutées au banc)."),
        ("H-3 et H-4 compléments v4", "`docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v3.md`.",
         "`docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v3.md`.\n\n"
         "**Compléments à la liste (contre-lecture du delta v3, « Changements de code requis »).** Code v4, branche "
         "`prep/sparks-exp7-nul-v4`, descendant du code v3 (`4c3bf146`), fichiers neufs seulement : (1) `timeout` sur chaque "
         "étape de l'amorce avant le calcul et sur `vastai destroy` ; (2) attente du principal sur `$!` ; (3) branche des "
         "ordres `ordres/sparks-exp7-nul-v4-<commit court>`, clé `instance`, consignation contrôlée ; (4) `deja_usd` qui ne "
         "baisse jamais, borne propre de la machine ; (5) branches des sorties liées au commit et à l'ordre, préfixe "
         "`BRANCHE_PREFIXE` (`calcul/` ou `essai/`) ; (6) lanceur v4 : `timeout`, environnement de `vastai` nettoyé qui garde "
         "`HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY`, `SSL_CERT_FILE` et `REQUESTS_CA_BUNDLE` s'ils sont présents (R-1497, par leur "
         "nom, jamais leur valeur), sortie de `vastai` jamais affichée, marqueur de création incertaine, erreur de certificat "
         "= refus « non parvenu » sans marqueur, `--label` lié au commit ; (7) mutations manquantes ; (8) répétition jouet "
         "corrigée. La liste fermée v4 (`src/controle_ia/sparks_exp7_nul_v4/liste-fermee-v1.txt`) compte les fichiers v2, v3 "
         "et v4 ; la garde de lancement lit celle-ci. Fonction par fonction : "
         "`docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v4.md`."),
        ("H-5 contre-lecture", "(`git diff 50fb15cd..<commit>`, `rapport-developpeur-addendum-1-v3.md`), par un sous-agent neuf.",
         "(`git diff 50fb15cd..<commit>`, `rapport-developpeur-addendum-1-v3.md`), par un sous-agent neuf. Contre-lecture du "
         "delta v3 faite (`cf2ffcb0…`, « à reprendre ») : ses 10 couples sont appliqués ici (section 0000) et ses huit "
         "changements sont faits en v4 ; reste la contre-lecture du delta v4 (`git diff 4c3bf146..<commit>`, "
         "`rapport-developpeur-addendum-1-v4.md`), par un sous-agent neuf."),
        ("H-6 pied", "Brouillon 3 (4 novembre 2026, même rédacteur-développeur), sur le brouillon 2",
         "Brouillon 4 (4 novembre 2026, même rédacteur-développeur), sur le brouillon 3 (4 novembre 2026, même "
         "rédacteur-développeur), sur le brouillon 2"),
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
    b3, cp = (racine / B3).read_bytes(), (racine / COUPLES).read_bytes()
    if sha(b3) != SHA_B3 or sha(cp) != SHA_COUPLES:
        raise SystemExit("REFUS : empreinte d'entrée différente")
    print(f"entrées : brouillon 3 {sha(b3)} ; couples {sha(cp)}")
    texte = b3.decode("utf-8")
    for i, c in enumerate(json.loads(cp), 1):
        texte = appliquer(texte, f"K-{i}", c["ancien"], c["nouveau"])
    inter = sha(texte.encode("utf-8"))
    print(f"après les 10 couples : {inter} (texte d'essai du contre-lecteur : 4ea5636b…)")
    if not inter.startswith("4ea5636b"):
        raise SystemExit("REFUS : texte après les couples différent de celui du contre-lecteur")
    for nom, a, n in changements_h(heure):
        texte = appliquer(texte, nom, a, n)
    if texte.count(MARQUEUR) != 3:
        raise SystemExit(f"REFUS : {texte.count(MARQUEUR)} marqueurs (trois attendus)")
    sortie = racine / B4
    if sortie.exists():
        raise SystemExit(f"REFUS : {sortie} existe déjà (R12)")
    sortie.write_text(texte, encoding="utf-8")
    print(f"marqueurs « {MARQUEUR} » : 3")
    print(f"sortie : {B4} {sha(texte.encode('utf-8'))} ({len(texte.encode('utf-8'))} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
