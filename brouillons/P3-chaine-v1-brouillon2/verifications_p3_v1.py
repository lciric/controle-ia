"""Vérifications communes de la chaîne du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202), v1,
brouillon 2 : un seul texte, lu à l'identique par le scellement, par les contrôles avant dépense et par le lanceur.
Décliné de `verifications_notations_v1.py` (notations refaites du pilote de T0.5). Bibliothèque standard seulement
(lancé par python3 -I, hors du dépôt).

  verifications_p3_v1.py go PREREG GO_MD DECISIONS_MD
      GO de calcul et décision de Lazar : une seule ligne « - GO de calcul et décision de Lazar : `GO-…` (R-…) » dans le
      texte ; le GO cité est GO-2026-10-04-08, le seul accepté (contre-lecture de la chaîne, CH-02) ; une seule ligne de
      ce GO au registre des GO, à huit colonnes, de type « calcul », accordée par Lazar ; aucune ligne « révocation » du
      registre des GO qui nomme ce GO, ni qui nomme la décision citée sans nommer d'autre GO (CH-09) ; une seule ligne
      R-… au registre des décisions, qui cite « (b) P1 + P2 + P3 + pilote du papier C » ; aucune autre ligne de ce
      registre qui la révoque, la retire ou l'annule (« révoque R-… », « R-… retirée », etc. ; CH-09). Écrit
      « GO-… (R-…) conforme ».
  verifications_p3_v1.py accord R-… DECISIONS_MD JOUR
      Accord de Lazar pour l'appel payant (R-185 ; CH-11) : une seule ligne « | R-… | » au registre des décisions, datée
      JOUR (jour UTC de l'appel, AAAA-MM-JJ), dont la colonne « décision » contient « accord de Lazar » (casse libre),
      « P3 » et « lancement » (casse libre). Écrit « R-… : accord de Lazar du JOUR pour le lancement de P3 : conforme ».
  verifications_p3_v1.py repetition CODE_RELU JOURNAL CANDIDAT_NOM CANDIDAT_SHA CONSIGNES_NOM CONSIGNES_SHA
      journal de la répétition jouet : commit du code répété, candidat répété et consignes répétées (nom de base et
      empreinte des pièces relues épinglées ; CH-15), fin, trois passages à leur code, trois récupérations conformes (run
      complet ; arrêt pendant les épisodes, synthétique ; gardes 0, 3f et 6b dans leur forme réelle sur des pièces
      factices, CH-07) et une récupération des traces seules (code 4), sans KO dans leur bloc, artefacts refusés chacun
      par un seul KO, au préfixe attendu, dans le seul bloc indenté qui suit sa ligne ; deux lignes « script répété »
      exactement, bien formées, sans doublon. Écrit une ligne « <script> <sha256> » par script répété.
  verifications_p3_v1.py preuves DOSSIER [JOURNAL …]
      journaux des bancs et de la répétition finale (tous les cinq si aucun n'est nommé ; la copie du scellement jouée par
      la répétition finale n'en nomme que trois, CH-03) : chacun présent dans DOSSIER, à son verdict conforme sur sa
      dernière ligne, sans aucune ligne d'échec (« NON CONFORME », trace d'exception, jeton affiché), avec ses lignes
      « script éprouvé : <script> <sha256> » bien formées et exactement les scripts qu'il éprouve ; une même empreinte
      pour un script éprouvé par plusieurs journaux. Écrit une ligne « <script> <sha256> » par script éprouvé ;
      l'appelant les compare aux copies versées.
Code 0 si conforme ; code 1 avec un message sur la dernière ligne sinon ; code 2 sur un usage faux.
"""
from __future__ import annotations

import re
import sys

GO_CALCUL = "GO-2026-10-04-08"          # seul GO accepté pour P3 (devis de la phase 0, R-192 ; CH-02)
# la décision citée contient « P3 » : la sous-condition « P3 » du brouillon 1 était redondante (CH-14), retirée
DECISION_CITEE = "(b) P1 + P2 + P3 + pilote du papier C"
VERBES_REVOCATION = r"(?:révoqu\w*|révocation|retir\w*|annul\w*)"
MOTIF_GO = r"GO-\d{4}-\d{2}-\d{2}-\d{2}"


