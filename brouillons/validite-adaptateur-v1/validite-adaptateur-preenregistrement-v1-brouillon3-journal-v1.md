# Journal — préenregistrement « validité de l'adaptateur », brouillon 3 — v1

- Rédacteur : le même que le brouillon 2 (Claude Opus 5.5, sous-agent de la session mère, reprise du 2026-11-10). Consigne inchangée : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-validite-adaptateur-brouillon2-v1.md`, `11fd157ed7ae2c5fd44c8707ef1157ab7ecd49365933cb370c0ca3507b67cc89` (revérifiée à 12:03 UTC), interdits communs v2 tenus. Ordres de la mère reçus pendant le tour, par message : (1) « Brouillon 3 de la validité de l'adaptateur : applique la contre-lecture 1 », avec les décisions Q-1/Q-3 (marqueur, variante stricte en annexe), fermeture de (ii) par la règle simple, Q-4 (a) avec VA-6k en ligne de réserve, CLVA-08, CLVA-09 ; (2) « Mot de Lazar reçu : « go pour la lecture large de GO-07 » (R-2207) » : marqueur remplacé par la citation de R-2207, variante stricte gardée en annexe, « variante non retenue (R-2207) ».
- Heures (relevées par `date -u`) : reprise 12:03:35 UTC ; registre et code de T0.6 relus 12:04-12:06 ; script de devis et de puissance 12:04:55 ; écriture du brouillon 3 à partir de 12:05:55 ; R-2207 lue 12:10:21 ; marqueur remplacé 12:10:39 ; validateur passé (liste vide) 12:10:48 ; journal à partir de 12:11.
- **T0.7 toujours non lu** par ce rédacteur : toutes les levées sont prises telles que la contre-lecture 1 les écrit, marquées « (T0.7 brouillon 21, levé par la contre-lecture 1) », avec ses lignes et le commit `8ae9fc44df4599af1e036e979af46aa8fa8f6185`.

## 1. Sources

| pièce | chemin | sha256 | lu |
|---|---|---|---|
| contre-lecture 1 (Fable 5.2) | `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon2-cl1.md` | `cf84198566978307c3cc3e1d10e62245042446b569a407b66bbcb029ffe9764e` (égale au compagnon) | en entier |
| brouillon 2 (relu par elle ; intact) | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon2.md` | `be0851f57bc09dc21ae7ed661d983fdf9aa0fb0148ea19c15f72c1c2bca830d9` | base du brouillon 3 |
| journal du brouillon 2 (intact) | `…-brouillon2-journal-v1.md` | `d4f503d29ab5f6af149b3f7d7340b1ee6a6407b169c8ee586b4cef322ca99567` | — |
| brouillon 1 (intact) | `…-brouillon1.md` | `022f75e29834de1e72174fdc5955c1313dc9bd599e4de44167c0e57b0af1162b` | l. 192 citée en annexe A |
| registre | `registres/decisions.md` R-2194 à R-2198, R-2207 | registre vivant | lignes citées |
| code de T0.6 au commit `1609a4bf` | `src/controle_ia/t06/session_v2.py` l. 140-155 ; `scripts/lancer_t06_v13.sh` l. 220-226 (par `git show <commit>:<chemin>`) | — | vérification de l'avis Q-2 : `verifier_instances` compte les seules instances dont l'étiquette commence par `offre.etiquette` (`t06-v2`) : exact |
| configuration de 7b | `prereg/T0.6-organismes-config-7b-v1.json` | `b7a5c1ba…` | `statistique_equivalence` « q99 », `tolerance_equivalence` 0,2 (l. 129, 143) |
| code de T0.6 sur `main` | `src/controle_ia/t06/lanceur.py` l. 542 | — | nom du sous-ensemble d'activations (`activations-sous-ensemble-t06.npz` ; en morceaux selon T0.6, plan, point 5) |

Non lus : T0.7 (texte et module), P3-bis, tout `diag/`, `runs/`, `donnees/`, tout chemin interdit. Aucune recherche récursive ; aucun appel externe ; aucune écriture git.

