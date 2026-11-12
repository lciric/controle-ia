"""Passe à blanc de l'extracteur de T0.7, v1 (fichier neuf, R12 ; consigne de la mère du 10 novembre 2026, « passe à blanc de
l'extracteur, puis ordre d'exécution de l'étape A » ; GO-2026-11-10-04 la nomme : « passe à blanc de l'extracteur »).

Jouée sur l'instance **avant** l'étape A, avec la configuration et le registre de l'étape A, elle éprouve trois choses et rien
d'autre :

1. **l'extraction des jeux génériques en mode réel** (modèle de la course lue, `lecture_v2.extracteur_de_la_course`, cache local
   seulement) sur un **échantillon petit, fixe et écrit** : pour chaque jeu scellé présent au registre, les enregistrements des
   `PAIRES_PAR_JEU` premières paires dans l'ordre canonique de `lire_jeu` (tâche, paire, membre), plus l'enregistrement le plus long (jetons de la conversation ;
   le premier en cas d'égalité), à l'empan de l'étape A (`sondes_neuves_v1.EMPAN_DE_JEU`), et pour J-C aussi l'action entière ;
   pour les phrases des concepts, les `PAIRES_PAR_CONCEPT` premières paires (par indice) de chaque concept, plus la phrase la
   plus longue ; les enregistrements pris sont écrits dans la sortie ;
2. **la frontière « avant le champ »** sur le **découpage réel des jetons**, au tokeniseur seul, sur **tous** les enregistrements
   des jeux lus à cet empan (J-C, J-A) : frontière `Extracteur.frontiere` de l'étape A, jugée par un décodage fidèle
   (`clean_up_tokenization_spaces=False`) : (F1) au moins un jeton avant la frontière et au moins un après ; (F2) les jetons
   avant la frontière redonnent le début de la réponse (sans ses blancs de tête) et n'entrent pas dans le champ `COST:` ; (F3)
   frontière maximale : le jeton suivant atteint le champ ; (F4) le champ `COST:` est à la position écrite, réponse sans ses
   blancs de tête ; plus, sur tous les enregistrements de tous les jeux, la garde du gabarit de l'étape A
   (`jetons_reponse_forcee` : identifiants = rendu complet du gabarit) ;
2 bis. **la garde d'identité des jeux** (E-8, décision D-2 (a), R-2101 ; `controle_jeux_v1.remesurer_jetons`) : les moyennes de
   longueur du journal du script des jeux (mots, caractères, jetons) recalculées au tokeniseur du modèle ; écart → arrêt motivé
   (l'étape A refait la même garde ; la passe l'éprouve avant que l'ouverture fixe le périmètre) ;
3. **la durée et la mémoire** : chargement du modèle, durée de chaque passe de l'échantillon, estimation de la durée de
   l'extraction de l'étape A (moyenne des passes hors la première × nombre de passes de l'étape A) ; mémoire de la carte (pic
   réservé, `torch.cuda.max_memory_reserved`, contre `PART_CARTE_MAX` de la carte) et de l'hôte (activations que l'étape A garde
   en mémoire pour tous les jeux et toutes les phrases, en float32, aux couches lues, × `FACTEUR_COPIES`, contre `PART_HOTE_MAX`
   de la mémoire disponible relevée après le chargement et l'échantillon).
   **DF-04** : aussi la mémoire de la **notation** (une couche, toutes les actions notées, float32 : jetons notés lus dans `mesures-t06.npz`),
   au même facteur et à la même part ; mesures illisibles : arrêt. **DF-02** : avec `code_t07_exige` vrai, `CODE-T07` est
   contrôlée avant tout (`code_t07_v1.controler_code`) ; absente ou non conforme : refus, code 2.

**Elle n'écrit rien de décisif** : ni manifeste de run, ni score, ni notation d'une action d'organisme, ni sonde, ni ligne de
registre, ni ligne `OUVERTURE-T07` ou `REFUS-T07` au journal (l'instant de fermeture du périmètre des jeux reste celui de la
première ouverture de l'étape A) ; elle ne lit de la course de T0.6 que son manifeste (`runs/<run>/manifeste.json` : modèle,
mode, graine du modèle jouet) ; aucun tirage aléatoire (aucune graine). **Sortie** : un seul fichier scellé,
`passes-blanches-t07/<AAAAMMJJ-HHMMSS>-passe-blanc-t07-<mode>/passe-blanc-extracteur-t07.json` (et son compagnon), hors de
`runs/`, `diag/` et `donnees/`, sous un nom qu'aucune sortie de l'étape A ne porte.

**Codes** : 0 passe tenue (frontière et mémoire tiennent, extraction de l'échantillon menée), sortie scellée ; 2 refus avant
tout calcul (configuration, registre, fichier cité ou sceau, modèle introuvable ; motif imprimé, rien d'écrit) ; 3 **arrêt
motivé** : la frontière, la mémoire ou l'extraction de l'échantillon ne tient pas (motif écrit dans la sortie scellée et
imprimé) ; l'étape A ne part pas sans un mot de la mère.

    PYTHONPATH=src python -m controle_ia.t07.lecture_v2 passe-blanc RACINE RUN_T06 CONFIG_T07 [--registre CHEMIN] [--racine-sortie R]
"""
from __future__ import annotations

