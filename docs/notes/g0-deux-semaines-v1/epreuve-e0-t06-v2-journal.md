# Épreuve E0 du lanceur de T0.6 v2 — test croisé sur activations synthétiques (0 USD, processeur)

- Développeur neuf du lanceur v2 (Claude Fable 5.1, sous-agent) ; épreuve proposée par la contre-lecture du lanceur v1
  (`docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v1/contre-lecture-lanceur-T0.6-v1.md`, E0, points 25 et 16 de
  C16). Jouée le 2026-11-05 entre 20:04 et 20:27 UTC (`date -u`), sur le processeur de la session : 4 cœurs
  « Intel(R) Xeon(R) Processor @ 2.10GHz », 15 Go de mémoire vive partagés, ≈ 6 Go de disque libre partagés, sous
  `nice -n 10`, un autre sous-agent actif sur la même machine (durées à lire comme des ordres de grandeur, majorants).
- Script : `scripts/epreuve_e0_t06_v2.py` (fichier d'état par étape, reprise par fichier). **Aucune donnée réelle** : activations
  tirées en bruit gaussien N(0, 1) (aucun signal planté), coûts et mentions tirés au hasard ; écrites en demi-précision par
  `lanceur_v2.ActivationsDemi` (comme le lanceur), relues par `test_croise_v2` avec les réglages de lecture de la configuration
  réelle brouillon 2 (`n_plancher` 200, `permutations_plancher` 200, `tirages_aire` 2 000, 4 fils, 5 familles × 3 couches).
  Aucune valeur d'aire ni d'état de jeu n'est imprimée ni consignée (C01) : seuls les comptes, durées, octets, pics de mémoire.
- Échelle : la taille réelle (64 tâches × 9 conditions × 10 actions × ≈ 222 jetons × 4 096 × 3 couches ≈ 31,5 Go en
  demi-précision) ne tient pas sous les 2 Go de disque permis ; jouée au **1/64** (8 tâches, ≈ 28 jetons par action : 492 Mo)
  et au **1/256** (4 tâches, ≈ 14 jetons : 124 Mo), le nombre de conditions, d'actions par tâche, la largeur, les couches et
  les réglages de lecture restant ceux de la course ; deux points pour mesurer la pente en jetons.

## Commandes exactes

```
cd /home/user/wt/t06-lanceur-v2 && . /home/user/controle-ia-travail/.venv/bin/activate && export PYTHONPATH=src
flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python scripts/epreuve_e0_t06_v2.py <bloc-notes>/e0-1-64 --echelle 1/64
flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python scripts/epreuve_e0_t06_v2.py <bloc-notes>/e0-1-256 --echelle 1/256 --etapes donnees,sous-ensemble,decisif,desc-c7
```
La première commande a atteint le délai de 900 s pendant l'étape `desc-c15` (après `donnees`, `sous-ensemble`, `decisif`,
`desc-c7` faites et écrites dans l'état) ; les étapes `desc-c15` et `desc-c23` n'ont pas été rejouées : la couche 7 suffit
à mesurer chaque famille, et les trois premières familles de la couche 15 ont donné les mêmes durées qu'en couche 7
(17,4 ; 21,5 ; 21,1 s). Les activations synthétiques ont été effacées après lecture (disque) ; les fichiers d'état
(`etat-e0.json`) restent dans le bloc-notes de la session.

## Mesures (durées en secondes, `time.perf_counter` ; pic de mémoire vive du processus, `resource.getrusage`, `ru_maxrss`)

| échelle | actions | jetons (par couche) | disque 3 couches (float16) | sous-ensemble 10 % | décisif (2 sens, validité, courbe) | lineaire-c7 | perceptron-c7 | attention-c7 | mahalanobis-c7 | pic RSS |
|---|---|---|---|---|---|---|---|---|---|---|
| 1/256 | 360 | 5 058 | 124 443 648 o | 36 actions, 1 morceau de 4 141 062 o | 13,9 s | 13,2 s | 12,2 s | 12,9 s | **144,0 s** | 1,61 Go |
| 1/64 | 720 | 20 037 | 492 705 792 o | 72 actions, 1 morceau de 15 826 684 o | 18,8 s | 16,1 s | 21,8 s | 22,6 s | **536,2 s** | 1,99 Go |

Écriture des activations : 1,3 s et 5,8 s (≈ 85 Mo/s en demi-précision, garde de finitude comprise) ; disque exactement
jetons × 4 096 × 2 octets × 3 couches (aucun surcoût de format). Le `decisif` au 1/64 lu avec les trois couches en
configuration ne charge que la couche de la sonde (15) : pic 1,56 Go.

## Extrapolation (pente en jetons entre les deux points ; constante = coût des planchers, Cholesky 4 096 × 4 096 et 200 directions par pli et par sens)

- Pentes mesurées : décisif ≈ 0,33 ms/jeton ; lineaire ≈ 0,19 ms/jeton ; perceptron ≈ 0,64 ms/jeton ; attention ≈ 0,65 ms/jeton ;
  **Mahalanobis ≈ 26 ms/jeton** (144 → 536 s pour 5 058 → 20 037 jetons : linéaire, ×3,7 pour ×3,96 jetons). La cause est
  dans le paquet gelé `sondes/familles.py` (`SondeMahalanobis.scores_par_jeton` : produit (h − μ)ᵀ P (h − μ) avec P de
  4 096 × 4 096 par jeton, borné par la mémoire, pas par le calcul) ; ce code est gelé (T0.7), je ne l'ai pas touché.
- Taille réelle : ≈ 1,28 million de jetons notés par couche (5 760 actions × ≈ 222 jetons, ×64 du 1/64). Sur ce processeur à
  4 cœurs : décisif ≈ 14 + 0,33 × 1 280 ≈ **7 min** ; par couche : lineaire ≈ 4 min, perceptron ≈ 14 min, attention ≈ 14 min,
  difference_moyennes (descriptif, couches 7 et 23) ≈ 7 min, **Mahalanobis ≈ 144 + 26 × 1 280 s ≈ 9,3 h**. Les quinze couples
  sur trois couches : **≈ 2 h sans Mahalanobis, ≈ 30 h avec** (trois couches × 9,3 h). Sur l'instance (≥ 16 cœurs
  effectifs) les produits matriciels vont plus vite, mais la notation Mahalanobis est bornée par la bande passante
  mémoire (une matrice de 134 Mo relue à chaque jeton) : gain attendu 1,5 à 4 fois au mieux, soit **8 à 20 h de carte payée
  pour les trois couples Mahalanobis**, contre ≈ 1 h au devis du texte pour tout le test croisé.
