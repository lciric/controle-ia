# Décision — N-013 : revendications précisées après le niveau 2 de l'état de l'art — v1

Date : 2026-10-06 (UTC).

**Décision de Lazar** : « N-013 option a, passe à la suite » (message reçu le 2026-10-06, avant 17:48 UTC, heure de la reprise). Consignée dans `registres/go.md` (GO-2026-10-06-04, type « revendication ») et dans `registres/decisions.md`.

**Portée.**
- Cette note fixe, à compter du GO, la lecture des énoncés ci-dessous du programme v2 (`docs/programme-controle-ia-v2.md`, section 5) et des décisions N-005 et N-006.
- Elle ne modifie pas le texte du programme, document qui fait foi transmis par Lazar. Une nouvelle version, s'il en transmet une, la remplacera sur ces points.
- Les préenregistrements (papier C, G1, puis phases 1 et 2) et les papiers partent de ces formulations. Ils citent les précédents avec leurs pages.
- **Aucune hypothèse n'est retirée.** Toutes restent des tests (R3) ; seules les parties déjà publiées cessent d'être revendiquées.

**Sources.**
- Proposition : `docs/decisions/proposition-N-013-revendications-niveau2-v1.md` (sha256 0d1f3d92…).
- 24 rapports de lecteurs neufs, scellés dans `docs/sources/lecture-pdf-niveau2/`. Ils portent sur 3 497 citations contrôlées par script, sans échec.
- Les rapports sont désignés plus bas par leur suffixe, par exemple `lot2-C1a` pour `rapport-lot2-C1a-juges-biais-v1.md`.

## 1. HC1 — loi de déférence

- **Inchangé, revendiqué** : la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille (décision N-005).
- **Retiré des pièces revendiquées : le verdict lu par la probabilité du jeton.** C'est une technique publiée :
  - Schick et al. 2021, d'après Wataoka et al., p. 4 ; Panickssery et al., 2404.13076, p. 2 (`lot2-C1a`) ;
  - 2411.03336, p. 25 ; 2602.20628, p. 6 (`lot2-A4`) ;
  - 2411.17693 (`lot3-Aa`) ; 2402.14016 (`lot2-C2b`) ;
  - recommandée par 2606.07612, p. 25 (`lot2-A2b`).

  Elle reste l'instrument de mesure de la loi (estimation continue de g et de ĉ, même lecture à toutes les intensités), citée comme méthode.
- **Ajoutés aux sources « citées comme publiées »** :
  - 2510.09462 : sous injection, des moniteurs de contrôle adoptent le score visé (« GPT-4.1 … assigning a score of 0 to all 375 backdoored code samples », p. 5) ; une seule intensité, score écrit (`lot2-A4`) ;
  - 2505.23575 : des moniteurs de contrôle sont trompés par la rhétorique de l'agent ; taux de capture à 1 % de faux positifs, score de 0 à 100 (`lot2-C1b`) ;
  - intensités graduées sur des juges, sans destination ni moniteur de contrôle : 2601.13433, autorité sur quatre niveaux avec logits (`lot2-C2a`) ; Koo et al., fausse majorité (`lot2-C1a`) ; 2402.14016, nombre de mots (`lot2-C2b`).

## 2. HC3 — usurpation

- **Cité comme acquis.** Les ordres en bande déplacent les juges génératifs, y compris un moniteur de contrôle :
  - 2508.19461 : ordres insérés par l'agent dans sa trajectoire, Claude 3.6 Sonnet ; l'échafaudage hiérarchique résiste (`lot3-Ca`) ;
  - 2510.09462 (`lot2-A4`).
- **Énoncé retenu (revendiqué)** :
  1. Sous le protocole « contenu = données », les ordres en bande insérés dans le contenu sont détectés presque sûrement par des juges moniteurs. Ces sources ne le testent pas : 2505.06311 détecte un contenu en forme d'ordre à 96,90 % hors domaine, mais sans juge moniteur ni attaquant adaptatif (`lot2-C3a`).
  2. L'usurpation stylistique de l'instructeur, **sans aucun ordre**, garde un g résiduel positif sur des juges moniteurs, mesuré comme loi continue (comme HC1), et un g nul sur des sondes qui lisent l'**agent auteur**.
- **Précédents partiels du versant stylistique, à citer** :
  - 2603.12277 : à argument constant, ôter le style fait tomber le succès d'attaque de 61 % à 10 % (p. 4) ; sur le modèle attaqué, avec un ordre présent, sans juge ni sonde de l'auteur (`lot2-C3a`) ;
  - SLEIGHT-Bench 2605.16626 : un débridage qui imite le langage de la consigne du moniteur échappe à 5 moniteurs sur 6 (lecture de figure, à trancher sur la transcription ; `lot3-Cd`).
