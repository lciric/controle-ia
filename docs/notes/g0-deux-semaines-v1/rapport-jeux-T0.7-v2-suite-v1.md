# Rapport additif — jeux synthétiques de T0.7 : suite du travail de la fille 8 (fille 12, Sonnet 5.5) — v1

Écrit le 2026-11-06 (relevé `date -u` : 12:4x UTC) ; branche `prep/fille-12-t07-v1`, dépôt `lciric/controle-ia-travail`. Aucune clé, aucune location, aucune dépense, rien sous `donnees/` ni `diag/`, aucune lecture de `runs/`. Les mesures viennent du script `scripts/verifier_jeux_synthetiques_t07_v2.py` (inchangé) avec le **tokeniseur factice** de la fille 8 (`cfc0c143…`, non opposable) et une réserve de travail bâtie sur la projection : **jeux non scellables**. Non scellé, non contre-lu (R2 à faire).

## 1. État exact (arrêt demandé par la mère à 12:40 UTC)

| tâches | contenu | état |
|---|---|---|
| r00–r07 | J-D, J-A (mode « contrôles » v2 par la fille 8, « direction ») | inchangées |
| r08–r17 | mode « contrôles » réécrit sous la consigne v2 (cette session) ; J-D et « direction » de la fille 8 gardés | **finies** (`taches/`) |
| r18–r29 | J-D (10) + J-A (20) écrits en entier | **finies** (`remises-completes/`) |
| r30–r31 | — | **perdues / non écrites** (un écrivain lancé puis arrêté avant tout fichier) |
| J-C « domaine, mode coût » | hors ordre | **aucune tâche écrite** (r00–r31) |

Fichiers : `brouillons/t07-jeux-synthetiques-v2-suite-fille12/` — `taches/` (r08–r17 fusionnés : D et `direction` repris tels quels de `…-brouillon1/taches/`), `remises-controles/` (10 enregistrements par tâche, r08–r17), `remises-completes/` (30 enregistrements par tâche, r18–r29), `entrees/`, `outils/` (pré-contrôle `verif_lot_v1.py`, `fusion_v1.py`, `aires_par_tache_v1.py`), `mesures/`, `consigne-ecrivain-fille12-v1.md`. Rien d'existant modifié (R12) ; les anciennes paires « contrôles » de r08–r17 restent telles quelles dans `…-brouillon1/taches/`. Aucun `.sha256` posé (la mère scelle).

## 2. Aires du contrôle 10 (sac de mots, une tâche laissée de côté ; seuil de réserve 0,90)

| ensemble | contrôles, entière | contrôles, avant COST | direction, entière | direction, avant COST | défauts durs de fréquence |
|---|---|---|---|---|---|
| **avant** r00–r13 (consigne v2 de la fille 8) | 1,000 | 0,994 | 0,703 | 0,749 | 20 |
| **avant** r08–r17 seules, anciennes paires | 0,996 | 0,976 | 0,728 | 0,708 | 11 |
| **avant** r00–r17, r00–r07 déjà réécrites | 0,898 | 0,880 | 0,702 | 0,758 | — |
| après, r00–r07 | 0,745 | 0,805 | 0,660 | 0,600 | 0 |
| après, r00–r11 | 0,757 | 0,747 | 0,700 | 0,740 | 0 |
| après, r00–r17 | 0,769 | 0,771 | 0,702 | 0,758 | 0 |
| après, r00–r21 | 0,789 | 0,802 | 0,716 | 0,773 | 0 |
| après, r00–r25 | 0,789 | 0,772 | 0,698 | 0,737 | 0 |
| **après, préfixe complet r00–r29 (30 tâches)** | **0,813** | **0,807** | **0,705** | **0,733** | **0** |

Aucune des quatre aires du préfixe complet n'atteint 0,90 ; contrôle 10 : « OK » à chaque étape, défauts durs = 0 dans les deux modes (réponse entière et avant COST). Valeurs par pli (une tâche laissée de côté) : `mesures/aires-par-pli-r00-r29-v1.json` ; **le journal ne donne que la moyenne, les valeurs par tâche sont celles de ce fichier, bruitées (20 documents par pli)**. Plis ≥ 0,90 : contrôles, 12 plis sur 30 (entière) et 10 sur 30 (avant COST) ; direction, 5 et 4. Journaux : `mesures/journal-verification-r00-r29-v1.txt` (préfixe), `journal-avant-*.txt`.

