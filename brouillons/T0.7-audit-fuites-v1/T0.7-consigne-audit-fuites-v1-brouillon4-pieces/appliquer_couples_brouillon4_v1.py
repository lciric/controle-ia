#!/usr/bin/env python3
"""Brouillon 4 de la consigne de l'audit des fuites de T0.7 : couples appliqués au brouillon 3 (v1).

Écrit le 2026-11-11 à partir de 13:28 UTC (heure relevée par `date -u`) par un agent neuf (Claude Opus 5.5) de la
session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sous la consigne
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-audit-fuites-t07-brouillon4-v1.md`
(`df38829a025db0f341b1a919d1c2afbfbd19c4f5c7019b8926483dd0f4cf629d`).

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python <ce script> essais     # essais R5 sur jouets, rien n'est écrit
    PYTHONPATH=src .venv/bin/python <ce script> appliquer  # essais, puis couples, brouillon 4 et fichier des couples
    PYTHONPATH=src .venv/bin/python <ce script> appliquer --a-blanc <dossier>  # même calcul, sorties dans <dossier>

Règles tenues : seuls des fichiers nommés sont lus (aucun parcours) ; git seulement par `git show <commit>:<chemin>` ;
aucune écriture hors du brouillon 4 et du fichier des couples ; un fichier existant différent n'est jamais écrasé (R12) ;
chaque « ancien » est présent une fois au moment de son remplacement ; défaire les couples, du dernier au premier, doit
redonner le brouillon 3 à l'octet, sinon rien n'est écrit. Aucun tirage, aucune graine.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

DOSSIER = "brouillons/T0.7-audit-fuites-v1"
B3 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon3.md"
B3_JOURNAL = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon3-journal-v1.md"
B4 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon4.md"
PIECES = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon4-pieces"
FICHIER_COUPLES = f"{PIECES}/couples-brouillon3-vers-brouillon4-v1.json"
JOURNAL_B4 = f"{PIECES}/journal-brouillon4-v1.md"
SCRIPT = f"{PIECES}/appliquer_couples_brouillon4_v1.py"
B21 = "brouillons/T0.7-sondes-v0-v1-brouillon21.md"
B22 = "brouillons/T0.7-sondes-v0-v1-brouillon22.md"
SCELLE = "prereg/T0.7-sondes-v0-v1.md"
RECEPTION = "docs/notes/runs-r1-r2-r4-v1/reception-v4-v1/etape-E-reception-r1-v4-v1.md"
DECISIONS = "registres/decisions.md"
CONSIGNE_B4 = "docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-audit-fuites-t07-brouillon4-v1.md"

ATTENDUS = {
    B3: "0d51099e5ef58829ce83731592eb8573aae8ce8848344488ffc672be45ac273e",
    B3_JOURNAL: "a153119f2edace5a42724758f38a33c418d1ecec7e72d6adad1790e0b4070b9a",
    B21: "f7dcb226efe8671b977ce906c286f7e7243f78a2c9fcf205cbfe5715866ea0cc",
    B22: "8b84cba5bd527e10a3b835ebc0caa7e7da0e31af503904e51621d752d65f0a37",
    SCELLE: "d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5",
    RECEPTION: "bb6652f2cdd914f2ba0b3cd70c8af37ee6dd40fb0da0db8e289133ed6f5e79e1",
    CONSIGNE_B4: "df38829a025db0f341b1a919d1c2afbfbd19c4f5c7019b8926483dd0f4cf629d",
}
# Empreintes des cellules du brouillon 21 citées par le brouillon 3 (§ 2.2 et annexe B).
CELLULE_B21_CONSIGNE = "95c8b659c54f218a903e1d0359a5a4a9ca9bd2e81072741803861a4bb4fa1121"
CELLULE_B21_AUDIT = "9cee4938b9aaaa852a1be89491ad93bbab491d670379681a34de1661bb6754e9"
# Repère du journal du brouillon 3 (§ 3, point 5) : cellule du brouillon 21 avec les couples A, B, C, D.
REPERE_ABCD = "381a72d5b52c1534d116c81b71568dd4728d1a4d90a22a25e99109508e30fede"

# Découpeur (R-2238).
COMMIT_DEC = "c7484c43657a2ce22d76af33efd06aaa11a6aafa"
DOSSIER_DEC = "donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1"
EMPREINTES_DEC = {
    "tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4",
    "tokenizer_config.json": "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424",
    "special_tokens_map.json": "6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec",
}

ECART_FUSION = 40  # éléments égaux (mots ou espaces) au plus entre deux différences fusionnées en un couple
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")


class Arret(Exception):
    """Arrêt : rien n'est écrit."""


# ----------------------------------------------------------------------------------------------- outils

def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def shat(texte: str) -> str:
    return sha(texte.encode("utf-8"))


def lire(chemin: str) -> bytes:
    octets = Path(chemin).read_bytes()
    if chemin in ATTENDUS:
        h = sha(octets)
        if h != ATTENDUS[chemin]:
            raise Arret(f"empreinte de {chemin} : {h} ≠ {ATTENDUS[chemin]}")
        compagnon = Path(chemin + ".sha256")
        if not compagnon.exists():
            raise Arret(f"compagnon absent : {compagnon}")
        hc = compagnon.read_text(encoding="utf-8").split()[0]
        if hc != h:
            raise Arret(f"compagnon de {chemin} : {hc} ≠ {h}")
    return octets


def cellules(ligne: str) -> list[str]:
    """Cellules d'une ligne de tableau, coupées aux `|` non échappés, une espace retirée de chaque bord."""
    if not (ligne.startswith("| ") and ligne.endswith(" |")):
        raise Arret(f"ligne de tableau mal formée : {ligne[:60]!r}")
    morceaux = re.split(r"(?<!\\)\|", ligne)
    if morceaux[0] != "" or morceaux[-1] != "":
        raise Arret("ligne de tableau mal bornée")
    sortie = []
    for m in morceaux[1:-1]:
        if not (m.startswith(" ") and m.endswith(" ")):
            raise Arret(f"cellule sans espace de bord : {m[:40]!r}")
        sortie.append(m[1:-1])
    return sortie


def ligne_cle(texte: str, cle: str) -> tuple[int, str]:
    lignes = texte.split("\n")
    trouvees = [i for i, l in enumerate(lignes) if l.startswith(f"| `{cle}` ")]
    if len(trouvees) != 1:
        raise Arret(f"clé {cle} trouvée {len(trouvees)} fois (une attendue)")
    i = trouvees[0]
    return i + 1, lignes[i]


