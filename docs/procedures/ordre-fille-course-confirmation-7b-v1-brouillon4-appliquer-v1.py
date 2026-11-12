"""Ordre de la course de confirmation 7b de T0.6, brouillon 4 : application des couples au brouillon 3 et vérifications (v1).

Rédacteur du brouillon 4 (sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5), 10 novembre 2026 ;
contre-lecture appliquée : `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon3-contre-lecture-v1.md` (`f738d855…`, R-2143).
Bibliothèque standard, `bash` et les outils de base (sed, grep, sha256sum, stat) ; aucun réseau, aucune clé, aucun appel externe,
aucun `vastai` (dans les essais, le mot est remplacé par une fonction factice qui n'écrit qu'une ligne), aucun `git` réel (fonction factice).

    cd <dossier hors du dépôt> && <python du dépôt> -I -B <chemin absolu de ce script> RACINE

1. vérifie l'empreinte du brouillon 3 (`eae1e64f…`) et celle des couples ;
2. applique dans l'ordre les couples de `…-brouillon4-couples-v1.json` (clés `id`, `section`, `motif`, `ancien`, `nouveau`) : chaque
   « ancien » doit être présent exactement une fois dans le texte au moment de son application, et différent de son « nouveau » ;
   sinon arrêt (code 1), rien n'est écrit ;
3. écrit `docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4.md` (R12 : refuse d'écraser un fichier différent ; un
   fichier identique est accepté) ;
4. vérifie : titre et statut ; titres de sections (seuls ceux des § 13 et § 14 changent) ; marqueurs restants (les trois attendus, une
   occurrence chacun) et marqueurs remplis absents, avec leurs valeurs ; blocs `bash` (`bash -n`, gabarits `<…>` remplacés par des
   valeurs factices ; enveloppe et inventaire écrits par le § 4.0 compris) ; extraits Python (`ast.parse`) ; jetons de garde du
   brouillon 3 conservés ; phrases exigées par chaque constat présentes, phrases retirées absentes ; essais en mémoire des lignes neuves
   (C1, C5, M1, C6, C8, M4, M9, M10) dans un dossier temporaire, environnement réduit à PATH, HOME et LANG ; différentiel compté.
Code 0 et « TOUT PASSE » si tout tient ; code 1 sinon.
"""
from __future__ import annotations

import ast
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SHA_B3 = "eae1e64f99ce2e4f90b7cf28ffecda597d11d3f48d72b3898960342d8e9c3ad6"
SHA_COUPLES = "769ea60e84dd11ab2a58ee6e1dcd9d3ea098f90520ca8ea40cf6db654d572668"
CHEMIN_B3 = "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon3.md"
CHEMIN_COUPLES = "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4-couples-v1.json"
CHEMIN_B4 = "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon4.md"
TITRE_B4 = ("# Ordre — course de confirmation 7b de T0.6 (organismes v0, sous préenregistrement scellé), session fille porteuse des "
            "clés — v1, brouillon 4")
GABARIT = re.compile(r"<<[A-Z0-9_]+>>")
RESTENT = ["<<COMMIT_MAIN_REMISE>>", "<<ID_SESSION_FILLE>>", "<<LIGNE_SCELLEMENT_T07>>"]
RETIRES = ["<<DEPENSE_ANTERIEURE_USD>>", "<<LIGNE_REGISTRE_BRAS_B>>", "<<EMPREINTE_ORDRE_EXECUTION_ETAPE_A_T07>>"]
VALEURS_REMPLIES = {"ANT0=0;": 1, "grep -c '^| R-2092 |' registres/decisions.md": 1}
TITRES_CHANGES = {
    "## 13. À juger par la contre-lecture": "## 13. Jugés par la contre-lecture du brouillon 3 (R-2143)",
    "## 14. Marqueurs (à remplir par la mère avant la contre-lecture ; une occurrence chacun)":
        "## 14. Marqueurs (remplis par la mère avant le scellement de l'ordre ; une occurrence chacun)",
}
# gabarits des blocs remplacés par des valeurs factices avant `bash -n`
FACTICES = {"<<COMMIT_MAIN_REMISE>>": "0" * 40, "<numéro de la recherche retenue>": "1", "<même numéro>": "1",
            "<run>": "20261112-000000-t06-reel", "<heure de la destruction en secondes>": "1794800000"}
