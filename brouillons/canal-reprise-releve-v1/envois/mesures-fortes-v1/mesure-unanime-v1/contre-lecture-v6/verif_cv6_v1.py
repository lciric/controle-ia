"""Vérifications de la contre-lecture v6 (R2) du préenregistrement « mesure unanime ».

Lancé depuis le dossier du préenregistrement (le script v6 et la lecture mécanique v2 y sont importés **sans
modification**), interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B`. Aucune donnée réelle : mondes synthétiques
seulement. Graines : `SeedSequence(2810202606, spawn_key=(partie, scénario, monde))`.

Parties (premier argument) :
- `lecture`  : la lecture mécanique v2 sur l'essai synthétique v6, puis sur des sorties modifiées (arbre de M2 ter sur
               les 32 combinaisons des cinq conditions, comparé à une réécriture indépendante du Seuil ; propagation des
               audits du placebo et du maximum de M4 à la ligne de lecture ; M2 bis à r₀ ≥ 0,5 ; cellule à zéro).
- `pas_fixe` : dérive linéaire avec le pas (montante, descendante), avec ou sans effet épisode, masques en préfixe ou
               dispersés : r₀ brut, centré par pas, du mélange, du mélange à pas fixé ; Ville sur réelles, mélange,
               mélange à pas fixé ; D et D′ (médianes sur 12 sondes, 10 mélanges).
- `feuille_4c` : mondes sans dérive (dépendance seule, marges gaussiennes), 30 sondes corrélées entre elles, 20 mélanges,
               2 000 rééchantillonnages comme le script (deux boucles séparées pour D et D′) : fréquence des feuilles,
               et la même lecture avec un tirage d'épisodes partagé par D et D′. Arguments : r0 c n_mondes graine_debut.
- `defaut_niveau` : excès apparié de M4 avec et sans un défaut de niveau commun aux deux termes (rang conforme abaissé
               d'un cran : niveau 0,075 au lieu de 0,05).
"""
import copy
import json
import math
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.getcwd())
import numpy as np  # noqa: E402

import analyse_fausses_alertes_v6 as a  # noqa: E402
import lecture_mecanique_v2 as lm  # noqa: E402

ENT = 2810202606
VILLE = ("ville", "processus_e")


def feuille_texte(v0, vm, vmp, bbD, bbDp, alpha=0.05):
    """Réécriture indépendante du Seuil de M2 ter (v6, lignes 177 à 184), lue dans le texte."""
    if v0 <= 0.05:
        return "1"
    if bbD <= 0:
        return "2a" if vm > alpha else "2b"
    if vm > alpha:
        return "3a" if bbDp > 0 else "3b"
    if bbDp > 0:
        return "4a" if vmp <= alpha else "4b"
    return "4c"


