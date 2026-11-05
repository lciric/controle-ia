# Orchestrateur du pôle, version 0.7.0 — fraîcheur par rapport à la course, clé canonique, plan des tranches scellé, journal tenu par `evaluer` (contre-lecture de la conception v9) — LISEZMOI v28

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), v28 écrite après le relevé `date -u` de 01:32:15
UTC le 28 octobre ; v1 à v27 gardées (R12). Suit la **conception v10 du pari apparié borné**
(`../pari-de-signe/conception-pari-de-signe-v10.md`) après la contre-lecture de la v9 et des versions 26 et 27
(`../pari-de-signe/contre-lecture-v9/rapport-contre-lecture-pari-signe-v9.md`, `b73789ca…` : K9-1 à K9-10 ; code « à
corriger »). **Correction de ce que le LISEZMOI v27 affirmait** : voir « lectures corrigées » ci-dessous. v10 et v28 pas
encore contre-lues.

| changement | fichiers |
|---|---|
| **K9-1** fraîcheur **par rapport à la course** : `Course.premiere_lecture` (unité → génération de première lecture par quelque fiche) ; une unité lue à une génération antérieure est refusée à toute fiche ; une tranche se partage dans sa génération, jamais ensuite | `pole/pari_apparie.py` |
| **K9-2** clés tenues par la course : `entrer(..., cles=…)`, `ajouter_trajectoire(..., empreinte_cle=…)` refuse une partie d'une autre clé ; `Lignees.entrer` refuse une seconde clé pour une fiche ; identifiants d'unités par l'**identité** stable de la banque (`banque["identite"]`, sinon l'empreinte) | `pole/pari_apparie.py`, `pole/engagement_apparie.py`, `pole/monde_banque_scores.py` |
| **K9-3** clé **canonique** : contrastes par forme (cellules triées, coefficients, constante), sans nom libre ; deux contrastes de même forme dans une fiche refusés ; renommer n'est pas une autre affirmation ; la démonstration refuse les redécouvertes du proposeur (redites tracées) | `pole/engagement_apparie.py` (`canonique`), `demonstrations/demo_pari_apparie_v7.py` |
| **K8-4 / K9-4** champ `e_processus` (combinaison sur Λ, règle d'arrêt, module, version 28) dans la clé ; essai « règle changée ⇒ clé changée » | `pole/pari_apparie.py` (`E_PROCESSUS`), `pole/engagement_apparie.py`, `essais/test_v7_engagement_apparie.py` |
| **K9-5** `construire(..., plan_tranches=…)` : plan des tranches (unités par génération, disjointes, dans la partie) **scellé dans la clé** ; `evaluer(monde, engagement, generation=g, …)` lit la tranche du plan dans l'ordre dérivé de l'empreinte et de g ; plus d'étiquette libre ; une tranche libre demande sa génération ; refus d'unités libres avec un plan | `pole/engagement_apparie.py` |
| **K9-6** `evaluer(..., fiche=…, journal=…)` **journalise lui-même** ; `Lignees.journaliser` refuse une seconde évaluation de la fiche dans la génération ; `Course(alpha, journal=…)` refuse à l'ajout une partie absente du journal ou d'une autre empreinte d'unités, et à la lecture une déclaration « sans partie » contredite | `pole/engagement_apparie.py`, `pole/pari_apparie.py` |
| **K9-9** plusieurs gardes dans `pa.evaluer` (dictionnaire ; le minimum porte sur tous les contrastes et toutes les gardes) ; `construire(garde=[…])` : une garde par comparateur ; `log_gardes_finales` | `pole/pari_apparie.py`, `pole/engagement_apparie.py` |
| **K9-10 c** déclaration « sans partie » refusée pour une fiche gelée, arrêtée, promue, exclue, non entrée ou qui a sa partie | `pole/pari_apparie.py` |
| démonstration : vérité de L1 = **espérance conditionnelle aux seuils scellés** (analytique ; K9-7) ; témoin « faux nul » lu comme **contrôle 12** ; fiche « forme-G1 » avec cinq gardes, sortie **e-Bonferroni** rapportée, richesses descriptives (K9-8) ; décisions « avant partie » avant toute issue de la génération (K9-10 b) ; décalages de loi (K9-10 e) ; cinq artefacts R5 ; essai `test_nul_repete` corrigé (Bonferroni ⊂ e-BH, K9-10 d) | `demonstrations/demo_pari_apparie_v7.py`, `essais/test_v7_demo_pari_apparie.py` |

**276 essais passent** (455 s sous charge ; 185 s à vide pour la v27).

## Lectures corrigées (ce que le LISEZMOI v27 disait, et ce qui est vrai)

- v27 : « L1 tenue : aucune fiche d'espérance ≤ 0 promue » — la vérité y était le signe **en population** ; conditionnellement
  aux seuils scellés (là où porte la garantie), les jumeaux de même loi ont des seuils différents et le « faux nul »
  valait +0,035 ; en courses répétées cette L1 se lisait « rompue » dans 13,5 % et 34 % des cas **sans aucune fausse
  promotion conditionnelle** (0 sur 250). **v28** : L1 sur l'espérance conditionnelle, tenue ; le jumeau est un contrôle 12
  (« jumeau non promu » dans la course publiée).
- v27 : « G1 promue en génération 3 » — par la lecture **e-BH de la course du pôle**, qui n'est pas la lecture de G1 (une
  fois, hors de la suite, N-050) ; sous e-Bonferroni (ce qui sort du pôle), la fiche ne sortait que dans 16 % des courses.
  **v28** : « forme-G1 » promue par e-BH en génération 3, **sortie e-Bonferroni : non** (log e 5,22 pour un seuil de fiche
  seule de 6,87) ; « comparateur le plus faible » retiré (bruit).
- v27 : « dents jusqu'à la force 0,5 » — ce sont des **décalages de loi** (0,5 ≈ 14 points de rappel), pas des points.
  **v28** : témoins promus aux décalages 1,2 et 1,0 (génération 2, sortie Bonferroni oui), 0,5 (génération 2, Bonferroni
  non), 0,8 « concentré » (génération 4) ; 0,1 non promu (espérance conditionnelle +0,000). 25 fiches, 25 affirmations ;
  nul × 200 : aucune promotion (Wilson [0 ; 0,019]). Les artefacts : cinq refus.

```
PY=/opt/venv-essaim-sim-v1/bin/python
$PY -I -B -m unittest                                                              # 276 essais
$PY -I -B demonstrations/demo_pari_apparie_v7.py DOSSIER_NEUF --nul 200             # ≈ 90 s
sha256sum -c EMPREINTES-orchestrateur-pole-v7-v28.txt
```

Le reste : LISEZMOI v27 à v1.