CH = 'ID=$(champ instance); [[ "$ID" =~ ^[0-9]+$ ]] || echo "ARRÊT : identifiant illisible dans lancement.txt"'
JETONS_GARDE = [
    "lecture-sondes-t06.json", "extraire_mesures_epreuve_t06_v1.py", "donnees/lecture-b-7a-quarantaine-v1", "essai/t06-explo-v3",
    "docs/notes/bras-attaque/", "donnees/bras-attaque*", "donnees/mode-tenu-a-l-ecart*", "prep/etiqueteur-v2-lecture-interrompue-reprise-v1",
    "registres/index-bras-attaque*", "verifier-arbre", "--single-branch", "--filter=blob:none", "refspec explicite", "env -i",
    "GO_ID=GO-2026-11-02-28", "GO-2026-11-02-28", "GO-2026-11-07-02", "GO-2026-11-07-04", "GO-2026-11-10-01", "R-2077", "R-2079",
    "DEPOT_URL=https://github.com/lciric/controle-ia-travail.git", "jamais `lciric/controle-ia`", "Jamais de chaîne v14", "controles-epreuve",
    "PREREG_ABSENT", "T06_EPUISEMENT_SIMULE_S", "T06_REGISTRE_GO", "`BRAS_B`", "TESTS_ARGS|BRAS_B'", "R10", "pkill", "killall", "garde des secrets",
    "instances.json", "offres.json", "creation-brute.json", "printenv", "export -p", "/proc/*/environ", "jamais `partiel`", "C01",
    "mot de Lazar", "H200", "200 USD", "60 USD", "180 USD", "Aucun couperet de temps", "2026-11-15T20:48Z",
    "1794873600", "≤ 1,30", "≤ 4,70", "≤ 0,08", "t06-v2", "calcul/t06-confirmation-7b-v1", "calcul/t06-reel-v4",
    "43d856596f4ff934ae6faa445faed0d00aaaa264b23b0bda344b6888dcd5e859", "6940a337d5e0c9a736aa7087275c5f6328133b67ed4df1c94535ba06a1965416",
    "935262b17ca95894a882b02f1526ee39d1738652", "1609a4bf2c1572f72bb8542d81d963ac6a8481c4",
    "ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169", "b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527",
    "ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d", "2022", "jamais affichés", "sans valeur de sonde", "ligne_B",
    "`start`, `reboot`, `copy`, `ssh`, `execute`", "intouchables", "':(glob,exclude)diag/*/lecture-sondes-t06.json*'",
    "'!/diag/*/lecture-sondes-t06.json*'", "exiger_prereg_scelle", "exiger_code_cite", "aucune création", "rien n'est exécuté",
    "Un écart : rien n'est exécuté", "jamais un autre identifiant", "ni geste sur une instance non créée par la fille",
]
# baisses de compte voulues : (jeton, raison)
BAISSES_VOULUES = {
    "jamais un autre identifiant": "commentaire du `stop` (§ 4.12) remplacé par la condition mécanique de C5 et M1 (identifiant de "
                                   "`lancement.txt`, présent une fois dans l'inventaire filtré)",
}
EXIGEES = {  # constat : [(phrase, occurrences minimales)]
    "B1": [("**Instance dont le run est encore vivant à cette heure : aucun geste de la fille**", 1),
           ("**Instance arrêtée, ou dont l'amorce a écrit sa ligne de fin : destruction au plus tard le 2026-11-16 à 23:00Z**", 1),
           ("la fille relève l'inventaire filtré le 17 à 01:15 UTC", 1),
           ("destruction d'une instance arrêtée au plus tard 2026-11-16T23:00Z ; run encore vivant : minuterie du 17 à 00:00Z (§ 4.13).", 1)],
    "C1": [('grep -vxF "diag/$RUN/resume.json"', 1), ('echo "OK (compagnon seul) $f"', 1),
           ("son contenu n'est ni descendu ni haché ; seul son compagnon est lu", 1), ("`OK (compagnon seul)` pour `resume.json`", 1),
           ("sondes, `resume.json`, données de `donnees/<run>/` et bras B restent sur le dépôt distant", 1)],
    "C2": [("**addendum v3 scellé : rempli**", 1), ('echo "addendum v3 du bras B scellé"', 1), ("**addendum v3 scellé** (R-2092, § 7)", 1),
           ("1a372523290fdaf0a606db592295885f01ff9d6adc9b877fd72279fc6a44ccdf", 3)],
    "C3": [("**parent** du commit qui ajoute cet ordre scellé", 1), ("**Ordre de remplissage** (C3)", 1),
           ("est une règle de la mère, non un geste de la fille", 1)],
    "C4": [("**Canal** : la fille écrit à Lazar dans sa session ; Lazar relaie à la mère", 1),
           ("compte rendu, puis destruction sur un mot de Lazar écrit dans la session de la fille (R-2113)", 1),
           ("compte rendu à Lazar et à la mère **avant** toute destruction (§ 4.13)", 1)],
    "C5": [(CH, 3), ('grep -c "^$ID t06-v2 "', 2), ("jamais retapé", 1)],
    "C6": [('"retenu (étape des sondes ou motif interdit, C01) : compte rendu"', 1), ('r.get("etape") in ("test croisé","résumé")', 1)],
    "C7": [("**Déclaré** : le devis du texte scellé comptait une instance gardée arrêtée", 1),
           ("R-2112, R-2113 : instance détruite dès le rapatriement vérifié (§ 4.13)", 1)],
    "C8": [("autant de morceaux que le champ `morceaux=`", 1), ("aucune ligne `ERREUR DE CHAÎNE (C11)` au journal", 1),
           ("etape=episodes-ecrits ' \"$D/progres.txt\"", 1)],
    "C9": [("sous GO-2026-11-10-06 ; R-2112, R-2115", 2)],
    "M1": [('grep -qE "^$ID t06-v2 (running|loading) "', 1)],
    "M2": [("**l'absence de l'identifiant dans l'inventaire filtré fait foi**", 1), ("une seconde demande (même bloc)", 1)],
    "M3": [('`[ "$(date +%s)" -ge <H60> ] && echo "60 USD atteints"`', 1), ("**Code 1** de `depense 60`", 1),
           ('"$(champ telechargement_forfait)"; echo "code $?"', 1)],
    "M4": [('j "commande $n : empreinte', 1), ('[ "$a" -le 600 ]', 1), ("**jugée acceptable**", 1)],
    "M5": [("'!/diag/20261109-070232-t06-reel/' '!/runs/20261109-070232-t06-reel/' '!/donnees/20261109-070232-t06-reel/'", 1),
           ("neuf exclusions", 1)],
    "M6": [("donné par Lazar une fois la session ouverte", 1), ('j "session <identifiant de la session fille>"', 1)],
    "M7": [("grep -F -e GO-2026-11-02-28 -e GO-2026-11-10-01 | grep -vci engagement", 1)],
    "M8": [("`session_v2.verifier_instances`, l. 153", 2), ("Les autres instances vues (identifiant, étiquette, état)", 1)],
    "M9": [('${VAST_API_KEY:+VAST_API_KEY="$VAST_API_KEY"}', 1)],
    "M10": [('if mkdir "$W"; then', 1), ("rien n'est réécrit", 2)],
    "M11": [("« erreur de mémoire à la distillation »", 1), ("« génération des données comprise »", 1)],
    "M12": [('[ "$P7" = prereg/T0.7-sondes-v0-v1.md ]', 1)],
    "M13": [("`BRANCHE_7B`", 1), ("`RUN_T06_7B`", 1), ("`RUN-CONFIRMATION-T06`", 2)],
    "M14": [("message de remise de Lazar", 3)],
}
ABSENTES = [
    "non rempli à la rédaction", "**addendum v3 scellé : non rempli**", "**Dans tous les cas, au plus tard le 2026-11-16 à 23:00Z**",
    "ID=<identifiant créé>", "destruction sur le mot de la mère", "mot de Lazar pour sa dépense", "à remplir par la mère avant la contre-lecture",
    "**à juger par la contre-lecture**", "print(\"motif :\", str(r.get(\"motif\"))[:300])", "au moins `1` morceau ;",
    "`lecture-cout-t06.json`, `resume.json` (hachés", "compte rendu à la mère **avant** toute destruction", "six exclusions",
    "VAST_API_KEY=\"${VAST_API_KEY:-}\"", "la mère écrit `AUCUNE`",
]
ENV_ESSAI = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8"}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def section_de(texte: str, position: int) -> str:
    nom = "(en-tête)"
    for m in re.finditer(r"^#{2,3} +(.+?)\s*$", texte, flags=re.M):
        if m.start() <= position:
            nom = m.group(1)
    return nom[:60]


