"""Extrait les chiffres du § 3 du rapport v5 des sorties d'effet d'unité. Usage : python3 -I -B verif_section3.py DOSSIER"""
import json, os, sys
D = sys.argv[1]
f = {'s0': 'simulation-puissance-garde-delta-v5-sortie-rejeu-v4-principale.json', 'l05': 'simulation-puissance-garde-delta-v5-sortie-effet-unite-0.5.json',
     'l10': 'simulation-puissance-garde-delta-v5-sortie-effet-unite-1.0.json', 'b': 'simulation-puissance-garde-delta-v5-sortie-effet-beta-0.17.json'}
S = {k: json.load(open(os.path.join(D, v)))['cellules'] for k, v in f.items()}
suf = {'s0': '', 'l05': '_effetA0.5', 'l10': '_effetA1.0', 'b': '_betaA_rho0.17_lien_coupe'}
def c(k, K, t, kk, delta=0.05, lien=True):
    s = suf[k] + ('_lien_coupe' if (not lien and k in ('l05', 'l10')) else '')
    return S[k][f'binomiale_Kh{K}_Ks{K}_taux{t}{s}|delta={delta}|n=160|n_garde=160|biais=0.0|k={kk}']['160.0']
print('garde seule k=1 : σ0 / l0.5 / l1.0 / bêta')
for K in (10, 3):
    for t in (0.01, 0.1):
        print(K, t, [round(c(k, K, t, 1)['garde_seule']['part'], 3) for k in ('s0', 'l05', 'l10', 'b')])
print('contraste k=1, K=10, τ=0.01 :', [round(c(k, 10, 0.01, 1)['k_contrastes']['part'], 3) for k in ('s0', 'l05', 'l10', 'b')])
print('min des k gardes, l1.0, K=10, τ=0.10 : k=1,3,8', [round(c('l10', 10, 0.1, kk)['k_gardes']['part'], 3) for kk in (1, 3, 8)])
print('fiche lien tenu / coupé (l1.0)')
for K, t, kk, d in ((10, 0.1, 1, 0.05), (10, 0.1, 3, 0.05), (10, 0.1, 8, 0.05), (10, 0.01, 3, 0.05), (10, 0.01, 8, 0.05), (3, 0.1, 8, 0.1)):
    print(K, t, kk, d, round(c('l10', K, t, kk, d)['fiche_entiere']['part'], 4), round(c('l10', K, t, kk, d, False)['fiche_entiere']['part'], 4),
          'écart', round(c('l10', K, t, kk, d, False)['fiche_entiere']['part'] - c('l10', K, t, kk, d)['fiche_entiere']['part'], 4))
print('fiche k=8 K=10 τ=0.01 l1.0 lien tenu', c('l10', 10, 0.01, 8)['fiche_entiere']['part'])
m = S['l10']['binomiale_Kh10_Ks10_taux0.01_effetA1.0|delta=0.05|n=160|n_garde=160|biais=0.0|k=1']['moments_tires']
print('moments l1.0 K10 τ0.01', m)
m = S['l10']['binomiale_Kh10_Ks10_taux0.1_effetA1.0|delta=0.05|n=160|n_garde=160|biais=0.0|k=1']['moments_tires']
print('moments l1.0 K10 τ0.10', m)
L = json.load(open(os.path.join(D, f['l10'])))['lois']
for nom in ('binomiale_Kh10_Ks10_taux0.01_effetA1.0', 'binomiale_Kh10_Ks10_taux0.1_effetA1.0'):
    print(nom, json.dumps(L[nom]['decomposition_effet_unite'], ensure_ascii=False)[:900])
# plus grand écart lien tenu - coupé sur toutes les cellules communes
ec = []
for et, v in S['l10'].items():
    if '_lien_coupe' in et: continue
    et2 = et.replace('_effetA1.0|', '_effetA1.0_lien_coupe|')
    if et2 in S['l10']:
        ec.append((round(S['l10'][et2]['160.0']['fiche_entiere']['part'] - v['160.0']['fiche_entiere']['part'], 4), et))
print('écart max coupé − tenu (σ=1)', max(ec)[:2])
