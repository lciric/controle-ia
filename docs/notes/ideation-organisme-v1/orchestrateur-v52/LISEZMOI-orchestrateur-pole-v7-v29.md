# Orchestrateur du pôle, version 0.7.0 — la course joue la génération, clé en deux parties, ordre dérivé de la clé, journal en lecture seule, gardes obligatoires (contre-lecture de la conception v10) — LISEZMOI v29

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v29 écrite après le relevé `date -u` de 02:07:46
UTC le 28 octobre ; v1 à v28 gardées (R12). Suit la **conception v11 du pari apparié borné**
(`../pari-de-signe/conception-pari-de-signe-v11.md`) après la contre-lecture de la v10 et de la version 28
(`../pari-de-signe/contre-lecture-v10/rapport-contre-lecture-pari-signe-v10.md`, `7bb83a48…` : K10-1 à K10-10 ; les chaînes
de la contre-lecture v9 rejouées contre la v28, toutes refusées ou sans effet). v11 et v29 pas encore contre-lues.

| changement | fichiers |
|---|---|
| **K10-1, K10-2** `jouer_generation(course, monde, engagements, abandons_avant=…, non_lancees=…, abandon_apres=…)` : joue une génération entière ; les décisions « avant toute issue » sont des **entrées** ; parties calculées, journalisées (génération de la course) et ajoutées **ici** ; compte rendu **sans trajectoire** | `pole/engagement_apparie.py` |
| **K10-3** ordre secret dérivé de l'**empreinte de la clé** (plus du nom, du budget ni de l'empreinte de l'engagement), de la génération et de la graine scellée du monde ; le monde utilise son **identité**, plus son empreinte (une unité factice ajoutée ne change plus l'ordre) | `pole/engagement_apparie.py`, `pole/monde_banque_scores.py` |
| **K10-4** journal en lecture seule pour l'appelant (`Lignees.journal` est un tuple ; ajout par `journaliser` seul) ; identifiants d'unités gardés ; génération entière exigée (une chaîne est refusée) | `pole/engagement_apparie.py` |
| **K10-5** partie **vide** journalisée vide (`marquer_vide`) et acceptée par la course comme déclaration « sans partie » | `pole/engagement_apparie.py`, `pole/pari_apparie.py` |
| **K10-6** clé en **deux parties** : `affirmation` (contrastes canoniques, comparateurs, τ, strate, seuils, gardes) et `lecture` (partie, plan, population, pondération, m_max, Λ, e-processus) ; `empreinte_affirmation` ; `Lignees` tient « une affirmation, une fiche » sur l'affirmation (fiche espionne à autre population : refusée) | `pole/engagement_apparie.py` |
| **K10-7** `Course(alpha, journal, essai=False)` : course sans journal ou entrée sans clés **refusées** sauf `essai=True` | `pole/pari_apparie.py` |
| **K10-8** lecture L3 : par partie, le **processus qui fixe le minimum** (contraste ou garde) et toutes les richesses ; dans la course publiée : `garde:blanc-juge`, `garde:blanc-cascade`, `garde:blanc-cascade` — les gardes sont la contrainte active de la forme G1 | `demonstrations/demo_pari_apparie_v7.py` |
| **K10-10** essai « Λ changée ⇒ clé changée » ; démonstration sur `jouer_generation` ; sept artefacts (+ fiche espionne, + course sans journal) | `essais/test_v7_engagement_apparie.py`, `essais/test_v7_demo_pari_apparie.py`, `demonstrations/demo_pari_apparie_v7.py` |

**278 essais passent** (295 s sous charge).

**Course publiée (v29, `../pari-de-signe/demonstration-v29/`)** : mêmes réglages que v27 et v28. L1 (espérance conditionnelle)
tenue ; contrôle 12 : jumeau non promu ; témoins promus aux décalages 1,2 et 1,0 (génération 2, sortie Bonferroni oui), 0,5
(génération 2, non), 0,8 concentré (génération 4) ; 0,1 non promu ; forme-G1 promue par e-BH en génération 3, **sortie
e-Bonferroni : non**, processus minimal : une garde à chaque partie ; 25 fiches, 25 affirmations (vrai par construction depuis
que la mémoire refuse les redites) ; nul × 200 : 0 promotion ; sept artefacts refusés. Les ordres de lecture ont changé
depuis la v28 (K10-3) : les log e des témoins bougent de quelques dixièmes, les promotions sont les mêmes.

**Frontière de confiance (dite, v11)** : le code ne garantit que ce qui passe par lui ; le monde tient les scores d'épreuve,
la course les lit ; l'orchestrateur ne reçoit que des comptes rendus.

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -I -B -m unittest                                                              # 278 essais
$PY -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF --nul 200             # ≈ 90 s
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v29.txt
```

Le reste : LISEZMOI v28 à v1.
