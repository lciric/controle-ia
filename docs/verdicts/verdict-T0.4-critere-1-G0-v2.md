# Verdict R13 — T0.4 v2, validation du harnais sur modèle réel — run A `20261005-144628-validation-reelle` — critère 1 de la porte G0 — v2

- Juge : sous-agent neuf (R13), ni auteur du préenregistrement, ni du code, ni de l'analyse, ni contre-lecteur. Date : 2026-10-05 (UTC).
- Table appliquée : `prereg/T0.4-validation-modele-reel-v2.md`, sha256 `886c8c07c6954a46c666b294c391523f0cdd3d03a5b99dae5079507503de3fb9`, section « Critères de lecture gelés ».
- Critère jugé (brief v2, ligne 192) : « Harnais validé : déterminisme, équivalence d'activations, gardes testées ».
- Mes recalculs : `recalculs/` (scripts et sorties brutes), scellés par `recalculs.sha256`.

## 1. Verdict

**Critère 1 de G0 : non prouvé par ce run.** Une seule ligne gelée s'applique, « P4 contraire », dans sa première branche : **logique validée** (P2, P2b et P3 conformes ; en double précision, écart maximal 9,78e-13 ; défaut D1 vu pour 20 actions comparables sur 20), mais **écart de demi-précision au-dessus du seuil de production** (P4 : 0,522 > 0,1 ; 28 actions sur 40, toutes dans le contexte, couches 15 et 23).
P0, P1, P5, P6 et P8 sont conformes ; P9 n'est pas déclenché. P7 n'est pas atteint (aucun run B) : aucune ligne ne le lit, et cela suffit aussi à exclure la première ligne. Suite gelée : réserve et nœud, au vu du repère de précision.

## 2. Empreintes vérifiées

Chaque sha256 ci-dessous a été recalculé sur mon clone (`git clone --no-hardlinks`, HEAD `93840abe50487f3c97003abb92697b8b4895bccf`, arbre de travail propre). « Compagnon » : égal au fichier `.sha256` voisin. « Chaîne » : `verifier_resultat` du code cité, sans arrêt (résultat intact, manifeste intact, rattachement par empreinte). Sorties : `recalculs/01-verifier-empreintes.sortie.txt` (57cdbf89…) et `recalculs/02-identite-du-run.sortie.txt` (1dd8207b…).

