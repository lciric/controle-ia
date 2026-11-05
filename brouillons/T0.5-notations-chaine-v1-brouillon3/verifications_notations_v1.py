"""Vérifications communes de la chaîne des notations refaites du pilote de T0.5 (N-021, option (a)), v1 : un seul
texte, lu à l'identique par le scellement et par les contrôles avant dépense (contre-lecture R2 de la chaîne : les deux
copies d'un même bloc avaient dérivé). Bibliothèque standard seulement (lancé par python3 -I, hors du dépôt).

  verifications_notations_v1.py go PREREG GO_MD DECISIONS_MD
      décision de Lazar sur N-021 : une seule ligne « - Décision de Lazar sur N-021 : `GO-…` (R-…) » dans le texte ;
      GO de type « revendication », accordé par Lazar, qui cite N-021 et l'option (a) ; ni lui ni GO-2026-10-04-08
      révoqués (ligne « révocation » qui les nomme) ; colonne d'état de N-021 exactement « tranché (a) par Lazar :
      GO (R-…) » ; une seule ligne R-…, qui cite le GO. Écrit « GO-… (R-…) conforme ».
  verifications_notations_v1.py repetition CODE_RELU JOURNAL CANDIDAT_NOM CANDIDAT_SHA
      journal de la répétition jouet : commit du code répété, candidat répété (nom de base et empreinte du candidat
      relu épinglé), fin, quatre passages à leur code, trois récupérations conformes (premier lancement, relance,
      arrêt synthétique pendant le deuxième juge) et une récupération des traces seules (code 4), sans KO dans leur
      bloc, six artefacts refusés chacun par un seul KO, au préfixe attendu, dans le seul bloc indenté qui suit sa ligne ; trois lignes « script répété »
      exactement, bien formées, sans doublon. Écrit une ligne « <script> <sha256> » par script répété.
  verifications_notations_v1.py preuves DOSSIER
      journaux des bancs et de la répétition finale (contre-lecture R2 de la chaîne, critique de complétude, constat 2) :
      les cinq journaux attendus présents dans DOSSIER, chacun à son verdict conforme sur sa dernière ligne, avec ses
      lignes « script éprouvé : <script> <sha256> » bien formées ; une même empreinte pour un script éprouvé par plusieurs
      bancs ; les dix scripts attendus éprouvés, exactement. Écrit une ligne « <script> <sha256> » par script éprouvé ;
      l'appelant les compare aux copies versées à S.
  verifications_notations_v1.py statuts-v1 FICHIER…
      arrêts consignés sur la branche du premier lancement (relance) : chaque fichier doit être un résultat lisible
      ({"resultat": {"partiel": {"juges": …}}}) ; tout statut autre que « en cours » refuse le relancement (préséance :
      aucun juge fini). Écrit les statuts lus.
Code 0 si conforme ; code 1 avec un message sur la dernière ligne sinon ; code 2 sur un usage faux.
"""
from __future__ import annotations

import json
import re
import sys

GO_CALCUL = "GO-2026-10-04-08"


def cellules(ligne: str) -> list[str]:
    return [x.strip() for x in ligne.strip().strip("|").split("|")]