import argparse
import json
import platform
import resource
import sys
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, etat_git
from ..harnais.formats import _ids
from ..premier_test_ia.empans import jetons_message_utilisateur, jetons_reponse_forcee
from ..scellement import sceller
from . import controle_jeux_v1 as cj
from . import registre_v1 as rg
from . import sondes_neuves_v1 as sn

COMMANDE = "python -m controle_ia.t07.lecture_v2 passe-blanc"
VERSION = "passe_blanc_v1"
NATURE = ("passe à blanc de l'extracteur de T0.7 : aucune donnée décisive (ni manifeste de run, ni score, ni notation d'organisme, "
          "ni sonde, ni ligne de registre, ni ouverture)")
DOSSIER = "passes-blanches-t07"
FICHIER = "passe-blanc-extracteur-t07.json"
PAIRES_PAR_JEU = 2
PAIRES_PAR_CONCEPT = 2
PART_CARTE_MAX = 0.90
PART_HOTE_MAX = 0.80
FACTEUR_COPIES = 2.0
OCTETS_FLOAT32 = 4
FAUTES_ECRITES = 20
CHAMP = "COST:"
CODE_OK, CODE_REFUS, CODE_ARRET = 0, 2, 3
JEUX = ((rg.SCELLEMENT_JEUX_JD, "JD", sn.JEU_JD), (rg.SCELLEMENT_JEUX_JC, "JC", sn.JEU_JC), (rg.SCELLEMENT_JEUX_JA, "JA", sn.JEU_JA))
REGLE_ECHANTILLON = (f"par jeu scellé présent : les enregistrements des {PAIRES_PAR_JEU} premières paires (tâche, paire) dans l'ordre "
                     "canonique de lire_jeu (tâche, paire, membre), plus l'enregistrement le plus long (jetons de la conversation ; le premier en cas d'égalité), à l'empan de "
                     f"l'étape A, et pour J-C aussi l'action entière ; phrases : les {PAIRES_PAR_CONCEPT} premières paires (par indice) "
                     "de chaque concept (phrase du concept et phrase neutre), plus la phrase la plus longue (jetons ; la première en cas "
                     "d'égalité)")


class RefusPasse(GardeArret):
    """Refus avant tout calcul (code 2) : rien n'est écrit."""


# ------------------------------------------------------------------------------------------------------------------ mesures
def _decoder(tok, ids) -> str:
    try:
        return tok.decode(list(ids), clean_up_tokenization_spaces=False)
    except TypeError:
        return tok.decode(list(ids))


def _meminfo(cle: str) -> int | None:
    try:
        for l in Path("/proc/meminfo").read_text().splitlines():
            if l.startswith(cle + ":"):
                return int(l.split()[1]) * 1024
    except (OSError, ValueError, IndexError):
        return None
    return None


def _statut(cle: str) -> int | None:
    try:
        for l in Path("/proc/self/status").read_text().splitlines():
            if l.startswith(cle + ":"):
                return int(l.split()[1]) * 1024
    except (OSError, ValueError, IndexError):
        return None
    return None


