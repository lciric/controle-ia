"""Lecture, par T0.7, des écrits de P3-bis que la garde adaptée exige (brouillon 19 de T0.7, `07039ed2…`, section « Module »,
entrées, et section « Écrits exigés par P3-bis », (d) ; N-066, option 1 ; format recopié de P3-bis brouillon 8, `477f1f5d…`, plan,
point 8), v1. **Rien n'est jamais écrit** dans ces fichiers par T0.7.

1. **Journal des ouvertures de P3-bis** `registres/ouvertures-p3bis-v1.md` (`lire_journal_p3bis`) : registre vivant en ajout seul,
   sans compagnon ; absent → « aucune ouverture » (liste vide). En tête, exactement les deux lignes `ENTETE_JOURNAL` ; puis une
   ligne de six cellules par tentative : `clé` (`OUVERTURE-P3BIS` ou `REFUS-OUVERTURE-P3BIS` ; seules les premières sont des
   ouvertures), `date` (`AAAA-MM-JJTHH:MM:SSZ`, UTC), `mode` (`pleine`, `reduite`, `pleine-anticipee`), `appui`, `paquets`,
   `motif`. T0.7 vérifie la forme ligne à ligne : en-tête, six cellules, clé, date, mode, et **ordre des ouvertures** (la première
   `pleine`, `reduite` ou `pleine-anticipee` ; après `reduite`, seule `pleine` ou `pleine-anticipee` ; après `pleine` ou
   `pleine-anticipee`, aucune) ; forme fautive → `JournalFautif` (refus, code 2, nœud). `paquets` et `motif` ne sont pas lus
   (« Ce que T0.7 en lit » : clé, date, mode, et l'appui des lignes `reduite` et `pleine`, comparé aux lignes citées par
   `garde_adaptee_v1`). **D-3 (R-2103 ; essai de concordance `c867a1b2…`)** : le lecteur applique **en entier** le prédicat de
   format de l'écrivain (`premier_test_ia/ouverture_p3bis_v2.py`, `330915f6…`, `lire_ligne_journal` et `exiger_format_journal`,
   l. 691-750) : chaque ligne finie par un saut de ligne (fichier sans saut final → faute), aucune ligne vide, aucune espace en
   tête ni en fin (la ligne commence et finit par `|`), cellules `appui` (jetons `CLÉ=sha256` séparés par une espace, clés
   `SCORES-T07`, `SONDES-T07`, `GARDE-ADAPTEE-T07-P3BIS`, `RENDEZ-VOUS-P3BIS-N` ; forme du mode pour une ouverture), `paquets`
   (deux empreintes séparées par une espace ; `-` permis pour un refus) et `motif` (`-` pour une ouverture ; `code : texte`, code
   de la liste fermée, pour un refus) à leur forme ; le fichier vide reste refusé. L'interprétation tolérante du brouillon 19
   (« ligne vide ignorée ») est retirée. La règle « dates non décroissantes » (CT-11) reste telle quelle.
2. **Registre des préalables de P3-bis** `registres/prealables-p3bis-v1.md` (`lire_prealables`) : même format que
   `registres/scellements-v1.md` (quatre cellules, date au motif `DATE`, chemin relatif sans « .. », empreinte du fichier entier
   égale à son compagnon) ; T0.7 lit `GARDE-ADAPTEE-T07-P3BIS` (au plus une ligne) et `RENDEZ-VOUS-P3BIS-N` (numéros consécutifs
   depuis 1, dates strictement croissantes) ; les trois clés d'écrit `ECRIT-…-P3BIS` sont connues et non lues ; toute autre ligne
   à quatre cellules dont la deuxième est une date au format → refus (P3-bis b8 : « toute autre clé : refus de la garde ») ;
   lignes datées strictement avant l'instant d'ouverture, sceaux et compagnons vérifiés.
3. **Fichier de décision du rendez-vous** `docs/decisions/rendez-vous-P3-bis-vN.md` (`lire_decision`) : celui que cite la ligne
   `RENDEZ-VOUS-P3BIS-N` du même numéro, jamais un fichier pris par son nom ; scellé, compagnon égal ; exactement une ligne
   `Décision : maintenir|ouvrir|ouvrir pleinement` et une ligne `Date : AAAA-MM-JJTHH:MM:SSZ`.
"""
from __future__ import annotations

