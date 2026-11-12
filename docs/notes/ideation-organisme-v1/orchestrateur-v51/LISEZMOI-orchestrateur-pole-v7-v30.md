# Orchestrateur du pôle, version 0.7.0 — deux passes dans la génération, journal qui fixe trajectoire et clé, fiches fantômes refusées, unités journalisées lues (contre-lecture de la conception v11) — LISEZMOI v30

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v30 écrite après le relevé `date -u` de 02:41:56
UTC le 28 octobre ; v1 à v29 gardées (R12). Suit la **conception v12 du pari apparié borné**
(`../pari-de-signe/conception-pari-de-signe-v12.md`) après la contre-lecture de la v11 et de la version 29
(`../pari-de-signe/contre-lecture-v11/rapport-contre-lecture-pari-signe-v11.md`, `ee82b1ee…` : K11-1 à K11-7). **v12 et v30
ne sont pas contre-lues : c'est la première tâche de la reprise sur ce sujet.**

| changement | fichiers |
|---|---|
| **K11-1** `jouer_generation` en **deux passes** : toutes les parties calculées, journalisées et ajoutées avant qu'`abandon_apres` ne voie une issue ; une exception au milieu est **tracée** (`Lignees.interrompre`, `interruptions`) et la reprise ne recalcule aucune partie journalisée (K11-4) | `pole/engagement_apparie.py` |
| **K11-3** le journal enregistre l'**empreinte de la trajectoire** ; la course refuse une trajectoire fabriquée, une clé déclarée différente de celle du journal, un abandon « avant partie » dont la partie est au journal, une **fiche fantôme** au journal, une entrée d'une génération à venir ; à la lecture, toute unité journalisée dans la génération est enregistrée comme lue (`premiere_lecture`) ; `evaluer(..., essai=False)` exige un journal hors essai | `pole/pari_apparie.py` (`_empreinte_trajectoire`), `pole/engagement_apparie.py` |
| **K11-7** docstrings à la version 30 ; essais : évaluation sans journal refusée, trajectoire fabriquée, abandon avant partie refusé, fiche fantôme, unités journalisées lues, deux passes, interruption tracée | `essais/test_v7_demo_pari_apparie.py` ; tests et démonstration : `essai=True` sur les évaluations hors course |

**279 essais passent.** Course publiée (`../pari-de-signe/demonstration-v30/`) : identique à la v29 en promotions (mêmes
ordres, mêmes clés) ; sept artefacts refusés ; nul × 200 : 0 promotion.

**Côté de confiance (v12)** : banque d'épreuve, monde et sa graine, course et journal, construction des engagements ;
l'orchestrateur n'y est pas. Ce que le code ne peut pas faire : vérifier l'authenticité d'un journal ou d'une course qu'on
lui passe.

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -I -B -m unittest                                                              # 279 essais
$PY -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF --nul 200
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v30.txt
```

Le reste : LISEZMOI v29 à v1.