def go(prereg: str, go_md: str, dec_md: str) -> str:
    texte, go_t, dec_t = (open(f, encoding="utf-8").read() for f in (prereg, go_md, dec_md))
    m = re.findall(r"^- Décision de Lazar sur N-021 : `(GO-\d{4}-\d{2}-\d{2}-\d{2})` \((R-\d{3,4})\)", texte, re.M)
    if len(m) != 1 or len(re.findall(r"^- Décision de Lazar sur N-021 :", texte, re.M)) != 1:
        raise SystemExit("ligne « Décision de Lazar sur N-021 » absente, en double ou mal formée")
    g, reg = m[0]
    lignes = go_t.split("\n")
    c = [cellules(x) for x in lignes if x.startswith(f"| {g} |")]
    if len(c) != 1 or len(c[0]) != 8:
        raise SystemExit(f"{g} absent, en double ou mal formé")
    if c[0][2] != "revendication" or c[0][6] != "Lazar" or "N-021" not in c[0][3] or "(a)" not in c[0][3]:
        raise SystemExit(f"{g} : {c[0][2]}, {c[0][6]} : GO de type « revendication », accordé par Lazar, sur N-021 (a), attendu")
    for x in (g, GO_CALCUL):
        for ligne in lignes:
            if not ligne.startswith("| GO-"):
                continue
            k = cellules(ligne)
            if (len(k) == 8 and k[2].lower() == "révocation" and (x in k[3] or x in k[7])) or \
                    (len(k) != 8 and "révocation" in ligne.lower() and x in ligne):
                raise SystemExit(f"{x} révoqué")
    dec = dec_t.split("\n")
    n21 = [x for x in dec if x.startswith("| N-021 |")]
    if len(n21) != 1:
        raise SystemExit("N-021 absent ou en double")
    etat = n21[0].rsplit("|", 2)[-2].strip()
    if not re.fullmatch(rf"tranché \(a\) par Lazar : {re.escape(g)} \({re.escape(reg)}\)", etat):
        raise SystemExit(f"N-021 : colonne d'état ≠ « tranché (a) par Lazar : {g} ({reg}) »")
    r = [x for x in dec if x.startswith(f"| {reg} |")]
    if len(r) != 1 or g not in r[0]:
        raise SystemExit(f"{reg} absent, en double ou sans {g}")
    return f"{g} ({reg}) conforme"


PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ",
            "passage 3-premier-manque : code 1 ", "passage 4-relance : code 0 ")
CONFORMES = ("récupération (passage-1-premier) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (passage-4-relance) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (arret-synthetique-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (passage-3-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES")
ARTEFACTS = {"récupération (artefact-relance-apres-notations) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC": "    KO  0 ",
             "récupération (artefact-notations-manquantes) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC": "    KO  4c ",
             "récupération (artefact-ajout-dans-le-pilote) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC": "    KO  1c ",
             "récupération (artefact-fin-de-juge-absente) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC": "    KO  6 lignes de fin de juge ",
             "récupération (artefact-relance-apres-dernier-lot) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC": "    KO  0 ",
             "récupération (artefact-notations-d-un-autre-run) : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC": "    KO  2b "}
SCRIPTS = {"construire_pilote_jouet_v1.py", "recuperation_notations_v1.sh", "repetition_jouet_notations_v1.sh"}


def bloc_indente(lignes: list[str], i: int) -> list[str]:
    """Lignes indentées (quatre espaces) qui suivent immédiatement la ligne i : le bloc de cette récupération, sans
    déborder sur la suivante (contre-lecture R2 de la chaîne, constat bloquant)."""
    j = i + 1
    while j < len(lignes) and lignes[j].startswith("    "):
        j += 1
    return lignes[i + 1:j]


