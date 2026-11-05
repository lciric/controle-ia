"""Extraction des énoncés, classifications et cibles semées (T0.5) : contrôle des sorties et assemblage des tâches.

Les sorties viennent de sous-agents neufs (option (a) de P-006) qui appliquent mot pour mot les invites H.9 (énoncé)
et H.10 (classification) de 2606.08892, et l'invite des cibles semées de la procédure d'extraction. Ce module ne
fait aucun appel à un modèle : il contrôle chaque sortie (schéma, interdits de H.9, cibles retrouvées dans le texte
du papier) et rend la liste de ses anomalies. Une sortie avec anomalie n'entre jamais dans les tâches : elle est
refaite ou le papier est remplacé, selon la procédure scellée (aucun repli silencieux).

Chaque anomalie commence par un code stable entre crochets (« [cibles.citation_introuvable] … »), le même que celui du
script de contrôle autonome remis aux sous-agents (`docs/procedures/T0.5-extraction-v1/verifier-sortie-v1.py`) ; un
test du dépôt compare les listes de codes des deux sur des cas sains et des artefacts.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import unicodedata
from pathlib import Path

from ..gardes import GardeArret

_FIGURE = re.compile(r"\[FIGURE\s*\d*\]|\bFig(?:ure|\.)\s*\d+|\bTable\s*\d+", re.I)
_ECHAPPEMENT_MD = re.compile(r"\\([!-/:-@\[-`{-~])")
# Guillemets, tirets (dont U+2010 à U+2012 et le signe moins U+2212) et espace insécable simplifiés ; trait d'union
# conditionnel (U+00AD) retiré.
_TYPO = {**{ord(a): b for a, b in zip("\u2018\u2019\u201c\u201d\u2013\u2014\u2010\u2011\u2012\u2212\u00a0",
                                      "''\"\"------- ")}, 0x00AD: None}
# Indices lexicaux d'un énoncé qui pourrait révéler la méthode, le dispositif ou les résultats (interdits de H.9) :
# simples alertes, jamais des anomalies ; le sous-agent relit alors les règles de H.9 (procédure v1, section 3).
_INDICES_FUITE = re.compile(
    r"\bwe\s+(?:propose|present|introduce|develop|design|show|find|demonstrate|evaluate|conduct|train)\b"
    r"|\bour\s+(?:method|approach|framework|model|algorithm|results?|experiments?|contributions?|findings?"
    r"|analysis|solution)\b"
    r"|\b(?:in\s+)?this\s+(?:paper|work)\b", re.I)
_CONTROLE = re.compile(r"[\x00-\x09\x0b-\x1f]")        # caractères de contrôle, sauf le saut de ligne
_SUBSTITUT = re.compile(r"[\ud800-\udfff]")             # substitut isolé (« \ud835 » sans sa paire ; D-10)
_DOLLAR = re.compile(r"(?<!\\)\$\$?")                    # délimiteur de formule : $ ou $$ non échappé
_LIGNE_VIDE = re.compile(r"\n[ \t]*\n")
_SAUT_MINUSCULE = re.compile(r"\n[a-z]")
CONSEIL_BARRE = ("une barre oblique inverse de LaTeX s'écrit doublée dans une chaîne JSON (\\t, \\b, \\f, \\r, \\n "
                 "sont des échappements)")
# Valeurs de H.10 (2606.08892, invite H.10) ; l'ordre de TYPES_PAPIER est l'échelle du motif 2. Copiées ici pour que
# les décisions de l'extraction ne dépendent pas du code du pilote (contre-lecture 2, D-8) ; un test vérifie leur accord
# avec `propositions`.
TYPES_PAPIER = ("theory_only", "mostly_theory", "mostly_experiments", "experiments_only")
TYPES_DONNEES = ("synthetic_only", "mostly_synthetic", "mostly_real", "real_only", "not_applicable")
MOTS_FUITE = 8          # mots consécutifs d'une citation de direction féconde repris par l'énoncé (fuite mécanique)


def normaliser(texte: str) -> str:
    """Texte comparable : formes Unicode composées, guillemets et tirets simplifiés, échappements du markdown
    (barre oblique inverse devant une ponctuation ASCII) et astérisques retirés, blancs réduits, minuscules.
    Appliquée aux deux côtés (citation et texte du papier), elle ne fait que tolérer la typographie."""
    t = unicodedata.normalize("NFKC", texte).translate(_TYPO)
    t = _ECHAPPEMENT_MD.sub(r"\1", t).replace("*", "")
    return re.sub(r"\s+", " ", t).strip().lower()


def _a(code: str, message: str) -> str:
    return f"[{code}] {message}"


def _chaines(objet):
    """Toutes les chaînes d'un objet JSON (clés comprises), en profondeur."""
    if isinstance(objet, str):
        yield objet
    elif isinstance(objet, dict):
        for k, v in objet.items():
            yield from _chaines(k)
            yield from _chaines(v)
    elif isinstance(objet, list):
        for v in objet:
            yield from _chaines(v)