def passage_en_lignes(texte: str, passage: str) -> tuple[int, int]:
    """Numéros (début, fin) du passage, présent exactement une fois et en lignes entières ; sinon arrêt."""
    if texte.count(passage) != 1:
        raise Arret(f"passage introuvable ou multiple ({texte.count(passage)} fois) : {passage[:60]!r}")
    i = texte.index(passage)
    if not ((i == 0 or texte[i - 1] == "\n") and (i + len(passage) == len(texte) or texte[i + len(passage)] == "\n")):
        raise Arret(f"passage présent, mais pas en lignes entières : {passage[:60]!r}")
    debut = texte[:i].count("\n") + 1
    return debut, debut + passage.count("\n")


def blocs_cites(lignes: list[str], titre_debut: str, titre_fin: str) -> list[tuple[int, str]]:
    """Blocs « > » entre deux titres : (numéro de la première ligne, texte du bloc sans le préfixe)."""
    d, f = lignes.index(titre_debut), lignes.index(titre_fin)
    blocs, courant = [], None
    for k in range(d, f):
        l = lignes[k]
        if l.startswith(">"):
            if courant is None:
                courant = [k + 1, []]
            courant[1].append(l[2:] if l.startswith("> ") else l[1:])
        elif courant is not None:
            blocs.append((courant[0], "\n".join(courant[1])))
            courant = None
    if courant is not None:
        blocs.append((courant[0], "\n".join(courant[1])))
    return blocs


def couples_cellule(a: str, b: str) -> list[tuple[str, str]]:
    """Couples « ancien → nouveau » de a à b : différence par mots et espaces (difflib), différences séparées par
    ECART_FUSION éléments égaux au plus fusionnées, chaque région élargie à gauche sur le contexte commun jusqu'à ce que
    les `**` et les accents graves y soient appariés, puis jusqu'à ce que l'ancien soit unique dans a."""
    ta, tb = re.findall(r"\S+|\s+", a), re.findall(r"\S+|\s+", b)
    ops = [o for o in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes() if o[0] != "equal"]
    regions: list[list[int]] = []
    for _, i1, i2, j1, j2 in ops:
        if regions and i1 - regions[-1][1] <= ECART_FUSION:
            regions[-1][1], regions[-1][3] = i2, j2
        else:
            regions.append([i1, i2, j1, j2])
    couples = []
    for i1, i2, j1, j2 in regions:
        def apparie(s: str) -> bool:
            return s.count("**") % 2 == 0 and s.count("`") % 2 == 0
        while True:
            anc, nou = "".join(ta[i1:i2]), "".join(tb[j1:j2])
            if apparie(anc) and apparie(nou) and anc and a.count(anc) == 1:
                break
            if i1 == 0 or j1 == 0 or ta[i1 - 1] != tb[j1 - 1]:
                raise Arret("région impossible à élargir sur un contexte commun")
            i1, j1 = i1 - 1, j1 - 1
        couples.append((anc, nou))
    return couples


def appliquer(texte: str, couples: list[tuple[str, str]]) -> str:
    for k, (anc, nou) in enumerate(couples, 1):
        n = texte.count(anc)
        if n != 1:
            raise Arret(f"couple {k} : « ancien » présent {n} fois (une attendue) : {anc[:70]!r}")
        texte = texte.replace(anc, nou, 1)
    return texte


def defaire(texte: str, couples: list[tuple[str, str]]) -> str:
    for k, (anc, nou) in reversed(list(enumerate(couples, 1))):
        n = texte.count(nou)
        if n != 1:
            raise Arret(f"couple {k} : « nouveau » présent {n} fois au moment de le défaire : {nou[:70]!r}")
        texte = texte.replace(nou, anc, 1)
    return texte


