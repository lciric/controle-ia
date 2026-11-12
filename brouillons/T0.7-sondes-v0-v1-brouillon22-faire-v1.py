"""T0.7 sondes v0, brouillon 22 : application des couples B22 au brouillon 21, et vérifications (v1).

Rédacteur du brouillon 22 (sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, Claude Opus 5.5), 10 novembre 2026 ;
consigne `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-t07-brouillon22-v1.md` (`727763aa…`),
méthode du script du brouillon 21 (`brouillons/T0.7-sondes-v0-v1-brouillon21-faire-v1.py`, `52ddf93a…`).
Bibliothèque standard, plus `controle_ia.prereg` et `controle_ia.t07.registre_v1` du dépôt (lus dans RACINE/src) et `git` en
lecture (`git show`, `git diff --quiet`) ; aucun réseau, aucune écriture hors de `brouillons/T0.7-sondes-v0-v1-brouillon22.md` et du
dossier temporaire.

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE [DOSSIER_TEMPORAIRE]

1. vérifie l'empreinte du brouillon 21 (`f7dcb226…`) et celle des couples B22 ;
2. applique les couples dans l'ordre ; chaque « ancien » présent exactement une fois au moment de son application et différent
   de son « nouveau », clés exactement `id`, `section`, `motif`, `ancien`, `nouveau` ; sinon arrêt (code 1), rien n'est écrit ;
   seuls B22-14 et B22-15 peuvent toucher l'empan gelé « Hypothèse » à « Liste d'arrêt » ;
3. écrit `brouillons/T0.7-sondes-v0-v1-brouillon22.md` (R12 : refuse d'écraser un fichier différent) ;
4. vérifie : (1) titre et premier statut ; (2) section « Écrits exigés par P3-bis » égale octet pour octet au brouillon 21 ;
   (3) sections neuves (deux), disparues (aucune) ; empan gelé : « Hypothèse », « Prédiction », « Métrique », « Seuil »,
   « Plan d'analyse », « Liste d'arrêt » égales octet pour octet ; « Règle « mots et coût » » et « Critères » égales au brouillon
   21 une fois B22-14 et B22-15 défaits (différences imprimées) ; (4) sept marqueurs restants, une occurrence chacun ; marqueurs
   remplis absents ; (5) dix-huit empreintes du texte égales à `git show 37485ce5:…` et au fichier `CODE-T07-v1.json` ; `src` de
   `main` égal à `37485ce5` (constat) ; (6) cellules `AUDIT-FUITES-T07` (avant : `9cee4938…`, après : `381a72d5…`, empreintes du
   journal de la consigne d'audit) et `CONSIGNE-AUDIT-FUITES-T07` (`95c8b659…`, inchangée) ; passages du § 2.3 de la consigne
   d'audit présents ligne à ligne ; (7) lignes du code citées au commit `37485ce5` ; (8) registre `registres/scellements-v1.md`
   et classement des clés `T08` et `VADAPT` par `registre_v1.classer_cle_inconnue` ; (9) `problemes` réduit à la ligne des sept
   marqueurs, vide à valeurs factices ; (10) phrases exigées présentes, passages retirés absents ; (11) pièce de puissance :
   empreintes citées égales, sortie rejouée égale à la sortie versée ; (12) différentiel compté.
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

SHA_B21 = "f7dcb226efe8671b977ce906c286f7e7243f78a2c9fcf205cbfe5715866ea0cc"
SHA_B22_COUPLES = "2adf0319f05f65b2afd2534666adca78ace2d2af1c6b978a0875821df7af2639"
TITRE_22 = "# Préenregistrement — T0.7 sondes v0 (critère 3 de G0), mode « coût » — v1 — brouillon 22"
ATTENDUS = sorted(f"<<{n}>>" for n in ("ENTROPIE_T07", "EMPREINTE_CONFIG_T07", "EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07", "GO_ETAPE_A_T07",
                                        "MOT_LAZAR_P064", "MOT_LAZAR_P065", "ESSAI_CLC04_T07"))
REMPLIS = ["<<COMMIT_CODE_T07>>", "<<EMPREINTES_CODE_T07>>", "<<T7P10_SONDES_P3>>", "<<REPLI_RECALCUL_T07>>"]
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
EMPAN_GELE = ("Hypothèse", "Règle « mots et coût »", "Prédiction chiffrée", "Métrique", "Seuil", "Plan d'analyse",
              "Écrits exigés par P3-bis", "Critères de lecture gelés", "Liste d'arrêt")
TOUCHES_GELEES = {"B22-14": "Règle « mots et coût »", "B22-15": "Critères de lecture gelés"}
NEUVES = ["Table « ce qui change du 21 au 22 »",
          "Concordance avec le texte de validité de l'adaptateur (préenregistrement séparé ; D-1 (b) ; brouillon 22)"]
COMMIT = "37485ce50601b7d7ff9035bc34c734ec689ca731"
MODULES = ["__init__.py", "code_t07_v1.py", "controle_jeux_v1.py", "criteres_v1.py", "donnees_p3_t07_v1.py", "garde_adaptee_v1.py",
           "journal_p3bis_v1.py", "lecture_v1.py", "lecture_v2.py", "lectures_t07_v1.py", "mahalanobis_v1.py", "passe_blanc_v1.py",
           "plancher_v1.py", "registre_v1.py", "repli_etapes_v1.py", "repli_recalcul_v1.py", "repli_v1.py", "sondes_neuves_v1.py"]
CELLULES = {"AUDIT-FUITES-T07": ("9cee4938b9aaaa852a1be89491ad93bbab491d670379681a34de1661bb6754e9",
                                 "381a72d5b52c1534d116c81b71568dd4728d1a4d90a22a25e99109508e30fede"),
            "CONSIGNE-AUDIT-FUITES-T07": ("95c8b659c54f218a903e1d0359a5a4a9ca9bd2e81072741803861a4bb4fa1121",
                                          "95c8b659c54f218a903e1d0359a5a4a9ca9bd2e81072741803861a4bb4fa1121")}
CONSIGNE_AUDIT = ("brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon3.md",
                  "0d51099e5ef58829ce83731592eb8573aae8ce8848344488ffc672be45ac273e")
CODE_V1 = ("registres/code-t07/CODE-T07-v1.json", "9ef4ede751fcceb51eda1e622deaa62552326e395fdbd647c6989ad32353701f")
# (fichier au commit 37485ce5, ligne, extrait attendu sur cette ligne) : lignes que le texte cite
LIGNES_CODE = [
    ("lecture_v2.py", 239, "def premiere_ouverture_a("),
    ("lecture_v2.py", 249, "return None"),
    ("lecture_v2.py", 276, "def reserve_couches_repli("),
    ("lecture_v2.py", 298, 'lignes_v[cle]["instant"] < int(fermeture)'),
    ("lecture_v2.py", 302, 'lc["instant"] < int(fermeture)'),
    ("lecture_v2.py", 501, '4 if config["mode"] == "reel" else 1'),
    ("lecture_v2.py", 598, 'for k in ("cle", "condition", "tache", "pas")'),
    ("lecture_v2.py", 599, 'index = {"sondes": []'),
    ("lecture_v2.py", 617, 'entree = {"rang": k'),
    ("lecture_v2.py", 630, 'tableaux[f"scores_{k}"]'),
    ("lecture_v2.py", 631, 'tableaux[f"plancher_{k}"]'),
    ("lecture_v2.py", 633, '"empreintes_deux_premieres"'),
    ("lecture_v2.py", 779, '{"planchers": {n: [p.nom for p in liste]'),
    ("lecture_v2.py", 780, '"principales":'),
    ("lecture_v2.py", 850, "aucune phrase → aucune tâche de plancher de concept"),
    ("lecture_v2.py", 862, '"phrases_concepts_etape_a"'),
    ("lecture_v2.py", 876, "reserve_couches_repli("),
    ("lecture_v2.py", 902, 'generiques["phrases"] is None and appris["directions"]'),
    ("lecture_v2.py", 936, '"sondes_lues": noms_finaux'),
    ("lecture_v2.py", 937, '"niveau_applique"'),
    ("lecture_v2.py", 939, '"principales": principales_rapport'),
    ("lecture_v2.py", 944, "fichiers_sondes_neuves=ecrire_sondes_neuves("),
    ("lecture_v2.py", 976, '"index": notation["index"]'),
    ("lecture_v2.py", 979, '"graines_derivees_apres_manifeste"'),
    ("lecture_v2.py", 981, '"notation-t07"'),
    ("lecture_v2.py", 1058, 'f"scores-t07/{run_t07}'),
    ("lecture_v2.py", 1112, '"issue_critere_3": issue["issue"]'),
    ("lecture_v2.py", 1114, '"entrees": issue["entrees"]'),
    ("lecture_v2.py", 1115, '"scores_ouverts": ouvre, "scores_ii_ouverts": ouvre and oii'),
    ("lecture_v2.py", 1118, '"jeux": jeux, "jeux_hors_jugement": hors'),
    ("lecture_v2.py", 1125, '"reserves_identifiees"'),
    ("lectures_t07_v1.py", 64, '"R15": "plancher sémantique non lu : jeu des phrases des concepts non scellé à l\'ouverture (T7-P9 non lue)"'),
    ("lectures_t07_v1.py", 69, "MOTIF_P9_SANS_PHRASES"),
    ("lectures_t07_v1.py", 494, '"id": "R15"'),
    ("registre_v1.py", 69, "EXIGEES_ETAPE_A = (RUN_CONFIRMATION_T06,)"),
    ("registre_v1.py", 70, "SCELLEMENT_CONCEPTS_T07"),
]
REGISTRE_ATTENDU = [
    "| SCELLEMENT-JEUX-T07-JD | 2026-11-10T08:22:50Z | donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl | 32f412888270a3c4b4bc347cf57055bd11b517000feceeaeed122476238ec228 |",
    "| SCELLEMENT-JEUX-T07-JA | 2026-11-10T08:22:50Z | donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl | 5b0409209e66e6c29b69e675c5836cefbef966d9cc0a34412837cae837e2aacf |",
    "| SCELLEMENT-T08-BASE-A | 2026-11-10T12:21:55Z | prereg/T0.8-base-A-mots-et-cout-v1.md | 72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d |",
]
PIECES = ("brouillons/T0.7-sondes-v0-v1-brouillon22-pieces/puissance_par_dose_t07_v1.py",
          "brouillons/T0.7-sondes-v0-v1-brouillon22-pieces/puissance-par-dose-t07-v1.txt")
PHRASES = (
    COMMIT, "22b8da91265b316fe4b1de1727617a7fff4d51f9", "registres/code-t07/CODE-T07-v2.json", "jamais cité",
    "git diff --quiet 37485ce5 C7 -- src", "7a32746203bf9b467898dbf82a04f32428bf9bd886f93902f82b57d9b0c719e6",
    "e58be6c9051d928e3818175ace1dbfd2db6afd2c6e725d7278032dbe13a90e90", "tests/test_lanceur_durable_v5_a1v4.py",
    "écrite quand les scores sont ouverts ; sinon l'état des phrases est au manifeste de l'étape A et dans `sondes-t07.json`",
    "tests/test_t07_ouvrir_reel_concepts_v1.py", "**CLC-07, réserve déclarée**",
    "72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d", "`2026-11-10T12:21:55Z`",
    "si BA-L2 s'applique (témoin positif de la base (A) en défaut), l'étape B attend le mot de Lazar",
    "**ignorées et comptées** (règle (3))", "**réserve VC-06**",
    "ea5fe3f05ab5ae070e38a0ecc28c73ea96de15e34a2250ddab9d000044f6096e", "`0d4dd3ca`",
    "defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd", "cf84198566978307c3cc3e1d10e62245042446b569a407b66bbcb029ffe9764e",
    "**(iv-a)** `S100` contre `T100` avec seuil", "**aucun critère de ce texte ne change**",
    "**Puissance par dose et écart au seuil de la base", "défauts échus le 10 novembre 2026 vers 17:13 UTC",
    "dont la source est **propre à une condition ou commune aux deux**", "(l. 133-144 au commit `7a54d431…`",
)
ABSENTES = (
    "la base (A) est fixée par T0.8, dont le texte n'existe pas\n(chemin critique v3, pas 9)",
    "`T08` : T0.8, dont le texte n'est pas écrit",
    "**non produite par l'action de l'organisme**",
    "(`aire_simple` rend `null` : pas une fuite)",
    "par exemple `registres/code-t07/CODE-T07-v1.json`",
    "mot : « défaut appliqué le 10 novembre à 17:13 UTC (R-1902), sauf mot contraire de Lazar » : **oui**",
    "**valeurs au dernier commit contre-lu, `8ae9fc44`**",
)


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sections(texte: str) -> dict:
    morceaux = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    return {titre.strip(): corps for titre, corps in zip(morceaux[1::2], morceaux[2::2])}


def section_de(texte: str, position: int) -> str:
    nom = "(avant la première section)"
    for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M):
        if m.start() <= position:
            nom = m.group(1)
    return nom


def gelee(nom: str) -> bool:
    return any(nom.startswith(g) for g in EMPAN_GELE)


def lignes_diff(a: str, b: str) -> list:
    return [l for l in difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]


def cellule(texte: str, cle: str) -> str:
    ls = [l for l in texte.split("\n") if l.startswith(f"| `{cle}`")]
    if len(ls) != 1:
        raise ValueError(f"ligne {cle} : {len(ls)} occurrences")
    c = re.split(r"(?<!\\)\|", ls[0])[1:-1]
    if len(c) != 4:
        raise ValueError(f"ligne {cle} : {len(c)} cellules")
    return c[1].strip()


def git(racine: Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(racine), *args], capture_output=True)


def appliquer(t: str, couples: list) -> tuple[str | None, list]:
    print(f"\n# application, B22 ({len(couples)} couples) (id ; occurrences de l'« ancien » ; ligne ; section ; empan gelé)")
    gelees = []
    for c in couples:
        if sorted(c) != ["ancien", "id", "motif", "nouveau", "section"]:
            print(f"ARRÊT : {c.get('id')} : clés {sorted(c)}")
            return None, gelees
        n = t.count(c["ancien"])
        if n != 1 or c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu), ou égal au « nouveau » ; rien n'est écrit")
            return None, gelees
        p = t.index(c["ancien"])
        sec = section_de(t, p)
        g = gelee(sec)
        if g:
            gelees.append(c["id"])
            if c["id"] not in TOUCHES_GELEES or not sec.startswith(TOUCHES_GELEES[c["id"]]):
                print(f"ARRÊT : {c['id']} touche la section gelée « {sec[:60]} » sans déclaration")
                return None, gelees
        print(f"{c['id']} ; 1 ; l. {t.count(chr(10), 0, p) + 1} ; {sec[:70]} ; {'OUI' if g else 'non'}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    return t, gelees


def main(argv: list) -> int:
    if not 1 <= len(argv) <= 2:
        print("usage : RACINE [DOSSIER_TEMPORAIRE]", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    sys.path.insert(0, str(racine / "src"))
    from controle_ia.prereg import problemes  # noqa: E402
    from controle_ia.t07 import registre_v1 as rg  # noqa: E402

    b21 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon21.md"
    c22 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon22-couples-v1.json"
    b22 = racine / "brouillons/T0.7-sondes-v0-v1-brouillon22.md"
    defauts = []
    for chemin, attendu in ((b21, SHA_B21), (c22, SHA_B22_COUPLES)):
        e = sha(chemin.read_bytes())
        if e != attendu:
            print(f"ARRÊT : empreinte de {chemin.relative_to(racine)} {e} ≠ {attendu}")
            return 1
        print(f"{chemin.relative_to(racine)} : {e} (égale)")
    texte21 = b21.read_bytes().decode("utf-8")
    couples = json.loads(c22.read_text(encoding="utf-8"))
    texte22, gelees = appliquer(texte21, couples)
    if texte22 is None:
        return 1
    print(f"couples qui touchent l'empan gelé : {gelees} (déclarés : {sorted(TOUCHES_GELEES)})")
    if sorted(gelees) != sorted(TOUCHES_GELEES):
        defauts.append("touches de l'empan gelé ≠ celles déclarées")

    octets22 = texte22.encode("utf-8")
    if b22.exists():
        if b22.read_bytes() != octets22:
            print(f"ARRÊT (R12) : {b22.relative_to(racine)} existe et diffère : rien n'est écrasé")
            return 1
        print(f"\n{b22.relative_to(racine)} déjà écrit, identique")
    else:
        b22.write_bytes(octets22)
        print(f"\nécrit : {b22.relative_to(racine)}")
    print(f"brouillon 22 : {sha(octets22)} ; {texte22.count(chr(10))} lignes")

    print("\n# vérifications")
    premiere = texte22.split("\n", 1)[0]
    statut = next(l for l in texte22.split("\n") if l.startswith("- Statut :"))
    ok = premiere == TITRE_22 and statut.startswith("- Statut : **brouillon 22**")
    print(f"(1) titre et premier statut au brouillon 22 : {ok}")
    if not ok:
        defauts.append("titre ou statut")

    s21, s22 = sections(texte21), sections(texte22)
    ecrits = [k for k in s21 if k.startswith("Écrits exigés par P3-bis")]
    egal = len(ecrits) == 1 and s21[ecrits[0]] == s22.get(ecrits[0])
    print(f"(2) section « Écrits exigés par P3-bis » ((a) à (e) comprises) égale octet pour octet au brouillon 21 : {egal}")
    if not egal:
        defauts.append("écrits changés")

    neuves = [k for k in s22 if k not in s21]
    disparues = [k for k in s21 if k not in s22]
    changees = [k for k in s21 if k in s22 and s21[k] != s22[k]]
    print(f"(3) sections neuves : {neuves} ; disparues : {disparues}")
    if neuves != NEUVES or disparues:
        defauts.append("sections neuves ou disparues inattendues")
    print(f"    sections changées ({len(changees)}) :")
    for k in changees:
        print(f"      - {k[:90]}{'  [EMPAN GELÉ]' if gelee(k) else ''}")
    defaire = {c["id"]: c for c in couples if c["id"] in TOUCHES_GELEES}
    for k in s21:
        if not gelee(k):
            continue
        x22 = s22[k]
        for ident, prefixe in TOUCHES_GELEES.items():
            if k.startswith(prefixe):
                x22 = x22.replace(defaire[ident]["nouveau"], defaire[ident]["ancien"], 1)
        egal = x22 == s21[k]
        d = lignes_diff(s21[k], s22[k])
        print(f"    empan gelé, « {k[:45]} » : {len(d)} lignes de différence ; égale au brouillon 21 une fois B22-14 et B22-15 "
              f"défaits : {egal}")
        for l in d:
            print(f"      {l[:260]}{' […]' if len(l) > 260 else ''}")
        if not egal:
            defauts.append(f"empan gelé « {k[:40]} » changé hors des couples déclarés")

    restes = {m: texte22.count(m) for m in sorted(set(GABARIT.findall(texte22)))}
    print(f"(4) marqueurs restants : {len(restes)} : {restes}")
    if sorted(restes) != ATTENDUS or any(v != 1 for v in restes.values()):
        defauts.append(f"marqueurs restants {restes} ≠ {ATTENDUS}, une occurrence chacun")
    absents = [m for m in REMPLIS if m in texte22]
    print(f"    marqueurs remplis encore présents : {absents}")
    if absents:
        defauts.append("marqueurs remplis encore présents")

    v1 = racine / CODE_V1[0]
    fichiers_v1 = json.loads(v1.read_text(encoding="utf-8"))["fichiers"] if sha(v1.read_bytes()) == CODE_V1[1] else None
    ecarts = []
    for n in MODULES:
        r = git(racine, "show", f"{COMMIT}:src/controle_ia/t07/{n}")
        h = sha(r.stdout) if r.returncode == 0 else None
        if (h is None or f"`src/controle_ia/t07/{n}` `{h}`" not in texte22 or fichiers_v1 is None
                or fichiers_v1.get(f"src/controle_ia/t07/{n}") != h):
            ecarts.append(n)
    print(f"(5) dix-huit empreintes du texte égales à `git show {COMMIT[:8]}:…` et à {CODE_V1[0]} ({CODE_V1[1][:8]}…) : "
          f"{not ecarts}{' ; écarts : ' + repr(ecarts) if ecarts else ''}")
    if ecarts:
        defauts.append("empreintes du code")
    egal_src = git(racine, "diff", "--quiet", COMMIT, "HEAD", "--", "src").returncode == 0
    tete = git(racine, "rev-parse", "--short=8", "HEAD").stdout.decode().strip()
    egal_tests = git(racine, "diff", "--quiet", COMMIT, "HEAD", "--", "tests").returncode == 0
    print(f"    constat : `src` de la tête ({tete}) égal à {COMMIT[:8]} : {egal_src} ; `tests` égal : {egal_tests} "
          f"(attendu faux : raison de C7)")

    for cle, (avant, apres) in CELLULES.items():
        h21, h22 = sha(cellule(texte21, cle).encode("utf-8")), sha(cellule(texte22, cle).encode("utf-8"))
        ok = h21 == avant and h22 == apres
        print(f"(6) cellule {cle} : brouillon 21 {h21[:8]}… (attendu {avant[:8]}…), brouillon 22 {h22[:8]}… (attendu {apres[:8]}…) : {ok}")
        if not ok:
            defauts.append(f"cellule {cle}")
    consigne = racine / CONSIGNE_AUDIT[0]
    if sha(consigne.read_bytes()) != CONSIGNE_AUDIT[1]:
        defauts.append("empreinte de la consigne d'audit")
    ca = consigne.read_text(encoding="utf-8")
    s23 = ca[ca.index("### 2.3 "):ca.index("\n## 3.")]
    cites = [l[2:] for l in s23.split("\n") if l.startswith("> ")]
    lignes22 = set(texte22.split("\n"))
    manquants = [l for l in cites if l not in lignes22]
    print(f"    passages de T0.7 recopiés au § 2.3 de la consigne d'audit : {len(cites) - len(manquants)} lignes sur {len(cites)} "
          f"présentes telles quelles dans le brouillon 22")
    if manquants:
        defauts.append("passages du § 2.3 de la consigne d'audit changés")

    fautes = []
    for f, n, extrait in LIGNES_CODE:
        r = git(racine, "show", f"{COMMIT}:src/controle_ia/t07/{f}")
        lignes = r.stdout.decode("utf-8").split("\n")
        if r.returncode != 0 or len(lignes) < n or extrait not in lignes[n - 1]:
            fautes.append(f"{f} l. {n}")
    print(f"(7) lignes du code citées par le texte, au commit {COMMIT[:8]} : {len(LIGNES_CODE) - len(fautes)} sur {len(LIGNES_CODE)}"
          f"{' ; fautes : ' + repr(fautes) if fautes else ''}")
    if fautes:
        defauts.append("lignes du code citées")

    reg = (racine / "registres/scellements-v1.md").read_text(encoding="utf-8").split("\n")
    presentes = [l for l in REGISTRE_ATTENDU if l in reg]
    autres = [l.split("|")[1].strip() for l in reg if l.startswith("| ") and l not in REGISTRE_ATTENDU]
    marques = ("T06", "T08", "P3BIS", "NARC")
    classes = {k: rg.classer_cle_inconnue(k, marques)[0] for k in ("SCELLEMENT-T08-BASE-A", "LECTURE-T08-BASE-A",
                                                                    "SCELLEMENT-VADAPT", "CODE-VADAPT")}
    ok = (len(presentes) == 3 and classes["SCELLEMENT-T08-BASE-A"] == classes["LECTURE-T08-BASE-A"] == "ignoree"
          and classes["SCELLEMENT-VADAPT"] == classes["CODE-VADAPT"] == "refus")
    print(f"(8) registre : {len(presentes)} lignes attendues sur 3 ; autres clés : {autres} ; classement : {classes} : {ok}")
    if not ok:
        defauts.append("registre ou classement des clés")

    p = problemes(b22)
    attendu = [f"marqueurs de gabarit restants : {', '.join(ATTENDUS)}"]
    print(f"(9) controle_ia.prereg.problemes(brouillon 22) : {p}")
    if p != attendu:
        defauts.append("problemes ≠ la seule ligne des marqueurs voulus")
    dossier = Path(argv[1]) if len(argv) == 2 else Path(tempfile.mkdtemp(prefix="t07-b22-factice-"))
    dossier.mkdir(parents=True, exist_ok=True)
    factice = texte22
    for m in ATTENDUS:
        factice = factice.replace(m, "valeur-factice-" + m.strip("<>").lower())
    copie = dossier / "T0.7-sondes-v0-v1-brouillon22-valeurs-factices.md"
    copie.write_text(factice, encoding="utf-8")
    pf = problemes(copie)
    print(f"    à valeurs factices ({copie}) : problemes = {pf}")
    if pf:
        defauts.append("problemes non vide à valeurs factices")

    plat = " ".join(texte22.split())
    manquantes = [ph for ph in PHRASES if " ".join(ph.split()) not in plat]
    print(f"(10) phrases exigées : {len(PHRASES) - len(manquantes)} sur {len(PHRASES)} présentes"
          f"{' ; manquantes : ' + repr(manquantes) if manquantes else ''}")
    if manquantes:
        defauts.append("phrases exigées manquantes")
    presentes = [ph for ph in ABSENTES if ph in texte22]
    print(f"     passages retirés encore présents : {presentes}")
    if presentes:
        defauts.append("passages retirés encore présents")

    py, txt = (racine / x for x in PIECES)
    h_py, h_txt = sha(py.read_bytes()), sha(txt.read_bytes())
    cites_ok = f"`{h_py}`" in texte22 and f"`{h_txt}`" in texte22
    r = subprocess.run([sys.executable, "-I", "-B", str(py)], capture_output=True, cwd=str(dossier))
    rejeu = r.returncode == 0 and r.stdout == txt.read_bytes()
    print(f"(11) pièce de puissance : empreintes citées ({h_py[:8]}…, {h_txt[:8]}…) : {cites_ok} ; rejouée, sortie égale : {rejeu}")
    if not (cites_ok and rejeu):
        defauts.append("pièce de puissance")

    d = lignes_diff(texte21, texte22)
    print(f"(12) différentiel 21 → 22 : {sum(1 for l in d if l[0] == '-')} lignes retirées, "
          f"{sum(1 for l in d if l[0] == '+')} lignes ajoutées ; {len(couples)} couples")

    if defauts:
        print("\nDÉFAUTS : " + " ; ".join(defauts))
        return 1
    print("\nTOUT PASSE")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
