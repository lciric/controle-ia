"""Contre-lecture v5 (R2) de la « mesure unanime » : vérifications sur données synthétiques seulement.

Le script v5 est importé sans modification (chemin passé en argument). Aucune donnée réelle n'est lue.
Parties :
  exces    — l'« excès apparié de M4 » du script (différence des médianes) contre la définition du texte et de la table
             (médiane, sur les sondes, de la différence par sonde) : essai synthétique v5 reproduit (5 tirages), puis un monde
             à sondes hétérogènes (r₀ de 0 à 0,6).
  pas_fixe — mélange à pas fixé : dérive linéaire avec le pas sans effet épisode, et effet épisode sans dérive ;
             r₀ d'origine, du mélange, du mélange à pas fixé ; Ville à τ = 0 sur les trois ; différences.
  issues   — la règle M2 ter en cinq issues, appliquée à une grille de combinaisons (exhaustivité, recouvrement, cas
             d'attribution discutables).
Graines : numpy.random.SeedSequence(2810202605, spawn_key=(partie, scénario, monde)) (R9).
Usage : python -I -B verif_cv5_v1.py CHEMIN_DU_DOSSIER_DU_SCRIPT PARTIE > sortie.json
"""
import importlib.util
import itertools
import json
import math
import sys

import numpy as np

DOSSIER, PARTIE = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("a5", f"{DOSSIER}/analyse_fausses_alertes_v5.py")
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
ENT = 2810202605
SOMMES = ("somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")


def q_sonde(al_list):
    """quantité de M4 par sonde : moyenne des cinq sommes de la moyenne sur (tirages, épisodes)."""
    return float(np.mean([np.mean([al[("conforme", s)] for al in al_list]) for s in SOMMES]))


def alertes_m4_et_tau0(X, masque, plis, perm, effets2):
    """par sonde : alertes du bras M4 (D tirages) et à τ = 0, comme `main()` du script v5."""
    S = X.shape[2]
    A_bras = {s: np.zeros((S, len(effets2), X.shape[0]), bool) for s in SOMMES}
    A0 = {s: np.zeros((S, 1, X.shape[0]), bool) for s in SOMMES}
    for si in range(S):
        Xs = X[:, :, si]
        al0, _ = a.un_passage(Xs, masque, plis, perm, effets2[0], 0.0)
        for s in SOMMES:
            A0[s][si, 0] = al0[("conforme", s)]
        for di, ef in enumerate(effets2):
            al, _ = a.un_passage(Xs, masque, plis, perm, ef, 2.0, calibrage_sans_effet=True, variance_constante=True)
            for s in SOMMES:
                A_bras[s][si, di] = al[("conforme", s)]
    return A_bras, A0


def par_sonde(A, idx=None):
    sl = idx if idx is not None else slice(None)
    return np.mean([A[s][:, :, sl].mean(axis=(1, 2)) for s in SOMMES], axis=0)


def comparer_exces(A_bras, A0, reelles, rng, B=300):
    qb, q0 = par_sonde(A_bras)[reelles], par_sonde(A0)[reelles]
    E = A0[SOMMES[0]].shape[2]
    dm, md = [], []
    for _ in range(B):
        idx = rng.integers(0, E, size=E)
        b, z = par_sonde(A_bras, idx)[reelles], par_sonde(A0, idx)[reelles]
        dm.append(float(np.median(b) - np.median(z)))
        md.append(float(np.median(b - z)))
    return {"mediane_M4": float(np.median(qb)), "mediane_tau0": float(np.median(q0)),
            "difference_des_medianes_(script)": float(np.median(qb) - np.median(q0)),
            "mediane_des_differences_(texte_et_table)": float(np.median(qb - q0)),
            "ecart": float(np.median(qb - q0) - (np.median(qb) - np.median(q0))),
            "intervalle_95_difference_des_medianes": [float(np.quantile(dm, .025)), float(np.quantile(dm, .975))],
            "intervalle_95_mediane_des_differences": [float(np.quantile(md, .025)), float(np.quantile(md, .975))],
            "rééchantillonnages": B}


