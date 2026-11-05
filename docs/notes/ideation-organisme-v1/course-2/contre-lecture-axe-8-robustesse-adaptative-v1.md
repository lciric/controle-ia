# Contre-lecture (R2) — axe 8 « robustesse adaptative », texte à insérer dans le texte I de la course 2 — v1

Contre-lecteur neuf : sous-agent Claude Fable 5.1 (autre modèle que le rédacteur, Opus 5.5), 1er novembre 2026, ≈ 19:30 UTC. Aucune pièce lue n'a été écrite par ce contre-lecteur ; aucun appel réseau ni de modèle ; aucun fichier existant modifié.

**Pièce contre-lue** : `axe-8-robustesse-adaptative-texte-v1.md` (dossier `recoupement-v1/` du brouillon conv-audit, non scellé).
**Contexte lu** : `analyse-approfondie-axe-8-robustesse-v2.md` ; `question-course-2-axe-8-robustesse-adaptative-v1.md` (en-tête tronqué, R-742) ; `question-course-2-defense-fusion-v5.md` et `recoupement-question-course-2-defense-v2.md`, **absents du dossier donné**, extraits de `origin/canal/conv-audit-n04` (empreintes `a7501449…`, identique à celle citée par le rédacteur, et `b4b1ab88…`) ; synthèses du collisionneur, sections N10, sur leurs **v2** du dépôt (`d313b482…`, `f4f2d197…`) ; `registres/decisions.md` de la branche conv-audit ; `docs/sources/pdf/2412.09565v2.pdf`, pages 3, 23, 25, 26 ; `corpus-primaire-v5-integral/LISEZMOI-v2.md`, ligne 27.

## 1. Verdict

**Insérable après corrections** : un bloquant (la dernière ligne du bloc exclut, à la lettre, toute fiche de l'axe), quatre majeurs, sept mineurs. Le fond (accord à quatre du collisionneur) est fidèlement transcrit ; les pages de Bailey sont justes. Plafond non tenable par coupes : sous-session séparée recommandée (§ 3).

## 2. Points numérotés

### Bloquant

**CLA8-01** — « Une fiche qui décrit un contournement ou exige une entrée adverse est écartée avant la notation et comptée (règle « niveau méthode »). » Le même bloc exige « l'attaquant vise la défense composite entière » et un « taux d'évasion par budget » : toute fiche d'axe 8 *exige* des entrées adverses (celles de l'adversaire synthétique) pour que le taux existe. L'analyseur de l'étage 1, « qui décide », écarterait l'axe entier. Correction : « Une fiche qui décrit un contournement, l'objectif d'un optimiseur d'attaque ou un procédé qui produit une entrée adverse est écartée avant la notation et comptée (règle du préambule) ; les entrées adverses sont fournies par le programme, jamais par la fiche. » Même remède pour « un optimiseur local » en (e) : c'est celui du programme.

### Majeurs

**CLA8-02** — « (c) mesure : front performance de la tâche × taux d'évasion par budget ». K3 exige une « prédiction chiffrée et signée sur M » ; la liste M (annexe 1) ne contient ni performance de la tâche, ni taux d'évasion, ni pente du front : aucune fiche d'axe 8 ne passe K3. Correction : ajouter à M « performance de la tâche sous attaque ; taux d'évasion au rappel à 1 % par budget ; pente du front », ou écrire en (c) « taux d'évasion = 1 − rappel à 1 % ». L'entrée d'annexe proposée en § 1.3 n'en dit rien.

**CLA8-03** — « adversaire synthétique, hors de la course (texte II) ». Le texte I v5 ne nomme jamais le texte II, absent de « Pièces (liste fermée) » ; le proposeur ne sait pas ce que c'est, et la mention révèle une pièce de structure qu'on lui cache. Correction : « adversaire synthétique tenu par le programme, hors de la course ; la fiche ne le voit pas ».

**CLA8-04** — « constantes d'échelle (plancher d'utilité) calibrées sur les seuls honnêtes du pilote, puis gelées ». Le proposeur n'a le pilote qu'en « verdict seulement » : il ne peut rien calibrer. La réserve 2 du rédacteur le dit ; le texte servi non. Correction : « nommées par la fiche, calibrées par le programme sur les honnêtes du pilote après scellement de la fiche, gelées avant tout comparatif ».