```
Préenregistrement et documents cités en tête (égaux aux citations)
886c8c07c6954a46c666b294c391523f0cdd3d03a5b99dae5079507503de3fb9  prereg/T0.4-validation-modele-reel-v2.md (compagnon ; empreinte attendue ; même contenu au commit 9767398 du manifeste)
9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2  docs/brief-claude-code-programme-complet-v2.md (sha256sums-lancement-v2 : OK)
2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c  docs/programme-controle-ia-v2.md (idem)
16d71febf1491780ab1230ed1fb8e4d8b1bec47fbed202e0ef26ca666def04c2  livrables/premier-rendu-v1/devis-v1.md
b013428ab8502a61a3ea19404ea3a6cdc64ea6a587010c45627e33f13ef29148  docs/notes/memoire-double-precision-T0.4-v1.md
fb9919f9c4d7d73fd03bdcf65e03ef2492dd1951d4ffb10b43cd08d1e361f277  docs/verdicts/verdict-T0.4-critere-1-G0-v1.md (lu pour le contexte)
06b4ff5627abd03c6708ea628b157d2c90d03b853be8d24a0d80e3b299bbe0ef  docs/decisions/proposition-N-010-v1.md
a91a5838f0ec44bae5689ed935eda1b558fcda692d6314106761da5ac02bce4b  docs/procedures/validation-T0.4-modele-reel-v3.md (compagnon ; empreintée, non relue)

Résultats du run : compagnon et chaîne conformes pour chacun (diag/… = diag/20261005-144628-validation-reelle ; 35 fichiers, 35 compagnons)
92e166325da9060a7b28b2e90b78a487654d170bf035883b2da681cf5cbc4487  runs/20261005-144628-validation-reelle/manifeste.json
e3ca201edef75f50409e42848f5c4faee0c411dd4a169933751c08bb228c63e6  diag/…/arret.json
fdff40031d5b5cdaa75c4e65b3ed6271ada882b4550a61b1cadeef143584c38a  diag/…/tests-instance.json
92095a65d637766223f1021ceabda7b30dc0bb967cab4bc097082ce24481eae7  diag/…/environnement-python.json
72f6b5ec0419ffd41253ef64cb4edc1d0a694f20d0c66c02e3e4989faa0928e8  diag/…/logique-episode-0-trajectoire.json
5da5523e7a489390537dfb504d9bb98f70f25e29fbc23a7c538aba0e2c836d28  diag/…/logique-episode-1-trajectoire.json
66c3e8afecf8e1d33c4fede4c3ddc6243abee9a5fb2d53885d6d201091fcab84  diag/…/logique-episode-2-trajectoire.json
ed92f464af02a13867bcfaa1a995a7e7ebec33a9364df0384b34afb227264b01  diag/…/logique-episode-3-trajectoire.json
b7b75a696fc85d6ae0a99078d4a4f02b6bc8b5e77d1d3834d701feda4d600777  diag/…/logique-episode-4-trajectoire.json
a9c19fb70a1569bf26562c67ad1963bf5c0856750d377704015099f9da13c4fb  diag/…/logique-episode-5-trajectoire.json
dd91f2f82ec3d1be8116b73153ab01213c1c7a47b233becefe6ab52ea1e0aad5  diag/…/logique-episode-6-trajectoire.json
64c507af7da6424929df655f327216dd85acfcd11ee606f30468d0f4d7e9d390  diag/…/logique-episode-7-trajectoire.json
123ca0b7ed7aecfcf4b09e8d89267d1efce1feff8d1fc2c73a23fe08686a043e  diag/…/controle-positif-episode-0-trajectoire.json
630754811600ee3714ee31d715be47576ea557d4f5f48e4fa865f60c1a1372bb  diag/…/controle-positif-episode-1-trajectoire.json
51c6dad966bfbdbea4fa6e9a4d07a59f4bd8d2b4a7c01fd898ff8415a7eb44e7  diag/…/controle-positif-episode-2-trajectoire.json
df35b569588e295b71239dc16db055d65997afde1a895d3b233d047dc837b309  diag/…/controle-positif-episode-3-trajectoire.json
0169c0a1c23d94730837464eb33ea6800775cb98933bfaeb868d591516e463a5  diag/…/controle-positif-episode-4-trajectoire.json
d39cbf37a63c3a905e84bfac3bf21a89b4cccfe8e1e8a7ec8c292a54edd156af  diag/…/controle-positif-episode-5-trajectoire.json
046d05d03fcdb53b8bbc01e3e3aa5ba945b4716c7db0dd44cbf3e41d2c118a58  diag/…/controle-positif-episode-6-trajectoire.json
f3b05e86e38b44bb8a17f019486e66e8350503153e4659e98f96948df1de1f75  diag/…/controle-positif-episode-7-trajectoire.json
4e348234587e5b82b6022b99464e5147c5f5752356691ee007938d2a8e522f11  diag/…/production-episode-0-trajectoire.json
b33dee743ca26e7ebb654ce3508edddafedc8742b5b7c7af2b8d4834ca36356d  diag/…/production-episode-1-trajectoire.json
06f9d3d5712a73c6db24c2b8c41444726cc27e6cbd5004af33706348817f9ac1  diag/…/production-episode-2-trajectoire.json
d2bbdff9982ae9f78607f92ea63ff3a97f118f9722e80b6f431174e66e6a44eb  diag/…/production-episode-3-trajectoire.json
29faf5cf909f4dca71c64f8d9ab27a42af739cc13ac759bc01bd170a96ba135c  diag/…/production-episode-4-trajectoire.json
3c7eefc7db0ce675cc811c24050b03d4676524b72fc1af51015ded89daf25942  diag/…/production-episode-5-trajectoire.json
36fd32cb52df892ceb1a631cba71758facb1b26f74eb5cc0da5a4e71bd791306  diag/…/production-episode-6-trajectoire.json
74de7bfe248f48f8863f15e6059655614ddef556134509d55f6349f91b526f67  diag/…/production-episode-7-trajectoire.json
ab7092d7e93c4f393a790b7b9d7e60e26cc45d1278aac9d2e351ba8a9b8cb47d  diag/…/production-episode-8-trajectoire.json
336c596eec83c140c76a25f43770cedea8edf857659a54228cd93066de7dc501  diag/…/production-episode-9-trajectoire.json
fc2cf230a972b4f849913f828331c4d9cb20dca42413b26a4090b800aef4df04  diag/…/production-episode-10-trajectoire.json
ea15acf8606dd10038490cdd093f3c0d3cb9e19ffa0592f4f0ba156c1b186045  diag/…/production-episode-11-trajectoire.json
a46424375c9647660cc12345bf940bddebd3ef3a2d3900af654a8838efce7d5e  diag/…/production-episode-12-trajectoire.json
87c9eff248597b228b72ba6c0987ce07df19f53ebb79d7d26505fe8659eb5a0f  diag/…/production-episode-13-trajectoire.json
039bf7029610e2d5fb2f04948c3e9c69a1aad2585f6f07489f882d5fa7c7e3fb  diag/…/production-episode-14-trajectoire.json
2932e1b70a491be183114a48720576dfafdfee018579fc197c1aa5d4b8b23b0d  diag/…/production-episode-15-trajectoire.json

Traces : sha256sum -c empreintes.sha256 conforme dans chaque dossier
ec505b2a08b73a580c1413c32fd94695d377cc8939a431bf4b7ac408e200055c  traces/t04-20261005-145255-g2el/empreintes.sha256 (5 fichiers : journal.txt c65552a1…, tests.txt ccd3c5c2…, run-A.err f4854227… ; run-A.json et tests.err vides, scellés vides e3b0c442…)
3c541ddf8d4955154d66761e90009adafcbea36391fd6544c61679e3290cd0e7  traces/t04-instance-54332340-20261005-145534/empreintes.sha256 (3 fichiers : journal-instance.txt 3e394106…, etats-surveillance.txt ed2d33fa…, sortie-surveillance.txt e96a2a39…)

Code au commit cité dc7aa7f (git show <commit>:<chemin> | sha256sum ; identique dans mon clone)
5087f65af287b417e4cbf5aa1d6329e0ad756f6ce94b8eee75fabf32dc7943c8  src/controle_ia/harnais/validation_reelle.py
6cc0d8c0c1a2b2c641e59a2b57dc8d5c971f005dd758b01e9acf36fee2149bfe  src/controle_ia/harnais/episode.py
5a86cf105d230940695339c48f965ebb4205dc2f84ed96cddc295e738b15cf50  src/controle_ia/harnais/activations.py
c625a099fba580f098f3ce923b4cfa723c4cd3638f302c15f8fd74119d3a7797  src/controle_ia/harnais/modeles.py
0a85164c002a7993f951299e11e7beb6e67b9ba80e3394c46676353dde9dbd5f  src/controle_ia/harnais/politique.py
f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d  src/controle_ia/harnais/sondes.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d  src/controle_ia/manifeste.py
219fd033e2be492126c1ed9e538c359ed72b8c18b7aaee66b0c5c486fdd8329c  src/controle_ia/gardes.py
f143a0e93aa6c142d7aa98f9c7bffadb38e78f3cbb99bb340189da975c453dca  scripts/validation_t04_instance.sh (égal à la citation)
548c14c5e567187216cdc4d361b873782ddc1c3e04570b7759ca935fe559d9f4  scripts/amorce_instance_t04.sh (égal à la citation)

Registres, pour le contexte (non scellés ; lus à HEAD 93840ab)
cc5cfa5765e10d989a5793720b98745b9172333213c9019f9668164608918ef7  registres/decisions.md (R-042 à R-045)
deb14c46726513ab5a99ffe8130257b27d478d4889b01cda4c8255a5cd43f248  registres/depenses.md
```

