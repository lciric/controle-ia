#!/usr/bin/env python3
"""Barreau 6 — fabrique et vérification du candidat 4 à partir du candidat 3, par couples {ancien, nouveau} — v1.

Entrées : le candidat 3 (`accumulation-barreau6-v1-candidat3.md`, empreinte exigée ci-dessous), le fichier de couples
`accumulation-barreau6-v1-candidat4-couples-v1.json` (RV-01 à RV-11 de la revérification sur T0.7 scellé, recopiés tels
qu'écrits et recoupés ici avec leur fichier d'origine, empreinte exigée ; C4-01 à C4-28 du rédacteur du candidat 4).

Contrôles, tous avant l'écriture (le moindre écart : arrêt, rien d'écrit) :
 1. empreintes du candidat 3 et du fichier de couples de la revérification ; RV-01 à RV-11 égaux, à l'octet, à leur origine ;
 2. identifiants : RV-01 à RV-11 et C4-01 à C4-28, dans l'ordre du texte ; G4-01 à G4-17 pour les couples en section gelée ;
 3. chaque « ancien » figure exactement une fois dans le candidat 3, dans une seule section, sans chevauchement ; il figure
    encore exactement une fois au moment de son application ;
 4. la section réelle de chaque couple (titre de niveau 2 qui le contient) est gelée si et seulement si le couple est
    déclaré en section gelée (sections gelées : celles de R1, listées dans le fichier de couples) ;
 5. défaire les couples (chaque « nouveau » exactement une fois, ordre inverse) redonne le candidat 3 à l'octet ;
 6. isolement : appliquer les seuls couples hors sections gelées laisse chaque section gelée égale à l'octet à celle du
    candidat 3, et appliquer les seuls couples en sections gelées laisse tout le reste égal ; mêmes titres, même ordre ;
 7. suppressions sensibles : dans les couples en sections gelées, tout mot supprimé qui porte un chiffre, un signe de
    comparaison ou « strictement » doit figurer dans la liste blanche ci-dessous (déclarée, motif écrit) ; sinon arrêt, nœud ;
 8. aucun marqueur `<<…>>` restant ;
 9. le candidat 4 n'est pas écrasé s'il existe et diffère (R12) ; `controle_ia.prereg.problemes` vide sur le candidat 4
    écrit (sinon il est effacé s'il vient d'être écrit) ; le candidat 3 n'est jamais réécrit.

Lancement : `python3 -I -B <ce script> <racine du dépôt> <dossier des couples> <dossier de sortie>` ; imprime « TOUT PASSE »
et l'empreinte du candidat 4.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

EMPREINTE_C3 = "d48fb8a36c960e85416dfe42b2a9d77824067333b543a9f16540766e02ff1dfb"
EMPREINTE_RV = "771abfaff6a09bea103d67fa2f5521f69690c3795494fe99a815c0e71f15def7"
C3 = "brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat3.md"
RV = "docs/notes/g0-deux-semaines-v1/accumulation-b6-code-v1/reverification-t07-scelle-v1-pieces/couples-proposes-v1.json"
COUPLES = "accumulation-barreau6-v1-candidat4-couples-v1.json"
C4 = "accumulation-barreau6-v1-candidat4.md"
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
# Liste blanche des suppressions sensibles en sections gelées (mot supprimé → motif) : rien d'autre n'est permis.
PERMIS = {
    "200": "écart E-1 (R-2330) : nombre de directions de plancher, 200 → 800 (RV-01 à RV-05)",
    "1,000": "CCB-3 (R-2281) : déclencheur d'audit écrit « 1 exactement », comme le code",
}
COMPARAISONS = {"<", ">", "≤", "≥", "=", "≠", "+", "−", "%", "→"}
MOT = re.compile(r"\w+(?:[.,/]\w+)*|[^\w\s]")
TITRE = re.compile(r"^## +(.+?)\s*$", re.M)


def arret(message: str) -> None:
    sys.exit(f"ARRÊT : {message} ; rien d'écrit")


def decouper(texte: str) -> list[tuple[str, int, int]]:
    """(titre, début, fin) de chaque morceau ; le préambule avant le premier titre de niveau 2 s'appelle « (en-tête) »."""
    t = list(TITRE.finditer(texte))
    morceaux = [("(en-tête)", 0, t[0].start() if t else len(texte))]
    for i, m in enumerate(t):
        morceaux.append((m.group(1).strip(), m.start(), t[i + 1].start() if i + 1 < len(t) else len(texte)))
    return morceaux


def sections(texte: str) -> list[tuple[str, str]]:
    return [(nom, texte[a:b]) for nom, a, b in decouper(texte)]


def gelee(nom: str) -> bool:
    return nom in GELEES


