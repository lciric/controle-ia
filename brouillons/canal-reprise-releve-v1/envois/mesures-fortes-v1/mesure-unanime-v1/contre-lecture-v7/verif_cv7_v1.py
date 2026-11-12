"""Contre-lecture v7 de la mesure unanime : vérifications (aucune donnée réelle ; rien de `donnees/` n'est ouvert).

Lancement, depuis le dossier du préenregistrement :
  /opt/venv-essaim-sim-v1/bin/python -I -B verif_cv7_v1.py lecture  ESSAI.json SORTIE_REEL_SYNTH.json TABLE.json > ...
  /opt/venv-essaim-sim-v1/bin/python -I -B verif_cv7_v1.py pas_fixe > ...
  /opt/venv-essaim-sim-v1/bin/python -I -B verif_cv7_v1.py garde_endormie DOSSIER_TMP > ...
Le script v7 et la lecture v3 sont importés sans modification ; les seules enveloppes posées le sont sur des noms du module
(garde endormie), jamais sur les fichiers. Graines : SeedSequence(2810202607, spawn_key=(partie, scénario, monde)).
"""
import copy
import itertools
import json
import math
import sys

sys.path.insert(0, ".")
import numpy as np

import analyse_fausses_alertes_v7 as a
import lecture_mecanique_v3 as lm

GRAINE = 2810202607


def seuil_du_texte(v0, bbD, vm, bbDp, vmp, bbDd, alpha=0.05):
    """Réécriture de l'arbre du Seuil v7, à partir du texte seul (lignes 187 à 195)."""
    if v0 <= 0.05:
        return "(1)"
    if bbD <= 0:
        return "(2a)" if vm > alpha else "(2b)"
    if vm > alpha:
        return "(3a)" if bbDp > 0 else "(3b)"
    if bbDp > 0:
        return "(4a)" if vmp <= alpha else "(4b)"
    return "(4c)" if bbDd > 0 else "(4d)"