## 2. Écarts du brouillon 2 au brouillon 3

Un par constat ; le tableau de traitement de la section « Contre-lecture » du brouillon 3 donne l'endroit de chaque changement. Résumé :
- **Bloquants** : CLVA-01 (`LECTURE-T07` retirée ; fichier `lecture-t07.json` exigé ; `arret-etape-b.json` → refus) ; CLVA-02 (G-2 sur deux champs recoupés, règle simple : **rien n'est lu, pièce R comprise** ; G-3 sans A1) ; CLVA-03 (W0 élargie, W-D, script d'énumération des grilles).
- **Majeurs** : CLVA-04 (directions lues dans `sondes-neuves-t07.npz` et le fichier figé ; E6 réduite) ; CLVA-05 (réserves : borne basse > 0,5 ; puissance 0,554) ; CLVA-06 (VA-2 : intervalle par tâches, tau partiel au pas ; puissance 0,155) ; CLVA-07 (issues réécrites, « établie » retiré ; V0 étendue à VA-4) ; CLVA-08 (`SCELLEMENT-VADAPT` avant `VERDICT-P3BIS`, `CODE-VADAPT` de même ou réserve) ; CLVA-09 (devis refait, voir § 4) ; CLVA-10 (R-2207 citée ; annexe A « variante non retenue ») ; CLVA-11 (recalcul du module de T0.7 réutilisé, garde d'équivalence).
- **Mineurs** : CLVA-12 à CLVA-20 appliqués tels quels (`k` et niveau lus ; `mention_etendue` ; champs des couples ; consigne honnête et étiquettes `vadapt-hd-v1`, `vadapt-r-v1` ; `c_d` mécanique ; journal des ouvertures propre ; multiplicité des réserves ≈ 0,4 par ligne ; VA-6k en ligne de réserve ; marques de levée).
- **Ajouts du rédacteur** : réserves R2, R4, R14 de T0.7 recopiées (levée 6) ; ordre de jeu de HD (`H'`, `HD100`, `HD50`, `HD25`, `HD75`) et ordre de priorité de R avec la recherche de `c_d` et R11 remontées (VA-6k devenue ligne de réserve) ; audit R4 élargi (réserves ≥ 3 fois l'attendu) ; phrase de l'issue la plus forte rendue exacte quand VA-6k est non calculable ; la ligne VA-6k entre dans « Prédiction » ; « sept lignes de validité » au lieu de six (VA-6k).
- **Section « Contre-lecture »** remplie (entrée « Contre-lecture 1 » avec les deux empreintes, traitement de chaque constat). Le validateur `controle_ia.prereg.problemes` rend une **liste vide** sur le brouillon 3 : le texte est formellement conforme, mais ne doit pas être scellé comme préenregistrement avant la contre-lecture suivante (différentiel, sur T0.7 scellé et le commit de `CODE-T07`) — réserve générale de la contre-lecture 1.

## 3. Nœuds et points ouverts pour la mère

- **N-VA-1 — le pire cas entier ne tient pas sous 30 USD (CLVA-09, demandé par la mère : « si c'est impossible, dis-le : c'est un nœud »).** Avec les essais ciblés comptés (HD 0,6 h, R 0,3 h), la sonde Mahalanobis (≥ 16 cœurs, 0 à 0,5 h) et la lecture large de R-2207 (R sur une instance à part, avec sa mise en place), le pire cas (hôte deux fois plus lent, 1,40 USD de l'heure) vaut **≈ 33,2 USD** (HD ≈ 24,6 ; R ≈ 8,7) ; l'attendu vaut **≈ 11,0 à 17,1 USD**. Des coupures avec marge sous 30 sont possibles et écrites (HD 21,0 ; R 8,5 ; réserve 0,5 ; arrêt au cumul plus un quart d'heure) ; ce qui est impossible, c'est de couvrir le pire cas **entier** sous 30. Options : (a) garder 30 USD avec ces coupures et l'ordre de sacrifice écrit (au pire cas, perte possible des doses 0,25 et 0,75 de HD et de la notation Mahalanobis de R) ; avantage : aucune dépense nouvelle, l'attendu est loin du plafond ; inconvénient : au pire cas, lignes « non calculables (coupure) » ; (b) demander à Lazar de porter la ligne à **35 USD** ; avantage : pire cas couvert avec marge ; inconvénient : un mot de Lazar de plus (dépense) ; (c) réduire le périmètre (par exemple R sans R10, R11 ni la recherche de `c_d`, 1 024 passes, ≈ 0,13 h, soit ≈ 0,4 USD de moins au pire : insuffisant seul) ; avantage : aucun mot ; inconvénient : perd VA-6k et ne suffit pas. **Recommandation (a)**, confiance 0,65 ; (b) si la mère porte déjà une ligne de dépense à Lazar dans la journée. Défaut : sans mot, (a) s'applique tel qu'écrit (aucune dépense au-delà de 30).
- **Lecture de `GO-2026-11-10-07`** : tranchée par R-2207 (lecture large) ; marqueur remplacé ; annexe A gardée, « variante non retenue (R-2207) » (choix du rédacteur parmi les deux permis : la garder plutôt que la retirer, pour que le différentiel reste lisible ; elle ne s'applique pas).
- **Inventaire** (avis Q-2 de la contre-lecture) : relire les préalables d'inventaire des ordres en vigueur de P3-bis et de l'étape A ; la destruction de HD avant l'étape A n'est exigée que si l'ordre de l'étape A demande un inventaire vide.
- **Champs fixés par le seul code de T0.7** (`scores_ouverts`, `scores_ii_ouverts`, `index.sondes[].plancher.empreintes_deux_premieres`, `fichiers_sondes_neuves`, `scores_<k>`, `plancher_<k>`, `meta.planchers`, graine « plancher/<nom> ») : confirmation du développeur de T0.7 au commit de `CODE-T07`, ou nommés dans T0.7 avant son scellement (point 4 de la contre-lecture). Confirmation aussi qu'aucune garde de T0.7 ne compte les ouvertures de `scores-actions-t07.npz` hors de son journal (CLVA-17).
- **Contre-lecture suivante** : différentielle (brouillon 2 → 3), par un lecteur de T0.7 scellé, autre modèle, non lecteur de P3-bis ; elle seule peut lever la réserve générale.
- Aucune modification d'hypothèse, de revendication ni de texte scellé ; aucune dépense engagée.

## 4. Devis et puissance — script et sortie (recopiés à l'octet)

Arithmétique du brouillon 3 : HD = mise en place 1,0 + essais 0,6 + génération 160 × 40,2 s + distillation 0,23 à 0,46 + évaluation 320 × 40,2 s + identité et poussée 0,2 ; R = mise en place 1,0 + essais 0,3 + relectures (1 024 + 832 + 512 passes × 0,45 s) + garde d'équivalence 0,05 + notation 0,1 à 0,5 + Mahalanobis 0 à 0,5 + poussée 0,1 ; pire cas : heures doublées à 1,40 USD de l'heure, disque et téléchargement à leurs bornes. Variante stricte (non retenue) : R sans mise en place ni téléchargement.

Script `devis_puissance_vadapt_b3.py`, `07aa8e6bdf2ff150c5583e1d36457ed8700ce0286df0ebfa69ae4e350f700008` :

```python
# Devis et puissance supposés, brouillon 3 « validité de l'adaptateur » ; aucune donnée lue.
from math import sqrt
from statistics import NormalDist
N = NormalDist(); G = 1.188; z80 = N.inv_cdf(0.80); z95_1 = N.inv_cdf(0.95)
def zb(niv): return N.inv_cdf(1 - (1 - niv) / 2)
def sigma(n1, n0): return G * sqrt((n1 + n0 + 1) / (12 * n1 * n0))
print("== puissance")
s = sigma(640, 640)
for niv in (0.9875, 0.9833, 0.975):
    print("soutien 640/640 niveau %.4f : aire min %.3f" % (niv, 0.5 + (z95_1 + zb(niv) + z80) * s))
print("reserve 640/640 (borne basse > 0,5, 95 %%) : aire min %.3f" % (0.5 + (zb(0.95) + z80) * s))
for k in (4, 3, 2):
    niv = 1 - 0.05 / k; zu = N.inv_cdf(1 - 0.05 / k)
    for n in (10, 8, 5):
        sd = sqrt(2 * (2 * n + 5) / (9 * n * (n - 1)) / 64)
        print("k=%d VA-2 64x%d : p seule %.3f ; borne basse>0 %.3f ; borne basse>q95 directions %.3f ; VA-4b %.3f"
              % (k, n, (zu + z80) * sd, (zb(niv) + z80) * sd, (z95_1 + zb(niv) + z80) * sd, (zb(niv) + z80) * sqrt(2) * sd))
print("reserves attendues par hasard par ligne : 16 x 0,025 = %.2f ; P(au moins une sur 16, independantes) = %.2f" % (16 * 0.025, 1 - 0.975 ** 16))
print("== devis")
ep, act = 40.2, 0.45
gen = 160 * ep / 3600; ev = 320 * ep / 3600
hd_lo = 1.0 + 0.6 + gen + 0.23 + ev + 0.2; hd_hi = 1.0 + 0.6 + gen + 0.46 + ev + 0.2
print("HD heures %.2f a %.2f (generation %.3f, evaluation %.3f)" % (hd_lo, hd_hi, gen, ev))
print("HD attendu calcul %.2f a %.2f ; + disque <= %.2f ; + telechargement 0,5 a 2 -> %.1f a %.1f" % (hd_lo*1.0889, hd_hi*1.30, 0.08*hd_hi, hd_lo*1.0889+0.5, hd_hi*1.30+0.08*hd_hi+2))
print("HD pire : %.2f h x 1,40 = %.2f + disque %.2f + tel 2 = %.2f" % (2*hd_hi, 2*hd_hi*1.40, 0.08*2*hd_hi, 2*hd_hi*1.40+0.08*2*hd_hi+2))
passes = 1024 + 832 + 512; rel = passes * act / 3600
r_lo = 1.0 + 0.3 + rel + 0.05 + 0.1 + 0.0 + 0.1; r_hi = 1.0 + 0.3 + rel + 0.05 + 0.5 + 0.5 + 0.1
print("R passes %d, relecture %.3f h ; heures %.2f a %.2f" % (passes, rel, r_lo, r_hi))
print("R attendu %.1f a %.1f" % (r_lo*1.0889+0.4, r_hi*1.30+1))
print("R pire : %.2f h x 1,40 = %.2f + tel 1 = %.2f" % (2*r_hi, 2*r_hi*1.40, 2*r_hi*1.40+1))
r4 = 1.0+0.3+rel+0.05+0.5+2.0+0.1
print("R pire si Mahalanobis sur 4 coeurs (refuse par l'offre) : %.2f h x 2 x 1,40 + 1 = %.2f" % (r4, 2*r4*1.40+1))
hdp = 2*hd_hi*1.40+0.08*2*hd_hi+2; rp = 2*r_hi*1.40+1
print("ensemble attendu %.1f a %.1f ; pire %.1f" % (hd_lo*1.0889+0.5 + r_lo*1.0889+0.4, hd_hi*1.30+0.08*hd_hi+2 + r_hi*1.30+1, hdp+rp))
q = 0.25*1.40
print("marge d'un quart d'heure de carte au prix pire : %.2f USD" % q)
# variante stricte : R sur l'instance de l'etape A (ni mise en place ni telechargement)
rs_lo = 0.3 + rel + 0.05 + 0.1 + 0.1; rs_hi = 0.3 + rel + 0.05 + 0.5 + 0.5 + 0.1
print("variante stricte R : %.2f a %.2f h ; attendu %.1f a %.1f ; pire %.2f" % (rs_lo, rs_hi, rs_lo*1.0889, rs_hi*1.30, 2*rs_hi*1.40))
print("variante stricte ensemble pire %.1f" % (hdp + 2*rs_hi*1.40))
```

Sortie `devis-puissance-vadapt-b3.txt`, `24709b555d22792eec9159e0511333961f9b5a473e54a9ce5d985a213ed34e5c` :

```
== puissance
soutien 640/640 niveau 0.9875 : aire min 0.596
soutien 640/640 niveau 0.9833 : aire min 0.594
soutien 640/640 niveau 0.9750 : aire min 0.591
reserve 640/640 (borne basse > 0,5, 95 %) : aire min 0.554
k=4 VA-2 64x10 : p seule 0.096 ; borne basse>0 0.104 ; borne basse>q95 directions 0.155 ; VA-4b 0.147
k=4 VA-2 64x8 : p seule 0.111 ; borne basse>0 0.120 ; borne basse>q95 directions 0.180 ; VA-4b 0.170
k=4 VA-2 64x5 : p seule 0.157 ; borne basse>0 0.170 ; borne basse>q95 directions 0.254 ; VA-4b 0.241
k=3 VA-2 64x10 : p seule 0.092 ; borne basse>0 0.100 ; borne basse>q95 directions 0.152 ; VA-4b 0.142
k=3 VA-2 64x8 : p seule 0.107 ; borne basse>0 0.117 ; borne basse>q95 directions 0.176 ; VA-4b 0.165
k=3 VA-2 64x5 : p seule 0.152 ; borne basse>0 0.165 ; borne basse>q95 directions 0.249 ; VA-4b 0.234
k=2 VA-2 64x10 : p seule 0.087 ; borne basse>0 0.096 ; borne basse>q95 directions 0.147 ; VA-4b 0.135
k=2 VA-2 64x8 : p seule 0.101 ; borne basse>0 0.111 ; borne basse>q95 directions 0.171 ; VA-4b 0.157
k=2 VA-2 64x5 : p seule 0.143 ; borne basse>0 0.157 ; borne basse>q95 directions 0.241 ; VA-4b 0.222
reserves attendues par hasard par ligne : 16 x 0,025 = 0.40 ; P(au moins une sur 16, independantes) = 0.33
== devis
HD heures 7.39 a 7.62 (generation 1.787, evaluation 3.573)
HD attendu calcul 8.05 a 9.91 ; + disque <= 0.61 ; + telechargement 0,5 a 2 -> 8.5 a 12.5
HD pire : 15.24 h x 1,40 = 21.34 + disque 1.22 + tel 2 = 24.56
R passes 2368, relecture 0.296 h ; heures 1.85 a 2.75
R attendu 2.4 a 4.6
R pire : 5.49 h x 1,40 = 7.69 + tel 1 = 8.69
R pire si Mahalanobis sur 4 coeurs (refuse par l'offre) : 4.25 h x 2 x 1,40 + 1 = 12.89
ensemble attendu 11.0 a 17.1 ; pire 33.2
marge d'un quart d'heure de carte au prix pire : 0.35 USD
variante stricte R : 0.85 a 1.75 h ; attendu 0.9 a 2.3 ; pire 4.89
variante stricte ensemble pire 29.4
```

Limites déclarées : effet de grappe 1,188 supposé ; plancher de bruit optimiste ; actions d'un épisode supposées indépendantes (optimiste, CLVA-06) ; temps de notation et de Mahalanobis sur 16 cœurs supposés à partir des temps de T0.7 levés par la contre-lecture 1 ; arrondis du brouillon pris sur cette sortie.

## 5. Scellement

Brouillon 3 et ce journal scellés par `controle_ia.scellement sceller` (compagnons `.sha256`) ; aucun commit (consigne). Brouillons 1 et 2 et leurs pièces intacts (empreintes en § 1).
