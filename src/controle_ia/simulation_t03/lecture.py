"""Lecture gelée de T0.3 : applique mécaniquement les critères du préenregistrement
(prereg/T0.3-simulation-lemme-theoreme-v1.md, section « Critères de lecture gelés »).

Verdict de cellule : « conforme », « contraire », « non concluant ».
Verdict de prédiction : « confirmée » (toutes conformes), « réfutée » (au moins une contraire),
« non concluante » (sinon). Une contraire statistique appelle une réplication (graine neuve,
5 × R) ; une contraire trajectorielle appelle un audit du code et de la preuve.
"""
from __future__ import annotations

import math

import numpy as np

from . import calibrage as cal
from .lois import facteur_variance_ar1

Z = 4.0                 # seuil Monte-Carlo, en écarts-types
SEUIL_P72 = 0.99        # P7.2 : e bilatéral sous tri croissant
BORNES_AUDIT = (0.3, 3.0)   # variance admise des écarts réduits (R4)
SYMETRIQUES = ("somme", "somme_bilat", "max", "e_terminal_ville")
ALPHA_DEFAUT = 0.05


def _v(p: float, R: int) -> float:
    """Variance d'une proportion, plancher d'un événement (évite un écart-type nul)."""
    return max(p * (1.0 - p), 1.0 / R) / R


def egal(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if abs(d) <= Z * se else "contraire"), d / se


def au_dessus(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if d > Z * se else "contraire" if d < -Z * se else "non concluant"), d / se


def en_dessous(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if d < -Z * se else "contraire" if d > Z * se else "non concluant"), d / se


def au_plus(p, R, p0, R0):
    d, se = p - p0, math.sqrt(_v(p, R) + _v(p0, R0))
    return ("conforme" if d <= Z * se else "contraire"), d / se


def theorie(p, R, p_th):
    se = math.sqrt(_v(p_th, R))
    return ("conforme" if abs(p - p_th) <= Z * se else "contraire"), (p - p_th) / se


def au_plus_valeur(p, R, v):
    se = math.sqrt(_v(v, R))
    return ("conforme" if p <= v + Z * se else "contraire"), (p - v) / se


def au_dessus_valeur(p, R, v):
    se = math.sqrt(_v(v, R))
    return ("conforme" if p > v + Z * se else "contraire" if p < v - Z * se else "non concluant"), (p - v) / se


def au_moins(p, R, v):
    se = math.sqrt(_v(v, R))
    return ("conforme" if p >= v - Z * se else "contraire"), (p - v) / se


def trajectoriel(violations: int):
    return ("conforme" if violations == 0 else "contraire"), None


BLOCS_DE = {"P1": ("P1a", "P1b"), "P2": ("P2",), "P3": ("P3", "P34"), "P4": ("P4", "P43"),
            "P5": ("P5_temps", "P5_agents"), "P6": ("P6",), "P7": ("P7",), "P8": ("P8",)}


def verdict(cellules: list[dict]) -> str:
    etats = [c["etat"] for c in cellules]
    if not etats:
        return "non concluante"
    if any(e == "contraire" for e in etats):
        return "réfutée"
    return "confirmée" if all(e == "conforme" for e in etats) else "non concluante"


