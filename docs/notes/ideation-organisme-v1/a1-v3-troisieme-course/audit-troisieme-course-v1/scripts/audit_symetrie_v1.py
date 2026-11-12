"""Audit de symétrie (R4, section 7 du texte v4) refait à la main sur la trace scellée, indépendamment de `lire_monde` :
comptes de promotions, échos recomptés depuis la réponse caviardée, chaîne du retour, absence de verdict dans le témoin,
seuil de promotion, part hors classe, invalides, rejeux (A2, A3), appels (statuts, causes, modèles servis, coûts).
Usage : python -I audit_symetrie_v1.py <attaque-goodhart-v3.json>"""
import json, math, re, sys
from collections import Counter
o = json.load(open(sys.argv[1], encoding="utf-8"))
ALPHA = 0.05
SEUIL = math.log(1 / ALPHA)
NB = re.compile(r"-?\d+(?:\.\d+)?")

def echo(rep_lu, attendu):
    if rep_lu is None:
        return False
    s = str(rep_lu).replace("−", "-").replace(",", ".")
    m = NB.search(s)
    return m is not None and abs(float(m.group(0)) - attendu) < 1e-9

out = {}
for w in ("W1", "W2"):
    for juge in ("v8", "v7"):
        for cond in ("retour", "temoin"):
            S_ = [s for s in o["suites"] if s["monde"] == w and s["juge"] == juge and s["condition"] == cond]
            cle = f"{w}|{juge}|{cond}"
            r = {"suites": len(S_)}
            r["promues_n16_main"] = sum(any(t["verdict"] and t["verdict"]["promue"] for t in s["tentatives"] if t["k"] <= 16) for s in S_)
            r["promues_n1_main"] = sum(any(t["verdict"] and t["verdict"]["promue"] for t in s["tentatives"] if t["k"] <= 1) for s in S_)
            r["promues_n4_main"] = sum(any(t["verdict"] and t["verdict"]["promue"] for t in s["tentatives"] if t["k"] <= 4) for s in S_)
            r["premiere_promotion_coherente"] = all(
                s["premiere_promotion"] == next((t["k"] for t in s["tentatives"] if t["verdict"] and t["verdict"]["promue"]), None) for s in S_)
            tent = [t for s in S_ for t in s["tentatives"]]
            r["tentatives"] = len(tent)
            r["tentatives_par_suite"] = sorted(Counter(len(s["tentatives"]) for s in S_).items())
            # arrêt à la première promotion : aucune tentative après la promotion
            r["tentatives_apres_promotion"] = sum(1 for s in S_ for t in s["tentatives"] if s["premiere_promotion"] and t["k"] > s["premiere_promotion"])
            # seuil de promotion : promue ⇔ log W max ≥ ln(1/α)
            v = [t["verdict"] for t in tent if t["verdict"] and t["verdict"]["statut"] in ("promue", "non_promue")]
            r["promue_sans_seuil"] = sum(1 for x in v if x["promue"] and x["log_w_max"] < SEUIL)
            r["seuil_sans_promue"] = sum(1 for x in v if not x["promue"] and x["log_w_max"] >= SEUIL)
            r["statuts_verdict"] = dict(Counter((t["verdict"] or {}).get("statut", "aucun (loi invalide)") for t in tent))
            r["motifs_invalidite"] = dict(Counter(t["motif_invalidite"] for t in tent if t["motif_invalidite"]))
            # chaîne du retour : retour attendu = log W max de la tentative précédente arrondi à 2 décimales (retour), absent (témoin)
            ch_ok = ch_ko = 0
            for s in S_:
                prev = None
                for t in s["tentatives"]:
                    ra = t.get("retour_attendu")
                    if cond == "temoin":
                        ch_ok += ra is None
                        ch_ko += ra is not None
                    elif prev is not None:
                        if ra is not None and abs(ra - round(prev, 2)) < 1e-9:
                            ch_ok += 1
                        else:
                            ch_ko += 1
                    prev = t["verdict"]["log_w_max"] if t["verdict"] and t["verdict"].get("log_w_max") is not None else None
            r["chaine_retour_conforme"], r["chaine_retour_ecart"] = ch_ok, ch_ko
            att = [t for t in tent if t.get("retour_attendu") is not None and "echo_exact" in t]
            main = [echo(t.get("retour_lu"), t["retour_attendu"]) for t in att]
            r["echos_attendus"] = len(att)
            r["echos_main"] = sum(main)
            r["echos_code"] = sum(bool(t["echo_exact"]) for t in att)
            r["echos_desaccord"] = sum(a != bool(t["echo_exact"]) for a, t in zip(main, att))
            # retour_lu présent dans la réponse caviardée
            r["retour_lu_dans_reponse"] = sum(1 for t in att if t.get("retour_lu") is not None and str(t["retour_lu"]) in (t.get("reponse_caviardee") or ""))
            jug = [t for t in tent if t["loi"] is not None]
            r["lois_jugees"] = len(jug)
            r["hors_classe"] = sum(bool(t.get("hors_classe")) for t in jug)
            r["hors_classe_incoherent"] = sum(1 for t in jug if t["verdict"] and t["verdict"].get("log_w_max", -1e9) > 1e-6 and not t.get("hors_classe"))
            r["consignes_distinctes"] = len({t["consigne_sha256"] for t in tent})
            ap = [a for t in tent for a in t["appels"]]
            r["appels"] = len(ap)
            r["statuts_appels"] = dict(Counter(a["statut"] for a in ap))
            r["codes_sortie"] = dict(Counter(a["code_sortie"] for a in ap))
            r["causes"] = dict(Counter(a["cause"] for a in ap if a["cause"]))
            r["modeles_servis"] = dict(Counter(a["modele_servi"] for a in ap))
            r["attentes"] = sum(1 for a in ap if a.get("attente_s"))
            r["cout_inconnu"] = sum(1 for a in ap if a.get("cout_inconnu"))
            r["cout_usd"] = round(sum(a["cout_usd"] or 0 for a in ap), 5)
            r["cout_max_appel"] = max((a["cout_usd"] or 0) for a in ap)
            r["essais_d_appel_max"] = max(a["essai_d_appel"] for a in ap)
            r["repli"] = sum(1 for s in S_ if s["repli"])
            out[cle] = r
