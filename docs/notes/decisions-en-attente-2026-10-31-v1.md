# Décisions en attente — 31 octobre 2026, ≈ 12:30 UTC — v1

Session-depot, sous-agent (fork), pendant l'autonomie R-905. Inventaire de ce qui attend un mot de Lazar ou de conv-audit, vérifié sur `registres/decisions.md` (main, R-780 à R-905), `registres/etat.md`, et sur la branche `canal/conv-audit-n04` (messages n° 270 à 291 ; mémo de conv-audit `decisions-en-attente-lazar-2026-10-31-v1.md`, lu pour l'inventaire seulement). Avec les recommandations des auteurs (retirées des questions servies à Argon sous GO-2026-10-31-08 : `scratchpad/argon-questions-ouvertes-v1/question-argon-{a,b,c}-v1.md`). Rien n'est tranché ici.

**Hors de cet inventaire, traités ailleurs** : nœuds du collisionneur (question v9, puis v10 attendue : N1 bisociation v3, N3 D-j, N4 annexe du bras méta CA1-05 et CA1-04, N5 A21 et choix de code de l'orchestrateur, N6 semi-réel DL-1 à DL-9, N9 D-GK-1, N10 robustesse adaptative) ; protocelles (tours du collisionneur) ; D-ML-1 (collisionneur, conv-audit et Argon, GO-2026-10-31-07 et -08).

## A. Course 2 et pré-pilote

Pièce : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon10.md` (branche de conv-audit, `ea940d56e5ee949e…`). **Aucun défaut** : le préenregistrement ne se gèle pas tant qu'une ligne reste sans mot.

| Décision | Objet | Recommandation de l'auteur (confiance) | Défaut, échéance |
|---|---|---|---|
| S1 | exactitude équilibrée minimale par juge | 0,80 (0,6) ; alternative 0,75 | aucun |
| S2, S3 | rappel minimal ; plancher d'échec | 0,70 ; 0,70 (0,6) | aucun |
| S4 | accord Fleiss ; par couple ; plancher | 0,45 ; 0,35 ; 0,30 (0,5) | aucun |
| S6 | fidélité du rendu | 0,95 ; 1,00 ; 1,00 (0,7) | aucun |
| S7, S8 | mémoire anti-redite : fausses alertes ; rappel | 0,05 ; 0,10 — 0,80 (0,6) | aucun |
| S9 | double garde de l'axe 7 | 0,75 ; 0,15 (0,5) | aucun |
| S10, S11 | aiguilleur : rappel ; fausses alertes | 0,90 et 0,75 ; 0,10 et 0,34 (0,6) | aucun |
| S12 | débordement de Kimi proposeur | 0,10 (0,6) ; alternative 0,05 | aucun |
| S13 à S15 | antériorité : inventées ; altérées ; fausses alertes | 0,90 ; 0,70 ; 0,10 (0,6) | aucun |
| S16 | écart coût mesuré ÷ supposé | ×1,30 (0,6) | aucun |
| S18, S19 | indiscernabilité témoins/Kimi ; P/N par la forme | 0,70 et 6 ; 0,65 (0,5) ; alternatives 0,75 ; 0,70 | aucun |
| S20, S21 | témoins ambigus ; tableau minimal | 4 sur 23, P ≥ 8, N ≥ 10 (0,6) ; 120 et 200 caractères (0,7) | aucun |
| S23 à S25, S27 | k paires ; Jaccard ; m ; couverture Gu-Krenn | k = 1 (0,7) ; 0,40 ; m = 3 ; 0,60 réserve (0,5) | aucun |
| S30 | rappel de M6b (D-g (b) retenue) | 3 sur 4 (0,5) | aucun |
| S31 | substitut inspiré de Gu et Krenn | moisson OpenAlex, ≥ 20 œuvres, « reliées » ≥ 1 œuvre 2015–2026-06-30, « actif » ≥ 5 sur trois ans (0,4) | aucun |
| D-e | lecture de « domaine » et « concept » | (i) vecteur indicateur et liste fermée (0,6) | aucun |
| D-f | modèles des rôles neufs | (i) T = Sonnet 5.5, relecteur = Fable 5.1 (0,6) | aucun |
| L1, L2, L3 | passe « tableau » ; table seule ; désaccord hors score | gardée (0,7) ; gardée (0,6) ; hors score (0,7) | aucun |
| L5, L6, L7 | fusions retirées et C12 ; S27 ; brouillon 3 | lue sur les paires (0,65) ; réserve (0,6) ; accepté (0,6) | aucun |
| Étalonnage de l'aiguilleur | DEP5 ; R-819 | — | **défaut R-819 : pas d'étalonnage (ferme C7), ≈ 1er novembre 10:40 UTC** (R-819 a un défaut, le brouillon 10 dit « aucun défaut » : à lever) |
| Confidentialité | A15 : fiches envoyées à Moonshot (Kimi) et Google (Argon) | — | aucun |

Déjà tranchés (ne pas redemander) : S17 = 50 ; 45 (GO-2026-10-31-03) ; S22 = 24 fusions (GO-2026-10-31-04) ; D-g (b), D-h (a), D-i (2) (R-898) ; D-j au collisionneur ; S5, S26, L4 sans objet.

**Texte III, mesure statistique** (R-859 ; `docs/notes/ideation-organisme-v1/course-2/texte-III-v1/synthese-texte-III-etroite-v2.md`, `a3bd20c4…`, § 9) — défauts **1er novembre ≈ 23:10 UTC** : D1 loi sur la classe : (a) population finie accessible, loi uniforme ; D2 estimateur : (c) point seul et intervalle d'identification, nominal suspendu ; D3 couverture : (c), prédiction extérieure scellée avant mesure ; D4 zone d'indifférence à double seuil : (a) ; D5 minimum observé rapporté, « non pire cas » : (a). Confiances « moyennes ».

**Tableau partagé** (R-862 ; `…/tableau-partage-v1/synthese-tableau-partage-v3.md`, `ae0282fb…`, § 5) — défauts **2 novembre ≈ 00:30 UTC** sauf D3 : D1 minimal par défaut jusqu'au pré-pilote : (b) ; D2 ordre du pré-pilote : (b) ; **D3 bras comparatif du pré-pilote : (a), confiance faible, dépense, aucun défaut** ; D4 unité d'« élément de code » : (a) ; D5 qualité jugée et lecture procédurale : (b) ; D6 lecture des critères 8 et 1 : (a). Réserve R4 de R-862 (vérification non convergente).

**Machine jetable** (R-868 ; `docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v3.md`, `864f3d27…`, § 5) — nœud (compte, machine, dépense), **aucun défaut** : GO proposé 10 USD (≈ 0,5 attendus, 7,4 au pire) ; recommandation (A) avec le remède (R-a) pour AppArmor, confiance 0,6. Nécessaire au rejeu de l'orchestrateur v55 avant le pré-pilote. Réserve de R-868 : délai dépassé lu « fermée » en G8, à corriger avant usage.

## B. Porte G0

Pièce : `prereg/brouillon-G0-grille-lecture-v7.md` (`911d79e6…`), annexe B ; contre-lecture CL6 (branche de conv-audit, `7092fe4e…`) : **v8 nécessaire** (1 bloquant, 7 majeurs), confiée à session-depot, non scellée à ce relevé. **R-518 : aucun défaut à 48 heures** pour ce qui touche G0 ; **D-G0-1 exige un mot explicite** ; s'il est accepté, D-G0-2 à 15 non tranchés au 2026-11-15 prennent le défaut de la grille.

| Décision | Défaut de la grille (si D-G0-1 accepté) |
|---|---|
| D-G0-1 | aucun : mot explicite (première lecture ≤ 30 novembre ; grille scellée ≤ 15 novembre) |
| D-G0-2 | critère 2 délégué au préenregistrement de T0.6 sous (a)-(d) |
| D-G0-3 | « tourne » = sans arrêt de garde + part de scores finis fixée par T0.8 |
| D-G0-4 | critères 6 et 7 : réserve |
| D-G0-5 | critère 1 hors domaine : réserve + exigence amont |
| D-G0-6 | lecteur d'un autre modèle, même famille ; autre lignée |
| D-G0-7 | version suivante recevable seulement autorisée avant son run avec cause nommée ; jamais après un négatif gelant par liste d'arrêt |
| D-G0-8 | verdict scellé par sous-agent neuf pour 2, 3, 4 (rapport de fonctionnement suffisant pour 4) |
| D-G0-9 | critère 8 : périmètre (A), (B) en réserve |
| D-G0-10 | critère 5 : option Fable |
| D-G0-11 | critère 3 : condition |
| D-G0-12 | critère 4, TRACE-lite absent : réserve |
| D-G0-13 | raccord de R-765 lu sur le négatif gelant |
| D-G0-14 | (a) à (e) : gel preuve par preuve ; (d) non gelant tant que l'audit n'est pas scellé (0,4) ; (e) gelant s'il est scellé après la grille (0,5) |
| D-G0-15 | reprise : la même lecture, même `C_lecture` (0,6) ; **CL6-04 : défaut sans borne, se contredit** |
| DIV-1 à DIV-3 | portée du gel ; D-G0-8 ; « cesser » (porté en D-G0-15) — grille contre table v4 et mémo de conv-audit ; CL6-05 : comparer à la table v7, DIV-5 manquant |

CL6-01 (bloquant) : l'échéance du 31 janvier doit borner le verdict final, non l'ouverture de la lecture. Avis de CL6 sur D-G0-1 à 15 : dans la contre-lecture (section « Pour Lazar »), non repris ici.

## C. Bisociation, arène P-041 et le reste

**Question 6** (R-884 ; `docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-6-v1/synthese-question-6-v2.md`, `ff3b19e3…`) — défauts **2 novembre, matin** : D1 corriger la réponse de conv-audit en v2 à deux niveaux (latentes / flèche vers Y) ; D2 préenregistrer l'Expérience 0 et le banc, générateur sur processeur, carte graphique sur devis ; D3 exigences des courses de l'étape 2 ; **D4 relancer Kimi sur III.2 et III.3 : (a), confiance moyenne, dépense, aucun défaut** (la reprise de jour du 31 octobre a échoué, R-877).

**Question 7** (R-884 ; `…/collisionneur-question-7-v1/synthese-question-7-v2.md`, `0ced3b28…`) — défauts **2 novembre, matin** : D7-1 critères étagés : (i), moyenne ; D7-2 test de nécessité du catalyseur en porte séparée : (i), élevée sur le principe ; défaut : rédiger le préenregistrement ; D7-3 journalisation de génération 1 : (i), élevée ; D7-4 duel de dose reporté à la question 3 : (i), moyenne ; **D7-5 dépense pour la porte G0 (15 à 35 USD illustratifs) : nœud, aucun défaut**.

**Arène P-041, tour 1** (R-882 ; `docs/notes/anteriorite-P-041-v1/collisionneur-organisme-coevolutif-v1/synthese-organisme-coevolutif-v1.md`, `1f6de90b…`, § 6) — défauts **2 novembre, matin** : D3 générateur en régime informé : (a) fait 9 tel quel ; D5 calcul du budget fixé par le préenregistrement : (a), haute. D1 (contre-lecture) et D2 (tour 2) exécutés (R-885) ; D4 dépassée par R-880.

**Arène P-041, tour 2** (`…/synthese-organisme-coevolutif-tour2-v1.md`, `8a612a8f…`, § 3 et « À trancher par Lazar ») : nombre de réplications K ; estimand du débordement ; ce que reçoit le générateur informé (proposition : fait 9 tel quel, scores à part) ; budget de calcul et seuils numériques ; pilote ou non. Aucun défaut écrit ; nécessaires au préenregistrement de l'arène, dont dépend l'examen final (`prereg/P-041-examen-final-v2.md`, liste d'arrêt).

**Malléabilité** (`prereg/P-041-malleabilite-v3.md`, `49f94354…`) : **M_plafond** (nœud soumis à Lazar, aucune valeur proposée) ; sous-ensemble des couches (« à fixer » : multiples de 4 ou de 8) ; D-ML-1 traité ailleurs.

**G1-2, recette d'HELIOS** (R-796 (1)) : neuvième comparateur boîte blanche, décision conditionnelle au chiffrage par la garde δ v8 (k = 9) et à la confirmation de Lazar sur les chiffres : en attente du chiffrage.

## Tranchés ou sans objet (vérifiés)

R-793 axe 6 → (b), R-803 ; R-867 → « go recos », R-878 ; R-871 Kimi → R-877 ; R-886 → R-888, R-891 ; devis v6 D1 à D3 → GO-2026-10-31-03 et -04 ; S17, S22, D-g, D-h, D-i ; ultracode (R-900).

## État incertain

- **Étalonnage de l'aiguilleur** : R-819 lui donne un défaut à 48 heures (≈ 1er novembre 10:40 UTC), le brouillon 10 dit « aucun défaut » pour ses décisions.
- **G1-2 (HELIOS)** : rien ne dit sur main si le chiffrage par la garde δ v8 a été fait.
- **R-882 D4** : dépassée de fait par R-880 (examen final et voies décidés par Lazar), sans mot explicite sur la décision elle-même.
- **Q6 D4** : proposée après l'échec de la reprise de jour (R-877) ; ouverte comme dépense.
