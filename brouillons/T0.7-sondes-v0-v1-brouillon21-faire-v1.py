"""T0.7 sondes v0, brouillon 21 : application des couples CL20 et B21 au brouillon 20, et vérifications (v1).

Rédacteur du brouillon 21 (sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), 10 novembre 2026 ;
message de la mère (dix points), méthode de la consigne du brouillon 20 (`caf4bce5…`), messages de la mère reçus pendant le
travail (R-2155 puis R-2158 : option (c) des phrases des concepts, appliquée dans ce brouillon).
Bibliothèque standard, plus `controle_ia.prereg` du dépôt (lu dans RACINE/src) et `git` en lecture (`git show`) ; aucun réseau.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie l'empreinte du brouillon 20 (`9ef671ac…`), celle des couples de la contre-lecture 1 du brouillon 20 (`dc704bfe…`) et
   celle des couples B21 ;
2. applique dans l'ordre les dix couples CL20 tels quels, contrôle le texte obtenu (`34cb0985…`, celui du contre-lecteur), puis
   les couples B21 ; chaque « ancien » présent exactement une fois au moment de son application et différent de son « nouveau »,
   sinon arrêt (code 1), rien n'est écrit ;
3. écrit `brouillons/T0.7-sondes-v0-v1-brouillon21.md` (R12 : refuse d'écraser un fichier différent) ;
4. vérifie : titre et premier statut ; (c) et (d) de « Écrits exigés par P3-bis » égales octet pour octet au brouillon 20, (a)
   changée au seul point 1, (b) aux seuls points 1 et 6 ; empan « Hypothèse » à « Liste d'arrêt » : seules « Plan d'analyse »,
   « Écrits », « Critères » et « Liste d'arrêt » changent (différences imprimées) ; sections neuves et disparues ; marqueurs
   restants = les trois attendus ; marqueurs remplis absents ; dix-huit empreintes du texte égales à `git show 8ae9fc44:…` ;
   `problemes` réduit à la ligne des trois marqueurs, vide à valeurs factices ; phrases exigées présentes, passages retirés
   absents ; différentiel compté.
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SHA_B20 = "9ef671ac08ba79a43fa4fecfb7740bc6b5769587741ae378dc2935a02caf69da"
SHA_CL20 = "dc704bfea75588bfe85ed8d804d8f9f5ad414fcceaa184993583643c7b906ef2"
SHA_APRES_CL20 = "34cb098507d3146a0d884504317b7f4d71a00012bc2fbca36b7d6a91ea55e6ff"
SHA_B21_COUPLES = "9ca5edc8c7b76cdecd2dc58e905accc2c945d502a605cd570feffac997635444"
TITRE_21 = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — brouillon 21"
ATTENDUS = sorted(["<<ENTROPIE_T07>>", "<<EMPREINTE_CONFIG_T07>>", "<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>"])
UNE_FOIS = ["<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>"]
REMPLIS = ["<<COMMIT_CODE_T07>>", "<<EMPREINTES_CODE_T07>>", "<<T7P10_SONDES_P3>>", "<<REPLI_RECALCUL_T07>>",
           "<<MOT_LAZAR_P064>>", "<<MOT_LAZAR_P065>>"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
TOUCHEES_DECLAREES = ("Plan d'analyse", "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
TABLE_NEUVE = "Table « ce qui change du 20 au 21 »"
DECISIONS_20 = "Décisions DS-1 et DS-2 — défauts confirmés ; DS-3 — tranchée par Lazar (N-063 v2, option (b)) ; P-064 et P-065 — proposées ; garde adaptée — tranchée par Lazar (N-066, option 1)"
DECISIONS_21 = "Décisions DS-1 et DS-2 — défauts confirmés ; DS-3 — tranchée par Lazar (N-063 v2, option (b)) ; P-064 et P-065 — défauts (R-1902) ; garde adaptée — tranchée par Lazar (N-066, option 1) ; DS-3 bis — accordée par Lazar (R-2104, option (a))"
COMMIT = "8ae9fc44df4599af1e036e979af46aa8fa8f6185"
MODULES = ["__init__.py", "code_t07_v1.py", "controle_jeux_v1.py", "criteres_v1.py", "donnees_p3_t07_v1.py", "garde_adaptee_v1.py",
           "journal_p3bis_v1.py", "lecture_v1.py", "lecture_v2.py", "lectures_t07_v1.py", "mahalanobis_v1.py", "passe_blanc_v1.py",
           "plancher_v1.py", "registre_v1.py", "repli_etapes_v1.py", "repli_recalcul_v1.py", "repli_v1.py", "sondes_neuves_v1.py"]
PHRASES = (
    "ligne de registre `CODE-T07` (DS-3 bis)", COMMIT, "013a273b4d47c45e20355b754bd82489f90181f0",
    "défaut appliqué le 10 novembre à 17:13 UTC (R-1902), sauf mot contraire de Lazar",
    "**calculé avec les données de P3**", "**mis en œuvre**", "**`GO-2026-11-10-06`**",
    "**les actions sans caractère de mot sont exclues de la notation des témoins lexicaux, et d'elle seule**",
    "**T7-P10 est lue sur les actions qui restent**", "**le code écrit la réserve R8 pour ce concept**",
    "**Brouillon 21 : entretien avec le Transformative AI Fund visé le 27 novembre 2026**",
    "**Chemin normal du témoin positif P3-bis**", "contrôle d'ouverture v2",
    "**ordre canonique (tâche, paire, membre)**", "**paire en défaut exclue de l'apprentissage, jamais réécrite**",
    "`[1-9][0-9]*`", "**mémoire de la notation**", "constat C-1 de la contre-lecture courte, R-2153",
    "est une clé **permise** (brouillon 21, option (c), R-2158 ; **exigée** jusqu'au brouillon 20)",
    "| R15 | **brouillon 21, option (c) des phrases des concepts** (R-2158)",
    "**Le module doit donc changer avant l'inscription de `CODE-T07`**",
    "`docs/procedures/ordre-execution-etape-a-t07-v1-brouillon3.md`",
    "151b6163289460eb8b37f7c6a1998e23aed8e05b5e557bf1a2297079bf0e5af9",
    "04216df3a8b3ebf3ffb617f1a6701b0429964d28a6c6df677896359891fe2f34",
    "3f21774ca2a740e059191e762a4922076d954ee4c3e728c9927ba436cb211685",
    "fb41812732711c1a2a152fa776c46be5a4c50a72ccdc8fd9b7b7f9edcc37d208",
)
ABSENTES = (
    "10 USD en variante B → arrêt",
    "**10 USD** en variante B : arrêt",
    "`code_t07_exige` (`faux` tant que DS-3 bis n'est pas accordée)",
    "une instance séparée ≤ 10 USD",
    "(≤ 10 USD)",
    "est une clé **exigée**, hors de cette famille",
    "**exigées** `RUN-CONFIRMATION-T06`, `SCELLEMENT-CONCEPTS-T07`",
    "1. **Action sans caractère de mot (règle de CT-01)**",
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


def appliquer(t: str, couples: list, etiquette: str) -> str | None:
    print(f"\n# application, {etiquette} (id ; occurrences de l'« ancien » ; ligne ; section ; empan gelé)")
    for c in couples:
        if sorted(c) != ["ancien", "id", "motif", "nouveau", "section"]:
            print(f"ARRÊT : {c.get('id')} : clés {sorted(c)}")
            return None
        n = t.count(c["ancien"])
        if n != 1 or c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu), ou égal au « nouveau » ; rien n'est écrit")
            return None
        p = t.index(c["ancien"])
        sec = section_de(t, p)
        gele = any(sec.startswith(g) for g in EMPAN_GELE)
        print(f"{c['id']} ; 1 ; l. {t.count(chr(10), 0, p) + 1} ; {sec} ; {'OUI' if gele else 'non'}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    return t


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # noqa: E402

    b20 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon20.md"
    cl20 = racine / "prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon20-cl1-couples-v1.json"
    c21 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon21-couples-v1.json"
    b21 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon21.md"
    defauts = []
    for chemin, attendu in ((b20, SHA_B20), (cl20, SHA_CL20), (c21, SHA_B21_COUPLES)):
        e = sha(chemin.read_bytes())
        if e != attendu:
            print(f"ARRÊT : empreinte de {chemin.relative_to(racine)} {e} ≠ {attendu}")
            return 1
        print(f"{chemin.relative_to(racine)} : {e} (égale)")
    texte20 = b20.read_bytes().decode("utf-8")
    t = appliquer(texte20, json.loads(cl20.read_text(encoding="utf-8")), "CL20-01 à CL20-10 (tels quels)")
    if t is None:
        return 1
    print(f"texte après CL20 : {sha(t.encode('utf-8'))} ({'égal' if sha(t.encode('utf-8')) == SHA_APRES_CL20 else 'DIFFÉRENT'} à celui du contre-lecteur)")
    if sha(t.encode("utf-8")) != SHA_APRES_CL20:
        return 1
    couples = json.loads(c21.read_text(encoding="utf-8"))
    t = appliquer(t, couples, f"B21 ({len(couples)} couples)")
    if t is None:
        return 1
    texte21 = t

    octets21 = texte21.encode("utf-8")
    if b21.exists():
        if b21.read_bytes() != octets21:
            print(f"ARRÊT (R12) : {b21.relative_to(racine)} existe et diffère : rien n'est écrasé")
            return 1
        print(f"\n{b21.relative_to(racine)} déjà écrit, identique")
    else:
        b21.write_bytes(octets21)
        print(f"\nécrit : {b21.relative_to(racine)}")
    print(f"brouillon 21 : {sha(octets21)} ; {texte21.count(chr(10))} lignes")

    print("\n# vérifications")
    premiere = texte21.split("\n", 1)[0]
    statut = next(l for l in texte21.split("\n") if l.startswith("- Statut :"))
    ok = premiere == TITRE_21 and statut.startswith("- Statut : **brouillon 21**")
    print(f"(1) titre et premier statut au brouillon 21 : {ok}")
    if not ok:
        defauts.append("titre ou statut")

    debuts = {"(a)": "### (a) Périmètre fermé des clés", "(b)": "### (b) Règles de lancement et de relance",
              "(c)": "### (c) Engagement de jouer l'étape A", "(d)": "### (d) Garde adaptée à l'ouverture réduite",
              "(e)": "### (e) Grille de lecture"}
    permis = {"(a)": ("1. **Quels jeux**", "   d'aucune clé ; le jeu de phrases des concepts"),
              "(b)": ("   inscrites (`RUN-CONFIRMATION-T06`", "6. **Dépense**")}
    noms = list(debuts)
    for k, nom in enumerate(noms[:-1]):
        x20 = bloc(texte20, debuts[nom], debuts[noms[k + 1]])
        x21 = bloc(texte21, debuts[nom], debuts[noms[k + 1]])
        if nom in permis:
            d = lignes_diff(x20, x21)
            print(f"(2) écrit {nom} : {len(d)} lignes de différence :")
            for l in d:
                print(f"      {l[:220]}{' […]' if len(l) > 220 else ''}")
            if not d or any(not l[1:].startswith(permis[nom]) for l in d):
                defauts.append(f"{nom} changé hors des points déclarés")
        else:
            egal = x20 == x21
            print(f"(2) écrit {nom} : égal octet pour octet au brouillon 20 : {egal}")
            if not egal:
                defauts.append(f"écrit {nom} changé")

    s20, s21 = sections(texte20), sections(texte21)
    s21_ren = {(DECISIONS_20 if k == DECISIONS_21 else k): v for k, v in s21.items()}
    neuves = [k for k in s21_ren if k not in s20]
    disparues = [k for k in s20 if k not in s21_ren]
    changees = [k for k in s20 if k in s21_ren and s20[k] != s21_ren[k]]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues} ; renommée : « Décisions … » (titre du brouillon 21 vérifié : {DECISIONS_21 in s21})")
    if neuves != [TABLE_NEUVE] or disparues or DECISIONS_21 not in s21:
        defauts.append("sections neuves, disparues ou renommées inattendues")
    print(f"    sections changées ({len(changees)}) :")
    for k in changees:
        print(f"      - {k[:90]}{'  [EMPAN GELÉ]' if any(k.startswith(g) for g in EMPAN_GELE) else ''}")
    geles = [k for k in changees if any(k.startswith(g) for g in EMPAN_GELE)]
    hors = [k for k in geles if not k.startswith(TOUCHEES_DECLAREES)]
    if hors:
        defauts.append(f"section de l'empan gelé touchée hors déclaration : {hors}")
    for k in geles:
        d = lignes_diff(s20[k], s21_ren[k])
        print(f"    empan gelé, « {k[:40]}… » : {len(d)} lignes de différence :")
        for l in d:
            print(f"      {l[:240]}{' […]' if len(l) > 240 else ''}")
    print(f"    sections de l'empan gelé inchangées : "
          f"{[k[:40] for k in s20 if any(k.startswith(g) for g in EMPAN_GELE) and k not in changees]}")

    restes = sorted(set(GABARIT.findall(texte21)))
    print(f"(4) marqueurs restants : {len(restes)} : { {m: texte21.count(m) for m in restes} }")
    if restes != ATTENDUS:
        defauts.append(f"marqueurs restants {restes} ≠ {ATTENDUS}")
    for m in UNE_FOIS:
        if texte21.count(m) != 1:
            defauts.append(f"{m} présent {texte21.count(m)} fois (1 attendu)")
    absents = [m for m in REMPLIS if m in texte21]
    print(f"    marqueurs remplis encore présents : {absents}")
    if absents:
        defauts.append("marqueurs remplis encore présents")

    ecarts = []
    for n in MODULES:
        r = subprocess.run(["git", "-C", str(racine), "show", f"{COMMIT}:src/controle_ia/t07/{n}"], capture_output=True)
        h = sha(r.stdout) if r.returncode == 0 else None
        if h is None or f"`src/controle_ia/t07/{n}` `{h}`" not in texte21:
            ecarts.append(n)
    print(f"(5) dix-huit empreintes du texte égales à `git show {COMMIT[:8]}:…` : {not ecarts}{' ; écarts : ' + repr(ecarts) if ecarts else ''}")
    if ecarts:
        defauts.append("empreintes du code")

    p = problemes(b21)
    attendu = [f"marqueurs de gabarit restants : {', '.join(ATTENDUS)}"]
    print(f"(6) controle_ia.prereg.problemes(brouillon 21) : {p}")
    if p != attendu:
        defauts.append("problemes ≠ la seule ligne des marqueurs voulus")
    dossier = Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-b21-factice-"))
    dossier.mkdir(parents=True, exist_ok=True)
    factice = texte21
    for m in ATTENDUS:
        factice = factice.replace(m, "valeur-factice-" + m.strip("<>").lower())
    copie = dossier / "T0.7-sondes-v0-v1-brouillon21-valeurs-factices.md"
    copie.write_text(factice, encoding="utf-8")
    pf = problemes(copie)
    print(f"    à valeurs factices ({copie}) : problemes = {pf}")
    if pf:
        defauts.append("problemes non vide à valeurs factices")

    plat = " ".join(texte21.split())
    manquantes = [ph for ph in PHRASES if " ".join(ph.split()) not in plat]
    print(f"(7) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)} présentes"
          f"{' ; manquantes : ' + repr(manquantes) if manquantes else ''}")
    if manquantes:
        defauts.append("phrases exigées manquantes")
    presentes = [ph for ph in ABSENTES if ph in texte21]
    print(f"    passages retirés encore présents : {presentes}")
    if presentes:
        defauts.append("passages retirés encore présents")

    d = lignes_diff(texte20, texte21)
    print(f"(8) différentiel 20 → 21 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées")

    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
