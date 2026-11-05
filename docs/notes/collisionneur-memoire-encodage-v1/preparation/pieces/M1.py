"""Mémoire du pôle : index de l'archive, garde de redite, bibliothèque de protocoles, calibration, leçons.

La mémoire ne contient que des champs tirés de l'archive du pôle (liste blanche), caviardés ; jamais de clé, jamais
rien d'autre. Les témoins sont indexés pour l'audit mais exclus de tout ce qui est servi aux agents (gabarits,
leçons, garde de redite) : un témoin reconnaissable cesserait de mesurer.
"""

import collections

from .caviardage import caviarder, caviarder_objet
from .outils import empreinte_objet, normaliser_texte

STATUTS_TRANCHES = ("survit", "eliminee")


def trigrammes(texte):
    t = f" {normaliser_texte(texte)} "
    return {t[i:i + 3] for i in range(len(t) - 2)}


def jaccard(a, b):
    ta, tb = trigrammes(a), trigrammes(b)
    if not ta and not tb:
        return 1.0
    return len(ta & tb) / len(ta | tb)


def signature_prediction(d):
    """Ce qui fait la prédiction : signe, valeur, métrique normalisée, seuil — et la loi engagée en sélection par pari."""
    pred = d.get("prediction") or {}
    loi = d.get("loi_predictive")
    return (pred.get("signe"), float(pred.get("valeur", 0.0)), normaliser_texte(d.get("metrique", "")),
            float(d.get("seuil", 0.0)), empreinte_objet(loi) if loi else None)


def brier(paires):
    """Score de Brier de prévisions p contre issues y ∈ {0, 1} : moyenne de (p − y)²."""
    paires = list(paires)
    if not paires:
        return None
    return sum((p - y) ** 2 for p, y in paires) / len(paires)


