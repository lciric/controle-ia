"""Lecture de T0.6, v2 (contre-lecture du lanceur v1, C06, L05 ; nom neuf, R12 : `lecture.py` reste tel quel) :
- réserve « paires de distillation exclues au-delà de 5 % » comptée **par adaptateur** (saboteur et témoin chacun) ;
- réserve « contrôle négatif de la garde d'équivalence non concluant » écrite aussi sous la table A ;
- état d'un jeu selon la règle de configuration `lecture.non_interpretable_si_au_dessus_seulement` (L05) : vrai, « non
  interprétable » n'est testé que si le jeu est au-dessus (règle du code v1) ; faux, un prédicteur trivial qui sépare au
  moins autant que la sonde rend le jeu « non interprétable » même sous le plancher (lettre de la table B, B5 avant B6/B7).
Le reste (T6-1 à T6-10, audit R4, tables A, B, C, relecture) vient de `lecture` tel quel.
"""
from __future__ import annotations

from .lecture import (PART_EXCLUES_MAX, audit_R4_sondes, lecture_cout, lecture_sondes, relire_tables, reserves_cout,
                      table_A, table_B_ou_C)
from .test_croise import AU_DESSUS, ECHEC, NON_AU_DESSUS, NON_INTERPRETABLE, separation

__all__ = ["lecture_cout_v2", "lecture_sondes_v2", "etat_du_jeu_v2", "appliquer_regle_etat", "reserves_cout_v2",
           "audit_R4_sondes", "lecture_sondes", "relire_tables", "table_A", "table_B_ou_C"]


def reserves_cout_v2(r: dict, config: dict, effectifs: dict, controle_negatif: str | None = None) -> list[str]:
    sortie = reserves_cout(r, config, {k: v for k, v in effectifs.items()
                                       if k not in ("actions_exclues_distillation", "actions_distillation")})
    par_adaptateur = effectifs.get("exclusions_par_adaptateur") or {}
    for ad, x in sorted(par_adaptateur.items()):
        excl, total = x.get("exclues"), x.get("actions")
        if excl is not None and total and excl / total > PART_EXCLUES_MAX:
            sortie.append(f"paires de distillation exclues au-delà de 5 % pour l'adaptateur {ad} ({excl} sur {total})")
    if controle_negatif == "non concluant":
        sortie.append("contrôle négatif de la garde d'équivalence « non concluant »")
    return sortie


def lecture_cout_v2(couts: dict, config: dict, graines: dict, generateur, audit: dict | None = None,
                    effectifs: dict | None = None, controle_negatif: str | None = None) -> dict:
    r = lecture_cout(couts, config, graines, generateur, audit, {})
    r["reserves"] = reserves_cout_v2(r, config, effectifs or {}, controle_negatif)
    return r


def etat_du_jeu_v2(resume: dict, si_au_dessus_seulement: bool) -> str:
    if "echec" in resume:
        return ECHEC
    au_dessus = resume["bas"] > resume["plancher"]["quantile"]
    sep = separation(resume["aire"])
    trivial = any(t["separation"] is not None and t["separation"] >= sep for t in resume["triviaux"].values())
    if si_au_dessus_seulement:
        if not au_dessus:
            return NON_AU_DESSUS
        return NON_INTERPRETABLE if trivial else AU_DESSUS
    if trivial:
        return NON_INTERPRETABLE
    return AU_DESSUS if au_dessus else NON_AU_DESSUS


def appliquer_regle_etat(jeux: dict, si_au_dessus_seulement: bool) -> dict:
    """Réécrit l'état de chaque jeu (décisifs, contrôles, validité, courbe, couples descriptifs) selon la règle."""
    def _un(j):
        if isinstance(j, dict) and ("echec" in j or "bas" in j):
            j["etat"] = etat_du_jeu_v2(j, si_au_dessus_seulement)
            j["regle_non_interpretable"] = "si au-dessus seulement" if si_au_dessus_seulement else "toujours"
        return j

    for sens in ("sens1", "sens2"):
        for k, v in list(jeux.get(sens, {}).items()):
            if k == "courbe":
                for c in v:
                    _un(v[c])
            else:
                _un(v)
    for v in (jeux.get("descriptifs") or {}).values():
        if isinstance(v, dict):
            for j in v.values():
                _un(j)
    return jeux


def lecture_sondes_v2(jeux: dict, ligne_A: str, config: dict, verdict_p3bis: str | None = None, bases_t08_lues: bool = False,
                      audit: dict | None = None, controle_negatif: str | None = None) -> dict:
    appliquer_regle_etat(jeux, bool(config["lecture"]["non_interpretable_si_au_dessus_seulement"]))
    s = lecture_sondes(jeux, ligne_A, verdict_p3bis, bases_t08_lues, audit, controle_negatif)
    s["regle_non_interpretable"] = config["lecture"]
    return s
