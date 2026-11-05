# Contrôle neuf de la synthèse du collisionneur (v1)

- **Pièce contrôlée** : `audit-taif-v2/synthese-audit-collisionneur-v1.md`, sha256 `d672e57a90019a444eb03d31347400cef3cad97880237ce97ff10ef579c163f6`. L'empreinte est conforme à son compagnon `.sha256`, vérifiée avant lecture. La pièce n'a pas été modifiée.
- **Contrôleur** : un sous-agent neuf, claude-opus-5-5, le 26 octobre 2026 vers 14:00 UTC. Il n'a écrit ni la synthèse, ni les cellules, ni les vérifications. C'est le même modèle que l'auteur de la synthèse, que CB et que RB : réserve R2, un contre-lecteur d'une autre famille reste souhaitable.
- **Méthode** :
  - empreintes recalculées ;
  - chaque PDF empreinté, puis ses pages réextraites par `pdftotext` ;
  - tirages au hasard par `numpy.random.SeedSequence` (numpy 2.5.3), sur des viviers figés et empreintés avant le tirage.
  - Les chemins sont relatifs à `scratchpad/`, sauf mention.
- **Périmètre** :
  - aucune écriture dans le dépôt, aucun appel payant ;
  - aucun fichier interdit ouvert ; les seuls fichiers du dépôt lus le sont par chemin explicite sous `docs/` (liste en annexe) ;
  - `resultats-T0.3-v1.md` n'a pas été ouvert.

## Verdict

**Conforme avec réserves.**
- Aucune phrase de la synthèse ne décrit un procédé opérationnel.
- Toutes les affirmations revérifiées tiennent : 5 sur 5 au tirage, plus 24 PDF contrôlés de façon ciblée (47 pages).
- Les empreintes de l'annexe sont toutes exactes : 56 PDF et 20 empreintes de pièces.
- Les trois items tirés figurent dans leurs cellules.

Les réserves portent sur la forme et la complétude :
- une dizaine de renvois sans statut ou sans empreinte ;
- deux pages de sources opérationnelles non signalées ;
- une sous-proposition sans verdict ;
- des items retenus sans route de décision ;
- une asymétrie de sources sur F03 ;
- le III.3 non fusionné, qui contient au moins une divergence avec la synthèse.

## 1. Filtre défensif

- Aucune phrase de la synthèse ne décrit un procédé pour tromper un moniteur, une sonde ou un juge : ni étapes, ni consignes, ni gabarits, ni code.
- Trois phrases sont limites, mais conformes : chacune est écrite comme hypothèse mise en défaut, avec sa source et sa mesure.
  - l. 47 et l. 297 : condition d'accès d'une obfuscation sans gradient ;
  - l. 140 : organisme « pré-évadé » par un noteur de même lignée.
- Deux signalements manquent au § 7. Ce sont des sources citées par la synthèse ; les procédés ne sont pas reproduits ici.
  - 2410.21514 (Benton et al.) p. 26 : un échafaudage d'élicitation, décrit par étapes, pour un surveillant chargé de saper la surveillance. La synthèse cite p. 25-27 au F05.
  - 2312.06942 p. 7 : un tableau des stratégies de l'équipe rouge, dont une collusion par signal. Le § 7 ne signale que la p. 13, alors que l'annexe donne la p. 7 comme relue.
- Les signalements existants sont confirmés sur les pages que j'ai ouvertes : 2607.25907 p. 6, 2412.09565 p. 9, 2512.07810 p. 17.
- Cellules III.1 et III.2 : un balayage par mots-clés ne trouve aucun procédé. CA l. 47, CB l. 51 et CC l. 3 écartent elles-mêmes un point en une ligne. C'est conforme à « aucune cellule n'a été signalée ».

## 2. Provenance

**Empreintes.** Toutes les empreintes de l'annexe sont conformes (script `controle-synthese-neuf-v1/scripts/verif_pdf_annexe.py`) :
- les 20 empreintes de pièces : question, neuf cellules (dont les trois du III.3), LISEZMOI-v2, R-508, lot B, N-053, N-054, programme v2, quatre scripts ou sorties de simulation ;
- les 56 PDF.

**Tirage des cinq affirmations « vérifiées ».** Le vivier compte 70 affirmations (`controle-synthese-neuf-v1/viviers-v1.txt`). Entropie du tirage : 222217239126568425524570237638396622374.