def sonde_memoire() -> dict:
    """Mémoire de l'hôte (`/proc` : disponible, résidente, pic résident) et de la carte (pic alloué et réservé, total), en octets ;
    une valeur illisible vaut `None` ; sans carte, `carte` vaut `None`."""
    hote = {"disponible": _meminfo("MemAvailable"), "totale": _meminfo("MemTotal"), "residente": _statut("VmRSS"),
            "pic_resident": _statut("VmHWM")}
    if hote["pic_resident"] is None:
        try:
            hote["pic_resident"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) * 1024
        except (OSError, ValueError):
            pass
    carte = None
    try:
        import torch
        if torch.cuda.is_available():
            carte = {"pic_alloue": int(torch.cuda.max_memory_allocated()), "pic_reserve": int(torch.cuda.max_memory_reserved()),
                     "totale": int(torch.cuda.get_device_properties(0).total_memory), "nom": torch.cuda.get_device_name(0)}
    except Exception as e:                                       # mesure illisible : écrite, jugée par la garde
        carte = {"illisible": f"{type(e).__name__}: {e}"[:300]}
    return {"hote": hote, "carte": carte}


def versions() -> dict:
    v = {"python": platform.python_version(), "numpy": np.__version__}
    for nom in ("torch", "transformers"):
        try:
            v[nom] = __import__(nom).__version__
        except Exception:
            v[nom] = None
    return v


# ---------------------------------------------------------------------------------------------------------------- frontière
def controler_frontiere(ext, reponse: str, position_cost: int) -> dict:
    """Frontière « avant le champ » de l'étape A (`Extracteur.frontiere`) sur le découpage réel, jugée par F1 à F4 (docstring du
    module). Rend {k, jetons, exacte, faute}."""
    tok = ext.fmt.tok
    t = reponse.strip()
    blancs = len(reponse) - len(reponse.lstrip())
    borne = int(position_cost) - blancs
    plein = _ids(tok, t)
    avant = ext.frontieres_ajustees
    k = ext.frontiere(reponse, int(position_cost))
    exacte = ext.frontieres_ajustees == avant
    faute = None
    if borne < 0 or not t[borne:].startswith(CHAMP):
        faute = f"F4 : le champ {CHAMP} n'est pas à la position écrite ({position_cost}) dans la réponse sans ses blancs de tête ({blancs})"
    elif not 1 <= k < len(plein):
        faute = f"F1 : frontière {k} hors de [1, {len(plein)}[ (aucun jeton avant le champ, ou aucun après)"
    else:
        dec = _decoder(tok, plein[:k])
        if not t.startswith(dec):
            faute = "F2 : les jetons avant la frontière ne redonnent pas le début de la réponse (décodage fidèle)"
        elif len(dec) > borne:
            faute = f"F2 : la frontière entre dans le champ {CHAMP} ({len(dec)} caractères décodés pour {borne} avant le champ)"
        elif len(_decoder(tok, plein[:k + 1])) <= borne:
            faute = "F3 : frontière non maximale (le jeton suivant est encore entier avant le champ)"
    return {"k": int(k), "jetons": len(plein), "exacte": bool(exacte), "faute": faute}


def controler_jeu(ext, recs: list, empan: str) -> dict:
    """Tokeniseur seul, sur tous les enregistrements d'un jeu : garde du gabarit de l'étape A et, à l'empan « avant le champ »,
    frontière (F1 à F4). Rend les jetons par enregistrement (conversation, empan de l'étape A, action entière) et les fautes."""
    fautes, conv, emp, entier = [], [], [], []
    exactes = ajustees = 0
    for i, r in enumerate(recs):
        lieu = {"indice": i, "tache": r["tache"], "paire": r["paire"], "membre": r["membre"]}
        try:
            f = jetons_reponse_forcee(ext.fmt, r["contexte_systeme"], r["observation"], r["reponse"], 0)
        except GardeArret as e:
            fautes.append({**lieu, "faute": f"gabarit : {e}"})
            for liste in (conv, emp, entier):
                liste.append(0)
            continue
        n_rep = int(f["fin"] - f["debut"])
        conv.append(len(f["ids"]))
        entier.append(n_rep)
        if empan == "avant_champ":
            fr = controler_frontiere(ext, r["reponse"], r["position_cost"])
            exactes += fr["exacte"]
            ajustees += not fr["exacte"]
            if fr["faute"]:
                fautes.append({**lieu, "faute": fr["faute"], "k": fr["k"], "jetons": fr["jetons"]})
            emp.append(fr["k"])
        else:
            emp.append(n_rep)
    return {"n": len(recs), "jetons_conversation": conv, "jetons_empan": emp, "jetons_action_entiere": entier,
            "frontiere": ({"exactes": exactes, "ajustees": ajustees} if empan == "avant_champ" else None), "fautes": fautes}


