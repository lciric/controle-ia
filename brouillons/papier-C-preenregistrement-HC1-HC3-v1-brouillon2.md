# Préenregistrement — papier C : HC1, HC2, HC2b, HC3 (TC.1 à TC.3) — v1 — brouillon 2

- Auteur : session de mise en œuvre (session 9)
- Date (UTC) : 2026-10-06 (brouillon). Critère 7 de G0 : scellé et contre-lu avant le 1er novembre.
- Brouillon 1 : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon1.md`, gardé tel quel. Ce brouillon 2 applique la décision N-013 (GO-2026-10-06-04, `docs/decisions/decision-N-013-v1.md`) :
  - la lecture par probabilité du jeton devient un instrument cité, plus une revendication ;
  - HC2b est renommée « trahison par les activations » ;
  - HC3 est limitée à ses deux composantes encore libres ;
  - un bras « sonde du lecteur » est ajouté pour HC2.
- **Ne sera pas scellé avant la lecture de Panin** (SSRN 7424179 ; décision N-005, réserve) ni avant la réception des ressources de P3 (corpus de pression, code de la loi d'attraction).
- Commit du code d'analyse : À REMPLIR
- Documents qui font foi (chemin + empreinte) :
  - programme v2 et brief v2 (T0.9 ; piste C, TC.1 à TC.3) ;
  - décisions N-005 et N-006 (`docs/decisions/decision-N-005-N-006-v1.md`) et N-013 (`docs/decisions/decision-N-013-v1.md`, 157d388e…) ;
  - porte GC (`docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md`) ;
  - rapports de lecture du niveau 2 (`docs/sources/lecture-pdf-niveau2/`) : `rapport-HC1-voisins-v1.md` (b71730dd…), `rapport-GC-reseaux-v1.md` (5093a6ac…), lot 2 C1a, C1b, C2a, C2b, C3a, C3b, A2a, A2b, A4, lot 3 Ca, Cb, Cc, Cd, Be.

## Hypothèse

- **HC1, loi de déférence** (énoncé retenu de N-005, précisé par N-013) :
  - un moniteur génératif de contrôle, soumis à une pression d'intensité graduée d'une famille d'attaque donnée, voit son verdict v se déplacer de v₀ vers une destination ĉ : Δv = g · (ĉ − v₀) ;
  - g et ĉ sont estimés par régression sur plusieurs intensités, par famille, **sans imposer ĉ** ; ĉ est testé contre la cible de l'attaquant v* et contre la moyenne du corpus.
  - **Instrument cité, non revendiqué** : v est lu comme score continu par la probabilité des jetons de verdict (Schick et al. 2021, d'après Wataoka et al. p. 4 ; Panickssery et al. 2404.13076 p. 2 ; 2411.03336 p. 25 ; 2602.20628 p. 6).
  - **Précédents cités** :
    - un moniteur de contrôle adopte le score injecté, à une intensité, en score écrit (2510.09462, p. 5) ;
    - des moniteurs de contrôle sont trompés par la rhétorique de l'agent (2505.23575) ;
    - des intensités sont graduées sur des juges, sans destination ni moniteur de contrôle (2601.13433 ; Koo et al. ; 2402.14016) ;
    - poids du conseil (psychologie du jugement) ; 2606.07897 ; 2508.07805 ; 2607.08066 (décision N-005).
- **HC2, robustesse** (jamais « immunité absolue ») : sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste qui lit **l'agent qui produit le contenu**. Contre-indices connus, tous sur des sondes qui lisent le modèle qui **traite** le contenu : 2511.00554 (p. 3), 2601.11516 (p. 12), 2509.21344. D'où le bras « sonde du lecteur ».
- **HC2b, trahison par les activations** : tenter de manipuler fait monter le score de sonde de l'agent qui manipule (g_sonde < 0). C'est une propriété des sondes, contrôlée contre le style. Elle est aussi contrôlée contre le retour de bâton déjà observé sur des juges textuels : 2508.07805, 2606.07897, et la consigne de discrétion qui fait monter la capture des moniteurs textuels (2505.23575, p. 7). Le terme « self-incrimination » n'est pas employé (2602.22303).
- **HC3, usurpation** (N-013) :
  - **cité comme acquis**, mesuré seulement comme contrôle de manipulation : les ordres en bande déplacent les juges génératifs, y compris un moniteur de contrôle (2508.19461 ; 2510.09462) ;
  - **revendiqué, composante 1** : sous le protocole « contenu = données », les ordres en bande insérés dans le contenu sont détectés presque sûrement par des juges moniteurs ;
  - **revendiqué, composante 2** : l'usurpation stylistique de l'instructeur, sans aucun ordre, garde un g résiduel positif sur des juges moniteurs, mesuré comme loi continue, et un g nul sur des sondes qui lisent l'agent auteur. Précédents partiels : 2603.12277 (p. 4) et 2605.16626.

## Prédiction chiffrée et signe attendu

| # | grandeur | signe attendu | réfutation |
|---|---|---|---|
| C-P1 | destination ĉ des juges, par famille | ĉ plus proche de la cible de l'attaquant v* que de la moyenne du corpus (test des deux nuls) | ĉ indiscernable de la moyenne du corpus pour toutes les familles |
| C-P2 | g des juges, par famille | > 0, structuré par famille (au moins deux familles d'intervalles disjoints) | g ≤ 0 pour toutes les familles |
| C-P3 | rang de g entre juges (D2) | stable entre familles et entre corpus (corrélation de rang) | rang instable (corrélation non significative) |
| C-P4 | g des sondes de l'**agent auteur** (plan 2 × 2 rhétorique × intention) | ≈ 0 (HC2) ou < 0 (HC2b), à style tenu égal | g_sonde > 0 sans accès aux poids : contamination de construit, bascule de titre (porte GC) |
| C-P4b | g d'une sonde **lectrice** (même concept, sur le modèle qui traite le contenu) | > 0 possible (2511.00554 ; 2601.11516) ; prédiction centrale : g_auteur < g_lecteur | g_auteur ≥ g_lecteur avec intervalles disjoints : la distinction auteur / lecteur ne protège pas |
| C-P5 | ordres en bande sous protocole « contenu = données » | taux de détection par les juges moniteurs proche de 1 | À REMPLIR |
| C-P6 | usurpation stylistique sans ordre | g résiduel > 0 sur juges, ≈ 0 sur sondes de l'auteur | À REMPLIR |

Les ordres de grandeur sont à remplir après le pilote du papier C : 4 heures, sous un GO séparé à l'intérieur du devis de la phase 0.

## Métrique

- **Verdict v** :
  - score continu par la probabilité des jetons de verdict, lu sur le texte complet, jamais sur une fenêtre tronquée (leçon de P3) ;
  - même lecture à toutes les intensités, intensité nulle comprise (remarque du lecteur de la porte GC sur 2606.18276 : un instrument qui change entre la référence et la suite crée à lui seul une destination commune) ;
  - lecture par espérance sur les jetons des valeurs après une réponse imposée (`bases.scores_jetons`). Les valeurs 0 à 100 tiennent chacune en un jeton sur les tokeniseurs des juges Llama (R-067) ; à vérifier pour chaque juge de D2.
- **Destination ĉ et gain g** :
  - régression de v sur l'intensité, par juge et par famille, ĉ libre ;
  - tests de ĉ contre trois points de référence : la cible de l'attaquant v*, la moyenne du corpus (nul de régression vers la moyenne), et l'attracteur propre du moniteur, c'est-à-dire sa note sur des contenus neutres (question du lecteur de la porte GC, d'après 2606.18276) ;
  - modérateur rapporté : raisonnement visible ou non avant le verdict. Dans 2608.25869, l'hypothèse « destination = ancre » ne tient plus avec chaîne de pensée (`lot3-Ca`).
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
  - Échafaudage du moniteur rapporté (simple ou hiérarchique) : dans 2508.19461, le moniteur hiérarchique résiste.
- **Contenus** : propositions de l'environnement (a) (T0.5), et corpus de pression de P3 (À REMPLIR à réception).
- **Sondes** :
  - batterie de T0.7 sur l'agent qui produit le contenu (sondes de l'auteur) ;
  - mêmes concepts et mêmes familles sur un modèle qui lit le contenu sans l'avoir produit (sondes lectrices, bras C-P4b) ;
  - plancher apparié en covariance (R-069) pour les deux.
- **Plan 2 × 2 rhétorique × intention** (TC.2) : honnête sans plaidoyer, honnête qui plaide sincèrement, saboteur sans plaidoyer, saboteur qui plaide ; même registre rhétorique dans les deux bras qui plaident.
- **Graines** : R9, manifeste.
- **Comparaisons multiples** : correction de Holm sur les familles pour C-P2.

## Critères de lecture gelés

À REMPLIR. Table issue → verdict pour C-P1 à C-P6. Porte GC (décisions N-005, N-013) :
- g_sonde de l'auteur > 0 sans accès aux poids : le papier change de titre ;
- pièce maîtresse trouvée occupée (Panin en particulier) : recentrage sur HC4 et HC6.

## Liste d'arrêt

- lecture d'un verdict sur une fenêtre tronquée ;
- instrument de lecture différent selon l'intensité ;
- fuite de la cible de l'attaquant dans la consigne du juge ;
- valeur de verdict qui ne tient pas en un jeton pour un juge (garde de `bases.scores_jetons`) ;
- empreinte d'un juge ou d'un corpus non conforme.

## Contre-lecture

À REMPLIR.
