"""Vérifications communes de la chaîne du premier test boîte blanche sur l'organisme (i-a) (P3, R-192, R-202), v1,
brouillon 3 (relecture courte traitée : RCh-01 à RCh-03, RCh-07 ; RT-01) : un seul texte, lu à l'identique par le
scellement, par les contrôles avant dépense et par le lanceur.
Décliné de `verifications_notations_v1.py` (notations refaites du pilote de T0.5). Bibliothèque standard seulement
(lancé par python3 -I, hors du dépôt).

  verifications_p3_v1.py go PREREG GO_MD DECISIONS_MD
      GO de calcul et décision de Lazar : une seule ligne « - GO de calcul et décision de Lazar : `GO-…` (R-…) » dans le
      texte ; le GO cité est GO-2026-10-04-08, le seul accepté (contre-lecture de la chaîne, CH-02), et la décision citée
      R-192, la seule acceptée (les formes de révocation sont fixées pour elle) ; une seule ligne de ce GO au registre des
      GO, à huit colonnes, de type « calcul », accordée par Lazar ; une seule ligne R-192 au registre des décisions, qui
      cite « (b) P1 + P2 + P3 + pilote du papier C ». Révocation (relecture courte, RCh-01, RCh-02, RT-01 : formes
      exactes, aucune recherche en texte libre), et rien d'autre : (a) une ligne du registre des GO, à huit colonnes, de
      type « révocation », dont le périmètre nomme R-192 ou GO-2026-10-04-08 ; (b) une ligne du registre des décisions
      dont la cellule de décision commence exactement par « **Révocation de R-192** ». Écrit « GO-… (R-…) conforme ».
  verifications_p3_v1.py accord R-… DECISIONS_MD JOUR
      Accord de Lazar pour l'appel payant (R-185 ; CH-11) : une seule ligne « | R-… | » au registre des décisions, datée
      JOUR (jour UTC de l'appel, AAAA-MM-JJ), dont la cellule de décision commence exactement par « **Accord de Lazar
      pour le lancement de P3** » (forme exacte : relecture courte, RCh-03). Écrit « R-… : accord de Lazar du JOUR pour
      le lancement de P3 : conforme ».
  verifications_p3_v1.py repetition CODE_RELU JOURNAL CANDIDAT_NOM CANDIDAT_SHA CONSIGNES_NOM CONSIGNES_SHA
      journal de la répétition jouet : commit du code répété, candidat répété et consignes répétées (nom de base et
      empreinte des pièces relues épinglées ; CH-15), fin, trois passages à leur code, quatre récupérations conformes
      (run complet ; arrêt pendant les épisodes, synthétique ; gardes 0, 3f et 6b dans leur forme réelle sur des pièces
      factices, CH-07 ; texte d'action dégénéré, un seul caractère répété, RCh-07) et une récupération des traces seules
      (code 4), sans KO dans leur bloc, dix-huit artefacts refusés chacun
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
DECISION = "R-192"                      # seule décision acceptée : les formes de révocation sont fixées pour elle
# la décision citée contient « P3 » : la sous-condition « P3 » du brouillon 1 était redondante (CH-14), retirée
DECISION_CITEE = "(b) P1 + P2 + P3 + pilote du papier C"
# formes exactes, citées mot pour mot par le texte et relues par le bloc 9 des contrôles (relecture courte : RCh-01 à
# RCh-03, RT-01) ; aucune recherche en texte libre
PREFIXE_REVOCATION = "**Révocation de R-192**"
PREFIXE_ACCORD = "**Accord de Lazar pour le lancement de P3**"
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
    if reg != DECISION:
        raise SystemExit(f"{reg} : seule la décision {DECISION} est acceptée pour P3 (formes de révocation fixées pour elle)")
    lignes = go_t.split("\n")
    c = [cellules(x) for x in lignes if x.startswith(f"| {g} |")]
    if len(c) != 1 or len(c[0]) != 8:
        raise SystemExit(f"{g} absent, en double ou mal formé")
    if c[0][2] != "calcul" or c[0][6] != "Lazar":
        raise SystemExit(f"{g} : {c[0][2]}, {c[0][6]} : GO de type « calcul », accordé par Lazar, attendu")
    # révocation, forme (a) : ligne du registre des GO, à huit colonnes, de type « révocation », dont le périmètre
    # (quatrième colonne) nomme R-192 ou GO-2026-10-04-08 (identifiants entiers)
    for ligne in lignes:
        if not ligne.startswith("| GO-"):
            continue
        k = cellules(ligne)
        if len(k) != 8 or k[2] != "révocation":
            continue
        noms = set(re.findall(rf"(?<![\w-])(?:{MOTIF_GO}|R-\d{{3,4}})(?![\w-])", k[3]))
        if g in noms:
            raise SystemExit(f"{g} révoqué au registre des GO ({k[0]})")
        if reg in noms:
            raise SystemExit(f"décision {reg} révoquée au registre des GO ({k[0]})")
    dec = dec_t.split("\n")
    r = [x for x in dec if x.startswith(f"| {reg} |")]
    if len(r) != 1 or DECISION_CITEE not in r[0]:
        raise SystemExit(f"{reg} absent, en double, ou sans la décision de Lazar « {DECISION_CITEE} »")
    # révocation, forme (b) : ligne du registre des décisions dont la cellule de décision commence exactement par le
    # préfixe ; rien d'autre (une ligne qui décrit les formes, comme R-215, ou dit « aucune révocation », n'en est pas une)
    for x in dec:
        if not x.startswith("| R-"):
            continue
        k = cellules(x)
        if len(k) >= 3 and k[2].startswith(PREFIXE_REVOCATION):
            raise SystemExit(f"décision {reg} révoquée par {k[0]} (registre des décisions, « {PREFIXE_REVOCATION} »)")
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
    # forme exacte (relecture courte, RCh-03) : une ligne du jour qui mentionne l'accord sans l'être (R-208, R-215,
    # R-217) ne passe pas
    if not c[2].startswith(PREFIXE_ACCORD):
        raise SystemExit(f"accord {reg} : la cellule de décision ne commence pas par « {PREFIXE_ACCORD} »")
    return f"{reg} : accord de Lazar du {jour} pour le lancement de P3 : conforme"


PASSAGES = ("passage 1-sain : code 0 ", "passage 2-artefact-branche-presente : code 2 ",
            "passage 3-manque : code 1 ")
CONFORMES = ("récupération (passage-1-sain) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (arret-synthetique-episodes) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (gardes-reelles) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
             "récupération (texte-degenere-repete) : code 0 ; RÉCUPÉRATION : TOUS CONFORMES",
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
    ("artefact-texte-echappe-dans-un-resultat", "4f"),
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
    if sum("RÉCUPÉRATION : TOUS CONFORMES" in x for x in lignes) != 4 or sum("TOUS CONFORMES" in x for x in lignes) != 5:
        raise SystemExit("quatre récupérations conformes et une récupération des traces seules attendues")
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
