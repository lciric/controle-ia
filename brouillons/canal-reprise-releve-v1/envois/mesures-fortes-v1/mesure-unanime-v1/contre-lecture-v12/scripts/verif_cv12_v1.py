"""Contre-lecture v12 (sous-agent neuf Fable 5.1) — vérifications de fond, recalculées indépendamment de l'auteur :
 1. l'arbre de M2 ter (neuf feuilles) : le Seuil est réécrit ici depuis le texte seul, puis comparé à
    `lecture_mecanique_v8.lire` sur les 64 combinaisons des six conditions binaires × deux r₀ (0,1 et 0,7) ; bornes à 10⁻⁹ ;
    étiquettes mot pour mot ; réserve d'incohérence (2a)/(2b) ;
 2. les bornes de M1, M2 (contrôle), M2 bis, M3 (tenu / fragile / audit ; cellule à zéro), M4 (excès, borne basse, maximum,
    r₀), placebo ; la ligne de lecture (aucun faux « confirmé », aucun faux blocage) ;
 3. l'excès apparié de M4 recalculé par sonde (différence par sonde puis médiane) avec `un_passage` sur le fichier
    synthétique de la répétition, comparé à la sortie déposée ;
 4. le mélange à pas fixé (marges par pas et masque gardés ; dépendance détruite ; dérive avec le pas gardée) ;
 5. les chiffres cités (formules et table).
Les modules sont importés SANS modification depuis la copie du dossier (empreintes vérifiées ici). Aucune donnée de
`donnees/` n'est lue. Graines : SeedSequence(2810202612, …).
Usage : python -I -B verif_cv12_v1.py COPIE_DOSSIER SORTIE_REPETITION_DEPOSEE.json NPZ_REPETITION DOSSIER_SORTIES"""
import copy
import hashlib
import importlib.util
import itertools
import json
import math
import os
import sys

import numpy as np

COPIE, SORTIE_DEP, NPZ, OUT = sys.argv[1:5]
EMP = {"lecture_mecanique_v8.py": "7f28af2b7cd5c86a9d6d8003cffc2551514d0451b6b7e5fd6537e68c7626a623",
       "analyse_fausses_alertes_v8.py": "52b1760a09970526a926f2119dceeef7f20e2f280bdb6a6c2d890962556c5400",
       "table-m2bis-m4-v8.json": "f63faada54a7b2432315c6766be988ea3bcd0049cff35199ca8234da5c98b120"}
for n, e in EMP.items():
    h = hashlib.sha256(open(os.path.join(COPIE, n), "rb").read()).hexdigest()
    assert h == e, (n, h)


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lm = charger("lm", os.path.join(COPIE, "lecture_mecanique_v8.py"))
afa = charger("afa", os.path.join(COPIE, "analyse_fausses_alertes_v8.py"))
TABLE_DOC = json.load(open(os.path.join(COPIE, "table-m2bis-m4-v8.json"), encoding="utf-8"))
TABLE = TABLE_DOC["table"]
BASE = json.load(open(SORTIE_DEP, encoding="utf-8"))
ALPHA = 0.05


def arr(x):
    return round(float(x), 9)


# ----------------------------------------------------------------------------------------------------------------------
# 1. L'arbre de M2 ter, réécrit depuis le texte v12 (Seuil, lignes 216 à 230) — sans regarder le code
def seuil_texte(v0, vm, vmp, bbD, bbDp, bbDd, alpha=ALPHA):
    """Renvoie (étiquette, réserve_incohérence). Toute comparaison après arrondi à 10⁻⁹ (CV6-4)."""
    v0, vm, vmp, bbD, bbDp, bbDd = map(arr, (v0, vm, vmp, bbD, bbDp, bbDd))
    if v0 <= 0.05:
        return "(1) Ville tenue sur P3 à τ = 0", False
    if bbD <= 0:
        et = "(2a) marges seules" if vm > alpha else "(2b) non attribuable"
        return et, bbDp > 0
    if vm > alpha:
        return ("(3a) marges et dépendance" if bbDp > 0 else "(3b) marges et structure intra-épisode"), False
    if bbDp > 0:
        return ("(4a) dépendance naturelle suffisante" if vmp <= alpha else "(4b) dépendance établie, mélange à pas fixé au-dessus de α"), False
    return ("(4c) structure intra-épisode avec dérive de pas mesurée" if bbDd > 0 else "(4d) structure intra-épisode non attribuée"), False