def titres(texte: str) -> list:
    return [l for l in texte.split("\n") if re.match(r"^#{2,3} ", l)]


def blocs_bash(texte: str) -> list:
    return re.findall(r"^```bash\n(.*?)^```$", texte, flags=re.M | re.S)


def ligne_unique(texte: str, debut: str) -> str:
    l = [x for x in texte.split("\n") if x.startswith(debut)]
    if len(l) != 1:
        raise AssertionError(f"ligne qui commence par {debut[:50]!r} : {len(l)} trouvées")
    return l[0]


def essai_bash(code: str, dossier: Path, extra: dict | None = None) -> tuple[int, str]:
    env = dict(ENV_ESSAI, HOME=str(dossier), **(extra or {}))
    r = subprocess.run(["bash", "-c", code], cwd=dossier, env=env, capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout + r.stderr


def sans_vastai(code: str) -> str:
    """Remplace tout appel de `vastai` par une fonction factice ; refuse un code où un `vastai` réel resterait."""
    code = code.replace("timeout -k 5 120 vastai", "faux_vastai").replace("vastai --version", "faux_vastai --version")
    if re.search(r"\bvastai\b", code):
        raise AssertionError("un appel de `vastai` resterait dans le code d'essai : rien n'est joué")
    return "faux_vastai() { echo \"FAUX-VASTAI $*\"; }\n" + code


def main(argv: list) -> int:
    if len(argv) != 1:
        print("usage : RACINE", file=sys.stderr)
        return 1
    racine = Path(argv[0]).resolve()
    b3, cp, b4 = racine / CHEMIN_B3, racine / CHEMIN_COUPLES, racine / CHEMIN_B4
    defauts: list = []

    # 1. empreintes
    brut = b3.read_bytes()
    if sha(brut) != SHA_B3:
        print(f"ARRÊT : empreinte du brouillon 3 {sha(brut)} ≠ {SHA_B3}")
        return 1
    print(f"brouillon 3 : {CHEMIN_B3} {SHA_B3} (égale)")
    t3 = brut.decode("utf-8")
    cbrut = cp.read_bytes()
    if sha(cbrut) != SHA_COUPLES:
        print(f"ARRÊT : empreinte des couples {sha(cbrut)} ≠ {SHA_COUPLES}")
        return 1
    couples = json.loads(cbrut.decode("utf-8"))
    print(f"couples : {CHEMIN_COUPLES} {SHA_COUPLES} (égale ; {len(couples)} couples)")
    for c in couples:
        if sorted(c) != ["ancien", "id", "motif", "nouveau", "section"]:
            print(f"ARRÊT : {c.get('id')} : clés {sorted(c)}")
            return 1

    # 2. application
    t = t3
    print("\n# application (id ; occurrences de l'« ancien » ; ligne dans le texte courant ; section)")
    for c in couples:
        n = t.count(c["ancien"])
        if n != 1:
            print(f"ARRÊT : {c['id']} : « ancien » présent {n} fois (1 attendu) ; rien n'est écrit")
            return 1
        if c["ancien"] == c["nouveau"]:
            print(f"ARRÊT : {c['id']} : « nouveau » égal à « ancien »")
            return 1
        p = t.index(c["ancien"])
        print(f"{c['id']} ; 1 ; l. {t.count(chr(10), 0, p) + 1} ; {section_de(t, p)}")
        t = t.replace(c["ancien"], c["nouveau"], 1)
    t4 = t

    # 3. écriture (R12)
    octets = t4.encode("utf-8")
    if b4.exists():
        if b4.read_bytes() != octets:
            print(f"ARRÊT (R12) : {CHEMIN_B4} existe et diffère : rien n'est écrasé")
            return 1
        print(f"\n{CHEMIN_B4} déjà écrit, identique")
    else:
        b4.write_bytes(octets)
        print(f"\nécrit : {CHEMIN_B4}")
    print(f"brouillon 4 : {sha(octets)} ; {len(octets)} octets ; {t4.count(chr(10))} lignes")

    print("\n# vérifications")
    # (1) titre, statut
    ok = t4.split("\n", 1)[0] == TITRE_B4 and sum(1 for l in t4.split("\n") if l.startswith("- **Statut** : brouillon 4,")) == 1
    print(f"(1) titre et statut au brouillon 4 : {ok}")
    if not ok:
        defauts.append("titre ou statut")

    # (2) titres de sections
    attendus = [TITRES_CHANGES.get(x, x) for x in titres(t3)]
    ok = titres(t4) == attendus
    print(f"(2) titres de sections : {len(titres(t4))}, égaux à ceux du brouillon 3 hors § 13 et § 14 : {ok}")
    if not ok:
        defauts.append("titres de sections")

    # (3) marqueurs
    trouves = GABARIT.findall(t4)
    ok = sorted(trouves) == sorted(RESTENT) and not any(r in t4 for r in RETIRES)
    print(f"(3) marqueurs restants : {sorted(set(trouves))}, une occurrence chacun : {ok}")
    for v, k in VALEURS_REMPLIES.items():
        n = t4.count(v)
        print(f"    valeur remplie {v!r} : {n} (attendu {k})")
        ok = ok and n == k
    if not ok:
        defauts.append("marqueurs")

    with tempfile.TemporaryDirectory(prefix="ordre-7b-b4-") as tmp:
        tmp = Path(tmp)
        # (4) blocs bash
        blocs = blocs_bash(t4)
        n_ok = 0
        for k, b in enumerate(blocs, 1):
            code = b
            for g, v in FACTICES.items():
                code = code.replace(g, v)
            f = tmp / f"bloc-{k:02d}.sh"
            f.write_text(code, encoding="utf-8")
            r = subprocess.run(["bash", "-n", str(f)], capture_output=True, text=True, env=dict(ENV_ESSAI, HOME=str(tmp)))
            if r.returncode == 0 and "here-document" not in r.stderr:
                n_ok += 1
            else:
                defauts.append(f"bash -n, bloc {k}")
                print(f"    bloc {k} : {r.stderr.strip()[:300]}")
        for nom in ("v13.sh", "inventaire.sh"):
            m = re.search(r'cat > "\$W/' + re.escape(nom) + r"\" <<'FIN'\n(.*?)\nFIN\n", t4, flags=re.S)
            f = tmp / ("contenu-" + nom)
            f.write_text(m.group(1) + "\n", encoding="utf-8")
            r = subprocess.run(["bash", "-n", str(f)], capture_output=True, text=True, env=dict(ENV_ESSAI, HOME=str(tmp)))
            print(f"    contenu écrit {nom} : bash -n code {r.returncode}")
            if r.returncode != 0:
                defauts.append(f"bash -n, {nom}")
        print(f"(4) blocs bash : {len(blocs)} (18 attendus) ; bash -n sans erreur : {n_ok}")
        if len(blocs) != 18:
            defauts.append("nombre de blocs bash")

        # (5) extraits Python
        extraits = [re.search(r"G='(.*?)'\ncd \"\$AM\"", t4, flags=re.S).group(1)]
        extraits += re.findall(r"python3 -I -c '([^']*)'", t4)
        extraits += [x.replace("'$M/src'", "'/tmp/src'") for x in re.findall(r'python3 -I -B -c "([^"]*)"', t4)]
        n_ok = 0
        for x in extraits:
            try:
                ast.parse(x)
                n_ok += 1
            except SyntaxError as e:
                defauts.append(f"ast.parse : {x[:60]!r} : {e}")
        print(f"(5) extraits Python : {len(extraits)} ; ast.parse sans erreur : {n_ok}")

        # (6) jetons de garde
        baisses = []
        for j in JETONS_GARDE:
            a, b = t3.count(j), t4.count(j)
            if a == 0:
                defauts.append(f"jeton absent du brouillon 3 : {j}")
            if b < a:
                baisses.append((j, a, b))
        print(f"(6) jetons de garde : {len(JETONS_GARDE)} ; comptes en baisse : {len(baisses)}")
        for j, a, b in baisses:
            r = BAISSES_VOULUES.get(j)
            print(f"    {j!r} : {a} → {b} ; {'voulu : ' + r if r else 'NON VOULU'}")
            if not r:
                defauts.append(f"jeton de garde perdu : {j}")

        # (7) phrases exigées et absentes
        manque = []
        for constat, phrases in EXIGEES.items():
            for p, k in phrases:
                if t4.count(p) < k:
                    manque.append(f"{constat} : {p[:70]!r} ({t4.count(p)} < {k})")
        presentes = [p for p in ABSENTES if p in t4]
        print(f"(7) phrases exigées : {sum(len(v) for v in EXIGEES.values())} pour {len(EXIGEES)} constats, manquantes : {len(manque)} ; "
              f"phrases retirées encore présentes : {len(presentes)}")
        for m in manque + presentes:
            print(f"    {m}")
        defauts += manque + presentes

        # (8) essais en mémoire
        print("(8) essais en mémoire")
        resultats = essais(t4, tmp)
        for nom, ok, detail in resultats:
            print(f"    {nom} : {'conforme' if ok else 'NON CONFORME'}{' — ' + detail if detail else ''}")
            if not ok:
                defauts.append(f"essai {nom}")

    # (9) différentiel
    d = [l for l in difflib.unified_diff(t3.split("\n"), t4.split("\n"), lineterm="", n=0)
         if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    print(f"(9) différentiel : {sum(1 for l in d if l[0] == '-')} lignes retirées, {sum(1 for l in d if l[0] == '+')} ajoutées ; "
          f"{len(t3.encode())} → {len(octets)} octets")

    if defauts:
        print(f"\nDÉFAUTS ({len(defauts)}) :")
        for x in defauts:
            print(f"  - {x}")
        return 1
    print("\nTOUT PASSE")
    return 0


def essais(t4: str, tmp: Path) -> list:
    res = []
    ligne_a = ligne_unique(t4, "W=/home/user/course-7b-v1;")
    W = tmp / "course-7b-v1"

    def a_ligne() -> str:
        return ligne_a.replace("W=/home/user/course-7b-v1;", f"W={W};", 1)

    def preparer(lancement: str, inventaire: str) -> None:
        (W / "c7b-1").mkdir(parents=True, exist_ok=True)
        (W / "c7b-1" / "lancement.txt").write_text(lancement, encoding="utf-8")
        (W / "inventaire.sh").write_text("cat \"$(dirname \"$0\")/inventaire-factice.txt\"\n", encoding="utf-8")
        (W / "inventaire-factice.txt").write_text(inventaire, encoding="utf-8")

    lanc = ("controles t06 v13 2026-11-14T16:00:00Z\ncommit 935262b1\ncreation preparee 2026-11-14T16:10:00Z\nprix_carte 1.2\n"
            "instance 11111111\ncreation 1794700000\ncreation preparee 2026-11-14T16:20:00Z\ninstance 22222222\ncreation 1794700600\n")

    # M10 : bloc du § 4.0 joué deux fois
    b40 = blocs_bash(t4)[1]
    code = sans_vastai(a_ligne() + "\n" + b40)
    r1 = essai_bash(code, tmp)
    fichiers = {n: sha((W / n).read_bytes()) for n in ("v13.sh", "inventaire.sh")} if (W / "v13.sh").exists() else {}
    j1 = (W / "journal-fille-7b-v1.md").read_text(encoding="utf-8") if (W / "journal-fille-7b-v1.md").exists() else ""
    r2 = essai_bash(code, tmp)
    fichiers2 = {n: sha((W / n).read_bytes()) for n in ("v13.sh", "inventaire.sh")} if (W / "v13.sh").exists() else {}
    j2 = (W / "journal-fille-7b-v1.md").read_text(encoding="utf-8") if (W / "journal-fille-7b-v1.md").exists() else ""
    l1 = j1.strip().split("\n")
    ok = (len(fichiers) == 2 and fichiers == fichiers2 and j1 == j2 and len(l1) == 2 and l1[0].endswith("session <identifiant de la session fille>")
          and "FAUX-VASTAI --version" in r1[1] and "existe déjà" in r2[1] and "FAUX-VASTAI" not in r2[1]
          and "HF_TOKEN absente" in r1[1])
    res.append(("M10 (§ 4.0 joué deux fois : la seconde n'écrit rien)", ok,
                f"1re : code {r1[0]}, journal {len(l1)} lignes ; 2e : « {r2[1].strip()[:70]} »"))

    # M9 : VAST_API_KEY passée seulement si présente (nom remplacé par CLE_FACTICE ; seuls ces arguments sont montrés)
    exe = ligne_unique(t4, "exec env -i PATH=")
    code = ("montrer() { for x in \"$@\"; do case \"$x\" in CLE_FACTICE=*) printf '[%s]\\n' \"$x\";; esac; done; }\n"
            + exe.replace("exec env -i ", "montrer ", 1).replace("VAST_API_KEY", "CLE_FACTICE"))
    ra = essai_bash(code, tmp)
    rb = essai_bash(code, tmp, {"CLE_FACTICE": "valeur factice"})
    ok = ra[1].strip() == "" and rb[1].strip() == "[CLE_FACTICE=valeur factice]"
    res.append(("M9 (absente : non passée ; présente : un seul argument)", ok, f"« {ra[1].strip()} » ; « {rb[1].strip()} »"))

    # C5 : identifiant lu dans lancement.txt
    cas = [(lanc, "22222222", False), ("commit x\n", "", True), (lanc + "instance 12a4\n", "12a4", True)]
    ok = True
    for lt, attendu, arret in cas:
        preparer(lt, "")
        r = essai_bash(a_ligne() + "\n" + CH + '\necho "ID=$ID"', tmp)
        ok = ok and f"ID={attendu}\n" in r[1] and (("ARRÊT : identifiant illisible" in r[1]) == arret)
    res.append(("C5 (dernière ligne `instance` ; illisible : ARRÊT)", ok, ""))

    # C5, M1 : stop (§ 4.12, trois premières lignes du bloc)
    b412 = blocs_bash(t4)[13].split("\n")
    stop = "\n".join(b412[1:4])
    cas = [(lanc, "22222222 t06-v2 running 1.2 3600\n58936096 autre running 0.4 99\n", True),
           (lanc, "22222222 t06-v2 exited 0.1 3600\n", False),
           (lanc, "", False),
           (lanc, "33333333 t06-v2 running 1.2 3600\n", False),
           ("commit x\n", "22222222 t06-v2 running 1.2 3600\n", False)]
    ok = b412[1] == CH
    for lt, inv, joue in cas:
        preparer(lt, inv)
        r = essai_bash(sans_vastai(a_ligne() + "\n" + stop), tmp)
        ok = ok and (("FAUX-VASTAI stop instance 22222222" in r[1]) == joue) and (("aucun stop" in r[1]) != joue) \
            and r[1].count("FAUX-VASTAI") == (1 if joue else 0)
    res.append(("C5 et M1 (`stop` seulement si l'identifiant est une fois à l'inventaire, en marche)", ok, f"{len(cas)} cas"))

    # C5 : destroy (§ 4.13)
    b413 = blocs_bash(t4)[16].split("\n")
    detr = "\n".join(b413[1:4])
    cas = [(lanc, "22222222 t06-v2 exited 0.1 3600\n", True), (lanc, "11111111 t06-v2 exited 0.1 3600\n", False),
           ("commit x\n", "22222222 t06-v2 exited 0.1 3600\n", False)]
    ok = b413[1] == CH
    for lt, inv, joue in cas:
        preparer(lt, inv)
        r = essai_bash(sans_vastai(a_ligne() + "\n" + detr), tmp)
        ok = ok and (("FAUX-VASTAI destroy instance 22222222 -y" in r[1]) == joue) and (("aucun geste" in r[1]) != joue) \
            and (("texte autre (non affiché), code 0" in r[1]) == joue)
    res.append(("C5 (`destroy` et `show instance` seulement si l'identifiant est une fois à l'inventaire)", ok, f"{len(cas)} cas"))

    # C1 : boucle des empreintes et ligne de resume.json, `git` factice qui consigne chaque contenu demandé
    arbre = tmp / "arbre"
    run = "20261112-000000-t06-reel"
    contenus = {f"runs/{run}/manifeste.json": "{}", f"diag/{run}/distillation-t06.json": "{\"d\": 1}",
                f"diag/{run}/resume.json": "{\"ligne_B\": \"SENTINELLE\"}"}
    noms = []
    for p, c in contenus.items():
        (arbre / p).parent.mkdir(parents=True, exist_ok=True)
        (arbre / p).write_text(c, encoding="utf-8")
        (arbre / (p + ".sha256")).write_text(f"{sha(c.encode())}  {Path(p).name}\n", encoding="utf-8")
        noms += [p, p + ".sha256"]
    boucle = ligne_unique(t4, 'grep -E "^(runs|diag)/$RUN/" "$L"')
    ligne_r = ligne_unique(t4, "f=diag/$RUN/resume.json;")
    faux_git = ('git() { [ "$1" = -C ] && shift 2; [ "$1" = show ] || return 99; p="${2#*:}"; echo "$p" >> "$T/demandes.txt"; '
                'cat "$T/arbre/$p" 2>/dev/null || return 128; }\n')

    def jouer_c1(liste: list) -> tuple:
        (tmp / "demandes.txt").write_text("", encoding="utf-8")
        (tmp / "liste.txt").write_text("\n".join(liste) + "\n", encoding="utf-8")
        code = (faux_git + f'T={tmp}; M=/inexistant; R=refs/remotes/origin/x; RUN={run}; L={tmp}/liste.txt\n' + boucle + "\n" + ligne_r)
        r = essai_bash(code, tmp)
        return r[1], (tmp / "demandes.txt").read_text(encoding="utf-8").split()

    s1, d1 = jouer_c1(noms)
    s2, d2 = jouer_c1([x for x in noms if x != f"diag/{run}/resume.json.sha256"])
    (arbre / f"diag/{run}/resume.json.sha256").write_text("abc  resume.json\n", encoding="utf-8")
    s3, d3 = jouer_c1(noms)
    ok = (f"OK runs/{run}/manifeste.json" in s1 and f"OK diag/{run}/distillation-t06.json" in s1
          and f"OK (compagnon seul) diag/{run}/resume.json" in s1 and "ÉCART" not in s1
          and all(f"diag/{run}/resume.json" not in d for d in (d1, d2, d3))
          and "resume.json absent ou compagnon non conforme" in s2 and "resume.json absent ou compagnon non conforme" in s3
          and "SENTINELLE" not in s1 + s2 + s3)
    res.append(("C1 (contenu de `resume.json` jamais demandé ; compagnon seul)", ok,
                f"contenus demandés : {sorted(set(d1))}"))

    # C6 : filtre du motif d'arret.json
    arret = ligne_unique(t4, 'R=refs/remotes/origin/$B; RUN=<run>; git -C "$M" show "$R:diag/$RUN/arret.json"')
    py = re.search(r"python3 -I -c '([^']*)'", arret).group(1)
    cas = [("distillation", "OutOfMemoryError: CUDA out of memory. Tried to allocate 2.00 GiB", False),
           ("données de distillation", "OutOfMemoryError: CUDA out of memory.", False),
           ("test croisé", "ValueError: x", True), ("résumé", "GardeArret: y", True),
           ("épisodes", "GardeArret: ligne_B=0.7", True), ("lecture du coût", "GardeArret: aire=0.71", True),
           ("épisodes", "GardeArret: Échec de la garde d'équivalence", True), ("contrôle d'identité", "GardeArret: logits différents", False)]
    ok = True
    for etape, motif, retenu in cas:
        entree = json.dumps({"resultat": {"etape": etape, "motif": motif, "partiel": {"x": "SENTINELLE-PARTIEL"}}})
        r = subprocess.run([sys.executable, "-I", "-c", py], input=entree, capture_output=True, text=True, env=dict(ENV_ESSAI, HOME=str(tmp)))
        sortie = r.stdout
        ok = ok and r.returncode == 0 and f"etape : {etape}" in sortie and ("retenu (" in sortie) == retenu \
            and ((motif[:20] in sortie) != retenu) and "SENTINELLE" not in sortie
    res.append(("C6 (motif retenu aux étapes des sondes ou avec un mot de C01 ; `partiel` jamais imprimé)", ok, f"{len(cas)} cas"))

    # C8 : morceaux annoncés et poussés ; lignes C11
    bdon = blocs_bash(t4)[15].split("\n")
    lignes_c8 = "\n".join(bdon[4:6])
    d = W / "c7b-1"
    d.mkdir(parents=True, exist_ok=True)
    (d / "progres.txt").write_text("AMORCE 2026-11-14T17:00:00Z : x\nPROGRES 2026-11-15T02:03:04Z etape=episodes-ecrits episodes=896 "
                                   "actions=8960 morceaux=7 reecrits=0\nPROGRES 2026-11-15T02:30:00Z etape=lecture-cout duree_s=1.0\n",
                                   encoding="utf-8")
    morceaux = [f"donnees/{run}/activations-sous-ensemble-t06-{k:03d}.npz" for k in range(7)]

    def jouer_c8(liste: list, journal: str) -> str:
        (tmp / "liste-c8.txt").write_text("\n".join(liste) + "\n", encoding="utf-8")
        (d / "journal-instance.txt").write_text(journal, encoding="utf-8")
        return essai_bash(a_ligne() + f"\nRUN={run}; L={tmp}/liste-c8.txt\n" + lignes_c8, tmp)[1]

    s1 = jouer_c8(morceaux + [m + ".sha256" for m in morceaux], "AMORCE x\n")
    s2 = jouer_c8(morceaux[:6] + [m + ".sha256" for m in morceaux], "AMORCE x\nERREUR DE CHAÎNE (C11) : y fait 9 octets\n")
    ok = ("morceaux annoncés (progres.txt) : 7 ; poussés : 7" in s1 and "(C11) au journal : 0" in s1
          and "poussés : 6" in s2 and "(C11) au journal : 1" in s2)
    res.append(("C8 (morceaux annoncés et poussés ; lignes C11)", ok, s1.strip().replace("\n", " | ")))

    # M4 : § 4.9 (première ligne) puis § 4.10 ; commande factice inoffensive
    l49 = blocs_bash(t4)[10].split("\n")[1].replace("<numéro de la recherche retenue>", "1")
    b410 = "\n".join(blocs_bash(t4)[11].split("\n")[1:3]).replace("<même numéro>", "1")
    f = d / "creation-sortie-1.txt"

    def jouer_m4(journal_faux: bool, vieux: bool) -> str:
        f.write_text("OFFRE CONFORME : x\nCOMMANDE DE CRÉATION (factice)\necho COMMANDE-FACTICE-EXECUTEE\n", encoding="utf-8")
        (W / "journal-fille-7b-v1.md").write_text("", encoding="utf-8")
        essai_bash(a_ligne() + "\n" + l49, tmp)
        if journal_faux:
            (W / "journal-fille-7b-v1.md").write_text("2026-11-14T16:00:00Z commande 1 : empreinte " + "0" * 64 + "\n", encoding="utf-8")
        if vieux:
            v = time.time() - 660
            os.utime(f, (v, v))
        return essai_bash(a_ligne() + "\n" + b410, tmp)[1]

    s1, s2, s3 = jouer_m4(False, False), jouer_m4(True, False), jouer_m4(False, True)
    ok = ("COMMANDE-FACTICE-EXECUTEE" in s1 and "code 0" in s1 and "RIEN N'EST EXÉCUTÉ" in s2 and "COMMANDE-FACTICE" not in s2
          and "RIEN N'EST EXÉCUTÉ" in s3 and "COMMANDE-FACTICE" not in s3)
    res.append(("M4 (exécution seulement à l'empreinte du § 4.9 et dans les dix minutes)", ok, ""))
    return res


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
