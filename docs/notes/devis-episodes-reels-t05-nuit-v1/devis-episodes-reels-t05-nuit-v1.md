# Devis : lot d'épisodes réels de la banque T0.5, nuit du 1er au 2 novembre 2026 (v1)

Statut : devis seul ; rien dépensé, lancé ni scellé (20:05 UTC, R-994).

## Verdict

**Faisable cette nuit, mais pas avec des tâches neuves.** Les 96 tâches de l'environnement ont toutes été courues. Un lot « neuf » ne peut donc être, d'ici 09:00 UTC, que de **nouveaux épisodes (graines neuves) sur des tâches déjà vues**. Il faut en plus quatre conditions : le mot direct de Lazar et une ligne GO ; une fiche scellée, contre-lue (R2) et essayée en jouet (R5) avant 21:30 UTC ; les critères de lecture gelés avant la lecture ; la configuration du pilote inchangée.

## 1. Chaîne existante et réserve de tâches

- Modèles (VÉRIFIÉ, `prereg/T0.5-pilote-8B-v1.md` l. 9) : l'agent et le juge 8B sont Llama-3.1-8B-Instruct `0e9e39f2…` ; le juge 3B est Llama-3.2-3B-Instruct `0cb88a4f…`. La grille est celle du pilote, rubrique H.4, invite b0 (même fiche, l. 38-43). La configuration donne 3 épisodes par tâche, une température de 1,0 pour l'agent comme pour les juges et un plafond de 15 000 s par course (VÉRIFIÉ, `prereg/T0.5-pilote-config-v1.json` l. 4, 7, 56, 59).
- Pilote : 60 tâches, 180 épisodes (VÉRIFIÉ, `registres/decisions.md` l. 280).
- Couche 1 bis : 36 tâches, 108 épisodes (VÉRIFIÉ, `registres/go.md` l. 89). Ces 36 tâches sont les rangs 60 à 63 des tâches d'évaluation plus les **32 tâches d'entraînement, c'est-à-dire la réserve** (VÉRIFIÉ, fiche `prereg/T0.5-banque-complete-36-v1.md` de `origin/prep/t05-banque-complete-v1`, l. 12). Le complément `e2` est consigné à `registres/decisions.md` l. 822, la notation des juges (GO-2026-10-28-16 et GO-2026-10-29-04) à `registres/go.md` l. 118 et 127.
- **Total : 64 + 32 = 96 tâches, 288 épisodes. Aucune tâche non courue** (VÉRIFIÉ : la règle de sélection s'arrête à 96 papiers, `docs/procedures/T0.5-selection-papiers-v1.md` l. 85-87).

Sources possibles de tâches neuves :

| Source | Ce qu'elle implique | Cette nuit ? |
|---|---|---|
| Suite du tirage arXiv (1 836 candidats ordonnés, `diag/20261006-134235-t05-corpus/candidats.json`) | Nouvelle version de la règle de sélection et une extraction par sous-agents, avec ses contre-vérifications (la procédure v1 a demandé quatre contre-lectures, `docs/procedures/T0.5-extraction-v1.md` l. 6-9) | **Non** (plusieurs jours) |
| Banque sœur v3-bis (N-049, `docs/decisions/decision-N-049-v1.md` l. 51) | Mondes plantés par générateur. Ce ne sont pas des épisodes réels du 8B, et la construction passe sur devis | Hors sujet |
| **Graines neuves sur les 96 tâches** | Mêmes papiers, textes neufs (température 1,0). Il faut renommer les identifiants de tâche, sinon le constructeur de banque refuse la notation en double (`construire_banque_t05_v3.py`, conv-audit, l. 121) | **Oui** |

Ces épisodes sont-ils « neufs » au sens du juge ? Les textes sont neufs, les tâches ne le sont pas. Les épisodes d'une même tâche sont corrélés, si bien que le gain de puissance réel se compte en tâches et non en épisodes. Un moniteur conçu en lisant les 60 premières tâches reste exposé au sur-ajustement à la tâche (N-049, l. 53-54 : « adapté aux textes » n'est pas « adapté à la famille »). Il faut le dire au préenregistrement et prévoir un rééchantillonnage par tâche (SUPPOSÉ : effet de grappe non mesuré).

## 2. Débit et coût observés

