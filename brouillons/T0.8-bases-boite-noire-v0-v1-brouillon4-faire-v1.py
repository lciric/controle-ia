#!/usr/bin/env python3
"""T0.8, bases boîte noire v0 — fabrication du brouillon 4 (v1).

Écrit par le rédacteur des brouillons 2 et 3 (même consigne, `ea0e5136…` ; décisions de la session
mère R-2250). Trois étapes, et rien d'autre :

1. vérifier les empreintes des entrées (brouillon 3, vérification courte du différentiel du
   brouillon 2 au brouillon 3) ; toute différence arrête (R11) ;
2. extraire du rapport les 11 couples VT3C-01 à VT3C-11, tels qu'écrits, et les appliquer au
   brouillon 3 dans l'ordre : chaque texte ancien une seule fois dans le brouillon 3 et une seule
   fois au moment de son application ; empreinte après eux seuls égale à celle du rapport
   (`350c2056…`) ;
3. appliquer les seuls couples déclarés que permet R-2250 : en-tête (titre, statut « brouillon 4 »)
   et date de fixation (R4-01 à R4-04), chacun trouvé une seule fois.

Écrit le brouillon 4 et le JSON des couples sous des noms neufs ; refuse d'écraser (R12).
Aucun réseau, aucun modèle, aucune écriture git.

Usage : python3 -I T0.8-bases-boite-noire-v0-v1-brouillon4-faire-v1.py --depot DEPOT \
            --brouillon4 SORTIE.md --couples SORTIE.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ENTREES = {
    "brouillon3": ("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon3.md",
                   "947994e4487d2d2b01b7e8e01d5fb17f75c178b846aea5546b4bd8da78effdc1"),
    "verification_courte_b3": ("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon3-verification-courte-v1.md",
                               "ced3b43eb21dd201c09fa912d9855295b048d3bdb015fd0a09269458b0d1809e"),
}
EMPREINTE_APRES_VT3C = "350c20566f6547379062c3386295e3e0db919d6320ab4ff4b1072accb91c76f7"  # rapport, l. 12
NOMBRE_VT3C = 11
SECTIONS_GELEES = (
    "Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Plan d'analyse",
    "Critères de lecture gelés", "Liste d'arrêt",
)
MARQUEURS_ATTENDUS = sorted([
    "<<COMMIT_CODE_T08>>", "<<CODE_MOTS_ET_COUT_T06>>", "<<RUN_7B>>", "<<EMPREINTES_ENTREES_7B>>",
    "<<ENTROPIE_T08>>", "<<GO_T08>>", "<<LIGNE_DEPENSE_T08>>",
])
B4 = "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4"

R4 = [
    {"id": "R4-01", "objet": "en-tête : titre, brouillon 4",
     "ancien": r"""par renvoi au texte scellé à part) — v1 — brouillon 3""",
     "nouveau": r"""par renvoi au texte scellé à part) — v1 — brouillon 4"""},

    {"id": "R4-02", "objet": "en-tête : statut « brouillon 4 »",
     "ancien": r"""- **Statut** : **brouillon 3**, **non scellé** ; il ne vaut pas préenregistrement (R1).""",
     "nouveau": r"""- **Statut** : **brouillon 4**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 4 applique par programme, tels qu'écrits, les 11 couples VT3C-01 à VT3C-11 de la vérification courte du différentiel du brouillon 2 au brouillon 3 (Fable 5.2, « gelable après corrections » ; `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon3-verification-courte-v1.md`, `ced3b43eb21dd201c09fa912d9855295b048d3bdb015fd0a09269458b0d1809e`) ; décisions de la session mère R-2250 (VT3-05 : l'arrêt neuf est borné à la lecture descriptive des épisodes de la pièce HD ; aucune ligne de la table D ne change) ; écrit le 2026-11-10 à partir de 14:55 UTC par le rédacteur des brouillons 2 et 3 ; script `""" + B4 + r"""-faire-v1.py`, couples `""" + B4 + r"""-couples-v1.json`, journal `""" + B4 + r"""-journal-v1.md` ; brouillon 3 (`947994e4487d2d2b01b7e8e01d5fb17f75c178b846aea5546b4bd8da78effdc1`) gardé intact (R12). Ce qui suit dans cet en-tête décrit le brouillon 3, inchangé au brouillon 4 :"""},

    {"id": "R4-03", "objet": "date de fixation (Ce que les auteurs savaient, règle pour la suite) : brouillon 4",
     "ancien": r"""au brouillon 3, le 10 novembre 2026, avant l'existence de 7b et de toute sortie de la pièce HD.""",
     "nouveau": r"""au brouillon 3, et, par les couples de la vérification courte du différentiel (VT3C-01 à VT3C-11), au brouillon 4, le 10 novembre 2026, avant l'existence de 7b et de toute sortie de la pièce HD."""},

    {"id": "R4-04", "objet": "date de fixation (Seuil) : brouillon 4",
     "ancien": r"""au brouillon 3, le 10 novembre 2026, avant l'existence de 7b ; aucun n'a été choisi en regardant une donnée.""",
     "nouveau": r"""au brouillon 3, ou, par les couples de la vérification courte du différentiel (VT3C-01 à VT3C-11), au brouillon 4, le 10 novembre 2026, avant l'existence de 7b ; aucun n'a été choisi en regardant une donnée."""},
]


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def arret(message: str) -> None:
    sys.exit(f"ARRÊT : {message}")