**Le run est bien celui du préenregistrement** (`recalculs/02-identite-du-run.sortie.txt`) :
- commit du manifeste : `9767398a72846c46ea5fe0687d1b986f6c903e84`, commit de scellement du préenregistrement (même empreinte du préenregistrement à ce commit) ; il descend du commit cité `dc7aa7f` ;
- arbre gelé (chemins gelés du code cité) identique entre `dc7aa7f` et `9767398` (`git diff --quiet` : 0) ; arbres git de `src/`, `tests/`, `scripts/` et `.claude/` identiques aux trois commits `dc7aa7f`, `9767398` et HEAD ; `commit_cite` d'`arret.json` = `dc7aa7fcd6b5b0c676ec7365d2a194a3c1924efc` ;
- configuration du manifeste égale à `CONFIG_REELLE` du code cité, plus la révision citée ; empreinte de configuration recalculée `79f85dc19ff8aefca87ea94fa12baf66d77dd5a436ce6c8b21a943255424d289`, égale à celle consignée ;
- révision `0e9e39f249a16976918f6564b8830bc894c89659` et entropie `140696434425628814214803363501781803624` égales aux citations ; les 598 graines (logique 160, contrôle positif 80, production 320, débit 32, sondes 6) se refont à l'identique depuis l'entropie citée ;
- manifeste décisif, dépôt propre, aucune réserve, préenregistrement cité avec son empreinte ;
- fichiers du run commités par l'instance (`fe2022f`, parent `9767398` ; traces `6853b26`), inchangés depuis (`git diff` vide jusqu'à HEAD) ;
- machine relevée : NVIDIA H200 NVL, 139,8 Gio, pilote 580.95.05, CUDA 13.0, torch 2.14.1+cu130, cuDNN 92400 ; réglages relus : algorithmes déterministes, format TF32 coupé (produits et cuDNN), réductions en précision réduite coupées, cuDNN déterministe, banc d'essai coupé, un fil.

## 3. Prédiction par prédiction

Valeurs recalculées par moi depuis les données par action d'`arret.json` (rapports, profils, contrôles négatifs, lignes) et depuis les trajectoires scellées, pas depuis les bilans (`recalculs/03-recalculs-predictions.sortie.txt`, 096ef12f… ; détail `recalculs/03-recalculs-predictions.json`, 4359497a…). Tous les bilans consignés sont égaux à mes recalculs. Les 100 actions comparées (40 de logique, 20 du contrôle positif, 40 de production) sont cohérentes avec leurs trajectoires (début de l'action = longueur du contexte ; jetons relus = n, ou n − 1 pour la ligne la plus longue). Les 26 trajectoires d'épisodes résumés ont l'empreinte consignée.