ETIQUETTES_TEXTE = {"(1) Ville tenue sur P3 à τ = 0", "(2a) marges seules", "(2b) non attribuable", "(3a) marges et dépendance",
                    "(3b) marges et structure intra-épisode", "(4a) dépendance naturelle suffisante",
                    "(4b) dépendance établie, mélange à pas fixé au-dessus de α", "(4c) structure intra-épisode avec dérive de pas mesurée",
                    "(4d) structure intra-épisode non attribuée"}


def sortie_modifiee(v0=None, vm=None, vmp=None, bbD=None, bbDp=None, bbDd=None, r0=None, **autres):
    s = copy.deepcopy(BASE)
    r = s["resultats"]
    if v0 is not None: r["tau=0.0"]["ville:processus_e"]["reelles"]["mediane"] = v0
    if vm is not None: r["melange_actions_permutees_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vm
    if vmp is not None: r["melange_pas_fixe_tau=0"]["ville:processus_e"]["reelles"]["mediane"] = vmp
    if bbD is not None: r["ville_tau0_reelles_moins_melange"]["intervalle_95"][0] = bbD
    if bbDp is not None: r["ville_tau0_reelles_moins_melange_pas_fixe"]["intervalle_95"][0] = bbDp
    if bbDd is not None: r["ville_tau0_melange_pas_fixe_moins_melange"]["intervalle_95"][0] = bbDd
    if r0 is not None:
        r["correlation_intra_episode_r0"]["reelles"]["mediane"] = r0
        r["correlation_intra_episode_r0"]["centre_par_pas_reelles"]["mediane"] = r0
    for k, v in autres.items():
        if k == "m1": r["tau=0.0"]["par_action:max"]["reelles"]["mediane"] = v
        elif k == "m1bb": r["tau=0.0"]["par_action:max"]["reelles"]["mediane_intervalle_95"][0] = v
        elif k == "v2": r["tau=2.0"]["ville:processus_e"]["reelles"]["mediane"] = v
        elif k == "m2bis": r["ville_tau2_moins_tau0"]["mediane"] = v
        elif k == "m2bis_bh": r["ville_tau2_moins_tau0"]["intervalle_95"][1] = v
        elif k == "exces": r["M4_exces_apparie"]["exces"] = v
        elif k == "exces_bb": r["M4_exces_apparie"]["intervalle_95"][0] = v
        elif k == "max4": r["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["reelles"]["mediane"] = v
        elif k == "max4_placebo": r["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["placebos"]["mediane"] = v
        elif k == "cellule": (t, st, med, q3) = v; r[f"tau={t}"][f"conforme:{st}"]["reelles"]["mediane"] = med; r[f"tau={t}"][f"conforme:{st}"]["reelles"]["q3"] = q3
        elif k == "cellule_placebo": (t, st, med) = v; r[f"tau={t}"][f"conforme:{st}"]["placebos"]["mediane"] = med
        elif k == "bras_zero": (bloc, st) = v; r[bloc][f"conforme:{st}"]["reelles"]["mediane"] = 0.0; r[bloc][f"conforme:{st}"]["reelles"]["q3"] = 0.0
        else: raise KeyError(k)
    return s


def lire(s):
    return lm.lire(s, TABLE, ALPHA, None, TABLE_DOC["manifeste"], None)


res = {"1_arbre": {}, "2_bornes": {}, "3_exces_M4": {}, "4_pas_fixe": {}, "5_chiffres": {}}
A = res["1_arbre"]
VAL = {"v0": (0.04, 0.10), "bbD": (-0.01, 0.02), "vm": (0.08, 0.02), "bbDp": (0.02, -0.01), "vmp": (0.02, 0.08), "bbDd": (0.01, -0.01)}
desaccords, feuilles, reserves_ok, par_r0 = [], {}, True, {}
for r0 in (0.1, 0.7):
    par_r0[r0] = {}
    for bits in itertools.product((0, 1), repeat=6):
        kw = {k: VAL[k][b] for k, b in zip(("v0", "bbD", "vm", "bbDp", "vmp", "bbDd"), bits)}
        attendu, res_att = seuil_texte(**kw)
        lec = lire(sortie_modifiee(r0=r0, **kw))
        obtenu = lec["verdicts"]["M2_ter"]
        res_obt = any("incohérence entre les deux mélanges" in x for x in lec["reserves"])
        feuilles[obtenu] = feuilles.get(obtenu, 0) + 1
        par_r0[r0][bits] = obtenu
        if obtenu != attendu:
            desaccords.append({"r0": r0, "entree": kw, "texte": attendu, "code": obtenu})
        if res_obt != res_att:
            reserves_ok = False
            desaccords.append({"r0": r0, "entree": kw, "reserve_texte": res_att, "reserve_code": res_obt})
A["combinaisons"] = 128
A["desaccords"] = desaccords
A["etiquettes_du_code_mot_pour_mot_celles_du_texte"] = set(feuilles) == ETIQUETTES_TEXTE
A["feuilles_atteintes_par_128_combinaisons"] = dict(sorted(feuilles.items()))
A["reserve_2a_2b_conforme"] = reserves_ok
A["r0_jamais_condition"] = par_r0[0.1] == par_r0[0.7]
# bornes de l'arbre
b = {}
b["v0=0.05 → (1)"] = lire(sortie_modifiee(v0=0.05))["verdicts"]["M2_ter"]
b["v0=0.05+1e-12 → (1)"] = lire(sortie_modifiee(v0=0.05 + 1e-12))["verdicts"]["M2_ter"]
b["v0=0.05+2e-9, bbD=0.02, vm=0.02, bbDp=0.02, vmp=0.02 → (4a)"] = lire(sortie_modifiee(v0=0.05 + 2e-9, bbD=0.02, vm=0.02, bbDp=0.02, vmp=0.02))["verdicts"]["M2_ter"]
b["v0=0.10, bbD=0 (≤0), vm=0.08 → (2a)"] = lire(sortie_modifiee(v0=0.10, bbD=0.0, vm=0.08))["verdicts"]["M2_ter"]
b["v0=0.10, bbD=1e-12 (≤0 après arrondi), vm=0.02 → (2b)"] = lire(sortie_modifiee(v0=0.10, bbD=1e-12, vm=0.02))["verdicts"]["M2_ter"]
b["v0=0.10, bbD=2e-9, vm=0.05 (pas > α), bbDp=0.02, vmp=0.05 (≤ α) → (4a)"] = lire(sortie_modifiee(v0=0.10, bbD=2e-9, vm=0.05, bbDp=0.02, vmp=0.05))["verdicts"]["M2_ter"]
b["v0=0.10, bbD=0.02, vm=0.05+2e-9, bbDp=0 → (3b)"] = lire(sortie_modifiee(v0=0.10, bbD=0.02, vm=0.05 + 2e-9, bbDp=0.0))["verdicts"]["M2_ter"]
b["v0=0.10, bbD=0.02, vm=0.02, bbDp=0.02, vmp=0.05+2e-9 → (4b)"] = lire(sortie_modifiee(v0=0.10, bbD=0.02, vm=0.02, bbDp=0.02, vmp=0.05 + 2e-9))["verdicts"]["M2_ter"]
b["v0=0.10, bbD=0.02, vm=0.02, bbDp=0, bbDd=0 → (4d)"] = lire(sortie_modifiee(v0=0.10, bbD=0.02, vm=0.02, bbDp=0.0, bbDd=0.0))["verdicts"]["M2_ter"]
b["… bbDd=1e-9 → (4c)"] = lire(sortie_modifiee(v0=0.10, bbD=0.02, vm=0.02, bbDp=0.0, bbDd=1e-9))["verdicts"]["M2_ter"]
b["… bbDd=1e-12 (→ 0) → (4d)"] = lire(sortie_modifiee(v0=0.10, bbD=0.02, vm=0.02, bbDp=0.0, bbDd=1e-12))["verdicts"]["M2_ter"]
A["bornes"] = b
A["bornes_conformes"] = all(k.split("→ ")[-1].strip() in v for k, v in b.items())

# ----------------------------------------------------------------------------------------------------------------------
# 2. Bornes des autres énoncés et ligne de lecture
Bn = res["2_bornes"]
V = lambda s, k: lire(s)["verdicts"][k]
m1 = {}
m1["med 0.06, bb 0.03+1e-9 → confirmé"] = V(sortie_modifiee(m1=0.06, m1bb=0.03 + 1e-9), "M1")
m1["med 0.06, bb 0.03 → non concluant"] = V(sortie_modifiee(m1=0.06, m1bb=0.03), "M1")
m1["med 0.06-2e-9, bb 0.04 → non concluant"] = V(sortie_modifiee(m1=0.06 - 2e-9, m1bb=0.04), "M1")
m1["med 0.03 → réfuté"] = V(sortie_modifiee(m1=0.03, m1bb=0.0), "M1")
m1["med 0.03+2e-9 → non concluant"] = V(sortie_modifiee(m1=0.03 + 2e-9, m1bb=0.0), "M1")
Bn["M1"] = m1
m2 = {}
m2["v2 0.075 → attendu"] = V(sortie_modifiee(v2=0.075), "M2_controle")
m2["v2 0.075-2e-9 → AUDIT"] = V(sortie_modifiee(v2=0.075 - 2e-9), "M2_controle")
m2["r0 0.3, bh 0 → AUDIT RÉFUTÉE"] = V(sortie_modifiee(r0=0.3, m2bis_bh=0.0), "M2_bis")
m2["r0 0.3, bh 1e-9 → pas d'audit"] = V(sortie_modifiee(r0=0.3, m2bis_bh=1e-9), "M2_bis")
m2["r0 0.5, bh -0.1 → aucune réfutation"] = V(sortie_modifiee(r0=0.5, m2bis_bh=-0.1), "M2_bis")
m2["r0 0.2 (table 0.104), med 0.154 → conforme"] = V(sortie_modifiee(r0=0.2, m2bis=0.15416666666666669), "M2_bis")
m2["r0 0.2, med 0.104+0.05+2e-9 → hors table"] = V(sortie_modifiee(r0=0.2, m2bis=0.10416666666666669 + 0.05 + 2e-9), "M2_bis")
Bn["M2_M2bis"] = m2
m3 = {}
L = arr(BASE["manifeste"]["niveau_conforme_L"]); Bm = arr(max(2 * L, 0.10))
m3["L, B"] = (L, Bm)
m3["cellule 0.10 (= B) → tenu"] = V(sortie_modifiee(cellule=("2.0", "page", 0.10, 0.12)), "M3")
m3["cellule 0.10+2e-9 → AUDIT"] = V(sortie_modifiee(cellule=("2.0", "page", 0.10 + 2e-9, 0.12)), "M3")
m3["cellule 0.08 (= 1,6 L) → tenu"] = V(sortie_modifiee(cellule=("2.0", "page", 0.08, 0.09)), "M3")
m3["cellule 0.08+2e-9 → fragile"] = V(sortie_modifiee(cellule=("2.0", "page", 0.08 + 2e-9, 0.09)), "M3")
m3["cellule 0.02 (= 0,4 L) → tenu"] = V(sortie_modifiee(cellule=("2.0", "page", 0.02, 0.03)), "M3")
m3["cellule 0.02-2e-9 → fragile"] = V(sortie_modifiee(cellule=("2.0", "page", 0.02 - 2e-9, 0.03)), "M3")
s0 = sortie_modifiee(cellule=("0.0", "max", 0.0, 0.0))
m3["cellule med 0, q3 0 → cellule_a_zero AUDIT"] = V(s0, "cellule_a_zero")
m3["cellule med 0, q3 0.017 → aucune"] = V(sortie_modifiee(cellule=("0.0", "max", 0.0, 0.017)), "cellule_a_zero")
lz = lire(sortie_modifiee(bras_zero=("M4_dependance_seule_variance_constante_tau=2", "max")))
m3["bras à zéro → réserve, pas audit"] = (lz["verdicts"]["cellule_a_zero"], [x[:60] for x in lz["reserves"]], lz["audits"])
Bn["M3"] = m3
m4 = {}
m4["exces 0.02, bb 0.01, max 0.013 → non concluant"] = V(sortie_modifiee(exces=0.02, exces_bb=0.01, max4=0.013), "M4")
m4["exces 0.02+1e-12 → non concluant"] = V(sortie_modifiee(exces=0.02 + 1e-12, exces_bb=0.01, max4=0.013), "M4")
m4["exces 0.02+2e-9 → confirmé"] = V(sortie_modifiee(exces=0.02 + 2e-9, exces_bb=0.01, max4=0.013), "M4")
m4["exces 0.05, bb 0 → non concluant"] = V(sortie_modifiee(exces=0.05, exces_bb=0.0, max4=0.013), "M4")
m4["exces 0.05, bb 1e-9 → confirmé"] = V(sortie_modifiee(exces=0.05, exces_bb=1e-9, max4=0.013), "M4")
m4["exces 0.05, bb 0.01, max 0.08 → confirmé"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.08), "M4")
m4["max 0.081 → non concluant"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.081), "M4")
m4["exces 0 → réfuté"] = V(sortie_modifiee(exces=0.0, exces_bb=-0.01, max4=0.013), "M4")
m4["exces -1e-12 → réfuté"] = V(sortie_modifiee(exces=-1e-12, exces_bb=-0.01, max4=0.013), "M4")
m4["exces 0.01, bb -0.01 → non concluant"] = V(sortie_modifiee(exces=0.01, exces_bb=-0.01, max4=0.013), "M4")
m4["max 0.10 → pas d'audit (confirmé ? non : max > 0.08 → non concluant)"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.10), "M4")
m4["max 0.10+2e-9 → AUDIT"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.10 + 2e-9), "M4")
m4["max 0.10+2e-9, r0 0.5 → AUDIT (à tout r₀)"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.10 + 2e-9, r0=0.5), "M4")
m4["r0 0.5 → non lisible"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.013, r0=0.5), "M4")
m4["r0 0.5-2e-9 → confirmé"] = V(sortie_modifiee(exces=0.05, exces_bb=0.01, max4=0.013, r0=0.5 - 2e-9), "M4")
Bn["M4"] = m4
pl = {}
pl["écart cellule 0.05 → mêmes médianes"] = V(sortie_modifiee(cellule=("1.0", "page", 0.06, 0.07), cellule_placebo=("1.0", "page", 0.01)), "placebo")
pl["écart cellule 0.05+2e-9 → AUDIT"] = V(sortie_modifiee(cellule=("1.0", "page", 0.06 + 2e-9, 0.07), cellule_placebo=("1.0", "page", 0.01)), "placebo")
pl["écart max M4 0.06 → AUDIT"] = V(sortie_modifiee(max4=0.07, max4_placebo=0.01), "placebo")
Bn["placebo"] = pl
lg = {}
def ligne(s): l = lire(s); return (l["ligne_de_lecture"][:70], l["audits"])
lg["base (répétition) → première ligne, aucun audit"] = ligne(BASE)
lg["M1 confirmé, M4 confirmé, mais M3 audit → AUDIT, pas première ligne"] = ligne(sortie_modifiee(cellule=("2.0", "page", 0.11, 0.12)))
lg["M1 confirmé, M4 confirmé, M2 bis réfutée (r0 0.2) → AUDIT"] = ligne(sortie_modifiee(r0=0.2, m2bis_bh=0.0))
lg["M1 confirmé, M4 confirmé, placebo écart → AUDIT"] = ligne(sortie_modifiee(max4=0.07, max4_placebo=0.01))
lg["M1 confirmé, M4 non concluant → pas de dépassement établi"] = ligne(sortie_modifiee(exces=0.01, exces_bb=-0.01))
lg["M1 confirmé, M4 réfuté → pas de dépassement établi"] = ligne(sortie_modifiee(exces=-0.01, exces_bb=-0.02))
lg["r0 0.6 → M4 non lisible ; M2 ter porte"] = ligne(sortie_modifiee(r0=0.6))
lg["M3 fragile seul → la ligne continue (première ligne)"] = ligne(sortie_modifiee(cellule=("2.0", "page", 0.09, 0.095)))
lg["M2 bis hors table seul → la ligne continue"] = ligne(sortie_modifiee(m2bis=0.3, m2bis_bh=0.4))
lg["M1 non concluant, M4 confirmé → ni première ligne ni blocage"] = ligne(sortie_modifiee(m1=0.05, m1bb=0.02))
lg["M1 réfuté → voir les lignes des critères"] = ligne(sortie_modifiee(m1=0.02, m1bb=0.0))
Bn["ligne_de_lecture"] = lg