import re
from pathlib import Path

from . import registre_v1 as rg

JOURNAL_P3BIS = "registres/ouvertures-p3bis-v1.md"
PREALABLES_P3BIS = "registres/prealables-p3bis-v1.md"
ENTETE_JOURNAL = ("| clé | date | mode | appui | paquets | motif |", "|---|---|---|---|---|---|")
OUVERTURE_P3BIS, REFUS_OUVERTURE_P3BIS = "OUVERTURE-P3BIS", "REFUS-OUVERTURE-P3BIS"
CLES_JOURNAL = (OUVERTURE_P3BIS, REFUS_OUVERTURE_P3BIS)
PLEINE, REDUITE, PLEINE_ANTICIPEE = "pleine", "reduite", "pleine-anticipee"
MODES_P3BIS = (PLEINE, REDUITE, PLEINE_ANTICIPEE)
SUIVANTS_PERMIS = {None: (PLEINE, REDUITE, PLEINE_ANTICIPEE), REDUITE: (PLEINE, PLEINE_ANTICIPEE), PLEINE: (), PLEINE_ANTICIPEE: ()}
GARDE_ADAPTEE_T07_P3BIS = "GARDE-ADAPTEE-T07-P3BIS"
CLES_ECRITS_P3BIS = ("ECRIT-PERIMETRE-JEUX-P3BIS", "ECRIT-LANCEMENT-RELANCE-P3BIS", "ECRIT-ENGAGEMENT-ETAPE-A-P3BIS")
RENDEZ_VOUS = re.compile(r"RENDEZ-VOUS-P3BIS-([1-9][0-9]*)")      # même motif que l'écrivain (R-2103)
# --- prédicat de format de l'écrivain (`ouverture_p3bis_v2.py`, `330915f6…`, l. 168-175), recopié (D-3, R-2103)
MOTIFS_REFUS = ("registre-absent", "ligne-absente", "ligne-double", "ligne-mal-formee", "sceau-faux", "compagnon-absent",
                "date-posterieure", "cle-inconnue", "rendez-vous-non-consecutif", "rendez-vous-non-croissant",
                "ligne-apres-decision-finale", "ni-scores-ni-ouvrir", "decision-maintenir", "garde-adaptee-absente",
                "garde-adaptee-posterieure", "deja-ouverte", "paquet-faux")
JETON_APPUI = re.compile(r"([A-Z0-9]+(?:-[A-Z0-9]+)+)=([0-9a-f]{64})")
CLE_RDV_APPUI = re.compile(r"RENDEZ-VOUS-P3BIS-[1-9][0-9]*")
PAQUETS_CELLULE = re.compile(r"[0-9a-f]{64} [0-9a-f]{64}")
MOTIF_CELLULE = re.compile(r"([a-z]+(?:-[a-z]+)*) : (\S.*)")
FICHIER_DECISION = "docs/decisions/rendez-vous-P3-bis-v{n}.md"
PREREG_T07 = "prereg/T0.7-sondes-v0-v1.md"
MAINTENIR, OUVRIR, OUVRIR_PLEINEMENT = "maintenir", "ouvrir", "ouvrir pleinement"
DECISIONS = (MAINTENIR, OUVRIR, OUVRIR_PLEINEMENT)
LIGNE_DECISION = re.compile(r"Décision : (maintenir|ouvrir pleinement|ouvrir)\s*")
LIGNE_DATE = re.compile(r"Date : (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s*")


class JournalFautif(rg.RefusRegistre):
    """Journal des ouvertures de P3-bis hors de son format : refus, code 2, nœud (section « Écrits exigés par P3-bis », (d))."""