| id | valeur recalculée | seuil ou règle | lecture gelée | `lecture_partielle` | accord |
|---|---|---|---|---|---|
| P0 | dernière ligne « 192 passed in 28.26s » ; 192 points de progression, aucune autre marque ; sortie d'erreur vide ; `tests-instance.json` identique aux traces | exactement 192 réussis, rien d'autre | conforme | `tests_instance` : conforme | oui |
| P1 | format vérifié (3 tours, 144 jetons) ; « Today Date: 26 Jul 2024 » dans l'ouverture ; 10 fichiers du modèle conformes (relevé identique à celui de la v1) ; carte 139,8 Gio ; mémoire vive effective 550,7 Go ; poids de la logique `torch.float64` ; **65 normalisations en double précision** | identité ; ≥ 130 Gio ; ≥ 96 Go ; 65 attendues | conforme ; pas de réserve sur les normalisations | `format` : conforme (le reste n'est pas une clé de lecture : gardes passées) | oui |
| P2 | maximum **9,776e-13** ; contexte 9,776e-13, zone générée 9,899e-14 ; par couche 7 / 15 / 23 : 5,21e-14 / 3,71e-13 / 9,78e-13 ; couverture : 28 actions remplies, 32 finies avant les autres, 1 850 positions générées comparées, lignes {1, 6} ; 40 actions | ≤ 1e-4 ; couverture | conforme | `logique_equivalence` : conforme | oui |
| P2b | 20 actions comparables, **20 vues** (100 %), aucune courte, aucun manque ; minimum des maxima **5,743e-2** (couche 23 ; minima par couche 0,247 / 0,116 / 0,0574) ; maximum du contexte **3,087e-13** | ≥ 95 % d'au moins 10 comparables ; contexte ≤ 1e-4 | conforme ; ligne « contexte du contrôle positif » non déclenchée | `controle_positif` : conforme | oui |
| P3 | 40 comparables, 40 passent, minimum des maxima 1,124 | ≥ 95 %, ≥ 10 | conforme | `logique_controle_negatif` : conforme | oui |
| P4 | maximum **0,5219** (épisode 1, action (1,9), couche 23, contexte) ; zone générée 0,0763 ; par couche 0,0678 / 0,2912 / 0,5219 ; **28 actions sur 40 au-dessus de 0,1** (couche 7 : 0 ; couche 15 : 22 ; couche 23 : 28 ; contexte : 28 ; zone générée : 0) ; 28 = nombre de fautes du motif d'arrêt | ≤ 0,1 | **contraire** | `production_equivalence` : contraire | oui |
| P5 | 40 comparables, 40 passent, minimum des maxima 1,061 | ≥ 95 %, ≥ 10, tolérance 0,1 | conforme | `production_controle_negatif` : conforme | oui |
| P6 | lot 0 rejoué (8 épisodes) : 5 empreintes identiques par épisode (trajectoire, activations, logits, vecteurs, scores), captures identiques (épisode 1, seul échantillonné du lot), empreintes des logits par action identiques | identité | conforme | `rejeu_en_processus` : conforme | oui |
| P7 | aucun run B : le script d'instance consigne l'arrêt de A puis sort (code 1) ; aucun run postérieur à A, aucune comparaison | identité | **non atteint** (aucune ligne ne le lit) | pas de clé (lu par `comparer_runs`) | sans objet |
| P8 | garde de relecture passée pour les 16 épisodes : dans le code, la relecture (`relire_et_controler`, arrêt à toute différence) précède le rejeu, le repère et les gardes d'équivalence ; `arret.json` contient les 16 épisodes avec l'empreinte de leur fichier npz, le stockage, le rejeu et le repère ; le motif est la garde d'équivalence | identité | conforme (attesté par l'ordre du code, non revérifiable hors de l'instance) | pas de clé | sans objet |
| P9 | zone générée : 0 écart nul sur 1 850 positions par couche (logique) et sur 1 402 (production) | au moins un écart non nul par phase | non déclenché | `audit_symetrie` : non déclenché | oui |

- `lecture_partielle` relue par `lire` du code cité sur le résumé partiel : identique pour les 9 clés. Mes lectures, refaites depuis les données par action : identiques aussi.
- Séparation entre D1 et l'arrondi (descriptif demandé au juge) : minimum des maxima de P2b sur maximum de P2 = 5,743e-2 / 9,776e-13 = **5,9e10** (10,8 ordres de grandeur) ; sur le maximum de la zone générée de P2 : 5,8e11.
- Domaine observé de la logique : contexte ≤ 1 096 jetons, ≤ 64 jetons générés relus, lot de 8, plus long contexte rempli d'un lot 1 226, remplissage ≤ 373. Contrôle positif : contexte ≤ 470, relus ≤ 56, rempli ≤ 628 (domaine plus court, prévu par le préenregistrement). Production : contexte ≤ 1 014, relus ≤ 86, rempli ≤ 1 447, remplissage ≤ 441.
- Descriptifs : pic de mémoire de la carte 78,3 Go (logique), 69,8 Go (contrôle positif), 19,0 Go (production) ; noyau « math » seul permis en logique ; flash, mémoire efficace, math et cuDNN permis en production. La phase de débit n'est pas atteinte.

## 4. Lignes de la table appliquées et suite prescrite