def git_show(commit: str, chemin: str) -> bytes:
    r = subprocess.run(["git", "show", f"{commit}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise Arret(f"`git show {commit[:8]}:{chemin}` : code {r.returncode}, "
                    f"{r.stderr.decode('utf-8', 'replace').strip()}")
    return r.stdout


def verifier_decoupeur(lire_git, commit: str, dossier: str, attendus: dict[str, str]) -> dict[str, str]:
    """Recalcule les empreintes des fichiers du découpeur par `git show` et les compare aux empreintes attendues et aux
    compagnons du commit (`<fichier>.sha256`, format de sha256sum). Tout écart ou fichier absent → Arret."""
    trouvees = {}
    for nom, attendu in attendus.items():
        h = sha(lire_git(commit, f"{dossier}/{nom}"))
        if h != attendu:
            raise Arret(f"découpeur {nom} : {h} ≠ {attendu}")
        champs = lire_git(commit, f"{dossier}/{nom}.sha256").decode("utf-8").split()
        if len(champs) != 2 or champs[0] != h or champs[1] != nom:
            raise Arret(f"compagnon de {nom} dans le commit : {' '.join(champs)[:90]!r} ≠ {h}  {nom}")
        trouvees[nom] = h
    return trouvees


def ecrire_sans_ecraser(chemin: str, octets: bytes) -> str:
    p = Path(chemin)
    if p.exists():
        if p.read_bytes() != octets:
            raise Arret(f"{chemin} existe avec un autre contenu : rien n'est écrasé (R12)")
        return "déjà présent, identique"
    p.write_bytes(octets)
    return "écrit"


# ----------------------------------------------------------------------------------------------- essais R5

def essais() -> list[str]:
    """Essais sur jouets : chaque garde passe sur un cas sain et arrête sur un artefact."""
    sortie, echecs = [], []

    def attendre_arret(nom, f):
        try:
            f()
        except Arret as e:
            sortie.append(f"essai {nom} : arrêt attendu obtenu ({e})")
            return
        echecs.append(nom)
        sortie.append(f"essai {nom} : ÉCHEC (aucun arrêt)")

    def attendre_sain(nom, f, verif):
        try:
            v = f()
        except Arret as e:
            echecs.append(nom)
            sortie.append(f"essai {nom} : ÉCHEC (arrêt inattendu : {e})")
            return
        if verif(v):
            sortie.append(f"essai {nom} : sain, conforme")
        else:
            echecs.append(nom)
            sortie.append(f"essai {nom} : ÉCHEC (résultat {v!r})")

    # 1. cellules : `|` échappé gardé ; ligne mal formée → arrêt
    attendre_sain("1a cellules, `\\|` échappé", lambda: cellules("| `K` | x \\|p\\| y | c | d |"),
                  lambda v: v == ["`K`", "x \\|p\\| y", "c", "d"])
    attendre_arret("1b cellules, ligne mal formée", lambda: cellules("| `K` | x | c | d"))
    # 2. clé : une fois → sain ; zéro ou deux fois → arrêt
    attendre_sain("2a clé unique", lambda: ligne_cle("a\n| `K` | x | y | z |\nb", "K"), lambda v: v[0] == 2)
    attendre_arret("2b clé absente", lambda: ligne_cle("a\nb", "K"))
    attendre_arret("2c clé en double", lambda: ligne_cle("| `K` | x | y | z |\n| `K` | x | y | z |", "K"))
    # 3. couples : application et retour exacts ; ancien absent ou double → arrêt ; nouveau double au retour → arrêt
    attendre_sain("3a appliquer puis défaire", lambda: defaire(appliquer("a b c", [("b", "B")]), [("b", "B")]),
                  lambda v: v == "a b c")
    attendre_arret("3b ancien absent", lambda: appliquer("a b c", [("z", "Z")]))
    attendre_arret("3c ancien en double", lambda: appliquer("a b b", [("b", "B")]))
    attendre_arret("3d nouveau ambigu au retour", lambda: defaire(appliquer("a b c", [("b", "a")]), [("b", "a")]))
    # 4. couples calculés : appliqués à a, ils redonnent b ; les `**` et accents graves appariés
    a = "une **différence de construction** entre deux, `x` reste ; fin."
    b = "une **différence entre deux** dans un élément, `x` reste ; fin neuve."
    attendre_sain("4 couples calculés", lambda: couples_cellule(a, b),
                  lambda v: appliquer(a, v) == b and all(x.count("**") % 2 == 0 for c in v for x in c))
    # 5. passages : en lignes entières, une fois → numéros ; absent, double ou partiel → arrêt
    attendre_sain("5a passage en lignes", lambda: passage_en_lignes("x\nab\ncd\ny", "ab\ncd"), lambda v: v == (2, 3))
    attendre_arret("5b passage absent", lambda: passage_en_lignes("x\nab\ny", "zz"))
    attendre_arret("5c passage double", lambda: passage_en_lignes("ab\nab", "ab"))
    attendre_arret("5d passage partiel", lambda: passage_en_lignes("xab\ny", "ab"))
    # 6. découpeur : lecteur jouet ; sain → empreintes ; octet changé, compagnon faux, fichier absent → arrêt
    contenu = {f"D/{n}": n.encode() * 3 for n in ("t.json", "c.json")}
    att = {n: sha(n.encode() * 3) for n in ("t.json", "c.json")}

    def lecteur(sain=True, compagnon_faux=False, absent=None, octet=None):
        def lire_git(commit, chemin):
            if chemin == absent:
                raise Arret(f"`git show {commit}:{chemin}` : absent (jouet)")
            if chemin.endswith(".sha256"):
                nom = chemin.rsplit("/", 1)[1][:-7]
                h = "0" * 64 if compagnon_faux else sha(contenu[chemin[:-7]])
                return f"{h}  {nom}\n".encode()
            c = contenu[chemin]
            return c[:-1] + b"#" if chemin == octet else c
        return lire_git

    attendre_sain("6a découpeur sain", lambda: verifier_decoupeur(lecteur(), "c0", "D", att), lambda v: v == att)
    attendre_arret("6b découpeur, octet changé",
                   lambda: verifier_decoupeur(lecteur(octet="D/c.json"), "c0", "D", att))
    attendre_arret("6c découpeur, compagnon faux",
                   lambda: verifier_decoupeur(lecteur(compagnon_faux=True), "c0", "D", att))
    attendre_arret("6d découpeur, commit ou fichier absent",
                   lambda: verifier_decoupeur(lecteur(absent="D/t.json"), "c0", "D", att))
    # 7. écriture : fichier différent existant → arrêt (contrôlé sur un chemin qui n'est jamais écrit : le script)
    attendre_arret("7 écriture sur un fichier différent", lambda: ecrire_sans_ecraser(SCRIPT, b"autre contenu"))
    sortie.append(f"essais : {len(sortie) - len(echecs)} conformes, {len(echecs)} en échec")
    if echecs:
        raise Arret("essais en échec : " + ", ".join(echecs) + "\n" + "\n".join(sortie))
    return sortie


# ----------------------------------------------------------------------------------------------- textes neufs

def bloc_cite(texte: str) -> str:
    return "\n".join("> " + l if l else ">" for l in texte.split("\n"))


def remplissage_ligne(info: dict) -> str:
    L = [
        f"**Source** : texte scellé de T0.7, `{SCELLE}`, sha256",
        f"`{info['sha_scelle']}` (égal à son compagnon et à R-2321),",
        f"section « Lignes de registre », l. {info['l_scelle']} ; remplissage par programme au brouillon 4 (script",
        "`appliquer_couples_brouillon4_v1.py` des pièces du brouillon 4).",
        "",
        "**Égalité avec le brouillon 22** : la ligne `AUDIT-FUITES-T07` du texte scellé (ligne entière, sans fin de ligne) "
        "est",
        f"**{'égale' if info['egale_b22'] else 'différente'} à l'octet** à celle du brouillon 22 (`{B22}`,",
        f"`{info['sha_b22']}`, l. {info['l_b22']}) ; sha256 de la ligne du texte",
        f"scellé : `{info['sha_ligne_scelle']}` ; de la ligne du brouillon 22 :",
        f"`{info['sha_ligne_b22']}`.",
        "",
        "Deuxième cellule (sha256 de la cellule seule, sans fin de ligne :",
        f"`{info['sha_c2']}`) :",
        "",
        bloc_cite(info["c2"]),
        "",
        "Troisième et quatrième cellules (égales à l'octet à celles du brouillon 21, annexe B ; la première cellule l'est "
        "aussi) :",
        "",
        bloc_cite(info["c3"] + " — " + info["c4"]),
        "",
        "Couples « ancien → nouveau » de la cellule du brouillon 21 (annexe B) à celle du texte scellé, **calculés par "
        "programme**",
        f"(différence par mots et espaces, `difflib.SequenceMatcher` ; différences séparées par {ECART_FUSION} éléments égaux "
        "au plus fusionnées ;",
        "chaque région élargie à gauche sur le contexte commun jusqu'à ce que les `**` et les accents graves y soient appariés "
        "et que",
        "l'« ancien » soit unique ; chaque « ancien » présent une fois dans la cellule du brouillon 21 ; appliqués dans l'ordre, "
        "ils",
        f"redonnent la cellule du texte scellé à l'octet) : **{len(info['couples'])} couples**, dans l'ordre de la cellule. "
        "Chacun",
        "recouvre un couple du journal du brouillon 3 (§ 4 ; couple A et couples facultatifs B, C, D, retenus par la mère : "
        "R-2212) ;",
        "les quatre couples du journal, appliqués tels qu'écrits, donnent la même cellule, dont l'empreinte est le repère du "
        "journal",
        f"du brouillon 3 (§ 3, point 5 : `{REPERE_ABCD}`).",
    ]
    for k, (anc, nou, lettre) in enumerate(info["couples"], 1):
        L += ["", f"Couple {k} (couple {lettre} du journal du brouillon 3) — ancien :", "", bloc_cite(anc), "",
              "nouveau :", "", bloc_cite(nou)]
    return "\n".join(L)


def couples_brouillon(info: dict, dec: dict | None, raison_dec: str | None) -> list[dict]:
    """Couples « ancien → nouveau » du brouillon 3 au brouillon 4, dans l'ordre du texte."""
    rempli = dec is not None
    C: list[dict] = []

    def ajoute(ident, motif, anc, nou):
        C.append({"id": ident, "motif": motif, "ancien": anc, "nouveau": nou})

    # Point 5 : titre et statut en tête (qui, quand, d'où).
    ajoute("C00", "mandat, point 5 : titre du brouillon 4",
           "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 3\n",
           "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 4\n")
    ajoute("C01", "mandat, point 5 : statut du brouillon 4 en tête",
           "- **Statut** : **brouillon 3**, non scellé sous son nom définitif, écrit le 2026-11-10 à partir de 12:03 UTC "
           "(heures relevées\n",
           "- **Statut** : **brouillon 4**, non scellé sous son nom définitif, écrit le 2026-11-11 à partir de 13:28 UTC "
           "(heure relevée\n"
           "  par `date -u`) par un **agent neuf** (Claude Opus 5.5, `claude-opus-5-5`, sous-agent de la session mère\n"
           "  `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sous la consigne\n"
           f"  `{CONSIGNE_B4}`\n"
           f"  (`{ATTENDUS[CONSIGNE_B4]}`, R-2346) et les interdits communs v2 (annexe A).\n"
           "  Cet agent n'a écrit ni T0.7, ni ses contre-lectures, ni son module, ni les brouillons 1 à 3 de cette consigne, ni "
           "leur\n"
           "  contre-lecture ; ayant lu T0.7, il est exclu ensuite de tout rôle de lecteur de P3-bis et de tout rôle "
           "d'auditeur ou de\n"
           "  contre-lecteur de l'audit décrit ici. **Brouillon 4 = brouillon 3**\n"
           f"  (`{B3}`,\n"
           f"  `{ATTENDUS[B3]}`, gardé intact) **+ les couples « ancien → nouveau »** du fichier\n"
           f"  `{FICHIER_COUPLES}`,\n"
           "  appliqués chacun une fois par le script `appliquer_couples_brouillon4_v1.py` du même dossier ; défaire les "
           "couples\n"
           "  redonne le brouillon 3 à l'octet (vérifié par le script). Sources, comparaisons et questions au journal\n"
           f"  `{JOURNAL_B4}`.\n"
           "- **Brouillon 3** (historique) : écrit le 2026-11-10 à partir de 12:03 UTC (heures relevées\n")
    # Cohérence : marqueurs.
    if rempli:
        etat_marqueurs = ("  `LIGNE_AUDIT_FUITES_T07_B22` (§ 2.1, sur le texte scellé de T0.7) et `CHEMIN_DECOUPEUR` (§ 6.1) "
                          "**remplis au\n  brouillon 4** ; **reste à remplir avant le scellement** : "
                          "`RAPPORT_CONTRE_LECTURE_2` (§ 14.2, contre-lecture des écarts\n  commandée par la mère). "
                          "Un marqueur restant interdit le scellement.")
    else:
        etat_marqueurs = ("  `LIGNE_AUDIT_FUITES_T07_B22` (§ 2.1) **rempli au brouillon 4, sur le texte scellé de T0.7** ; "
                          "**restent à remplir\n  avant le scellement** : `CHEMIN_DECOUPEUR` (§ 6.1 ; le commit du découpeur "
                          "n'est pas dans le clone local, couple\n  prêt au fichier des couples, journal du brouillon 4, § 5) "
                          "et `RAPPORT_CONTRE_LECTURE_2` (§ 14.2, contre-lecture des\n  écarts commandée par la mère). "
                          "Un marqueur restant interdit le scellement.")
    ajoute("C02", "cohérence (« texte scellé » au lieu de « brouillon 22 ») : état des marqueurs",
           "- **Marqueurs à remplir avant le scellement** (par la session mère, par programme, chacun avec sa source) :\n"
           "  `LIGNE_AUDIT_FUITES_T07_B22` (§ 2.1) ; `CHEMIN_DECOUPEUR` (§ 6.1) ; `RAPPORT_CONTRE_LECTURE_2` (§ 14, ou ligne\n"
           "  retirée si la mère ne commande pas de contre-lecture des écarts). Un marqueur restant interdit le scellement.",
           "- **Marqueurs** (remplis par programme, chacun avec sa source) :\n" + etat_marqueurs)
    ajoute("C03", "cohérence : ordre des opérations",
           "**Ordre** : brouillon 22 de T0.7 (ligne `AUDIT-FUITES-T07` corrigée), puis remplissage de\n"
           "  `LIGNE_AUDIT_FUITES_T07_B22`, puis scellement de cette consigne.",
           "**Ordre** : brouillon 22 de T0.7 (ligne `AUDIT-FUITES-T07` corrigée), puis texte scellé de\n"
           "  T0.7 (R-2321 ; même ligne, à l'octet), puis remplissage de `LIGNE_AUDIT_FUITES_T07_B22` sur le texte scellé "
           + ("et de\n  `CHEMIN_DECOUPEUR` (brouillon 4), puis contre-lecture des écarts (§ 14.2), puis scellement de cette "
              "consigne." if rempli else
              "(brouillon 4),\n  puis remplissage de `CHEMIN_DECOUPEUR`, contre-lecture des écarts (§ 14.2) et scellement de "
              "cette consigne."))
    ajoute("C04", "cohérence : ce qui gouverne (ligne du texte scellé)",
           "La ligne `AUDIT-FUITES-T07` est recopiée au § 2.1 **telle qu'elle sera au brouillon 22** (marqueur), sa recopie du\n",
           "La ligne `AUDIT-FUITES-T07` est recopiée au § 2.1 **telle qu'elle est au texte scellé de T0.7**\n"
           f"  (`{SCELLE}`, `{info['sha_scelle']}`, l. {info['l_scelle']} ; "
           "remplie au\n"
           f"  brouillon 4 ; {'égale' if info['egale_b22'] else 'différente'} à l'octet à celle du brouillon 22), sa recopie du\n")
    ajoute("C05", "cohérence : vérification des cellules contre le texte scellé",
           "l. 2067 et 2068). Au scellement de cette consigne, puis à celui de\n"
           "  T0.7 (`prereg/T0.7-sondes-v0-v1.md`), la session mère vérifie par programme que les cellules recopiées aux § 2.1 "
           "et 2.2\n  sont celles du texte de T0.7 alors en vigueur (empreintes des cellules)",
           f"l. 2067 et 2068 ; ligne `CONSIGNE-AUDIT-FUITES-T07` égale à l'octet à celle\n"
           f"  du texte scellé, l. {info['l_scelle_consigne']}, vérifié par programme au brouillon 4). Au scellement de cette "
           "consigne, la session mère\n  vérifie par programme que les cellules recopiées aux § 2.1 et 2.2 sont celles du texte "
           "scellé de T0.7 (empreintes des\n  cellules ; fait au brouillon 4, journal du brouillon 4, § 2)")
    ajoute("C06", "cohérence : § 0, Q3 (ligne corrigée, puis scellée)",
           "est corrigée **au brouillon 22 de T0.7**, pas ici\n"
           "  (phrase proposée au journal, § 4) ; cette consigne applique la ligne telle qu'elle sera au brouillon 22 (§ 2.1). "
           "Si la\n  ligne du brouillon 22 ne dit pas l'option (a), cette consigne est refaite.",
           "a été corrigée **au brouillon 22 de T0.7**, pas\n"
           "  ici (couple A du journal du brouillon 3, § 4, retenu avec B, C et D : R-2212), et la ligne corrigée est celle du "
           "texte\n  scellé (R-2321) ; cette consigne applique la ligne du texte scellé (§ 2.1). Si la ligne du texte scellé ne "
           "dit pas\n  l'option (a), cette consigne est refaite (conformité vérifiée par la contre-lecture des écarts, § 14.2).")
    ajoute("C07", "cohérence : § 1 (définition gelée du texte scellé)",
           "ligne `AUDIT-FUITES-T07` (au brouillon 22) :",
           "ligne `AUDIT-FUITES-T07` (texte scellé de T0.7, § 2.1) :")
    # Point 1 : § 2.1.
    ajoute("C08", "mandat, point 1 : titre du § 2.1",
           "### 2.1 Ligne `AUDIT-FUITES-T07`, telle qu'elle sera au brouillon 22 de T0.7\n",
           "### 2.1 Ligne `AUDIT-FUITES-T07`, telle qu'elle est au texte scellé de T0.7\n")
    ajoute("C09", "mandat, point 1 : marqueur rempli sur le texte scellé",
           "<<LIGNE_AUDIT_FUITES_T07_B22>>", remplissage_ligne(info))
    ajoute("C10", "mandat, point 1 : note de remplissage",
           "(**Remplissage**, par la session mère, par programme, après l'écriture du brouillon 22 : le marqueur est remplacé "
           "par\n(1) le chemin et le sha256 du brouillon 22 ; (2) la deuxième cellule de la ligne `AUDIT-FUITES-T07`, citée en "
           "bloc (« > »),\nà l'octet ; (3) le sha256 de cette cellule seule, sans fin de ligne ; (4) les troisième et quatrième "
           "cellules, citées de\nmême ; (5) la liste des couples « ancien → nouveau » qui la séparent de la cellule du "
           "brouillon 21 (annexe B), calculée par\nprogramme. La contre-lecture des écarts (§ 14) vérifie ce remplissage.)",
           "(**Remplissage**, fait au brouillon 4, par programme, **sur le texte scellé** de T0.7, le brouillon 22 ayant été "
           "dépassé\npar le texte scellé (R-2321, R-2346) : le marqueur est remplacé par (1) le chemin et le sha256 du texte "
           "scellé ; (2) la\ndeuxième cellule de la ligne `AUDIT-FUITES-T07`, citée en bloc (« > »), à l'octet ; (3) le sha256 "
           "de cette cellule seule,\nsans fin de ligne ; (4) les troisième et quatrième cellules, citées de même ; (5) la liste "
           "des couples « ancien → nouveau »\nqui la séparent de la cellule du brouillon 21 (annexe B), calculée par programme ; "
           "(6) l'égalité à l'octet, ou non, de la\nligne du texte scellé avec celle du brouillon 22. La contre-lecture des "
           "écarts (§ 14.2) vérifie ce remplissage.)")
    # Point 2 : § 2.2 et § 2.3 (passages égaux : seuls les repères du texte scellé sont ajoutés).
    titre22 = ("### 2.2 Ligne `CONSIGNE-AUDIT-FUITES-T07` — deuxième cellule, brouillon 21 (sha256 : "
               f"`{CELLULE_B21_CONSIGNE}`)\n")
    ajoute("C11", "mandat, point 2 : § 2.2 comparé au texte scellé (égal)",
           titre22,
           titre22 + "\nLigne entière (quatre cellules) du brouillon 21 (l. 2086) **égale à l'octet** à celle du texte scellé "
           f"de T0.7\n(`{SCELLE}`, l. {info['l_scelle_consigne']} ; vérifié par programme au brouillon 4, journal du brouillon 4, "
           "§ 2) :\nrien n'est recopié à neuf.\n")
    ajoute("C12", "mandat, point 2 : § 2.3 comparé au texte scellé (égal)",
           "### 2.3 Passages de T0.7 qui lisent F ou bornent l'audit (recopiés tels quels du brouillon 21)\n",
           "### 2.3 Passages de T0.7 qui lisent F ou bornent l'audit (recopiés tels quels du brouillon 21)\n\n"
           "Chaque passage cité ci-dessous est présent **une fois, en lignes entières et à l'octet**, dans le texte scellé de "
           "T0.7\n(vérifié par programme au brouillon 4, journal du brouillon 4, § 3) : rien n'est recopié à neuf ; les numéros "
           "de ligne\nsont ceux du brouillon 21, suivis de ceux du texte scellé.\n")
    P = info["passages"]  # numéros du texte scellé, par repère
    ajoute("C13", "mandat, point 2 : repère du texte scellé (point 4 ter)",
           "Plan, point 4 ter (l. 1350-1355) :", f"Plan, point 4 ter (l. 1350-1355 ; texte scellé l. {P['4ter']}) :")
    ajoute("C14", "mandat, point 2 : repère du texte scellé (L1b)",
           "Grille, ligne L1b (l. 1765 ; seule", f"Grille, ligne L1b (l. 1765 ; texte scellé l. {P['L1b']} ; seule")
    ajoute("C15", "mandat, point 2 : repère du texte scellé (L6)",
           "Grille, ligne L6 (l. 1769) :", f"Grille, ligne L6 (l. 1769 ; texte scellé l. {P['L6']}) :")
    ajoute("C16", "mandat, point 2 : repère du texte scellé (liste d'arrêt)",
           "Liste d'arrêt (l. 1864-1867) :", f"Liste d'arrêt (l. 1864-1867 ; texte scellé l. {P['arret']}) :")
    ajoute("C17", "mandat, point 2 : repère du texte scellé (« Non interprétable »)",
           "Métrique, puce « Non interprétable » (l. 1083-1089 ;",
           f"Métrique, puce « Non interprétable » (l. 1083-1089 ; texte scellé l. {P['ni']} ;")
    ajoute("C18", "mandat, point 2 : repère du texte scellé (module, paraphrase)",
           "Module (T0.7 l. 2442-2444, et code) :",
           f"Module (T0.7 l. 2442-2444 au brouillon 21, l. {P['module']} au texte scellé, mêmes lignes à l'octet ; et code) :")
    # Point 3 : découpeur (seulement si le commit est présent et les empreintes égales).
    if rempli:
        ajoute("C19", "mandat, point 3 : `CHEMIN_DECOUPEUR` (R-2238)", "`<<CHEMIN_DECOUPEUR>>`", texte_decoupeur(dec))
    # Cohérence : § 6.
    ajoute("C20", "cohérence : § 6, lecture (a)",
           "(R-2203 ; texte de la ligne au brouillon 22, § 2.1)",
           "(R-2203 ; ligne du texte scellé de T0.7, § 2.1)")
    # Point 4 : § 14.2 et annexe B.
    ajoute("C21", "mandat, point 4 : titre du § 14.2 (commandée)",
           "### 14.2 Contre-lecture des écarts (recommandée avant le scellement)",
           "### 14.2 Contre-lecture des écarts (commandée par la mère : R-2212, Q16 ; R-2346)")
    ajoute("C22", "mandat, point 4 : objet du § 14.2",
           "(chemin et sha256 ; sous-agent neuf, autre modèle que Claude Opus 5.5 ; objet : le\n"
           "différentiel du brouillon 2 au brouillon 3, le remplissage des marqueurs `LIGNE_AUDIT_FUITES_T07_B22` et\n"
           "`CHEMIN_DECOUPEUR`, et la conformité de la ligne du brouillon 22 à la décision R-2203 ; fichiers à lui donner : ce\n"
           "brouillon et son journal, le brouillon 2, la contre-lecture 1, le brouillon 22 de T0.7, les interdits communs v2). "
           "Si la mère\nne la commande pas, elle retire cette section 14.2 au scellement et le dit dans la ligne de registre.",
           "(chemin et sha256 ; sous-agent neuf, autre modèle que Claude Opus 5.5 (Claude Fable 5.2,\n"
           "R-2346) ; objet : le **différentiel du brouillon 3 au brouillon 4** (couples du fichier des couples, rejoués : "
           "défaire les\ncouples redonne le brouillon 3 à l'octet), les **remplissages** des marqueurs "
           "`LIGNE_AUDIT_FUITES_T07_B22` (sur le\ntexte scellé : chemin, empreintes, cellules à l'octet, couples depuis le "
           "brouillon 21, égalité avec le brouillon 22) et\n`CHEMIN_DECOUPEUR` (commit, dossier et trois empreintes contre "
           "R-2238 et les compagnons du commit), et la **conformité\nde la ligne `AUDIT-FUITES-T07` du texte scellé à la "
           "décision R-2203** (lecture (a)) ; fichiers à lui donner : ce brouillon,\nses pièces (fichier des couples, script, "
           "sortie du script, journal du brouillon 4), le brouillon 3 et son journal, la\ncontre-lecture 1, le texte scellé de "
           "T0.7 et, pour comparaison, ses brouillons 21 et 22, les interdits communs v2).")
    ajoute("C23", "mandat, point 4 : annexe B (reste, pour comparaison)",
           "pour comparaison (recopiée par programme ; non applicable une fois le § 2.1 rempli)",
           "pour comparaison (recopiée par programme ; **reste** : base des couples du § 2.1 ; non applicable, le § 2.1, rempli "
           "sur le texte scellé, gouverne)")
    return C


def texte_decoupeur(dec: dict) -> str:
    return ("le dossier\n"
            f"`{DOSSIER_DEC}/` du commit `{COMMIT_DEC}` (branche de données privée\n"
            f"`{DOSSIER_DEC}`, orpheline, jamais fusionnée dans `main` ; R-2238), extrait par\n"
            f"`git archive {COMMIT_DEC} {DOSSIER_DEC}/ | tar -x -C <bac à sable>` dans le bac à\n"
            "sable de l'auditeur, sur sa machine (exception écrite à la règle 4 des interdits, annexe A : cette seule commande, "
            "en\nlecture ; le commit doit être présent dans le clone local, aucun `fetch`), avec les empreintes "
            + " ; ".join(f"`{n}` `{h}`" for n, h in dec.items())
            + " (R-2238 ; égales à la réception R1 v4,\n"
            f"`{RECEPTION}` l. 70-72, `{ATTENDUS[RECEPTION][:8]}…` ; recalculées par `git show` au remplissage et "
            "égales aux\ncompagnons du commit)")


# ----------------------------------------------------------------------------------------------- principal

def constats() -> tuple[dict, list[str]]:
    rapport: list[str] = []
    txt = {c: lire(c).decode("utf-8") for c in (B3, B3_JOURNAL, B21, B22, SCELLE, RECEPTION, CONSIGNE_B4)}
    for c in (B3, B3_JOURNAL, B21, B22, SCELLE, RECEPTION, CONSIGNE_B4):
        rapport.append(f"entrée {c} : sha256 {ATTENDUS[c]} (égale à l'attendu et au compagnon)")
    info: dict = {"sha_scelle": ATTENDUS[SCELLE], "sha_b22": ATTENDUS[B22]}
    # Lignes AUDIT-FUITES-T07 et CONSIGNE-AUDIT-FUITES-T07.
    l21a, la21 = ligne_cle(txt[B21], "AUDIT-FUITES-T07")
    l22a, la22 = ligne_cle(txt[B22], "AUDIT-FUITES-T07")
    lsa, las = ligne_cle(txt[SCELLE], "AUDIT-FUITES-T07")
    l21c, lc21 = ligne_cle(txt[B21], "CONSIGNE-AUDIT-FUITES-T07")
    l22c, lc22 = ligne_cle(txt[B22], "CONSIGNE-AUDIT-FUITES-T07")
    lsc, lcs = ligne_cle(txt[SCELLE], "CONSIGNE-AUDIT-FUITES-T07")
    c21, c22, cs = cellules(la21), cellules(la22), cellules(las)
    k21, ks = cellules(lc21), cellules(lcs)
    for nom, c in (("AUDIT b21", c21), ("AUDIT b22", c22), ("AUDIT scellé", cs), ("CONSIGNE b21", k21),
                   ("CONSIGNE scellé", ks)):
        if len(c) != 4:
            raise Arret(f"{nom} : {len(c)} cellules (quatre attendues)")
    if shat(c21[1]) != CELLULE_B21_AUDIT or shat(k21[1]) != CELLULE_B21_CONSIGNE:
        raise Arret("cellules du brouillon 21 différentes des empreintes citées par le brouillon 3")
    rapport.append(f"AUDIT-FUITES-T07 : brouillon 21 l. {l21a}, brouillon 22 l. {l22a}, texte scellé l. {lsa}")
    rapport.append(f"CONSIGNE-AUDIT-FUITES-T07 : brouillon 21 l. {l21c}, brouillon 22 l. {l22c}, texte scellé l. {lsc}")
    rapport.append(f"cellule 2 AUDIT, brouillon 21 : {shat(c21[1])} (= citée par le brouillon 3, annexe B)")
    rapport.append(f"cellule 2 AUDIT, texte scellé : {shat(cs[1])} ; brouillon 22 : {shat(c22[1])}")
    for k in (0, 2, 3):
        rapport.append(f"cellule {k + 1} AUDIT : brouillon 21 = texte scellé : {c21[k] == cs[k]} ; "
                       f"brouillon 22 = texte scellé : {c22[k] == cs[k]}")
        if c21[k] != cs[k]:
            raise Arret(f"cellule {k + 1} de AUDIT-FUITES-T07 changée entre le brouillon 21 et le texte scellé")
    egale_b22 = la22 == las
    rapport.append(f"ligne AUDIT entière, brouillon 22 = texte scellé à l'octet : {egale_b22} "
                   f"(sha256 {shat(las)} / {shat(la22)})")
    rapport.append(f"ligne CONSIGNE entière : brouillon 21 = texte scellé : {lc21 == lcs} ; brouillon 22 = texte scellé : "
                   f"{lc22 == lcs} (sha256 {shat(lcs)})")
    if lc21 != lcs:
        raise Arret("ligne CONSIGNE-AUDIT-FUITES-T07 changée : le § 2.2 serait à recopier (cas non prévu ici)")
    # Couples de la cellule (brouillon 21 → texte scellé), et recoupement avec les couples A, B, C, D du journal.
    cc = couples_cellule(c21[1], cs[1])
    if appliquer(c21[1], cc) != cs[1]:
        raise Arret("les couples calculés ne redonnent pas la cellule du texte scellé")
    journal = txt[B3_JOURNAL]
    jl = journal.split("\n")
    q = [l[4:] for l in jl if l.startswith("  > ")]
    if len(q) != 2:
        raise Arret("couple A du journal du brouillon 3 : deux lignes « > » attendues")
    norm = re.sub(r"\n +", " ", journal)
    jc = {"A": (q[0], q[1])}
    for lettre in "BCD":
        m = re.search(r"^- " + lettre + r" : « (.*?) » → « (.*?) »\.$", norm, re.M)
        if not m:
            raise Arret(f"couple {lettre} du journal introuvable")
        jc[lettre] = (m.group(1), m.group(2))
    cellule_j = appliquer(c21[1], [jc[x] for x in "ABCD"])
    rapport.append(f"couples A, B, C, D du journal appliqués à la cellule du brouillon 21 : {shat(cellule_j)} ; "
                   f"= texte scellé : {cellule_j == cs[1]} ; = repère du journal : {shat(cellule_j) == REPERE_ABCD}")
    if cellule_j != cs[1] or shat(cellule_j) != REPERE_ABCD:
        raise Arret("la cellule du texte scellé n'est pas celle des couples A, B, C, D")
    etiquetes = []
    for anc, nou in cc:
        i = c21[1].index(anc)
        lettres = [x for x in "ABCD" if (lambda p: p < i + len(anc) and i < p + len(jc[x][0]))(c21[1].index(jc[x][0]))]
        if len(lettres) != 1:
            raise Arret(f"couple calculé sans couple unique du journal : {anc[:50]!r}")
        etiquetes.append((anc, nou, lettres[0]))
        rapport.append(f"couple calculé ({lettres[0]}) : ancien {len(anc)} caractères, présent "
                       f"{c21[1].count(anc)} fois ; nouveau {len(nou)} caractères")
    info.update(l_scelle=lsa, l_b22=l22a, l_scelle_consigne=lsc, egale_b22=egale_b22, sha_ligne_scelle=shat(las),
                sha_ligne_b22=shat(la22), c2=cs[1], sha_c2=shat(cs[1]), c3=cs[2], c4=cs[3], couples=etiquetes)
    # § 2.2 et annexe B du brouillon 3 : recopies égales aux cellules du brouillon 21.
    b3l = txt[B3].split("\n")
    i22 = b3l.index("### 2.2 Ligne `CONSIGNE-AUDIT-FUITES-T07` — deuxième cellule, brouillon 21 (sha256 : "
                    f"`{CELLULE_B21_CONSIGNE}`)")
    if b3l[i22 + 2] != "> " + k21[1] or b3l[i22 + 6] != "> " + k21[2] + " — " + k21[3]:
        raise Arret("§ 2.2 du brouillon 3 différent des cellules du brouillon 21")
    rapport.append("§ 2.2 du brouillon 3 : cellule 2 et cellules 3 — 4 égales à l'octet au brouillon 21, donc au texte scellé")
    ib = [i for i, l in enumerate(b3l) if l.startswith("## Annexe B")][0]
    if b3l[ib + 5] != "> " + c21[1] or b3l[ib + 9] != "> " + c21[2] + " — " + c21[3]:
        raise Arret("annexe B du brouillon 3 différente de la ligne du brouillon 21")
    rapport.append("annexe B du brouillon 3 : cellules égales à l'octet au brouillon 21")
    # § 2.3 : chaque passage cité, dans le brouillon 21 et dans le texte scellé.
    blocs = blocs_cites(b3l, "### 2.3 Passages de T0.7 qui lisent F ou bornent l'audit (recopiés tels quels du brouillon 21)",
                        "## 3. Qui exécute")
    reperes = ["4ter", "L1b", "L6", "arret", "ni"]
    attendus_b21 = {"4ter": (1350, 1355), "L1b": (1765, 1765), "L6": (1769, 1769), "arret": (1864, 1867),
                    "ni": (1083, 1089)}
    if len(blocs) != len(reperes):
        raise Arret(f"§ 2.3 : {len(blocs)} blocs cités ({len(reperes)} attendus)")
    passages = {}
    for rep, (lb3, bloc) in zip(reperes, blocs):
        d21 = passage_en_lignes(txt[B21], bloc)
        if d21 != attendus_b21[rep]:
            raise Arret(f"§ 2.3 {rep} : brouillon 21 l. {d21}, attendu {attendus_b21[rep]}")
        ds = passage_en_lignes(txt[SCELLE], bloc)
        passages[rep] = f"{ds[0]}" if ds[0] == ds[1] else f"{ds[0]}-{ds[1]}"
        rapport.append(f"§ 2.3 {rep} (brouillon 3 l. {lb3}, sha256 {shat(bloc)}) : brouillon 21 l. "
                       f"{d21[0]}-{d21[1]}, texte scellé l. {ds[0]}-{ds[1]} (une fois, lignes entières, à l'octet)")
    l21 = txt[B21].split("\n")
    mod = "\n".join(l21[2441:2444])
    dm = passage_en_lignes(txt[SCELLE], mod)
    passages["module"] = f"{dm[0]}-{dm[1]}"
    rapport.append(f"§ 2.3 paraphrase « Module » : brouillon 21 l. 2442-2444 = texte scellé l. {dm[0]}-{dm[1]} "
                   f"(sha256 {shat(mod)})")
    # Autres renvois du brouillon 3 aux lignes du brouillon 21 (information, non changés au brouillon 4).
    for n in (1385, 1386, 1387, 1388, 1389, 1390, 2046, 2047, 2048, 2049, 2050, 2078):
        l = l21[n - 1]
        occ = [i + 1 for i, x in enumerate(txt[SCELLE].split("\n")) if x == l]
        rapport.append(f"renvoi au brouillon 21 l. {n} : ligne présente dans le texte scellé aux l. {occ}")
    info["passages"] = passages
    # R-2238 et réception R1 v4 : empreintes du découpeur.
    r2238 = [l for l in Path(DECISIONS).read_text(encoding="utf-8").split("\n") if l.startswith("| R-2238 |")]
    if len(r2238) != 1:
        raise Arret("ligne R-2238 introuvable ou multiple")
    for n, h in EMPREINTES_DEC.items():
        if h not in r2238[0] or f"`{h}`" not in txt[RECEPTION]:
            raise Arret(f"empreinte de {n} absente de R-2238 ou de la réception R1 v4")
    if COMMIT_DEC not in r2238[0] or DOSSIER_DEC not in r2238[0]:
        raise Arret("commit ou dossier du découpeur absent de R-2238")
    rapport.append("découpeur : commit, dossier et trois empreintes présents dans R-2238 ; trois empreintes présentes dans "
                   f"la réception R1 v4 ({RECEPTION}, sha256 {ATTENDUS[RECEPTION]})")
    return info, rapport


def principal(argv: list[str]) -> int:
    a_blanc = None
    if len(argv) == 3 and argv[0] == "appliquer" and argv[1] == "--a-blanc":
        a_blanc, argv = Path(argv[2]), argv[:1]
    if argv not in (["essais"], ["appliquer"]):
        print(__doc__)
        return 2
    if not (Path(SCRIPT).is_file() and Path(B3).is_file()):
        print("ARRÊT : à lancer depuis la racine du dépôt (script ou brouillon 3 introuvable)")
        return 1
    try:
        for l in essais():
            print(l)
        if argv == ["essais"]:
            return 0
        info, rapport = constats()
        for l in rapport:
            print(l)
        dec, raison = None, None
        try:
            dec = verifier_decoupeur(git_show, COMMIT_DEC, DOSSIER_DEC, EMPREINTES_DEC)
            print("découpeur : trois empreintes recalculées par `git show`, égales à R-2238 et aux compagnons du commit")
        except Arret as e:
            raison = str(e)
            print(f"découpeur : NON REMPLI — {raison}")
        couples = couples_brouillon(info, dec, raison)
        b3 = lire(B3).decode("utf-8")
        b4 = appliquer(b3, [(c["ancien"], c["nouveau"]) for c in couples])
        if defaire(b4, [(c["ancien"], c["nouveau"]) for c in couples]).encode("utf-8") != lire(B3):
            raise Arret("défaire les couples ne redonne pas le brouillon 3 à l'octet")
        print(f"couples : {len(couples)} appliqués, chacun une fois ; défaits du dernier au premier : brouillon 3 à l'octet")
        restants = sorted(set(MARQUEUR.findall(b4)))
        for m in restants:
            print(f"marqueur restant : {m} ({b4.count(m)} fois)")
        if restants != sorted(set(["<<RAPPORT_CONTRE_LECTURE_2>>"] + ([] if dec else ["<<CHEMIN_DECOUPEUR>>"]))):
            raise Arret(f"marqueurs restants inattendus : {restants}")
        if dec is None:
            prepare = {"id": "C19-en-attente", "motif": "mandat, point 3 : `CHEMIN_DECOUPEUR` (R-2238) — NON APPLIQUÉ : "
                       + raison, "ancien": "`<<CHEMIN_DECOUPEUR>>`",
                       "nouveau": texte_decoupeur(dict(EMPREINTES_DEC)),
                       "condition": "à appliquer seulement après que `git show` sur le commit rend les trois fichiers à ces "
                                    "empreintes, égales aux compagnons du commit (relancer ce script, sortie sous un nom neuf)"}
        sortie_couples = {
            "de": {"chemin": B3, "sha256": ATTENDUS[B3]},
            "vers": {"chemin": B4, "sha256": shat(b4)},
            "regle": "appliqués dans l'ordre, chaque « ancien » présent une fois au moment de son remplacement ; défaits du "
                     "dernier au premier (« nouveau » → « ancien », chaque « nouveau » présent une fois), ils redonnent le "
                     "brouillon 3 à l'octet",
            "couples": couples,
            "en_attente": [prepare] if dec is None else [],
        }
        o_couples = (json.dumps(sortie_couples, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        cible_b4, cible_couples = B4, FICHIER_COUPLES
        if a_blanc is not None:
            print(f"À BLANC : sorties écrites sous {a_blanc}, aucune sous {DOSSIER}")
            cible_b4, cible_couples = str(a_blanc / Path(B4).name), str(a_blanc / Path(FICHIER_COUPLES).name)
        print(f"brouillon 4 : {cible_b4} — {ecrire_sans_ecraser(cible_b4, b4.encode('utf-8'))} — sha256 {shat(b4)}")
        print(f"couples : {cible_couples} — {ecrire_sans_ecraser(cible_couples, o_couples)} — sha256 {sha(o_couples)}")
        return 0
    except Arret as e:
        print(f"ARRÊT : {e}")
        return 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