| Tiré | Affirmation de la synthèse | PDF, sha256 | Page relue | Résultat |
|---|---|---|---|---|
| P10 (F12) | les méthodes non supervisées trouvent le trait le plus saillant | 2312.10029v2, `8f8b5e7a…` | 1 ; 11-12 pour la réserve | confirmé : « whatever feature of the activations is most prominent » ; portée limitée au non supervisé (p. 11-12) |
| P34 (A28) | une sonde de tromperie monte sur des aveux honnêtes | 2502.03407v1, `a4820ad5…` | 8 | confirmé : « honest confessions of past misdeeds are often rated as dishonest by the probe » |
| P54 (C12) | sonde appariée entraînée et évaluée dans la même distribution ; contexte confondu avec la source | 2603.19426v1, `095a5a7c…` | 3 | confirmé : découpage 80/20 sur données mêlées ; évaluation = MMLU, ARC, GSM8K, MuTual ; déploiement = ShareGPT |
| P61 (F03) | Tice et al., NeurIPS 2025 | 2412.01784v3, `7fbe44ec…` | 1 | confirmé |
| P62 (F05, vérificateur) | Benton ne manipule aucun cadrage banc d'essai contre production | 2410.21514v1, `67f35893…` | 25-27 | confirmé : un seul protocole, avec échafaudage contre sans |

**Contrôles ciblés en plus.** Ils portent le verdict et les décisions. Tous sont confirmés, et les sha256 sont conformes à l'annexe.
- **Décision 1, C05, C06** : 2509.21344.
  - p. 5 : le filtrage des scores « cannot account for information that leaks […] via attention » ; segmentation des positions.
  - p. 6 : filtrage aléatoire en témoin.
  - p. 7 : même limite.
  - p. 8 : « much more confident » dans les organismes.
- **Décision 5, C01** :
  - 2607.06596 p. 1 : 41 % contre 19 %.
  - 2607.06596 p. 2 : le moniteur à consigne fixe n'a pas de bonus de diagonale.
  - 2607.06596 p. 3 : gpt-4.1-mini, d'un autre fournisseur ; la lignée est la famille de calibrage.
  - 2607.06596 p. 13 : 41 contre 19 sur huit familles ; 18 % contre moins de 2 % sur les quatre ouvertes.
  - 2602.20628 p. 1 : 9,8 % contre 2,8 % ; borne élicitée par réglage fin sur GPT-4.1.
  - Table (d) de R-508 recomptée : 30 lignes sur 46 ne sont lues qu'en p. 1. La même table figure dans les faits du tour : le « 24 des 39 » de CC (l. 10) est bien faux.
- **C10, C11, C18** :
  - 2607.25907 p. 8 : 0,43 et 0,51 contre 0,44 ; p. 6 : Llama-3.2-3B, couche 14 (R-508 l. 92 écrit bien Llama-3.1-8B).
  - fiche Sonnet 4.5 p. 104 ; 2503.11926 p. 1 ; 2507.11473 p. 5.
- **C15** : 2509.18058 p. 23, 4 réponses « New Incorrect » pour Qwen3-4B et pour Qwen3-8B.
- **Décision 2, A25, A26, C08, C09** :
  - 2510.20487 p. 1 : 49 milliards de paramètres ; méthode en deux étapes.
  - 2510.20487 p. 4-5 : 115,6 millions de jetons ; modèle désigné par son nom.
  - 2309.00667 p. 1 et 3 ; 2510.13900 p. 1 ; 2503.10965 p. 19.
- **Décision 3, F06, C07** :
  - 2412.09565 p. 9 : « gradient-free manner » ;
  - 2412.09565 p. 24 : « difficult to draw broad conclusions based on this one case » ;
  - 2505.13763 p. 7 ; 2608.21664 p. 5 et 7.
