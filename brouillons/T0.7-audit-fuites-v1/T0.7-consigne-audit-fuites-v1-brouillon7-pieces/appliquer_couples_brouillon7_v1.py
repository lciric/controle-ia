#!/usr/bin/env python3
"""Brouillon 7 de la consigne de l'audit des fuites de T0.7 : brouillon 6 + trois couples (v1).

Écrit le 2026-11-11 à partir de 14:06 UTC (heure relevée par `date -u`) par l'agent des brouillons 4 à 6 (Claude Opus
5.5), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur le message de la mère reçu à 14:06 UTC : la
puce « Marqueurs » doit être juste dans le texte scellé (couple prêt au journal du brouillon 6, § 4), statut
« brouillon 7 » au besoin.

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python <ce script> essais
    PYTHONPATH=src .venv/bin/python <ce script> appliquer [--a-blanc <dossier>]

Chaque « ancien » présent une fois ; défaire les couples redonne le brouillon 6 à l'octet ; aucun `<<…>>` ; aucun fichier
différent écrasé (R12). Réutilise, après contrôle de son empreinte, le script scellé du brouillon 4 et ses 19 essais.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

DOSSIER = "brouillons/T0.7-audit-fuites-v1"
B6 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon6.md"
SCRIPT_B4 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon4-pieces/appliquer_couples_brouillon4_v1.py"
B7 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon7.md"
PIECES = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon7-pieces"
FICHIER_COUPLES = f"{PIECES}/couples-brouillon6-vers-brouillon7-v1.json"
JOURNAL_B7 = f"{PIECES}/journal-brouillon7-v1.md"
SCRIPT = f"{PIECES}/appliquer_couples_brouillon7_v1.py"
NOM_DEFINITIF = "prereg/T0.7-consigne-audit-fuites-v1.md"
ATTENDUS = {
    B6: "71118f666253c99abeb3bf60a162e5aba8fdcb5e5788c2265ae444be7a30fcac",
    SCRIPT_B4: "7539b4779e9def222791fafa5165915e00ab85a7bca12693c85101ccd41dd037",
}
MARQUEUR = re.compile(r"<<[^<>\n]*>>")


class Arret(Exception):
    pass


def sha(o: bytes) -> str:
    return hashlib.sha256(o).hexdigest()


def lire(chemin: str) -> bytes:
    o = Path(chemin).read_bytes()
    if sha(o) != ATTENDUS[chemin] or Path(chemin + ".sha256").read_text(encoding="utf-8").split()[0] != sha(o):
        raise Arret(f"empreinte ou compagnon de {chemin} différent de {ATTENDUS[chemin]}")
    return o


def module_b4():
    lire(SCRIPT_B4)
    spec = importlib.util.spec_from_file_location("couples_b4", SCRIPT_B4)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def couples() -> list[dict]:
    return [
        {"id": "F01", "motif": "puce « Marqueurs » juste : aucun marqueur restant ; `RAPPORT_CONTRE_LECTURE_2` rempli au "
         "§ 14.2 (couple prêt au journal du brouillon 6, § 4)",
         "ancien": "; **reste à remplir avant le scellement** : `RAPPORT_CONTRE_LECTURE_2` (§ 14.2,\n"
                   "  contre-lecture des écarts commandée par la mère).",
         "nouveau": "; `RAPPORT_CONTRE_LECTURE_2` (§ 14.2) **rempli au brouillon 6**\n"
                    "  (R-2355) ; **aucun marqueur ne reste**."},
        {"id": "F02", "motif": "titre et statut en tête : brouillon 7, prêt au scellement ; l'ancien statut devient "
         "« Brouillon 6 (historique) »",
         "ancien": "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 6\n\n"
                   "- **Statut** : **brouillon 6, prêt au scellement** par la session mère sous le nom définitif\n",
         "nouveau": "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 7\n\n"
                    "- **Statut** : **brouillon 7, prêt au scellement** par la session mère sous le nom définitif\n"
                    f"  `{NOM_DEFINITIF}` (avec compagnon `.sha256`) ; écrit le 2026-11-11 à partir de 14:06 UTC\n"
                    "  (heure relevée par `date -u`) par l'agent des brouillons 4 à 6 (Claude Opus 5.5, `claude-opus-5-5`, "
                    "sous-agent de\n  la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur le message de la mère de "
                    "14:06 UTC. **Brouillon 7 = brouillon 6**\n"
                    f"  (`{B6}`,\n"
                    f"  `{ATTENDUS[B6]}`, scellé, gardé intact) **+ trois couples** du fichier\n"
                    f"  `{FICHIER_COUPLES}`,\n"
                    "  appliqués chacun une fois par le script `appliquer_couples_brouillon7_v1.py` du même dossier : la "
                    "puce\n  « Marqueurs » mise à jour (aucun marqueur restant ; `RAPPORT_CONTRE_LECTURE_2` rempli au "
                    "§ 14.2), ce statut, et la\n  phrase du statut du brouillon 6 sur cette puce ; défaire les trois "
                    "couples redonne le brouillon 6 à l'octet\n"
                    f"  (vérifié par le script). **Aucun marqueur ne reste.** Journal : `{JOURNAL_B7}`.\n"
                    "- **Brouillon 6** (historique) : prêt au scellement par la session mère sous le nom définitif\n"},
        {"id": "F03", "motif": "statut historique du brouillon 6 : sa phrase sur la puce « Marqueurs » n'est plus vraie au "
         "brouillon 7",
         "ancien": "la puce « Marqueurs » ci-dessous garde l'état du brouillon 5.",
         "nouveau": "la puce « Marqueurs » y gardait l'état du brouillon 5 (mise à jour au\n  brouillon 7)."},
    ]


def principal(argv: list[str]) -> int:
    a_blanc = None
    if len(argv) == 3 and argv[0] == "appliquer" and argv[1] == "--a-blanc":
        a_blanc, argv = Path(argv[2]), argv[:1]
    if argv not in (["essais"], ["appliquer"]):
        print(__doc__)
        return 2
    if not (Path(SCRIPT).is_file() and Path(B6).is_file()):
        print("ARRÊT : à lancer depuis la racine du dépôt")
        return 1
    try:
        m = module_b4()
        print(f"script du brouillon 4 : sha256 {ATTENDUS[SCRIPT_B4]} (égal à l'attendu et au compagnon)")
        for l in m.essais():
            print(l)
        ok = not MARQUEUR.findall("".join(c["nouveau"] for c in couples()))
        print(f"essai B7-1 couples sans marqueur : {'sain, conforme' if ok else 'ÉCHEC'}")
        if not ok:
            raise Arret("essai B7-1 en échec")
        if argv == ["essais"]:
            return 0
        b6 = lire(B6)
        print(f"entrée {B6} : sha256 {ATTENDUS[B6]} (égale à l'attendu et au compagnon)")
        C = couples()
        t6 = b6.decode("utf-8")
        avant = MARQUEUR.findall(t6)
        print(f"marqueurs au brouillon 6 : {avant if avant else 'aucun'}")
        t7 = m.appliquer(t6, [(c["ancien"], c["nouveau"]) for c in C])
        if m.defaire(t7, [(c["ancien"], c["nouveau"]) for c in C]).encode("utf-8") != b6:
            raise Arret("défaire ne redonne pas le brouillon 6 à l'octet")
        print(f"couples : {len(C)} appliqués, chacun une fois ; défaits du dernier au premier : brouillon 6 à l'octet")
        restants = MARQUEUR.findall(t7)
        print(f"marqueurs restants : {restants if restants else 'aucun'}")
        if restants or "reste à remplir" in t7.split("## 0.")[0]:
            raise Arret("marqueur restant, ou en-tête qui dit encore « reste à remplir »")
        o = (json.dumps({"de": {"chemin": B6, "sha256": ATTENDUS[B6]},
                         "vers": {"chemin": B7, "sha256": sha(t7.encode("utf-8"))},
                         "regle": "appliqués dans l'ordre, chaque « ancien » présent une fois ; défaits du dernier au "
                                  "premier, ils redonnent le brouillon 6 à l'octet",
                         "couples": C}, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        c7, cc = B7, FICHIER_COUPLES
        if a_blanc is not None:
            print(f"À BLANC : sorties sous {a_blanc}")
            c7, cc = str(a_blanc / Path(B7).name), str(a_blanc / Path(FICHIER_COUPLES).name)
        print(f"brouillon 7 : {c7} — {m.ecrire_sans_ecraser(c7, t7.encode('utf-8'))} — sha256 {sha(t7.encode('utf-8'))}")
        print(f"couples : {cc} — {m.ecrire_sans_ecraser(cc, o)} — sha256 {sha(o)}")
        return 0
    except Exception as e:
        if type(e).__name__ != "Arret":
            raise
        print(f"ARRÊT : {e}")
        return 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