class Lecteur:
    def __init__(self, resultats: dict, alpha: float = ALPHA_DEFAUT):
        self.r = resultats
        self.alpha = alpha
        self.predictions: dict[str, dict] = {}
        self.z_theorie: list[float] = []
        self.z_egalites: list[float] = []

    def cellule(self, pred: str, nom: str, fonction, *args, genre: str = "statistique", theorique: bool = False,
                egalite: bool = False, **details):
        etat, z = fonction(*args)
        if theorique and z is not None:
            p_th = args[-1]
            if 0.01 <= p_th <= 0.99:
                self.z_theorie.append(float(z))
        if egalite and z is not None:
            self.z_egalites.append(float(z))
        self.predictions.setdefault(pred, {"cellules": []})["cellules"].append(
            {"nom": nom, "etat": etat, "z": None if z is None else round(float(z), 3), "genre": genre, **details})

    def p0(self, cfg: str, alarme: str) -> tuple[float, int]:
        c = self.r["calibrage"][cfg]
        return c["alarmes_p0"][alarme] / c["R0"], c["R0"]

    # --- P1 ---
    def P1(self):
        a = self.alpha
        for g in self.r["P1a"]["groupes"]:
            n0, B, R = g["n0"], g["B"], g["R"]
            tag = f"{g['N']}x{g['T']}/B{B}"
            for c in g["cellules"]:
                v = c["disc_somme"] + c["disc_eterm"] + (1 if c["ecart_max"] > g["tolerance_ecart"] else 0)
                self.cellule("P1.1", f"{tag}/{c['schema']}/m{c['m']}/{c['genre']}", trajectoriel, v,
                             genre="trajectoriel", discordances_somme=c["disc_somme"],
                             discordances_eterm=c["disc_eterm"], ecart_max=c["ecart_max"])
            p_th = cal.puissance_somme(a, n0, B)
            self.cellule("P1.2", tag, theorie, g["alarmes_ref_somme"] / R, R, p_th, theorique=True,
                         p=g["alarmes_ref_somme"] / R, p_th=p_th)
        cel = self.r["P1b"]["cellules"]
        for c in cel:
            p_th = cal.puissance_somme(a, c["n0"], c["B"])
            self.cellule("P1.3", f"{c['N']}x{c['T']}/B{c['B']}", theorie, c["alarmes_somme"] / c["R"], c["R"], p_th,
                         theorique=True, p=c["alarmes_somme"] / c["R"], p_th=p_th)
        par = {(c["N"], c["T"], c["B"]): c for c in cel}
        Bs = sorted({c["B"] for c in cel})
        n0s = sorted({c["n0"] for c in cel if c["N"] == 1})
        for B in Bs:
            for n_a, n_b in zip(n0s[:-1], n0s[1:]):
                ca, cb = par[(1, n_a, B)], par[(1, n_b, B)]
                self.cellule("P1.3", f"décroissance/B{B}/{n_a}>{n_b}", au_dessus, ca["alarmes_somme"] / ca["R"], ca["R"],
                             cb["alarmes_somme"] / cb["R"], cb["R"])
            for c in cel:
                if c["N"] > 1 and c["B"] == B and (1, c["n0"], B) in par:
                    c1 = par[(1, c["n0"], B)]
                    self.cellule("P1.4", f"{c['N']}x{c['T']}~1x{c['n0']}/B{B}", egal, c["alarmes_somme"] / c["R"],
                                 c["R"], c1["alarmes_somme"] / c1["R"], c1["R"], egalite=True)

    # --- P2 ---
    def P2(self):
        a = self.alpha
        cel = self.r["P2"]["cellules"]
        p0, R0 = self.p0(self.r["P2"]["cfg"], "max")
        for c in cel:
            p_th = cal.puissance_max(a, c["n0"], c["B"], c["m"])
            self.cellule("P2.1", f"B{c['B']}/m{c['m']}", theorie, c["alarmes_max"] / c["R"], c["R"], p_th,
                         theorique=True, p=c["alarmes_max"] / c["R"], p_th=p_th)
        for B in sorted({c["B"] for c in cel}):
            seq = sorted([c for c in cel if c["B"] == B], key=lambda c: c["m"])
            for ca, cb in zip(seq[:-1], seq[1:]):
                self.cellule("P2.2", f"B{B}/m{cb['m']}≤m{ca['m']}", au_plus, cb["alarmes_max"] / cb["R"], cb["R"],
                             ca["alarmes_max"] / ca["R"], ca["R"])
            dern = seq[-1]
            self.cellule("P2.3", f"B{B}/m{dern['m']}", au_dessus, dern["alarmes_max"] / dern["R"], dern["R"], p0, R0)

    # --- P3 ---
    def P3(self):
        a = self.alpha
        for g in self.r["P3"]["groupes"]:
            tag = f"{g['N']}x{g['T']}/B{g['B']}"
            for m, viol in g["violations"].items():
                self.cellule("P3.1", f"{tag}/m{m}", trajectoriel, sum(viol.values()), genre="trajectoriel", **viol)
            taux = {(c["m"], c["calendrier"]): c["alarmes"] / g["R"] for c in g["cellules"]}
            for m in sorted({c["m"] for c in g["cellules"]}):
                for avant in ("debut", "uniforme"):
                    self.cellule("P3.2", f"{tag}/m{m}/{avant}>fin", au_dessus, taux[(m, avant)], g["R"],
                                 taux[(m, "fin")], g["R"])
            p_th = cal.borne_terminale(a, g["n0"], g["B"], g["rho"])
            self.cellule("P3.3", tag, theorie, g["alarmes_terminal"] / g["R"], g["R"], p_th, theorique=True,
                         p=g["alarmes_terminal"] / g["R"], p_th=p_th)
        for c in self.r["P34"]["cellules"]:
            R = c["R"]
            ref = c["comptes"]["e_unilat_cal"]["a_temps"] / R
            for a_ in ("page", "detecteur_e"):
                self.cellule("P3.4", f"B{c['B']}/m{c['m']}/{a_}>e_unilat_cal", au_dessus,
                             c["comptes"][a_]["a_temps"] / R, R, ref, R)

    # --- P4 ---
    def P4(self):
        for c in self.r["P4"]["configs"]:
            tag, cfg = f"{c['N']}x{c['T']}", f"gauss_{c['N']}x{c['T']}"
            for arr, t in c["T1"].items():
                v = sum(t["valeurs_differentes"].values()) + sum(t["discordances"].values())
                self.cellule("P4.1", f"{tag}/{arr}", trajectoriel, v, genre="trajectoriel", **t)
            for k_arr, (arr, comptes) in enumerate(c["T2"].items()):
                for al, k in comptes.items():
                    p0, R0 = self.p0(cfg, al)
                    doublon = k_arr > 0 and al in SYMETRIQUES      # même multi-ensemble : même valeur
                    self.cellule("P4.2", f"{tag}/{arr}/{al}", egal, k / c["R"], c["R"], p0, R0, egalite=not doublon)
        p = self.r["P43"]
        cfg = p["cfg"]
        p0, R0 = self.p0(cfg, "dispersion_agents")
        pt = p["alarmes_total"] / p["R"]
        loi = self.r["calibrage"][cfg]["loi"]
        p_th = cal.puissance_dispersion_rebrassage(int(loi["T"]), loi["mus"], self.alpha,
                                                   self.r["calibrage"][cfg]["seuils"]["dispersion_agents"])
        self.cellule("P4.3", "rebrassage_total>P0", au_dessus, pt, p["R"], p0, R0)
        self.cellule("P4.3", "rebrassage_total=forme_close", theorie, pt, p["R"], p_th, theorique=True, p=pt, p_th=p_th)
        self.cellule("P4.3", "rebrassage_intra_agent", egal, p["alarmes_intra_agent"] / p["R"], p["R"], p0, R0,
                     egalite=True)

    # --- P5 ---
    def P5(self):
        t = self.r["P5_temps"]
        R, cfg = t["R"], t["cfg"]
        for arr, c in t["arrangements"].items():
            v = c["viol_page"] + c["viol_glissante"] + c["borne_sans_alarme"]
            self.cellule("P5.1", arr, trajectoriel, v, genre="trajectoriel", viol_page=c["viol_page"],
                         viol_glissante=c["viol_glissante"], borne_sans_alarme=c["borne_sans_alarme"])
        for arr, c in t["arrangements"].items():
            if c["r"] >= 5 and arr.startswith("bloc_"):
                for al in ("glissante_5", "page"):
                    p0, R0 = self.p0(cfg, al)
                    self.cellule("P5.2", f"{arr}/{al}", au_dessus, c["alarmes"][al] / R, R, p0, R0)
        for arr, cible in (("apparie_autocorr", "autocorr"), ("apparie_suites", "suites")):
            c = t["arrangements"][arr]
            incomplet = c["ecart_hors_tolerance"] / R > 0.01
            p0, R0 = self.p0(cfg, cible)
            if incomplet:
                self.cellule("P5.3", f"{arr}/{cible}", lambda: ("non concluant", None), ecart_hors_tolerance=c["ecart_hors_tolerance"])
            else:
                self.cellule("P5.3", f"{arr}/{cible}", au_plus, c["alarmes"][cible] / R, R, p0, R0)
            for al in ("glissante_5", "page"):
                p0l, R0l = self.p0(cfg, al)
                self.cellule("P5.3", f"{arr}/{al}", au_dessus, c["alarmes"][al] / R, R, p0l, R0l)
        a = self.r["P5_agents"]
        nom_ce = f"co_elevation_{a['mc']}"
        self.cellule("P5.4", f"{nom_ce}≥{a['mc']}·v({a['mc']})", trajectoriel, a["viol_co_elevation"],
                     genre="trajectoriel")
        p0, R0 = self.p0(a["cfg"], nom_ce)
        self.cellule("P5.5", nom_ce, au_dessus, a["alarmes"][nom_ce] / a["R"], a["R"], p0, R0)

    # --- P6 ---
    def P6(self):
        a = self.alpha
        for c in self.r["P6"]["cellules"]:
            loi, R, k, cfg = c["loi"], c["R"], c["alarmes"], c["cfg"]
            p = {al: n / R for al, n in k.items()}
            nom = c["nom"]
            if c["role"] == "copule_temps":
                phi, gauss = float(loi["phi"]), loi.get("marginale", "gauss") == "gauss"
                if phi > 0:
                    if gauss:
                        for al in ("somme", "e_unilat_ville"):
                            self.cellule("P6.1", f"{nom}/{al}", au_dessus, p[al], R, *self.p0(cfg, al))
                    self.cellule("P6.1", f"{nom}/max", au_plus, p["max"], R, *self.p0(cfg, "max"))
                    self.cellule("P6.1", f"{nom}/autocorr", au_dessus, p["autocorr"], R, *self.p0(cfg, "autocorr"))
                else:
                    if gauss:
                        for al in ("somme", "e_unilat_ville"):
                            self.cellule("P6.2", f"{nom}/{al}", en_dessous, p[al], R, *self.p0(cfg, al))
                    self.cellule("P6.2", f"{nom}/autocorr_abs", au_dessus, p["autocorr_abs"], R,
                                 *self.p0(cfg, "autocorr_abs"))
                if gauss:
                    p_th = cal.rejet_somme_sous_variance(a, facteur_variance_ar1(phi, int(loi["T"])))
                    self.cellule("P6.3", f"{nom}/somme", theorie, p["somme"], R, p_th, theorique=True,
                                 p=p["somme"], p_th=p_th)
            elif c["role"] == "equicorrelation":
                cc, N = float(loi["c"]), int(loi["N"])
                p_th = cal.rejet_somme_sous_variance(a, 1.0 + (N - 1) * cc)
                self.cellule("P6.4", f"{nom}/somme=théorie", theorie, p["somme"], R, p_th, theorique=True,
                             p=p["somme"], p_th=p_th)
                for al in ("somme", "e_unilat_ville", "co_elevation_N", "correlation_agents"):
                    self.cellule("P6.4", f"{nom}/{al}", au_dessus, p[al], R, *self.p0(cfg, al))
                self.cellule("P6.4", f"{nom}/max", au_plus, p["max"], R, *self.p0(cfg, "max"))
            elif c["role"] == "construction_2606":
                T = int(loi["T"])
                phi0 = float(self.r["calibrage"][cfg]["loi"]["phi"])
                rapport = facteur_variance_ar1(float(loi["phi"]), T) / facteur_variance_ar1(phi0, T)
                p_th = cal.rejet_somme_sous_variance(a, rapport)
                self.cellule("P6.5", f"{nom}/somme=théorie", theorie, p["somme"], R, p_th, theorique=True,
                             p=p["somme"], p_th=p_th)
                self.cellule("P6.5", f"{nom}/max", au_plus, p["max"], R, *self.p0(cfg, "max"))
                self.cellule("P6.5", f"{nom}/autocorr", au_dessus, p["autocorr"], R, *self.p0(cfg, "autocorr"))

    # --- P7 ---
    def P7(self):
        t = self.r["P7"]
        R, cfg = t["R"], t["cfg"]
        for arr, c in t["arrangements"].items():
            v = c["viol_inclusion_haute"] + c["viol_inclusion_basse"] + c["viol_sommes_partielles"]
            self.cellule("P7.1", arr, trajectoriel, v, genre="trajectoriel", **{k: c[k] for k in c if k.startswith("viol")})
            for al in ("page", "glissante_10"):
                self.cellule("P7.3", f"{arr}/{al}", au_dessus, c["alarmes"][al] / R, R, *self.p0(cfg, al))
        c = t["arrangements"]["tri_croissant"]
        self.cellule("P7.2", "tri_croissant/e_bilat_ville", au_moins, c["alarmes"]["e_bilat_ville"] / R, R, SEUIL_P72)

    # --- P8 ---
    def P8(self, bien_specifies, signe, depasse):
        a = self.alpha
        par_nom = {s["nom"]: s for s in self.r["P8"]["reglages"]}
        for s in self.r["P8"]["reglages"]:
            R, p = s["R"], s["alarmes"]["e_unilat_ville"] / s["R"]
            if s["nom"] in bien_specifies:
                self.cellule("P8.1", s["nom"], au_plus_valeur, p, R, a)
            if s["nom"] in signe:
                ref = par_nom[signe[s["nom"]]]
                self.cellule("P8.2", f"{s['nom']}>{ref['nom']}", au_dessus, p, R,
                             ref["alarmes"]["e_unilat_ville"] / ref["R"], ref["R"])
            if s["nom"] in depasse:
                self.cellule("P8.3", s["nom"], au_dessus_valeur, p, R, a)
            c = s["conforme"]
            for st, liste in c["alarmes_par_tirage"].items():
                taux = np.array(liste, dtype=float) / c["n_test"]
                se = max(float(taux.std(ddof=1)) / math.sqrt(c["L"]),
                         math.sqrt(a * (1 - a) / (c["L"] * c["n_test"])))
                d = float(taux.mean()) - c["taux_theorique"]
                etat = "conforme" if abs(d) <= Z * se else "contraire"
                self.cellule("P8.4", f"{s['nom']}/{st}", lambda e=etat, zz=d / se: (e, zz), egalite=True,
                             taux=float(taux.mean()), taux_theorique=c["taux_theorique"])

    def audit_symetrie(self) -> dict:
        sortie = {"bornes": list(BORNES_AUDIT)}
        for nom, liste in (("formes_closes", self.z_theorie), ("egalites", self.z_egalites)):
            z = np.array(liste)
            s2 = float(z.var(ddof=1)) if z.size > 1 else float("nan")
            sortie[nom] = {"n": int(z.size), "variance_z": s2,
                           "hors_bornes": bool(z.size > 1 and not (BORNES_AUDIT[0] <= s2 <= BORNES_AUDIT[1]))}
        sortie["audit_declenche"] = sortie["formes_closes"]["hors_bornes"] or sortie["egalites"]["hors_bornes"]
        return sortie

    def lire(self, p8: dict) -> dict:
        for methode, blocs in BLOCS_DE.items():
            if all(x in self.r for x in blocs):
                getattr(self, methode)(**(p8 if methode == "P8" else {}))
        sortie = {}
        for pred in sorted(self.predictions):
            cel = self.predictions[pred]["cellules"]
            v = verdict(cel)
            a_repliquer = [c["nom"] for c in cel if c["etat"] == "contraire" and c["genre"] == "statistique"]
            a_auditer = [c["nom"] for c in cel if c["etat"] == "contraire" and c["genre"] == "trajectoriel"]
            sortie[pred] = {"verdict": v, "n_cellules": len(cel),
                            "n_conformes": sum(c["etat"] == "conforme" for c in cel),
                            "n_contraires": sum(c["etat"] == "contraire" for c in cel),
                            "a_repliquer": a_repliquer, "a_auditer": a_auditer, "cellules": cel}
        return {"predictions": sortie, "audit_symetrie": self.audit_symetrie(), "z_seuil": Z}