def partie_exces():
    out = {}
    # (1) l'essai synthétique v5, reproduit avec les graines du script (5 tirages)
    ss = np.random.SeedSequence(a.ENTROPIE)
    rng_plis, rng_synth, _ = [np.random.default_rng(s) for s in ss.spawn(3)]
    X, masque, noms, reelles, placebos, _ = a.synthetique(rng_synth)
    perm = rng_plis.permutation(X.shape[0]); plis = a.plis_de_perm(perm)
    effets2 = [np.random.default_rng(s).normal(size=X.shape[0]) for s in np.random.SeedSequence(a.ENTROPIE, spawn_key=(20, 1)).spawn(5)]
    Xr = X[:, :, reelles]
    A_bras, A0 = alertes_m4_et_tau0(Xr, masque, plis, perm, effets2)
    rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(1, 1)))
    out["essai_synthetique_v5_reproduit"] = comparer_exces(A_bras, A0, list(range(len(reelles))), rng)
    out["essai_synthetique_v5_reproduit"]["attendu_dans_sortie_v5"] = {"M4_quantite": 0.085, "quantite_tau0": 0.04667, "exces": 0.03833}
    # (2) un monde à 30 sondes hétérogènes (r₀ de 0 à 0,6), E = 60, longueurs 5 à 10, 5 tirages d'effet communs
    res = []
    for monde in range(3):
        rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(1, 2, monde)))
        E, T, S = 60, 10, 30
        r0s = np.linspace(0.0, 0.6, S)
        u = rng.normal(size=(E, 1, S)) * np.sqrt(r0s / (1 - r0s))[None, None, :]
        X = u + rng.normal(size=(E, T, S))
        masque = np.ones((E, T), bool)
        for e in range(E):
            masque[e, int(rng.integers(5, T + 1)):] = False
        X[~masque] = np.nan
        perm = rng.permutation(E); plis = a.plis_de_perm(perm)
        effets2 = [rng.normal(size=E) for _ in range(5)]
        A_bras, A0 = alertes_m4_et_tau0(X, masque, plis, perm, effets2)
        r = comparer_exces(A_bras, A0, list(range(S)), rng)
        r["monde"] = monde
        res.append(r)
    out["sondes_heterogenes_r0_0_a_0.6"] = res
    return out


def ville_rate(Xs, masque, plis, perm):
    al, _ = a.un_passage(Xs, masque, plis, perm, np.zeros(Xs.shape[0]), 0.0)
    return float(al[("ville", "processus_e")].mean())


def partie_pas_fixe():
    out = []
    scenarios = [("derive_decroissante_beta0.6_sans_effet", 0.0, -0.6, "prefixe"),
                 ("derive_decroissante_beta0.3_sans_effet", 0.0, -0.3, "prefixe"),
                 ("derive_croissante_beta0.6_sans_effet", 0.0, 0.6, "prefixe"),
                 ("derive_decroissante_beta0.6_sans_effet_masque_disperse", 0.0, -0.6, "disperse"),
                 ("effet_episode_r0_0.4_sans_derive", 0.4, 0.0, "prefixe"),
                 ("effet_episode_r0_0.4_et_derive_decroissante_0.6", 0.4, -0.6, "prefixe")]
    for k, (nom, r0, beta, type_masque) in enumerate(scenarios):
        for monde in range(2):
            rng = np.random.default_rng(np.random.SeedSequence(ENT, spawn_key=(2, k, monde)))
            E, T, S, D = 60, 10, 12, 5
            masque = np.ones((E, T), bool)
            for e in range(E):
                n = int(rng.integers(5, T + 1))
                if type_masque == "prefixe":
                    masque[e, n:] = False
                else:
                    masque[e] = False
                    masque[e, np.sort(rng.choice(T, n, replace=False))] = True
            t = np.arange(T, dtype=float)
            var_u = r0 / (1 - r0)
            X = rng.normal(size=(E, 1, S)) * math.sqrt(var_u) + rng.normal(size=(E, T, S)) + beta * (t - 4.5)[None, :, None]
            X[~masque] = np.nan
            perm = rng.permutation(E); plis = a.plis_de_perm(perm)
            r0_o, r0_m, r0_p, v_o, v_m, v_p = [], [], [], [], [], []
            for si in range(S):
                Xs = X[:, :, si]
                r0_o.append(a.correlation_intra_episode(Xs, masque)); v_o.append(ville_rate(Xs, masque, plis, perm))
                rm, rp, vm, vp = [], [], [], []
                for d in range(D):
                    Xm = a.melanger_actions(Xs, masque, rng); Xp = a.melanger_actions_pas_fixe(Xs, masque, rng)
                    rm.append(a.correlation_intra_episode(Xm, masque)); rp.append(a.correlation_intra_episode(Xp, masque))
                    vm.append(ville_rate(Xm, masque, plis, perm)); vp.append(ville_rate(Xp, masque, plis, perm))
                r0_m.append(np.mean(rm)); r0_p.append(np.mean(rp)); v_m.append(np.mean(vm)); v_p.append(np.mean(vp))
            md = lambda v: round(float(np.median(v)), 4)
            out.append({"scenario": nom, "monde": monde, "r0_vise": r0, "beta_pas": beta, "masque": type_masque,
                        "r0_origine": md(r0_o), "r0_melange": md(r0_m), "r0_pas_fixe": md(r0_p),
                        "ville_origine": md(v_o), "ville_melange": md(v_m), "ville_pas_fixe": md(v_p),
                        "origine_moins_melange": round(md(v_o) - md(v_m), 4), "origine_moins_pas_fixe": round(md(v_o) - md(v_p), 4)})
    return out