def repetition(code: str, journal: str, nom: str, sha: str) -> list[str]:
    lignes = open(journal, encoding="utf-8").read().split("\n")
    exigees = [f"commit du code répété : {code}", f"candidat répété : {nom} {sha}", "FIN DE LA RÉPÉTITION",
               *CONFORMES, *ARTEFACTS]
    for e in exigees:
        if lignes.count(e) != 1:
            raise SystemExit(f"ligne absente ou en double : {e}")
    if sum(x.startswith("candidat répété : ") for x in lignes) != 1:
        raise SystemExit("plusieurs lignes « candidat répété »")
    for p in PASSAGES:
        if sum(x.startswith(p) for x in lignes) != 1:
            raise SystemExit(f"passage : {p.strip()}")
    if sum("RÉCUPÉRATION : TOUS CONFORMES" in x for x in lignes) != 3 or sum("TOUS CONFORMES" in x for x in lignes) != 4:
        raise SystemExit("trois récupérations conformes et une récupération des traces seules attendues")
    for etiquette in CONFORMES:
        ko = [x for x in bloc_indente(lignes, lignes.index(etiquette)) if x.startswith("    KO")]
        if ko:
            raise SystemExit(f"{etiquette} : KO {ko}")
    for etiquette, prefixe in ARTEFACTS.items():
        ko = [x for x in bloc_indente(lignes, lignes.index(etiquette)) if x.startswith("    KO")]
        if len(ko) != 1 or not ko[0].startswith(prefixe):
            raise SystemExit(f"{etiquette} : KO {ko}")
    scripts = {}
    for x in lignes:
        if x.startswith("script répété : "):
            m = re.fullmatch(r"script répété : ([a-z_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
            if not m:
                raise SystemExit(f"ligne « script répété » mal formée : {x[:90]}")
            if m.group(1) in scripts:
                raise SystemExit(f"script répété en double : {m.group(1)}")
            scripts[m.group(1)] = m.group(2)
    if set(scripts) != SCRIPTS:
        raise SystemExit(f"scripts répétés {sorted(scripts)} : les trois attendus exactement")
    return [f"{s} {scripts[s]}" for s in sorted(scripts)]


JOURNAUX = {"banc-lanceur-notations-v1.log": "FIN DU BANC DU LANCEUR DES NOTATIONS ; cas non conformes : 0",
            "banc-surveillance-notations-v1.log": "FIN DU BANC DE LA SURVEILLANCE DES NOTATIONS ; cas non conformes : 0",
            "banc-controles-notations-v1.log": "FIN DU BANC DES CONTRÔLES DES NOTATIONS ; cas non conformes : 0",
            "banc-scellement-notations-v1.log": "FIN DU BANC DU SCELLEMENT DES NOTATIONS ; cas non conformes : 0",
            "repetition-finale-notations-v1.log": "RÉPÉTITION FINALE : CONFORME"}
EPROUVES = {"lancer_notations_v1.sh", "verifications_notations_v1.py", "controles_avant_depense_notations_v1.sh",
            "sceller_notations_v1.sh", "surveiller_notations_v1.sh", "repetition_finale_notations_v1.sh",
            "essais_lanceur_notations_v1.sh", "essais_controles_notations_v1.sh", "essais_scellement_notations_v1.sh",
            "essais_surveillance_notations_v1.sh"}


def preuves(dossier: str) -> list[str]:
    vus: dict[str, str] = {}
    for nom, verdict in JOURNAUX.items():
        try:
            lignes = open(f"{dossier}/{nom}", encoding="utf-8").read().split("\n")
        except OSError:
            raise SystemExit(f"journal {nom} absent ou illisible")
        non_vides = [x for x in lignes if x.strip()]
        if not non_vides or non_vides[-1] != verdict:
            raise SystemExit(f"journal {nom} : dernière ligne ≠ « {verdict} »")
        propres = 0
        for x in lignes:
            if x.startswith("script éprouvé : "):
                m = re.fullmatch(r"script éprouvé : ([a-z_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
                if not m:
                    raise SystemExit(f"journal {nom} : ligne « script éprouvé » mal formée : {x[:90]}")
                if vus.setdefault(m.group(1), m.group(2)) != m.group(2):
                    raise SystemExit(f"{m.group(1)} éprouvé sous deux empreintes")
                propres += 1
        if not propres:
            raise SystemExit(f"journal {nom} : aucune ligne « script éprouvé »")
    if set(vus) != EPROUVES:
        raise SystemExit(f"scripts éprouvés {sorted(vus)} ≠ les dix attendus (manquants {sorted(EPROUVES - set(vus))})")
    return [f"{s} {vus[s]}" for s in sorted(vus)]


def statuts_v1(fichiers: list[str]) -> str:
    vus = []
    for f in fichiers:
        try:
            juges = json.load(open(f, encoding="utf-8"))["resultat"]["partiel"]["juges"]
            vus += [j["statut"] for j in juges.values()]
        except Exception as e:                  # arrêt illisible : rien ne s'établit, pas de relancement
            raise SystemExit(f"arrêt illisible sur -v1 ({type(e).__name__}) : relancement interdit")
    fini = sorted(set(vus) - {"en cours"})
    if fini:
        raise SystemExit(f"arrêt consigné avec un juge fini ou de statut inconnu ({', '.join(fini)}) : relancement interdit")
    return "statuts : " + (", ".join(sorted(set(vus))) or "aucun juge")


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] == "go" and len(argv) == 5:
        print(go(*argv[2:5]))
    elif len(argv) >= 2 and argv[1] == "repetition" and len(argv) == 6:
        print("\n".join(repetition(*argv[2:6])))
    elif len(argv) == 3 and argv[1] == "preuves":
        print("\n".join(preuves(argv[2])))
    elif len(argv) >= 3 and argv[1] == "statuts-v1":
        print(statuts_v1(argv[2:]))
    else:
        print("usage : go PREREG GO_MD DECISIONS_MD | repetition CODE JOURNAL NOM SHA | preuves DOSSIER | statuts-v1 FICHIER…",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