def lire(resultats: dict, alpha: float, p8: dict) -> dict:
    return Lecteur(resultats, alpha).lire(p8)


def fusionner(principale: dict, replication: dict) -> dict:
    """Règle de réplication gelée (critère C) : une cellule statistique « contraire » de la lecture
    principale devient « non concluant » si sa réplication (graines neuves, 5 × R) est conforme ; elle reste
    « contraire » sinon, ou si elle n'a pas été répliquée. Toute violation trajectorielle observée en
    réplication rend sa cellule « contraire » (audit). Les autres cellules de la réplication sont
    descriptives. Après fusion, aucune autre reprise : `a_repliquer` est vidé, `repliquees` le remplace."""
    import copy

    sortie = copy.deepcopy(principale)
    for pred, x in sortie["predictions"].items():
        rep = {c["nom"]: c for c in replication.get("predictions", {}).get(pred, {}).get("cellules", [])}
        for c in x["cellules"]:
            if c["etat"] == "contraire" and c["genre"] == "statistique" and c["nom"] in rep:
                c["replication"] = rep[c["nom"]]["etat"]
                if rep[c["nom"]]["etat"] == "conforme":
                    c["etat"] = "non concluant"
                    c["note"] = "contraire en lecture principale, conforme en réplication : bruit Monte-Carlo probable"
        noms = {c["nom"]: c for c in x["cellules"]}
        for nom, rc in rep.items():          # toute violation trajectorielle observée en réplication compte
            if rc.get("genre") == "trajectoriel" and rc["etat"] == "contraire":
                if nom in noms:
                    noms[nom]["etat"] = "contraire"
                    noms[nom]["note"] = "violation trajectorielle observée en réplication : audit"
                else:
                    x["cellules"].append({**rc, "note": "violation trajectorielle observée en réplication : audit"})
        x["a_auditer"] = [c["nom"] for c in x["cellules"] if c["etat"] == "contraire" and c["genre"] == "trajectoriel"]
        x["repliquees"] = [c["nom"] for c in x["cellules"] if "replication" in c]
        x["a_repliquer"] = []
        x["verdict"] = verdict(x["cellules"])
        x["n_conformes"] = sum(c["etat"] == "conforme" for c in x["cellules"])
        x["n_contraires"] = sum(c["etat"] == "contraire" for c in x["cellules"])
    return sortie