def _cellules(ligne: str) -> list[str] | None:
    """Cellules d'une ligne de table `| a | b | … |` (None si la ligne ne commence ou ne finit pas par `|`)."""
    s = ligne.strip()
    if len(s) < 2 or not (s.startswith("|") and s.endswith("|")):
        return None
    return [c.strip() for c in s[1:-1].split("|")]


def _forme_appui(mode: str, cles: list[str]) -> bool:
    if mode == PLEINE:
        return cles == [rg.SCORES_T07, rg.SONDES_T07]
    if mode == REDUITE:
        return len(cles) == 2 and bool(CLE_RDV_APPUI.fullmatch(cles[0])) and cles[1] == GARDE_ADAPTEE_T07_P3BIS
    return len(cles) == 1 and bool(CLE_RDV_APPUI.fullmatch(cles[0]))


def faute_de_cellules(cle: str, mode: str, appui: str, paquets: str, motif: str) -> str | None:
    """D-3 : cellules `appui`, `paquets`, `motif` au prédicat de l'écrivain (`lire_ligne_journal`, l. 691-719) ; rend la faute ou None."""
    cles = []
    if appui != "-":
        for jeton in appui.split(" "):
            m = JETON_APPUI.fullmatch(jeton)
            if m is None:
                return f"appui : jeton {jeton!r} (CLÉ=sha256 attendu)"
            if not (m.group(1) in (rg.SCORES_T07, rg.SONDES_T07, GARDE_ADAPTEE_T07_P3BIS) or CLE_RDV_APPUI.fullmatch(m.group(1))):
                return f"appui : clé {m.group(1)!r} inconnue"
            cles.append(m.group(1))
    if cle == OUVERTURE_P3BIS:
        if not _forme_appui(mode, cles):
            return f"appui {appui!r} hors de la forme du mode {mode}"
        if not PAQUETS_CELLULE.fullmatch(paquets):
            return f"paquets {paquets!r} (deux empreintes séparées par une espace attendues)"
        if motif != "-":
            return f"motif {motif!r} d'une ouverture (« - » attendu)"
        return None
    if paquets != "-" and not PAQUETS_CELLULE.fullmatch(paquets):
        return f"paquets {paquets!r} d'un refus (« - » ou deux empreintes attendus)"
    m = MOTIF_CELLULE.fullmatch(motif)
    if m is None or m.group(1) not in MOTIFS_REFUS:
        return f"motif {motif!r} (code de la liste fermée, « : », texte attendus)"
    return None


