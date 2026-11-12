#!/usr/bin/env python3
"""Barreau 6 — fabrique et vérification du candidat 5 à partir du candidat 4, par couples {ancien, nouveau} — v1.

Entrées : le candidat 4 (`accumulation-barreau6-v1-candidat4.md`, empreinte exigée), le fichier de couples
`accumulation-barreau6-v1-candidat5-couples-v1.json` (C5-01 à C5-15 ; décisions de la mère R-2339), et le fichier de couples
du candidat 4 (empreinte exigée), dont le couple préparé Q-1 doit être recopié tel quel.

Contrôles, tous avant l'écriture (le moindre écart : arrêt, rien d'écrit) :
 1. empreintes du candidat 4 et du fichier de couples du candidat 4 ; le couple Q-1 du candidat 5 égal, à l'octet, au couple
    préparé au candidat 4 (`proposes_non_appliques`) ;
 2. identifiants C5-01 à C5-15 dans l'ordre du texte ; G5-01 à G5-04 pour les couples en section gelée ;
 3. chaque « ancien » figure exactement une fois dans le candidat 4, dans une seule section, sans chevauchement, et encore une
    fois au moment de son application ;
 4. section réelle (titre de niveau 2) gelée si et seulement si le couple est déclaré en section gelée ;
 5. défaire les couples (chaque « nouveau » exactement une fois, ordre inverse) redonne le candidat 4 à l'octet ;
 6. isolement : les couples hors sections gelées laissent les sept sections gelées égales à l'octet, et inversement ; mêmes
    titres, même ordre ;
 7. suppressions sensibles en sections gelées : tout mot supprimé qui porte un chiffre, un signe de comparaison ou
    « strictement » arrête le script (liste blanche vide : aucune suppression de ce genre n'est permise au candidat 5), nœud ;
 8. aucun marqueur `<<…>>` restant ;
 9. le candidat 5 n'est pas écrasé s'il existe et diffère (R12) ; `controle_ia.prereg.problemes` vide sur le candidat 5 écrit
    (sinon il est effacé s'il vient d'être écrit) ; le candidat 4 n'est jamais réécrit.

Lancement : `python3 -I -B <ce script> <racine du dépôt> <dossier des couples> <dossier de sortie>` ; imprime « TOUT PASSE »
et l'empreinte du candidat 5.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

EMPREINTE_C4 = "e3aef53004d18b07e7eb30c31d30ad00986f69528cd55f2e0a57bea9423dcf84"
EMPREINTE_COUPLES_C4 = "d9dbbb8d211fa99eab7ab1b93b9ed3dde39fb923b35249e7bd349bdbca472bbb"
C4 = "brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat4.md"
COUPLES_C4 = ("brouillons/accumulation-barreau6-v1/accumulation-barreau6-v1-candidat4-pieces/"
              "accumulation-barreau6-v1-candidat4-couples-v1.json")
COUPLES = "accumulation-barreau6-v1-candidat5-couples-v1.json"
C5 = "accumulation-barreau6-v1-candidat5.md"
N_COUPLES, N_GELES = 15, 4
GELEES = ("Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
          "Critères de lecture gelés", "Liste d'arrêt")
PERMIS: dict[str, str] = {}   # aucune suppression sensible permise au candidat 5
COMPARAISONS = {"<", ">", "≤", "≥", "=", "≠", "+", "−", "%", "→"}
MOT = re.compile(r"\w+(?:[.,/]\w+)*|[^\w\s]")
TITRE = re.compile(r"^## +(.+?)\s*$", re.M)


def arret(message: str) -> None:
    sys.exit(f"ARRÊT : {message} ; rien d'écrit")


def decouper(texte: str) -> list[tuple[str, int, int]]:
    t = list(TITRE.finditer(texte))
    morceaux = [("(en-tête)", 0, t[0].start() if t else len(texte))]
    for i, m in enumerate(t):
        morceaux.append((m.group(1).strip(), m.start(), t[i + 1].start() if i + 1 < len(t) else len(texte)))
    return morceaux


def sections(texte: str) -> list[tuple[str, str]]:
    return [(nom, texte[a:b]) for nom, a, b in decouper(texte)]


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
    c4_brut = (r / C4).read_bytes()
    if hashlib.sha256(c4_brut).hexdigest() != EMPREINTE_C4:
        arret("candidat 4 : empreinte différente de celle attendue")
    c4 = c4_brut.decode("utf-8")
    cb = (r / COUPLES_C4).read_bytes()
    if hashlib.sha256(cb).hexdigest() != EMPREINTE_COUPLES_C4:
        arret("couples du candidat 4 : empreinte différente de celle attendue")
    q1 = next(q for q in json.loads(cb.decode("utf-8"))["proposes_non_appliques"] if q["id"] == "Q-1")
    doc = json.loads((Path(dossier_couples) / COUPLES).read_text(encoding="utf-8"))
    if doc["candidat_4"]["sha256"] != EMPREINTE_C4 or tuple(doc["sections_gelees"]) != GELEES:
        arret("fichier de couples : référence ou sections gelées différentes")
    couples = doc["couples"]

    # 1. Q-1 tel que préparé
    q = [c for c in couples if c["source"] == "Q-1"]
    if len(q) != 1 or (q[0]["ancien"], q[0]["nouveau"]) != (q1["ancien"], q1["nouveau"]):
        arret("Q-1 : absent, en double ou différent du couple préparé au candidat 4")
    print(f"1. Q-1 ({q[0]['id']}) égal à l'octet au couple préparé du candidat 4 ({EMPREINTE_COUPLES_C4[:8]}…)")

    # 2-4. identifiants, positions, sections
    if [c["id"] for c in couples] != [f"C5-{i:02d}" for i in range(1, N_COUPLES + 1)]:
        arret(f"C5-01 à C5-{N_COUPLES:02d} attendus, dans l'ordre")
    pos = []
    for c in couples:
        n = c4.count(c["ancien"])
        if n != 1:
            arret(f"{c['id']} : « ancien » présent {n} fois dans le candidat 4")
        pos.append(c4.index(c["ancien"]))
    if pos != sorted(pos):
        arret("couples hors de l'ordre du texte")
    for i in range(len(couples) - 1):
        if pos[i] + len(couples[i]["ancien"]) > pos[i + 1]:
            arret(f"chevauchement : {couples[i]['id']} et {couples[i + 1]['id']}")
    morceaux = decouper(c4)
    g = 0
    for c, p in zip(couples, pos):
        dans = [nom for nom, a, b in morceaux if a <= p and p + len(c["ancien"]) <= b]
        if len(dans) != 1:
            arret(f"{c['id']} : « ancien » à cheval sur deux sections")
        c["_section"] = dans[0]
        if (dans[0] in GELEES) != bool(c["gelee"]):
            arret(f"{c['id']} : section réelle « {dans[0]} » ; déclaré gelée = {c['gelee']}")
        if c["gelee"]:
            g += 1
            if c.get("g5") != f"G5-{g:02d}":
                arret(f"{c['id']} : numéro de déclaration {c.get('g5')} ; G5-{g:02d} attendu")
        elif c.get("g5") is not None:
            arret(f"{c['id']} : hors section gelée, mais porte un numéro G5")
    if g != N_GELES:
        arret(f"{g} couples en sections gelées ; {N_GELES} déclarés au texte")
    print(f"2-4. {len(couples)} couples, ordre du texte, chaque « ancien » une fois, aucun chevauchement ; sections réelles "
          f"conformes ; {g} en sections gelées (G5-01 à G5-{g:02d})")

    c5 = appliquer(c4, couples, "aller")
    # 5. défaire
    if appliquer(c5, couples, "retour").encode("utf-8") != c4_brut:
        arret("défaire les couples ne redonne pas le candidat 4 à l'octet")
    print("5. défaire les couples (ordre inverse, chaque « nouveau » une fois) redonne le candidat 4 à l'octet")

    # 6. isolement
    hors = [c for c in couples if not c["gelee"]]
    dans_g = [c for c in couples if c["gelee"]]
    s4, s5 = sections(c4), sections(c5)
    sn, sg = sections(appliquer(c4, hors, "aller")), sections(appliquer(c4, dans_g, "aller"))
    titres = [n for n, _ in s4]
    if any([n for n, _ in s] != titres for s in (s5, sn, sg)):
        arret("titres de niveau 2 changés")
    for (nom, t4), (_, t5), (_, tn), (_, tg) in zip(s4, s5, sn, sg):
        if nom in GELEES:
            if tn != t4 or t5 != tg:
                arret(f"section gelée « {nom} » touchée par un couple non déclaré gelé")
        elif tg != t4 or t5 != tn:
            arret(f"section « {nom} » touchée par un couple déclaré gelé")
    touchees = Counter(c["_section"] for c in couples)
    print("6. isolement : les couples hors sections gelées laissent les sept sections gelées égales à l'octet ; les couples "
          "en sections gelées ne touchent rien d'autre ; titres inchangés")
    for nom in titres:
        if touchees[nom]:
            print(f"   {'GELÉE ' if nom in GELEES else '       '}{nom} : "
                  + ", ".join(f"{c['id']}{'/' + c['g5'] if c['g5'] else ''}" for c in couples if c['_section'] == nom))

    # 7. suppressions sensibles
    total = Counter()
    print("7. suppressions et remplacements, mot à mot, dans les couples en sections gelées :")
    for c in dans_g:
        a, b = MOT.findall(c["ancien"]), MOT.findall(c["nouveau"])
        ops = difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
        sup = [(" ".join(a[i1:i2]), " ".join(b[j1:j2]) if op == "replace" else "")
               for op, i1, i2, j1, j2 in ops if op in ("replace", "delete")]
        for op, i1, i2, j1, j2 in ops:
            if op in ("replace", "delete"):
                total.update(m for m in a[i1:i2] if sensible(m))
        ins = sum(j2 - j1 for op, i1, i2, j1, j2 in ops if op == "insert")
        print(f"   {c['g5']} {c['id']} ({c['_section']}) : {len(sup)} remplacement(s) ou suppression(s), {ins} mot(s) inséré(s) seuls")
        for x, y in sup:
            print(f"      « {x} » → « {y} »")
    hors_liste = {m: n for m, n in total.items() if m not in PERMIS}
    if hors_liste:
        arret(f"mot sensible supprimé en section gelée, hors de la liste blanche : {hors_liste} (nœud)")
    print("   mots sensibles supprimés en sections gelées : aucun")

    # 8. marqueurs
    restes = sorted(set(re.findall(r"<<[A-Z0-9_]+>>", c5)))
    if restes:
        arret(f"marqueurs restants : {restes}")
    print("8. aucun marqueur <<…>> restant")

    # 9. écriture, puis problemes
    sys.path.insert(0, str(r / "src"))
    from controle_ia.prereg import problemes  # noqa: E402
    sortie = Path(dossier_sortie) / C5
    if sortie.exists():
        if sortie.read_bytes() != c5.encode("utf-8"):
            arret("candidat 5 déjà présent et différent (R12)")
        neuf = False
        print("9. candidat 5 déjà présent, identique")
    else:
        sortie.write_text(c5, encoding="utf-8")
        neuf = True
        print(f"9. candidat 5 écrit : {sortie}")
    p = problemes(sortie)
    if p:
        if neuf:
            sortie.unlink()
        arret(f"controle_ia.prereg.problemes : {p}")
    print("   controle_ia.prereg.problemes sur le candidat 5 : [] (vide)")
    if (r / C4).read_bytes() != c4_brut:
        arret("le candidat 4 a changé pendant le travail")
    print(f"TOUT PASSE ; candidat 5 : {hashlib.sha256(c5.encode('utf-8')).hexdigest()} ; "
          f"{len(c4.splitlines())} → {len(c5.splitlines())} lignes")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage : accumulation-barreau6-v1-candidat5-faire-v1.py <racine du dépôt> <dossier des couples> <dossier de sortie>")
    main(sys.argv[1], sys.argv[2], sys.argv[3])
