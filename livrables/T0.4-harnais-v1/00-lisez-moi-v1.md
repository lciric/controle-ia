# T0.4 — harnais d'épisodes et journalisation des activations — livrable v1

Date : 2026-10-06 (UTC). Dépôt : https://github.com/lciric/controle-ia (privé), branche `main`.

## Verdict
- **Critère 1 de la porte G0 (« Harnais validé : déterminisme, équivalence d'activations, gardes testées ») : prouvé** sur le modèle réel de l'agent (Llama-3.1-8B-Instruct), par les runs A `20261006-114025-validation-reelle` et B `20261006-115440-validation-reelle` (rejeu dans un second processus).
- Verdict R13 d'un juge neuf : `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md`, sha256 `63444faa4ce253fcfc19981224ab95bc243e9b2c74bf83daf181d0059d5b4a13`. Seule la première ligne de la table gelée s'applique ; aucune réserve au sens de la table.
- Préenregistrement appliqué : `prereg/T0.4-validation-modele-reel-v3.md`, sha256 `4f711cd3a58182856c804e6652ec92c1aaab865fe9b595ea1d6be65757b8ed5f`, deux contre-lectures neuves (R2). Code cité : commit `b6ab5d15e76972a70e7ffc90cce4dbe280d03061`, 206 tests réussis sur l'instance.

## Ce que le harnais fait
- Épisodes joués par lots, en pas synchronisés (agent i, pas t), remplissage à gauche et positions explicites ; transcriptions en jetons, jamais retokenisées.
- Activations du flux résiduel aux blocs 7, 15 et 23, par une passe avant unique sur la transcription complète ; une garde compare, sur un échantillon, les activations capturées pendant la génération à celles de la passe unique.
- Stockage : activations par jeton sur un sous-échantillon, vecteurs par action et scores de sondes en ligne pour tous ; relecture du disque au bit près.

## Les trois versions de la validation
| version | carte | ce qui a été lu | verdict |
|---|---|---|---|
| v1 (2026-10-05) | A100 80 Go | logique en simple précision stricte : écart maximal 1,27e-4 pour un seuil de 1e-4 | non concluant (précision probable) ; nœud N-010 |
| v2 (2026-10-05) | H200 NVL | logique en double précision validée (9,8e-13 ; défaut D1 vu 20 fois sur 20) ; production en demi-précision au-dessus du seuil sur le maximum (0,52 > 0,1) ; pas de rejeu entre processus | non prouvé ; nœud N-011 |
| v3 (2026-10-06) | H200 NVL | tout conforme, rejeu entre processus identique | **prouvé** |

## Chiffres de la v3 (recalculés par le juge depuis les données par action)
- Logique, double précision : écart maximal 3,10e-13 (seuil 1e-4) ; défaut D1 injecté vu pour 20 actions sur 20 (au moins 8,3e-2).
- Chemin de production, simple précision, noyau « math » : écart maximal 3,16e-4 (seuil 3e-3) ; D1 vu 20 fois sur 20 (au moins 6,8e-2).
- Production, demi-précision : plus grand 99e centile par action et par couche 0,0334 (seuil 0,2) ; maximum 0,162, rapporté sans seuil ; rapport au repère de précision 0,656, 0,550 et 0,391 (au plus 3).
- Contrôles négatifs (décalage d'un jeton) : 40 actions sur 40 dans chacune des trois phases.
- Rejeu dans le processus et entre processus : identique, hors durées, débits et pics de mémoire.

## Domaine de validité
Carte H200 NVL, pilote 580.159.03, CUDA 13.0, torch 2.14.1+cu130, transformers 5.18.0, noyau d'attention « math », lot de 8. Validé strictement (chemin) jusqu'à 1 087 jetons de contexte rempli (contexte comparé 1 083, 92 jetons générés relus) ; production observée jusqu'à 1 192. Hors de ce domaine : revalider, ou garder la garde d'équivalence en ligne sur un échantillon.

## Observations portées à Lazar (sans effet sur la lecture)
1. Au noyau « math », le contexte de la production coïncide au bit près avec la passe unique (lignes remplies comprises) : la garde de production lit la seule zone générée.
2. Le débit a été mesuré sur des contextes d'au plus 1 271 jetons, pas 2 048 : 41,2 Go au pic, environ 119 jetons générés par seconde pour un lot de 32. L'avantage budgétaire prêté par N-011 à l'option retenue reste à établir dans le devis des phases suivantes.
3. La production dépasse un peu le domaine strict du chemin (1 192 contre 1 087 jetons).
4. La relecture du disque et les fichiers du modèle sont attestés par les gardes de l'instance, pas relus hors d'elle.

## Coût
Carte : 1,31 heure sur les 6 du devis de T0.4 (cumul des tentatives). Phase 0 : environ 5,1 USD dépensés sur un plafond de 150, plus le stockage des instances arrêtées (destruction recommandée, décision de Lazar, N-009).

## Pièces
| pièce | contenu |
|---|---|
| `T0.4-validation-modele-reel-v3.md` | le préenregistrement scellé (copie ; original et empreinte dans `prereg/`) |
| `verdict-T0.4-critere-1-G0-v3.md` | le verdict R13 (copie ; original dans `docs/verdicts/`, recalculs du juge dans `…-v3-recalculs.tar`, sha256 `9f115e2ad9002006900da3cf21f9a0b7aeed9e1e2605f7082c59f055c5fecdbe`) |
| `validation-T0.4-modele-reel-v4.md` | la procédure de lancement appliquée (copie ; original dans `docs/procedures/`) |
| dans le dépôt | code `src/controle_ia/harnais/` ; contre-lectures `prereg/contre-lectures/T0.4-v3-*` ; résultats `diag/20261006-114025-validation-reelle/` et `diag/20261006-115440-validation-reelle/`, manifestes `runs/` ; traces `traces/t04-20261006-120752-qRPl/` et `traces/t04-instance-54476244-20261006-121128/` ; notes de mémoire `docs/notes/` ; versions antérieures (v1, v2) et leurs verdicts |

## Ce qui reste ouvert
- Points reportés à une version ultérieure du code, sans effet sur la lecture d'un run : R-037 (v1), W-5 (v2), Y-3 et Y-8 (v3 : deux tests du débit, un libellé).
- Débit et mémoire à des contextes de 2 048 jetons, au noyau « math », pour le devis des phases suivantes.
