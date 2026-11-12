"""Ordre d'exécution de l'étape A de T0.7, variante B, brouillon 5 : application au brouillon 4 des douze couples de la contre-lecture
R2 et des retouches déclarées de la mère (R-2258), puis vérifications (v1).

Rédacteur des brouillons 4 et 5 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 10 novembre
2026. Contre-lecture appliquée : `prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md` (`88ea9f06…`, Fable 5.2) ;
couples : `prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1-couples.json` (`cf2e4c98…`, clés `n`, `constat`,
`ancien`, `nouveau`). Bibliothèque standard et `bash -n` seulement ; aucun réseau, aucune clé, aucun `git`, aucun `vastai`.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie l'empreinte du brouillon 4 (`d5047be2…`) et celle des couples ;
2. applique les douze couples **tels qu'écrits**, dans l'ordre de `n` : chaque « ancien » présent exactement une fois au moment de
   son application et différent de son « nouveau » ; sinon arrêt (code 1), rien n'est écrit ;
3. vérifie l'empreinte du texte après les douze couples seuls : `f3256fd6…` (R-2258 ; contre-lecture, § 7) ; sinon arrêt ;
4. applique les retouches déclarées D-1 à D-10 (R-2258 : en-tête « brouillon 5 », contre-lu, « Non contre-lu » retiré ; `ATT`
   retrouvée sous Python 3.11.17 ; réserve CLE-12 ; S-8 à S-11 en réserve pour une v3 du script, le script v2 restant celui de
   l'ordre ; sources), même règle d'unicité ;
5. vérifie : titre ; « Non contre-lu » absent ; les dix marqueurs, une occurrence chacun, et aucun autre `<<…>>` ; blocs `bash`
   (`bash -n`, marqueurs remplacés par des valeurs factices) ; extraits `python3 -I -c '…'` des blocs (`ast.parse`) ; phrases
   exigées par chaque couple et chaque retouche présentes ;
6. écrit `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md` (R12 : refuse d'écraser un fichier différent ; un fichier
   identique est accepté). Le scellement se fait à part (`controle_ia.scellement sceller`).
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SHA_B4 = "d5047be2a1cc371917bc09352f66cd59f6a7d8b5d4f2c43e32d3c98a36f6d72c"
SHA_COUPLES = "cf2e4c982133e2ad662c7e67bd5eafe80ae783e32ec98e6cda42f524d1643fa5"
SHA_APRES_COUPLES = "f3256fd603e3d2c330245c9c4850b9a84064603bb9daee4fad46f7d8b9915de5"
CHEMIN_B4 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon4.md"
CHEMIN_COUPLES = "prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1-couples.json"
CHEMIN_B5 = "docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5.md"
TITRE_B5 = ("# Ordre d'exécution — étape A de T0.7, variante B (instance A100 neuve, activations recalculées) — v1, brouillon 5")
MARQUEURS = ["<<ID_SESSION_FILLE>>", "<<EMPREINTE_CONFIG_T07>>", "<<LIGNE_SCELLEMENT_T07>>", "<<DEPENSE_ANTERIEURE_USD>>",
             "<<RUN_T06_7B>>", "<<BRANCHE_7B>>", "<<COMMIT_CODE_T07>>", "<<COMMIT_SCELLEMENT_T07>>", "<<CHEMIN_CONFIG_T07>>",
             "<<PERIMETRE_T07>>"]
FACTICES = {"<<DEPENSE_ANTERIEURE_USD>>": "0", "<<RUN_T06_7B>>": "20261112-000000-t06-reel",
            "<<BRANCHE_7B>>": "calcul/t06-confirmation-7b-v1", "<<COMMIT_CODE_T07>>": "0" * 40,
            "<<COMMIT_SCELLEMENT_T07>>": "1" * 40, "<<CHEMIN_CONFIG_T07>>": "prereg/T0.7-configuration-v1.json",
            "<<PERIMETRE_T07>>": "JD,JA"}
CL1 = "`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1.md`"

RETOUCHES = [
    ("D-1", "en-tête : titre",
     "activations recalculées) — v1, brouillon 4\n",
     "activations recalculées) — v1, brouillon 5\n"),
    ("D-2", "en-tête : statut du brouillon 5",
     "- **Statut** : brouillon 4, écrit le 2026-11-10 à partir de 15:14 UTC (`date -u`) par un sous-agent développeur **neuf**",
     "- **Statut** : **brouillon 5**, écrit le 2026-11-10 à partir de 16:12 UTC (`date -u`) par le rédacteur du brouillon 4, qui\n"
     "  applique la contre-lecture R2 du brouillon 4 (" + CL1 + ",\n"
     "  `88ea9f0661e07a7840b10c060f1488a479efa9d01e82bbdbb643b72329c74704`, Fable 5.2) : ses **douze couples tels qu'écrits**\n"
     "  (`prereg/contre-lectures/ordre-execution-etape-a-t07-v1-brouillon4-cl1-couples.json`,\n"
     "  `cf2e4c982133e2ad662c7e67bd5eafe80ae783e32ec98e6cda42f524d1643fa5`), par le script\n"
     "  `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon5-appliquer-v1.py` (empreinte du texte après les douze seuls :\n"
     "  `f3256fd603e3d2c330245c9c4850b9a84064603bb9daee4fad46f7d8b9915de5`, vérifiée), puis les retouches **déclarées** D-1 à D-10\n"
     "  de ce script (R-2258 : en-tête ; `ATT` retrouvée sous Python 3.11.17 ; réserve CLE-12 ; S-8 à S-11 en réserve pour une v3\n"
     "  du script ; sources). Remplace le brouillon 4 (`d5047be2a1cc371917bc09352f66cd59f6a7d8b5d4f2c43e32d3c98a36f6d72c`, gardé\n"
     "  tel quel, R12). **Brouillon 4** : écrit le 2026-11-10 à partir de 15:14 UTC (`date -u`) par un sous-agent développeur **neuf**"),
    ("D-3", "en-tête : contre-lu, « Non contre-lu » retiré",
     "**Non contre-lu.** Le script v2 n'est pas modifié : ce que je propose d'y changer est au",
     "**Contre-lu** (R2, brouillon 4, `88ea9f06…`) : « scellable après corrections », aucun constat bloquant ; douze couples\n"
     "  appliqués ; `ATT` retrouvée sous Python 3.11.17 (§ 11 bis). Le script v2 n'est pas modifié et **reste celui de l'ordre**\n"
     "  (R-2255, R-2258) : ce que je propose d'y changer est au"),
    ("D-4", "§ 10 : jugés par la contre-lecture",
     "## 10. À juger par la contre-lecture\n",
     "## 10. Jugés par la contre-lecture R2 du brouillon 4 (`88ea9f06…`)\n\n"
     "Issues (contre-lecture, § 1 à § 6 ; décisions de la mère, R-2258) : aucun constat bloquant ; CLE-01 à CLE-08, CLE-10 et CLE-11\n"
     "appliqués par les couples 1 à 12 ; CLE-09 relève du candidat de T0.7 (aucun couple dans cet ordre) ; **CLE-12 accepté avec\n"
     "réserve** (§ 7). Points tels qu'ils étaient soumis :\n"),
    ("D-5", "§ 10.2 : ATT sous Python 3.11.17",
     "2. `ATT` : mesurée sous Python 3.13.16 et le paquet local (§ 11 bis) ;",
     "2. `ATT` : mesurée sous Python 3.13.16 et le paquet local (§ 11 bis), **retrouvée sous Python 3.11.17** par la contre-lecture\n"
     "   (même ligne, § 11 bis) ;"),
    ("D-6", "§ 7 : réserve CLE-12",
     "- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement.\n",
     "- Plafond (§ 6), minuterie, refus d'un contrôle ou d'un classifieur : arrêt, compte rendu ; aucun contournement.\n"
     "- **Réserve CLE-12** (acceptée par la mère, R-2258 ; dite à Lazar comme information) : une minuterie qui tombe pendant l'étape A\n"
     "  détruit une étape ouverte : nœud de dépense (écrit (b) 6 de T0.7), relance seulement sur un mot de Lazar. La marge entre le\n"
     "  pire cas du devis (10,9 h, § 6) et 12 h est de **1,1 h** (moins quand `HMAX` < 12 h, § 4.4) ; la durée réelle de l'étape A\n"
     "  **n'a jamais été mesurée** (la passe à blanc n'estime que l'extraction). Allonger la minuterie dépasserait le plafond de\n"
     "  20 USD fixé par Lazar.\n"),
    ("D-7", "§ 11 bis : mesure sous Python 3.11.17",
     "- **Commande de remesure** (si P12 échoue)",
     "- **Mesure de la contre-lecture R2 sous Python 3.11.17** (`88ea9f06…`, § 3 ; de 15:46:49 à 16:03:50 UTC, heures qu'elle\n"
     "  rapporte) : clone `--shared` du dépôt local aux motifs des étapes 2 et 3 du script, tête `709d16fc` (arbres `tests/`\n"
     "  `79230a58…` et `src/` `744a9e16…`), versions figées de `requirements-cpu.txt` (`torch` 2.14.1 en construction processeur),\n"
     "  commande exacte de l'étape 6 : **code 0, `346 passed, 2 skipped, 4 xfailed`** (1 019,6 s), mêmes deux sauts et mêmes quatre\n"
     "  échecs attendus, aucun avertissement, liste des essais `bd49a367…` égale à celle de la mesure ci-dessus. Les deux mesures se\n"
     "  complètent (atteignabilité depuis une seule branche : la première ; interpréteur de l'instance : la seconde) ; aucune ne joue\n"
     "  la construction carte de `torch` ni le git de l'image (S-1, S-2).\n"
     "- **Commande de remesure** (si P12 échoue)"),
    ("D-8", "§ 13 : S-2 réduit",
     "| S-2 | risque résiduel | Mesure sous Python 3.13.16 (bac à sable) ; l'instance joue Python 3.11 (image `python:3.11-bookworm`) "
     "et `requirements-gpu.txt` (mêmes versions figées, `torch` en construction carte). `python3.11` existe sur la machine de la "
     "session, sans `torch` : une mesure sous 3.11 demanderait d'y installer `torch` (≈ 1 Go ; disque serré). | la mère peut "
     "remesurer sous 3.11 avec la commande du § 11 bis, ou accepter le risque |",
     "| S-2 | risque résiduel, réduit | Mesure sous Python 3.13.16 (bac à sable), **retrouvée sous Python 3.11.17** par la "
     "contre-lecture R2 (§ 11 bis) ; l'instance joue Python 3.11 (image `python:3.11-bookworm`) et `requirements-gpu.txt` (mêmes "
     "versions figées, `torch` en construction carte). Restent la construction carte de `torch` et le git de l'image, qu'aucune "
     "mesure ne joue. | rien de plus avant le lancement (R-2255, R-2258) |"),
    ("D-9", "§ 13 : S-8 à S-11 en réserve pour une v3",
     "| S-7 | cosmétique | `essais-sauts.txt` porte deux fois certaines lignes `XFAIL` (résumé court de `-rsxX` et lignes de "
     "résultat). | sans effet sur la comparaison | rien |\n",
     "| S-7 | cosmétique | `essais-sauts.txt` porte deux fois certaines lignes `XFAIL` (résumé court de `-rsxX` et lignes de "
     "résultat). | sans effet sur la comparaison | rien |\n"
     "| S-8 | réserve v3 (R-2258) | Les trois « T07 REFUS » (l. 27, 34, 42) sortent par `exit 2`, avant la minuterie, sans demander "
     "l'état « stopped », sans date : invisibles au filtre du § 4.5 d'origine. | dater, journaliser et demander « stopped » | § 4.5 "
     "(couples 6 et 7) |\n"
     "| S-9 | réserve v3 (R-2258) | Après cinq `DELETE` en échec, la minuterie ne demande pas l'état « stopped » ; la carte continue. "
     "| demander « stopped » (voie que l'amorce de T0.6 emploie en fin de run) | § 6 (couple 4), § 4.7 |\n"
     "| S-10 | réserve v3 (R-2258) | Sur un écart de la ligne d'essais, `essais.txt` n'est ni poussé ni journalisé : la fille ne voit "
     "que la ligne. | écrire au journal les lignes `SKIPPED`, `XFAIL`, `FAILED`, `ERROR` | remesure (§ 11 bis) |\n"
     "| S-11 | réserve v3 (R-2258) | La garde du repli écrit `OUVERTURE-T07` au début de `repli-seul` ; la poussée ne vient qu'après "
     "le recalcul (l. 357-365) : une instance perdue dans l'intervalle emporte la ligne. | pousser le journal des ouvertures dès la "
     "garde | § 7 (couple 5) |\n\n"
     "S-8 à S-11 viennent de la contre-lecture R2 (`88ea9f06…`, § 5). Aucun des onze ne bloque l'étape A ; tous restent en réserve pour\n"
     "une v3 éventuelle (décision de la mère) ; **le script v2 (`e68d3306…`) reste celui de cet ordre** (R-2255, R-2258).\n"),
    ("D-10", "sources",
     "(R-2112, R-2115, R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249)",
     "(R-2112, R-2115, R-2153, R-2220, R-2229, R-2231, R-2241, R-2246, R-2249, R-2255, R-2258) ; contre-lecture R2 du brouillon 4\n"
     "(" + CL1 + ", `88ea9f06…`) et ses couples (`cf2e4c98…`)"),
]

# phrases que chaque retouche doit laisser dans le texte (contrôle final)
EXIGEES = ["— v1, brouillon 5", "**brouillon 5**", "douze couples tels qu'écrits", "f3256fd603e3d2c330245c9c4850b9a84064603bb9daee4fad46f7d8b9915de5",
           "**Contre-lu** (R2, brouillon 4", "**reste celui de l'ordre**", "## 10. Jugés par la contre-lecture R2 du brouillon 4",
           "**Réserve CLE-12**", "**1,1 h**", "**n'a jamais été mesurée**", "**Mesure de la contre-lecture R2 sous Python 3.11.17**",
           "| S-2 | risque résiduel, réduit |", "| S-8 | réserve v3", "| S-9 | réserve v3", "| S-10 | réserve v3", "| S-11 | réserve v3",
           "R-2255, R-2258) ; contre-lecture R2 du brouillon 4"]
ABSENTES = ["**Non contre-lu.**", "## 10. À juger par la contre-lecture", "— v1, brouillon 4\n"]


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def echec(motif: str) -> None:
    print(f"ÉCHEC : {motif}")
    sys.exit(1)


def remplacer(texte: str, ident: str, ancien: str, nouveau: str) -> str:
    n = texte.count(ancien)
    if n != 1:
        echec(f"{ident} : « ancien » présent {n} fois (une attendue)")
    if ancien == nouveau:
        echec(f"{ident} : « ancien » égal au « nouveau »")
    return texte.replace(ancien, nouveau)


def blocs_bash(texte: str) -> list[str]:
    return re.findall(r"```bash\n(.*?)```", texte, flags=re.S)


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        echec("usage : appliquer RACINE")
    racine = Path(argv[0]).resolve()
    b4 = (racine / CHEMIN_B4).read_bytes()
    if sha(b4) != SHA_B4:
        echec(f"brouillon 4 : empreinte {sha(b4)[:12]}… ≠ {SHA_B4[:12]}…")
    brut = (racine / CHEMIN_COUPLES).read_bytes()
    if sha(brut) != SHA_COUPLES:
        echec(f"couples : empreinte {sha(brut)[:12]}… ≠ {SHA_COUPLES[:12]}…")
    couples = json.loads(brut.decode("utf-8"))
    if [c["n"] for c in couples] != list(range(1, 13)):
        echec("couples : douze couples numérotés 1 à 12 attendus")
    texte = b4.decode("utf-8")
    for c in couples:
        texte = remplacer(texte, f"couple {c['n']} ({c['constat']})", c["ancien"], c["nouveau"])
    apres = sha(texte.encode("utf-8"))
    print(f"après les douze couples : {apres}")
    if apres != SHA_APRES_COUPLES:
        echec(f"empreinte après les douze couples {apres[:12]}… ≠ {SHA_APRES_COUPLES[:12]}… (R-2258)")
    for c in couples:
        if c["nouveau"] not in texte:
            echec(f"couple {c['n']} : « nouveau » absent après application")
    for ident, quoi, ancien, nouveau in RETOUCHES:
        texte = remplacer(texte, f"{ident} ({quoi})", ancien, nouveau)
        print(f"{ident} appliquée : {quoi}")
    # vérifications
    if texte.splitlines()[0] != TITRE_B5:
        echec("titre du brouillon 5")
    for m in MARQUEURS:
        if texte.count(m) != 1:
            echec(f"marqueur {m} : {texte.count(m)} occurrences (une attendue)")
    autres = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", texte)) - set(MARQUEURS))
    if autres:
        echec(f"marqueurs inattendus : {autres}")
    for p in EXIGEES:
        if p not in texte:
            echec(f"phrase exigée absente : {p!r}")
    for p in ABSENTES:
        if p in texte:
            echec(f"phrase retirée encore présente : {p!r}")
    for c in couples:
        if c["nouveau"] not in texte:
            echec(f"couple {c['n']} : « nouveau » absent du texte final")
    blocs = blocs_bash(texte)
    if len(blocs) != 8:
        echec(f"{len(blocs)} blocs bash (8 attendus)")
    n_py = 0
    with tempfile.TemporaryDirectory() as d:
        for k, b in enumerate(blocs, 1):
            for m, v in FACTICES.items():
                b = b.replace(m, v)
            p = Path(d) / f"bloc-{k}.sh"
            p.write_text(b, encoding="utf-8")
            r = subprocess.run(["bash", "-n", str(p)], capture_output=True, text=True)
            if r.returncode != 0:
                echec(f"bloc bash {k} : bash -n en échec : {r.stderr.strip()[:300]}")
            for extrait in re.findall(r"python3 -I -c '([^']*)'", b):
                try:
                    ast.parse(extrait)
                except SyntaxError as e:
                    echec(f"bloc bash {k} : extrait Python illisible ({e})")
                n_py += 1
    print(f"blocs bash : {len(blocs)}, bash -n sans erreur ; extraits Python : {n_py}, ast.parse sans erreur")
    sortie = racine / CHEMIN_B5
    octets = texte.encode("utf-8")
    if sortie.exists() and sortie.read_bytes() != octets:
        echec(f"{CHEMIN_B5} existe avec un autre contenu (R12)")
    if not sortie.exists():
        sortie.write_bytes(octets)
    print(f"écrit : {CHEMIN_B5} ({sha(octets)})")
    print("TOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
