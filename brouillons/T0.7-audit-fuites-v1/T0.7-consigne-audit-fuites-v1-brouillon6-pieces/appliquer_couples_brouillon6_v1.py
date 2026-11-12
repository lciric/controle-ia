#!/usr/bin/env python3
"""Brouillon 6 de la consigne de l'audit des fuites de T0.7 : brouillon 5 + les quatorze couples de la contre-lecture 2
+ deux couples du rédacteur (v1).

Écrit le 2026-11-11 à partir de 14:03 UTC (heure relevée par `date -u`) par l'agent des brouillons 4 et 5 (Claude Opus
5.5), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`, sur décision de la mère (R-2355 : les quatorze
couples retenus ; marqueur `RAPPORT_CONTRE_LECTURE_2` rempli ; statut « prêt au scellement »).

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python <ce script> essais
    PYTHONPATH=src .venv/bin/python <ce script> appliquer
    PYTHONPATH=src .venv/bin/python <ce script> appliquer --a-blanc <dossier>

Les couples de la contre-lecture sont lus dans son fichier scellé et appliqués tels quels, dans son ordre ; le texte
obtenu doit valoir le repère du contre-lecteur (`142d0a9e…`), sinon arrêt. Puis deux couples du rédacteur. Chaque
« ancien » présent une fois au moment de son remplacement ; défaire les seize couples, du dernier au premier, doit
redonner le brouillon 5 à l'octet ; aucun marqueur `<<…>>` ne doit rester ; aucun fichier différent n'est écrasé (R12).
Réutilise, après contrôle de son empreinte, les fonctions du script scellé du brouillon 4 et ses 19 essais sur jouets.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

DOSSIER = "brouillons/T0.7-audit-fuites-v1"
B5 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon5.md"
SCRIPT_B4 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon4-pieces/appliquer_couples_brouillon4_v1.py"
B6 = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon6.md"
PIECES = f"{DOSSIER}/T0.7-consigne-audit-fuites-v1-brouillon6-pieces"
FICHIER_COUPLES = f"{PIECES}/couples-brouillon5-vers-brouillon6-v1.json"
JOURNAL_B6 = f"{PIECES}/journal-brouillon6-v1.md"
SCRIPT = f"{PIECES}/appliquer_couples_brouillon6_v1.py"
CL2 = "prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon5-cl2.md"
CL2_PIECES = "prereg/contre-lectures/T0.7-consigne-audit-fuites-v1-brouillon5-cl2-pieces"
CL2_COUPLES = f"{CL2_PIECES}/couples-cl2-v1.json"
CL2_CONSIGNE = ("docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/"
                "consigne-contre-lecture-2-audit-fuites-b5-v1.md")
NOM_DEFINITIF = "prereg/T0.7-consigne-audit-fuites-v1.md"

ATTENDUS = {
    B5: "7228ce724d4f2a7c146124ceb70156cf99118b2acebcdc4b3b7d9e5d977d2b67",
    SCRIPT_B4: "7539b4779e9def222791fafa5165915e00ab85a7bca12693c85101ccd41dd037",
    CL2: "c9035156f36d0a394a7548c1771c02a222d28f9fedd7ae4cb9f4ee44c66f0415",
    CL2_COUPLES: "47af739fd47873b12227ccced3f55a818891079713aea2520730b93cae9ae387",
    CL2_CONSIGNE: "ac451ef0104ae69c8cb2e9606a0182637c55f77f4f1f378c6594b8ef6b812467",
}
REPERE_CL2 = "142d0a9e9c0451bcef7468556e38370c1f997628d08d27328d85e942aae1b5e8"  # brouillon 5 + 14 couples (CL2)
ORDRE_CL2 = ["K01", "K02", "K03", "K14", "K04", "K05", "K06", "K07", "K08", "K09", "K10", "K11", "K12", "K13"]
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")


class Arret(Exception):
    pass


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire(chemin: str) -> bytes:
    octets = Path(chemin).read_bytes()
    h = sha(octets)
    if h != ATTENDUS[chemin]:
        raise Arret(f"empreinte de {chemin} : {h} ≠ {ATTENDUS[chemin]}")
    hc = Path(chemin + ".sha256").read_text(encoding="utf-8").split()[0]
    if hc != h:
        raise Arret(f"compagnon de {chemin} : {hc} ≠ {h}")
    return octets


def module_b4():
    lire(SCRIPT_B4)
    spec = importlib.util.spec_from_file_location("couples_b4", SCRIPT_B4)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def couples_redacteur() -> list[dict]:
    e01_nouveau = (
        f"**Rapport** : `{CL2}`\n"
        f"(`{ATTENDUS[CL2]}`, égal à son compagnon) ; contre-lecteur :\n"
        "sous-agent neuf, **Claude Fable 5.2** (`claude-fable-5-2`), autre modèle que l'auteur des brouillons 2 à 6 (Claude Opus\n"
        f"5.5) ; consigne `{CL2_CONSIGNE}`\n"
        f"(`{ATTENDUS[CL2_CONSIGNE][:8]}…`) ; texte relu : brouillon 5 (`{ATTENDUS[B5][:8]}…`) ; verdict : **« scellable après "
        "corrections »**, quatre couples\nexigés (K01, K02, K03, K14) et dix facultatifs (K04 à K13), **tous retenus par la "
        "mère (R-2355)** et appliqués tels\nquels au brouillon 6 (texte obtenu égal au repère du contre-lecteur, "
        f"`{REPERE_CL2[:8]}…`) ; pièces scellées :\n`{CL2_PIECES}/` (couples\n`{ATTENDUS[CL2_COUPLES][:8]}…`) ; pas de "
        "troisième contre-lecture (avis du lecteur, R-2355). Ce qui était commandé\n(texte du brouillon 5, où « ce brouillon » "
        "désigne le brouillon 5) : (chemin et sha256 ;"
    )
    e02_nouveau = (
        "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 6\n\n"
        "- **Statut** : **brouillon 6, prêt au scellement** par la session mère sous le nom définitif\n"
        f"  `{NOM_DEFINITIF}` (avec compagnon `.sha256`) ; écrit le 2026-11-11 à partir de 14:03 UTC\n"
        "  (heure relevée par `date -u`) par l'agent des brouillons 4 et 5 (Claude Opus 5.5, `claude-opus-5-5`, sous-agent de\n"
        "  la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`), sur décision de la mère (R-2355). **Brouillon 6 = brouillon 5**\n"
        f"  (`{B5}`,\n"
        f"  `{ATTENDUS[B5]}`, scellé, gardé intact) **+ les quatorze couples de la\n"
        f"  contre-lecture 2** (`{CL2_COUPLES}`,\n"
        f"  `{ATTENDUS[CL2_COUPLES]}` ; K01, K02, K03, K14 exigés, K04 à K13\n"
        "  facultatifs), appliqués tels quels dans leur ordre (texte obtenu égal au repère du contre-lecteur,\n"
        f"  `{REPERE_CL2}`) **+ deux couples du rédacteur** (remplissage de\n"
        "  `RAPPORT_CONTRE_LECTURE_2` au § 14.2 ; ce statut) ; les seize couples sont au fichier\n"
        f"  `{FICHIER_COUPLES}`,\n"
        "  appliqués chacun une fois par le script `appliquer_couples_brouillon6_v1.py` du même dossier ; défaire les seize\n"
        "  couples redonne le brouillon 5 à l'octet (vérifié par le script). **Plus aucun marqueur** : le dernier,\n"
        "  `RAPPORT_CONTRE_LECTURE_2`, est rempli au § 14.2 ; la puce « Marqueurs » ci-dessous garde l'état du brouillon 5.\n"
        f"  Journal : `{JOURNAL_B6}`.\n"
        "- **Brouillon 5** (historique) : écrit le 2026-11-11 à partir de 13:47 UTC (heure relevée\n"
    )
    return [
        {"id": "E01", "origine": "rédacteur", "motif": "remplissage de `RAPPORT_CONTRE_LECTURE_2` (§ 14.2) : chemin et "
         "empreinte complète du rapport, contre-lecteur, verdict, R-2355",
         "ancien": "`<<RAPPORT_CONTRE_LECTURE_2>>` (chemin et sha256 ;", "nouveau": e01_nouveau},
        {"id": "E02", "origine": "rédacteur", "motif": "titre et statut en tête : brouillon 6, prêt au scellement par la "
         f"session mère sous `{NOM_DEFINITIF}` ; l'ancien statut devient « Brouillon 5 (historique) »",
         "ancien": "# Consigne de l'audit des fuites de T0.7 — v1 — brouillon 5\n\n"
                   "- **Statut** : **brouillon 5**, non scellé sous son nom définitif, écrit le 2026-11-11 à partir de 13:47 "
                   "UTC (heure relevée\n",
         "nouveau": e02_nouveau},
    ]


def essais_b6(m) -> list[str]:
    sortie = list(m.essais())
    t = "".join(c["nouveau"] for c in couples_redacteur())
    ok = not MARQUEUR.findall(t) and ATTENDUS[CL2] in t and "Claude Fable 5.2" in t and "R-2355" in t \
        and NOM_DEFINITIF in t
    sortie.append(f"essai B6-1 couples du rédacteur (sans marqueur ; empreinte complète du rapport, contre-lecteur, R-2355, "
                  f"nom définitif cités) : {'sain, conforme' if ok else 'ÉCHEC'}")
    if not ok:
        raise Arret("essai B6-1 en échec")
    return sortie


def principal(argv: list[str]) -> int:
    a_blanc = None
    if len(argv) == 3 and argv[0] == "appliquer" and argv[1] == "--a-blanc":
        a_blanc, argv = Path(argv[2]), argv[:1]
    if argv not in (["essais"], ["appliquer"]):
        print(__doc__)
        return 2
    if not (Path(SCRIPT).is_file() and Path(B5).is_file()):
        print("ARRÊT : à lancer depuis la racine du dépôt")
        return 1
    try:
        m = module_b4()
        print(f"script du brouillon 4 : {SCRIPT_B4} — sha256 {ATTENDUS[SCRIPT_B4]} (égal à l'attendu et au compagnon)")
        for l in essais_b6(m):
            print(l)
        if argv == ["essais"]:
            return 0
        b5 = lire(B5)
        lire(CL2)
        lire(CL2_CONSIGNE)
        brut = lire(CL2_COUPLES)
        for c in (B5, CL2, CL2_CONSIGNE, CL2_COUPLES):
            print(f"entrée {c} : sha256 {ATTENDUS[c]} (égale à l'attendu et au compagnon)")
        jc = json.loads(brut.decode("utf-8"))
        if jc["de"] != {"chemin": B5, "sha256": ATTENDUS[B5]}:
            raise Arret("fichier des couples de la contre-lecture : brouillon source différent")
        ids = [c["id"] for c in jc["couples"]]
        if ids != ORDRE_CL2:
            raise Arret(f"couples de la contre-lecture : ordre ou identifiants inattendus {ids}")
        cl2 = [{"id": c["id"], "origine": "contre-lecture 2", "statut": c["statut"], "motif": c["motif"],
                "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in jc["couples"]]
        t5 = b5.decode("utf-8")
        t_cl2 = m.appliquer(t5, [(c["ancien"], c["nouveau"]) for c in cl2])
        h_cl2 = sha(t_cl2.encode("utf-8"))
        print(f"brouillon 5 + 14 couples de la contre-lecture : sha256 {h_cl2} ; = repère du contre-lecteur : "
              f"{h_cl2 == REPERE_CL2}")
        if h_cl2 != REPERE_CL2:
            raise Arret("texte différent du repère du contre-lecteur")
        restants_avant = sorted(set(MARQUEUR.findall(t_cl2)))
        print(f"marqueurs avant les couples du rédacteur : {restants_avant}")
        tous = cl2 + couples_redacteur()
        t6 = m.appliquer(t5, [(c["ancien"], c["nouveau"]) for c in tous])
        if m.defaire(t6, [(c["ancien"], c["nouveau"]) for c in tous]).encode("utf-8") != b5:
            raise Arret("défaire les seize couples ne redonne pas le brouillon 5 à l'octet")
        print(f"couples : {len(tous)} appliqués (14 de la contre-lecture, 2 du rédacteur), chacun une fois ; défaits du "
              "dernier au premier : brouillon 5 à l'octet")
        restants = sorted(set(MARQUEUR.findall(t6)))
        print(f"marqueurs restants : {restants if restants else 'aucun'}")
        if restants:
            raise Arret(f"marqueurs restants : {restants}")
        o_couples = (json.dumps({
            "de": {"chemin": B5, "sha256": ATTENDUS[B5]},
            "vers": {"chemin": B6, "sha256": sha(t6.encode("utf-8"))},
            "repere_contre_lecture": {"apres_les_14_couples": REPERE_CL2, "source": {"chemin": CL2_COUPLES,
                                                                                   "sha256": ATTENDUS[CL2_COUPLES]}},
            "regle": "appliqués dans l'ordre (14 de la contre-lecture, tels quels, puis 2 du rédacteur), chaque « ancien » "
                     "présent une fois au moment de son remplacement ; défaits du dernier au premier, ils redonnent le "
                     "brouillon 5 à l'octet",
            "couples": tous,
        }, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        c6, cc = B6, FICHIER_COUPLES
        if a_blanc is not None:
            print(f"À BLANC : sorties écrites sous {a_blanc}, aucune sous {DOSSIER}")
            c6, cc = str(a_blanc / Path(B6).name), str(a_blanc / Path(FICHIER_COUPLES).name)
        print(f"brouillon 6 : {c6} — {m.ecrire_sans_ecraser(c6, t6.encode('utf-8'))} — sha256 {sha(t6.encode('utf-8'))}")
        print(f"couples : {cc} — {m.ecrire_sans_ecraser(cc, o_couples)} — sha256 {sha(o_couples)}")
        return 0
    except Exception as e:  # Arret de ce script ou du script du brouillon 4
        if type(e).__name__ != "Arret":
            raise
        print(f"ARRÊT : {e}")
        return 1


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