def partie_lecture():
    base = json.load(open("sortie-synthetique-essai-v6.json", encoding="utf-8"))
    table = json.load(open("table-m2bis-m4-v6.json", encoding="utf-8"))["table"]
    out = {"essai_v6_tel_quel": lm.lire(base, table)}
    # (1) arbre : 32 combinaisons
    grille, feuilles, desaccords = [], {}, []
    for v0 in (0.04, 0.07):
        for vm in (0.01, 0.06):
            for vmp in (0.01, 0.06):
                for bbD in (-0.01, 0.01):
                    for bbDp in (-0.01, 0.01):
                        s = copy.deepcopy(base)
                        r = s["resultats"]
                        r["tau=0.0"]["ville:processus_e"]["reelles"]["mediane"] = v0
                        r["melange_actions_permutees_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vm
                        r["melange_pas_fixe_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vmp
                        r["ville_tau0_reelles_moins_melange"]["intervalle_95"][0] = bbD
                        r["ville_tau0_reelles_moins_melange_pas_fixe"]["intervalle_95"][0] = bbDp
                        f_lec = lm.lire(s, table)["verdicts"]["M2_ter"].split(")")[0].strip("(")
                        f_txt = feuille_texte(v0, vm, vmp, bbD, bbDp)
                        feuilles[f_lec] = feuilles.get(f_lec, 0) + 1
                        if f_lec != f_txt:
                            desaccords.append([v0, vm, vmp, bbD, bbDp, f_lec, f_txt])
                        grille.append([v0, vm, vmp, bbD, bbDp, f_lec])
    out["M2_ter_grille"] = {"combinaisons": len(grille), "feuilles_atteintes": feuilles, "desaccords_texte_lecture": desaccords}

    # (2) audit du placebo : M1 confirmé, M3 tenu, M4 confirmé, mais un écart réelles − placebo de 0,08 sur une cellule de M3
    s = copy.deepcopy(base)
    s["resultats"]["tau=0.0"]["par_action:max"]["reelles"]["mediane_intervalle_95"] = [0.07, 0.10]
    s["resultats"]["tau=1.0"]["conforme:somme_terminale"]["placebos"]["mediane"] = (
        s["resultats"]["tau=1.0"]["conforme:somme_terminale"]["reelles"]["mediane"] - 0.08)
    l2 = lm.lire(s, table)
    out["placebo_audit"] = {k: l2["verdicts"][k] for k in ("M1", "M3", "M4", "placebo")}
    out["placebo_audit"]["ligne_de_lecture"] = l2["ligne_de_lecture"]

    # (3) audit du maximum de M4 (> 0,10) avec M1 confirmé
    s = copy.deepcopy(base)
    s["resultats"]["tau=0.0"]["par_action:max"]["reelles"]["mediane_intervalle_95"] = [0.07, 0.10]
    s["resultats"]["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["reelles"]["mediane"] = 0.12
    l3 = lm.lire(s, table)
    out["M4_max_audit"] = {k: l3["verdicts"][k] for k in ("M1", "M4")}
    out["M4_max_audit"]["ligne_de_lecture"] = l3["ligne_de_lecture"]

    # (4) M2 bis à r₀ ≥ 0,5 avec un écart de 0,12 à la table
    s = copy.deepcopy(base)
    s["resultats"]["correlation_intra_episode_r0"]["reelles"]["mediane"] = 0.6
    s["resultats"]["correlation_intra_episode_r0"]["centre_par_pas_reelles"]["mediane"] = 0.6
    s["resultats"]["ville_tau2_moins_tau0"]["mediane"] = 0.17
    l4 = lm.lire(s, table)
    out["M2_bis_r0_0.6_ecart"] = {"verdict": l4["verdicts"]["M2_bis"], "quantites": l4["quantites"]["M2_bis"]}

    # (5) cellule à zéro : médiane et q3 nuls (au moins 75 % des sondes à 0), pas toutes
    s = copy.deepcopy(base)
    c = s["resultats"]["tau=0.5"]["conforme:balayage"]["reelles"]
    c["mediane"], c["q3"], c["part_au_dessus_de_2alpha"] = 0.0, 0.0, 0.1
    l5 = lm.lire(s, table)
    out["cellule_a_zero_q3_nul_mais_10_pourcent_au_dessus_de_2alpha"] = {"verdict": l5["verdicts"]["cellule_a_zero"], "M3": l5["verdicts"]["M3"]}

    # (6) excès exactement 0,02 en rationnel, lu en flottant
    out["note_flottant"] = "voir verif-flottant-sortie.txt"
    return out


def monde(rng, r0=0.0, c=0.0, beta=0.0, E=60, T=10, S=12, masques="prefixe"):
    """Scores gaussiens ; effet épisode de variance r0/(1 − r0), dont une part c commune à toutes les sondes ; dérive
    beta·(t − 4,5) avec le pas brut t ; masques en préfixe (longueurs 5 à 10) ou dispersés (positions tirées)."""
    var_u = r0 / (1 - r0) if r0 > 0 else 0.0
    g = rng.normal(size=(E, 1, 1)); h = rng.normal(size=(E, 1, S))
    u = math.sqrt(var_u) * (math.sqrt(c) * g + math.sqrt(1 - c) * h)
    t = np.arange(T, dtype=float)[None, :, None]
    X = u + beta * (t - (T - 1) / 2) + rng.normal(size=(E, T, S))
    masque = np.zeros((E, T), bool)
    for e in range(E):
        k = int(rng.integers(a.MIN_ACTIONS, T + 1))
        if masques == "prefixe":
            masque[e, :k] = True
        else:
            masque[e, np.sort(rng.choice(T, size=k, replace=False))] = True
    X[~masque] = np.nan
    return X, masque


def bras_ville(X, masque, rng, Dm):
    E, _, S = X.shape
    perm = rng.permutation(E); plis = a.plis_de_perm(perm); zero = np.zeros(E)
    rm = rng.spawn(Dm)
    rmp = rng.spawn(Dm)
    A0 = np.zeros((S, 1, E), bool); Am = np.zeros((S, Dm, E), bool); Amp = np.zeros((S, Dm, E), bool)
    r0b, r0c, r0m, r0mp = [], [], [], []
    for si in range(S):
        Xs = X[:, :, si]
        r0b.append(a.correlation_intra_episode(Xs, masque)); r0c.append(a.correlation_intra_episode(a.centrer_par_pas(Xs, masque), masque))
        A0[si, 0] = a.un_passage(Xs, masque, plis, perm, zero, 0.0)[0][VILLE]
        tm, tmp = [], []
        for di in range(Dm):
            Xm = a.melanger_actions(Xs, masque, rm[di]); tm.append(a.correlation_intra_episode(Xm, masque))
            Am[si, di] = a.un_passage(Xm, masque, plis, perm, zero, 0.0)[0][VILLE]
            Xmp = a.melanger_actions_pas_fixe(Xs, masque, rmp[di]); tmp.append(a.correlation_intra_episode(Xmp, masque))
            Amp[si, di] = a.un_passage(Xmp, masque, plis, perm, zero, 0.0)[0][VILLE]
        r0m.append(np.mean(tm)); r0mp.append(np.mean(tmp))
    med = lambda A, idx=slice(None): float(np.median(A[:, :, idx].mean(axis=(1, 2))))
    return A0, Am, Amp, {"r0_brut": float(np.median(r0b)), "r0_centre_par_pas": float(np.median(r0c)),
                         "r0_melange": float(np.median(r0m)), "r0_melange_pas_fixe": float(np.median(r0mp)),
                         "ville_reelles": med(A0), "ville_melange": med(Am), "ville_melange_pas_fixe": med(Amp),
                         "D": med(A0) - med(Am), "D_prime": med(A0) - med(Amp)}, med


def partie_pas_fixe():
    out = {}
    scen = [("derive_montante_sans_effet_prefixe", 0.0, 0.3, "prefixe"), ("derive_descendante_sans_effet_prefixe", 0.0, -0.3, "prefixe"),
            ("derive_montante_sans_effet_disperses", 0.0, 0.3, "disperses"), ("derive_descendante_sans_effet_disperses", 0.0, -0.3, "disperses"),
            ("forte_derive_descendante_sans_effet_prefixe", 0.0, -0.6, "prefixe"),
            ("effet_r0_0.4_sans_derive_prefixe", 0.4, 0.0, "prefixe"), ("effet_r0_0.4_derive_descendante_prefixe", 0.4, -0.3, "prefixe"),
            ("effet_r0_0.4_derive_montante_prefixe", 0.4, 0.3, "prefixe")]
    for k, (nom, r0, beta, msq) in enumerate(scen):
        res = []
        for w in range(2):
            rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(2, k, w)))
            X, masque = monde(rng, r0=r0, beta=beta, masques=msq)
            res.append({c: round(v, 4) for c, v in bras_ville(X, masque, rng, 10)[3].items()})
        out[nom] = res
        print(nom, res, file=sys.stderr, flush=True)
    return out


def partie_feuille_4c(r0, c, n_mondes, debut):
    out = {"r0": r0, "c": c, "sondes": 30, "melanges": 20, "bootstrap": 2000, "mondes": []}
    for w in range(debut, debut + n_mondes):
        rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(3, int(r0 * 100), int(c * 100), w)))
        X, masque = monde(rng, r0=r0, c=c, S=30)
        A0, Am, Amp, q, med = bras_ville(X, masque, rng, 20)
        rb = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(4, w)))
        E = X.shape[0]
        # comme le script : deux boucles, chacune avec ses propres tirages d'épisodes
        dm = [med(A0, i) - med(Am, i) for i in (rb.integers(0, E, size=E) for _ in range(2000))]
        dp = [med(A0, i) - med(Amp, i) for i in (rb.integers(0, E, size=E) for _ in range(2000))]
        # variante : un tirage d'épisodes partagé par D et D′
        idxs = [rb.integers(0, E, size=E) for _ in range(2000)]
        dm2 = [med(A0, i) - med(Am, i) for i in idxs]; dp2 = [med(A0, i) - med(Amp, i) for i in idxs]
        dd = [med(Amp, i) - med(Am, i) for i in idxs]  # Ville pas fixé − mélange : la dérive, mesurée
        bb = lambda v: float(np.quantile(v, 0.025))
        f_script = feuille_texte(q["ville_reelles"], q["ville_melange"], q["ville_melange_pas_fixe"], bb(dm), bb(dp))
        f_partage = feuille_texte(q["ville_reelles"], q["ville_melange"], q["ville_melange_pas_fixe"], bb(dm2), bb(dp2))
        # bruit de Monte-Carlo : 20 répliques indépendantes des deux boucles du script (2 000 tirages chacune) ;
        # part des répliques où bb(D) et bb(D′) tombent de part et d'autre de 0, et feuilles obtenues
        repl, feuilles_repl = [], {}
        for _ in range(20):
            b1 = bb([med(A0, i) - med(Am, i) for i in (rb.integers(0, E, size=E) for _ in range(2000))])
            b2 = bb([med(A0, i) - med(Amp, i) for i in (rb.integers(0, E, size=E) for _ in range(2000))])
            repl.append([round(b1, 4), round(b2, 4)])
            f = feuille_texte(q["ville_reelles"], q["ville_melange"], q["ville_melange_pas_fixe"], b1, b2)
            feuilles_repl[f] = feuilles_repl.get(f, 0) + 1
        ligne = {"monde": w, **{k: round(v, 4) for k, v in q.items()}, "bbD": round(bb(dm), 4), "bbD_prime": round(bb(dp), 4),
                 "bbD_partage": round(bb(dm2), 4), "bbD_prime_partage": round(bb(dp2), 4),
                 "pas_fixe_moins_melange_intervalle": [round(bb(dd), 4), round(float(np.quantile(dd, 0.975)), 4)],
                 "feuille_script": f_script, "feuille_tirage_partage": f_partage,
                 "repliques_bbD_bbDprime": repl, "feuilles_sur_20_repliques_du_script": feuilles_repl,
                 "repliques_de_part_et_d_autre_de_0": int(sum((x > 0) != (y > 0) for x, y in repl))}
        out["mondes"].append(ligne)
        print(json.dumps(ligne, ensure_ascii=False), file=sys.stderr, flush=True)
    return out


