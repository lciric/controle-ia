"""Brouillon 3 de l'addendum n° 1 à SPARKS-EXP7-NUL : brouillon 2 + les 11 couples de la contre-lecture du delta v2,
appliqués dans l'ordre, puis G-1 à G-6 (minuterie et redémarrages, code v3), même règle : chaque « ancien » doit
apparaître exactement une fois au moment de son application, sinon refus. Les trois marqueurs « À REMPLIR » restent.

    python3 -I -B appliquer-couples-addendum-1-brouillon3-v1.py RACINE_DU_DEPOT HEURE_UTC
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SHA_B2 = "7e98397e53784637c03c1f1f7450e582c25939a46d15ca53380ebf8b70958170"
SHA_COUPLES = "58321f8d35cec9f882bb71cdd548f830ac47565c96f1c5e4876ec5d9a2584bc9"
B2 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon2.md"
B3 = "prereg/SPARKS-EXP7-NUL-addendum-1-brouillon3.md"
COUPLES = "docs/notes/weight-space-programming-v1/contre-lecture-delta-v2-v1/couples-brouillon3-v1.json"
MARQUEUR = "À REMPLIR"

LIGNES_E = [
    ("ligne de destruction : « par son identifiant » → `vastai destroy instance <id> -y`, aucune sortie brute, ou destruction par la machine après poussée vérifiée", "leçon du 4 novembre (R-1480, R-1482)", "couple 1 ; contre-lecture du delta v2, point 10"),
    ("— → ligne d'arrêt « aucune session vivante » (borne sur la machine, minuterie, borne résiduelle du stockage, tir réel avant la création)", "R-1481 : aucune garde qui passe par un modèle n'en est indépendante", "couple 2 ; points 22 et 23"),
    ("générateurs des secondaires de l'incrément : non écrits → ceux du principal, après lui, ordre écrit", "R9", "couple 3 ; point 14"),
    ("rappel de forme : « un » → « un, pour toute faute, composants compris »", "lecture retenue du développeur", "couple 4 ; point 11"),
    ("format de conversation au secours : jeton de début retiré en tête, essai d'égalité des jetons", "lecture retenue du développeur", "couple 5 ; point 15"),
    ("égalité des lots : un essai → deux (fractions sur l'instance, repli déclaré ; parts et « porteur » parmi les essais, sans repli) ; état lu par la garde avant la création", "écart plus strict, écrit", "couple 6 ; points 16 et 24"),
    ("nom du texte scellé non dit → `prereg/SPARKS-EXP7-NUL-addendum-1.md`, compagnon, commit descendant du code", "exigé par la garde du code", "couple 7 ; point 17"),
    ("répétition jouet : création seule → création, redémarrage de copie, phase causale, minuterie", "chemin de redémarrage", "couple 8 ; points 21 et 28"),
    ("liste fermée : `--name-status` → `--name-status --no-renames`, compagnons et liste comptés, égalité au scellement", "contrôle exact", "couple 9 ; point 19"),
    ("comptes : « essais et banc » → tout run compté, runs incomplets et banc à 49 sur 50 compris", "R4", "couple 10"),
    ("borne de l'amorce : création seule → chaque démarrage, dépense imputée passée à chaque démarrage", "chemin de redémarrage", "couple 11 ; point 23"),
]
LIGNES_G = [
    ("G-1", "en-tête du brouillon 2 → brouillon 3, contre-lecture du delta v2 et empreintes", "R6", "message de la mère du 4 novembre (≈ 22:15 UTC)"),
    ("G-2", "— → table A-22 et A-23 (minuterie, redémarrages sur ordre écrit)", "changements à v1 déclarés", "contre-lecture du delta v2, points 21 et 22"),
    ("G-3", "— → section « Minuterie de destruction et redémarrages »", "chemin de redémarrage et borne sur la machine écrits avant toute donnée", "points 21 à 23 ; message de la mère"),
    ("G-4", "section 2 : compléments de la liste de code → plus les six changements du code v3", "liste fermée", "contre-lecture du delta v2, « Changements de code requis »"),
    ("G-5", "« Contre-lecture » : reste la contre-lecture du delta v2 → faite (« à reprendre, sur le code ») ; reste celle du delta v3", "état", "contre-lecture du delta v2"),
    ("G-6", "pied du brouillon 2 → pied du brouillon 3", "état", "—"),
]

SECTION = """## Minuterie de destruction et redémarrages (écarts E-4 et E-5 ; contre-lecture du delta v2, points 21 à 23)

