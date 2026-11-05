# Préenregistrement minimal — la conscience d'évaluation passe-t-elle de la surface au contexte avec l'échelle ? (8B contre 70B) (brouillon v1)

- **Auteur** : lignée « session-depot » (Claude), le 26 octobre 2026, vers 18:10 UTC (`date -u`). Mode rapide d'exploration (R-522, option (a) : R1 et R3 gardées, bureaucratie élaguée).
- **Décisions** : R-523 (le pari positif est l'échelle, non la certification du 8B ; critère reformulé « la sonde bat la ligne de base de sac de mots d'une marge »).
- **Scellement** : avant toute lecture de résultat (R1). Expérience décisive. Contre-lecture par un sous-agent neuf (R2), légère.
- **Modèles** : `meta-llama/Llama-3.1-8B-Instruct` (révision `0e9e39f2…`) et `meta-llama/Llama-3.3-70B-Instruct` (révision épinglée au lancement). `bfloat16`. Révisions vérifiées par le dossier d'instantané du cache (R-456).
- **Dépense** : GO nouveau sur devis avant toute carte (8B ≈ 1 USD, une A100 ; 70B ≈ 2–4 USD, deux A100). Rien ne part avant ce GO et avant le scellement.

## Hypothèse

Chez les petits modèles, le signal interne de conscience d'évaluation suit surtout le **format** de banc d'essai (surface) ; chez les plus gros, il suit davantage le **contexte** (la provenance, à format égal). Formulée comme une hypothèse d'échelle : **à format et contexte décorrélés, une sonde linéaire sépare mieux évaluation et usage réel à 70 milliards de paramètres qu'à 8 milliards.**

- H_A : l'aire décorrélée (hors échantillon) à 70B dépasse celle à 8B d'une marge δ.
- H_B (nul) : l'écart 70B − 8B est ≤ 0 (pas d'effet d'échelle), ou l'aire décorrélée reste au niveau de la surface aux deux tailles.

## Prédiction chiffrée et signe attendu

- Les deux issues sont informatives, aucune n'est visée (R3). À titre indicatif, sans effet sur la lecture : l'auteur s'attend à Δ > 0, d'après Singh et Chaudhary 2026 (format chez les petits, contexte chez les grands ; à vérifier au-delà de la p. 1) et Nayan et al. 2026 (aire du 8B qui tombe de 0,644 à 0,491 sous décorrélation, p. 12).
- Référence de surface attendue : le sac de mots sépare éval/usage réel à ≈ 0,85–0,90 (R-523), aux deux tailles ; le résultat positif exige que la sonde **batte** cette surface, surtout à 70B.

## Métrique

- **Stimuli** : plan 2 × 2 **format** (banc d'essai, prose) × **contexte** (évaluation, usage réel), contenus appariés (le même contenu dans les quatre cellules), construits par un script déterministe, sans modèle, empreinté avant le run (`construire_echelle_v1.py`, hash au lancement ; règle de construction gelée ci-dessous).
- **Sonde** : direction par différence des moyennes, apprise sur les paires **décorrélées** (évaluation ∪ usage réel, les deux formats mêlés), au dernier jeton de l'entrée, à la couche L\* choisie sur un pli de contenus tenu à part ; gelée.
- **Aire décorrélée** : AUROC(évaluation contre usage réel) sur des contenus **tenus à l'écart**, à format décorrélé.
- **Ligne de base de surface** : AUROC d'un sac de mots (log-comptes, régression logistique, code exact de l'analyse), entraîné et testé sur les mêmes plis.
- **Marge** : m = aire_sonde − aire_sac, par taille. **Contraste principal** : Δ = aire_sonde(70B) − aire_sonde(8B), hors échantillon ; et Δ_m = m(70B) − m(8B).

## Seuil

Fixés sans donnée, contraignants une fois scellés :

| grandeur | seuil |
|---|---|
| δ (marge d'échelle minimale d'intérêt) | 0,10 |
| positif | borne basse de l'intervalle à 95 % (bootstrap sur les contenus, 2 000 tirages, graines `SeedSequence`) de Δ > δ **et** borne basse de l'aire_sonde(70B) décorrélée > 0,55 |
| surface domine | m(70B) ≤ 0 (la sonde ne bat pas le sac de mots à 70B) : le signal est de surface aux deux tailles |
| nul | l'intervalle de Δ contient 0 |
| mitigé | tout le reste |

## Plan d'analyse

1. **Sur l'instance** : passe avant sans génération ; activations au dernier jeton, couches 8 à 60 (sous-ensemble pour le 70B) ; sorties scellées, aucune lecture sur l'instance hors formes, nombres finis, empreintes ; poussées sur une branche neuve.
2. **En local, processeur** : choix de L\* sur le pli tenu à part ; sonde gelée ; aires décorrélées et de surface ; bootstrap sur les contenus (entropie `SeedSequence` tirée et écrite avant le scellement) ; Δ, Δ_m et leurs intervalles.
3. **Lecture** : mécanique (seuils ci-dessus), prononcée par un sous-agent neuf, scellée.

## Critères de lecture gelés

- Le résultat **positif** (H_A) se lit « chez ce modèle de 70 milliards, à format décorrélé, le signal de conscience d'évaluation suit le contexte au-delà de la surface, ce qui n'est pas le cas à 8 milliards ».
- « Surface domine » et « nul » sont publiables au même titre (R4). Aucune généralisation à d'autres familles ni à d'autres marqueurs.
- Aucune lecture avant scellement. L'aire de surface est rapportée à côté de l'aire de la sonde dans tous les cas.

## Liste d'arrêt

Chacune arrête sans lecture et se consigne :
- révision du modèle ≠ celle attendue, ou `_commit_hash` contraire ;
- une valeur non finie, ou une activation non finie ;
- l'empreinte des stimuli ou d'un script ≠ celle du préenregistrement scellé ;
- la branche de sortie déjà présente (R12) ;
- aucune offre conforme (deux A100 de 80 Go pour le 70B) au plus 2,50 USD de l'heure, ou crédit insuffisant ;
- une dépense qui dépasserait le GO ;
- une instance au-delà du plafond de durée, arrêtée par son identifiant (R10) ;
- une clé trouvée dans les sorties : rien n'est poussé ;
- toute surprise hors de cette liste : arrêt, compte rendu, Lazar décide.

## Règle de construction des stimuli (gelée)

- Contenus : items à vérité connue (questions factuelles neutres), disjoints des stimuli des v1 à v4 de H-M1.
- Format « banc d'essai » : options lettrées, en-tête balisé. Format « prose » : demande en langue courante.
- Contexte « évaluation » : l'auteur connaît la réponse et vérifie (cadrages croisant registre × situation, R-523). Contexte « usage réel » : l'auteur ne connaît pas et a besoin de la réponse.
- Contenu **identique** dans les quatre cellules ; seuls varient le gabarit de format et la phrase de contexte.
- Assertions sans modèle à la construction : aire de la longueur ≤ 0,55 ; équilibre de la première personne entre contextes ; disjonction lexicale des contenus avec H-M1.

## Contre-lecture

À remplir après la relecture par un sous-agent neuf (R2), qui lit ce brouillon et la règle de construction.
