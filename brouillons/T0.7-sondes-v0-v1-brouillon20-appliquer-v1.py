"""T0.7 sondes v0, brouillon 20 : application des couples au brouillon 19 et vérifications (v1).

Rédacteur du brouillon 20 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), 10 novembre 2026 ;
consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-redaction-t07-brouillon20-v1.md` (`caf4bce5…`),
plus le message de la mère reçu vers 07:12 UTC (GO_ETAPE_A_T07 = GO-2026-11-10-04 ; devis selon cette ligne).
Bibliothèque standard, plus `controle_ia.prereg` du dépôt (lu dans RACINE/src) ; aucun réseau, aucune clé, aucun appel externe.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie l'empreinte du brouillon 19 (`07039ed2…`) et celle des couples (`b438549a…`) ;
2. applique dans l'ordre les couples de `brouillons/T0.7-sondes-v0-v1-brouillon20-couples-v1.json` (clés `id`, `section`,
   `motif`, `ancien`, `nouveau`) : chaque « ancien » doit être présent exactement une fois dans le texte au moment de son
   application, et différent de son « nouveau », sinon arrêt (code 1), rien n'est écrit ;
3. écrit `brouillons/T0.7-sondes-v0-v1-brouillon20.md` (R12 : refuse d'écraser un fichier différent ; un fichier identique est
   accepté) ;
4. vérifie : titre et premier statut au brouillon 20 ; sections (a), (c) et (d) de « Écrits exigés par P3-bis » égales octet pour
   octet au brouillon 19, (b) différente au seul point 6 ; sections de l'empan « Hypothèse » à « Liste d'arrêt » égales hors de
   « Écrits exigés par P3-bis » et de « Liste d'arrêt » (différences imprimées) ; sections neuves et disparues ; marqueurs
   restants = les neuf attendus, les cinq du code et de l'ordre une fois chacun ; marqueurs remplis absents et leurs valeurs
   présentes ; `controle_ia.prereg.problemes` réduit à la ligne des neuf marqueurs ; liste vide à valeurs factices (copie dans
   DOSSIER_TEMPORAIRE, ou un dossier temporaire neuf) ; phrases exigées par la consigne présentes (règle de CT-01, commande,
   douze modules, quatre fichiers d'essais, devis) ; différentiel compté.
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

SHA_B19 = "07039ed28065e835b0c6b5ca150438cd8b3bfb3927833009aaa8b31855c5b1ad"
SHA_COUPLES = "b438549a00bab4f5b02f57a5d0442bef0dda0b6ab90cd6e52a13afd2a798c858"
SHA_T06 = "ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169"
TITRE_20 = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — brouillon 20"
UNE_FOIS = ["<<COMMIT_CODE_T07>>", "<<EMPREINTES_CODE_T07>>", "<<T7P10_SONDES_P3>>", "<<REPLI_RECALCUL_T07>>",
            "<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>"]
RESTENT = ["<<ENTROPIE_T07>>", "<<EMPREINTE_CONFIG_T07>>", "<<MOT_LAZAR_P064>>", "<<MOT_LAZAR_P065>>"]
ATTENDUS = sorted(UNE_FOIS + RESTENT)
REMPLIS = {"<<EMPREINTE_PREREG_T06>>": SHA_T06, "<<GO_ETAPE_A_T07>>": "GO-2026-11-10-04"}
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
TOUCHEES_DECLAREES = ("Écrits exigés par P3-bis", "Liste d'arrêt")
TABLE_NEUVE = "Table « ce qui change du 19 au 20 »"
PHRASES = (
    # règle de CT-01 (consigne, point 2)
    "**le témoin lexical du concept est écrit « échec »**",
    "**T7-P10 est « non lue : témoin lexical en échec » pour ce concept**",
    "**l'étape A continue**",
    # commande et fichiers (consigne, point 2)
    "python -m controle_ia.t07.lecture_v2 etape-a RACINE RUN_T06 CONFIG_T07",
    "`… empreinte-config CONFIG_T07`",
    "`garde_adaptee_v1.py`", "`journal_p3bis_v1.py`", "`lectures_t07_v1.py`", "`repli_v1.py`", "`sondes_neuves_v1.py`",
    "`tests/test_t07_lecture_v2.py`", "`tests/test_t07_sondes_neuves_v1.py`", "`tests/test_t07_repli_v1.py`",
    "**`niveau_base_t06`** (0,95", "**`scores_base_t06`** (nul sous « égalité »)",
    "**Q11** (arrêt de T0.6 sans", "**la lettre est gardée**",
    "est écrite dans `notation-t07.json` à la fin de l'étape A",
    "il ne porte donc pas leurs noms complets (famille, couche)",
    "**première ligne** `{\"format_lecture\": \"message_utilisateur\"}`",
    # devis (message de la mère)
    "- **Plafond : 20 USD** pour l'étape A sur l'instance de 7b",
    "**seulement après un mot de Lazar**",
    "détruit l'instance au plus tard le 17 novembre 2026 à 00:00 UTC",
    # calendrier (consigne, point 6)
    "**option (c) de Lazar** (R-2079)",
    "création **au plus tard le 15 novembre 2026**",
)
ABSENTES = (
    "- Commit du code d'analyse : `51a1874c",
    "empreintes au commit ci-dessus (**brouillon 18, provisoires**",
    "`python -m controle_ia.t07.lecture_v1\netape-a",
    "- **Plafond : 10 USD** pour la lecture de T0.7",
)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sections(texte: str) -> dict:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def bloc(texte: str, debut: str, fin: str) -> str:
    i = texte.index(debut)
    return texte[i:texte.index(fin, i)]


def section_de(texte: str, position: int) -> str:
    nom = "(avant la première section)"
    for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M):
        if m.start() <= position:
            nom = m.group(1)
    return nom[:70]


def lignes_diff(a: str, b: str) -> list:
    return [l for l in difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # noqa: E402

    b19 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon19.md"
    couples_chemin = racine / "brouillons/T0.7-sondes-v0-v1-brouillon20-couples-v1.json"
    b20 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon20.md"
    defauts = []

    brut = b19.read_bytes()
    if sha(brut) != SHA_B19:
        print(f"ARRÊT : empreinte du brouillon 19 {sha(brut)} ≠ {SHA_B19}")
        return 1
    print(f"brouillon 19 : {b19.relative_to(racine)} {SHA_B19} (égale)")
    texte19 = brut.decode("utf-8")
    cbrut = couples_chemin.read_bytes()
    if sha(cbrut) != SHA_COUPLES:
        print(f"ARRÊT : empreinte des couples {sha(cbrut)} ≠ {SHA_COUPLES}")
        return 1
    couples = json.loads(cbrut.decode("utf-8"))
    print(f"couples : {couples_chemin.relative_to(racine)} {SHA_COUPLES} (égale ; {len(couples)} couples)")
    for c in couples:
        if sorted(c) != ["ancien", "id", "motif", "nouveau", "section"]:
            print(f"ARRÊT : {c.get('id')} : clés {sorted(c)}")
            return 1

    # 2. application
    t = texte19
    print("\n# application (id ; occurrences de l'« ancien » ; ligne d'application dans le texte courant ; section ; empan gelé)")
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu) ; rien n'est écrit")
            return 1
        if c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « nouveau » égal à « ancien »")
            return 1
        p = t.index(c["ancien"])
        sec = section_de(t, p)
        gele = any(sec.startswith(g) for g in EMPAN_GELE)
        print(f"{c['id']} ; 1 ; l. {t.count(chr(10), 0, p) + 1} ; {sec} ; {'OUI' if gele else 'non'}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    texte20 = t

    # 3. écriture (R12)
    octets20 = texte20.encode("utf-8")
    if b20.exists():
        if b20.read_bytes() != octets20:
            print(f"ARRÊT (R12) : {b20.relative_to(racine)} existe et diffère : rien n'est écrasé")
            return 1
        print(f"\n{b20.relative_to(racine)} déjà écrit, identique")
    else:
        b20.write_bytes(octets20)
        print(f"\nécrit : {b20.relative_to(racine)}")
    print(f"brouillon 20 : {sha(octets20)} ; {texte20.count(chr(10))} lignes")

    # 4. vérifications
    print("\n# vérifications")
    premiere = texte20.split("\n", 1)[0]
    statut = next(l for l in texte20.split("\n") if l.startswith("- Statut :"))
    ok_titre = premiere == TITRE_20 and statut.startswith("- Statut : **brouillon 20**")
    print(f"(1) titre et premier statut au brouillon 20 : {ok_titre}")
    if not ok_titre:
        defauts.append("titre ou statut")

    debuts = {"(a)": "### (a) Périmètre fermé des clés", "(b)": "### (b) Règles de lancement et de relance",
              "(c)": "### (c) Engagement de jouer l'étape A", "(d)": "### (d) Garde adaptée à l'ouverture réduite",
              "(e)": "### (e) Grille de lecture"}
    noms = list(debuts)
    for k, nom in enumerate(noms[:-1]):
        a19 = bloc(texte19, debuts[nom], debuts[noms[k + 1]])
        a20 = bloc(texte20, debuts[nom], debuts[noms[k + 1]])
        if nom == "(b)":
            d = lignes_diff(a19, a20)
            print(f"(2) écrit (b) : {len(d)} lignes de différence :")
            for l in d:
                print(f"      {l[:200]}")
            if not d or any(not (l[1:].startswith("6. **Dépense**") or l[1:].startswith("   refusé → nœud")) for l in d):
                defauts.append("(b) changé hors du point 6")
        else:
            egal = a19 == a20
            print(f"(2) écrit {nom} : égal octet pour octet au brouillon 19 : {egal}")
            if not egal:
                defauts.append(f"écrit {nom} changé")

    s19, s20 = sections(texte19), sections(texte20)
    neuves = [k for k in s20 if k not in s19]
    disparues = [k for k in s19 if k not in s20]
    changees = [k for k in s19 if k in s20 and s19[k] != s20[k]]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != [TABLE_NEUVE] or disparues:
        defauts.append("sections neuves ou disparues inattendues")
    print(f"    sections changées ({len(changees)}) :")
    for k in changees:
        gele = any(k.startswith(g) for g in EMPAN_GELE)
        print(f"      - {k[:90]}{'  [EMPAN GELÉ]' if gele else ''}")
    geles = [k for k in changees if any(k.startswith(g) for g in EMPAN_GELE)]
    hors = [k for k in geles if not k.startswith(TOUCHEES_DECLAREES)]
    if hors:
        defauts.append(f"section de l'empan gelé touchée hors déclaration : {hors}")
    for k in geles:
        d = lignes_diff(s19[k], s20[k])
        print(f"    empan gelé, « {k[:40]}… » : {len(d)} lignes de différence :")
        for l in d:
            print(f"      {l[:240]}{' […]' if len(l) > 240 else ''}")
    print(f"    sections de l'empan gelé inchangées : "
          f"{[k[:40] for k in s19 if any(k.startswith(g) for g in EMPAN_GELE) and k not in changees]}")

    restes = sorted(set(GABARIT.findall(texte20)))
    comptes = {m: texte20.count(m) for m in restes}
    print(f"(4) marqueurs restants : {len(restes)} : {comptes}")
    if restes != ATTENDUS:
        defauts.append(f"marqueurs restants {restes} ≠ {ATTENDUS}")
    for m in UNE_FOIS:
        if texte20.count(m) != 1:
            defauts.append(f"{m} présent {texte20.count(m)} fois (1 attendu)")
    for m, valeur in REMPLIS.items():
        print(f"    {m} : absent {m not in texte20} ; valeur présente {texte20.count(valeur)} fois")
        if m in texte20 or valeur not in texte20:
            defauts.append(f"{m} non rempli")

    p = problemes(b20)
    attendu = [f"marqueurs de gabarit restants : {', '.join(ATTENDUS)}"]
    print(f"(5) controle_ia.prereg.problemes(brouillon 20) : {p}")
    if p != attendu:
        defauts.append("problemes ≠ la seule ligne des marqueurs voulus")
    dossier = Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-b20-factice-"))
    dossier.mkdir(parents=True, exist_ok=True)
    factice = texte20
    for m in ATTENDUS:
        factice = factice.replace(m, "valeur-factice-" + m.strip("<>").lower())
    copie = dossier / "T0.7-sondes-v0-v1-brouillon20-valeurs-factices.md"
    copie.write_text(factice, encoding="utf-8")
    pf = problemes(copie)
    print(f"(6) à valeurs factices ({copie}) : problemes = {pf}")
    if pf:
        defauts.append("problemes non vide à valeurs factices")

    plat = " ".join(texte20.split())
    manquantes = [ph for ph in PHRASES if " ".join(ph.split()) not in plat]
    print(f"(7) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)} présentes"
          f"{' ; manquantes : ' + repr(manquantes) if manquantes else ''}")
    if manquantes:
        defauts.append("phrases exigées manquantes")
    presentes = [ph for ph in ABSENTES if ph in texte20]
    print(f"    passages retirés encore présents : {presentes}")
    if presentes:
        defauts.append("passages retirés encore présents")

    d = lignes_diff(texte19, texte20)
    print(f"(8) différentiel 19 → 20 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées")

    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
