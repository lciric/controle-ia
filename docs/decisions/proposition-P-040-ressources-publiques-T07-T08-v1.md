# Proposition P-040 — ressources publiques (épisodes, activations, dictionnaires) ajoutées au programme aux étapes T0.7 et T0.8 — v1

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 11:49. **Mot de Lazar (12:48 heure de Paris)** sur les trois
recommandations de l'inventaire des ressources publiques (`brouillons/canal-reprise-releve-v1/envois/inventaire-ressources-publiques-activations-episodes-v1.md`,
`2a9a2095…`) : « go, ajoute dans le programme à la bonne étape ». Le programme v2 et le brief v2 sont scellés (R12) : cette proposition fixe la
lecture **en attendant une version nouvelle** (CLAUDE.md, « Décisions de Lazar sur les nœuds ») ; elle devient une décision N-0xx sur `main` quand
session-depot la consigne avec le mot de Lazar. Aucune dépense ici : chaque ligne passe par un devis chiffré par session-depot et une ligne de GO.
Tout chiffre de l'inventaire est RAPPORTÉ (pages secondaires), non opposable (R7) ; licences, empreintes et retraits de sûreté à la lecture
avant tout usage. Aucune de ces ressources ne remplace les épisodes de nos organismes (critères 2 à 4 de G0 : même jeu d'épisodes, N-029 § 2).

## Ce qui s'ajoute, et où (brief v2, section 7)

| ajout | étape | ce que ça sert | ce que ça ne change pas | condition |
|---|---|---|---|---|
| **A. Rejouer NARCBench (CORE, STEGO ; HELIOS, arXiv 2604.01151) sur notre Llama-3.1-8B-Instruct**, couches 7, 15, 23, agrégation max ou attention, lecture séquentielle ; **activations 70B publiées comme plancher externe** | **T0.7** (l. 166, « Batterie de sondes v0 »), **bras descriptif** à côté du bras principal | transfert de nos sondes vers une famille publiée ; comparaison chiffre à chiffre avec HELIOS (rappel à 1 % de fausses alertes, aire) ; famille tenue à l'écart supplémentaire pour G1 **rapportée**, hors liste scellée | le bras principal de P-011 (c) ; le critère 3 de G0 (lu sur (i) et (ii) de T0.6) ; la liste des comparateurs de N-056 (8 par mode) — y ajouter la recette d'HELIOS comme comparateur boîte blanche serait une modification de revendication : **nœud à part** | devis (≈ 10 à 30 heures-carte, SUPPOSÉ) ; licence de NARCBench vérifiée ; textes servis par la chaîne du corpus (retraits de sûreté) |
| **B. Encoder en lecture seule Liars' Bench et SHADE-Arena dans le 8B** → **banque de traits** et **comparateur boîte noire** (verdicts de moniteurs fournis) | **T0.8** (l. 175, « Bases boîte noire v0 ») pour le comparateur ; **T0.7** pour la banque de traits | prédicteur sur les traits du texte (N-029) entraîné hors politique ; base boîte noire de référence externe, rapportée | N-029 (contenu de la base : juge par action, prédicteur sur traits, TRACE-lite) ; le critère 4 (tourne sur les épisodes de T0.6) | devis (≈ 5 à 20 heures-carte, SUPPOSÉ) ; licence (SHADE-Arena : CC BY-NC, usage de recherche) ; barrière d'accès de Liars' Bench ; aucune donnée de ces bancs dans un préenregistrement sans PDF empreinté |
| **C. Llama Scope (OpenMOSS, Apache-2.0, 8B base, 32 K traits) aux couches 7, 15, 23 sur les épisodes de T0.6**, Goodfire couche 19 (Instruct) en contrôle, après mesure du décalage base / Instruct | **T0.7**, bras descriptif « banque de traits et témoin panel de concepts sans lien » | traits interprétables à côté des sondes ; témoin négatif (concepts sans lien) pour l'artefact de source ; matériau pour l'axe 1 de la course 2 | N-026 : un bras descriptif ne fait franchir aucune porte ; aucune sonde de traits dans le bras principal sans préenregistrement | devis (quelques heures-carte, SUPPOSÉ) ; décalage base / Instruct mesuré et consigné avant toute lecture |

## Ordre et dépendances

A, B et C viennent **après** l'existence des épisodes de T0.6 (critère 2) pour tout ce qui les lit ; A peut commencer avant (il rejoue des épisodes
publiés), sur devis ; B dépend de l'accès aux bancs ; C dépend de T0.6. Aucun ne touche la porte G0 ni ses critères (N-027). Chaque ligne a
son préenregistrement court (hypothèse, prédiction chiffrée, métrique, seuil, lecture gelée) avant lecture ; lecture par sous-agent neuf.

## Décision demandée à Lazar (déjà donnée en mot : « go »)

Consigner P-040 comme décision sur `main` (session-depot), avec les trois conditions : devis avant GO pour chaque ligne ; licences et empreintes
vérifiées ; rien de ces ressources dans la liste scellée des comparateurs de G1 sans nœud à part.