def appliquer(texte: str, couples: list[dict], sens: str = "aller") -> str:
    for c in (couples if sens == "aller" else list(reversed(couples))):
        avant, apres = (c["ancien"], c["nouveau"]) if sens == "aller" else (c["nouveau"], c["ancien"])
        n = texte.count(avant)
        if n != 1:
            arret(f"{c['id']} ({sens}) : texte cherché présent {n} fois (exactement une attendue)")
        texte = texte.replace(avant, apres)
    return texte


def sensible(m: str) -> bool:
    return any(ch.isdigit() for ch in m) or m in COMPARAISONS or m.startswith("strictement")


def main(racine: str, dossier_couples: str, dossier_sortie: str) -> None:
    r = Path(racine)
    c3_brut = (r / C3).read_bytes()
    if hashlib.sha256(c3_brut).hexdigest() != EMPREINTE_C3:
        arret("candidat 3 : empreinte différente de celle attendue")
    c3 = c3_brut.decode("utf-8")
    rv_brut = (r / RV).read_bytes()
    if hashlib.sha256(rv_brut).hexdigest() != EMPREINTE_RV:
        arret("couples de la revérification : empreinte différente de celle attendue")
    rv = {c["id"]: c for c in json.loads(rv_brut.decode("utf-8"))["couples"]}
    doc = json.loads((Path(dossier_couples) / COUPLES).read_text(encoding="utf-8"))
    if doc["candidat_3"]["sha256"] != EMPREINTE_C3 or doc["couples_reverification"]["sha256"] != EMPREINTE_RV:
        arret("fichier de couples : empreintes de référence différentes")
    if tuple(doc["sections_gelees"]) != GELEES:
        arret("fichier de couples : liste des sections gelées différente de celle du script")
    couples = doc["couples"]

    # 1. RV tels qu'écrits
    vus = [c for c in couples if c["id"].startswith("RV-")]
    if sorted(c["id"] for c in vus) != [f"RV-{i:02d}" for i in range(1, 12)]:
        arret("RV-01 à RV-11 attendus, chacun une fois")
    for c in vus:
        if c["ancien"] != rv[c["id"]]["ancien"] or c["nouveau"] != rv[c["id"]]["nouveau"]:
            arret(f"{c['id']} : différent du couple de la revérification (il doit être appliqué tel qu'écrit)")
    print(f"1. RV-01 à RV-11 égaux à l'octet à {RV} ({EMPREINTE_RV[:8]}…)")

    # 2. identifiants et ordre ; 3. anciens uniques, sans chevauchement, dans une seule section
    ids_c4 = [c["id"] for c in couples if c["id"].startswith("C4-")]
    if ids_c4 != [f"C4-{i:02d}" for i in range(1, 29)]:
        arret("C4-01 à C4-28 attendus, dans l'ordre du texte")
    pos = []
    for c in couples:
        n = c3.count(c["ancien"])
        if n != 1:
            arret(f"{c['id']} : « ancien » présent {n} fois dans le candidat 3")
        pos.append(c3.index(c["ancien"]))
    if pos != sorted(pos):
        arret("couples hors de l'ordre du texte")
    for (a, pa), (b, pb) in zip(zip(couples, pos), list(zip(couples, pos))[1:]):
        if pa + len(a["ancien"]) > pb:
            arret(f"chevauchement : {a['id']} et {b['id']}")
    morceaux = decouper(c3)
    g = 0
    for c, p in zip(couples, pos):
        dans = [nom for nom, a, b in morceaux if a <= p and p + len(c["ancien"]) <= b]
        if len(dans) != 1:
            arret(f"{c['id']} : « ancien » à cheval sur deux sections")
        c["_section"] = dans[0]
        # 4. section réelle gelée ⇔ couple déclaré en section gelée
        if gelee(dans[0]) != bool(c["gelee"]):
            arret(f"{c['id']} : section réelle « {dans[0]} » ; déclaré gelée = {c['gelee']}")
        if c["gelee"]:
            g += 1
            if c.get("g4") != f"G4-{g:02d}":
                arret(f"{c['id']} : numéro de déclaration {c.get('g4')} ; G4-{g:02d} attendu")
        elif c.get("g4") is not None:
            arret(f"{c['id']} : hors section gelée, mais porte un numéro G4")
    if g != 17:
        arret(f"{g} couples en sections gelées ; 17 déclarés au texte")
    print(f"2-4. {len(couples)} couples (RV-01 à RV-11, C4-01 à C4-28), ordre du texte, chaque « ancien » une fois, "
          f"aucun chevauchement ; sections réelles conformes ; {g} en sections gelées (G4-01 à G4-17)")

    # application
    c4 = appliquer(c3, couples, "aller")
    # 5. défaire redonne le candidat 3 à l'octet
    if appliquer(c4, couples, "retour").encode("utf-8") != c3_brut:
        arret("défaire les couples ne redonne pas le candidat 3 à l'octet")
    print("5. défaire les couples (ordre inverse, chaque « nouveau » une fois) redonne le candidat 3 à l'octet")

    # 6. isolement des sections gelées
    hors = [c for c in couples if not c["gelee"]]
    dans_g = [c for c in couples if c["gelee"]]
    n_txt, g_txt = appliquer(c3, hors, "aller"), appliquer(c3, dans_g, "aller")
    s3, s4, sn, sg = sections(c3), sections(c4), sections(n_txt), sections(g_txt)
    if [n for n, _ in s3] != [n for n, _ in s4] or [n for n, _ in s3] != [n for n, _ in sn] or [n for n, _ in s3] != [n for n, _ in sg]:
        arret("titres de niveau 2 changés")
    for (nom, t3), (_, t4), (_, tn), (_, tg) in zip(s3, s4, sn, sg):
        if gelee(nom):
            if tn != t3 or t4 != tg:
                arret(f"section gelée « {nom} » touchée par un couple non déclaré gelé")
        else:
            if tg != t3 or t4 != tn:
                arret(f"section « {nom} » touchée par un couple déclaré gelé")
    touchees = Counter(c["_section"] for c in couples)
    print("6. isolement : les couples hors sections gelées laissent les sept sections gelées égales à l'octet ; les couples "
          "en sections gelées ne touchent rien d'autre ; titres inchangés")
    for nom, _ in s3:
        if touchees[nom]:
            print(f"   {'GELÉE ' if gelee(nom) else '       '}{nom} : {touchees[nom]} couple(s) : "
                  + ", ".join(f"{c['id']}{'/' + c['g4'] if c['g4'] else ''}" for c in couples if c['_section'] == nom))

    # 7. suppressions sensibles dans les sections gelées
    total = Counter()
    print("7. suppressions et remplacements, mot à mot, dans les couples en sections gelées :")
    for c in dans_g:
        a, b = MOT.findall(c["ancien"]), MOT.findall(c["nouveau"])
        sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
        sup = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op in ("replace", "delete"):
                sup.append((" ".join(a[i1:i2]), " ".join(b[j1:j2]) if op == "replace" else ""))
                total.update(m for m in a[i1:i2] if sensible(m))
        ins = sum(j2 - j1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == "insert")
        print(f"   {c['g4']} {c['id']} ({c['_section']}) : {len(sup)} remplacement(s) ou suppression(s), {ins} mot(s) inséré(s) seuls")
        for x, y in sup:
            print(f"      « {x} » → « {y} »")
    hors_liste = {m: n for m, n in total.items() if m not in PERMIS}
    if hors_liste:
        arret(f"mot sensible supprimé en section gelée, hors de la liste blanche : {hors_liste} (nœud)")
    print("   mots sensibles supprimés en sections gelées : "
          + ", ".join(f"« {m} » × {n} ({PERMIS[m]})" for m, n in sorted(total.items())))

    # 8. marqueurs ; problemes
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", c4)))
    if restes:
        arret(f"marqueurs restants : {restes}")
    sys.path.insert(0, str(r / "src"))
    from controle_ia.prereg import problemes  # noqa: E402  (code du dépôt, lu après les contrôles de forme)
    print("8. aucun marqueur <<…>> restant")

    # 9. écriture (R12), puis controle_ia.prereg.problemes sur le fichier écrit ; un candidat 4 écrit par ce lancement et
    # non conforme est effacé aussitôt (rien ne reste) ; un candidat 4 déjà présent n'est jamais touché
    sortie = Path(dossier_sortie) / C4
    if sortie.exists():
        if sortie.read_bytes() != c4.encode("utf-8"):
            arret("candidat 4 déjà présent et différent (R12)")
        neuf = False
        print("9. candidat 4 déjà présent, identique")
    else:
        sortie.write_text(c4, encoding="utf-8")
        neuf = True
        print(f"9. candidat 4 écrit : {sortie}")
    p = problemes(sortie)
    if p:
        if neuf:
            sortie.unlink()
        arret(f"controle_ia.prereg.problemes : {p}")
    print("   controle_ia.prereg.problemes sur le candidat 4 : [] (vide)")
    if (r / C3).read_bytes() != c3_brut:
        arret("le candidat 3 a changé pendant le travail")
    for motif in ("6c98ea20", "brouillon 22"):
        lieux = [c4.count("\n", 0, m.start()) + 1 for m in re.finditer(re.escape(motif), c4)]
        print(f"   « {motif} » gardé aux lignes {lieux} (histoire, parent ou origine déclarée)")
    print(f"TOUT PASSE ; candidat 4 : {hashlib.sha256(c4.encode('utf-8')).hexdigest()} ; "
          f"{len(c3.splitlines())} → {len(c4.splitlines())} lignes")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage : accumulation-barreau6-v1-candidat4-faire-v1.py <racine du dépôt> <dossier des couples> <dossier de sortie>")
    main(sys.argv[1], sys.argv[2], sys.argv[3])