# ----------------------------------------------------------------------------------------------------------------------
# 3. Excès apparié de M4 recalculé par sonde sur le fichier de la répétition (jamais donnees/)
E3 = res["3_exces_M4"]
emp_npz = hashlib.sha256(open(NPZ, "rb").read()).hexdigest()
assert emp_npz == "447dc136dde083f68d1f9899344207bd5b8a6caf56c95b441d1c492dd72cb709", emp_npz
X, masque, noms, reelles, placebos, meta = afa.charger_reel(NPZ, emp_npz, 3, 2)
E = X.shape[0]
ss = np.random.SeedSequence(afa.ENTROPIE)
rng_plis = np.random.default_rng(ss.spawn(3)[0])
perm = rng_plis.permutation(E); plis = afa.plis_de_perm(perm)
effets2 = [np.random.default_rng(s).normal(size=E) for s in np.random.SeedSequence(afa.ENTROPIE, spawn_key=(20, 1)).spawn(20)]
effet0 = np.random.default_rng(np.random.SeedSequence(afa.ENTROPIE, spawn_key=(0, 1)).spawn(20)[0]).normal(size=E)
SOMMES = ("somme_terminale", "somme_sequentielle", "page", "processus_e", "balayage")
exces_par_sonde, q_bras, q_0, max_bras = [], [], [], []
for si in reelles:
    Xs = X[:, :, si]
    al0, _ = afa.un_passage(Xs, masque, plis, perm, effet0, 0.0)
    t0 = float(np.mean([al0[("conforme", s)].mean() for s in SOMMES]))
    taux_bras = []
    mx = []
    for di in range(20):
        al, _ = afa.un_passage(Xs, masque, plis, perm, effets2[di], 2.0, calibrage_sans_effet=True, variance_constante=True)
        taux_bras.append([al[("conforme", s)].mean() for s in SOMMES])
        mx.append(al[("conforme", "max")].mean())
    tb = float(np.mean(taux_bras))  # moyenne sur tirages et sur les cinq sommes
    exces_par_sonde.append(tb - t0); q_bras.append(tb); q_0.append(t0); max_bras.append(float(np.mean(mx)))