def lire_journal_p3bis(chemin: Path) -> list[dict]:
    """Lignes du journal, dans l'ordre du fichier : {numero (ligne du fichier, depuis 1), cle, date, instant, mode, appui, paquets,
    motif}. Absent → []. Forme fautive → `JournalFautif` (toutes les fautes relevées, jointes par « ; »)."""
    chemin = Path(chemin)
    if not chemin.exists():
        return []
    if not chemin.is_file():
        raise JournalFautif(f"journal de P3-bis {chemin} : pas un fichier")
    lignes = chemin.read_text(encoding="utf-8").split("\n")
    fautes, sortie = [], []
    if len(lignes) < 2 or lignes[0] != ENTETE_JOURNAL[0] or lignes[1] != ENTETE_JOURNAL[1]:
        raise JournalFautif(f"journal de P3-bis {chemin} : en-tête absent ou différent des deux lignes {list(ENTETE_JOURNAL)} : nœud")
    if lignes[-1] != "":                                                                   # D-3 : saut de ligne final
        fautes.append("dernière ligne sans saut de ligne")
    else:
        lignes = lignes[:-1]
    precedent, instant_precedent = None, None
    for i, brute in enumerate(lignes[2:], start=3):
        if "\r" in brute or not (len(brute) >= 2 and brute.startswith("|") and brute.endswith("|")):     # D-3 : ligne vide, espaces
            fautes.append(f"ligne {i} : ligne vide, ou qui ne commence ou ne finit pas par « | »")
            continue
        c = [x.strip() for x in brute[1:-1].split("|")]
        if len(c) != 6:
            fautes.append(f"ligne {i} : {len(c)} cellules, six attendues")
            continue
        cle, date, mode, appui, paquets, motif = c
        if cle not in CLES_JOURNAL:
            fautes.append(f"ligne {i} : clé {cle!r} inconnue ({list(CLES_JOURNAL)})")
            continue
        try:
            instant = rg.instant_utc(date)
        except rg.RefusRegistre as e:
            fautes.append(f"ligne {i} : {e}")
            continue
        if mode not in MODES_P3BIS:
            fautes.append(f"ligne {i} : mode {mode!r} inconnu ({list(MODES_P3BIS)})")
            continue
        forme = faute_de_cellules(cle, mode, appui, paquets, motif)                        # D-3 : appui, paquets, motif
        if forme:                                         # faute écrite ; date et ordre de la ligne jugés aussi (toutes les fautes)
            fautes.append(f"ligne {i} : {forme}")
        if instant_precedent is not None and instant < instant_precedent:                 # CT-11
            fautes.append(f"ligne {i} : date {date} antérieure à la ligne précédente (journal en ajout seul : dates non décroissantes)")
            continue
        instant_precedent = instant
        if cle == OUVERTURE_P3BIS:
            if mode not in SUIVANTS_PERMIS[precedent]:
                fautes.append(f"ligne {i} : ouverture {mode!r} après {precedent!r} : ordre interdit par P3-bis (b8, plan, point 8)")
                continue
            precedent = mode
        sortie.append({"numero": i, "cle": cle, "date": date, "instant": instant, "mode": mode, "appui": appui,
                       "paquets": paquets, "motif": motif})
    if fautes:
        raise JournalFautif(f"journal de P3-bis {chemin} hors de son format : " + " ; ".join(fautes) + " : nœud")
    return sortie


def ouvertures(journal: list[dict]) -> list[dict]:
    """Les seules lignes `OUVERTURE-P3BIS` (une ligne `REFUS-OUVERTURE-P3BIS` n'est jamais une ouverture)."""
    return [l for l in journal if l["cle"] == OUVERTURE_P3BIS]


def lire_appui(appui: str) -> list[tuple[str, str]]:
    """Cellule `appui` → [(CLÉ, sha256)] ; forme `CLÉ=sha256` séparées par une espace ; hors forme → `RefusRegistre`."""
    sortie = []
    for morceau in appui.split(" "):
        cle, egal, sha = morceau.partition("=")
        if not egal or not rg.CLE.fullmatch(cle) or not rg.SHA.fullmatch(sha):
            raise rg.RefusRegistre(f"appui {appui!r} : forme `CLÉ=sha256` séparées par une espace attendue")
        sortie.append((cle, sha))
    return sortie