- **Autres sources** : 1909.03368 p. 2 (4,5 contre 26,0) ; 2310.11324 p. 1 (76 points, LLaMA-2-13B) ; 2512.07810 p. 4, 7, 16, 17 et 22 ; 2504.10374 p. 7 ; 2605.26047 p. 1 ; 2407.12831 p. 2 ; 2208.07610 p. 1 ; 2411.17693 p. 1-2.
- **Chiffres internes** :
  - A07 et A08 : retrouvés dans `audit-taif-v2/scripts-lot6/sortie-sim-lot6-v1.txt` (`08dbc91f…`).
  - A20 : recalculé ; seuils 3,889 et 4,353, rappel de 50 % puis 32 %.
  - III.3 : 12:08 à 12:16 UTC, 2,92 USD, étage à 9,32 USD ; conforme à `journal-suite-v1.txt` et à `etat.md`.
  - N-007 l. 33 : 0,21 à 0,35.
  - N-013 l. 79 et N-015 l. 18 : c'est bien N-013 qui retire le bruit sur les poids.

**Lacunes.** Elles sont de forme, sauf mention. « Confirmé » veut dire lu par moi sur le PDF empreinté.
1. **Renvois sans statut**, tous confirmés :
   - A26 « 2309.00667 p. 3 » ;
   - A23 « p. 4 » et « p. 16 » de 2512.07810 ;
   - A31 « Taylor p. 16-17 ; Boxo p. 1 » ;
   - C01 « exacts en p. 1 ».