r4 = BASE["resultats"]["M4_exces_apparie"]
E3["exces_par_sonde_recalcule"] = [round(x, 6) for x in exces_par_sonde]
E3["exces_mediane_recalculee"] = round(float(np.median(exces_par_sonde)), 9)
E3["exces_sortie_deposee"] = round(r4["exces"], 9)
E3["difference_des_medianes_recalculee"] = round(float(np.median(q_bras) - np.median(q_0)), 9)
E3["difference_des_medianes_deposee"] = round(r4["difference_des_medianes"], 9)
E3["quantite_M4_recalculee"] = round(float(np.median(q_bras)), 9)
E3["quantite_M4_deposee"] = round(BASE["resultats"]["M4_quantite"]["mediane"], 9)
E3["quantite_tau0_recalculee"] = round(float(np.median(q_0)), 9)
E3["quantite_tau0_deposee"] = round(r4["quantite_tau0"], 9)
E3["max_conforme_bras_recalcule"] = round(float(np.median(max_bras)), 9)
E3["max_conforme_bras_depose"] = round(BASE["resultats"]["M4_dependance_seule_variance_constante_tau=2"]["conforme:max"]["reelles"]["mediane"], 9)
E3["conforme"] = (abs(E3["exces_mediane_recalculee"] - E3["exces_sortie_deposee"]) < 1e-9 and
                  abs(E3["quantite_M4_recalculee"] - E3["quantite_M4_deposee"]) < 1e-9 and
                  abs(E3["max_conforme_bras_recalcule"] - E3["max_conforme_bras_depose"]) < 1e-9)