def lire_prealables(chemin: Path, racine: Path, instant: int) -> dict:
    """Registre des préalables de P3-bis → {"garde_adaptee": entree ou None, "rendez_vous": [entree…] (N croissant), "sha256",
    "chemin"} ; entree = {cle, numero (rendez-vous), date, instant, chemin, sha256}. Absent → `RefusRegistre`. Toutes les fautes
    sont relevées, puis rendues ensemble."""
    chemin, racine = Path(chemin), Path(racine)
    if not chemin.is_file():
        raise rg.RefusRegistre(f"registre des préalables de P3-bis {chemin} absent")
    fautes, garde, rdv = [], [], []
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        c = _cellules(ligne)
        if not c or not (len(c) == 4 and rg.DATE.fullmatch(c[1])):
            continue                                          # titre, ligne vide, texte : ignorés (comme `registre_v1`)
        cle, date, rel, sha = c
        m = RENDEZ_VOUS.fullmatch(cle)
        if cle not in CLES_ECRITS_P3BIS and cle != GARDE_ADAPTEE_T07_P3BIS and not m:
            fautes.append(f"préalables de P3-bis : clé {cle!r} inconnue : refus")
            continue
        if cle in CLES_ECRITS_P3BIS:
            continue                                          # connues de P3-bis, non lues par T0.7
        if not rg.SHA.fullmatch(sha) or not rel or rel.startswith("/") or ".." in Path(rel).parts:
            fautes.append(f"préalables de P3-bis : ligne {cle} mal formée (chemin {rel!r}, empreinte {sha!r})")
            continue
        try:
            t = rg.instant_utc(date)
            if not t < int(instant):
                raise rg.RefusRegistre(f"préalables de P3-bis : ligne {cle} datée {date}, pas strictement antérieure à l'ouverture "
                                       f"({rg.date_utc(instant)})")
            rg.sceau_conforme(racine / rel, sha)
        except rg.RefusRegistre as e:
            fautes.append(str(e))
            continue
        entree = {"cle": cle, "date": date, "instant": t, "chemin": rel, "sha256": sha}
        if m:
            entree["numero"] = int(m.group(1))
            rdv.append(entree)
        else:
            garde.append(entree)
    if len(garde) > 1:
        fautes.append(f"préalables de P3-bis : {len(garde)} lignes {GARDE_ADAPTEE_T07_P3BIS}, au plus une attendue")
    numeros = [e["numero"] for e in rdv]
    if numeros != list(range(1, len(rdv) + 1)):
        fautes.append(f"préalables de P3-bis : numéros de rendez-vous {numeros} non consécutifs depuis 1 (dans l'ordre du fichier)")
    if any(not rdv[k]["instant"] < rdv[k + 1]["instant"] for k in range(len(rdv) - 1)):
        fautes.append("préalables de P3-bis : dates des lignes de rendez-vous non strictement croissantes")
    if fautes:
        raise rg.RefusRegistre(" ; ".join(fautes))
    return {"chemin": str(chemin), "sha256": rg.sha256_de(chemin), "garde_adaptee": garde[0] if garde else None, "rendez_vous": rdv}


def lire_decision(racine: Path, entree: dict) -> dict:
    """Décision portée par le fichier que cite une ligne `RENDEZ-VOUS-P3BIS-N` : chemin `docs/decisions/rendez-vous-P3-bis-vN.md` du
    même N (sinon refus), sceau conforme (déjà vérifié par `lire_prealables`, revérifié ici), exactement une ligne `Décision : …` et
    une ligne `Date : …`. Rend {numero, decision, date, chemin, sha256}."""
    attendu = FICHIER_DECISION.format(n=entree["numero"])
    if entree["chemin"] != attendu:
        raise rg.RefusRegistre(f"ligne {entree['cle']} : cite {entree['chemin']!r}, {attendu!r} attendu (même numéro)")
    chemin = Path(racine) / attendu
    rg.sceau_conforme(chemin, entree["sha256"])
    texte = chemin.read_text(encoding="utf-8").splitlines()
    decisions = [m.group(1) for m in (LIGNE_DECISION.fullmatch(l) for l in texte) if m]
    dates = [m.group(1) for m in (LIGNE_DATE.fullmatch(l) for l in texte) if m]
    if len(decisions) != 1 or len(dates) != 1:
        raise rg.RefusRegistre(f"{attendu} : exactement une ligne « Décision : maintenir|ouvrir|ouvrir pleinement » et une ligne "
                               f"« Date : AAAA-MM-JJTHH:MM:SSZ » attendues ({len(decisions)} et {len(dates)} trouvées)")
    return {"numero": entree["numero"], "decision": decisions[0], "date": dates[0], "chemin": attendu, "sha256": entree["sha256"]}


__all__ = ["JournalFautif", "lire_journal_p3bis", "ouvertures", "lire_appui", "lire_prealables", "lire_decision", "JOURNAL_P3BIS",
           "PREALABLES_P3BIS", "ENTETE_JOURNAL", "OUVERTURE_P3BIS", "REFUS_OUVERTURE_P3BIS", "PLEINE", "REDUITE", "PLEINE_ANTICIPEE",
           "MODES_P3BIS", "GARDE_ADAPTEE_T07_P3BIS", "FICHIER_DECISION", "PREREG_T07", "MAINTENIR", "OUVRIR", "OUVRIR_PLEINEMENT",
           "DECISIONS", "CLES_ECRITS_P3BIS"]
