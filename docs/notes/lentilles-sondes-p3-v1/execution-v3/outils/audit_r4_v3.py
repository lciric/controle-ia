"""Audit R4 de la sortie réelle v3 des lentilles sur les sondes non principales de P3.

Descriptif seulement : aucun verdict de la règle primaire v3 n'est recalculé autrement ni changé.
Bibliothèque standard seule ; lit deux fichiers dont l'empreinte est contrôlée en dur :
- la sortie scellée `sortie-jlens-sondes-p3-v3.json` (da240e02…) ;
- la liste `concepts-sondes-p3-v3.json` (aac34d5c…).

Usage : python3 -I audit_r4_v3.py SORTIE.json CONCEPTS.json  > journal

Sorties (sur la sortie standard, en JSON puis en texte) :
1. pour chaque cas déclenché (S >= 10) : tête de début de mot, mots qui font S, recomptes sans les mots signalés
   par CLR3-05 (strict, élargi aux familles morphologiques, élargi plus les mots larges de la section 2 de la règle),
   borne supérieure de n_iso et n_pl sous la liste réduite ;
2. les mêmes cas sous l'autre concept (comptes et rang dans la nulle isotrope de l'autre concept) ;
3. les nulles des cas (n_iso, n_pl, histogrammes, position du plancher) ;
4. miroirs « trop mauvais » (CLR3-04) : liste propre en tête de −w, cases rejetées par les seuls planchers ;
5. mots de chaque case « cohérente » (CLR3-05) ;
6. contrôles : recompte de S depuis la tête, autres déclencheurs de la section 5, recouvrement entre sondes.

Pourquoi les bornes sont valables : retirer des mots de la liste ne peut que faire baisser (ou laisser) le compte de
chaque direction nulle ; donc #{nulle réduite >= S'} <= #{nulle complète >= S'}. La nulle isotrope est symétrique
(−u est isotrope si u l'est), de même que les planchers N(0, Σ) ; l'histogramme de +u vaut donc pour −w. Ces rangs
sont descriptifs.
"""

import hashlib
import json
import sys
from collections import Counter

SHA_SORTIE = "da240e028c3388579f6efb951954d74e16e6623dd00e971af498eddfd4bfe051"
SHA_CONCEPTS = "aac34d5cb52637fef6ebdd0d36009f8842efdef52d5e5298334e3a84f388bf6c"
N_ISO = 10000
N_ISO_MAX = 14
N_PL_MAX = 2

# CLR3-05, mots nommés tels quels par la contre-lecture (section 1).
CLR305_STRICT = {
    "enjeux": {"critical", "serious", "severe", "fatal", "severity", "breach", "compromised", "killed", "dead",
               "safety"},
    "tromperie": {"hide", "secret", "fake", "spoof", "phishing"},
}
# Familles morphologiques de ces mots présentes dans la liste v3 (choix de l'auditeur, écrit avant le recompte).
CLR305_FAMILLES = {
    "enjeux": {"critically", "seriously", "seriousness", "severely", "fatally", "fatalities", "breaches", "killing"},
    "tromperie": {"hides", "hiding", "hid", "secrets", "secretly", "secretive", "secrecy"},
}
# Règle v3, section 2, « mots larges restants », avec leur famille présente dans la liste.
LARGES_S2 = {
    "enjeux": {"serious", "critical", "safety", "damage", "dead", "damages", "damaging"},
    "tromperie": {"secret", "hide"},
}


def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def mot_de(jeton, liste):
    """Mot de la liste porté par un jeton de début de mot (espace initial, puis exactement le mot, casse libre)."""
    if not jeton.startswith(" "):
        return None
    m = jeton[1:].lower()
    return m if m in liste else None


def n_sup_egal(histo, s):
    return sum(int(v) for k, v in histo.items() if int(k) >= s)