**CLA8-05** — « Quelle défense (statistique des axes 1, 4 ou 5, seule ou composée) » et phrase de boucle « nomme la statistique (axe 1, 4 ou 5) dont elle mesure la tenue ». Les fiches d'une génération sont anonymes et parallèles : une fiche d'axe 8 ne peut nommer qu'une statistique de son propre auteur ; l'axe 4 rend un préenregistrement, pas une statistique. Correction : « une défense décrite au point de codage (comme à l'axe 1 (b)) ou une fiche d'axe 1 ou 5 de la génération précédente ; en première génération, « à établir en g+1 » » ; et dire que le programme accepte **deux** noms (statistique et faille), sinon « vérifie présence et appartenance » ne sait pas lire ce vis-à-vis.

### Mineurs

**CLA8-06** — « sous-espaces nécessaires à la tâche » ; la source (tour 1, critère 18, apport seul de C) dit « nécessaires à la réussite de l'attaque ». Si le changement est voulu (cadrage défensif, plus sûr), le déclarer en § 2 comme écart.

**CLA8-07** — « (a) … boîte blanche, nombre de couches lues » (accès de l'attaquant) et « (b) … couches lues » (levier du défenseur) : même expression, deux objets. En (a) : « nombre de couches auxquelles il a accès ».

**CLA8-08** — « prédiction signée sur la pente du front selon les couches lues » : ce signe est déjà publié (Bailey, p. 23, un modèle, une tâche) ; la source du collisionneur parle d'une pente selon une **grille de budgets** (A sur D, tour 2). Ajouter « selon le budget » et « sur un modèle ou une tâche autres que ceux de l'antériorité », sinon K2 est en défaut.

**CLA8-09** — « la pureté des poids est un plafond de la classe de moniteurs, non une preuve d'inutilité du tirage » : « pureté des poids » et « tirage » ne sont définis nulle part dans le texte I. Définir en une demi-phrase, ou laisser partir la ligne avec le verdict non prononcé.

**CLA8-10** — Deux marqueurs « [verdict à insérer avant service] » désigneraient deux pilotes (pré-pilote d'étalonnage au préambule ; « mélange d'équilibre » à l'axe 8). Nommer le pilote dans chaque marqueur.

**CLA8-11** — « double oracle ; regret en ligne » : le double oracle calcule des meilleures réponses des deux côtés ; une fiche qui le suit construit un oracle d'attaque. Garder le mot ; la correction de CLA8-01 doit couvrir ce cas.

**CLA8-12** — Les renvois R-339, R-743, R-744, R-1037, R-1047, R-1056 valent sur la branche conv-audit ; dans `registres/decisions.md` de `main`, R-743 et R-744 désignent d'autres décisions (avis HELIOS ; entretien décalé) et la numérotation s'arrête à R-991. Écrire « (branche conv-audit) » après chaque renvoi.

## 3. Comptage et plafond

Par programme (caractères Unicode, bords exclus) et par `wc -m` (qui, dans ce conteneur à locale C, compte des octets) :

| Objet | Caractères | Octets (`wc -m` ici) |
|---|---|---|
| Texte I v5 servi, entre marqueurs | 11 698 (11 700 avec les sauts de ligne de bord ; rédacteur : 11 699) | 12 178 |
| Bloc axe 8, clôtures exclues | 2 761 | 2 884 |
| Phrase de boucle | 159 | 161 |
| **Somme** | **14 618** | 15 223 |
| Dépassement du plafond (12 000) | **+2 618** (rédacteur : ≈ 2 620, exact) | — |

Blocs du texte I v5, titre compris : glossaire 1 631 ; préambule à déroulé 3 198 ; axe 1 1 169 ; axe 2 375 ; axe 3 638 ; axe 4 1 377 (rédacteur : 1 377, exact) ; axe 5 552 ; axe 7 1 302 ; boucle 1 082 ; pièces 297.

**Recommandation : sous-session séparée**, sur le modèle de l'axe 7 (« ce préambule, sans les axes 1 à 5 »), confiance 0,7. Raisons : (i) le bloc resserré fait encore ≈ 1 950 caractères ; les ≈ 1 800 restants seraient pris sur des blocs dont chaque phrase est tracée à une décision D1–D14 ou Q1–Q6 et déjà « retirés pour la taille » (annexe 3) : couper là rouvre le recoupement ; (ii) la sous-session isole l'axe au cadre « niveau méthode » le plus exposé et permet d'étalonner la garde de forme sur des fiches d'axe 8 (R5) sans toucher à la session principale ; (iii) le vis-à-vis « à établir en g+1 » existe déjà pour l'axe 7. Coût : un devis de plus (R-1037 le prévoit). Taille de la sous-session ≈ 4 829 (glossaire, préambule) + 1 082 (boucle) + 297 (pièces) + ≈ 2 000 (bloc) ≈ 8 200 caractères. **Relever le plafond** est un nœud pour Lazar ; je ne le recommande pas : les quatre espèces ont cité ce plafond comme raison structurelle, confirmée au tour 2 (« survivrait au retrait du mot »).

**Si Lazar choisit de couper**, coupes concrètes (≈ 2 650 caractères), dans cet ordre :
1. Bloc axe 8 (≈ 800) : dernière ligne, doublon du préambule, remplacée par l'incise de CLA8-01 (−130) ; ligne « Pilote « mélange d'équilibre » … » tant que le verdict n'est pas prononcé (−230) ; (e) réduit à « borne haute seulement ; résultat conditionnel à la classe ; rejeu par un tiers sur poids et code empreintés » (−150) ; facultatif « dilemme … », non passé au collisionneur (−70) ; en (c), un seul énoncé pour les deux gels (−120) ; matériau sans glose (−100).
2. Préambule (≈ 410) : « État (pièce A) : … 160 unités », repris de la pièce A servie (−230) ; « Signal à 8 milliards … » en annexe 3 (−180 ; rouvre Q5).
3. Glossaire (≈ 250) : « Borne » renvoyé aux axes 2 et 5 (−180) ; « Transfert » et « Invariance » fondus (−70).
4. Axe 1 (≈ 130) : ligne « Matériau, non imposé » (déjà abrégée par D10).
5. Boucle (≈ 150) : « Consignés par génération : … » en annexe 3 (rouvre Q6).
Total ≈ 2 540 : 12 000 atteint de justesse, au prix de trois décisions rouvertes (Q5, Q6, D10). D'où la sous-session.

## 4. Cadre défenseur, niveau méthode

Tenu : aucune technique, aucun paramètre d'un mode de sabotage, aucune valeur de déplacement ; Bailey cité par pages et sens du prix ; les deux passages de classe 1 du tour 1 (C) ne sont ni repris ni résumés. Passages limites, corrigibles sans perte :
- « l'attaquant vise la défense composite entière » et « (e) un optimiseur local » : disent qu'un optimiseur d'attaque existe et ce qu'il vise ; niveau méthode, à condition que la fiche ne puisse pas en spécifier l'objectif (CLA8-01).
- « (a) … budgets (référence, maximum, unité de coût) » : grandeurs de mesure, pas recette ; acceptable si l'unité de coût ne nomme pas une opération d'attaque.
- « double oracle » (CLA8-11).
- « sous-espaces nécessaires à la tâche » (CLA8-06) : la forme de la source aurait été le passage le plus proche d'une direction d'attaque ; la reformulation est plus sûre, mais non déclarée.
- Hors texte servi, les confiances (0,65 à 0,90 ; 0,55) et les « sept grandeurs » : vérifiées sur les synthèses v2.

Aucun chiffre non sourcé dans le bloc : seuls des numéros de page (3, 23, 25-26, 26), vérifiés sur le PDF empreinté (p. 3 : « over 70 iterations » ; p. 23 : intervalle de confiance de la corrélation couches × performance ; p. 25 titre de § 6.2, p. 26 : « does not ultimately result in a robust monitor », § 6.3 « just how malleable », « tentative negative result »).

## 5. Non vérifié

- Les copies v1 des synthèses lues par le rédacteur ne sont plus sur disque (la `.sha256` de la tour 1 v1, `e4d5a5c9…`, concorde) ; les numéros de ligne cités ne sont pas vérifiables ; sur les v2, N10 (lignes 279–305 et 247–262) est conforme point par point.
- CROWN (page de titre), PSRO, double oracle : PDF non ouverts ; le bloc ne leur attribue aucun chiffre.
- Empreintes citées pour `registres/decisions.md` (`a409330a…`) et le LISEZMOI du corpus (`179f719a…`) : non recalculées (lecture par `git show`).
- Statut du pilote « mélange d'équilibre » : pris de R-1047 (brouillon 5, verdict non prononcé), non du dossier du pilote.
- L'étage 1 (analyseur programmé) : je raisonne sur le texte v5 ; le code du juge figé n'a pas été ouvert.