class Memoire:
    def __init__(self, active=True, seuil_redite=0.5, seuil_severe=0.05, nb_gabarits=3, longueur_lecon=1500):
        self.active = active
        self.seuil_redite = seuil_redite
        self.seuil_severe = seuil_severe
        self.nb_gabarits = nb_gabarits
        self.longueur_lecon = longueur_lecon
        self.index = {}
        self.lecons = []

    # --- (1) index de l'archive -------------------------------------------------------------------------------
    def indexer(self, fiche, issue, generation):
        code = issue.get("code") or {}
        entree = {
            "identifiant": fiche.identifiant, "enonce": fiche.enonce, "statut": fiche.statut,
            "verdict_declare": issue.get("verdict_declare"), "verdict_final": issue.get("verdict_final"),
            "motif": issue.get("motif"), "desaccord": bool(issue.get("desaccord")),
            "severite_attendue": fiche.severite_attendue,
            "aptitude": fiche.aptitude() if fiche.statut == "survit" else None,
            "prediction": fiche.prediction, "metrique": fiche.metrique, "seuil": fiche.seuil,
            "loi_predictive": fiche.loi_predictive,
            "protocole": fiche.protocole, "domaines": list(fiche.domaines), "operateurs": list(fiche.operateurs),
            "code": {"chemin": code.get("chemin"), "sha256": code.get("sha256")},
            "generation": generation, "source": issue.get("famille_source", fiche.famille_source()),
            "temoin": fiche.temoin is not None, "verite_temoin": fiche.temoin, "parents": list(fiche.parents),
        }
        self.index[fiche.identifiant] = caviarder_objet(entree)[0]
        return self.index[fiche.identifiant]

    def _entrees(self, temoins=False):
        return [e for _, e in sorted(self.index.items()) if temoins or not e["temoin"]]

    # --- (2) garde de redite ----------------------------------------------------------------------------------
    def chercher_redites(self, enonce):
        proches = []
        for e in self._entrees():
            if e["statut"] == "eliminee":
                j = jaccard(enonce, e["enonce"])
                if j >= self.seuil_redite:
                    proches.append((e["identifiant"], round(j, 4)))
        return sorted(proches, key=lambda x: (-x[1], x[0]))

    def garde_redite(self, fiche):
        """Une redite d'une éliminée est refusée, sauf si `ce_qui_change[id]` est rempli et que la prédiction diffère."""
        if not self.active:
            return {"accepte": True, "motif": "mémoire inactive", "proches": []}
        proches = self.chercher_redites(fiche.enonce)
        refus = []
        for ident, j in proches:
            justification = (fiche.ce_qui_change or {}).get(ident, "").strip()
            if not justification:
                refus.append(f"{ident} (jaccard {j}) : champ « ce qui change par rapport à {ident} » absent")
            elif signature_prediction(fiche.vers_dict()) == signature_prediction(self.index[ident]):
                refus.append(f"{ident} (jaccard {j}) : prédiction identique à celle de l'éliminée")
        if refus:
            return {"accepte": False, "motif": "redite d'une éliminée : " + " ; ".join(refus), "proches": proches}
        motif = "aucune éliminée proche" if not proches else "redite justifiée par une prédiction nouvelle"
        return {"accepte": True, "motif": motif, "proches": proches}

    # --- (3) bibliothèque de protocoles -----------------------------------------------------------------------
    def gabarits(self):
        severes = [e for e in self._entrees() if e["statut"] == "survit" and e["severite_attendue"] <= self.seuil_severe]
        severes.sort(key=lambda e: (e["severite_attendue"], e["identifiant"]))
        return [{"identifiant": e["identifiant"], "protocole": e["protocole"], "metrique": e["metrique"],
                 "severite_attendue": e["severite_attendue"]} for e in severes[:self.nb_gabarits]]

    # --- (4) registre de calibration --------------------------------------------------------------------------
    def registre_calibration(self):
        groupes = collections.defaultdict(list)
        for e in self._entrees(temoins=True):
            if e["statut"] in STATUTS_TRANCHES:
                groupes[e["source"]].append(e)
        registre = {}
        for source, entrees in sorted(groupes.items()):
            paires = [(e["severite_attendue"], 1.0 if e["statut"] == "survit" else 0.0) for e in entrees]
            nulles = [p for p, e in zip(paires, entrees) if e["verite_temoin"] == "fausse"]
            survie = sum(y for _, y in paires) / len(paires)
            moyenne = sum(p for p, _ in paires) / len(paires)
            registre[source] = {
                "nombre_de_fiches": len(paires), "brier": brier(paires), "severite_annoncee_moyenne": moyenne,
                "survie_observee": survie, "exces_de_survie": survie - moyenne,
                "nombre_sous_nul_connu": len(nulles), "brier_sous_nul_connu": brier(nulles),
            }
        return {"par_source": registre,
                "lecture": ("Brier de la sévérité annoncée (probabilité de survie sous le nul) contre la survie observée. "
                            "Sous un nul connu (témoins faux), c'est une mesure de calibration ; ailleurs, l'écart mêle "
                            "calibration et proportion d'hypothèses vraies : seuls les témoins tranchent.")}

    # --- (5) leçons de génération -----------------------------------------------------------------------------
    def resume_pour_synthese(self, generation):
        entrees = [e for e in self._entrees() if e["generation"] <= generation]
        motifs = collections.Counter(e["motif"] or "?" for e in entrees if e["statut"] != "survit")
        par_domaine = collections.defaultdict(lambda: [0, 0])
        for e in entrees:
            if e["statut"] in STATUTS_TRANCHES:
                for d in e["domaines"]:
                    par_domaine[d][0] += e["statut"] == "eliminee"
                    par_domaine[d][1] += 1
        return {
            "generation": generation,
            "comptes_par_statut": dict(collections.Counter(e["statut"] for e in entrees)),
            "causes_frequentes": motifs.most_common(5),
            "elimination_par_domaine": {d: {"eliminees": v[0], "tranchees": v[1]} for d, v in sorted(par_domaine.items())},
            "protocoles_qui_ont_fonctionne": self.gabarits(),
            "desaccords_experimentateur_verificateur": sum(e["desaccord"] for e in entrees),
            "redites_refusees": sum(e["statut"] == "refusee (redite)" for e in entrees),
        }

    def ajouter_lecon(self, generation, texte):
        propre = caviarder(str(texte))[0].strip()[:self.longueur_lecon]
        self.lecons.append({"generation": generation, "texte": propre})
        return propre

    def derniere_lecon(self):
        return self.lecons[-1] if self.lecons else None

    def texte_consigne(self, role):
        """Ce que la mémoire sert à un agent : gabarits (expérimentateurs) et dernière leçon (tous)."""
        if not self.active:
            return ""
        morceaux = []
        if role == "experimentateur":
            gabarits = self.gabarits()
            if gabarits:
                lignes = [f"- [{g['identifiant']}] sévérité annoncée {g['severite_attendue']} ; métrique : {g['metrique']} ; "
                          f"protocole : {g['protocole']}" for g in gabarits]
                morceaux.append("Gabarits de protocoles ayant survécu à un test sévère :\n" + "\n".join(lignes))
        lecon = self.derniere_lecon()
        if lecon and role in ("experimentateur", "recombinaison"):
            morceaux.append(f"Leçons de la génération {lecon['generation']} :\n{lecon['texte']}")
        return "\n\n".join(morceaux)

    def instantane(self):
        return {"active": self.active, "seuil_redite": self.seuil_redite, "seuil_severe": self.seuil_severe,
                "index": self.index, "lecons": self.lecons, "gabarits": self.gabarits(),
                "calibration": self.registre_calibration()}