def issue_m2ter(v_reel, v_mel, bb_mel, bb_pas, alpha=0.05):
    """Seuil v5, M2 ter, lu dans l'ordre (lignes 159 à 165)."""
    if v_reel <= alpha:
        return "1 tenue"
    if bb_mel <= 0:
        return "2 marges seules"
    if v_mel > alpha:
        return "3 marges et dépendance"
    if bb_pas > 0:
        return "4 dépendance naturelle suffisante"
    return "5 structure avec dérive de pas"


def partie_issues():
    grille = {"v_reel": [0.03, 0.05, 0.07, 0.12], "v_mel": [0.005, 0.03, 0.05, 0.07], "v_pas": [0.005, 0.03, 0.07],
              "bb_mel": [-0.01, 0.0, 0.01], "bb_pas": [-0.01, 0.0, 0.01]}
    comptes, discutables = {}, []
    for v_reel, v_mel, v_pas, bb_mel, bb_pas in itertools.product(*grille.values()):
        i = issue_m2ter(v_reel, v_mel, bb_mel, bb_pas)
        comptes[i] = comptes.get(i, 0) + 1
        if i == "2 marges seules" and v_mel <= 0.05:
            discutables.append({"cas": "marges seules alors que le mélange est ≤ α", "v_reel": v_reel, "v_mel": v_mel, "bb_mel": bb_mel})
        if i == "3 marges et dépendance" and bb_pas <= 0:
            discutables.append({"cas": "« dépendance » sans différence au mélange à pas fixé établie", "v_mel": v_mel, "bb_mel": bb_mel, "bb_pas": bb_pas})
        if i == "4 dépendance naturelle suffisante" and v_pas > 0.05:
            discutables.append({"cas": "« suffisante » alors que Ville sur le mélange à pas fixé est déjà > α", "v_mel": v_mel, "v_pas": v_pas, "bb_pas": bb_pas})
    total = sum(comptes.values())
    uniques = {}
    for d in discutables:
        uniques[d["cas"]] = uniques.get(d["cas"], 0) + 1
    return {"combinaisons": total, "issues": comptes, "chaque_combinaison_a_une_issue": total == math.prod(len(v) for v in grille.values()),
            "note": "règle en « sinon » successifs : exhaustive et sans recouvrement par construction ; Ville sur le mélange à pas fixé n'entre dans aucune issue",
            "cas_discutables_par_type": uniques, "exemples": [next(d for d in discutables if d["cas"] == c) for c in uniques]}


if __name__ == "__main__":
    f = {"exces": partie_exces, "pas_fixe": partie_pas_fixe, "issues": partie_issues}[PARTIE]
    json.dump({"partie": PARTIE, "numpy": np.__version__, "script_v5": f"{DOSSIER}/analyse_fausses_alertes_v5.py",
               "resultat": f()}, sys.stdout, ensure_ascii=False, indent=1)
    print()