def echantillon_jeu(recs: list, jetons_conversation: list) -> list[int]:
    """Indices de l'échantillon fixe d'un jeu (`REGLE_ECHANTILLON`), triés."""
    paires, pris = [], []
    for i, r in enumerate(recs):
        cle = (r["tache"], r["paire"])
        if cle not in paires:
            if len(paires) == PAIRES_PAR_JEU:
                continue
            paires.append(cle)
        pris.append(i)
    if jetons_conversation:
        pris.append(int(np.argmax(np.asarray(jetons_conversation))))
    return sorted(set(pris))


def jetons_phrase(ext, texte: str, format_lecture: str) -> int:
    if format_lecture == "message_utilisateur":
        r = jetons_message_utilisateur(ext.fmt, "", texte, sn.MAX_JETONS_PHRASE)
        return int(r["fin"] - r["debut"])
    return len(_ids(ext.fmt.tok, texte.strip()))


# --------------------------------------------------------------------------------------------------------------------- entrées
def lire_entrees(racine: Path, registre: Path) -> dict:
    """Jeux scellés et phrases des concepts **présents au registre** (première ligne de chaque clé, lecture seule ; aucune garde
    d'ouverture, aucune ligne de journal), sceau et empreinte de la ligne vérifiés, contenu contrôlé (`lire_jeu`,
    `lire_phrases_concepts`). Rien de présent → refus."""
    from .lecture_v2 import lire_lignes_actuelles
    lignes = lire_lignes_actuelles(registre, [c for c, _, _ in JEUX] + [rg.SCELLEMENT_CONCEPTS_T07])
    jeux, fichiers, phrases = {}, {}, None
    try:
        for cle, nom, jeu in JEUX:
            if cle in lignes:
                p = Path(racine) / lignes[cle]["chemin"]
                fichiers[nom] = {"cle": cle, "chemin": lignes[cle]["chemin"], "sha256": rg.sceau_conforme(p, lignes[cle]["sha256"]),
                                 "date_ligne": lignes[cle]["date"]}
                jeux[nom] = sn.lire_jeu(p, jeu)
        if rg.SCELLEMENT_CONCEPTS_T07 in lignes:
            l = lignes[rg.SCELLEMENT_CONCEPTS_T07]
            p = Path(racine) / l["chemin"]
            fichiers["concepts"] = {"cle": rg.SCELLEMENT_CONCEPTS_T07, "chemin": l["chemin"],
                                    "sha256": rg.sceau_conforme(p, l["sha256"]), "date_ligne": l["date"]}
            phrases = sn.lire_phrases_concepts(p, 1)
    except GardeArret as e:
        raise RefusPasse(f"entrée illisible ou sceau faux : {e}") from None
    if not jeux and phrases is None:
        raise RefusPasse("aucun jeu générique ni jeu de phrases des concepts au registre : rien à éprouver")
    return {"jeux": jeux, "phrases": phrases, "fichiers": fichiers}