def partie_defaut_niveau():
    out = {}
    orig = a.rang_conforme
    for r0 in (0.2, 0.5):
        rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(5, int(r0 * 10))))
        X, masque = monde(rng, r0=r0, S=12)
        E = X.shape[0]; perm = rng.permutation(E); plis = a.plis_de_perm(perm)
        effets = [rng.normal(size=E) for _ in range(10)]
        res = {}
        for nom, rc in (("sans_defaut", orig), ("defaut_rang_moins_1", lambda K, al: orig(K, al) - 1)):
            a.rang_conforme = rc
            t0, t4 = [], []
            for si in range(X.shape[2]):
                Xs = X[:, :, si]
                al0 = a.un_passage(Xs, masque, plis, perm, effets[0], 0.0)[0]
                t0.append(np.mean([al0[("conforme", s)].mean() for s in a.STATISTIQUES[1:]]))
                t4.append(np.mean([np.mean([a.un_passage(Xs, masque, plis, perm, effets[d], 2.0, calibrage_sans_effet=True,
                                                         variance_constante=True)[0][("conforme", s)].mean() for s in a.STATISTIQUES[1:]])
                                   for d in range(10)]))
            a.rang_conforme = orig
            t0, t4 = np.array(t0), np.array(t4)
            res[nom] = {"quantite_tau0": float(np.median(t0)), "quantite_M4": float(np.median(t4)), "exces_par_sonde": float(np.median(t4 - t0))}
        res["variation_de_l_exces"] = res["defaut_rang_moins_1"]["exces_par_sonde"] - res["sans_defaut"]["exces_par_sonde"]
        res["variation_du_niveau_tau0"] = res["defaut_rang_moins_1"]["quantite_tau0"] - res["sans_defaut"]["quantite_tau0"]
        out[f"r0={r0}"] = res
    return out


if __name__ == "__main__":
    p = sys.argv[1]
    if p == "lecture":
        r = partie_lecture()
    elif p == "pas_fixe":
        r = partie_pas_fixe()
    elif p == "feuille_4c":
        r = partie_feuille_4c(float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    elif p == "defaut_niveau":
        r = partie_defaut_niveau()
    else:
        raise SystemExit("partie inconnue")
    json.dump({"partie": p, "argv": sys.argv[1:], "numpy": np.__version__, "resultat": r}, sys.stdout, ensure_ascii=False, indent=1)
    print()