- **Une amorce, relancée à chaque démarrage.** `vastai start` relance les arguments du conteneur, donc l'amorce (`scripts/amorce_instance_sparks_exp7_nul_v3.sh`), avec l'environnement fixé à la création. L'amorce distingue la création (aucun dépôt sur le disque) du redémarrage (disque existant ; commit du disque égal à `COMMIT`, sinon refus).
- **Minuterie, en tout premier, sans Python.** Avant tout clone et tout calcul, l'amorce exige `curl` et `git` (absents : refus visible, rien ne part), puis lance, détachée (`setsid`), une minuterie en bash et `curl` seuls. Son échéance absolue `ECHEANCE_UTC_S` est posée à la création, au plus la fin du 18 novembre 2026 (1795046400), et gardée sur le disque : un redémarrage garde l'échéance d'origine. À l'échéance, ou dès que la machine pose le fichier `sparks-v3-detruire`, la minuterie appelle `DELETE /instances/<CONTAINER_ID>/` de l'interface de programmation de Vast, avec la clé du conteneur. En repli, si `vastai` est sur la machine, elle lance `vastai destroy instance <id> -y` (R-1482), sortie non gardée (R-1480). Elle recommence chaque minute pendant 30 minutes, puis écrit une alarme au journal. Identifiant illisible : aucun geste. Le code ne demande **jamais l'arrêt** de la machine (il tuerait la minuterie) : quand une destruction est due, le processus principal attend la fin de la minuterie.
- **Qui pose `sparks-v3-detruire`.** L'amorce : (i) à la fin du contrôle causal, seulement si les sorties sont poussées et la poussée vérifiée (tête distante égale à la tête locale, fichier `POUSSEE-VERIFIEE`) ; sinon, pas de destruction, le conteneur sort, nœud de Lazar ; (ii) sur ordre « fin » ; (iii) à tout démarrage à partir de l'échéance (aucun calcul).
- **Ordres écrits.** Rien de neuf ne passe par l'environnement. Avant chaque redémarrage, la session écrit `ordres/ordre-NNN.json` (numéros croissants) sur la branche `calcul/sparks-exp7-nul-v3-ordres`, puis redémarre. L'amorce lit l'ordre à la tête de cette branche, le valide (`redemarrage.py` : phase « copie », « causal » ou « fin » ; clés fermées ; numéro égal au nom du fichier ; un numéro déjà exécuté refuse, rien ne part) et le consigne fait avant d'agir. Le champ `deja_usd` (dépense imputée par la session) est **relu à chaque démarrage** pour la borne de durée (ligne du devis).
- **Copie.** Ordre « copie » : 1 à 4 cas (identifiants internes, publics), `premier` (le premier lot porte aussi les couches du départ et les rapports de fabrication), `copie_minutes` de 5 à 60. L'amorce lie en dur les couches des modèles des cas dans `lots/lot-NNN/`, avec un manifeste d'empreintes, garde le conteneur en vie `copie_minutes`, puis sort. La session copie (`vastai copy`), vérifie le manifeste (`sha256sum -c`), puis sert. Refus si la borne de durée est sous `copie_minutes` + 5 minutes.
- **Phase causale.** Ordre « causal » : la clé ouverte scellée et les réponses scellées sont sur la branche des ordres (`ordres/causal/`). L'amorce lance la phase causale sous `timeout` (borne d'au moins 60 minutes), puis la destruction si la poussée est vérifiée.
- **Ce que la machine ne borne pas.** Le stockage d'une instance arrêtée, puisque rien n'y tourne : il n'est borné que par la durée de l'absence de toute session (prix horaire du stockage × durée, 0,53 à 1,20 USD par jour aux prix du devis) et par la minuterie au démarrage suivant. Une machine qui ne lance jamais son amorce n'est bornée que par une session (ligne « aucune session vivante » de la liste d'arrêt).
- **Épreuves.** Minuterie, amorce et redémarrages sont éprouvés sur processeur, contre un dépôt d'essai local, `curl` et `vastai` simulés, sans réseau : cas sain et artefact pour chaque garde (`tests/test_sparks_exp7_nul_v3.py`, banc v3). Restent, avant le scellement : le **tir réel de la minuterie avant la création** (R-1477) et la répétition jouet complète (création, redémarrage de copie, phase causale) par la session reliée au dépôt distant.