def lire(chemin: str) -> str:
    try:
        return open(chemin, encoding="utf-8").read()
    except OSError:
        raise SystemExit(f"fichier {chemin} absent ou illisible") from None


def cellules(ligne: str) -> list[str]:
    return [x.strip() for x in ligne.strip().strip("|").split("|")]


def go(prereg: str, go_md: str, dec_md: str) -> str:
    texte, go_t, dec_t = lire(prereg), lire(go_md), lire(dec_md)
    m = re.findall(rf"^- GO de calcul et décision de Lazar : `({MOTIF_GO})` \((R-\d{{3,4}})\)", texte, re.M)
    if len(m) != 1 or len(re.findall(r"^- GO de calcul et décision de Lazar :", texte, re.M)) != 1:
        raise SystemExit("ligne « GO de calcul et décision de Lazar » absente, en double ou mal formée")
    g, reg = m[0]
    if g != GO_CALCUL:
        raise SystemExit(f"{g} : seul {GO_CALCUL} est accepté pour P3 (GO de calcul de la phase 0, R-192)")
    lignes = go_t.split("\n")
    c = [cellules(x) for x in lignes if x.startswith(f"| {g} |")]
    if len(c) != 1 or len(c[0]) != 8:
        raise SystemExit(f"{g} absent, en double ou mal formé")
    if c[0][2] != "calcul" or c[0][6] != "Lazar":
        raise SystemExit(f"{g} : {c[0][2]}, {c[0][6]} : GO de type « calcul », accordé par Lazar, attendu")
    for ligne in lignes:
        if not ligne.startswith("| GO-"):
            continue
        k = cellules(ligne)
        bien_formee = len(k) == 8
        if not (k[2].lower() == "révocation" if bien_formee else "révocation" in ligne.lower()):
            continue
        texte_r = " ".join(k[3:]) if bien_formee else ligne
        autres_go = set(re.findall(MOTIF_GO, texte_r)) - {k[0], g}
        if g in texte_r:
            raise SystemExit(f"{g} révoqué")
        if re.search(rf"\b{re.escape(reg)}\b", texte_r) and not autres_go:
            raise SystemExit(f"décision {reg} révoquée au registre des GO ({k[0]})")
    dec = dec_t.split("\n")
    r = [x for x in dec if x.startswith(f"| {reg} |")]
    if len(r) != 1 or DECISION_CITEE not in r[0]:
        raise SystemExit(f"{reg} absent, en double, ou sans la décision de Lazar « {DECISION_CITEE} »")
    motif = re.compile(rf"{VERBES_REVOCATION}\s+(?:de\s+)?(?:la\s+)?(?:décision\s+)?{re.escape(reg)}\b"
                       rf"|\b{re.escape(reg)}\s+(?:est\s+)?{VERBES_REVOCATION}", re.I)
    for x in dec:
        if x.startswith("| R-") and not x.startswith(f"| {reg} |") and motif.search(x):
            raise SystemExit(f"décision {reg} révoquée, retirée ou annulée par {cellules(x)[0]} (registre des décisions)")
    return f"{g} ({reg}) conforme"


def accord(reg: str, dec_md: str, jour: str) -> str:
    if not re.fullmatch(r"R-\d{3,4}", reg):
        raise SystemExit(f"identifiant de l'accord « {reg[:20]} » mal formé : R-… attendu")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", jour):
        raise SystemExit(f"jour « {jour[:20]} » mal formé : AAAA-MM-JJ attendu")
    lignes = [x for x in lire(dec_md).split("\n") if x.startswith(f"| {reg} |")]
    if len(lignes) != 1:
        raise SystemExit(f"accord {reg} absent ou en double au registre des décisions")
    c = cellules(lignes[0])
    if len(c) < 3 or c[1] != jour:
        raise SystemExit(f"accord {reg} daté {c[1] if len(c) > 1 else '?'} : accord du jour de l'appel ({jour}) attendu")
    manquants = [m for m, present in (("accord de Lazar", "accord de lazar" in c[2].lower()), ("P3", "P3" in c[2]),
                                      ("lancement", "lancement" in c[2].lower())) if not present]
    if manquants:
        raise SystemExit(f"accord {reg} : la décision ne contient pas {', '.join(f'« {x} »' for x in manquants)}")
    return f"{reg} : accord de Lazar du {jour} pour le lancement de P3 : conforme"


PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ",
            "passage 3-manque : code 1 ")
CONFORMES = ("récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (arret-synthetique-episodes) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (gardes-reelles) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (passage-3-traces-seules) : code 4 ; RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES")
_KO1 = " : code 1 ; RÉCUPÉRATION : 1 CONTRÔLE(S) EN ÉCHEC"
ARTEFACTS = {f"récupération ({nom}){_KO1}": f"    KO  {prefixe} " for nom, prefixe in (
    ("artefact-scores-manquants", "4c"),
    ("artefact-donnee-orpheline", "4c"),
    ("artefact-ajout-hors-perimetre", "1c"),
    ("artefact-scores-alteres", "2b"),
    ("artefact-sceau-des-scores-faux", "2b"),
    ("artefact-resultat-autre-manifeste", "2b"),
    ("artefact-scores-hors-plan", "4d"),
    ("artefact-textes-incomplets", "4e"),
    ("artefact-texte-hors-du-fichier-des-textes", "4f"),
    ("artefact-sondes-figees-incompletes", "5"),
    ("artefact-figees-apres-episodes", "6d"),
    ("artefact-figees-apres-premier-episode", "6e"),
    ("artefact-lot-manquant", "6f"),
    ("artefact-jeton-dans-une-trace", "7"),
    ("artefact-copie-non-versee", "0"),
    ("artefact-versions-autres", "3f"),
    ("artefact-carte-autre", "6b"))}
SCRIPTS = {"recuperation_p3_v1.sh", "repetition_jouet_p3_v1.sh"}


def bloc_indente(lignes: list[str], i: int) -> list[str]:
    """Lignes indentées (quatre espaces) qui suivent immédiatement la ligne i : le bloc de cette récupération."""
    j = i + 1
    while j < len(lignes) and lignes[j].startswith("    "):
        j += 1
    return lignes[i + 1:j]