- Originalité revue à environ 0,35, contre 0,55 au programme (mon estimation, non sourcée).

## 3. HC4 — taxe de déplacement

- **Énoncé retenu** : obtenir sur une sonde qui lit l'agent le déplacement que la rhétorique obtient gratuitement sur un juge exige un accès en écriture aux activations ou aux poids : le contexte seul n'y suffit pas.
- Le coût se mesure par axe (accès, requêtes, calcul, taux de succès) et par régime d'accès :
  - **contexte seul** : l'écart « de plusieurs ordres de grandeur » reste la prédiction à tester ;
  - **poids réglables** : il n'est plus revendiqué.
- **À citer** : 2609.36490 (`lot3-Cc`).
  - Contexte seul : la modification est alignée sur la direction surveillée mais trop faible pour évader (p. 1).
  - Avec le droit de régler les poids : réglage de rang 1, une époque, 32 verdicts binaires, 96 % d'évasion de sondes jamais vues (llama-3.1-8b, à 1 % de faux positifs). C'est la borne basse du coût dans ce régime.

## 4. HC5 — contre-mesures

- **Énoncé retenu** :
  - paraphrase de confiance ;
  - quorum hétérogène en type d'accès, **juges génératifs et sondes qui lisent l'agent** ;
  - matrice de transfert des attaques de corruption **entre juges et sondes**.
- **À citer** :
  - 2603.13791 : quorum de trois juges et d'une sonde qui lit un encodeur séparé, jamais l'agent ; ni matrice, ni paraphrase, ni attaque ; chiffres non opposables, au moins dix incohérences internes (`lot3-Cc`) ;
  - 2605.15377 : quorum entre familles de juges, sans sonde (`lot2-B1`) ;
  - 2505.23575 : quorum textuel, actions et chaîne de pensée (`lot2-C1b`) ;
  - 2609.36490 : matrice de transfert entre trois sondes seulement (`lot3-Cc`) ;
  - 2605.09684 : transfert entre moniteurs juges (`lot3-Cd`).

## 5. HC2b — renommée « trahison par les activations »

- Le terme anglais « self-incrimination » n'est plus employé : il désigne déjà, dans 2602.22303, un outil `report_scheming()` appris par réglage fin, sans sonde (`lot3-Be`). Le nom anglais se fixera à la rédaction du papier C.
- **Énoncé inchangé sur le fond** : tenter de manipuler fait monter le score de sonde de l'agent qui manipule. C'est une propriété des sondes, contrôlée contre le style.
- Elle est aussi contrôlée contre le retour de bâton textuel : la consigne de discrétion fait monter la capture de tous les moniteurs textuels (2505.23575, p. 7 ; `lot2-C1b`).
- Contre-indice faible à citer : la signature hors distribution d'une manipulation s'efface par entraînement (2609.36490 ; `lot3-Cc`).

## 6. H6 — marge asymétrique (papier A)

- **Énoncé retenu** : pour l'une au moins des quatre interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête.
- **Le bruit sur les poids n'est pas revendiqué** : 2412.01784 (v3, NeurIPS 2025) montre que la sous-performance volontaire cède avant la compétence honnête, au sens du meilleur de cinq tirages, avec un usage en détection (`lot3-Ac`).
- Risque de collision à surveiller : 2607.13087 annonce l'affaiblissement sélectif de l'attaquant (`lot3-Ac`).

## 7. H5 et H7 (papier B)

- **H5, retenu** : la loi, c'est-à-dire la sécurité qui croît avec le nombre M de moniteurs seulement par la diversité effective. L'instrument (matrice de transfert d'une attaque sur un panel de sondes) est cité : 2609.36490, sur trois sondes (`lot3-Cc`).
- **H7, retenu** : la prédiction de la pente d'adaptation de l'équipe rouge par l'information mutuelle entre l'état de détection et ses observations, et la comparaison des politiques de riposte.
- Le mécanisme est cité : le verdict comme canal de fuite, la dépendance causale de l'attaque aux verdicts, les verdicts bruités testés (2609.36490 ; `lot3-Cc`).

## 8. Ce qui ne change pas

- Énoncés inchangés : la pièce maîtresse de HC1, HC2, HC6, H1, H2 (N-007), L et T (N-003, N-004), Tr, H8, H3, H4′, et la statistique de population du papier B.
- La porte GC (N-005) n'est pas déclenchée.
- Pour HC2, le préenregistrement du papier C ajoute un bras « sonde du lecteur » (sonde sur le modèle qui traite le contenu), pour tester la distinction entre auteur et lecteur. Des sondes lectrices sont déplacées par des attaques de contenu en boîte noire :
  - 2511.00554, p. 3 (`lot2-A2b`) ;
  - 2601.11516, p. 12 (`lot2-A2a`) ;
  - 2509.21344 (`lot3-Cb`).
