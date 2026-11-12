"""Analyse de la brèche de W2 (troisième course de l'attaque de Goodhart v3) — v1.

Lecture seule. Aucun appel de modèle, aucun réseau, aucun jugement sous le nul v9.
Entrées : la sortie scellée de la course et l'arbre du code de l'organisme au commit de la course (291e917).
Sortie : un JSON de constats, imprimé et écrit à côté de ce script.

Usage : python -I analyse_w2_v1.py <sortie attaque-goodhart-v3.json> <manifeste.json> <arbre organisme 291e917> <sortie.json>
"""
import collections
import json
import math
import sys


def charger(chemin):
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecart_max(a, b):
    """Plus grand écart absolu entre deux lois de même forme (softmax : poids et biais ; fixe : probas) ; None si formes différentes."""
    if not isinstance(a, dict) or not isinstance(b, dict) or a.get("type") != b.get("type"):
        return None
    if a["type"] == "softmax":
        pa = [x for ligne in a["poids"] for x in ligne] + list(a["biais"])
        pb = [x for ligne in b["poids"] for x in ligne] + list(b["biais"])
    elif a["type"] == "fixe":
        pa, pb = list(a["probas"]), list(b["probas"])
    else:
        return None
    if len(pa) != len(pb):
        return None
    return max(abs(float(x) - float(y)) for x, y in zip(pa, pb))