# cohérence lecture ↔ sortie déposée
lec_base = lire(BASE)
E3["lecture_M4_exces_egal_sortie"] = lec_base["quantites"]["M4"]["exces"] == r4["exces"]
E3["lecture_M4_verdict_base"] = lec_base["verdicts"]["M4"]
# un défaut de niveau commun (+c sur les deux termes) laisse l'excès inchangé
E3["defaut_de_niveau_commun_annule_dans_exces"] = round(float(np.median((np.array(q_bras) + 0.03) - (np.array(q_0) + 0.03))), 9) == E3["exces_mediane_recalculee"]

# ----------------------------------------------------------------------------------------------------------------------
# 4. Mélange à pas fixé
P = res["4_pas_fixe"]
rng = np.random.default_rng(np.random.SeedSequence(2810202612, spawn_key=(4,)))
Ep, T = 60, 10
masque_p = np.ones((Ep, T), bool)
for e in range(Ep):
    k = int(rng.integers(5, T + 1)); masque_p[e, k:] = False
masque_p[::7, 3] = False  # une action invalide au milieu : le « pas » doit être l'indice brut
# (a) effet épisode r₀ = 0,3, aucune dérive
var_u = 0.3 / 0.7
Xa = rng.normal(0, math.sqrt(var_u), size=(Ep, 1)) + rng.normal(0, 1, size=(Ep, T)); Xa[~masque_p] = np.nan
# (b) dérive linéaire 0,3 par pas, aucun effet épisode
Xb = 0.3 * np.arange(T)[None, :] + rng.normal(0, 1, size=(Ep, T)); Xb[~masque_p] = np.nan
# (c) rien
Xc = rng.normal(0, 1, size=(Ep, T)); Xc[~masque_p] = np.nan
def verif(Xo):
    rm = np.random.default_rng(np.random.SeedSequence(2810202612, spawn_key=(4, 1)))
    rp = np.random.default_rng(np.random.SeedSequence(2810202612, spawn_key=(4, 2)))
    Xm, Xp = afa.melanger_actions(Xo, masque_p, rm), afa.melanger_actions_pas_fixe(Xo, masque_p, rp)
    marges_pas = all(np.array_equal(np.sort(Xp[masque_p[:, t], t]), np.sort(Xo[masque_p[:, t], t])) for t in range(T))
    masque_garde = np.array_equal(np.isnan(Xp), ~masque_p) and np.array_equal(np.isnan(Xm), ~masque_p)
    marges_tot = np.array_equal(np.sort(Xm[masque_p]), np.sort(Xo[masque_p]))
    moy_pas = lambda Z: [round(float(np.mean(Z[masque_p[:, t], t])), 3) for t in range(T)]
    return {"marges_par_pas_gardees_pas_fixe": bool(marges_pas), "masques_gardes": bool(masque_garde), "marges_totales_gardees_melange": bool(marges_tot),
            "r0": {"origine": round(afa.correlation_intra_episode(Xo, masque_p), 3), "melange": round(afa.correlation_intra_episode(Xm, masque_p), 3),
                   "pas_fixe": round(afa.correlation_intra_episode(Xp, masque_p), 3), "centre_par_pas": round(afa.correlation_intra_episode(afa.centrer_par_pas(Xo, masque_p), masque_p), 3)},
            "moyenne_par_pas": {"origine": moy_pas(Xo), "pas_fixe": moy_pas(Xp), "melange": moy_pas(Xm)},
            "moyenne_par_pas_identique_pas_fixe": moy_pas(Xo) == moy_pas(Xp)}