"""


def table_000() -> str:
    t = ["## 000. Changements du brouillon 2 au brouillon 3 (avant → après ; raison ; source)", "",
         "E-1 à E-11 : les couples de la contre-lecture du delta v2 (`docs/notes/weight-space-programming-v1/"
         "contre-lecture-delta-v2-v1/couples-brouillon3-v1.json`, `58321f8d…`), appliqués dans l'ordre par script, chaque "
         "« ancien » unique au moment de son application. G-1 à G-6 : changements demandés par la mère après cette "
         "contre-lecture, appliqués ensuite par le même script, sous la même règle (`docs/notes/weight-space-programming-v1/"
         "brouillon3-addendum-1-v1/appliquer-couples-addendum-1-brouillon3-v1.py` et sa sortie, même dossier).", "",
         "| N° | Avant → après | Raison | Source |", "|---|---|---|---|"]
    t += [f"| E-{i} | {a} | {r} | {s} |" for i, (a, r, s) in enumerate(LIGNES_E, 1)]
    t += [f"| {n} | {a} | {r} | {s} |" for n, a, r, s in LIGNES_G]
    return "\n".join(t) + "\n\n---\n\n"


def changements_g(heure: str) -> list[tuple[str, str, str]]:
    return [
        ("G-1 titre", "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 2\n",
         "# Addendum n° 1 au préenregistrement SPARKS-EXP7-NUL — brouillon 3\n"),
        ("G-1 date", "Brouillon 2 écrit le 4 novembre 2026 à partir de 08:37 UTC (`date -u`), toujours avant toute donnée.",
         "Brouillon 2 écrit le 4 novembre 2026 à partir de 08:37 UTC (`date -u`), toujours avant toute donnée. Brouillon 3 "
         f"écrit le 4 novembre 2026 à partir de {heure} UTC (`date -u`), toujours avant toute donnée."),
        ("G-1 auteur", "(section 00).\n- Décision",
         "(section 00).\n- Brouillon 3 : même rédacteur-développeur que le brouillon 2 (il n'a écrit aucune contre-lecture) ; "
         "brouillon 2 (`7e98397e…`) + les 11 couples de la contre-lecture du delta v2 + G-1 à G-6 (section 000). Contre-lecture "
         "du delta v2 : `docs/notes/weight-space-programming-v1/contre-lecture-delta-v2-v1/contre-lecture-delta-v2-v1.md`, "
         "sha256 `578fd025bf4a46fd075631eb5beed026a8e6f9e5358a15c72e0fc7ff3c2ea9cc` (verdict « à reprendre, sur le code ; le "
         "texte est scellable après les 11 couples »), couples `couples-brouillon3-v1.json` `58321f8d…` (même dossier, "
         "compagnons « OK »).\n- Décision"),
        ("G-0 table", "## 00. Changements du brouillon 1 au brouillon 2", table_000() + "## 00. Changements du brouillon 1 au brouillon 2"),
        ("G-2 lignes A", "| Situe l'apport du lecteur là où la base se trompe | décision D-2 |",
         "| Situe l'apport du lecteur là où la base se trompe | décision D-2 |\n"
         "| A-22 | Destruction par une session seule → **minuterie de destruction sur la machine** (échéance absolue, ordre de la machine après poussée vérifiée) | R-1481 : borne sans session vivante | contre-lecture du delta v2, point 22 ; section « Minuterie de destruction et redémarrages » |\n"
         "| A-23 | Redémarrages de copie et phase causale sans voie exécutable → **ordres écrits** sur une branche du dépôt, lus à chaque démarrage | Un redémarrage garde l'environnement de la création | contre-lecture du delta v2, point 21 ; même section |"),
        ("G-4 compléments v3", "Fonction par fonction : `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v2.md`.",
         "Fonction par fonction : `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v2.md`.\n\n"
         "**Compléments à la liste (contre-lecture du delta v2, « Changements de code requis »).** Code v3, branche "
         "`prep/sparks-exp7-nul-v3`, descendant du code v2 (`50fb15cd`) et donc de `55399606`, fichiers neufs seulement : (1) "
         "chemin de redémarrage (amorce v3, `redemarrage.py` : ordres écrits, lots de copie, phase causale, `deja_usd` relu à "
         "chaque démarrage) ; (2) minuterie de destruction sur la machine, sans Python, lancée en tout premier par l'amorce "
         "(section « Minuterie de destruction et redémarrages ») ; (3) secondaire « sur M5 » (`analyse.m5_secondaire`) ; (4) a "
         "priori de B3 = −1 au construit inversé (`bases.orientation_b3`, transmis par `instance.bases_etalonnage`) ; (5) essai "
         "d'égalité des jetons du format de conversation ; (6) mutations manquantes (point 26, scripts compris) et « tuée » au "
         "seul code 1 avec « failed ». La liste fermée v3 (`src/controle_ia/sparks_exp7_nul_v3/liste-fermee-v1.txt`) compte les "
         "fichiers v2 et v3 ; la garde de lancement lit celle-ci. Fonction par fonction : "
         "`docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v3.md`."),
        ("G-3 section", "## Devis (variante carte graphique louée ; pire cas)", SECTION + "## Devis (variante carte graphique louée ; pire cas)"),
        ("G-5 contre-lecture", "(dix points en tête).",
         "(dix points en tête). Contre-lecture du delta v2 faite (`578fd025…`, « à reprendre, sur le code ») : ses 11 couples "
         "sont appliqués ici (section 000) et ses six changements de code sont faits en v3 ; reste la contre-lecture du delta "
         "v3 (`git diff 50fb15cd..<commit>`, `rapport-developpeur-addendum-1-v3.md`), par un sous-agent neuf."),
        ("G-6 pied", "Brouillon 2 (4 novembre 2026, rédacteur-développeur neuf), sur le brouillon 1",
         "Brouillon 3 (4 novembre 2026, même rédacteur-développeur), sur le brouillon 2 (4 novembre 2026, rédacteur-développeur "
         "neuf), sur le brouillon 1"),
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
    b2, cp = (racine / B2).read_bytes(), (racine / COUPLES).read_bytes()
    if sha(b2) != SHA_B2 or sha(cp) != SHA_COUPLES:
        raise SystemExit("REFUS : empreinte d'entrée différente")
    print(f"entrées : brouillon 2 {sha(b2)} ; couples {sha(cp)}")
    texte = b2.decode("utf-8")
    for i, c in enumerate(json.loads(cp), 1):
        texte = appliquer(texte, f"E-{i}", c["ancien"], c["nouveau"])
    inter = sha(texte.encode("utf-8"))
    print(f"après les 11 couples : {inter} (texte d'essai du contre-lecteur : e5535c96…)")
    if not inter.startswith("e5535c96"):
        raise SystemExit("REFUS : texte après les couples différent de celui du contre-lecteur")
    for nom, a, n in changements_g(heure):
        texte = appliquer(texte, nom, a, n)
    if texte.count(MARQUEUR) != 3:
        raise SystemExit(f"REFUS : {texte.count(MARQUEUR)} marqueurs (trois attendus)")
    sortie = racine / B3
    if sortie.exists():
        raise SystemExit(f"REFUS : {sortie} existe déjà (R12)")
    sortie.write_text(texte, encoding="utf-8")
    print(f"marqueurs « {MARQUEUR} » : 3")
    print(f"sortie : {B3} {sha(texte.encode('utf-8'))} ({len(texte.encode('utf-8'))} octets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