- Mémoire vive à la taille réelle, une couche à la fois (C16) : ≈ 21 Go en simple précision pour les actions de la couche,
  plus les copies en double précision des jetons d'entraînement d'une sonde (≈ 11 % des jetons, ≈ 2,3 Go, deux fois) et la
  covariance 4 096 × 4 096 (134 Mo) : ≈ 30 Go, sous les 128 000 Mo exigés (C05). Le pic mesuré au 1/64 (2 Go pour 0,16 Go de
  couche sur disque) est dominé par des constantes (bibliothèques, planchers) et n'est pas linéaire.
- Disque : 31,5 Go pour trois couches à 222 jetons, 56,6 Go au pire cas de 400 jetons (62,3 Go exigés avec la marge de C03) :
  tient sur les 150 Go du point 9. Sous-ensemble de 10 % : ≈ 1,05 Go, soit **≈ 12 morceaux** de moins de 90 Mo (C11).

## Conclusion

1. Le test croisé décisif (différence de moyennes, deux sens, validité, courbe) tient en quelques minutes à la taille réelle.
2. Les couples descriptifs sans Mahalanobis tiennent en ≈ 2 h sur 4 cœurs (moins sur l'instance) ; **avec Mahalanobis, le
   test croisé coûte des heures de carte payée (8 à 30 h selon la machine)**, hors du devis (« ≈ 1 h »). Ce n'est pas un défaut
   du lanceur : c'est le coût de la notation Mahalanobis du paquet gelé. Pour que ce choix soit une valeur de configuration et
   non du code, la v2 ajoute `familles_descriptives` (liste des familles des couples, la famille décisive comprise) ; la
   configuration réelle brouillon 2 garde les cinq familles du texte. **Nœud pour Lazar** (modification du texte, couple L14) :
   retirer Mahalanobis des couples descriptifs (ou l'évaluer hors ligne, sur le sous-ensemble poussé, après la course), ou
   accepter le surcoût au devis ; recommandation : la retirer de la course et la laisser à une lecture hors ligne.
3. Mesures à confirmer sur la carte (E3) : débit d'écriture des activations et durée réelle d'un couple sur 16 cœurs.