def _extrait(s: str, i: int, rayon: int = 30) -> str:
    """Une trentaine de caractères autour de la position i (messages, D-4)."""
    return repr(s[max(0, i - rayon):i + rayon])


def position_formule_corrompue(s: str) -> int | None:
    """Position d'un saut de ligne venu d'une barre oblique inverse non doublée (CL-1 ; contre-lecture 2, D-1), ou None :
    - « \\n » suivi de « abla » (« \\nabla » lu comme un saut de ligne), partout ;
    - entre deux délimiteurs $ (ou $$) non échappés, appariés dans l'ordre, sans ligne vide entre eux : un saut de ligne
      suivi d'une minuscule (« \\nu », « \\neq », « \\not »…).
    Un segment qui couvre une ligne vide relie deux montants de deux paragraphes, pas une formule. Résidus déclarés
    (contre-lecture 3, E-3 et E-4) : faux positif, une formule que le papier lui-même coupe d'un saut de ligne (pandoc
    garde ces sauts), recopiée telle quelle (le message dit de remplacer ce saut par une espace) ; faux négatifs, un
    « \\nu » qu'un montant désapparie, une commande en « \\n » hors de toute paire de $ ou suivie d'une majuscule
    (« \\nRightarrow »). Dans une citation, une telle corruption est déjà rattrapée par `citation_introuvable`."""
    i = s.find("\nabla")
    if i >= 0:
        return i
    delims = list(_DOLLAR.finditer(s))
    for ouvre, ferme in zip(delims[0::2], delims[1::2]):
        segment = s[ouvre.end():ferme.start()]
        if _LIGNE_VIDE.search(segment):
            continue
        m = _SAUT_MINUSCULE.search(segment)
        if m:
            return ouvre.end() + m.start()
    return None


def anomalies_texte(objet, fichier: str) -> list[str]:
    """Barres obliques inverses non doublées (CL-1) : en JSON, « \\theta », « \\beta », « \\frac », « \\rho » se lisent
    sans erreur comme tabulation, retour arrière, saut de page ou retour chariot, et « \\nabla » comme un saut de
    ligne. Anomalies : tout caractère de contrôle autre que le saut de ligne ; un saut de ligne de formule
    (`position_formule_corrompue`) ; un substitut isolé, que l'écriture en UTF-8 refuserait (D-10). Chaque message
    situe la première occurrence (D-4)."""
    a = []
    for s in _chaines(objet):
        m = _CONTROLE.search(s)
        if m:
            a.append(_a("texte.controle", f"{fichier} : caractère de contrôle près de {_extrait(s, m.start())} ; "
                                          f"{CONSEIL_BARRE} ; une tabulation copiée du papier se remplace par une "
                                          "espace"))
            break
    for s in _chaines(objet):
        i = position_formule_corrompue(s)
        if i is not None:
            a.append(_a("texte.formule", f"{fichier} : saut de ligne dans une formule près de {_extrait(s, i)} ; "
                                         f"{CONSEIL_BARRE} ; si les $ sont des montants, écrire les montants sans $ ; "
                                         "si le papier lui-même a un saut de ligne à cet endroit (formule sur deux "
                                         "lignes), remplacer ce saut de ligne par une espace"))
            break
    for s in _chaines(objet):
        m = _SUBSTITUT.search(s)
        if m:
            a.append(_a("texte.substitut", f"{fichier} : caractère de substitution isolé près de "
                                           f"{_extrait(s, m.start())} (échappement \\uD8xx sans sa paire)"))
            break
    return a


