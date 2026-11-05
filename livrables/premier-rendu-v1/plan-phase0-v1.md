# Plan de phase 0 ordonnancé — v1

Période : 5 octobre → 1er novembre 2026 (M0). Porte de sortie : G0. Rédigé le 2026-10-04.
Hypothèses du plan : GO sur le devis de phase 0 et jeton HuggingFace reçus au plus tard le 12 octobre ; accès à arxiv.org et budget de recherche web relevé au plus tard le 7 octobre.

## 1. Tâches, dépendances, matériel

| Tâche | Contenu | Dépend de | Matériel | Fenêtre |
|---|---|---|---|---|
| T0.1 | Socle, gouvernance, gardes, continuité | — | processeur | **fait le 4 oct.** (reste : dépôt distant, nœud N-001) |
| T0.2 | Vérification de l'état de l'art sur PDF empreintés ; ressources et licences ; message FakeLab | accès arxiv.org + budget de recherche web | processeur | ressources de code : fait ; recherche web : partielle ; PDF : 7 → 16 oct. |
| T0.3 | Note mathématique, préenregistrement, contre-lecture, simulation, figures, résultats scellés | note v1 (fait) ; N-003 et N-004 pour la formulation des revendications (pas pour le run) | processeur | 5 → 16 oct. |
| T0.4 | Harnais d'épisodes : génération, passe avant unique, crochets, garde d'équivalence, rejeu au bit près, indexation (i, t), estimation du stockage | — | processeur (petit modèle Llama à poids aléatoires), puis GPU (validation sur 8B) | code 6 → 12 oct. ; GPU session 1 |
| T0.5 | Environnement (a) v0 : propositions d'expériences, cibles semées, évaluateur faible, contributions (i, t) | T0.2 (code de Terekhov et al. public ?) ; T0.4 | processeur puis GPU | conception 8 → 13 oct. ; pilote en session 1 |
| T0.6 | Organismes (i) instruction cachée et (ii) LoRA par distillation ; contrôles croisés ; dose-réponse | T0.5 ; décision P-002 (famille iii) | GPU | (i) session 1 ; (ii) session 2 |
| T0.7 | Sondes v0 : 4 concepts, 5 familles, agrégation max ou attention, plancher apparié, anti-circularité, test de validité (i)/(ii) | T0.4 ; T0.6 | processeur (code) puis GPU (activations) | code 12 → 18 oct. ; session 2 ; analyse 21 → 24 oct. |
| T0.8 | Bases boîte noire : par action, TRACE-lite, séquentielle | T0.5 ; T0.6 ; D1 | processeur (code) puis GPU | code 12 → 18 oct. ; session 2 |
| T0.9 | Papier C : conception et préenregistrement HC1 à HC3 ; pilote sur GO | ressources P3 ; T0.2 (2607.08066, 2508.07805, 2606.07897) ; N-005, N-006 ; D2 | processeur ; pilote GPU sur GO | 14 → 28 oct. ; pilote en session 3 |
| Prérég. G1 | Plan 2 × 2, métriques, seuils, critère disjonctif, liste d'arrêt | T0.5 à T0.8 conçus ; T0.3 | processeur | 22 → 28 oct. |
| G0 | Dossier de preuves, verdict par sous-agent neuf (R13), GO | tout | processeur | 29 → 31 oct. |

## 2. Sessions GPU (chacune sur GO, scripts de lancement prêts, arrêt par identifiant)
- **Session 1 (≈ 13–15 oct.)** : validation du harnais sur Llama-3.1-8B-Instruct (déterminisme, équivalence) ; pilote de l'environnement (a) ; grille dose-réponse de la famille (i).
- **Session 2 (≈ 19–23 oct.)** : distillation et LoRA de la famille (ii) ; extraction des activations ; sondes ; moniteurs boîte noire sur les mêmes épisodes.
- **Session 3 (≈ 27–29 oct.)** : reprises, pilote du papier C (GO séparé), marge.

## 3. Chemin critique
GO devis + jeton HuggingFace → session 1 (harnais 8B → environnement → famille i) → session 2 (famille ii → sondes au-dessus du plancher ; boîte noire sur les mêmes épisodes) → préenregistrement G1 → G0.
En parallèle, sur le chemin critique de G0 (critère 8), de T0.5 et de T0.9 : accès arxiv.org et budget de recherche → T0.2.
Marge : T0.3 (indépendante, doit finir vers le 16 oct.) ; T0.9 (doit finir le 28 oct.).

## 4. Ce qui avance sans GPU d'ici le premier GO
T0.2 (dès l'accès), T0.3 en entier, tout le code de T0.4, T0.7 et T0.8 testé sur un petit modèle à poids aléatoires (aucun téléchargement), la conception de T0.5, T0.6 et T0.9, les scripts de lancement Vast.ai et le préenregistrement de G1.