# ---------------------------------------------------------------------------------------------------------------------- passe
def _juger_memoire(mesure: dict, octets_etape_a: int, mode: str, octets_notation: int | None = None) -> tuple[dict, str | None]:
    hote, carte = mesure["hote"], mesure["carte"]
    besoin = int(FACTEUR_COPIES * octets_etape_a)
    jugement = {"activations_etape_a_octets": int(octets_etape_a), "facteur_copies": FACTEUR_COPIES, "besoin_hote_octets": besoin,
                "part_hote_max": PART_HOTE_MAX, "part_carte_max": PART_CARTE_MAX, **mesure}
    if octets_notation is not None:                     # DF-04 : notation, une couche à la fois, toutes les actions notées
        jugement.update(notation_octets=int(octets_notation), besoin_notation_octets=int(FACTEUR_COPIES * octets_notation))
    if hote.get("disponible") is None:
        return jugement, "mémoire de l'hôte illisible (/proc/meminfo) : la garde de mémoire ne peut être jugée"
    if besoin > PART_HOTE_MAX * hote["disponible"]:
        return jugement, (f"mémoire de l'hôte : l'étape A garderait ≈ {besoin / 2**30:.2f} Gio d'activations (copies comprises) pour "
                          f"{hote['disponible'] / 2**30:.2f} Gio disponibles (part maximale {PART_HOTE_MAX})")
    if octets_notation is not None and FACTEUR_COPIES * octets_notation > PART_HOTE_MAX * hote["disponible"]:
        return jugement, (f"mémoire de la notation : une couche de toutes les actions notées ≈ {FACTEUR_COPIES * octets_notation / 2**30:.2f} "
                          f"Gio (copies comprises) pour {hote['disponible'] / 2**30:.2f} Gio disponibles (part maximale {PART_HOTE_MAX})")
    if carte is None:
        if mode == "reel":
            return jugement, "mode réel sans carte visible (torch.cuda.is_available() faux) : la mémoire de la carte ne peut être jugée"
        jugement["carte_jugee"] = "sans objet : aucune carte (mode jouet)"
        return jugement, None
    if "illisible" in carte:
        return jugement, f"mémoire de la carte illisible ({carte['illisible']})"
    if carte["pic_reserve"] > PART_CARTE_MAX * carte["totale"]:
        return jugement, (f"mémoire de la carte : pic réservé {carte['pic_reserve'] / 2**30:.2f} Gio pour {carte['totale'] / 2**30:.2f} "
                          f"Gio (part maximale {PART_CARTE_MAX})")
    return jugement, None


def octets_notation(racine: Path, run_t06: str, largeur: int) -> dict:
    """DF-04 : mémoire de la notation de l'étape A (`lecture_v2.noter` charge, pour une couche, les activations de toutes les actions
    notées, en float32) : 4 × largeur × somme des jetons notés, lue dans `donnees/<run>/mesures-t06.npz` (sceau vérifié ; seule la
    colonne `jetons_notes` est lue). Illisible → `GardeArret` (aucun repli silencieux)."""
    chemin = Path(racine) / "donnees" / run_t06 / "mesures-t06.npz"
    try:
        rg.sceau_conforme(chemin)
        with np.load(chemin) as z:
            j = np.asarray(z["jetons_notes"], dtype=np.int64)
    except GardeArret:
        raise
    except (OSError, ValueError, KeyError) as e:
        raise GardeArret(f"mesures de la course illisibles ({type(e).__name__}) : mémoire de la notation non estimable") from None
    notes = j[j > 0]
    return {"actions_notees": int(notes.size), "jetons_notes": int(notes.sum()), "octets": int(OCTETS_FLOAT32 * int(largeur) * int(notes.sum()))}