def alertes_h9(sortie) -> list[str]:
    """Indices lexicaux relevés dans l'énoncé (alertes, non bloquantes), dédoublonnés et triés."""
    rq = sortie.get("research_questions") if isinstance(sortie, dict) else None
    if not isinstance(rq, str):
        return []
    return sorted({" ".join(m.group(0).lower().split()) for m in _INDICES_FUITE.finditer(rq)})


def anomalies_h9(sortie: dict) -> list[str]:
    """Contrôle d'une sortie de H.9 (énoncé, affiliations, coûts)."""
    if not isinstance(sortie, dict):
        return [_a("h9.objet", "sortie H.9 : objet JSON attendu")]
    a = []
    rq = sortie.get("research_questions")
    if not isinstance(rq, str) or len(rq.strip()) < 200:
        a.append(_a("h9.enonce_court", "research_questions absent ou trop court (moins de 200 caractères)"))
    elif _FIGURE.search(rq):
        a.append(_a("h9.figure", f"research_questions cite une figure ou un tableau : {_FIGURE.search(rq).group(0)!r}"))
    if not isinstance(sortie.get("affiliations"), list):
        a.append(_a("h9.affiliations", "affiliations : liste attendue"))
    couts = sortie.get("costs")
    if not isinstance(couts, dict) or "total" not in couts or not isinstance(couts.get("splits", []), list):
        a.append(_a("h9.couts", "costs : objet {total, splits} attendu"))
    return a + anomalies_texte(sortie, "h9.json")


def _cle(v) -> str:
    return str(v).replace("\\_", "_").strip()


def h10_normalisee(sortie: dict) -> dict:
    """Sortie de H.10 aux clés sans tiret bas échappé (« data\\_type », comme dans l'invite, CL-27)."""
    return {_cle(k): v for k, v in sortie.items()} if isinstance(sortie, dict) else sortie


def anomalies_h10(sortie: dict) -> list[str]:
    """Contrôle d'une sortie de H.10 (classification)."""
    if not isinstance(sortie, dict):
        return [_a("h10.objet", "sortie H.10 : objet JSON attendu")]
    s, a = h10_normalisee(sortie), []
    if _cle(s.get("theory_experiment", "")) not in TYPES_PAPIER:
        a.append(_a("h10.type_papier", f"theory_experiment illisible : {s.get('theory_experiment')!r}"))
    if _cle(s.get("data_type", "")) not in TYPES_DONNEES:
        a.append(_a("h10.type_donnees", f"data_type illisible : {s.get('data_type')!r}"))
    if not isinstance(s.get("domains", None), list):
        a.append(_a("h10.domaines", "domains : liste attendue"))
    return a + anomalies_texte(sortie, "h10.json")


BORNES_CIBLES = {"controls": (3, 6), "fruitful_directions": (1, 3), "sterile_directions": (0, 3)}


def nombre_positif(h) -> bool:
    """Nombre strictement positif et fini, convertible en flottant sans dépassement (CL-14 ; contre-lecture 2, D-11) ;
    un booléen n'en est pas un."""
    if isinstance(h, bool) or not isinstance(h, (int, float)):
        return False
    try:
        f = float(h)          # un entier trop grand pour un flottant est refusé (le pilote calcule en flottants)
    except OverflowError:
        return False
    return math.isfinite(f) and f > 0