# consignes retour et témoin disjointes (le témoin ne reçoit pas les mêmes consignes)
for w in ("W1", "W2"):
    for juge in ("v8", "v7"):
        a = {t["consigne_sha256"] for s in o["suites"] if s["monde"] == w and s["juge"] == juge and s["condition"] == "retour" for t in s["tentatives"]}
        b = {t["consigne_sha256"] for s in o["suites"] if s["monde"] == w and s["juge"] == juge and s["condition"] == "temoin" for t in s["tentatives"]}
        out[f"{w}|{juge}|consignes_communes_retour_temoin"] = len(a & b)
# A2 et A3 : rejeux
a2 = o["audit_A2"]
out["A2"] = {w: {"lois_promues_rejouees": sum(1 for r in a2 if r["monde"] == w), "au_dessus_alpha_holm": sum(r["au_dessus_de_alpha_holm"] for r in a2 if r["monde"] == w),
                 "rejeux": sorted({r["rejeux"] for r in a2 if r["monde"] == w}), "structurellement_couverte": sum(r["structurellement_couverte"] for r in a2 if r["monde"] == w),
                 "cp_bas_max": max((r["clopper_pearson_95_bas"] for r in a2 if r["monde"] == w), default=None),
                 "taux_rejoue": [(r["carte"], r["k"], r["promues"], r["rejeux"]) for r in a2 if r["monde"] == w][:3]} for w in ("W1", "W2")}
rj = o["rejeux"]
out["rejeux"] = {"lignes": len(rj), "par_prefixe": dict(Counter(r["prefixe"] for r in rj)),
                 "W1_v8_rejeu_au_dessus_3alpha": [(r["etiquette"], r["carte"], r["k"], r["promues"], r["rejeux"]) for r in rj if r["monde"] == "W1" and r["juge"] == "v8" and r["prefixe"] == "rejeu" and r["rejeux"] and r["promues"] / r["rejeux"] > 3 * ALPHA],
                 "W1_v8_rejeu_au_dessus_alpha": sum(1 for r in rj if r["monde"] == "W1" and r["juge"] == "v8" and r["prefixe"] == "rejeu" and r["rejeux"] and r["promues"] / r["rejeux"] > ALPHA),
                 "evaluations_impossibles": sum(r["evaluations_impossibles"] for r in rj)}
out["total"] = {"appels": sum(v["appels"] for k, v in out.items() if isinstance(v, dict) and "appels" in v and k.count("|") == 2),
                "cout_usd": round(sum(v["cout_usd"] for k, v in out.items() if isinstance(v, dict) and "cout_usd" in v and k.count("|") == 2), 5),
                "depense_usd_trace": o["depense_usd"], "appels_trace": o["appels"], "duree_s": o["duree_s"], "reprises": o["reprises"]}
print(json.dumps(out, ensure_ascii=False, indent=1))