LIGNES_E = [
    {"enonce": "Lemme : « la puissance ne dépend que de B et de la variance — pas de la répartition du sabotage "
               "sur les agents ni sur les pas de temps »",
     "lecture": ("Établi par preuve, vérifié en simulation : exact pour la statistique terminale à n₀ fixé, la "
                 "« variance » étant celle de la statistique (n₀σ²), pour toute répartition (agents, pas, valeurs, "
                 "choix adaptatif des positions). Faux à variance par action fixée quand n₀ = NT varie : la "
                 "puissance décroît en n₀. Faux pour la lecture séquentielle toujours valide quant au calendrier "
                 "(répartition sur les pas) : avancer le sabotage aide le défenseur, le reporter le ramène vers la "
                 "borne terminale, seule invariante. L'invariance entre agents au même pas (L4) n'est pas testée en T0.3."),
     "exiges": ["P1.1", "P1.2", "P1.3", "P1.4", "P3.1", "P3.2", "P3.3"], "complementaires": []},
    {"enonce": "Brief T0.3 : « celle du max par action s'effondre quand la fragmentation croît »",
     "lecture": ("Établi par preuve, vérifié en simulation : exact, avec un plancher strictement au-dessus de α à "
                 "n₀ fixé."),
     "exiges": ["P2.1", "P2.2", "P2.3"], "complementaires": []},
    {"enonce": "Théorème : « toute statistique fondée sur les marginales (max, moyenne, somme cumulée) a une puissance "
               "égale au taux de faux positifs » (dommage dans la corrélation, marginale préservée)",
     "lecture": ("Vrai en classe C (multi-ensemble préservé) pour les statistiques symétriques, trajectoire par "
                 "trajectoire, et pour toute statistique sous rebrassage uniforme (T1, T2) ; le groupe de "
                 "permutations compte. Faux en classe K (copule) : la somme et le processus e passent au-dessus de "
                 "leur taux sous P₀ pour une dépendance positive et en dessous pour une négative ; sous dépendance "
                 "positive, le max reste à son taux ou en dessous (Slepian) ; c'est le cas de la construction de "
                 "2606.10456 (somme 0,07 à 0,25 à α = 0,05)."),
     "exiges": ["P4.1", "P4.2", "P4.3", "P6.1", "P6.2", "P6.3", "P6.4", "P6.5"], "complementaires": []},
    {"enonce": "Théorème : « il faut un agrégateur d'autocorrélation (dans le temps) ou de co-élévation (entre agents) »",
     "lecture": ("En classe K, sous dépendance positive, l'autocorrélation et la co-élévation détectent (P6.1, P6.4) ; "
                 "sous dépendance négative, "
                 "la somme et le processus e passent sous leur taux sous P₀ et l'autocorrélation en valeur absolue "
                 "détecte (P6.2) ; sous dépendance positive, la somme n'est pas aveugle (P6.3, P6.4). Face à un "
                 "attaquant adaptatif de classe C, l'autocorrélation et les suites sont neutralisables (P5.3) ; seules "
                 "les statistiques locales — balayage, Page, co-élévation — gardent une garantie trajectorielle "
                 "(P5.1, P5.4)."),
     "exiges": ["P5.1", "P5.3", "P5.4", "P6.1", "P6.2", "P6.3", "P6.4"], "complementaires": ["P5.2", "P5.5"]},
    {"enonce": "Brief T0.3 : « la somme cumulée échoue » (attaque à marginale préservée)",
     "lecture": ("Exact pour la somme terminale en classe C (T1) ; exact au sens adverse pour la somme séquentielle "
                 "unilatérale sous arrangements à sommes partielles dominées (T4), dont la règle bilatérale "
                 "s'échappe ; inexact en classe K : la somme n'est pas aveugle (Φ̄(z_α·√(v₀/v₁)), 0,07 à 0,25 dans la "
                 "construction de 2606.10456 à α = 0,05), mais reste faible."),
     "exiges": ["P4.1", "P6.1", "P6.5", "P7.1", "P7.2"], "complementaires": ["P7.3"]},
    {"enonce": "Garde de G1 : « le taux de faux positifs des agrégateurs toujours valides est vérifié empiriquement "
               "sur épisodes honnêtes »",
     "lecture": ("Décisive : la règle de Ville dépasse son taux bien spécifié sous effet épisode, corrélation entre "
                 "agents, dépendance temporelle ou σ sous-estimé, et dépasse α aux niveaux les plus forts d'effet épisode, de "
                 "corrélation entre agents et de sous-estimation de σ. Le "
                 "calibrage conforme sur épisodes honnêtes entiers tient son taux quand les épisodes de calibrage et "
                 "de déploiement sont échangeables (vérification de l'instrument) ; sa robustesse à un décalage entre "
                 "eux n'est pas testée en T0.3."),
     "exiges": ["P8.1", "P8.2", "P8.3", "P8.4"], "complementaires": []},
]


def enonces_du_programme(lecture: dict) -> list[dict]:
    """Table E gelée : une lecture par énoncé, prononcée seulement si toutes ses prédictions exigées sont
    confirmées ; sinon « non établi ». Les prédictions complémentaires sont affichées, sans effet."""
    v = {k: x["verdict"] for k, x in lecture["predictions"].items()}
    sortie = []
    for ligne in LIGNES_E:
        etablie = all(v.get(k) == "confirmée" for k in ligne["exiges"])
        sortie.append({"enonce": ligne["enonce"],
                       "lecture": ligne["lecture"] if etablie else "non établi : voir " + ", ".join(ligne["exiges"]),
                       "exiges": ligne["exiges"], "complementaires": ligne["complementaires"],
                       "verdicts": {k: v.get(k, "absente") for k in ligne["exiges"] + ligne["complementaires"]}})
    return sortie
