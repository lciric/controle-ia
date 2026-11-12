#!/usr/bin/env python3
"""Épreuve de l'étiqueteur, brouillon 2 : rendu de la consigne, mesure des consignes rendues, tirage de la phase 2 (v1).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 novembre 2026.
Pièce du brouillon 2 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon2.md` (même dossier).
Le générateur des items (`generer_items_v1.py`) n'est pas modifié ; ce script s'en sert pour le découpage des contrôles.

Trois usages :
1. `rendre_consigne(item, question)` : la consigne exacte d'un item, construite depuis le seul fichier des items
   (jamais depuis la clé) et le texte gelé de la question (annexe A du préenregistrement, entre ses deux marqueurs) ;
2. `jetons` : longueurs des consignes réellement rendues et de la réponse visible la plus longue que le format
   permet raisonnablement, pour le devis de la phase 1 ;
3. `phase2` : tirage stratifié d'environ 80 items pour les annotateurs (20 tâches ; par tâche : le jumeau, un placebo,
   deux versions plantées ; quotas fixés par case), avec un pas « surligné » par item pour la passe de réalisme ;
   graine `numpy.random.SeedSequence([entropie, 2])`, fixée au scellement, avant toute lecture.

Bibliothèque standard et numpy seulement ; aucun module du programme importé.

Usage :
    python -I -B epreuve_phases_v1.py jetons --items ITEMS.jsonl --question PREENREGISTREMENT.md
    python -I -B epreuve_phases_v1.py phase2 --items ITEMS.jsonl --cle CLE.jsonl --entropie N --sortie DOSSIER
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generer_items_v1 as gen  # noqa: E402  (script du même dossier, pas un module du programme)

VERSION = "v1"
N_TACHES_PHASE2 = 20
PLANTES_PAR_TACHE = 2
PLACEBOS_PAR_TACHE = 1
ECART_MIN_PHASE2 = 10
MARQUE_DEBUT = "<!-- debut-question-fermee -->"
MARQUE_FIN = "<!-- fin-question-fermee -->"


class ArretPhases(RuntimeError):
    """Arrêt explicite (R5)."""


# ---------------------------------------------------------------------------------------------------------------
# Consigne
# ---------------------------------------------------------------------------------------------------------------
def extraire_question(chemin: Path) -> str:
    """Texte gelé de la question : entre les deux marqueurs, sans la clôture de code."""
    texte = Path(chemin).read_text(encoding="utf-8")
    if texte.count(MARQUE_DEBUT) != 1 or texte.count(MARQUE_FIN) != 1:
        raise ArretPhases("marqueurs de la question absents ou en double")
    bloc = texte.split(MARQUE_DEBUT, 1)[1].split(MARQUE_FIN, 1)[0]
    m = re.fullmatch(r"\s*```text\n(.*)\n```\s*", bloc, re.S)
    if not m:
        raise ArretPhases("bloc de la question mal formé")
    question = m.group(1)
    if question.count("<ENONCE>") != 1 or question.count("<PLAN>") != 1:
        raise ArretPhases("emplacements <ENONCE> et <PLAN> absents ou en double")
    return question


def rendre_plan(item: dict) -> str:
    """« STEP n: », saut de ligne, texte du pas ; une ligne vide entre deux pas."""
    pas = sorted(item["pas"], key=lambda x: x["pas"])
    if [x["pas"] for x in pas] != list(range(gen.N_PAS)):
        raise ArretPhases(f"item {item.get('item')} : pas incomplets")
    return "\n\n".join(f"STEP {x['pas']}:\n{x['texte']}" for x in pas)


def rendre_consigne(item: dict, question: str) -> str:
    """Consigne d'un item. N'accepte que les champs du fichier des items : toute autre clé arrête (garde de fuite)."""
    if set(item) != {"item", "rang", "tache", "enonce", "pas"}:
        raise ArretPhases(f"item {item.get('item')} : champs inattendus {sorted(set(item))}")
    if not item["enonce"]:
        raise ArretPhases(f"item {item['item']} : énoncé vide")
    return question.replace("<ENONCE>", item["enonce"]).replace("<PLAN>", rendre_plan(item))


def reponse_visible_longue(item: dict) -> str:
    """Réponse la plus longue que le format admet sans abus : chaque pas « YES | UNINFORMATIVE » avec, pour citation,
    tout le contenu de ses champs CONTROLS (ou « ABSENT » s'il n'en a pas)."""
    lignes = []
    for x in sorted(item["pas"], key=lambda x: x["pas"]):
        blocs = gen.analyser_controles(x["texte"])
        contenu = " ".join(x["texte"][b.contenu:b.fin].strip() for b in blocs).strip()
        if contenu:
            lignes.append(f'STEP {x["pas"]}: YES | UNINFORMATIVE | "{contenu}"')
        else:
            lignes.append(f"STEP {x['pas']}: YES | ABSENT")
    return "\n".join(lignes)


def mesurer(items: list, question: str) -> dict:
    entree = np.array([len(rendre_consigne(it, question)) for it in items])
    sortie = np.array([len(reponse_visible_longue(it)) for it in items])

    def resume(a):
        return {"moyenne": float(a.mean()), "mediane": float(np.median(a)), "maximum": int(a.max()),
                "total": int(a.sum())}

    return {"items": len(items), "caracteres_consigne": resume(entree),
            "caracteres_reponse_visible_longue": resume(sortie)}


# ---------------------------------------------------------------------------------------------------------------
# Tirage de la phase 2
# ---------------------------------------------------------------------------------------------------------------
def strate(c: dict) -> str:
    if c["version"] == "jumeau":
        return "jumeau"
    if c["version"] == "placebo":
        return f"placebo@{c['dose_nominale']}"
    return f"{c['type']}@{c['dose_nominale']}"


def quotas(rng: np.random.Generator, n_taches: int) -> tuple:
    """Quotas des cases plantées (n_taches × 2 répartis sur 9 cases) et des doses de placebo (n_taches × 1 sur 3)."""
    cellules = [f"{t}@{d}" for d in gen.DOSES for t in gen.TYPES]
    total_p = n_taches * PLANTES_PAR_TACHE
    q_p = {c: total_p // len(cellules) for c in cellules}
    for k in rng.permutation(len(cellules))[: total_p % len(cellules)]:
        q_p[cellules[int(k)]] += 1
    doses = [f"placebo@{d}" for d in gen.DOSES]
    total_pl = n_taches * PLACEBOS_PAR_TACHE
    q_pl = {d: total_pl // len(doses) for d in doses}
    for k in rng.permutation(len(doses))[: total_pl % len(doses)]:
        q_pl[doses[int(k)]] += 1
    return q_p, q_pl


def _prendre(rng, candidats: list, restant: dict, deja: set):
    """Parmi les candidats dont la strate a encore du quota, celui de plus grand quota restant (hasard à égalité)."""
    possibles = [c for c in candidats if restant.get(strate(c), 0) > 0 and c["item"] not in deja]
    if not possibles:
        return None
    ordre = [possibles[int(i)] for i in rng.permutation(len(possibles))]
    ordre.sort(key=lambda c: -restant[strate(c)])
    return ordre[0]


def tirer_phase2(items: list, cle: list, entropie: int, n_taches: int = N_TACHES_PHASE2,
                 ecart_min: int = ECART_MIN_PHASE2) -> list:
    """Rend la liste ordonnée des items de la phase 2 : {item, rang_phase2, tache, strate, pas_surligne}."""
    rng = np.random.default_rng(np.random.SeedSequence([entropie, 2]))
    par_item = {it["item"]: it for it in items}
    par_tache = {}
    for c in cle:
        par_tache.setdefault(c["tache"], []).append(c)
    taches = sorted(par_tache)
    q_p, q_pl = quotas(rng, n_taches)
    choix = None
    for _ in range(2000):
        retenues = sorted(taches[int(i)] for i in rng.choice(len(taches), size=n_taches, replace=False))
        for _ in range(50):
            restant = dict(q_p) | dict(q_pl)
            selection = {}
            reussi = True
            for t in [retenues[int(i)] for i in rng.permutation(n_taches)]:
                cs = par_tache[t]
                pris = [c for c in cs if c["version"] == "jumeau"]
                for _k in range(PLANTES_PAR_TACHE):
                    c = _prendre(rng, [x for x in cs if x["version"] == "plante"], restant, {x["item"] for x in pris})
                    if c is None:
                        reussi = False
                        break
                    restant[strate(c)] -= 1
                    pris.append(c)
                if not reussi:
                    break
                c = _prendre(rng, [x for x in cs if x["version"] == "placebo"], restant, set())
                if c is None:
                    reussi = False
                    break
                restant[strate(c)] -= 1
                pris.append(c)
                selection[t] = pris
            if reussi and all(v == 0 for v in restant.values()):
                choix = selection
                break
        if choix:
            break
    if not choix:
        raise ArretPhases("tirage de la phase 2 impossible sous les quotas")
    ordre = gen.ordre_presentation(rng, {t: v for t, v in sorted(choix.items())}, ecart_min)
    sortie = []
    for rang, (t, k) in enumerate(ordre):
        c = choix[t][k]
        if c["version"] == "jumeau":
            textes = [x["texte"] for x in sorted(par_item[c["item"]]["pas"], key=lambda x: x["pas"])]
            eligibles = [p for p, tx in enumerate(textes) if gen.unites_substantielles(tx, gen.analyser_controles(tx))]
            pas_surligne = int(rng.choice(eligibles))
        else:
            pas_surligne = int(rng.choice(c["pas_modifies"]))
        sortie.append({"item": c["item"], "rang_phase2": rang + 1, "tache": t, "strate": strate(c),
                       "pas_surligne": pas_surligne})
    return sortie


def lire_jsonl(chemin: Path) -> list:
    return [json.loads(x) for x in Path(chemin).read_text(encoding="utf-8").splitlines() if x.strip()]


def principal(argv: list | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sous = p.add_subparsers(dest="commande", required=True)
    j = sous.add_parser("jetons")
    j.add_argument("--items", required=True, type=Path)
    j.add_argument("--question", required=True, type=Path)
    t = sous.add_parser("phase2")
    t.add_argument("--items", required=True, type=Path)
    t.add_argument("--cle", required=True, type=Path)
    t.add_argument("--entropie", required=True, type=int)
    t.add_argument("--sortie", required=True, type=Path)
    a = p.parse_args(argv)
    if a.commande == "jetons":
        print(json.dumps(mesurer(lire_jsonl(a.items), extraire_question(a.question)), ensure_ascii=False, indent=2))
        return 0
    tirage = tirer_phase2(lire_jsonl(a.items), lire_jsonl(a.cle), a.entropie)
    a.sortie.mkdir(parents=True, exist_ok=True)
    octets = gen.en_jsonl(tirage)
    empreinte = gen.ecrire(a.sortie, f"tirage-phase2-{VERSION}.jsonl", octets)
    # Rendu : nombre et empreinte seulement (le tirage dit les strates : il ne va jamais aux annotateurs).
    print(json.dumps({"items": len(tirage), "taches": len({x["tache"] for x in tirage}),
                      "empreinte": empreinte}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except (ArretPhases, gen.ArretGeneration) as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
