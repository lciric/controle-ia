"""Contre-lecture GD6 : compare le rejeu du script v6 (sous-ensemble) aux sorties de l'auteur.
Usage : python -I -B comparer-rejeu-gd6.py DOSSIER_AUTEUR DOSSIER_REJEU SORTIE.json
(a) même graine : chaque cellule rejouée doit être identique, champ pour champ, à la cellule de même étiquette de l'auteur ;
(b) graine neuve : part « fiche du mode 1 retenue » (ebh_A.retenues_fiches_du_sujet) et composants, contre l'auteur ;
(c) K_s ≠ K_h : parts rejouées seules (pas d'équivalent chez l'auteur). Aucune donnée réelle lue."""
import json
import math
import os
import sys


def aplatir(x, pre=""):
    if isinstance(x, dict):
        out = {}
        for k, v in x.items():
            out |= aplatir(v, f"{pre}/{k}")
        return out
    if isinstance(x, list):
        out = {}
        for i, v in enumerate(x):
            out |= aplatir(v, f"{pre}[{i}]")
        return out
    return {pre: x}


def charger(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def resume(c):
    return {"retenue_ebhA": c["ebh_A"]["retenues_fiches_du_sujet"],
            "min8_gardes_40": c["40.0"]["k_gardes"]["part"], "min8_contrastes_40": c["40.0"]["k_contrastes"]["part"],
            "fiche_40": c["40.0"]["fiche_entiere"]["part"], "fiche_160": c["160.0"]["fiche_entiere"]["part"],
            "min8_gardes_160": c["160.0"]["k_gardes"]["part"]}


def main():
    aut, rej, sortie = sys.argv[1:4]
    pre = "simulation-puissance-garde-delta-v6-sortie-"
    A = {0: charger(os.path.join(aut, pre + "principale.json")), 1: charger(os.path.join(aut, pre + "dispersion-1.0-independante.json"))}
    res = {"meme_graine": {}, "graine_neuve": {}, "ks_different": {}}
    for s in (0, 1):
        R = charger(os.path.join(rej, f"rejeu-meme-graine-sigma{s}.json"))
        for et, c in R["cellules"].items():
            a = A[s]["cellules"].get(et)
            if a is None:
                res["meme_graine"][et] = "absente chez l'auteur"
                continue
            fa, fr = aplatir(a), aplatir(c)
            communs = set(fa) & set(fr)
            diff = [k for k in communs if fa[k] != fr[k]]
            res["meme_graine"][et] = {"champs_communs": len(communs), "differences": len(diff), "exemples": diff[:5],
                                      "seulement_auteur": len(set(fa) - set(fr)), "seulement_rejeu": len(set(fr) - set(fa))}
        N = charger(os.path.join(rej, f"rejeu-graine-neuve-sigma{s}.json"))
        for et, c in N["cellules"].items():
            a = A[s]["cellules"][et]
            ra, rn = resume(a), resume(c)
            p = ra["retenue_ebhA"]
            et_diff = math.sqrt(2 * max(p * (1 - p), 1e-6) / 2000)
            res["graine_neuve"][et] = {"auteur": ra, "rejeu": rn,
                                       "ecart_retenue": rn["retenue_ebhA"] - ra["retenue_ebhA"],
                                       "ecart_en_erreurs_types_de_la_difference": (rn["retenue_ebhA"] - ra["retenue_ebhA"]) / et_diff}
        K = charger(os.path.join(rej, f"ks-different-sigma{s}.json"))
        for et, c in K["cellules"].items():
            res["ks_different"][et] = resume(c)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    for bloc in ("meme_graine",):
        for et, v in res[bloc].items():
            print(bloc, et, v if isinstance(v, str) else (v["champs_communs"], v["differences"], v["seulement_auteur"], v["seulement_rejeu"]))
    for et, v in res["graine_neuve"].items():
        print("neuve", et, round(v["auteur"]["retenue_ebhA"], 3), round(v["rejeu"]["retenue_ebhA"], 3),
              round(v["ecart_en_erreurs_types_de_la_difference"], 2), {k: round(x, 3) for k, x in v["rejeu"].items()})
    for et, v in res["ks_different"].items():
        print("ks", et, {k: round(x, 3) for k, x in v.items()})


main()