2. **Sans page ni statut**, à vérifier :
   - C15 « sonde moyennée » ;
   - F09 « SAD est comportemental, sans activations » ;
   - F15 « Burns et al. est mal attribué » (l'annexe ne donne aucune page relue).
3. **Chiffres internes sans empreinte (R6)** :
   - « 0,046 à 0,055 » : `resultats-T0.3-v1.md` P8, absent de N-007, à vérifier ;
   - état de l'art v1 l. 154 ;
   - antériorité niveau 2 l. 77, 78 et 207 ;
   - P-015 l. 58.
4. **A22 (« 240 » et « 600 » actions)** : les hypothèses de calcul ne sont pas dites. Je retrouve ces ordres de grandeur avec 1 % contre 3 %, un test unilatéral à 5 % et une puissance de 80 %. Ce sont mes hypothèses, pas celles du vérificateur.
5. **Pages imprécises** :
   - C06 attribue à 2509.21344 p. 6 un placebo « du même nombre de positions ». La page filtre au hasard des fractions croissantes de jetons, jusqu'à 95 %.
   - « Gemma-2-2b » n'est pas sur la p. 24 citée ; la p. 22 dit seulement GemmaScope.
   - Annexe : les auteurs de 2208.07610 sont en p. 1, pas en p. 2.
6. **Formulation** : « contredite par sa source » (§ 1, point 2) est un peu fort.
   - 2509.21344 reconnaît la limite du filtrage (p. 5, 7) et préfère les organismes (p. 8).
   - Mais elle garde le filtrage des scores comme outil bon marché (p. 8).
   - La recommandation de la décision 1, qui met le filtrage en diagnostic, est conforme à la source.

## 3. Fidélité aux cellules

Trois items ont été tirés parmi les vingt qui citent des cellules : A16, A19 et F06.
- **F06 : conforme.**
  - CA l. 38 : taxe en courbe par régime d'accès ; titre fautif « Latent-Defense Mechanisms ».
  - CA l. 110 : le test ne mesure qu'un point de la courbe.
  - CB l. 47 : coût en utilité ; titre exact.
  - RB l. 44 : titre de A à vérifier.
  - « CB a raison contre CA » est exact.
- **A19 : conforme.**
  - RB l. 56-59 : l'hypothèse est reprise mot pour mot.
  - La remarque « leurs deux hypothèses prédisent la même chose » est juste : H_A et H_B de RB prédisent toutes deux une dépendance intra-tâche nulle.
- **A16 : conforme, avec une nuance.**
  - RB l. 33-34 et RC l. 22-23 et 63 portent bien l'objection.
  - Mais CA décrit un essaim « mixte » (l. 154), à « lignées mélangées » (l. 85).
  - La phrase « un essaim Qwen homogène partage aussi ses poids » répond donc à la lecture de RB et RC, pas à celle de CA.
  - L'argument de fiabilité vaut pour les deux lectures.
- **Renvois de lignes vérifiés en plus**, tous conformes :
  - A34 : CA l. 120 ; CC l. 3, 9 et 10.
  - A35 : CA l. 106, 144 et 155.
  - Rangs du § 5.a : CA l. 138-150, CB l. 114-126, CC l. 115-140.

## 4. Complétude

- Les 69 candidats (F01 à F15, A01 à A35, C01 à C19) ont chacun un verdict.
- Le décompte est exact : 32 retenus, dont 7 sans réserve ; 35 déjà couverts, dont 22 angles morts ; 2 rejetés.

**Ce qui manque.**
1. **La fusion du III.3**, déclarée au § 7. Elle contient au moins une divergence concrète avec la synthèse :
   - la riposte de CC (l. 51-58) fait d'un détecteur lexical positif une précondition, et conclut à l'absence d'écho s'il échoue ; la synthèse refuse ce détecteur comme arbitre (C05) ;
   - la riposte de CB (l. 35) accepte l'« imputation neutre » proposée par RC.
2. **Une sous-proposition sans verdict** : l'imputation neutre des positions masquées (RC l. 124). Seule la seconde moitié est reprise, le déclencheur lexical et la sensibilité du filtre (C06, décision 1 (c)).
3. **Des items retenus sans route de décision** :
   - A35 (pilote du temps d'audit aval) n'apparaît plus qu'au § 7 (l. 259) ;
   - A16 et A23 n'ont qu'un rang « ensuite » (l. 191), sans décision.
4. **La symétrie des sources (R4) sur F03.** Le rejet ne cite que le résultat négatif : 2512.07810 p. 22, « unreliable ». Il ne dit pas que 2412.01784 p. 1 annonce un signal « reliable, model-agnostic », ni que N-013 l. 79 s'appuie sur ce papier. Le rejet comme faille neuve tient, mais la divergence entre sources doit être dite.
5. **Une correction de RB non reprise** : 2412.04984 (Meinke et al.) ne documente pas l'imitation d'erreurs humaines (RB l. 140, contre CC l. 31). A31 ne le dit pas.
6. **Une correspondance non dite** : les cellules et les faits citent N-047 (F3), alors que la synthèse cite N-053. N-053 remplace N-047 à contenu égal (N-053 l. 7). Une ligne suffirait.
7. **Un § 7 incomplet** sur le contenu opérationnel des sources (voir § 1).

## Annexe — traces du contrôle

| Fichier | sha256 |
|---|---|
| `controle-synthese-neuf-v1/viviers-v1.txt` (viviers figés avant tirage) | `491891c11519a6a4f6e956bd78d216e00e1cd169f9d3ca8b9b53837a79e86a1d` |
| `controle-synthese-neuf-v1/tirage-v1.txt` (sortie du tirage) | `07c51277fb8e5ab5cc677b72a5e9caaa80128910d0be5993116187a8ef214d0d` |
| `controle-synthese-neuf-v1/scripts/tirage_v1.py` | `8e041b47a21bd4b705c7fdb8d33b76c05574c521570dd67243721baf76870dc5` |
| `controle-synthese-neuf-v1/scripts/verif_pdf_annexe.py` | `86864952f2c642e9cc515bf4fb5dc7732d56574a1f90024da5b43bb93f5ecad7` |
| `controle-synthese-neuf-v1/scripts/extraire.sh` | `531ef0a7f3813a94a5559d3230d13356a1bd0e80268c2cbb095db77e0f2897c6` |
| dépôt `docs/notes/audit-controle-v1/audit-litterature-v1.md` (R-508, lu) | `29b32f620cb2310fad83166fd4f2957b3ce43b1c3dea090834d8c28f86e4823b` |
| dépôt `docs/decisions/decision-N-007-N-008-v1.md` (lu) | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` |
| dépôt `docs/decisions/decision-N-013-v1.md` (lu) | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` |
| dépôt `docs/decisions/decision-N-015-v1.md` (lu) | `462785b333101c20e5a923b2155bfd5964dd4172aa896440c51e8baca3602b7b` |
| dépôt `docs/decisions/decision-N-053-v1.md` (lu) | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| `collisionneur-audit-controle-v1/faits-audit-controle-v1.md` (table (d) de F2 recomptée) | `574c6b769b291255a95bf1bba39fef17888dbd85b030b7656c81d48f440583a7` |

- Les 58 pages extraites sont dans `controle-synthese-neuf-v1/txt/`, une page par fichier, nommées `<auteur>-p<N>.txt`.
- J'ai aussi lu l'en-tête de `docs/decisions/decision-N-047-v1.md` (`20941ec350762a140dba753ffa535f68dc7217cf91df5c20c8e8eef9a0d95267`, conforme à son compagnon).
- N-054 et le programme v2 n'ont été qu'empreintés.