def repetition(code: str, journal: str, nom: str, sha: str, nom_c: str, sha_c: str) -> list[str]:
    lignes = lire(journal).split("\n")
    exigees = [f"commit du code répété : {code}", f"candidat répété : {nom} {sha}", f"consignes répétées : {nom_c} {sha_c}",
               "FIN DE LA RÉPÉTITION", *CONFORMES, *ARTEFACTS]
    for e in exigees:
        if lignes.count(e) != 1:
            raise SystemExit(f"ligne absente ou en double : {e}")
    for prefixe in ("candidat répété : ", "consignes répétées : "):
        if sum(x.startswith(prefixe) for x in lignes) != 1:
            raise SystemExit(f"plusieurs lignes « {prefixe.strip(' :')} »")
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
            m = re.fullmatch(r"script répété : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
            if not m:
                raise SystemExit(f"ligne « script répété » mal formée : {x[:90]}")
            if m.group(1) in scripts:
                raise SystemExit(f"script répété en double : {m.group(1)}")
            scripts[m.group(1)] = m.group(2)
    if set(scripts) != SCRIPTS:
        raise SystemExit(f"scripts répétés {sorted(scripts)} : les deux attendus exactement")
    return [f"{s} {scripts[s]}" for s in sorted(scripts)]


# journal → (verdict de sa dernière ligne, scripts qu'il éprouve exactement)
JOURNAUX = {
    "banc-lanceur-p3-v1.log": ("FIN DU BANC DU LANCEUR DE P3 ; cas non conformes : 0",
                               {"lancer_p3_v1.sh", "verifications_p3_v1.py", "essais_lanceur_p3_v1.sh"}),
    "banc-surveillance-p3-v1.log": ("FIN DU BANC DE LA SURVEILLANCE DE P3 ; cas non conformes : 0",
                                    {"surveiller_p3_v1.sh", "controle_cinq_minutes_p3_v1.sh", "essais_surveillance_p3_v1.sh"}),
    "banc-controles-p3-v1.log": ("FIN DU BANC DES CONTRÔLES DE P3 ; cas non conformes : 0",
                                 {"controles_avant_depense_p3_v1.sh", "verifications_p3_v1.py", "essais_controles_p3_v1.sh"}),
    "banc-scellement-p3-v1.log": ("FIN DU BANC DU SCELLEMENT DE P3 ; cas non conformes : 0",
                                  {"sceller_p3_v1.sh", "verifications_p3_v1.py", "essais_scellement_p3_v1.sh"}),
    "repetition-finale-p3-v1.log": ("RÉPÉTITION FINALE : CONFORME",
                                    {"sceller_p3_v1.sh", "controles_avant_depense_p3_v1.sh", "verifications_p3_v1.py",
                                     "repetition_finale_p3_v1.sh"}),
}


def preuves(dossier: str, noms: list[str]) -> list[str]:
    noms = noms or list(JOURNAUX)
    inconnus = [n for n in noms if n not in JOURNAUX]
    if inconnus or len(set(noms)) != len(noms):
        raise SystemExit(f"journaux nommés inconnus ou en double : {noms}")
    vus: dict[str, str] = {}
    for nom in noms:
        verdict, attendus = JOURNAUX[nom]
        try:
            lignes = open(f"{dossier}/{nom}", encoding="utf-8").read().split("\n")
        except OSError:
            raise SystemExit(f"journal {nom} absent ou illisible") from None
        non_vides = [x for x in lignes if x.strip()]
        if not non_vides or non_vides[-1] != verdict:
            raise SystemExit(f"journal {nom} : dernière ligne ≠ « {verdict} »")
        fautes = [x for x in lignes if "NON CONFORME" in x or x.lstrip().startswith(("Traceback", "JETON AFFICHÉ"))]
        if fautes:
            raise SystemExit(f"journal {nom} : ligne d'échec avant le verdict : {fautes[0].strip()[:90]}")
        propres = set()
        for x in lignes:
            if x.startswith("script éprouvé : "):
                m = re.fullmatch(r"script éprouvé : ([a-z0-9_]+_v1\.(?:py|sh)) ([0-9a-f]{64})", x)
                if not m:
                    raise SystemExit(f"journal {nom} : ligne « script éprouvé » mal formée : {x[:90]}")
                if vus.setdefault(m.group(1), m.group(2)) != m.group(2):
                    raise SystemExit(f"{m.group(1)} éprouvé sous deux empreintes")
                propres.add(m.group(1))
        if not propres:
            raise SystemExit(f"journal {nom} : aucune ligne « script éprouvé »")
        if propres != attendus:
            raise SystemExit(f"journal {nom} : scripts éprouvés ≠ attendus (manquants {sorted(attendus - propres)}, "
                             f"en trop {sorted(propres - attendus)})")
    return [f"{s} {vus[s]}" for s in sorted(vus)]


def main(argv: list[str]) -> int:
    if len(argv) == 5 and argv[1] == "go":
        print(go(*argv[2:5]))
    elif len(argv) == 5 and argv[1] == "accord":
        print(accord(*argv[2:5]))
    elif len(argv) == 8 and argv[1] == "repetition":
        print("\n".join(repetition(*argv[2:8])))
    elif len(argv) >= 3 and argv[1] == "preuves":
        print("\n".join(preuves(argv[2], argv[3:])))
    else:
        print("usage : go PREREG GO_MD DECISIONS_MD | accord R-… DECISIONS_MD JOUR | repetition CODE JOURNAL NOM SHA "
              "NOM_CONSIGNES SHA_CONSIGNES | preuves DOSSIER [JOURNAL …]", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