def anomalies_cibles(sortie: dict, texte_papier: str) -> list[str]:
    """Contrôle des cibles semées : schéma, bornes, identifiants uniques et textuels, et chaque citation retrouvée dans
    le texte converti du papier (à la normalisation près)."""
    if not isinstance(sortie, dict):
        return [_a("cibles.objet", "cibles : objet JSON attendu")]
    a, ids = [], set()
    corps = normaliser(texte_papier)
    for famille, (lo, hi) in BORNES_CIBLES.items():
        items = sortie.get(famille)
        if not isinstance(items, list) or not lo <= len(items) <= hi:
            a.append(_a("cibles.bornes", f"{famille} : entre {lo} et {hi} éléments attendus"))
            continue
        for it in items:
            if not isinstance(it, dict):
                a.append(_a("cibles.element", f"{famille} : élément non conforme"))
                continue
            ident = it.get("id")
            if not isinstance(ident, str) or not ident.strip() or ident in ids:
                a.append(_a("cibles.identifiant", f"{famille} : identifiant absent, non textuel ou en double "
                                                  f"({ident!r})"))
            else:
                ids.add(ident)
            if len(str(it.get("description", "")).strip()) < 10:
                a.append(_a("cibles.description", f"{ident!r} : description absente ou trop courte"))
            preuve = str(it.get("evidence", "")).strip()
            if len(preuve) < 20:
                a.append(_a("cibles.citation_courte", f"{ident!r} : citation absente ou trop courte"))
            elif normaliser(preuve) not in corps:
                a.append(_a("cibles.citation_introuvable", f"{ident!r} : citation introuvable dans le texte du "
                                                           "papier"))
    calcul = sortie.get("compute")
    if not isinstance(calcul, dict) or calcul.get("basis") not in ("reported", "estimated"):
        a.append(_a("cibles.calcul", "compute : objet {reference_gpu_hours, basis, evidence} attendu"))
    else:
        h = calcul.get("reference_gpu_hours")
        if h is not None and not nombre_positif(h):
            a.append(_a("cibles.calcul_valeur", f"compute.reference_gpu_hours : nombre positif ou null attendu "
                                                f"({str(h)[:40]!r})"))
    return a + anomalies_texte(sortie, "cibles.json")


def _ngrammes(texte: str, n: int) -> set:
    mots = normaliser(texte).split()
    return {tuple(mots[i:i + n]) for i in range(len(mots) - n + 1)}


def anomalies_fuite(sortie_h9: dict, cibles: dict, n: int = MOTS_FUITE) -> list[str]:
    """Fuite mécanique (CL-26) : l'énoncé reprend au moins `n` mots consécutifs de la citation d'une direction
    féconde (l'approche ou le résultat du papier). Ne s'applique qu'à des sorties de forme valide."""
    rq = sortie_h9.get("research_questions") if isinstance(sortie_h9, dict) else None
    items = cibles.get("fruitful_directions") if isinstance(cibles, dict) else None
    if not isinstance(rq, str) or not isinstance(items, list):
        return []
    enonce = _ngrammes(rq, n)
    a = []
    for it in items:
        if isinstance(it, dict) and _ngrammes(str(it.get("evidence", "")), n) & enonce:
            a.append(_a("h9.fuite_citation", f"l'énoncé reprend {n} mots consécutifs ou plus de la citation de "
                                             f"{it.get('id')!r} (direction féconde) : il peut révéler l'approche ; "
                                             "corriger l'énoncé, pas la citation"))
    return a


def assembler_tache(identifiant: str, sortie_h9: dict, sortie_h10: dict, cibles: dict, texte_papier: str) -> dict:
    """Tâche prête pour le pilote, seulement si les trois sorties sont sans anomalie (sinon arrêt)."""
    anomalies = (anomalies_h9(sortie_h9) + anomalies_h10(sortie_h10) + anomalies_cibles(cibles, texte_papier)
                 + anomalies_fuite(sortie_h9, cibles))
    if anomalies:
        raise GardeArret(f"{identifiant} : {len(anomalies)} anomalie(s) : {anomalies[:5]}")
    h10 = h10_normalisee(sortie_h10)
    classification = {k: _cle(h10[k]) for k in ("theory_experiment", "data_type")}
    classification["domains"] = [str(d) for d in h10["domains"]]
    return {"identifiant": identifiant, "questions": sortie_h9["research_questions"].strip(),
            "classification": classification, "cibles": cibles, "couts_rapportes": sortie_h9["costs"]}


