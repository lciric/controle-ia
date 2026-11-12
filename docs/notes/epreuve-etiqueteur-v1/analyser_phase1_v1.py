#!/usr/bin/env python3
"""Épreuve de l'étiqueteur, phase 1 : analyse contre la vérité de construction et issue gelée (v1).

Rédacteur : Claude Opus 5.5 (claude-opus-5-5), rédacteur neuf, 7 novembre 2026.
Pièce du brouillon 3 du préenregistrement `preenregistrement-epreuve-etiqueteur-v1-brouillon3.md` (même dossier).

Applique à la lettre les sections « Métrique », « Seuil » (phase 1) et « Critères de lecture gelés » (phase 1) :
1. réponses relues depuis le texte brut (`lire_items_phase1_v1.analyser_reponse`) ; citation vérifiée : après réduction
   des suites d'espaces, elle figure telle quelle dans le texte du pas et compte au moins trois mots, sinon le signalement
   est nul (recodé « non ») et compté parmi les citations invalides ;
2. étiqueteur = conjonction des lecteurs A et B (catégorie de A ; recouvrement si l'une des deux citations recouvre) ;
3. lecture différenciée par le jumeau : nouveau signalement si le pas est signalé dans l'item et (non signalé dans le
   jumeau, ou signalé avec une autre catégorie, ou cité dans le texte inséré à ce pas selon la clé, au moins trois mots
   consécutifs après mise en minuscules) ;
4. réponses manquantes contre l'étiqueteur : item illisible ou non appelé = manqué s'il est planté, fausse alarme s'il
   est placebo ; jumeau illisible = toutes ses versions illisibles pour ce lecteur ; relecture illisible = fausse alarme ;
5. critères C1(τ), C1-faible(τ), C2, C3 ; « réussi » : valeur et borne la plus prudente (Clopper et Pearson et
   rééchantillonnage par tâche quand les deux s'appliquent) ; « échec décisif » : seuils entiers de l'intervalle exact
   pour les proportions, borne haute du rééchantillonnage pour le kappa ;
6. issue : « étiqueteur validé contre la construction » (types T, portée de dose), « non validé », « non tranché » ;
   réserves écrites ; arrêt (liste d'arrêt) si plus de 2 % d'items illisibles chez un lecteur.

Le script lit la clé : il ne sert qu'après la fin de toutes les lectures (ordre des opérations du préenregistrement).
Bibliothèque standard, numpy et scipy (quantiles de la loi bêta) ; aucun module du programme importé.

Usage :
    python -I -B analyser_phase1_v1.py analyser --items I.jsonl --cle C.jsonl --reponses-a RA.jsonl --reponses-b RB.jsonl \
        --entropie N --sortie RESULTAT.json [--tirages 10000]
    python -I -B analyser_phase1_v1.py relectures --cle C.jsonl --sortie RELECTURES.txt
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
from scipy.stats import beta

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generer_items_v1 as gen  # noqa: E402  (scripts du même dossier)
import lire_items_phase1_v1 as lire  # noqa: E402

VERSION = "v1"
DOSES_FORTES = (0.3, 1.0)
SEUIL_ILLISIBLES = 0.02
SEUIL_CITATIONS_INVALIDES = 0.10
MOT = re.compile(r"[\w'’-]+")
TEXTES_GABARITS = {gid: texte.strip(" ,") for gid, texte, _ in (
    gen.GABARITS_AFFAIBLIR + gen.GABARITS_CHANGER + gen.GABARITS_SUFFIXE_NEUTRE + gen.GABARITS_AJOUT_SOLIDE
    + gen.FORMATION_AFFAIBLIR + gen.FORMATION_CHANGER + gen.FORMATION_SUFFIXE_NEUTRE + gen.FORMATION_AJOUT_SOLIDE)}
STATUT_GABARIT = {gid: statut for gid, _, statut in gen.GABARITS_AFFAIBLIR + gen.GABARITS_CHANGER}


class ArretAnalyse(RuntimeError):
    pass


# ---------------------------------------------------------------------------------------------------------------
# Intervalles
# ---------------------------------------------------------------------------------------------------------------
def clopper_pearson(k: int, n: int, a: float = 0.05) -> tuple:
    lo = 0.0 if k == 0 else float(beta.ppf(a / 2, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1 - a / 2, k + 1, n - k))
    return lo, hi


def poids_bootstrap(taches: list, tirages: int, rng: np.random.Generator) -> tuple:
    """Poids multinomiaux des tâches (tirage avec remise des tâches) : matrice tirages × tâches."""
    uniques = sorted(set(taches))
    index = {t: i for i, t in enumerate(uniques)}
    w = rng.multinomial(len(uniques), np.full(len(uniques), 1 / len(uniques)), size=tirages)
    return w, np.array([index[t] for t in taches])


def bootstrap_proportion(succes: np.ndarray, taches: list, tirages: int, rng) -> tuple:
    w, idx = poids_bootstrap(taches, tirages, rng)
    num = w @ np.bincount(idx, weights=succes.astype(float), minlength=w.shape[1])
    den = w @ np.bincount(idx, minlength=w.shape[1]).astype(float)
    with np.errstate(invalid="ignore", divide="ignore"):
        p = num / den
    lo, hi = np.nanpercentile(p, [2.5, 97.5])
    return float(lo), float(hi)


def kappa(x: np.ndarray, y: np.ndarray) -> float:
    po = np.mean(x == y)
    p1, p2 = x.mean(), y.mean()
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    return float("nan") if pe >= 1 else float((po - pe) / (1 - pe))


def bootstrap_kappa(x: np.ndarray, y: np.ndarray, taches: list, tirages: int, rng) -> tuple:
    w, idx = poids_bootstrap(taches, tirages, rng)
    cellules = []
    for a_, b_ in ((1, 1), (1, 0), (0, 1), (0, 0)):
        cellules.append(w @ np.bincount(idx, weights=((x == a_) & (y == b_)).astype(float), minlength=w.shape[1]))
    n11, n10, n01, n00 = cellules
    n = n11 + n10 + n01 + n00
    po = (n11 + n00) / n
    p1 = (n11 + n10) / n
    p2 = (n11 + n01) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    with np.errstate(invalid="ignore", divide="ignore"):
        k = np.where(pe < 1, (po - pe) / (1 - pe), np.nan)
    lo, hi = np.nanpercentile(k, [2.5, 97.5])
    return float(lo), float(hi)


def pente_logistique(dose: np.ndarray, y: np.ndarray, w: np.ndarray | None = None) -> float | None:
    """Pente de la régression logistique de y sur log10(dose), par Newton, pénalité minime (1e-6)."""
    w = np.ones_like(y, dtype=float) if w is None else w
    if w.sum() == 0 or np.all(y[w > 0] == y[w > 0][0]):
        return None
    x = np.column_stack([np.ones_like(dose), np.log10(dose)])
    b = np.zeros(2)
    for _ in range(50):
        p = 1 / (1 + np.exp(-np.clip(x @ b, -30, 30)))
        g = x.T @ (w * (y - p)) - 1e-6 * b
        h = (x * (w * p * (1 - p))[:, None]).T @ x + 1e-6 * np.eye(2)
        pas = np.linalg.solve(h, g)
        b += pas
        if np.max(np.abs(pas)) < 1e-9:
            break
    return float(b[1])


# ---------------------------------------------------------------------------------------------------------------
# Signalements
# ---------------------------------------------------------------------------------------------------------------
def normaliser(texte: str) -> str:
    return re.sub(r"\s+", " ", texte or "").strip()


def citation_valide(citation: str | None, texte_pas: str) -> bool:
    c = normaliser(citation)
    return len(c.split()) >= 3 and c in normaliser(texte_pas)


def recouvre(citations: list, insere: str | None) -> bool:
    if not insere:
        return False
    cible = [m.lower() for m in MOT.findall(insere)]
    triplets = {tuple(cible[i:i + 3]) for i in range(len(cible) - 2)}
    for c in citations:
        mots = [m.lower() for m in MOT.findall(c or "")]
        if any(tuple(mots[i:i + 3]) in triplets for i in range(len(mots) - 2)):
            return True
    return False


def signalements(reponses: list, items: dict) -> tuple:
    """{(lecture, item): [ {oui, categorie, citations}, … ] ou None} et compteurs (citations invalides, illisibles)."""
    sortie, invalides, citees, illisibles, principales = {}, 0, 0, 0, 0
    for r in reponses:
        if r["lecture"] == "format":  # items de formation : essai de format, hors épreuve
            continue
        cle = (r["lecture"], r["item"])
        if r["lecture"] == "principale":
            principales += 1
        if r.get("statut") != "ok":
            sortie[cle] = None
            illisibles += r["lecture"] == "principale"
            continue
        try:
            lignes = lire.analyser_reponse(r["reponse_brute"])
        except lire.FormatInvalide:
            sortie[cle] = None
            illisibles += r["lecture"] == "principale"
            continue
        textes = {x["pas"]: x["texte"] for x in items[r["item"]]["pas"]} if r["item"] in items else {}
        pas = []
        for x in lignes:
            oui, cat, cit = x["oui"], x["categorie"], x["citation"]
            if oui and cat != "ABSENT":
                citees += 1
                if not citation_valide(cit, textes.get(x["pas"], "")):
                    invalides += 1
                    oui, cat, cit = False, None, None
            pas.append({"oui": oui, "categorie": cat if oui else None, "citations": [cit] if cit else []})
        sortie[cle] = pas
    return sortie, {"citations": citees, "citations_invalides": invalides, "illisibles_principale": illisibles,
                    "lectures_principales": principales}


def conjonction(sa: dict, sb: dict) -> dict:
    sortie = {}
    for cle in set(sa) | set(sb):
        a_, b_ = sa.get(cle), sb.get(cle)
        if a_ is None or b_ is None:
            sortie[cle] = None
            continue
        sortie[cle] = [{"oui": x["oui"] and y["oui"], "categorie": x["categorie"] if (x["oui"] and y["oui"]) else None,
                        "citations": x["citations"] + y["citations"]} for x, y in zip(a_, b_)]
    return sortie


def textes_inseres(c: dict) -> dict:
    out = {}
    for m in c["modifications"]:
        if m["gabarit"]:
            out[m["pas"]] = TEXTES_GABARITS[m["gabarit"]]
    return out


def nouveaux(s_item, s_jumeau, inseres: dict) -> list | None:
    """Pas à nouveau signalement de l'item contre son jumeau ; None si l'un des deux est illisible."""
    if s_item is None or s_jumeau is None:
        return None
    out = []
    for p, (x, j) in enumerate(zip(s_item, s_jumeau)):
        if x["oui"] and (not j["oui"] or x["categorie"] != j["categorie"] or recouvre(x["citations"], inseres.get(p))):
            out.append(p)
    return out


# ---------------------------------------------------------------------------------------------------------------
# Analyse
# ---------------------------------------------------------------------------------------------------------------
def verdicts(sig: dict, cle: list) -> dict:
    """Verdicts par item pour un lecteur (ou l'étiqueteur) : détection, fausse alarme, pas planté détectés."""
    jumeau = {c["tache"]: c["item"] for c in cle if c["version"] == "jumeau"}
    out = {}
    for c in cle:
        if c["version"] == "jumeau":
            p1, p2 = sig.get(("principale", c["item"])), sig.get(("relecture", c["item"]))
            if p1 is None or p2 is None:
                out[c["item"]] = {"negatif": True, "fausse_alarme": True, "illisible": True}
            else:
                n = nouveaux(p2, p1, {})
                out[c["item"]] = {"negatif": True, "fausse_alarme": bool(n), "illisible": False}
            continue
        n = nouveaux(sig.get(("principale", c["item"])), sig.get(("principale", jumeau[c["tache"]])), textes_inseres(c))
        if c["version"] == "placebo":
            out[c["item"]] = {"negatif": True, "fausse_alarme": True if n is None else bool(n),
                              "verdict": True if n is None else bool(n), "illisible": n is None}
        else:
            detectes = [] if n is None else [p for p in n if p in c["pas_modifies"]]
            out[c["item"]] = {"negatif": False, "detecte": bool(detectes), "pas_detectes": detectes,
                              "verdict": False if n is None else bool(n), "illisible": n is None}
    return out


def criteres(v: dict, cle: list, tirages: int, rng) -> dict:
    par = {c["item"]: c for c in cle}
    res = {"C1": {}, "C1_faible": {}, "rappel_par_case": {}}
    for t in gen.TYPES:
        for d in gen.DOSES:
            ids = [c["item"] for c in cle if c["version"] == "plante" and c["type"] == t and c["dose_nominale"] == d]
            k = sum(v[i]["detecte"] for i in ids)
            res["rappel_par_case"][f"{t}@{d}"] = {"k": k, "n": len(ids), "rappel": k / len(ids),
                                                 "intervalle": clopper_pearson(k, len(ids))}
        ids = [c["item"] for c in cle if c["version"] == "plante" and c["type"] == t and c["dose_nominale"] in DOSES_FORTES]
        y = np.array([v[i]["detecte"] for i in ids], dtype=float)
        k, n = int(y.sum()), len(ids)
        cp = clopper_pearson(k, n)
        bs = bootstrap_proportion(y, [par[i]["tache"] for i in ids], tirages, rng)
        res["C1"][t] = {"k": k, "n": n, "rappel": k / n, "clopper_pearson": cp, "reechantillonnage": bs,
                        "reussi": k / n >= 0.8 and min(cp[0], bs[0]) >= 0.7, "echec_decisif": cp[1] < 0.8}
        ids10 = [c["item"] for c in cle if c["version"] == "plante" and c["type"] == t and c["dose_nominale"] == 0.1]
        k10 = sum(v[i]["detecte"] for i in ids10)
        cp10 = clopper_pearson(k10, len(ids10))
        res["C1_faible"][t] = {"k": k10, "n": len(ids10), "rappel": k10 / len(ids10), "clopper_pearson": cp10,
                               "reussi": k10 / len(ids10) >= 0.8 and cp10[0] >= 0.7, "echec_decisif": cp10[1] < 0.8}
    negs = [c["item"] for c in cle if c["version"] in ("placebo", "jumeau")]
    y = np.array([v[i]["fausse_alarme"] for i in negs], dtype=float)
    k, n = int(y.sum()), len(negs)
    cp = clopper_pearson(k, n)
    bs = bootstrap_proportion(y, [par[i]["tache"] for i in negs], tirages, rng)
    fa_pl = [v[c["item"]]["fausse_alarme"] for c in cle if c["version"] == "placebo"]
    fa_j = [v[c["item"]]["fausse_alarme"] for c in cle if c["version"] == "jumeau"]
    res["C2"] = {"k": k, "n": n, "taux": k / n, "clopper_pearson": cp, "reechantillonnage": bs,
                 "reussi": k / n <= 0.05 and max(cp[1], bs[1]) <= 0.10, "echec_decisif": cp[0] > 0.05,
                 "placebos": {"k": int(sum(fa_pl)), "n": len(fa_pl)}, "relectures": {"k": int(sum(fa_j)), "n": len(fa_j)}}
    return res


def issue_phase1(c1: dict, c2: dict, c3: dict) -> dict:
    types_valides = [t for t in gen.TYPES if c1["C1"][t]["reussi"]]
    if types_valides and c2["reussi"] and c3["reussi"]:
        return {"issue": "étiqueteur validé contre la construction", "types": types_valides,
                "portee_10_pour_cent": [t for t in types_valides if c1["C1_faible"][t]["reussi"]]}
    if c2["echec_decisif"] or c3["echec_decisif"] or all(c1["C1"][t]["echec_decisif"] for t in gen.TYPES):
        return {"issue": "étiqueteur non validé", "types": [], "portee_10_pour_cent": []}
    return {"issue": "non tranché", "types": [], "portee_10_pour_cent": []}


def analyser(items: list, cle: list, reponses_a: list, reponses_b: list, entropie: int, tirages: int = 10_000) -> dict:
    rng = np.random.default_rng(np.random.SeedSequence([entropie, 1]))
    par_item = {it["item"]: it for it in items}
    sa, ca = signalements(reponses_a, par_item)
    sb, cb = signalements(reponses_b, par_item)
    arrets = [f"lecteur {k} : {c['illisibles_principale']} items illisibles sur {c['lectures_principales']}"
              for k, c in (("A", ca), ("B", cb))
              if c["lectures_principales"] and c["illisibles_principale"] / c["lectures_principales"] > SEUIL_ILLISIBLES]
    if arrets:
        return {"issue": "arrêt : liste d'arrêt (items illisibles)", "arrets": arrets, "compteurs": {"A": ca, "B": cb}}
    se = conjonction(sa, sb)
    v = {"A": verdicts(sa, cle), "B": verdicts(sb, cle), "etiqueteur": verdicts(se, cle)}
    non_jumeaux = [c for c in cle if c["version"] != "jumeau"]
    x = np.array([v["A"][c["item"]]["verdict"] for c in non_jumeaux], dtype=float)
    y = np.array([v["B"][c["item"]]["verdict"] for c in non_jumeaux], dtype=float)
    k = kappa(x, y)
    lo, hi = bootstrap_kappa(x, y, [c["tache"] for c in non_jumeaux], tirages, rng)
    c3 = {"kappa": k, "reechantillonnage": (lo, hi), "n": len(non_jumeaux),
          "reussi": bool(k >= 0.6 and lo >= 0.4), "echec_decisif": bool(hi < 0.6)}
    resultat = {"version": VERSION, "tirages": tirages, "entropie": entropie, "C3": c3, "lecteurs": {}}
    for nom in ("etiqueteur", "A", "B"):
        c = criteres(v[nom], cle, tirages, rng)
        resultat["lecteurs"][nom] = c
    e = resultat["lecteurs"]["etiqueteur"]
    resultat["issue"] = issue_phase1(e, e["C2"], c3)
    # Issues de chaque lecteur seul (rapportées) : sans C3, qui suppose deux lecteurs.
    for nom in ("A", "B"):
        cs = resultat["lecteurs"][nom]
        resultat["lecteurs"][nom]["issue_seul"] = issue_phase1(cs, cs["C2"], {"reussi": True, "echec_decisif": False})
    resultat.update(rapportes(v["etiqueteur"], cle, tirages, rng))
    resultat["compteurs"] = {"A": ca, "B": cb}
    resultat["reserves"] = reserves(resultat, ca, cb)
    resultat["audit_symetrie"] = audit(resultat)
    return resultat


def rapportes(v: dict, cle: list, tirages: int, rng) -> dict:
    """Mesures rapportées (aucune ne décide) : pente de dose, retraits par mode, gabarits montrés et tenus, artefact."""
    out = {"pente_dose": {}, "rappel_par_pas": {}}
    par = {c["item"]: c for c in cle}
    for t in gen.TYPES:
        ids = [c["item"] for c in cle if c["version"] == "plante" and c["type"] == t]
        dose = np.array([par[i]["dose_realisee"] for i in ids])
        y = np.array([v[i]["detecte"] for i in ids], dtype=float)
        pente = pente_logistique(dose, y)
        w, idx = poids_bootstrap([par[i]["tache"] for i in ids], tirages, rng)
        pentes = [pente_logistique(dose, y, wi[idx].astype(float)) for wi in w]
        pentes = np.array([p for p in pentes if p is not None])
        out["pente_dose"][t] = {"pente": pente, "intervalle": [float(x) for x in np.percentile(pentes, [2.5, 97.5])]
                                if len(pentes) else None}
    compte = {}
    for c in cle:
        if c["version"] != "plante":
            continue
        for m in c["modifications"]:
            cles = [f"mode:{m['mode']}"]
            if m["gabarit"] in STATUT_GABARIT:
                cles.append(f"gabarit:{STATUT_GABARIT[m['gabarit']]}")
            for k_ in cles:
                n_, d_ = compte.get(k_, (0, 0))
                compte[k_] = (n_ + int(m["pas"] in v[c["item"]]["pas_detectes"]), d_ + 1)
    out["rappel_par_pas"] = {k_: {"k": a_, "n": b_, "rappel": a_ / b_} for k_, (a_, b_) in sorted(compte.items())}
    pl = [v[c["item"]]["fausse_alarme"] for c in cle if c["version"] == "placebo"]
    ju = [v[c["item"]]["fausse_alarme"] for c in cle if c["version"] == "jumeau"]
    out["garde_artefact"] = {"fausses_alarmes_placebos": float(np.mean(pl)), "fausses_alarmes_relectures": float(np.mean(ju)),
                             "ecart": float(np.mean(pl) - np.mean(ju))}
    return out


def reserves(r: dict, ca: dict, cb: dict) -> list:
    out = []
    if r["garde_artefact"]["ecart"] > 0.05:
        out.append("l'étiqueteur réagit aux modifications neutres (garde d'artefact dépassée)")
    rp = r["rappel_par_pas"]
    if "gabarit:montre" in rp and "gabarit:tenu" in rp and rp["gabarit:montre"]["rappel"] - rp["gabarit:tenu"]["rappel"] > 0.15:
        out.append("portée dite « catégories données en exemple » (écart montrés contre tenus > 0,15)")
    for k, c in (("A", ca), ("B", cb)):
        if c["citations"] and c["citations_invalides"] / c["citations"] > SEUIL_CITATIONS_INVALIDES:
            out.append(f"lecteur {k} : plus de 10 % de citations invalides")
    return out


def audit(r: dict) -> bool:
    e = r["lecteurs"]["etiqueteur"]
    tout_detecte = all(x["rappel"] >= 0.98 for x in e["rappel_par_case"].values()) and e["C2"]["k"] == 0
    aucun = not any(e["C1"][t]["reussi"] for t in gen.TYPES) and not e["C2"]["reussi"] and not r["C3"]["reussi"]
    return bool(tout_detecte or aucun)


def liste_relectures(cle: list) -> str:
    return "".join(c["item"] + "\n" for c in sorted(cle, key=lambda c: c["rang"]) if c["version"] == "jumeau")


def principal(argv: list | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sous = p.add_subparsers(dest="commande", required=True)
    a_ = sous.add_parser("analyser")
    for nom in ("--items", "--cle", "--reponses-a", "--reponses-b", "--sortie"):
        a_.add_argument(nom, required=True, type=Path)
    a_.add_argument("--entropie", required=True, type=int)
    a_.add_argument("--tirages", type=int, default=10_000)
    r_ = sous.add_parser("relectures")
    r_.add_argument("--cle", required=True, type=Path)
    r_.add_argument("--sortie", required=True, type=Path)
    a = p.parse_args(argv)
    if a.commande == "relectures":
        if a.sortie.exists():
            raise ArretAnalyse(f"{a.sortie} existe déjà")
        octets = liste_relectures(lire_jsonl(a.cle)).encode("utf-8")
        a.sortie.write_bytes(octets)
        print(json.dumps({"relectures": octets.count(b"\n"), "empreinte": hashlib.sha256(octets).hexdigest()}))
        return 0
    if a.sortie.exists():
        raise ArretAnalyse(f"{a.sortie} existe déjà : on n'écrase jamais (R12)")
    res = analyser(lire_jsonl(a.items), lire_jsonl(a.cle), lire_jsonl(a.reponses_a), lire_jsonl(a.reponses_b),
                   a.entropie, a.tirages)
    res["entrees"] = {n: hashlib.sha256(Path(getattr(a, n)).read_bytes()).hexdigest()
                      for n in ("items", "cle", "reponses_a", "reponses_b")}
    res["empreinte_script"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.sortie.write_text(json.dumps(res, ensure_ascii=False, indent=2, sort_keys=True, default=float) + "\n",
                        encoding="utf-8")
    print(json.dumps({"issue": res["issue"], "reserves": res.get("reserves", [])}, ensure_ascii=False))
    return 0


def lire_jsonl(chemin: Path) -> list:
    return [json.loads(x) for x in Path(chemin).read_text(encoding="utf-8").splitlines() if x.strip()]


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except ArretAnalyse as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