def main(chemin_sortie, chemin_concepts):
    if sha256(chemin_sortie) != SHA_SORTIE:
        sys.exit("refus : empreinte de la sortie inattendue")
    if sha256(chemin_concepts) != SHA_CONCEPTS:
        sys.exit("refus : empreinte de la liste inattendue")
    d = json.load(open(chemin_sortie, encoding="utf-8"))
    c = json.load(open(chemin_concepts, encoding="utf-8"))
    listes = {k: {m.lower() for m in c[k]} for k in ("tromperie", "enjeux")}
    for k in CLR305_STRICT:
        for ens in (CLR305_STRICT[k], CLR305_FAMILLES[k], LARGES_S2[k]):
            manquants = ens - listes[k]
            if manquants:
                sys.exit(f"refus : mots signalés absents de la liste {k} : {sorted(manquants)}")
    autre = {"tromperie": "enjeux", "enjeux": "tromperie"}
    iso = d["descriptif"]["nulles"]["isotropes"]
    pl = d["descriptif"]["nulles"]["planchers_couche_15"]
    sondes = {s["nom"]: s for s in d["sondes"]}
    cases = d["regle_primaire"]["cases"]
    if len(cases) != 32:
        sys.exit("refus : il faut 32 cases")
    sortie = {"controles": [], "declenches": [], "coherentes": [], "miroirs_moins_w": [],
              "rejets_par_planchers_seuls": [], "recouvrement_entre_sondes": []}

    def ctrl(libelle, ok):
        sortie["controles"].append({"controle": libelle, "ok": bool(ok)})
        if not ok:
            sys.exit(f"refus : contrôle en échec : {libelle}")

    ctrl("sortie non factice", d["essai_factice"] is False)
    ctrl("règle complète", d["regle_primaire"]["complete"] is True)

    for case in cases:
        s = sondes[case["sonde"]]
        lent = s["lentilles"][case["lentille"]]
        k = case["concept"]
        tete = lent["plus"]["tete_debut_de_mot"]
        ctrl(f"{case['sonde']}/{case['lentille']} : tête de 20 jetons de début de mot",
             len(tete) == 20 and all(t["texte"].startswith(" ") for t in tete))
        mots = [mot_de(t["texte"], listes[k]) for t in tete]
        S = sum(m is not None for m in mots)
        ctrl(f"{case['sonde']}/{case['lentille']} : S recompté = S rendu ({S})", S == case["S"])
        ctrl(f"{case['sonde']}/{case['lentille']} : S = comptes_par_concept_plus",
             S == lent["descriptif_regle"]["comptes_par_concept_plus"][k])
        cle_iso = f"c{case['couche']}/{case['lentille']}/{k}"
        h = iso[cle_iso]["comptes"]
        ctrl(f"{case['sonde']}/{case['lentille']} : n_iso recompté depuis l'histogramme",
             n_sup_egal(h, S) == case["n_iso"])
        if case["couche"] == 15:
            hp = pl[f"{k}/{case['lentille']}"]["comptes"]
            ctrl(f"{case['sonde']}/{case['lentille']} : n_pl recompté depuis l'histogramme",
                 n_sup_egal(hp, S) == case["n_pl"])
        # autre concept, mêmes têtes
        ka = autre[k]
        mots_a = [mot_de(t["texte"], listes[ka]) for t in tete]
        Sa = sum(m is not None for m in mots_a)
        ctrl(f"{case['sonde']}/{case['lentille']} : compte de l'autre concept = sortie",
             Sa == lent["descriptif_regle"]["comptes_par_concept_plus"][ka])
        # −w
        tete_m = lent["moins"]["tete_debut_de_mot"]
        mots_m = [mot_de(t["texte"], listes[k]) for t in tete_m]
        Sm = sum(m is not None for m in mots_m)
        ctrl(f"{case['sonde']}/{case['lentille']} : compte −w = sortie",
             Sm == lent["descriptif_regle"]["comptes_par_concept_moins"][k])
        if Sm > 0:
            e = {"case": f"{case['sonde']}/{case['lentille']}", "S_moins": Sm,
                 "mots": [m for m in mots_m if m], "n_iso_desc": n_sup_egal(h, Sm),
                 "S_plus": S, "verdict_plus": case["verdict"]}
            if case["couche"] == 15:
                e["n_pl_desc"] = n_sup_egal(pl[f"{k}/{case['lentille']}"]["comptes"], Sm)
            sortie["miroirs_moins_w"].append(e)
        vsp = lent["descriptif_regle"]["verdict_sans_planchers"]
        if case["couche"] == 15 and vsp == "cohérent" and case["verdict"] != "cohérent":
            sortie["rejets_par_planchers_seuls"].append(f"{case['sonde']}/{case['lentille']}")
        if case["couche"] == 15:
            # contrôle indépendant : sans planchers = S >= 2 et n_iso <= 14
            attendu = "cohérent" if (S >= 2 and case["n_iso"] <= N_ISO_MAX) else "non cohérent"
            ctrl(f"{case['sonde']}/{case['lentille']} : verdict sans planchers recalculé", vsp == attendu)

        sortie.setdefault("croise_32_cases", []).append(
            {"case": f"{case['sonde']}/{case['lentille']}", "concept": k, "S_propre": S, "compte_autre_concept": Sa,
             "mots_autre_concept": [m for m in mots_a if m], "S_moins_w_propre": Sm, "verdict": case["verdict"]})

        def recomptes():
            reduit = {}
            for nom, retire in (("sans_CLR305_strict", CLR305_STRICT[k]),
                                ("sans_CLR305_elargi", CLR305_STRICT[k] | CLR305_FAMILLES[k]),
                                ("sans_CLR305_elargi_et_larges_s2",
                                 CLR305_STRICT[k] | CLR305_FAMILLES[k] | LARGES_S2[k])):
                Sr = sum(1 for m in mots if m and m not in retire)
                r = {"S": Sr, "retires": [m for m in mots if m and m in retire],
                     "borne_sup_n_iso": n_sup_egal(h, Sr)}
                ok = Sr >= 2 and r["borne_sup_n_iso"] <= N_ISO_MAX
                if case["couche"] == 15:
                    r["borne_sup_n_pl"] = n_sup_egal(pl[f"{k}/{case['lentille']}"]["comptes"], Sr)
                    ok = ok and r["borne_sup_n_pl"] <= N_PL_MAX
                r["reste_au_dessus_des_seuils_par_la_borne"] = ok
                reduit[nom] = r
            return reduit

        if case["verdict"] == "cohérent":
            distincts = sorted({m for m in mots if m})
            larges = {m for m in distincts if m in LARGES_S2[k]}
            sortie["coherentes"].append({
                "case": f"{case['sonde']}/{case['lentille']}", "S": S, "n_iso": case["n_iso"], "n_pl": case["n_pl"],
                "mots_en_ordre_de_tete": [m for m in mots if m], "mots_distincts": distincts,
                "un_seul_mot": len(distincts) == 1, "seulement_mots_larges_s2": bool(distincts) and larges == set(distincts),
                "mots_clr305_strict": sorted(set(distincts) & CLR305_STRICT[k]),
                "mots_clr305_famille": sorted(set(distincts) & CLR305_FAMILLES[k]),
                "autre_concept": {"concept": ka, "compte": Sa, "mots": [m for m in mots_a if m]},
                "recomptes_descriptifs": recomptes(),
                "tete_debut_de_mot": [t["texte"] for t in tete],
            })

        if S >= 10:
            reduit = recomptes()
            ha = iso[f"c{case['couche']}/{case['lentille']}/{ka}"]["comptes"]
            e = {
                "case": f"{case['sonde']}/{case['lentille']}", "concept": k, "couche": case["couche"],
                "verdict": case["verdict"],
                "tete_debut_de_mot": [{"rang": i + 1, "jeton": t["texte"], "logit": round(t["logit"], 3),
                                       "mot_de_la_liste": mots[i], "mot_autre_concept": mots_a[i]}
                                      for i, t in enumerate(tete)],
                "S": S, "mots_distincts": sorted({m for m in mots if m}),
                "hors_liste_en_tete": [t["texte"] for i, t in enumerate(tete) if mots[i] is None],
                "recomptes_descriptifs": reduit,
                "autre_concept": {"concept": ka, "compte": Sa, "mots": [m for m in mots_a if m],
                                  "n_iso_autre_concept_desc": n_sup_egal(ha, Sa),
                                  "z_autre_concept": lent["diagnostics_z"][ka]["z"],
                                  "meilleur_rang_plus_autre_concept_vocabulaire_entier":
                                      lent["diagnostics_z"][ka]["meilleur_rang_plus"]},
                "nulle_isotrope": {"cle": cle_iso, "n_iso": case["n_iso"], "p_rang": case["p_rang"],
                                   "histogramme": h, "maximum": iso[cle_iso]["maximum"],
                                   "quinzieme_plus_grand": sorted(
                                       [int(kk) for kk, v in h.items() for _ in range(int(v))])[-15]},
                "moins_w": {"compte_concept_propre": Sm, "mots": [m for m in mots_m if m],
                            "tete": [t["texte"] for t in tete_m]},
            }
            if case["couche"] == 15:
                cp = f"{k}/{case['lentille']}"
                vals = sorted([int(kk) for kk, v in pl[cp]["comptes"].items() for _ in range(int(v))])
                e["planchers"] = {"cle": cp, "n_pl": case["n_pl"], "histogramme": pl[cp]["comptes"],
                                  "maximum": vals[-1], "troisieme_plus_grand": vals[-3],
                                  "rang_descriptif": f"{1 + case['n_pl']}/201",
                                  "n_pl_autre_concept_desc": n_sup_egal(pl[f"{ka}/{case['lentille']}"]["comptes"], Sa)}
            sortie["declenches"].append(e)

    # déclencheurs : recompte indépendant de la liste
    attendus = sorted(f"{x['sonde']}/{x['lentille']} : S = {x['S']} ≥ 10" for x in cases if x["S"] >= 10)
    ctrl("liste des déclencheurs S ≥ 10 identique à la sortie",
         attendus == sorted(d["descriptif"]["declencheurs_audit"]["declenches"]))
    X = {l: sum(1 for x in cases if x["lentille"] == l and x["verdict"] == "cohérent") for l in ("logits", "jacobienne")}
    autres = {
        "X >= 12 ou X = 0 pour les deux": any(v >= 12 for v in X.values()) or all(v == 0 for v in X.values()),
        "b >= 6 et c = 0, ou l'inverse": False,
        "médiane isotrope >= 1": any(v["mediane"] >= 1 for v in iso.values()),
        "case cohérente d'un seul mot": any(e["un_seul_mot"] for e in sortie["coherentes"]),
        "case cohérente de mots larges seuls": any(e["seulement_mots_larges_s2"] for e in sortie["coherentes"]),
    }
    b = d["regle_primaire"]["comparaison"]["b_jacobienne_seule"]
    cc = d["regle_primaire"]["comparaison"]["c_logits_seuls"]
    autres["b >= 6 et c = 0, ou l'inverse"] = (b >= 6 and cc == 0) or (cc >= 6 and b == 0)
    sortie["X"] = X
    sortie["autres_declencheurs_section_5"] = autres
    ctrl("X par lentille = verdict d'ensemble rendu",
         all(X[l] == d["regle_primaire"]["verdict_ensemble"][l]["X"] for l in X))

    # recouvrement des têtes +w entre sondes du même concept, même couche, même lentille (descriptif)
    noms = list(sondes)
    for lentille in ("logits", "jacobienne"):
        for i, a in enumerate(noms):
            for bnom in noms[i + 1:]:
                sa, sb = sondes[a], sondes[bnom]
                if sa["concept"] != sb["concept"] or sa["couche"] != sb["couche"]:
                    continue
                ta = {t["id"] for t in sa["lentilles"][lentille]["plus"]["tete_debut_de_mot"]}
                tb = {t["id"] for t in sb["lentilles"][lentille]["plus"]["tete_debut_de_mot"]}
                sortie["recouvrement_entre_sondes"].append(
                    {"lentille": lentille, "a": a, "b": bnom, "communs_sur_20": len(ta & tb)})
    return sortie


if __name__ == "__main__":
    res = main(sys.argv[1], sys.argv[2])
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    print()
