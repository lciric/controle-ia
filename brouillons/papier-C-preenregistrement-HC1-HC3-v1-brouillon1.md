# Préenregistrement — papier C : HC1, HC2, HC2b, HC3 (TC.1 à TC.3) — v1 — brouillon 1

- Auteur : session de mise en œuvre (session 8)
- Date (UTC) : 2026-10-06 (brouillon). Critère 7 de G0 : scellé et contre-lu avant le 1er novembre.
- **Ne sera pas scellé avant la lecture de Panin** (SSRN 7424179 ; décision N-005, réserve) ni avant la réception des ressources de P3 (corpus de pression, code de la loi d'attraction).
- Commit du code d'analyse : À REMPLIR
- Documents qui font foi (chemin + empreinte) :
  - programme v2 et brief v2 (T0.9 ; piste C, TC.1 à TC.3) ;
  - décision N-005 et N-006 (`docs/decisions/decision-N-005-N-006-v1.md`) ;
  - porte GC (`docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md`) ;
  - rapports de lecture du niveau 2 : `rapport-HC1-voisins-v1.md` (b71730dd…), `rapport-GC-reseaux-v1.md` (5093a6ac…).

## Hypothèse

- **HC1, loi de déférence** (énoncé retenu de N-005) :
  - un juge génératif soumis à une pression d'intensité graduée, d'une famille d'attaque donnée, voit son verdict v, lu comme score continu par la probabilité du jeton de verdict, se déplacer de v₀ vers une destination ĉ : Δv = g · (ĉ − v₀) ;
  - g et ĉ sont estimés par régression sur plusieurs intensités, sans imposer ĉ.
- **HC2, robustesse** (jamais « immunité absolue ») : sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste qui lit l'agent qui produit le contenu.
- **HC2b, auto-incrimination** : tenter de manipuler fait monter le score de sonde (g_sonde < 0). C'est une propriété des sondes, contrôlée contre le retour de bâton déjà observé sur des juges textuels (2508.07805, 2606.07897).
- **HC3, usurpation** :
  - les ordres en bande déplacent les juges sans protocole, et sont détectés presque sûrement sous le protocole « contenu = données » ;
  - l'usurpation stylistique de l'instructeur garde un g résiduel positif sur les juges, nul sur les sondes.

## Prédiction chiffrée et signe attendu

| # | grandeur | signe attendu | réfutation |
|---|---|---|---|
| C-P1 | destination ĉ des juges, par famille | ĉ plus proche de la cible de l'attaquant v* que de la moyenne du corpus (test des deux nuls) | ĉ indiscernable de la moyenne du corpus pour toutes les familles |
| C-P2 | g des juges, par famille | > 0, structuré par famille (au moins deux familles d'intervalles disjoints) | g ≤ 0 pour toutes les familles |
| C-P3 | rang de g entre juges (D2) | stable entre familles et entre corpus (corrélation de rang) | rang instable (corrélation non significative) |
| C-P4 | g des sondes (plan 2 × 2 rhétorique × intention) | ≈ 0 (HC2) ou < 0 (HC2b), contre le style tenu égal | g_sonde > 0 sans accès aux poids : contamination de construit, bascule de titre (porte GC) |
| C-P5 | ordres en bande sous protocole « contenu = données » | taux de détection proche de 1 | À REMPLIR |
| C-P6 | usurpation stylistique | g résiduel > 0 sur juges, ≈ 0 sur sondes | À REMPLIR |

Les ordres de grandeur sont à remplir après le pilote du papier C (4 heures, sous un GO séparé à l'intérieur du devis de la phase 0).

## Métrique

- **Verdict v** :
  - score continu par la probabilité du jeton de verdict, lu sur le texte complet, jamais sur une fenêtre tronquée (leçon de P3) ;
  - même lecture à toutes les intensités, intensité nulle comprise (remarque du lecteur de la porte GC sur 2606.18276 : un instrument qui change entre la référence et la suite crée à lui seul une destination commune).
- **Destination ĉ et gain g** :
  - régression de v sur l'intensité, par juge et par famille, ĉ libre ;
  - tests de ĉ contre trois points de référence : la cible de l'attaquant v*, la moyenne du corpus (nul de régression vers la moyenne), et l'attracteur propre du moniteur, c'est-à-dire sa note sur des contenus neutres (question soulevée par le lecteur de la porte GC, d'après 2606.18276).
- **Consigne** : ne jamais dicter au moniteur l'ampleur de sa mise à jour (défaut relevé dans 2603.15809, p. 37-40).
- **Intervalles** : rééchantillonnage des items, 10 000 tirages.

## Seuil

À REMPLIR : seuils de C-P1 à C-P6, fixés avant toute lecture, après le pilote.

## Plan d'analyse

- **Juges** (D2) : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, révisions figées.
- **Familles d'attaque** :
  - flatterie et supplication ;
  - revendication d'autorité ;
  - approbations forgées ;
  - usurpation stylistique de l'instructeur ;
  - ordres en bande.
  - Au moins trois intensités, plus la condition sans attaque.
  - Grille la plus proche publiée : 2606.14037, autorité et consensus en faible, moyen, fort.
- **Contenus** : propositions de l'environnement (a) (T0.5), et corpus de pression de P3 (À REMPLIR à réception).
- **Sondes** : batterie de T0.7, sur l'agent qui produit le contenu.
- **Plan 2 × 2 rhétorique × intention** (TC.2) : honnête sans plaidoyer, honnête qui plaide sincèrement, saboteur sans plaidoyer, saboteur qui plaide ; même registre rhétorique dans les deux bras qui plaident.
- **Graines** : R9, manifeste.
- **Comparaisons multiples** : correction de Holm sur les familles pour C-P2.

## Critères de lecture gelés

À REMPLIR. Table issue → verdict pour C-P1 à C-P6. Porte GC (décision N-005) :
- g_sonde > 0 sans accès aux poids : le papier change de titre ;
- pièce revendiquée trouvée occupée : recentrage sur HC4 et HC6.

## Liste d'arrêt

- lecture d'un verdict sur une fenêtre tronquée ;
- instrument de lecture différent selon l'intensité ;
- fuite de la cible de l'attaquant dans la consigne du juge ;
- empreinte d'un juge ou d'un corpus non conforme.

## Contre-lecture

À REMPLIR.