def passe_a_blanc(racine: Path, registre: Path, config: dict, run_t06: str, racine_sortie: Path | None = None,
                  instant: int | None = None, extracteur=None, mesure=sonde_memoire) -> dict:
    """Passe à blanc (docstring du module). Rend {issue, motif, chemin, sha256, sortie}. `RefusPasse` avant tout calcul (code 2) ;
    sinon la sortie est écrite et scellée, issue « tenue » ou « arrêt »."""
    from .lecture_v2 import empreinte_canonique, exiger_configuration, extracteur_de_la_course
    racine, registre = Path(racine), Path(registre)
    racine_sortie = Path(racine_sortie) if racine_sortie else racine
    instant = int(time.time()) if instant is None else int(instant)
    try:
        exiger_configuration(config)
    except GardeArret as e:
        raise RefusPasse(f"configuration : {e}") from None
    try:
        depot = {k: v for k, v in etat_git(racine).items() if k != "statut"}
    except GardeArret as e:
        raise RefusPasse(f"dépôt de la racine : {e}") from None
    mode = config["mode"]
    code_t07 = None
    if config["code_t07_exige"]:                        # DF-02 : CODE-T07 contrôlée avant la passe (refus, code 2)
        from . import code_t07_v1 as ct
        from .lecture_v2 import lire_lignes_actuelles, premiere_ouverture_a
        ligne = lire_lignes_actuelles(registre, (rg.CODE_T07,)).get(rg.CODE_T07)
        if ligne is None:
            raise RefusPasse("CODE-T07 exigée (code_t07_exige vrai) et absente du registre")
        try:
            rg.sceau_conforme(racine / ligne["chemin"], ligne["sha256"])
            code_t07 = ct.controler_code(racine, ligne, premiere_ouverture_a(registre, run_t06))
        except GardeArret as e:
            raise RefusPasse(f"CODE-T07 : {e}") from None
    nom = time.strftime("%Y%m%d-%H%M%S", time.gmtime(instant)) + f"-passe-blanc-t07-{mode}"
    dossier = racine_sortie / DOSSIER / nom
    if dossier.exists():
        raise RefusPasse(f"{dossier} existe déjà (R12)")
    entrees = lire_entrees(racine, registre)
    couches = [int(c) for c in config["couches"]]
    t0 = time.perf_counter()
    try:
        ext = extracteur if extracteur is not None else extracteur_de_la_course(racine, run_t06, config)
    except GardeArret as e:
        raise RefusPasse(f"modèle de la course : {e}") from None
    except (OSError, ValueError) as e:
        raise RefusPasse(f"modèle de la course introuvable dans le cache local ({type(e).__name__}: {str(e)[:200]})") from None
    duree_chargement = round(time.perf_counter() - t0, 3)
    memoire_chargement = mesure()
    motifs: list[str] = []
    # (2) frontière et gabarit : tokeniseur seul, tous les enregistrements
    t0 = time.perf_counter()
    controles = {n: controler_jeu(ext, recs, sn.EMPAN_DE_JEU[recs[0]["jeu"]]) for n, recs in entrees["jeux"].items()}
    jetons_phr = []
    if entrees["phrases"]:
        fl = entrees["phrases"]["format_lecture"]
        for c in sorted(entrees["phrases"]["concepts"]):
            for r in sorted(entrees["phrases"]["concepts"][c], key=lambda x: x["indice"]):
                for cote in ("phrase_concept", "phrase_neutre"):
                    try:
                        jetons_phr.append((c, r["indice"], cote, jetons_phrase(ext, r[cote], fl)))
                    except GardeArret as e:
                        motifs.append(f"phrase {c}/{r['indice']}/{cote} : {e}")
                        jetons_phr.append((c, r["indice"], cote, 0))
    # (2 bis) garde d'identité des jeux (E-8, D-2 (a) ; consigne v3 des jeux, § 2) : remesure des jetons contre le journal du script
    remesure = {}
    for n, recs in entrees["jeux"].items():
        try:
            remesure[n] = cj.remesurer_jetons(n, recs, racine / entrees["fichiers"][n]["chemin"], lambda x: len(_ids(ext.fmt.tok, x)), mode)
        except GardeArret as e:
            remesure[n] = {"etat": f"écart : {e}"}
            motifs.append(str(e))
    duree_tokeniseur = round(time.perf_counter() - t0, 3)
    for n, c in controles.items():
        if c["fautes"]:
            motifs.append(f"jeu {n} : {len(c['fautes'])} enregistrement(s) en faute (frontière ou gabarit), premier : {c['fautes'][0]['faute']}")
    # (1) extraction de l'échantillon, au modèle
    passes, pris, largeur = [], {}, None
    for n, recs in entrees["jeux"].items():
        empan = sn.EMPAN_DE_JEU[recs[0]["jeu"]]
        idx = echantillon_jeu(recs, controles[n]["jetons_conversation"])
        pris[n] = [{"indice": i, "tache": recs[i]["tache"], "paire": recs[i]["paire"], "membre": recs[i]["membre"]} for i in idx]
        for i in idx:
            r = recs[i]
            for e in ([empan, "action_entiere"] if n == "JC" else [empan]):
                t0 = time.perf_counter()
                try:
                    a = ext.reponse(r["contexte_systeme"], r["observation"], r["reponse"], e, r["position_cost"])
                except GardeArret as err:
                    motifs.append(f"extraction de l'échantillon, jeu {n}, enregistrement {i} ({e}) : {err}")
                    continue
                d = time.perf_counter() - t0
                formes = {c: list(a[c].shape) for c in couches}
                largeur = largeur or int(a[couches[0]].shape[1])
                attendu = controles[n]["jetons_action_entiere" if e == "action_entiere" else "jetons_empan"][i]
                if any(s[0] != attendu for s in formes.values()):
                    motifs.append(f"extraction de l'échantillon, jeu {n}, enregistrement {i} ({e}) : {formes} jetons pour {attendu} "
                                  "attendus au tokeniseur")
                passes.append({"objet": f"{n}/{i}/{e}", "jetons_conversation": controles[n]["jetons_conversation"][i],
                               "jetons_empan": attendu, "duree_s": round(d, 4)})
    if entrees["phrases"]:
        fl = entrees["phrases"]["format_lecture"]
        choisies = []
        for c in sorted(entrees["phrases"]["concepts"]):
            for r in sorted(entrees["phrases"]["concepts"][c], key=lambda x: x["indice"])[:PAIRES_PAR_CONCEPT]:
                choisies += [(c, r["indice"], "phrase_concept", r["phrase_concept"]), (c, r["indice"], "phrase_neutre", r["phrase_neutre"])]
        if jetons_phr:
            c, ind, cote, _ = jetons_phr[int(np.argmax([x[3] for x in jetons_phr]))]
            r = next(x for x in entrees["phrases"]["concepts"][c] if x["indice"] == ind)
            if (c, ind, cote, r[cote]) not in choisies:
                choisies.append((c, ind, cote, r[cote]))
        pris["phrases"] = [{"concept": c, "indice": ind, "cote": cote} for c, ind, cote, _ in choisies]
        for c, ind, cote, texte in choisies:
            t0 = time.perf_counter()
            try:
                a = ext.phrase(texte, fl)
            except GardeArret as err:
                motifs.append(f"extraction de l'échantillon, phrase {c}/{ind}/{cote} : {err}")
                continue
            largeur = largeur or int(a[couches[0]].shape[1])
            passes.append({"objet": f"phrase/{c}/{ind}/{cote}", "jetons_empan": int(a[couches[0]].shape[0]),
                           "duree_s": round(time.perf_counter() - t0, 4)})
    # (3) durée et mémoire
    n_passes_a = sum(c["n"] * (2 if n == "JC" else 1) for n, c in controles.items()) + len(jetons_phr)
    jetons_a = (sum(sum(c["jetons_empan"]) for c in controles.values()) + sum(controles["JC"]["jetons_action_entiere"] if "JC" in controles else [])
                + sum(x[3] for x in jetons_phr))
    durees = [p["duree_s"] for p in passes]
    base = durees[1:] if len(durees) > 1 else durees
    estimation = round(sum(base) / len(base) * n_passes_a, 1) if base else None   # durée par passe (jamais des jetons)
    octets_a = OCTETS_FLOAT32 * len(couches) * int(largeur or 0) * int(jetons_a)
    notation = None
    try:
        notation = octets_notation(racine, run_t06, int(largeur or 0))
    except GardeArret as e:
        motifs.append(f"mémoire de la notation non estimable : {e}")
    memoire, motif_memoire = _juger_memoire(mesure(), octets_a, mode, notation["octets"] if notation else None)
    if notation:
        memoire["notation"] = notation
    if largeur is None:
        motifs.append("aucune passe de l'échantillon menée : largeur des activations inconnue, mémoire de l'étape A non estimable")
    if motif_memoire:
        motifs.append(motif_memoire)
    frontiere = {n: {"enregistrements": c["n"], **c["frontiere"], "fautes": len([f for f in c["fautes"] if f["faute"].startswith("F")])}
                 for n, c in controles.items() if c["frontiere"] is not None}
    sortie = {
        "nature": NATURE, "version": VERSION, "commande": COMMANDE, "instant": rg.date_utc(instant), "mode": mode, "run_t06": run_t06,
        "depot": depot,
        "configuration": {"empreinte_canonique": empreinte_canonique(config), "couches": couches, "registre": str(registre)},
        "versions": versions(), "fichiers": entrees["fichiers"],
        "echantillon": {"regle": REGLE_ECHANTILLON, "pris": pris},
        "gabarit": {"par_jeu": {n: {"enregistrements": c["n"], "fautes": len([f for f in c["fautes"] if f["faute"].startswith("gabarit")])}
                                for n, c in controles.items()},
                    "tient": not any(f["faute"].startswith("gabarit") for c in controles.values() for f in c["fautes"])},
        "remesure_jetons": remesure,
        "frontiere": {"regle": "F1 à F4 (docstring de passe_blanc_v1), tous les enregistrements des jeux lus avant le champ",
                      "par_jeu": frontiere, "tient": not any(f["faute"].startswith("F") for c in controles.values() for f in c["fautes"]),
                      "fautes": [{"jeu": n, **f} for n, c in controles.items() for f in c["fautes"]][:FAUTES_ECRITES]},
        "durees": {"chargement_modele_s": duree_chargement, "tokeniseur_s": duree_tokeniseur, "passes": passes,
                   "passes_etape_a": n_passes_a, "jetons_etape_a": int(jetons_a),
                   "extraction_etape_a_estimee_s": estimation,
                   "note": "estimation : moyenne des passes de l'échantillon hors la première × passes de l'extraction de l'étape A ; "
                           "rapportée, jamais une garde (aucun couperet de temps)"},
        "memoire": {"apres_chargement": memoire_chargement, "jugement": memoire,
                    "tient": motif_memoire is None and largeur is not None and notation is not None},
        "code_t07": code_t07,
        "issue": "tenue" if not motifs else "arrêt", "motifs": motifs,
    }
    dossier.mkdir(parents=True)
    chemin = dossier / FICHIER
    chemin.write_text(json.dumps(sortie, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    sha = sceller(chemin)
    return {"issue": sortie["issue"], "motifs": motifs, "chemin": str(chemin.relative_to(racine_sortie)), "sha256": sha, "sortie": sortie}


def main(argv: list[str]) -> int:
    from .lecture_v2 import charger_configuration
    p = argparse.ArgumentParser(prog=COMMANDE, description=__doc__.splitlines()[0])
    p.add_argument("racine")
    p.add_argument("run_t06")
    p.add_argument("config_t07")
    p.add_argument("--registre", default=None, help="défaut : clé `registre` de la configuration")
    p.add_argument("--racine-sortie", default=None)
    a = p.parse_args(argv)
    try:
        config = charger_configuration(Path(a.config_t07))
        registre = Path(a.registre) if a.registre else Path(a.racine) / config["registre"]
        r = passe_a_blanc(Path(a.racine), registre, config, a.run_t06, Path(a.racine_sortie) if a.racine_sortie else None)
    except GardeArret as err:
        print(f"REFUS (passe à blanc, rien d'écrit) : {err}", file=sys.stderr)
        return CODE_REFUS
    s = r["sortie"]
    j = s["memoire"]["jugement"]
    print(f"passe à blanc : {r['issue']} ; sortie {r['chemin']} {r['sha256']}")
    print(f"frontière : {json.dumps(s['frontiere']['par_jeu'], ensure_ascii=False)} ; gabarit : {json.dumps(s['gabarit']['par_jeu'], ensure_ascii=False)}")
    print(f"durées : chargement {s['durees']['chargement_modele_s']} s, {len(s['durees']['passes'])} passes, extraction de l'étape A estimée "
          f"{s['durees']['extraction_etape_a_estimee_s']} s pour {s['durees']['passes_etape_a']} passes ; mémoire : besoin de l'hôte "
          f"{j['besoin_hote_octets']} octets, disponible {j['hote'].get('disponible')}, carte {j['carte']}")
    if r["issue"] != "tenue":
        for m in r["motifs"]:
            print(f"ARRÊT (passe à blanc) : {m}", file=sys.stderr)
        return CODE_ARRET
    return CODE_OK