- Génération : 180 épisodes en 7 037,2 s, soit environ 117 s par tâche (VÉRIFIÉ, `diag/20261012-105125-t05-pilote-reel/episodes.json` l. 37). Appariement : 461 s (même dossier, `appariements.json` l. 89467).
- Notations décisives avec la grille H.4, 180 par juge : 8B en 10 478,2 s (≈ 58 s par notation), 3B en 4 944,1 s (≈ 27 s) (VÉRIFIÉ, `diag/20261017-193648-t05-notations-reel/resume.json` l. 15, 25). **Seulement 54 notes complètes sur 180 pour le 8B et 50 pour le 3B** (même fichier, l. 14, 24).
- Une tâche entièrement notée (3 épisodes, 4 notations par juge) prend donc environ 465 s (SUPPOSÉ, calcul). La couche 1 bis (36 tâches) a atteint le plafond de 15 000 s (VÉRIFIÉ, `registres/arrets.md` l. 43). **Au plus 30 tâches par course** sans toucher à la configuration.
- Instances : A100 SXM4 80 Go, de 1,08 à 1,366 USD/h (VÉRIFIÉ, `registres/depenses.md` l. 202, 204, 209, 234). Plafond des lanceurs : 1,40 USD/h (VÉRIFIÉ, `registres/decisions.md` l. 800). Couche 1 bis : 4,56 h, entre 6,2 et 7,2 USD (`depenses.md` l. 208). Complément : 2,77 h, entre 3,3 et 4,3 USD (l. 211).
- Mise en route : environ 19 min de l'instance à la course (VÉRIFIÉ : création 15:19:57, course `20261027-153857`, `arrets.md` l. 43). La fiche prévoyait environ 45 min de mise en place et de tests (`depenses.md` l. 209). Un premier hôte a été perdu au clonage (l. 203), et une seule offre conforme existait le 27 octobre (`decisions.md` l. 800).

## 3. Scénarios (départ 21:30 UTC, configuration du pilote inchangée)

Chaque course compte au plus 30 tâches et tourne sur une instance neuve : l'amorce refuse une seconde course sur la même instance (R12, `arrets.md` l. 47). Pire cas : 1,40 USD/h, plus 1 USD de descente des modèles par instance, le tout × 1,5.

| Scénario | Instances × courses | Tâches (graines neuves) | Épisodes produits et notés | Heures par instance (fin estimée) | Coût au pire cas |
|---|---|---|---|---|---|
| Petit | 1 × 1 | 30 | 90 | ≈ 4,5 h (≈ 02:00) | ≈ 11 USD |
| Moyen | 2 × 1 en parallèle | 60 (les tâches du pilote) | 180 | ≈ 4,5 h (≈ 02:00 ; ≈ 06:30 si une seule offre, deux courses à la suite) | ≈ 22 USD |
| Grand | 2 × 2 à la suite (4 courses de 24 tâches) | 96 | 288 | ≈ 7,5 h (≈ 05:00) | ≈ 37 USD |

Avec le taux de complétude du pilote (≈ 30 %), il faut s'attendre à environ 27, 54 et 86 notes 8B complètes. Ce chiffre est SUPPOSÉ : il reprend le taux du pilote.

Risques :
- pas d'offre conforme, ou un hôte perdu (déjà arrivé deux fois sur huit) ;
- plafond de 15 000 s si les épisodes s'allongent ;
- faible complétude de la grille H.4, et la cellule v2 plus rapide reste « à redéfinir » (H_B, `decisions.md` l. 1016) ;
- pseudo-réplication par tâche ;
- surveillance de nuit (arrêt par identifiant, R10).

À préenregistrer avant la lecture (R1) :
- le rôle du lot : banque élargie, ou épreuve neuve lue une seule fois ;
- l'entropie (R9) ;
- les tâches choisies et leurs nouveaux identifiants ;
- l'unité de rééchantillonnage, qui est la tâche ;
- le critère de promotion des témoins vrais et le seuil ;
- la liste d'arrêt.

**Critères L1 à L4 et seuil 3,0 : introuvables.** `demo_couche1_proposeur_v7.py` (`0a782a5b…`, quatorze copies identiques, dans le bloc-notes et sur `origin/canal/conv-audit-n04`) ne contient ni « L1 » ni « 3,0 ». Il fixe `"seuil": 20.0` (l. 67), et sa l. 6 décrit la banque réelle comme une **v2 de 120 épisodes et 13 moniteurs**, pas 180. Conv-audit doit fournir ces critères avant le scellement.

## 4. Conditions et alternative

1. Mot direct de Lazar dans session-depot et ligne GO (R-994). Recommandation : le **moyen**, avec un plafond de 25 USD.
2. Fiche dérivée de `T0.5-banque-complete-36-v1`. Les tâches sont renommées par un script de dérivation empreinté, avec une entropie nouvelle. La fiche est scellée, contre-lue (R2) et essayée en jouet avant 21:30, soit 1 h 25 de préparation : c'est tendu.
3. Critères de lecture fournis par conv-audit et scellés avant toute lecture.

Si l'une de ces conditions manque, **l'alternative la moins coûteuse est 0 USD cette nuit** : préparer la fiche et la lecture au calme, puis lancer le moyen le soir du 2 novembre. Il n'y a de vraie puissance neuve qu'avec des tâches neuves, ce qui veut dire une extension de la sélection et de l'extraction, sur devis à part.