P["a_effet_episode_r0_0.3"] = verif(Xa); P["b_derive_0.3_par_pas"] = verif(Xb); P["c_rien"] = verif(Xc)
P["garde_scores_invalides_leve_sur_artefact"] = False
try:
    Xart = afa.melanger_actions_pas_fixe(Xa, masque_p, rng).copy(); Xart[~masque_p] = 0.0
    afa.verifier_scores_invalides(Xart, masque_p)
except RuntimeError as e:
    P["garde_scores_invalides_leve_sur_artefact"] = str(e)

# ----------------------------------------------------------------------------------------------------------------------
# 5. Chiffres cités
C = res["5_chiffres"]
C["1-0.99^50"] = round(1 - 0.99 ** 50, 4)
C["M1 T uniforme 5..10 : moyenne de 1-(0.99)^T"] = round(float(np.mean([1 - 0.99 ** t for t in range(5, 11)])), 4)
C["M1 T=8"] = round(1 - 0.99 ** 8, 4)
K = 39; rang = afa.rang_conforme(K, ALPHA)
C["K=39 : rang, niveau"] = (rang, round(afa.niveau_conforme(K, ALPHA), 4), "2/40 = 0,05")
C["E=60 : plis de 6, calibrage 54 = 15 + 39"] = (60 - math.ceil(60 / 10), 60 - math.ceil(60 / 10) - 15)
C["E=44 : K"] = 44 - math.ceil(44 / 10) - 15
t = TABLE
C["table ville τ=0 (0,00 ; 0,033 ; 0,083 ; 0,133)"] = [round(t[k]["ville_tau0_median"], 3) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["table ville τ=2 (0,138 à 0,152)"] = [round(t[k]["ville_tau2_median"], 4) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["table M2 bis (+0,138 ; +0,104 ; +0,065 ; +0,019)"] = [round(t[k]["difference_mediane"], 3) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["table excès M4 (0,143 ; 0,073 ; 0,027 ; 0,006)"] = [round(t[k]["M4_exces_median"], 4) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["table quantité brute M4 (0,19 ; 0,12 ; 0,075 ; 0,054)"] = [round(t[k]["M4_sommes_median"], 4) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["table max M4 (0,019 à 0,026 ; 0,4 à 0,5 L)"] = [round(t[k]["M4_max_median"], 4) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["max M4 en unités de L=0,05"] = [round(t[k]["M4_max_median"] / 0.05, 2) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["M4 : excès = brute − sommes τ=0 dans la table ?"] = [round(t[k]["M4_sommes_median"] - t[k]["sommes_tau0_median"], 4) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]
C["note : la table ne garantit pas excès = différence des médianes (excès = médiane des différences)"] = True
C["interpolation à r0=0.196 (répétition) : excès, ville τ=0, M2 bis"] = (round(lm.interpoler(TABLE, "M4_exces_median", 0.196), 4), round(lm.interpoler(TABLE, "ville_tau0_median", 0.196), 4), round(lm.interpoler(TABLE, "difference_mediane", 0.196), 4))
C["r0 médian de la répétition déposée"] = round(BASE["resultats"]["correlation_intra_episode_r0"]["reelles"]["mediane"], 4)
C["r0 estimé de la table ≈ r0 nominal"] = [round(t[k]["r0_estime_median"], 3) for k in ("r0=0.0", "r0=0.2", "r0=0.5", "r0=0.8")]


class Enc(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (set, tuple)): return sorted(o) if isinstance(o, set) else list(o)
        if isinstance(o, (np.integer,)): return int(o)
        if isinstance(o, (np.floating,)): return float(o)
        if isinstance(o, np.bool_): return bool(o)
        return str(o)


def normaliser(o):
    if isinstance(o, dict): return {str(k): normaliser(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [normaliser(v) for v in o]
    if isinstance(o, set): return sorted(o)
    return o


os.makedirs(OUT, exist_ok=True)
for k, v in res.items():
    with open(os.path.join(OUT, f"sortie-verif-cv12-{k}-v1.json"), "w", encoding="utf-8") as f:
        json.dump(normaliser(v), f, ensure_ascii=False, indent=1, cls=Enc)
print(json.dumps({"arbre_desaccords": len(desaccords), "etiquettes_ok": A["etiquettes_du_code_mot_pour_mot_celles_du_texte"],
                  "r0_jamais_condition": A["r0_jamais_condition"], "bornes_arbre_ok": A["bornes_conformes"], "reserve_ok": reserves_ok,
                  "exces_M4_conforme": E3["conforme"], "exces": (E3["exces_mediane_recalculee"], E3["exces_sortie_deposee"])}, ensure_ascii=False))
