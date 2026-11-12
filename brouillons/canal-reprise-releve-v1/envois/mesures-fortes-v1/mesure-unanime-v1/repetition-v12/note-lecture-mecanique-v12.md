# Mesure unanime — note de lecture v1 : fausses alertes par épisode honnête entier de l'agrégateur séquentiel, sans puis avec corrélation injectée (scores de P3)

répétition générale (aucune instance réelle), écrite après le relevé `date -u` de 04:40:14 UTC, le 28 octobre 2026. Préenregistrement **NON SCELLÉ** (GardeArret) : `preenregistrement-mesure-unanime-v12.md` (`89d278e8e7ca02d1a8b4942b25c466287e70bce2a5c4aa190524355a82f56186`), commit du scellement `repetition-generale`. Sortie : `repetition-v12/sortie-reelle-v12.json` (`0d6561a47300ca9661c6fc043f1a3c1c7c8519d572321409efd7f770f74bed19`), script `analyse_fausses_alertes_v8.py` (`52b1760a09970526a926f2119dceeef7f20e2f280bdb6a6c2d890962556c5400`), données `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/mesures-fortes-v1/mesure-unanime-v1/synthetique-format-reel-repetition.npz` (`447dc136dde083f68d1f9899344207bd5b8a6caf56c95b441d1c492dd72cb709`), commit du manifeste `repetition-generale`. Lecture mécanique : `repetition-v12/lecture-mecanique-reelle-v12.json` (`1098dea6841dd6373c05a1fa074b95889d5edb622149f1120d1c65e160bc908c`) ; table `table-m2bis-m4-v8.json` (`f63faada54a7b2432315c6766be988ea3bcd0049cff35199ca8234da5c98b120`). **RÉPÉTITION GÉNÉRALE ou essai : aucune donnée réelle, cette note n'est pas une lecture**.

## Verdict (ligne de lecture gelée, appliquée mécaniquement)

**première ligne : la synthèse a raison (comparateur par épisode entier ; sommes sans niveau sous dépendance non vue, maximum tenu) — proposé à Lazar pour G1 et H2**

## Les verdicts, énoncé par énoncé (seuils gelés du préenregistrement)

| énoncé | verdict | quantités |
|---|---|---|
| M1 (seuil par action, τ = 0) | confirmé | médiane 0,067, intervalle [0,033 ; 0,117] |
| M1 bis (par action, de τ = 0 à τ = 2) | ni l'un ni l'autre | 0,067, 0,073, 0,065, 0,045 |
| M2 (contrôle, Ville à τ = 2) | attendu | médiane 0,122 |
| M2 bis (Ville τ = 2 moins τ = 0) | conforme à la table ; signe > 0 attendu : tenu | 0,072 [0,038 ; 0,110] ; table au r₀ médian : 0,105 |
| M2 ter (la lecture sur P3) | (1) Ville tenue sur P3 à τ = 0 | Ville τ = 0 réelles 0,050 (table au r₀ : 0,033) ; mélange 0,004 ; mélange à pas fixé 0,004 ; D 0,046 [0,012 ; 0,080] ; D′ 0,046 [0,011 ; 0,080] ; dérive mesurée 0,000 [-0,003 ; 0,004] |
| M3 (24 cellules conformes, calibrage partagé) | tenu | L = 0,050, B = 0,100 ; pire cellule tau=2.0:balayage = 0,057 ; fragiles : 0 ; audit : 0 |
| M4 (dépendance seule, excès apparié) | confirmé | excès 0,047 [0,023 ; 0,085] (différence des médianes 0,053) ; quantité 0,103, à τ = 0 0,050 ; maximum conforme 0,013 ; table (excès au r₀) 0,075 |
| contrôle placebo | mêmes médianes (aucun écart > 0,05) | écarts réelles − placebo sur les 24 cellules de M3 et le maximum de M4 : max |écart| = 0,042 |
| cellule conforme à 0 | aucune | |

## Corrélation intraclasse (rapportée, jamais une condition)

r₀ médian des sondes réelles : 0,196 ; placebo : 0,224 ; centré par pas : 0,195 ; mélange à pas fixé : -0,001.

## Réserves du script de lecture

- aucune.

## Les 24 cellules de M3 (médianes sur les sondes réelles)

| cellule | médiane |
|---|---|
| tau=0.0:max | 0,033 |
| tau=0.0:somme_terminale | 0,050 |
| tau=0.0:somme_sequentielle | 0,050 |
| tau=0.0:page | 0,050 |
| tau=0.0:processus_e | 0,050 |
| tau=0.0:balayage | 0,050 |
| tau=0.5:max | 0,048 |
| tau=0.5:somme_terminale | 0,043 |
| tau=0.5:somme_sequentielle | 0,043 |
| tau=0.5:page | 0,045 |
| tau=0.5:processus_e | 0,042 |
| tau=0.5:balayage | 0,046 |
| tau=1.0:max | 0,046 |
| tau=1.0:somme_terminale | 0,043 |
| tau=1.0:somme_sequentielle | 0,043 |
| tau=1.0:page | 0,045 |
| tau=1.0:processus_e | 0,044 |
| tau=1.0:balayage | 0,048 |
| tau=2.0:max | 0,052 |
| tau=2.0:somme_terminale | 0,054 |
| tau=2.0:somme_sequentielle | 0,054 |
| tau=2.0:page | 0,056 |
| tau=2.0:processus_e | 0,056 |
| tau=2.0:balayage | 0,057 |

## Manifeste

E = 60 ; K par pli = [39, 39, 39, 39, 39, 39, 39, 39, 39, 39] ; L = 0,050 ; tirages 20 ; rééchantillonnages 2000 ; sondes réelles 3, placebo 2 ; numpy 2.5.4 ; python 3.13.17 ; entropie 20261028.

## Réserves de l'auteur (à la main, après la lecture mécanique)

⟨À ÉCRIRE : ce que la lecture ne dit pas ; R4 si un résultat paraît trop propre ; aucune interprétation hors des critères gelés.⟩