def exclue_par_classification(sortie_h10: dict) -> bool:
    """Règle d'exclusion de la procédure : un papier « theory_only » sort du pilote (remplacé par la réserve)."""
    return _cle(h10_normalisee(sortie_h10).get("theory_experiment", "")) == "theory_only"


# --- Procédure v1 (docs/procedures/T0.5-extraction-v1.md) : copie de lecture, sorties d'un papier, avis de
# contre-vérification, statut de chaque papier, listes de tâches. Aucun appel à un modèle ; rien n'est réparé.

TAILLE_PARTIE = 25_000
LIGNES_PARTIE = 1500
NOMS_SORTIES = ("h9", "h10", "cibles")
FAMILLES_CIBLES = ("controls", "fruitful_directions", "sterile_directions")


def copie_de_lecture(texte: str, taille_partie: int = TAILLE_PARTIE, lignes_partie: int = LIGNES_PARTIE) -> list[str]:
    """Le texte converti, découpé aux fins de ligne en parties consécutives d'au plus `taille_partie` caractères et
    `lignes_partie` lignes, pour l'outil de lecture d'un sous-agent (qui lit par morceaux d'un nombre borné de
    jetons ; contre-lecture, CL-20). Aucune ligne n'est coupée : la concaténation des parties est le texte, au
    caractère près (garde). Une ligne plus longue qu'une partie arrête."""
    lignes = texte.split("\n")
    if any(len(ligne) + 1 > taille_partie for ligne in lignes):
        raise GardeArret(f"copie de lecture : ligne de plus de {taille_partie - 1} caractères")
    parties, courant, taille = [], [], 0
    for ligne in lignes:
        if courant and (taille + len(ligne) + 1 > taille_partie or len(courant) >= lignes_partie):
            parties.append("\n".join(courant) + "\n")
            courant, taille = [], 0
        courant.append(ligne)
        taille += len(ligne) + 1
    parties.append("\n".join(courant))
    exiger_copie(parties, texte, taille_partie, lignes_partie)
    return parties


def exiger_copie(parties: list[str], texte: str, taille_partie: int, lignes_partie: int) -> None:
    """Gardes finales de la copie de lecture (séparées pour être éprouvées sur un artefact) : la concaténation est le
    texte, et chaque partie tient dans ses bornes."""
    if "".join(parties) != texte:
        raise GardeArret("copie de lecture : la concaténation des parties n'est pas le texte")
    if any(len(p) > taille_partie or p.count("\n") > lignes_partie for p in parties):
        raise GardeArret("copie de lecture : partie hors bornes")


def _refuser_constante(nom):
    raise ValueError(f"constante JSON non standard : {nom}")


def lire_json(chemin) -> tuple[object, str]:
    """Objet JSON d'un fichier et empreinte de ses octets ; `ValueError` si illisible (NaN et infinis refusés)."""
    brut = Path(chemin).read_bytes()
    return json.loads(brut.decode("utf-8"), parse_constant=_refuser_constante), hashlib.sha256(brut).hexdigest()


def controler_sorties(sorties: dict, texte_papier: str) -> list[str]:
    """Anomalies des sorties lues (`sorties[nom]` pour les noms présents), fuite mécanique comprise."""
    anomalies = []
    if "h9" in sorties:
        anomalies += anomalies_h9(sorties["h9"])
    if "h10" in sorties:
        anomalies += anomalies_h10(sorties["h10"])
    if "cibles" in sorties:
        anomalies += anomalies_cibles(sorties["cibles"], texte_papier)
    if "h9" in sorties and "cibles" in sorties:
        anomalies += anomalies_fuite(sorties["h9"], sorties["cibles"])
    return anomalies


