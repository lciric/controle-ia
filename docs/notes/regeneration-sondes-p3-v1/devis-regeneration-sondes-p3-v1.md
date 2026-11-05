# Devis — régénération du fichier complet des sondes figées de P3 — v1

Écrit par la lignée « session-depot » (instance 2, Opus 5.5) le 28 octobre 2026 vers 17:10 UTC, sur le mot de Lazar
(R-646 : « alors on les régénère tant pis, je ne veux pas le fichier léger, on garde une rigueur IMPLACABLE !!! » ; puis
« go devis régénération des sondes »). **Rien n'est lancé par ce document.**

## 1. Ce qui manque, et pourquoi

Au premier test boîte blanche (P3, run `20261019-230011-p3-reel`, instance 56799469), les sondes ont été entraînées puis
figées en deux fichiers (`src/controle_ia/premier_test_ia/run.py`, docstring, étape 5) :
- le **fichier complet**, sceau `91b61c45cdafd0ab979e261171b9661920715fa42c6cbc9751cd2697bfd3177a` (430 sondes, ligne
  `PROGRES … etape=sondes-figees … sondes=430` de `traces/p3-20261020-020648-jcOO/`), **resté sur l'instance détruite** ;
- le **fichier léger** `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (au dépôt) : toutes les sondes **sauf
  les matrices de Mahalanobis** (six sondes : deux concepts × trois couches).

La couche 2 doit lire **toutes** les sondes figées de P3 (décision de Lazar, D5 renversée, R-646).

## 2. Méthode : refaire les seules étapes 1 à 5 de P3, à l'identique

Un script neuf sous nom neuf (R12), `regenerer_sondes_p3_v1.py`, appelle **les mêmes fonctions** que P3 pour les étapes
1 à 5 (contrôle du format de l'agent ; données génériques ; extraction des activations ; entraînement des 2 × 5 × 3 sondes,
principales et planchers ; écriture des sondes figées), puis **s'arrête** : aucun épisode, aucun juge.

Ce qui est tenu identique, et vérifié avant tout calcul :
| élément | valeur de P3 | preuve |
|---|---|---|
| code des étapes 1 à 5 | commit `97dd829` | `git diff 97dd829 HEAD -- src/controle_ia/premier_test_ia/ src/controle_ia/sondes/ src/controle_ia/harnais/` : **vide** (vérifié le 28 octobre) |
| configuration | `prereg/P3-premier-test-config-v1.json` (couches 7, 15, 23 ; `n_par_classe_enjeux` 1 000 ; `part_entrainement` 0,8 ; `n_plancher` 200 ; `fils_entrainement` 32 ; `budget_entrainement_s` 3 600 ; …) | manifeste `runs/20261019-230011-p3-reel/manifeste.json`, `config_sha256` |
| graines | celles du manifeste (`decoupage-tromperie`, `decoupage-enjeux`, planchers…), dérivées par `SeedSequence` (R9) | même manifeste, clé `graines` |
| données génériques | fichiers versés et scellés, empreintes de la provenance (`docs/sources/donnees-T0.7/provenance-donnees-sondes-v1.md`) ; 598 « tromperie », 2 000 « enjeux », 7 faits exclus | `src/controle_ia/premier_test_ia/donnees.py` ; ligne `PROGRES … etape=donnees` |
| modèle | `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f2…` | manifeste |
| logiciels | python 3.11.17, torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2 (gelés dans `requirements-*.txt`) | manifeste, clé `versions` ; `traces/…/pip-freeze.txt` |
| matériel | A100 SXM4 80 Go, processeur AMD EPYC 7513 | `registres/depenses.md`, ligne du 2026-10-19 22:35 UTC (offre 46608730) |

**Point non consigné par P3** : le nombre effectif de fils de calcul de l'entraînement (borné par 32, par les cœurs de
l'affinité et par le quota du groupe de contrôle). Il peut changer les derniers bits des sondes entraînées sur processeur.
Le script le consigne cette fois, et la machine choisie offre au moins 32 cœurs ; le critère d'acceptation tient compte de
ce risque.

## 3. Critère d'acceptation — à sceller avant le calcul, appliqué mécaniquement

1. **Identité au bit près** : le fichier complet régénéré a le sceau `91b61c45…` → **accepté** : c'est le fichier de P3.
2. Sinon, **identité de ce qui est vérifiable** : (a) chaque tableau du fichier léger se retrouve dans le fichier régénéré,
   à une différence absolue maximale ≤ 1e-6 (la tolérance d'identité de P3, `tolerance_identite`) ; (b) les aires de
   validation de chaque sonde, recalculées, égalent celles de `diag/20261019-230011-p3-reel/sondes-figees.json` à 1e-6
   près ; → **accepté avec déclaration** : les matrices de Mahalanobis sont **régénérées, non identiques prouvées** au
   fichier perdu, et toute lecture les déclare comme telles (sceau neuf consigné).
3. Sinon → **refusé** : rien n'est utilisé ; compte rendu à Lazar avec les écarts mesurés ; la suite (nouvelles sondes
   figées déclarées comme une version 2 distincte de P3, ou autre) est un nœud.

Dans les trois cas : manifeste de run (R9), sceaux de tout fichier produit (R6), arrêt de l'instance par identifiant (R10).

## 4. Coût

| poste | P3 (mesuré) | régénération |
|---|---|---|
| de la création de l'instance au fichier figé | 57 min (22:28:53 → 23:25:47 UTC, dont 908 essais, installation, descente du modèle) | ≈ 1 h |
| prix de la carte | 1,0889 USD/h (A100 SXM4 80 Go) | 1,09 à 1,37 USD/h selon l'offre |
| descente et disque | ≈ 0,03 USD/Go, disque 0,022 USD/h | < 0,5 USD |
| **attendu** | | **≈ 1,5 à 2 USD** |
| **pire cas** (hôte lent, une relance après panne d'hôte avant calcul) | | **≈ 5 USD** |

**Plafond proposé : 6 USD**, une campagne (une instance ; une seconde seulement si la première est perdue par l'hôte avant
tout calcul), échéance 15 novembre.

## 5. Avant le lancement

1. Le script (≈ 3 à 5 heures de travail), testé en **mode jouet** sur processeur (P3 a un modèle et un tokeniseur jouets),
   avec la garde d'arrêt après l'étape 5 testée sur un cas sain et sur un artefact (R5).
2. La fiche de lancement, avec le critère du § 3, **scellée** ; contre-lecture par un sous-agent neuf (R2).
3. Ta ligne de GO ; contrôle du crédit Vast.ai ; création par identifiant avec `GO_ID`.

## 6. Ce que la régénération ne change pas

Le verdict de P3 (R13, `verdict-P3-premier-test-i-a-v2`) reste attaché au fichier d'origine ; aucune lecture de P3 n'est
refaite. Les sondes régénérées servent la couche 2 et ce qui la lit.
