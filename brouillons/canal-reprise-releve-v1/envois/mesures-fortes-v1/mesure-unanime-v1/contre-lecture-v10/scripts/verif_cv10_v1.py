"""Contre-lecture v10 de la mesure unanime : vérifications sur processeur, sans aucune donnée réelle.
Le script v8 et la lecture v6 sont importés SANS modification depuis la copie du dossier (fichiers identiques à l'octet).
Parties :
  arbre    — M2 ter : ma réécriture du Seuil (texte v10, lignes 219 à 229) contre `lecture_mecanique_v6.lire`, sur les
             64 combinaisons des six conditions binaires, aux bornes, à deux r₀ ; étiquettes contre les lignes des critères ;
             réserve (2a)/(2b) ; base : la sortie de la répétition générale v10 (format réel).
  pas_fixe — mélange à pas fixé : marges par pas et masque gardés ; dérive linéaire en t sans effet épisode, dépendance sans
             dérive, ni l'une ni l'autre ; r₀ et Ville (D, D′) par `un_passage` du script.
  gardes   — compte les appels de `verifier_scores_invalides` pendant un `main()` en mode réel sur le fichier de répétition
             (enveloppe posée sur le nom du module, jamais sur le fichier).
Graines : SeedSequence(2810202610, spawn_key=(partie, …)).
Usage : python -I -B verif_cv10_v1.py PARTIE COPIE_DOSSIER [CHEMIN_NPZ_REPETITION]
"""
import copy
import importlib.util
import io
import json
import os
import re
import sys
import contextlib

import numpy as np

PARTIE, COPIE = sys.argv[1], sys.argv[2]


def charger(nom, fichier):
    spec = importlib.util.spec_from_file_location(nom, os.path.join(COPIE, fichier))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def seuil_texte(v0, vm, vmp, bbD, bbDp, bbDd, alpha=0.05):
    """Réécriture du Seuil v10 (lignes 219 à 229), faite sur le texte seul ; arrondi à 1e-9 (CV6-4)."""
    a = lambda x: round(float(x), 9)
    v0, vm, vmp, bbD, bbDp, bbDd = map(a, (v0, vm, vmp, bbD, bbDp, bbDd))
    if v0 <= 0.05:
        return "(1)"
    if bbD <= 0:
        return "(2a)" if vm > alpha else "(2b)"
    if vm > alpha:
        return "(3a)" if bbDp > 0 else "(3b)"
    if bbDp > 0:
        return "(4a)" if vmp <= alpha else "(4b)"
    return "(4c)" if bbDd > 0 else "(4d)"


