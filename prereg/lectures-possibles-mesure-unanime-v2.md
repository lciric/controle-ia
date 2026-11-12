# Lectures possibles de la mesure unanime, écrites avant la course — v2

Session-dépôt `session_01QPDgKgcLdggoVJfGC5cBw8`, 10 novembre 2026. Annexe de présentation du préenregistrement
`preenregistrement-mesure-unanime-v15.md` (`3a1651f4…`, scellé). **Scellée et datée par le tiers avec lui, avant la course.**
Remplace la v1 (`docs/notes/entretien-resultats-v1/lectures-possibles-mesure-unanime-v1.md`, brouillon, gardée) selon la
contre-lecture v15 (`contre-lecture-v15/rapport-contre-lecture-mesure-unanime-v15.md`, `18ef0083…`, points NB-1 à NB-6).

## Ce que cette note fait, et ce qu'elle ne fait pas

- Elle fixe, **avant toute lecture des scores réels pour cette mesure**, la phrase dite au jury pour chaque issue de la
  mesure, et les limites dites avec elle. Une issue, une phrase.
- Elle **ne modifie aucun critère**. L'issue est rendue par la lecture mécanique gelée (`lecture_mecanique_v8.py`) selon le
  Seuil et les Critères de lecture gelés du préenregistrement v15 (identiques au bit près à la v13), puis prononcée par un
  lecteur neuf. Cette note choisit seulement les mots. Toute autre formulation devant le jury est un nœud pour Lazar.
- La table ci-dessous **n'est pas exhaustive** : une combinaison qui n'y figure pas (par exemple la quatrième mesure
  confirmée avec la première non confirmée, ou le contrôle « fragile ») est rapportée par la phrase du verdict gelé, sans
  autre mot.
- Ce que l'on ne dit **jamais**, quelle que soit l'issue : « nos sondes détectent le sabotage ». La mesure ne porte que sur
  des épisodes **honnêtes** : elle dit comment calibrer un moniteur séquentiel, pas s'il attrape un saboteur.

## Les faits de procédure, dits dans tous les cas

Préenregistrée en quinze versions, soumise à quinze contre-lectures par des instances neuves de plusieurs modèles (treize
rapports entiers, un complément, un contrôle ciblé), figée chez un tiers avant la course si ce dépôt a eu lieu, lancée une
seule fois (un témoin interdit toute relance), lue par un script gelé, verdict prononcé par un lecteur qui n'a rien écrit.
Données : scores, action par action, de trente sondes réelles et quatre cents sondes placebo, sur les épisodes honnêtes
entiers du premier test boîte blanche, sur Llama-3.1-8B-Instruct. Ces scores existent depuis le 20 octobre ; d'autres
travaux en ont tiré des aires et des statistiques voisines, déclarées dans l'annexe des usages antérieurs ; aucun n'a calculé
les quantités que mesure cette mesure.

## Une issue, une phrase

| Issue gelée (préenregistrement v15) | Phrase pour le jury | Limites dites avec elle |
|---|---|---|
| **Audit** déclenché (contrôle de calibrage hors borne, contrôle du mécanisme non atteint, différence injectée réfutée, maximum du bras de dépendance au-dessus de 0,10, placebo différent des sondes réelles, cellule de contrôle à zéro) : rien n'est lu | « Les contrôles internes de la mesure l'ont arrêtée avant toute lecture. Nous ne revendiquons rien, et nous rapportons l'audit. » | aucune |
| **Quatrième mesure confirmée** (dépendance naturelle r₀ < 0,5 ; excès apparié > 0,02, borne basse > 0 ; maximum ≤ 0,08), première mesure confirmée, contrôle tenu | « Nous avions prédit, avant toute lecture de ces scores pour cette mesure, qu'une dépendance entre actions que le calibrage n'a pas vue — ici injectée par nous, à moyenne et variance marginales préservées — fait perdre leur garantie de fausses alertes aux statistiques de somme, mais pas au maximum : le signe que donne notre théorème négatif. Sur les scores réels de trente sondes, c'est ce que nous mesurons. Conséquence pratique : un moniteur séquentiel se calibre sur des épisodes honnêtes entiers, de même structure que ceux qu'il surveille. » Si, et seulement si, le dépôt chez le tiers a précédé la course : ajouter « à une date posée par un tiers ». | épisodes honnêtes seulement ; dépendance injectée (semi-synthétique), moyenne et variance marginales préservées, une seule intensité (τ = 2) ; épisodes de 5 à 10 actions ; un seul modèle de 8 milliards de paramètres |
| **Quatrième mesure non concluante ou réfutée** (r₀ < 0,5) | « Sur nos scores réels, à cette longueur d'épisode, le dépassement prédit pour les statistiques de somme n'est pas établi. Nous le rapportons tel quel, avec la dépendance naturelle mesurée. Cela ne conclut rien sur le théorème lui-même. » | celles de la ligne précédente |
| **Quatrième mesure non lisible** (r₀ ≥ 0,5) | D'abord : « La quatrième mesure n'était pas lisible : la dépendance naturelle des scores était déjà forte. » Puis, selon la feuille gelée de la lecture sur la dépendance naturelle, sans injection : (1) « La règle de fausses alertes calibrée sous indépendance tient sur ces scores, à cette longueur d'épisode. » ; (4a) « La dépendance naturelle des scores réels suffit, sans aucune injection, à faire perdre sa garantie à une règle calibrée sous indépendance. » ; (2a) « La forme des scores suffit à faire dépasser la règle ; un effet de leur structure n'est pas établi. » ; (3a) « La forme des scores et leur dépendance s'ajoutent pour faire dépasser la règle. » ; (4b), (4c), (4d), (2b), (3b) : la phrase du verdict gelé, rapportée sans attribution au-delà de ce qu'elle dit | épisodes de 5 à 10 actions ; un seul modèle ; la feuille et ses deux différences rapportées avec r₀ |
| Première mesure seule (un seuil fixé action par action ne contrôle pas les fausses alertes par épisode) | jamais mise en tête : c'est presque un théorème (tests multiples) ; dite seulement en appui | — |

## Où la phrase s'insère dans l'entretien

Dans la chaîne de prédictions : théorie → simulation (31 prédictions sur 31, verdict formel « confirmé avec réserves »,
`bc53b746…`) → **activations réelles (cette mesure)** → littérature (attaque publiée de Bailey rejouée, suspendue à la
licence). Chaque maillon renvoie à son chemin, son empreinte et, le cas échéant, sa date posée par le tiers.