def lire_sorties(dossier_sorties, texte_papier: str) -> dict:
    """Contrôle des trois sorties d'un papier (`h9.json`, `h10.json`, `cibles.json`) : sorties lues, empreintes,
    anomalies (bloquantes), alertes (non bloquantes) et règle « theory_only ». Un fichier absent ou illisible est une
    anomalie."""
    dossier = Path(dossier_sorties)
    sorties, empreintes, anomalies = {}, {}, []
    for nom in NOMS_SORTIES:
        chemin = dossier / f"{nom}.json"
        if not chemin.is_file():
            anomalies.append(_a("fichier.absent", f"{nom}.json absent"))
            continue
        try:
            sorties[nom], empreintes[nom] = lire_json(chemin)
        except ValueError as e:  # JSONDecodeError et UnicodeDecodeError en dérivent
            anomalies.append(_a("json.illisible", f"{nom}.json illisible : {e}"))
            empreintes[nom] = hashlib.sha256(chemin.read_bytes()).hexdigest()
    anomalies += controler_sorties(sorties, texte_papier)
    theorie = not anomalies and exclue_par_classification(sorties["h10"])
    return {"sorties": sorties, "empreintes": empreintes, "anomalies": anomalies,
            "alertes": alertes_h9(sorties.get("h9")), "theory_only": theorie}


def code_anomalie(anomalie: str) -> str:
    """Code stable d'une anomalie (« [code] message »)."""
    m = re.match(r"\[([a-z0-9_.]+)\]", anomalie)
    if not m:
        raise GardeArret(f"anomalie sans code : {anomalie[:60]!r}")
    return m.group(1)


CHAMPS_AVIS = {"statement_leaks": bool, "leak_passages": list, "theory_experiment_correct": bool,
               "theory_experiment_expected": str, "data_type_correct": bool, "data_type_expected": str,
               "domains_reasonable": bool, "targets": list, "compute_plausible": bool, "comment": str}


def ids_cibles(cibles: dict) -> list[str]:
    """Identifiants des cibles, dans l'ordre : contrôles, directions fécondes, directions stériles."""
    return [it["id"] for f in FAMILLES_CIBLES for it in cibles[f]]


def anomalies_avis(avis, h9: dict, h10: dict, cibles: dict) -> list[str]:
    """Contrôle de forme et de cohérence d'un avis de contre-vérification (aucun jugement sur le fond)."""
    if not isinstance(avis, dict):
        return [_a("avis.objet", "avis : objet JSON attendu")]
    a = []
    if set(avis) != set(CHAMPS_AVIS):
        a.append(_a("avis.champs", f"avis : champs manquants {sorted(set(CHAMPS_AVIS) - set(avis))}, "
                                   f"en trop {sorted(set(avis) - set(CHAMPS_AVIS))}"))
    for k, t in CHAMPS_AVIS.items():
        if k in avis and not isinstance(avis[k], t):
            a.append(_a("avis.type", f"avis : {k} de type {type(avis[k]).__name__}, {t.__name__} attendu"))
    if a:
        return a
    h10 = h10_normalisee(h10)
    for k, valeurs, reel in (("theory_experiment", TYPES_PAPIER, h10.get("theory_experiment")),
                             ("data_type", TYPES_DONNEES, h10.get("data_type"))):
        attendu = _cle(avis[f"{k}_expected"])
        if attendu not in valeurs:
            a.append(_a("avis.valeur", f"avis : {k}_expected hors des valeurs de H.10 ({attendu!r})"))
        elif avis[f"{k}_correct"] != (attendu == _cle(reel)):
            a.append(_a("avis.coherence", f"avis : {k}_correct incohérent avec {k}_expected"))
    cles = [t.get("id") if isinstance(t, dict) else None for t in avis["targets"]]
    if cles != ids_cibles(cibles):
        a.append(_a("avis.cibles", f"avis : cibles {cles} ≠ cibles du fichier {ids_cibles(cibles)}"))
    for t in avis["targets"]:
        if not (isinstance(t, dict) and isinstance(t.get("grounded"), bool) and isinstance(t.get("observable"), bool)):
            a.append(_a("avis.cible", f"avis : cible {str(t)[:60]!r} sans grounded ou observable booléens"))
    passages = avis["leak_passages"]
    if avis["statement_leaks"] != bool(passages):
        a.append(_a("avis.fuite", "avis : statement_leaks incohérent avec leak_passages"))
    enonce = normaliser(str(h9.get("research_questions", "")))
    for p in passages:
        if not isinstance(p, str) or not normaliser(p) or normaliser(p) not in enonce:
            a.append(_a("avis.passage", f"avis : passage introuvable dans l'énoncé : {str(p)[:60]!r}"))
    return a + anomalies_texte(avis, "avis.json")