def arbre():
    lm = charger("lm", "lecture_mecanique_v6.py")
    base = json.load(open(os.path.join(COPIE, "sortie-reelle-v10-repetition.json"), encoding="utf-8"))
    tf = json.load(open(os.path.join(COPIE, "table-m2bis-m4-v8.json"), encoding="utf-8"))
    table, tm = tf["table"], tf["manifeste"]
    texte = open(os.path.join(COPIE, "preenregistrement-mesure-unanime-v10.md"), encoding="utf-8").read()
    etiquettes_criteres = dict(re.findall(r"^\| M2 ter \((\d[a-d]?)\) : « ([^»]+) »", texte, flags=re.M))

    def cas(v0, vm, vmp, bbD, bbDp, bbDd, r0=None):
        d = copy.deepcopy(base); r = d["resultats"]
        r["tau=0.0"]["ville:processus_e"]["reelles"]["mediane"] = v0
        r["melange_actions_permutees_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vm
        r["melange_pas_fixe_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vmp
        r["ville_tau0_reelles_moins_melange"]["intervalle_95"] = [bbD, bbD + 0.05]
        r["ville_tau0_reelles_moins_melange_pas_fixe"]["intervalle_95"] = [bbDp, bbDp + 0.05]
        r["ville_tau0_melange_pas_fixe_moins_melange"]["intervalle_95"] = [bbDd, bbDd + 0.05]
        if r0 is not None:
            r["correlation_intra_episode_r0"]["reelles"]["mediane"] = r0
        return lm.lire(d, table, table_manifeste=tm)

    out = {"combinaisons": 0, "desaccords_feuille": [], "desaccords_etiquette": [], "comptes": {}, "bornes": {}, "r0": {},
           "reserve_2a_2b": {}, "etiquettes_criteres": etiquettes_criteres}
    for v0 in (0.03, 0.08):
        for vm in (0.01, 0.07):
            for vmp in (0.01, 0.07):
                for bbD in (-0.01, 0.01):
                    for bbDp in (-0.01, 0.01):
                        for bbDd in (-0.01, 0.01):
                            lec = cas(v0, vm, vmp, bbD, bbDp, bbDd)
                            f_code = lec["verdicts"]["M2_ter"]
                            cle = f_code.split(")")[0] + ")"
                            f_txt = seuil_texte(v0, vm, vmp, bbD, bbDp, bbDd)
                            out["combinaisons"] += 1
                            out["comptes"][cle] = out["comptes"].get(cle, 0) + 1
                            if cle != f_txt:
                                out["desaccords_feuille"].append([v0, vm, vmp, bbD, bbDp, bbDd, f_code, f_txt])
                            etiq = f_code.split(") ", 1)[1]
                            if etiquettes_criteres.get(cle.strip("()")) != etiq:
                                out["desaccords_etiquette"].append([cle, etiq, etiquettes_criteres.get(cle.strip("()"))])
    bornes = {"v0=0,05": (0.05, 0.01, 0.01, 0.01, 0.01, 0.01), "v0=0,05+1e-12": (0.05 + 1e-12, 0.01, 0.01, 0.01, 0.01, 0.01),
              "v0=0,05+2e-9": (0.05 + 2e-9, 0.01, 0.01, 0.01, 0.01, 0.01), "bbD=0": (0.08, 0.07, 0.01, 0.0, 0.01, 0.01),
              "bbD=+1e-12": (0.08, 0.07, 0.01, 1e-12, 0.01, 0.01), "vm=0,05": (0.08, 0.05, 0.01, 0.01, 0.01, 0.01),
              "vmp=0,05": (0.08, 0.01, 0.05, 0.01, 0.01, 0.01), "bbDd=0": (0.08, 0.01, 0.01, 0.01, -0.01, 0.0),
              "bbDp=0": (0.08, 0.01, 0.01, 0.01, 0.0, -0.01)}
    for nom, args in bornes.items():
        out["bornes"][nom] = {"code": cas(*args)["verdicts"]["M2_ter"], "texte": seuil_texte(*args)}
    for r0 in (0.1, 0.7):
        out["r0"][str(r0)] = [cas(0.08, 0.01, 0.01, 0.01, 0.01, 0.01, r0=r0)["verdicts"]["M2_ter"],
                              cas(0.08, 0.07, 0.01, -0.01, 0.01, 0.01, r0=r0)["verdicts"]["M2_ter"]]
    for nom, args in {"2a_bbDp_pos": (0.08, 0.07, 0.01, -0.01, 0.01, 0.01), "2b_bbDp_pos": (0.08, 0.01, 0.01, -0.01, 0.01, 0.01),
                      "2b_bbDp_neg": (0.08, 0.01, 0.01, -0.01, -0.01, 0.01)}.items():
        l = cas(*args)
        out["reserve_2a_2b"][nom] = {"feuille": l["verdicts"]["M2_ter"], "reserves": l["reserves"], "audits": l["audits"]}
    return out


def pas_fixe():
    afa = charger("afa", "analyse_fausses_alertes_v8.py")
    ss = np.random.SeedSequence(2810202610, spawn_key=(2,))
    rng = np.random.default_rng(ss)
    E, T, S = 60, 10, 12
    masque = np.ones((E, T), bool)
    for e in range(E):
        k = rng.integers(5, T + 1); masque[e, k:] = False
        if masque[e].sum() > 5 and rng.random() < 0.4:  # quelques invalides au milieu : « pas » = indice brut
            masque[e, rng.integers(1, k - 1)] = False
    perm = np.random.default_rng(np.random.SeedSequence(2810202610, spawn_key=(2, 9))).permutation(E)
    plis = afa.plis_de_perm(perm)
    eff0 = np.zeros(E)
    mondes = {"derive_0,3_par_pas_sans_effet": (0.3, 0.0), "dependance_r0_0,3_sans_derive": (0.0, 0.3), "ni_l_un_ni_l_autre": (0.0, 0.0)}
    out = {}
    for nom, (pente, part) in mondes.items():
        r0o, r0p, r0m, vo, vp, vmm, marges_ok, masque_ok = [], [], [], [], [], [], True, True
        for s in range(S):
            g = np.random.default_rng(np.random.SeedSequence(2810202610, spawn_key=(2, s, len(nom))))
            u = g.normal(0, np.sqrt(part), size=(E, 1)) if part > 0 else 0.0
            X = u + g.normal(0, np.sqrt(1 - part), size=(E, T)) + pente * np.arange(T)[None, :]
            X[~masque] = np.nan
            Xp = afa.melanger_actions_pas_fixe(X, masque, g)
            Xm = afa.melanger_actions(X, masque, g)
            masque_ok &= bool(np.array_equal(np.isnan(Xp), ~masque) and np.array_equal(np.isnan(Xm), ~masque))
            for t in range(T):
                marges_ok &= bool(np.array_equal(np.sort(X[masque[:, t], t]), np.sort(Xp[masque[:, t], t])))
            r0o.append(afa.correlation_intra_episode(X, masque)); r0p.append(afa.correlation_intra_episode(Xp, masque)); r0m.append(afa.correlation_intra_episode(Xm, masque))
            vo.append(afa.un_passage(X, masque, plis, perm, eff0, 0.0)[0][("ville", "processus_e")].mean())
            vp.append(afa.un_passage(Xp, masque, plis, perm, eff0, 0.0)[0][("ville", "processus_e")].mean())
            vmm.append(afa.un_passage(Xm, masque, plis, perm, eff0, 0.0)[0][("ville", "processus_e")].mean())
        med = lambda v: round(float(np.median(v)), 4)
        out[nom] = {"marges_par_pas_gardees": marges_ok, "masque_garde": masque_ok,
                    "r0_origine": med(r0o), "r0_pas_fixe": med(r0p), "r0_melange": med(r0m),
                    "ville_reelles": med(vo), "ville_pas_fixe": med(vp), "ville_melange": med(vmm),
                    "D_reelles_moins_melange": round(med(vo) - med(vmm), 4), "Dprime_reelles_moins_pas_fixe": round(med(vo) - med(vp), 4),
                    "derive_pas_fixe_moins_melange": round(med(vp) - med(vmm), 4)}
    return out


def gardes():
    chemin = sys.argv[3]
    afa = charger("afa", "analyse_fausses_alertes_v8.py")
    compte = {"verifier_scores_invalides": 0, "verifier_scores": 0}
    orig_i, orig_s = afa.verifier_scores_invalides, afa.verifier_scores

    def env_i(X, m):
        compte["verifier_scores_invalides"] += 1; return orig_i(X, m)

    def env_s(X, m):
        compte["verifier_scores"] += 1; return orig_s(X, m)
    afa.verifier_scores_invalides, afa.verifier_scores = env_i, env_s
    emp = __import__("hashlib").sha256(open(chemin, "rb").read()).hexdigest()
    sys.argv = ["analyse_fausses_alertes_v8.py", "--reel", chemin, "--empreinte-attendue", emp, "--sondes-reelles", "3",
                "--sondes-placebo", "2", "--commit", "verif-cv10"]
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        afa.main()
    sortie = json.loads(tampon.getvalue())
    return {"appels": compte, "sondes": 5, "E": sortie["manifeste"]["E"], "note": "un_passage appelé 141 fois par sonde (20 mélanges + 20 pas fixés + 1 + 3×20 + 2×20)"}


if __name__ == "__main__":
    res = {"arbre": arbre, "pas_fixe": pas_fixe, "gardes": gardes}[PARTIE]()
    json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
    print()