| ligne de la table | s'applique ? | pourquoi |
|---|---|---|
| P0 à P9 et P2b conformes, P9 non déclenché ; lecture de B = lecture de A ; P7 conforme | non | P4 contraire ; P7 non atteint ; pas de run B |
| P0 contraire | non | 192 réussis |
| P1 contraire | non | toutes les gardes de P1 passées |
| P2 contraire (> 1e-4) | non | 9,776e-13 |
| P2 : ≤ 1e-2, diffus (maxima du contexte et de la zone générée ≥ 1e-5, rapport ≤ 3) | non | maxima de 9,8e-13 et 9,9e-14, sous 1e-5 |
| P2 non concluant (couverture) | non | les quatre éléments de couverture sont présents |
| P2b contraire | non | 20 sur 20 |
| P2b non concluant (< 10 comparables) | non | 20 comparables |
| P2 non concluant, P2b contraire ou non concluant | non | aucun des deux |
| contrôle positif : maximum du contexte > 1e-4 | non | 3,087e-13 |
| P3 ou P5 contraire | non | 40 sur 40 dans les deux phases |
| P3 ou P5 non concluant | non | 40 comparables dans les deux phases |
| **P4 contraire** | **oui** | 0,5219 > 0,1 ; P2, P2b et P3 conformes : première branche |
| P6 contraire | non | 8 épisodes identiques |
| P7 contraire (différence, lecture de B ≠ A, ou arrêt de B) | non | B n'a pas tourné : ni différence, ni lecture de B, ni arrêt de B |
| P8 contraire | non | aucun arrêt de relecture |
| P9 déclenché | non | écarts non nuls dans la zone générée des deux phases |
| arrêt pour une cause d'infrastructure (réseau, instance perdue, durée) | non | arrêt par une garde, à 385 s sur 9 000 ; pas de signal TERM |
| arrêt pour une cause déterministe (noyau refusé, mémoire, mise en place) | non | aucune de ces causes ; motif : `GardeArret: production : 28 faute(s) de garde` |
| arrêt de cause indéterminée | non | cause écrite dans `arret.json` et dans `run-A.err` |
| A et B complets, résultats non poussés | non | A arrêté, résultats poussés et fusionnés |

**Règle de cumul.** Une seule ligne s'applique : « P4 contraire ». Sa lecture : « si P2, P2b et P3 sont conformes : logique validée, écart de demi-précision au-dessus du seuil de production ». La première ligne, seule à valider le critère 1, ne s'applique pas.

**Issue lue par aucune ligne.** P7 « non atteint » : la table n'a pas de ligne pour un run B jamais lancé après un arrêt de A sur une garde. Cela découle de la suite de la ligne P4 (« le run s'arrête après… »). La première ligne exige « lecture de B égale à celle de A ; P7 conforme » : le déterminisme entre deux processus n'est donc pas éprouvé en v2, et ce manque suffit, à lui seul, à exclure la première ligne. Le débit, non atteint, est descriptif : aucune ligne ne le lit.