## 3. Défauts restants du script (préfixe r00–r29)

- **Seuls défauts : 15 écarts en jetons** (> 15 % entre les deux membres, contrôle 6), tous mesurés avec le tokeniseur factice : **non opposables**, à rejouer avec le `tokenizer.json` conforme (`79e3e522…`, introuvable ici). 7 défauts portent sur des paires de r00–r17 (fille 8, r12, r16), 8 sur 5 paires de r18–r29 (r24 p4 ; r25 p2 et p9 ; r26 p7 ; r29 p7).
- Corrections faites : un renvoi unique pour r08 p3, r10 p3, r11 p4–p5 ; r12 (formes « 200k », trois paires) ; r13 p1 (8 mots) ; r19 p1 (ordinal « 500th », corrigé par moi dans le fichier) ; r14 et r15 : champ `tache` normalisé (préfixe `rNN-` retiré, 20 enregistrements). Aucune tâche n'a eu de troisième boucle.
- Contrôle 9 : textes d'actions de P3 et épisodes de T0.6 absents → à rejouer par la chaîne de T0.7.

## 4. Indices de surface déclarés par les écrivains

Contrôles : cibles faibles nommées avec un vocabulaire d'ingénierie (optimiseur, échauffement, vitesse, perte d'entraînement, norme de gradient) quand le côté honnête parle de jeux tenus à l'écart ; paires 1 et 5 où le membre honnête porte des noms de modèles de référence absents du membre faible (r12, r13) ; reformulations du membre faible à la même place (« Assemble » pour « Build ») signalées à r24–r25 ; clôtures stéréotypées (« claim fails if », « Repeat over 3 seeds ») communes aux deux membres. Direction : membre faible souvent plus « ingénierie » (latence, mémoire, distillation, calibration, étalonnage) ; paire 8 de r18 et r19 où le membre faible est le leurre que l'énoncé écarte ; membre faible plus court dans plusieurs paires ; r28 p3 et p7 mots « continue », « fine-tune », « short ». Mesure : longueurs moyennes par étiquette (J-A) : 166,5 contre 165,1 mots ; avant COST : 851 contre 843 caractères ; groupes de chiffres 3,03 contre 3,00. Paires jugées incertaines par leurs écrivains : r10 p3, r11 p5, r17 p5, r18 p3 et p8, r19 p3, r20 p7, r21 p4–p5 et p8–p10, r24 p7–p8, r25 p5–p6, r26 p8 et p10, r27 p7–p8, r28 p9, r29 p7.

## 5. Trois risques

1. **L'aire monte avec les tâches ajoutées** (0,745 à 8 tâches, 0,769 à 18, 0,813 à 30) et la moitié des plis dépasse déjà 0,90 pour le mode « contrôles » : la moyenne sur 32 peut franchir 0,90 ; les deux dernières tâches (r30–r31) et le tokeniseur conforme restent à passer. Le seuil de 0,90 n'est pas un état stable.
2. **Les indices lexicaux sont déplacés, pas supprimés** : les écrivains neufs ont chacun leurs habitudes (vocabulaire d'ingénierie du côté faible, leurre rejeté par l'énoncé), et le contrôle de fréquence documentaire ne voit que les termes courants au niveau du jeu. La contre-vérification à l'aveugle (section 9 de la consigne v3) n'est pas faite ; elle reste la seule lecture du fond.
3. **Pas de J-C, pas de r30–r31, pas de tokeniseur conforme** : le jeu de coût (640 séquences) n'existe pas, le préfixe de 30 tâches n'est pas le jeu de 32, et la règle des jetons est jouée avec un tokeniseur factice. Aucun de ces trois points n'est scellable en l'état.

## 6. Ce qu'il faut faire ensuite (pour la session suivante, depuis la branche `prep/fille-12-t07-v1`)

1. r30 (`2509.21302v4`) et r31 (`2604.05112v1`) : lots complets avec `consigne-ecrivain-fille12-v1.md` et `entrees/` (fichiers prêts), puis `outils/verif_lot_v1.py complet`, `fusion` inutile (remises complètes).
2. J-C : écrire d'après la consigne v3 (section 11 et annexes), 10 paires par tâche, 32 tâches ; `incitation_id` par rotation (annexe B).
3. Rejouer le script avec le tokeniseur conforme et la réserve scellée, sur les 32 tâches ; contre-vérification à l'aveugle ; scellement.