def section_de(texte: str, position: int) -> str:
    titres = list(re.finditer(r"^## +(.+?)\s*$", texte[:position], flags=re.M))
    return titres[-1].group(1).strip() if titres else "(en-tête)"


def une_fois(texte: str, morceau: str, quoi: str) -> int:
    n = texte.count(morceau)
    if n != 1:
        arret(f"{quoi} : trouvé {n} fois (une seule attendue)")
    return texte.index(morceau)


def extraire(texte: str) -> list[dict]:
    blocs = re.split(r"^### (VT3C-\d\d) — (.*)$", texte, flags=re.M)
    couples = []
    for i in range(1, len(blocs), 3):
        ident, titre, corps = blocs[i], blocs[i + 1], blocs[i + 2]
        m = re.search(r"Texte actuel :\n\n```\n(.*?)\n```\n\nTexte corrigé :\n\n```\n(.*?)\n```\n", corps, flags=re.S)
        if not m:
            arret(f"{ident} : forme inattendue dans le rapport")
        couples.append({"id": ident, "titre": titre.strip(), "ancien": m.group(1), "nouveau": m.group(2)})
    if [c["id"] for c in couples] != [f"VT3C-{k:02d}" for k in range(1, NOMBRE_VT3C + 1)]:
        arret("les couples extraits ne sont pas exactement VT3C-01 à VT3C-11, dans l'ordre")
    return couples


def appliquer(texte: str, c: dict) -> tuple[str, dict]:
    pos = une_fois(texte, c["ancien"], c["id"])
    section = section_de(texte, pos)
    texte = texte[:pos] + c["nouveau"] + texte[pos + len(c["ancien"]):]
    return texte, {"id": c["id"], "objet": c.get("objet", c.get("titre")), "section": section,
                   "section_gelee": section in SECTIONS_GELEES, "ancien": c["ancien"], "nouveau": c["nouveau"]}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--depot", required=True)
    p.add_argument("--brouillon4", required=True)
    p.add_argument("--couples", required=True)
    a = p.parse_args()
    depot = Path(a.depot)
    sortie_b4, sortie_json = Path(a.brouillon4), Path(a.couples)
    for s in (sortie_b4, sortie_json):
        if s.exists():
            arret(f"{s} existe déjà : on n'écrase jamais (R12)")
    lus = {}
    for nom, (chemin, attendu) in ENTREES.items():
        octets = (depot / chemin).read_bytes()
        if sha(octets) != attendu:
            arret(f"empreinte de {chemin} : {sha(octets)} au lieu de {attendu} (R11)")
        lus[nom] = octets.decode("utf-8")

    b3 = lus["brouillon3"]
    texte = b3
    vt3c = []
    for c in extraire(lus["verification_courte_b3"]):
        une_fois(b3, c["ancien"], f"{c['id']} dans le brouillon 3")
        texte, trace = appliquer(texte, c)
        vt3c.append(trace)
    apres = sha(texte.encode("utf-8"))
    if apres != EMPREINTE_APRES_VT3C:
        arret(f"empreinte après les 11 couples VT3C : {apres} au lieu de {EMPREINTE_APRES_VT3C}")

    declares = []
    for c in R4:
        texte, trace = appliquer(texte, c)
        declares.append(trace)

    marqueurs = re.findall(r"<<[A-Z0-9_]+>>", texte)
    if sorted(marqueurs) != MARQUEURS_ATTENDUS:
        arret(f"marqueurs restants inattendus : {sorted(marqueurs)}")
    final = texte.encode("utf-8")
    sortie_b4.write_bytes(final)
    sortie_json.write_text(json.dumps({
        "objet": "T0.8 bases boîte noire v0, brouillon 4 : couples VT3C et couples déclarés R4 (v1)",
        "entrees": {nom: {"chemin": ch, "sha256": em} for nom, (ch, em) in ENTREES.items()},
        "sections_gelees": list(SECTIONS_GELEES),
        "couples_verification_courte_b3": vt3c,
        "sha256_apres_11_couples_vt3c": apres,
        "couples_declares_redacteur": declares,
        "marqueurs_restants": sorted(marqueurs),
        "sortie": {"chemin": sortie_b4.name, "sha256": sha(final)},
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"couples VT3C appliqués : {len(vt3c)} ; empreinte après eux : {apres}")
    print(f"couples déclarés appliqués : {len(declares)}")
    for t in vt3c + declares:
        print(f"  {t['id']} | {t['section']} | gelée={t['section_gelee']}")
    print(f"marqueurs restants : {', '.join(sorted(marqueurs))}")
    print(f"brouillon 4 : {sortie_b4} ; sha256 {sha(final)}")


if __name__ == "__main__":
    main()