def poser(s, v0, bbD, vm, bbDp, vmp, bbDd):
    r = s["resultats"]
    r["tau=0.0"]["ville:processus_e"]["reelles"]["mediane"] = v0
    r["melange_actions_permutees_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vm
    r["melange_pas_fixe_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vmp
    r["ville_tau0_reelles_moins_melange"]["intervalle_95"][0] = bbD
    r["ville_tau0_reelles_moins_melange_pas_fixe"]["intervalle_95"][0] = bbDp
    r["ville_tau0_melange_pas_fixe_moins_melange"]["intervalle_95"][0] = bbDd
    return s


def partie_lecture(chemin_essai, chemin_reel_synth, chemin_table):
    essai = json.load(open(chemin_essai, encoding="utf-8"))
    tab = json.load(open(chemin_table, encoding="utf-8"))
    table, tman = tab["table"], tab["manifeste"]
    out = {}
    # 1. arbre de M2 ter : 2^6 combinaisons, plus les bornes exactes et le bruit flottant
    feuilles, desaccords = {}, []
    for bits in itertools.product((0, 1), repeat=6):
        v0 = (0.08 if bits[0] else 0.03); bbD = (0.01 if bits[1] else -0.01); vm = (0.07 if bits[2] else 0.03)
        bbDp = (0.01 if bits[3] else -0.01); vmp = (0.07 if bits[4] else 0.03); bbDd = (0.01 if bits[5] else -0.01)
        s = poser(copy.deepcopy(essai), v0, bbD, vm, bbDp, vmp, bbDd)
        lu = lm.lire(s, table, table_manifeste=tman)["verdicts"]["M2_ter"].split(" ")[0]
        attendu = seuil_du_texte(v0, bbD, vm, bbDp, vmp, bbDd)
        feuilles[attendu] = feuilles.get(attendu, 0) + 1
        if lu != attendu:
            desaccords.append({"bits": bits, "lecture": lu, "texte": attendu})
    out["arbre_64_combinaisons"] = {"feuilles_atteintes": feuilles, "nombre_de_feuilles": len(feuilles), "desaccords": desaccords}
    bornes = []
    for v0, bbD, vm, bbDp, vmp, bbDd in ((0.05, 0.01, 0.03, 0.01, 0.03, 0.0), (0.05000000000000001, 0.01, 0.03, 0.01, 0.03, 0.0),
                                         (0.08, 0.0, 0.05, 0.0, 0.03, 0.0), (0.08, 3.5e-18, 0.03, -3.5e-18, 0.03, 3.5e-18),
                                         (0.08, 0.01, 0.05000000000000001, 0.0, 0.05, 0.0), (0.08, 0.01, 0.03, 0.01, 0.05000000000000001, 0.0)):
        s = poser(copy.deepcopy(essai), v0, bbD, vm, bbDp, vmp, bbDd)
        bornes.append({"entree": [v0, bbD, vm, bbDp, vmp, bbDd], "lecture": lm.lire(s, table, table_manifeste=tman)["verdicts"]["M2_ter"],
                       "texte_apres_arrondi": seuil_du_texte(*[round(x, 9) for x in (v0, bbD, vm, bbDp, vmp, bbDd)])})
    out["arbre_bornes_exactes"] = bornes
    # 2. audits : chaque audit doit suspendre la ligne ; cellule à zéro : portée sur la ligne ?
    cas = {}
    def lire_avec(f):
        s = copy.deepcopy(essai); f(s["resultats"]); l = lm.lire(s, table, table_manifeste=tman)
        return {"verdicts": {k: l["verdicts"][k] for k in ("M1", "M2_controle", "M3", "M4", "placebo", "cellule_a_zero")},
                "audits": l["audits"], "ligne_de_lecture": l["ligne_de_lecture"]}
    cas["essai_tel_quel"] = lire_avec(lambda r: None)
    cas["placebo_ecart_0.08_sur_tau1_somme_terminale"] = lire_avec(lambda r: r["tau=1.0"]["conforme:somme_terminale"]["placebos"].__setitem__(
        "mediane", r["tau=1.0"]["conforme:somme_terminale"]["reelles"]["mediane"] - 0.08))
    cas["maximum_M4_0.12"] = lire_avec(lambda r: r["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["reelles"].__setitem__("mediane", 0.12))
    cas["M3_cellule_0.11"] = lire_avec(lambda r: r["tau=0.5"]["conforme:page"]["reelles"].__setitem__("mediane", 0.11))
    cas["M2_controle_0.07"] = lire_avec(lambda r: r["tau=2.0"]["ville:processus_e"]["reelles"].__setitem__("mediane", 0.07))
    def zero(r):
        r["tau=0.0"]["conforme:somme_terminale"]["reelles"]["mediane"] = 0.0
        r["tau=0.0"]["conforme:somme_terminale"]["reelles"]["q3"] = 0.0
        r["tau=0.0"]["conforme:somme_terminale"]["placebos"]["mediane"] = 0.0
    cas["cellule_a_zero_tau0_somme_terminale"] = lire_avec(zero)
    # bras M4 à zéro (hors des 24 cellules) : la règle « cellule à zéro » le voit-elle ?
    def zero_m4(r):
        for st in ("somme_terminale",):
            r["M4_dependance_seule_variance_constante_tau=2"][f"conforme:max"]["reelles"]["mediane"] = 0.0
            r["M4_dependance_seule_variance_constante_tau=2"][f"conforme:max"]["reelles"]["q3"] = 0.0
            r["M4_dependance_seule_variance_constante_tau=2"][f"conforme:max"]["placebos"]["mediane"] = 0.0
    cas["maximum_M4_a_zero"] = lire_avec(zero_m4)
    out["audits_et_cellule_a_zero"] = cas
    # 3. manifeste : la sortie du MODE RÉEL (lancé sur un fichier synthétique) passe-t-elle la garde de E ?
    reel = json.load(open(chemin_reel_synth, encoding="utf-8"))
    m = reel["manifeste"]
    try:
        lm.lire(reel, table, empreinte_donnees=m["empreinte_donnees"], table_manifeste=tman); res = "passe"
    except SystemExit as e:
        res = f"REFUS : {e}"
    out["mode_reel_sur_synthetique"] = {"cle_E_au_manifeste": "E" in m, "gardes": m.get("gardes"), "tirages": m.get("tirages"),
                                        "bootstrap": m.get("bootstrap"), "lecture_v3": res}
    # ce que la lecture v3 lit si E était au manifeste (pour montrer que le reste passe)
    r2 = copy.deepcopy(reel); r2["manifeste"]["E"] = r2["manifeste"]["gardes"]
    l2 = lm.lire(r2, table, empreinte_donnees=m["empreinte_donnees"], table_manifeste=tman)
    out["mode_reel_sur_synthetique_si_E_au_manifeste"] = {"verdicts": l2["verdicts"], "ligne_de_lecture": l2["ligne_de_lecture"]}
    # 4. ce que la lecture ne vérifie pas : une sortie au bon nom de script mais d'empreinte, de tirages et de commit quelconques
    r3 = copy.deepcopy(essai); r3["manifeste"].update({"empreinte_script": "0" * 64, "tirages": 1, "bootstrap": 10, "commit": None})
    try:
        lm.lire(r3, table, table_manifeste=tman); res3 = "passe (ni l'empreinte du script, ni les tirages, ni le commit ne sont vérifiés)"
    except SystemExit as e:
        res3 = f"refus : {e}"
    out["manifeste_non_verifie"] = res3
    try:
        lm.lire(copy.deepcopy(essai), table, empreinte_donnees="968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf", table_manifeste=tman)
        out["essai_avec_empreinte_reelle_attendue"] = "passe"
    except SystemExit as e:
        out["essai_avec_empreinte_reelle_attendue"] = f"refus : {e}"
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1, default=str); print()


def monde(rng, scenario, E=60, T=10, n=12):
    """Scénarios du mélange à pas fixé.
    derive_lineaire : moyenne β·(t − 4,5)/4,5 (β = 1 écart type), aucun effet épisode, masques dispersés ;
    bosse_precoce : moyenne +0,8 aux pas 0 et 1, −0,2 ailleurs, aucun effet épisode, masques dispersés ;
    dependance : effet épisode r₀ = 0,3, aucune dérive, masques dispersés ;
    longueur : effet épisode lié à la longueur (u_e = 0,9·(k_e − 7,5)/1,7 + bruit, r₀ ≈ 0,3), masques en préfixe."""
    masque = np.ones((E, T), bool)
    longueurs = rng.integers(a.MIN_ACTIONS, T + 1, size=E)
    if scenario == "longueur":
        for e in range(E):
            masque[e, longueurs[e]:] = False
    else:
        for e in range(E):
            inval = rng.choice(T, size=T - longueurs[e], replace=False)
            masque[e, inval] = False
    t = np.arange(T)[None, :, None]
    X = rng.normal(0, 1, size=(E, T, n))
    if scenario == "derive_lineaire":
        X = X + 1.0 * (t - 4.5) / 4.5
    elif scenario == "bosse_precoce":
        X = X + np.where(t <= 1, 0.8, -0.2)
    elif scenario == "dependance":
        X = X + rng.normal(0, math.sqrt(0.3 / 0.7), size=(E, 1, n))
    elif scenario == "longueur":
        z = (longueurs - 7.5) / 1.7
        u = 0.9 * z[:, None] + rng.normal(0, 0.45, size=(E, n))
        X = X + (u * math.sqrt(0.3 / 0.7) / np.std(u))[:, None, :]
    X[~masque] = np.nan
    return X, masque


def partie_pas_fixe(n_melanges=10, n_boot=600, mondes=2):
    out = {}
    for isc, scenario in enumerate(("derive_lineaire", "bosse_precoce", "dependance", "longueur")):
        res = []
        for w in range(mondes):
            rng = np.random.default_rng(np.random.SeedSequence(GRAINE, spawn_key=(2, isc, w)))
            X, masque = monde(rng, scenario)
            E, S = X.shape[0], X.shape[2]
            perm = rng.permutation(E); plis = a.plis_de_perm(perm); effet = np.zeros(E)
            V0, VM, VP = np.zeros((S, 1, E)), np.zeros((S, n_melanges, E)), np.zeros((S, n_melanges, E))
            r0, r0m, r0p, r0c = [], [], [], []
            for si in range(S):
                Xs = X[:, :, si]
                r0.append(a.correlation_intra_episode(Xs, masque))
                r0c.append(a.correlation_intra_episode(a.centrer_par_pas(Xs, masque), masque))
                V0[si, 0] = a.un_passage(Xs, masque, plis, perm, effet, 0.0)[0][("ville", "processus_e")]
                for d in range(n_melanges):
                    Xm = a.melanger_actions(Xs, masque, rng); Xp = a.melanger_actions_pas_fixe(Xs, masque, rng)
                    r0m.append(a.correlation_intra_episode(Xm, masque)); r0p.append(a.correlation_intra_episode(Xp, masque))
                    VM[si, d] = a.un_passage(Xm, masque, plis, perm, effet, 0.0)[0][("ville", "processus_e")]
                    VP[si, d] = a.un_passage(Xp, masque, plis, perm, effet, 0.0)[0][("ville", "processus_e")]
            med = lambda A, idx: float(np.median(A[:, :, idx].mean(axis=(1, 2))))
            tout = np.arange(E)
            bD, bDp, bDd = [], [], []
            for _ in range(n_boot):
                idx = rng.integers(0, E, size=E)
                m0, mm, mp = med(V0, idx), med(VM, idx), med(VP, idx)
                bD.append(m0 - mm); bDp.append(m0 - mp); bDd.append(mp - mm)
            v0, vm, vp = med(V0, tout), med(VM, tout), med(VP, tout)
            bb = lambda x: round(float(np.quantile(x, 0.025)), 9)
            feuille = seuil_du_texte(round(v0, 9), bb(bD), round(vm, 9), bb(bDp), round(vp, 9), bb(bDd))
            res.append({"monde": w, "r0_median": round(float(np.median(r0)), 3), "r0_centre_par_pas": round(float(np.median(r0c)), 3),
                        "r0_melange": round(float(np.median(r0m)), 3), "r0_melange_pas_fixe": round(float(np.median(r0p)), 3),
                        "ville_reelles": round(v0, 4), "ville_melange": round(vm, 4), "ville_melange_pas_fixe": round(vp, 4),
                        "D": [round(v0 - vm, 4), bb(bD)], "D_prime": [round(v0 - vp, 4), bb(bDp)], "derive": [round(vp - vm, 4), bb(bDd)],
                        "feuille_du_seuil": feuille})
        out[scenario] = res
    json.dump({"pas_fixe": out, "note": "12 sondes indépendantes, E = 60, %d mélanges, %d rééchantillonnages appariés ; [point, borne basse]" % (n_melanges, n_boot)},
              sys.stdout, ensure_ascii=False, indent=1); print()


def partie_garde_endormie(dossier):
    """CV6-6 : si la garde des actions invalides dort, le test des gardes doit lever."""
    vrai = a.verifier_scores_invalides
    a.verifier_scores_invalides = lambda X, masque: None
    try:
        a.test_gardes(dossier); res = "NE LÈVE PAS (garde endormie non vue)"
    except (RuntimeError, AssertionError) as e:
        res = f"lève : {type(e).__name__}: {e}"
    finally:
        a.verifier_scores_invalides = vrai
    json.dump({"garde_des_actions_invalides_endormie": res}, sys.stdout, ensure_ascii=False, indent=1); print()


if __name__ == "__main__":
    partie = sys.argv[1]
    if partie == "lecture":
        partie_lecture(*sys.argv[2:5])
    elif partie == "pas_fixe":
        partie_pas_fixe()
    elif partie == "garde_endormie":
        partie_garde_endormie(sys.argv[2])
