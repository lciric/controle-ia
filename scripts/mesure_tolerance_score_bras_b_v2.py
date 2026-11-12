"""[v2 : graines par `numpy.random.SeedSequence` (R9, contre-lecture R-1746) ; la v1 tirait par `default_rng(0)`] Mesure de justification de la tolérance de G4 (addendum du bras B v2, § 1) : scores de W recalculés des activations VERSÉES de R1 v4 ; aucune action rejouée, aucun résultat du bras B.

    PYTHONPATH=src python3 scripts/mesure_tolerance_score_bras_b_v2.py
"""
import json, numpy as np, sys
from pathlib import Path
sys.path.insert(0, "src")
from controle_ia.audit_fuite_r1_v4 import bras_b_v3 as bb
from controle_ia.manifeste import generateur
c=json.load(open("docs/notes/g0-deux-semaines-v1/config-bras-b-t06-v1.json"))
R=Path(".")
d=bb.charger_audit(R/c["chemin_maximum"],R/c["chemin_complement"],R/c["chemin_scores"],c["lignes"],c["largeur"],c["indice_couche"],c["couches"],c["n_taches"],c["n_pas"])
el=d["fidele"]&d["notee"]
man=json.load(open(R/c["chemin_audit_manifeste"]))
pli=bb.carte_des_plis(d,generateur(man["graines"]["plis"]),c["n_plis"],c["n_taches"])
modeles=bb.modeles_de_pli(d["maximum"],d["condition"],el,pli)
s=bb.scores_par_modeles(d["maximum"],el,pli,modeles)
print("eligibles",int(el.sum()))
for cond in ("honnete","mention","saboteur"):
    m=el&(d["condition"]==cond); print(cond,"n",int(m.sum()),"moy %.3f sd %.3f"%(s[m].mean(),s[m].std()))
print("sd globale des scores %.3f"%s[el].std())
# dispersion entre plis : écart-type des moyennes de score par pli (par condition)
for cond in ("honnete","saboteur"):
    mm=[s[el&(d["condition"]==cond)&(pli==k)].mean() for k in sorted(modeles)]
    print("moyennes par pli",cond,np.round(mm,3),"sd entre plis %.3f"%np.std(mm))
# bruit de précision : activations perturbées par un arrondi relatif de 2^-p
X=d["maximum"].astype(np.float64)
ENTROPIE = 20261108                                                 # R9 : entropie écrite, une SeedSequence, un générateur par usage (spawn)
rng_bruit, rng_aires = (np.random.default_rng(g) for g in np.random.SeedSequence(ENTROPIE).spawn(2))
rng = rng_bruit
for p,nom in ((11,"float16 (arrondi unique)"),(8,"bfloat16 (8 bits de mantisse)"),(6,"bruit relatif 2^-6")):
    eps=2.0**-p
    Xp=X*(1+eps*rng.uniform(-1,1,size=X.shape))
    sp=bb.scores_par_modeles(Xp,el,pli,modeles)
    dd=np.abs(sp[el]-s[el]); print(nom,"écart de score: moyen %.4f, p99 %.4f, max %.4f"%(dd.mean(),np.quantile(dd,.99),dd.max()))
# effet d'un décalage uniforme/bruité des scores contrefactuels sur les aires: on prend le saboteur d'origine comme proxy
from controle_ia.sondes.evaluation import aire_sous_courbe
H=el&(d["condition"]=="honnete"); S=el&(d["condition"]=="saboteur"); M=el&(d["condition"]=="mention")
def auc(sc,pos,neg):
    sel=pos|neg; return aire_sous_courbe(sc[sel],pos[sel].astype(int))
base_sm=auc(s,S,M); base_sh=auc(s,S,H)
print("aires de référence S/M %.4f  S/H %.4f"%(base_sm,base_sh))
for t in (0.005,0.01,0.02,0.05,0.1,0.2,0.5):
    worst=0
    for _ in range(5):
        sp=s+rng_aires.uniform(-t,t,size=s.shape)
        worst=max(worst,abs(auc(sp,S,M)-base_sm),abs(auc(sp,S,H)-base_sh))
    print("bruit uniforme ±%.3f sur les scores : écart maximal d'aire %.4f"%(t,worst))