def motifs_echec_avis(avis: dict, cibles: dict, h10: dict) -> list[str]:
    """Motifs d'échec d'un papier à la contre-vérification (procédure v1, section 6) ; liste vide si réussi. La
    classification n'échoue que sur une erreur qui change une décision (CL-10) : « theory_only » attendu et non donné,
    ou l'inverse, ou un écart de deux crans ou plus sur l'échelle de H.10."""
    m = []
    if avis["statement_leaks"]:
        m.append("énoncé qui révèle ce que H.9 interdit")
    echelle = list(TYPES_PAPIER)
    donne, attendu = _cle(h10_normalisee(h10).get("theory_experiment")), _cle(avis["theory_experiment_expected"])
    if ((donne == "theory_only") != (attendu == "theory_only")
            or abs(echelle.index(donne) - echelle.index(attendu)) >= 2):
        m.append("theory_experiment faux au point de changer une décision")
    bons = {t["id"] for t in avis["targets"] if t["grounded"] and t["observable"]}
    n = sum(it["id"] in bons for it in cibles["controls"])
    if n < 3:
        m.append(f"{n} contrôle(s) fondé(s) et observable(s), moins de 3")
    if not any(it["id"] in bons for it in cibles["fruitful_directions"]):
        m.append("aucune direction féconde fondée et observable")
    return m


def echantillon_contre_verification(ordre: list[str], graine: dict, admissibles: set[str], n: int = 16):
    """Les `n` premiers papiers admissibles d'une permutation de `ordre` tirée par la graine du manifeste (R9)."""
    from ..manifeste import generateur

    permutation = [ordre[i] for i in generateur(graine).permutation(len(ordre))]
    retenus = [p for p in permutation if p in admissibles][:n]
    if len(retenus) < n:
        raise GardeArret(f"échantillon de contre-vérification : {len(retenus)} papiers admissibles, {n} attendus")
    return retenus, permutation


ROLES_VERDICT = ("echantillon", "audit", "theorie", "reprise")


def _premier(verdicts: list[dict], role: str, tentative: int) -> dict | None:
    return next((v for v in verdicts if v["role"] == role and v["tentative"] == tentative), None)