def main():
    sortie, manifeste, arbre, chemin_sortie = sys.argv[1:5]
    d = charger(sortie)
    m = charger(manifeste)
    entropie = int(m["reglages"]["entropie_racine"])
    sys.path.insert(0, arbre + "/orchestrator")
    from pole import attaque_goodhart_v2 as ag  # code au commit de la course (empreintes vérifiées à part)

    constats = {"entropie_egale_empreinte_du_texte": entropie == int(d["preenregistrement"]["sha256"], 16)}

    # 1. Suites : promotions, rang de la première promotion, appels, par (monde, condition, juge)
    par_case = {}
    for s in d["suites"]:
        cle = f'{s["monde"]}|{s["condition"]}|{s["juge"]}'
        c = par_case.setdefault(cle, {"suites": 0, "promues": 0, "rangs": collections.Counter(), "tentatives": 0,
                                      "appels": 0, "lois_jugees": 0, "hors_classe": 0, "couvertes": 0})
        c["suites"] += 1
        c["promues"] += s["premiere_promotion"] is not None
        if s["premiere_promotion"] is not None:
            c["rangs"][s["premiere_promotion"]] += 1
        for t in s["tentatives"]:
            c["tentatives"] += 1
            a = t.get("appels")
            c["appels"] += len(a) if isinstance(a, list) else int(a or 0)
            if t.get("loi") is not None:
                c["lois_jugees"] += 1
                c["hors_classe"] += bool(t.get("hors_classe"))
                c["couvertes"] += bool(t.get("couverte"))
    for c in par_case.values():
        c["rangs"] = dict(sorted(c["rangs"].items()))
    constats["par_case"] = dict(sorted(par_case.items()))
    constats["appels_total"] = sum(c["appels"] for c in par_case.values())

    # 2. Lois promues de W2 sous v8 : forme, membre dominant, richesse, égalité à la loi du monde
    cartes = {}
    lois_promues = []
    for s in d["suites"]:
        if s["monde"] != "W2" or s["juge"] != "v8" or s["premiere_promotion"] is None:
            continue
        t = [t for t in s["tentatives"] if t["k"] == s["premiere_promotion"]][0]
        ci = s["carte"]
        if ci not in cartes:
            cartes[ci] = ag.carte(entropie, ci, "W2")
        L = cartes[ci]["L"]
        loi = t["loi"]
        info = {"carte": ci, "condition": s["condition"], "k": t["k"], "type": loi.get("type"),
                "log_w_max": t["verdict"]["log_w_max"], "dominant": t["verdict"]["dominant"],
                "hors_classe": t.get("hors_classe"), "couverte": t.get("couverte")}
        if loi.get("type") == "par_sous_population":
            l0, l1 = loi["lois"].get("0"), loi["lois"].get("1")
            info["ecart_0_S1"], info["ecart_1_S2"] = ecart_max(l0, L["S1"]), ecart_max(l1, L["S2"])
            info["ecart_0_S2"], info["ecart_1_S1"] = ecart_max(l0, L["S2"]), ecart_max(l1, L["S1"])
            info["types_morceaux"] = [l0.get("type") if isinstance(l0, dict) else None,
                                      l1.get("type") if isinstance(l1, dict) else None]
        lois_promues.append(info)
    constats["w2_v8_lois_promues"] = len(lois_promues)
    constats["w2_v8_types"] = dict(collections.Counter(x["type"] for x in lois_promues))
    constats["w2_v8_dominants"] = dict(collections.Counter(x["dominant"] for x in lois_promues))
    lw = sorted(x["log_w_max"] for x in lois_promues)
    constats["w2_v8_log_w_max"] = {"min": lw[0], "mediane": lw[len(lw) // 2], "max": lw[-1],
                                   "seuil_log_20": math.log(20)}
    psp = [x for x in lois_promues if x["type"] == "par_sous_population"]
    exactes = [x for x in psp if x.get("ecart_0_S1") is not None and x.get("ecart_1_S2") is not None
               and max(x["ecart_0_S1"], x["ecart_1_S2"]) <= 1e-6]
    proches = [x for x in psp if x.get("ecart_0_S1") is not None and x.get("ecart_1_S2") is not None
               and max(x["ecart_0_S1"], x["ecart_1_S2"]) <= 1e-3]
    inverses = [x for x in psp if x.get("ecart_0_S2") is not None and x.get("ecart_1_S1") is not None
                and max(x["ecart_0_S2"], x["ecart_1_S1"]) <= 1e-3]
    constats["w2_v8_par_sous_population"] = len(psp)
    constats["w2_v8_egales_au_monde_a_1e-6"] = len(exactes)
    constats["w2_v8_egales_au_monde_a_1e-3"] = len(proches)
    constats["w2_v8_monde_inverse_a_1e-3"] = len(inverses)
    constats["w2_v8_ecart_au_monde_max"] = max(
        (max(x["ecart_0_S1"], x["ecart_1_S2"]) for x in psp
         if x.get("ecart_0_S1") is not None and x.get("ecart_1_S2") is not None), default=None)
    constats["w2_v8_autres"] = [x for x in lois_promues if x not in proches][:6]

    # 3. Audit A2 recalculé depuis les comptes (Clopper-Pearson, Holm) avec les fonctions du banc
    b = ag.banc()
    a2 = [r for r in d["audit_A2"]]
    p = {i: b.p_valeur_exacte(r["promues"], r["rejeux"], ag.ALPHA, "basse") for i, r in enumerate(a2)}
    au_dessus = b.holm(p)
    ecarts = 0
    for i, r in enumerate(a2):
        cp = b.clopper_pearson(r["promues"], r["rejeux"])[0]
        if abs(cp - r["clopper_pearson_95_bas"]) > 1e-12 or (i in au_dessus) != r["au_dessus_de_alpha_holm"]:
            ecarts += 1
    w2a = [r for r in a2 if r["monde"] == "W2"]
    constats["audit_A2"] = {"entrees": len(a2), "w2": len(w2a), "ecarts_au_recalcul": ecarts,
                            "w2_au_dessus_holm": sum(r["au_dessus_de_alpha_holm"] for r in w2a),
                            "w2_promues_sur_rejeux": dict(collections.Counter(f'{r["promues"]}/{r["rejeux"]}' for r in w2a)),
                            "w2_somme_promues": sum(r["promues"] for r in w2a), "w2_somme_rejeux": sum(r["rejeux"] for r in w2a),
                            "w2_cp95_bas_min": min(r["clopper_pearson_95_bas"] for r in w2a),
                            "w1": [{k: r[k] for k in ("carte", "etiquette", "k", "promues", "rejeux", "au_dessus_de_alpha_holm")}
                                   for r in a2 if r["monde"] == "W1"]}

    # 4. Rejeux principaux (toutes les lois jugées) : taux de promotion par (monde, juge)
    rj = collections.defaultdict(lambda: [0, 0, 0])
    for r in d["rejeux"]:
        k = f'{r["monde"]}|{r["etiquette"].split("|")[2]}|{r["juge"]}'
        rj[k][0] += 1
        rj[k][1] += r["promues"]
        rj[k][2] += r["rejeux"]
    constats["rejeux_principaux"] = {k: {"lois": v[0], "promues": v[1], "rejeux": v[2],
                                         "taux": round(v[1] / v[2], 4) if v[2] else None} for k, v in sorted(rj.items())}

    # 5. Lecture gelée : issues, prédictions, écarts du retour
    lec = d["lecture"]
    constats["issues"] = lec["issues"]
    constats["predictions"] = {w: lec["mondes"][w].get("predictions") for w in lec["mondes"]}
    constats["ecarts_goodhart_par_carte_W2"] = lec["mondes"]["W2"].get("ecarts_goodhart_par_carte")
    constats["plafond_multiplicite"] = lec["mondes"]["W2"].get("plafond_multiplicite_1_moins_1_moins_alpha_puissance_n")
    constats["depense_usd"] = d["depense_usd"]
    constats["duree_s"] = d["duree_s"]
    constats["appels_declares"] = d["appels"]

    with open(chemin_sortie, "w", encoding="utf-8") as f:
        json.dump(constats, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(constats, ensure_ascii=False, sort_keys=True)[:6000])


if __name__ == "__main__":
    main()