**Suite prescrite par la ligne P4** (je la recopie, je n'en choisis aucune option) :
- « le run s'arrête après le stockage, la relecture, le rejeu et le repère de précision ». C'est fait : l'ordre du code et le contenu d'`arret.json` le montrent (stockage des 16 épisodes, relecture, rejeu du lot 0, repère, puis arrêt par la garde d'équivalence de la production) ;
- « réserve et nœud, au vu du repère ; options : extraction en simple précision, ou seuil de production révisé par v3 fondé sur le repère ».

Selon la table et R13, ce verdict est scellé puis soumis à Lazar.

## 5. Repère de précision et localisation des écarts de production

Je ne propose aucun seuil. Le préenregistrement dit qu'un seuil de production révisé, par une nouvelle version, se fonderait sur le repère, jamais sur le maximum observé.

### 5.1 Repère de précision

Le repère compare deux passes uniques : demi-précision bfloat16 (noyaux par défaut) contre double précision (phase de logique). Il porte sur les mêmes transcriptions, celles de l'échantillon de logique (épisodes 1 et 6, 2 agents, 4 245 jetons par couche), sans remplissage ni cache. Source : `arret.json`, `partiel.production.repere_precision`.

| couche | jetons | q50 | q99 | maximum |
|---|---|---|---|---|
| 7 | 4 245 | 0,0127 | 0,0290 | 0,0940 |
| 15 | 4 245 | 0,0143 | 0,0671 | 0,5124 |
| 23 | 4 245 | 0,0128 | 0,0874 | 0,7886 |

**Lecture descriptive.**
- La demi-précision seule s'écarte de la double précision d'environ 1,3e-2 par jeton en médiane, à toutes les couches.
- La queue est longue aux couches 15 et 23 : jusqu'à 0,51 et 0,79 par jeton. Ces maxima sont mesurés sans aucun chemin de génération, ni remplissage, ni cache.

### 5.2 Où sont les écarts de la production

Sources : `recalculs/04-localisation-production.sortie.txt` (107d7c8b…), `09-remplissage-et-domaine.sortie.txt` (3eff4806…), `10-zeros-contexte-production.sortie.txt`.

- **Zone.** Tous les dépassements de 0,1 sont dans le contexte, c'est-à-dire le préremplissage du lot de 8 comparé à la passe unique. Aucun n'est dans la zone générée : son maximum vaut 0,0763 (épisode 1, action (0,2), couche 15).
- **Couches.** Aucun dépassement à la couche 7 (maximum 0,0678). 22 actions dépassent à la couche 15 (maximum 0,291), 28 à la couche 23 (maximum 0,522).
- **Épisodes et actions.**
  - Épisode 1 : 15 actions sur 20, soit (0,4) à (0,9) et (1,1) à (1,9).
  - Épisode 14 : 13 actions sur 20, soit (0,4) à (0,9), (1,1), (1,2) et (1,5) à (1,9).
  - Sous le seuil : les pas 0 à 3 de l'agent 0, le pas 0 de l'agent 1, et les actions (1,3) et (1,4) de l'épisode 14.
- **Longueur du contexte.**
  - Les contextes des actions qui dépassent vont de 158 à 1 014 jetons ; ceux des actions sous le seuil, de 68 à 460. Toutes les actions de plus de 460 jetons de contexte dépassent.
  - Corrélation de rang entre la longueur du contexte et l'écart maximal d'une action : 0,82. En double précision, la logique donne 0,79.
- **Remplissage.**
  - Les deux seules actions sans remplissage (pas 0, agent 0, contexte de 68 jetons) ont un écart de contexte **exactement nul** à toutes les positions et à toutes les couches.
  - Les 38 actions remplies ont des écarts de contexte non nuls, avec une médiane par jeton de 0,014 à 0,019 à la couche 23. Cette médiane ne dépend pas de la quantité de remplissage (3 à 441 jetons).
  - Chacune des 38 actions remplies a exactement 3 positions de contexte à écart nul à la couche 7, et 2 aux couches 15 et 23. Les profils ne disent pas lesquelles ; ce sont probablement les premières positions.
  - En double précision, au contraire, actions remplies et non remplies ont le même niveau d'écart (médianes vers 1e-14).
- **Concentration.**
  - À la couche 23, pour les actions qui dépassent, le maximum vaut 1,6 à 6,6 fois le q99 du contexte (médiane 2,9) : le dépassement tient à quelques positions par action.
  - Médianes, sur les actions, du q50 par jeton (couches 7 / 15 / 23) : contexte 0,0145 / 0,0180 / 0,0164 ; zone générée 0,0135 / 0,0147 / 0,0127.

### 5.3 Situation par rapport au repère

- **Médianes.** Les médianes par jeton de la production (0,013 à 0,018) sont du même ordre que celles du repère (0,013 à 0,014).
- **Maxima.** À chaque couche, le maximum de la production vaut 0,72, 0,57 et 0,66 fois celui du repère (couches 7, 15 et 23). Le maximum du repère dépasse 0,1 aux couches 15 et 23, pas à la couche 7, comme la production. Ses q99 (0,029, 0,067, 0,087) sont sous 0,1.
- **Limite de la comparaison.** Elle porte sur des résumés : rien ne dit que les jetons qui dépassent en production sont ceux où le repère est grand. Le repère porte sur les transcriptions de la logique, pas sur celles de la production (voir section 7).

## 6. Audit de symétrie (R4)

### 6.1 P2, succès très propre (9,8e-13)

- **Captures et passe unique identiques par construction ? Non, d'après les données.**
  - Aucun écart n'est exactement nul : 0 sur 23 111 positions par couche (21 261 de contexte et 1 850 générées), soit 69 333 valeurs.
  - Pour les 40 actions, les deux tableaux sont distincts en mémoire, et une perturbation d'une unité au dernier rang, en double précision, change l'écart.
  - Le défaut D1, injecté dans la seule génération, porte l'écart de la zone générée de ≤ 9,9e-14 à ≥ 5,7e-2. Les captures viennent donc bien du chemin de génération : copiées de la passe unique, elles ne verraient pas D1.
- **Le décodage est-il exercé ?** Oui.
  - Données : 1 850 positions générées comparées (jusqu'à 64 par action) ; 28 actions remplies (jusqu'à 373 jetons) ; 32 lignes finies avant les autres ; lignes 1 et 6 du lot.
  - Contrôle négatif : 40 actions sur 40, minimum 1,12. La mesure voit un décalage d'un jeton.
- **Ordre de grandeur.**
  - 9,8e-13 est dans la fourchette annoncée (1e-16 à 1e-11). C'est environ quatre fois l'estimation tirée de la v1 par le rapport des arrondis unitaires (2,4e-13).
  - Le contexte (9,8e-13) dépasse la zone générée (9,9e-14). C'est un profil d'arrondi : préremplissage d'un lot de 8 contre passe unique d'une autre longueur. Ce n'est pas une signature de décodage.
- **Recoupements.**
  - 26 empreintes de trajectoires sur 26 sont égales aux empreintes consignées.
  - 100 actions sur 100 sont cohérentes avec leur trajectoire.
- **Limites propres à P2, déjà écrites dans le préenregistrement.**
  - Un décalage constant des positions absolues d'une ligne échappe à l'équivalence.
  - Seul le noyau d'attention « math » est exercé.
  - La validation vaut sur le domaine observé (section 3).
- **Non vérifiable.** Je ne vérifie pas la justesse numérique des profils. Ce sont des résumés calculés sur l'instance ; je vérifie leur cohérence interne, leur cohérence avec les trajectoires, et le recalcul des lectures.

### 6.2 P2b, défaut D1 vu très au-dessus du seuil

- **Contexte.** Le maximum du contexte des actions du contrôle positif vaut 3,1e-13, au niveau de P2. La ligne gelée « contexte du contrôle positif > 1e-4 » ne se déclenche pas : aucun désalignement propre à la phase.
- **D1 vu pour une autre raison ? Rien ne le montre.**
  - Dans le code, la seule différence avec la logique est `decalage_positions` : dans `generer_lot`, il ne touche que la position des jetons décodés (`suivante`).
  - Même modèle en mémoire, même noyau « math », même processus.
  - Graines propres : 80 tâches `controle-positif/…`. Les ouvertures sont identiques à celles de la logique, les actions différentes.
  - 0 écart nul sur les 627 positions générées par couche.
- **Ampleur.** Les valeurs sont dans la fourchette annoncée (1e-3 à 1). Le minimum par couche décroît avec la profondeur : 0,247, 0,116, 0,057.
- **Portée.**
  - La sensibilité est établie sur un domaine plus court que celui de P2 (rempli ≤ 628 contre 1 226), comme prévu.
  - Dans cet échantillon, les lignes 1 et 6 ne sont jamais les plus longues de leur lot (`recalculs/06-longueurs-actions.sortie.txt`). Le cas « dernier jeton non relu » n'y figure donc pas ; sans effet sur la lecture.
  - D1 décale toutes les positions décodées : c'est un défaut d'ensemble. P2b ne dit rien d'un défaut plus fin (une seule position, un seul pas), et le préenregistrement ne le revendique pas.

### 6.3 P4 contraire : défaut de logique ou précision ?

**Ce qui va dans le sens de la précision.**
- Le même code de harnais (positions explicites, remplissage, masque, cache, relecture des captures) est validé en double précision : P2, P2b et P3 sont conformes.
- Les dépassements sont tous dans le contexte, aucun dans la zone générée. Or un défaut de décodage se loge dans la zone générée, comme le montre D1.
- Les médianes par jeton de la production égalent celles du repère, et ses maxima restent sous ceux du repère, mesurés sans remplissage ni cache.
- Les maxima croissent avec la longueur du contexte, comme en double précision, et tiennent à quelques positions.
- Le contrôle négatif de la production est conforme : 40 sur 40, minimum 1,06.

**Ce qui reste ouvert.**
- La production emprunte un chemin que la logique n'exerce pas :
  - demi-précision bfloat16 ;
  - noyaux d'attention par défaut : flash, mémoire efficace, cuDNN et math permis. Le noyau effectivement choisi n'est pas consigné ;
  - normalisations RMS de la bibliothèque.
- L'apparition des écarts coïncide exactement avec la présence de remplissage : 0 exact pour les 2 actions sans remplissage, non nul pour les 38 remplies. Deux causes l'expliqueraient :
  - un changement de noyau quand le masque n'est pas trivial ;
  - un défaut propre au traitement du masque par un noyau fusionné.
- Contre une fuite grossière à travers le masque : l'écart médian ne dépend pas de la quantité de remplissage (3 à 441 jetons). De plus, 2 ou 3 positions de contexte par action remplie restent identiques au bit près.
- Le domaine de remplissage de la production dépasse celui de la logique : 441 contre 373 jetons de remplissage au plus ; 1 447 contre 1 226 de longueur remplie.

**Conclusion d'audit.**
- Les données favorisent la précision, sans l'établir. Elles n'excluent pas un défaut propre au chemin de production (demi-précision et noyaux fusionnés avec remplissage à gauche), que P2 ne couvre pas.
- Cela ne change pas la lecture gelée : P2, P2b et P3 sont conformes, donc « logique validée ». C'est une réserve à porter au nœud.

### 6.4 Autres points

- **P6.** Conforme, mais limité au lot 0 de la production. Les captures n'y existent que pour l'épisode 1. La logique n'est pas rejouée dans le processus.
- **P8.** Attesté par l'ordre du code et par le contenu d'`arret.json`, pas par une relecture indépendante (section 7).
- **P9.** Non déclenché.
  - En production, le contexte compte 250, 212 et 212 écarts nuls (couches 7, 15, 23).
  - 136 viennent des deux actions sans remplissage (68 positions chacune) ; les autres sont les 2 ou 3 positions par action remplie déjà décrites.
  - P9 ne porte que sur la zone générée. Elle n'a aucun écart nul.
- **Trace d'instance.** Après la fin de l'amorce (code 1), le conteneur a relancé l'amorce 16 fois entre 14:53:07 et 14:55:05. La garde R12 l'a refusée chaque fois (« dossiers d'un essai précédent présents ») : aucun second run. La session a ensuite arrêté l'instance par son identifiant (R-045). C'est sans effet sur la lecture.

## 7. Limites et ce qui reste hors de portée

**Ce que contient le disque de l'instance arrêtée**, d'après le code, et non vu par moi :
- les 16 fichiers `donnees/20261005-144628-validation-reelle/production-episode-<k>-tableaux.npz`, avec leurs compagnons ;
- dans chacun : les vecteurs d'action et les scores de sondes de l'épisode ; pour les épisodes 1 et 14 seulement, les activations par jeton de la passe unique, codées en bfloat16 (48 272 518 et 41 686 150 octets) ;
- leurs empreintes sont consignées dans `arret.json` (`tableaux_sha256`) : on peut les contrôler s'ils sont récupérés ;
- s'y trouvent aussi le cache du modèle et les journaux.

**Ce qui n'existe nulle part**, d'après le code, seulement en mémoire puis résumé par des profils et des empreintes :
- les captures de génération, de toutes les phases ;
- les activations en double précision de la logique ;
- celles du contrôle positif ;
- les passes uniques en demi-précision du repère.

**Ce que cela empêche de conclure :**
1. Je ne peux pas dire quels jetons portent les dépassements de la production (en-tête, séparateurs, tours précédents…), ni s'ils coïncident avec les jetons où la demi-précision s'écarte le plus de la double précision. Précision et défaut propre au chemin de production restent donc inséparables. Même le disque de l'instance ne le permettrait pas, faute de captures de génération : il faudrait un nouveau calcul, et c'est l'affaire du nœud.
2. Je ne peux revérifier aucun écart numérique. Je vérifie la cohérence des résumés et je recalcule les lectures.
3. Je ne peux pas revérifier P8 de façon indépendante.
4. Je ne peux pas comparer les fichiers du modèle aux empreintes publiées (pas de réseau). Ils sont attestés par la garde du code sur l'instance, et leur relevé est identique à celui de la v1 (même révision, autre instance).
5. Le noyau d'attention effectivement choisi en production n'est pas consigné.
6. P7 : le déterminisme entre processus n'est pas éprouvé en v2, ni la lecture de B. Le débit n'est pas mesuré.
7. Le préenregistrement garde l'instance arrêtée avec son disque jusqu'à ce verdict. Les fichiers npz de la production n'existent que là : leur destruction est irréversible.

## 8. Transparence

- **Qui je suis.** Contexte neuf. Je n'ai vu aucune des conversations qui ont produit le préenregistrement, le code ou l'analyse. Je tourne sur le même modèle (Claude Opus 5.5) que l'auteur et les contre-lecteurs : un biais commun reste possible.
- **Ce que j'ai lu.**
  - Le préenregistrement v2 en entier.
  - `manifeste.json`, `arret.json` (dont `partiel` et `lecture_partielle`), `tests-instance.json`, `environnement-python.json`, et les 32 trajectoires.
  - Les deux dossiers de traces.
  - Les registres : R-042 à R-045, et les dépenses (0,74 heure cumulée sur 6 ; reste 5,26).
  - Le code cité : `validation_reelle.py` (en entier), `episode.py`, `activations.py`, `modeles.py`, `politique.py`, `exiger_identite` de `sondes.py`, `manifeste.py`, `gardes.py`, et la séquence des runs A et B du script d'instance.
  - Le début du verdict de la v1.
- **Ce que je n'ai pas lu.** Les rapports de contre-lecture, la procédure v3 (seulement empreintée), le brief et le programme au-delà de la ligne du critère.
- **Ce que j'ai lancé** (processeur seulement, depuis mon clone, `PYTHONPATH=src`) :
  - `01-verifier-empreintes.sh` ;
  - `02-identite-du-run.py` ;
  - `03-recalculs-predictions.py` ;
  - `04-localisation-production.py` ;
  - `05-controle-positif-trajectoires.py` ;
  - `06-longueurs-actions.py` ;
  - `09-remplissage-et-domaine.py` ;
  - `10-zeros-contexte-production.py` ;
  - les commandes de `07-arbre-code-registres.sortie.txt` : `verifier-arbre` (« arbre intact ») et empreintes du code ;
  - la suite de tests du clone : `08-tests-processeur-clone.sortie.txt`, 192 réussis en 88 s. C'est un contrôle de cohérence ; P0 se lit sur la sortie de l'instance.
- **Ce que je n'ai pas fait.** Aucune commande `vastai`, aucun accès réseau, aucune lecture de jeton, aucune dépense. Aucune écriture dans le dépôt de référence : à la fin, `git --no-optional-locks status` y est vide et HEAD reste `93840ab`.
- **Ce que je n'ai pas pu vérifier.** Voir la section 7 : valeurs par jeton, justesse numérique des profils, relecture npz, empreintes publiées du modèle, noyau choisi en production, run B.