def statut_papier(p: str, validations: dict[int, dict], verdicts: list[dict]) -> dict:
    """Statut d'un papier selon la procédure v1, depuis les validations par tentative ({K: {papier: fiche}}) et ses
    verdicts lisibles de contre-vérification, dans l'ordre des rondes ({role, tentative, motifs}).

    Tentatives : 1 ; 2 si et seulement si 1 est invalide ; 3 si et seulement si une reprise est due : premier avis
    « echantillon » ou « audit » en échec sur la tentative retenue, ou « theory_only » contesté par l'avis « theorie ».
    Une exclusion « theory_only » n'est acquise qu'après son avis « theorie » (CL-25). Tout autre cas est une
    procédure non suivie : arrêt."""
    tentatives = sorted(k for k, v in validations.items() if p in v)
    if not tentatives or tentatives[0] != 1:
        raise GardeArret(f"{p} : tentative 1 absente")
    if validations[1][p]["anomalies"]:
        if 2 not in tentatives:
            raise GardeArret(f"{p} : invalide à la tentative 1 et non refait")
        if validations[2][p]["anomalies"]:
            if 3 in tentatives:
                raise GardeArret(f"{p} : tentative 3 sans motif")
            return {"statut": "exclu", "motif": "sorties invalides à deux tentatives", "tentative": None}
        retenue = 2
    else:
        if 2 in tentatives:
            raise GardeArret(f"{p} : tentative 2 sans motif (tentative 1 valide)")
        retenue = 1
    if validations[retenue][p]["theory_only"]:
        th = _premier(verdicts, "theorie", retenue)
        if th is None:
            raise GardeArret(f"{p} : exclusion « theory_only » non contre-vérifiée")
        if not th["motifs"]:
            if 3 in tentatives:
                raise GardeArret(f"{p} : tentative 3 sans motif")
            return {"statut": "exclu", "motif": "theory_only (confirmé)", "tentative": retenue}
        reprise_due, contre_verifie = True, True
    else:
        e, au = _premier(verdicts, "echantillon", retenue), _premier(verdicts, "audit", retenue)
        reprise_due = bool((e and e["motifs"]) or (au and au["motifs"]))
        contre_verifie = e is not None
    if not reprise_due:
        if 3 in tentatives or _premier(verdicts, "reprise", 3) is not None:
            raise GardeArret(f"{p} : reprise sans motif")
        return {"statut": "retenu", "tentative": retenue, "contre_verifie": contre_verifie}
    if 3 not in tentatives:
        raise GardeArret(f"{p} : échec de contre-vérification non repris")
    if validations[3][p]["anomalies"]:
        return {"statut": "exclu", "motif": "reprise invalide", "tentative": None}
    if validations[3][p]["theory_only"]:
        return {"statut": "exclu", "motif": "theory_only (reprise)", "tentative": 3}
    r = _premier(verdicts, "reprise", 3)
    if r is None:
        raise GardeArret(f"{p} : reprise non contre-vérifiée")
    if r["motifs"]:
        return {"statut": "exclu", "motif": "contre-vérification échouée deux fois", "tentative": 3}
    return {"statut": "retenu", "tentative": 3, "contre_verifie": True}


MINIMUM_ENTRAINEMENT = 20


def exiger_disjointes(evaluation: list[str], entrainement: list[str]) -> None:
    """Aucune tâche d'entraînement n'est une tâche d'évaluation (garde finale, séparée pour être éprouvée)."""
    if set(evaluation) & set(entrainement):
        raise GardeArret("une tâche d'entraînement est aussi une tâche d'évaluation")


def listes_de_taches(pilote: list[str], reserve: list[str], statuts: dict[str, dict]) -> dict:
    """Tâches d'évaluation (le pilote, chaque papier exclu remplacé par le premier papier de réserve retenu et non
    utilisé, dans l'ordre) et tâches d'entraînement (papiers de réserve retenus et non utilisés)."""
    if set(pilote) & set(reserve) or len(set(pilote)) != len(pilote) or len(set(reserve)) != len(reserve):
        raise GardeArret("pilote et réserve : listes en double ou qui se recoupent")
    if set(statuts) != set(pilote) | set(reserve):
        raise GardeArret("statuts incomplets ou en trop par rapport au pilote et à la réserve")
    retenus = {p for p, s in statuts.items() if s["statut"] == "retenu"}
    file = [r for r in reserve if r in retenus]
    evaluation, remplacements, sans_remplacant = [], [], []
    for p in pilote:
        if p in retenus:
            evaluation.append(p)
        elif file:
            r = file.pop(0)
            evaluation.append(r)
            remplacements.append({"exclu": p, "remplacant": r})
        else:
            sans_remplacant.append(p)
    if sans_remplacant:
        raise GardeArret(f"{len(sans_remplacant)} papier(s) du pilote sans remplaçant : réserve épuisée, "
                         "tirage complémentaire à proposer à Lazar")
    entrainement = file
    exiger_disjointes(evaluation, entrainement)
    return {"evaluation": evaluation, "remplacements": remplacements, "entrainement": entrainement,
            "entrainement_insuffisant": len(entrainement) < MINIMUM_ENTRAINEMENT}
