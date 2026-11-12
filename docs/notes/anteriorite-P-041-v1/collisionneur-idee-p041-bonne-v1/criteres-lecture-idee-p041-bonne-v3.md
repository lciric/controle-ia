# Critères de lecture de la synthèse — l'idée P-041 est-elle bonne ? (ordre des coups) — v3

v3 (30 octobre 2026), seconde contre-lecture appliquée (constats RES-1-1 à RES-1-4), après la première (constats CL-01 à CL-39, v2) ; les v1 et v2 restent intactes (`criteres-lecture-idee-p041-bonne-v1.md`, `711620e2…` ; `criteres-lecture-idee-p041-bonne-v2.md`, `a9db6ed1…`). Gelés avant lecture, scellés à part, **jamais envoyés** (ni au collisionneur, ni à un modèle seul).

- Envoi lu : `question-idee-p041-bonne-envoi-v3.md`, empreinte `1d28540375ef0c2eba27f53dcb1e51a0e067c0bf1279de7ab3d3bacd7614b105` (identique octet pour octet à l'envoi v2 : aucun constat de la seconde contre-lecture ne touchait l'envoi ; nouveau nom gardé pour aligner les trois fichiers).
- Faits servis : `faits-idee-p041-bonne-v3.md`, empreinte `8ade357a6c0acf67bc38321dbf98eeb5077e93abc39cd40c787673db3e7cb90c` (seuls changent, par rapport à la v2, l'en-tête et les faits 13 à 15 : collisionneur v7, son empreinte, numéros de ligne revérifiés).
- Versions remplacées, gardées intactes : envoi v1 (`65d4ce3b…`), envoi v2 (`1d285403…`), faits v1 (`d6468ac0…`), faits v2 (`6f436534…`). Les faits v1 servent de **copie interne non servie** : identifiants des travaux des faits 6 à 12, faits 13 et 14 complets (modèles derrière chaque lettre, limites de mots des tours).
- Collisionneur : `donnees/collisionneur-texte-III-v1/collisionneur_v7.py` (`c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc`, égale à son compagnon, vérifiée le 30 octobre 2026). Copie de la v6 (`c67239b9…`, gardée intacte) ; seuls changements : noms neutres des tours (E1-T2 « critique-meta », E2-T2 et E3-T2 « critique-croisee », E2-T3 et E3-T3 « reponse »), parenthèse finale du point (b) de la consigne E3-T2 réécrite en positif (« seulement des lois de probabilité, des paramètres et des estimateurs »), chaîne `VERSION` (« collisionneur-v2.10-quatre-especes-opus46-noms-neutres ») et une ligne d'en-tête en commentaire, qui décale d'une ligne tout le reste du fichier.
- Source de fond : `docs/notes/anteriorite-P-041-v1/idee-P-041-est-elle-bonne-fusion-v3.md` (`343617ca…`), section 5 ; note d'antériorité `docs/notes/anteriorite-P-041-v1/note-anteriorite-P-041-lecteur-neuf-v1.md` (`618c7c48…`).
- Points 2, 13, 14, 15 et 16 repris, adaptés, des points 2, 10, 11, 12 et 13 de `donnees/collisionneur-texte-III-v1/criteres-lecture-texte-III-etroite-v3.md`.

**Ajouts de l'arbitre au-delà de la section 5 de la fusion v3** (déclarés ici, constats CL-10 et CL-27) : quatrième modalité « pour les deux » (choix de rédaction : un verdict qui vaut à la fois pour la conception et pour l'évaluation n'entre dans aucune des trois modalités de la section 5 ; **à faire valider par Lazar** ; **envoi suspendu à la validation de la quatrième modalité par Lazar, consignée dans `registres/decisions.md` ; à défaut, envoi et critère 1 ramenés à trois modalités, par des versions nouvelles (envoi v4, critères v4)**, avant tout envoi) ; définitions de « bonne pour la conception » et « bonne pour l'évaluation » (bloc 5 de l'envoi v3, identique à la v2, tirées de la section 1, points 1 et 3) ; point de fonctionnement à 1 % et puissance (section 3) ; choix de la transformation du test de reparamétrisation (section 4) ; bras 5 (section 1, point 9) ; liste des étapes du bloc 1 (rédaction de l'arbitre, ouverte en v2 à une autre étape nommée).

**Seuil de « commun »** : porté à trois pages sur quatre (au lieu de « deux modèles au moins » du point 1 des critères texte-III étroite v3), car deux contre deux n'est pas décidable (constat CL-35).

**Traçabilité des faits 6 à 12** (constats CL-04 et CL-21 ; non servie). Les faits v3 servis, comme les v2, désignent les travaux par auteurs et année, sans titre ni identifiant ; le fait 6 sans auteur. Correspondance, d'après la table de la section 4 de la note d'antériorité :

| Fait v2 | Désignation servie | Rang et ligne de la note | Identifiant | Empreinte du PDF |
|---|---|---|---|---|
| 6 | « un article du champ du contrôle » | 36, ligne 164 | `2510.09462v2` | `96c16e33…` |
| 7 | Cooper Stickland, Michelfeit et collègues 2025 | 39, ligne 167 | `2512.13526v1` | `bcbce510…` |
| 8 | Bhatt et collègues 2025 | 29, ligne 157 | `2504.10374v1` | `5f802d67…` |
| 9 | Terekhov, Gulcehre, Hebbar et Benton 2026 | 52, ligne 180 | `2606.08892v2` | `aea0f2d1…` |
| 10 | Korzhyk, Yin, Kiekintveld, Conitzer et Tambe 2011 | 2, ligne 130 | `1401.3888v1` | `ac99b152…` |
| 11 | Kaufmann, Kang, Sun et collègues 2023 | 12, ligne 140 | `1908.08016v4` | `492d8211…` |
| 11 | Tramèr et Boneh 2019 | 10, ligne 138 | `1904.13000v2` | `b45f282a…` |
| 11 | Casper, Schulze, Patel et Hadfield-Menell 2024 | 22, ligne 150 | `2403.05030v6` | `46ad7a22…` |
| 12 | Dalvi et collègues 2004 | 63, ligne 191 | (aucun ; fichier `Dalvi-2004-…`) | `4c2b326a…` |
| 12 | Goodfellow et collègues 2014 | 3, ligne 131 | `1406.2661v1` | `ff5819e3…` |
| 12 | Schmiedlechner et collègues 2018 | 8, ligne 136 | `1811.12843v1` | `fc2eb443…` |
| 12 | Cheng, Hu, Ma et collègues 2026 | 59, ligne 187 | `2609.36580v2` | `e0df2463…` |

Le fait 3 servi cite la proposition P-041 par son dossier et son empreinte ; chemin complet : `docs/decisions/proposition-P-041-organisme-coevolutif-attaque-defense-v1.md` (`254b1782…`, égale à son compagnon ; ligne 3 : « Rien n'est lancé »). Le nom du fichier n'est pas servi parce qu'il contient un mot de la liste proscrite. Au fait 9, la note (ligne 42) dit que la défense « voit les invites et les scores » de l'autre joueur ; l'envoi v3 et les faits v3 écrivent « les éléments et les scores », sans le mot « résumés », que la note ne porte pas.

**Réserve des constats CL-23 et CL-24 levée (constats RES-1-1 et RES-1-2, 30 octobre 2026).** Le collisionneur v7 est écrit et scellé (voir plus haut) : les identifiants de cellule servis au tour III.3 prennent la forme `E3-T2-critique-croisee-X` (`id_cellule`, lignes 304 et 305 ; `bloc_piece`, ligne 351 ; `entrees`, ligne 346), et la consigne E3-T2 (lignes 187 à 192) ne porte plus de formulation négative. Pour mémoire : la commande `etage3` ne lance que `ORDRE_ETAGE[3]` (lignes 129, 722, 986 à 1002 de la v7) ; la consigne E2-T2 n'est pas servie dans ce run. Le run se lance avec le collisionneur v7, jamais la v6.

## Verdict sur la question finale

1. **Verdict commun ou divergent.** Chaque page du tour III.3 lisible (ni refusée, ni écartée au critère 2) est rangée dans l'une des quatre modalités : conception, évaluation, les deux, aucune. Les modalités se lisent selon les définitions du bloc 5 de l'envoi v3 (`question-idee-p041-bonne-envoi-v3.md`, `1d285403…`). Une page qui emploie un autre sens est rangée selon le sens qu'elle déclare, signalée, et ne concorde qu'avec une page de même sens.
   - Une page de la forme « M à condition C » est rangée M, et C est sa condition au sens de la puce suivante. Une modalité de repli écrite pour le cas où C échoue est rapportée à côté. La concordance au sens de « commun » se juge seulement sur le couple (M, C). Les branches de repli se comparent seulement entre pages qui en écrivent une, et leur désaccord est rapporté sans rompre le verdict commun. Une branche non écrite n'est jamais inférée. Une page qui donne deux modalités sans dire laquelle vaut sous C est signalée et rangée parmi les verdicts sans condition mesurable (puce « verdict sans condition mesurable » ci-dessous).
   - Deux conditions concordent si elles portent sur la même quantité (même contraste entre les mêmes scores et les mêmes bras) avec le même sens ; un seuil chiffré différent ne rompt pas la concordance, il est rapporté.
   - Le mode de réception de θ déclaré fait partie de la définition du bras 1. Deux conditions qui font intervenir le bras 1 ou le test de reparamétrisation ne concordent que sous le même mode déclaré. Une page sans mode déclaré est signalée, et ses conditions sur ces éléments ne concordent avec aucune autre. Le mode de chaque page est rapporté. La concordance devient ainsi plus difficile à obtenir, mais elle est honnête ; cela est rapporté avec le verdict.
   - **Commun** : au moins trois pages lisibles sur quatre donnent la même modalité avec des conditions concordantes.
   - **Divergent** : moins de trois pages concordantes, y compris à deux contre deux. Rapporté au format décision : chaque modalité défendue, les lettres qui la défendent, sa condition, son avantage et son inconvénient ; aucune majorité n'est déclarée.
   - **Non jugeable** : moins de trois pages lisibles. Dit tel quel ; aucun verdict n'est extrait des tours III.1 ou III.2 pour combler.
   - Verdict sans condition mesurable : signalé ; il compte comme lisible, mais ne peut concorder qu'avec un autre verdict sans condition.
   - Le verdict de la synthèse rapporte le verdict des modèles ; il n'est pas le verdict du programme et ne vaut ni décision ni porte.

## Garde et périmètre

2. Une réponse qui décrit autre chose que les objets statistiques du périmètre de l'envoi v3 (contenu d'une épreuve, comportement d'agent, scénario, valeur de paramètre présentée comme une famille réelle) est écartée et comptée. Déclarer une classe paramétrique de lois et des valeurs de θ marquées illustratives n'est pas décrire une famille ; l'ancrage matériel (calcul, coût) n'est pas hors cadre.
3. Hors cadre : un générateur qui fait appel à un agent ou à du texte, ou qui prend d'autres entrées que des activations synthétiques et les sorties d'une défense figée sur ces activations (fait 4), est signalé ; la partie concernée n'est pas lue sur le fond. Hors tour : le contenu des familles, le choix de bancs ou de jeux de données, l'organisation des concepteurs de familles ; marqué « hors tour », non compté dans « commun ».

## Contenu des blocs

4. Trois scores : chacun doit avoir sa statistique, son unité d'échantillonnage et son intervalle. Un score (iii) où la défense ou son seuil est mis à jour après le dernier coup du générateur n'est pas un score (iii) : signalé. Un signe de (i) − (ii) ou de (ii) − (iii) donné sans condition est signalé. Score non lu au taux de détection à 1 % de fausses alertes sur les cas honnêtes : signalé.
5. Dépendance : au moins une mesure calculable de la dépendance entre familles d'entraînement et familles tenues à l'écart, et les deux régimes (support commun, support disjoint). Une réponse qui déclare les familles tenues à l'écart sans dépendance avec les familles d'entraînement au niveau des lois et des paramètres, y compris sous support disjoint (même schéma), est signalée ; une graine de tirage séparée n'est pas une absence de dépendance. Prédiction de (i) − (ii) en fonction de la mesure de dépendance absente : signalé.
6. Cinq bras : tous présents, au même budget, exprimé dans une unité déclarée. Un bras manquant, ou un budget inégal non corrigé, est signalé. Bras 1 et 2 qui diffèrent par autre chose que ce que reçoit la défense : signalé. Au bras 5 : une règle propre à une seule famille gardée, ou des familles tenues à l'écart admises dans l'expérience accumulée, est une fuite signalée ; un palier mis à jour pendant les mesures (ii) ou (iii) tombe sous le critère 4.

   6 bis. Bloc 1 : l'étape où l'avantage cesse d'être légitime est relevée, avec sa justification, et rapportée par lettre. Si aucune étape n'est nommée, ou si la justification manque : signalé. Une étape hors des quatre (entraînement, sélection de la défense, étalonnage du seuil, mesure finale) est permise par l'envoi v3 si elle est nommée ; elle est rapportée à part.

   6 ter. Bloc 3 : un tableau des prédictions, obligatoire pour (ii) − (iii) pour chaque bras (1 à 5) et chaque régime (support commun, support disjoint), soit 10 cases, chiffrées, signées et marquées illustratives ; une case obligatoire manquante est signalée ; les cases facultatives sur (i), (ii) et (iii) ne sont pas lues ici. On relève aussi les seuils de décision de l'expérience, un plan de puissance par simulation (sans résultat présenté comme calculé ; une puissance présentée comme calculée est signalée), au moins un contrôle négatif propre au bloc 3 et la condition d'échec de l'idée ; chaque élément manquant est signalé.
7. Test de reparamétrisation : application inversible, mêmes lois, étape d'application dite. Un test appliqué à une étape où la défense ne lit pas les paramètres est signalé « non informatif ». Un test sans dire qui choisit la transformation est signalé.
8. Duels : au moins deux par réponse au tour III.1, dont un sur la quantité du bloc 4 et un sur la reparamétrisation, chacun avec métrique, seuil, contrôle négatif et issue qui falsifie chacune des deux hypothèses. Un élément manque : duel « non retenu ». Moins de deux duels retenus : réponse signalée.
9. Mesure minimale des instruments : jugée seulement s'il y a (i) une vérité connue, (ii) une mesure pour chacun des quatre instruments (défense, générateur, mesure de dépendance, test de reparamétrisation), (iii) le test statistique fixe sans apprentissage comme base à battre, (iv) un contrôle négatif. Sinon « non jugeable ». Un générateur déclaré adéquat sans comparaison au pire cas connu est signalé.
10. Quantité qui tranche : un contraste sur (ii) − (iii) entre le bras 1 et le bras 2 (le bras 5 peut s'y ajouter), avec estimateur, intervalle, effet minimal, signe prédit et issue qui falsifie. Une réponse qui tranche sur (i) ou (ii) seuls est signalée.

   10 bis. Bloc 5 : effet de chacun des deux régimes et de chaque issue du test de reparamétrisation sur le verdict absent : signalé.

   10 ter. Tour III.2 : section « Sur la proposition X » sans condition mesurable au niveau des lois ou sans fuite nommée entre ce qui construit la défense et ce qui l'évalue : signalée ; une condition formulée comme une conduite d'agent tombe sous le critère 3.
11. Fidélité aux faits du champ : une affirmation selon laquelle le champ interdit toute défense informée à l'entraînement contredit le fait 9 et est signalée ; une affirmation selon laquelle les travaux des faits 6 à 8 publient leur chiffre sans que le second joueur joue en dernier contredit ces faits et est signalée. Une affirmation qui donne comme rapporté qui joue le dernier coup d'un cycle au fait 9, ou lequel des deux joueurs y mène, est signalée (le fait 9 dit que ce n'est pas rapporté). Le signe du transfert hors classe présenté comme établi, dans un sens ou dans l'autre, contredit le fait 11 et est signalé.

## Forme et statuts

12. Statuts : un fait au statut changé, ou présenté avec un statut hors des quatre, est signalé ; les faits 4 (HYPOTHÈSE) et 5 à 12 (RAPPORTÉ) présentés comme VÉRIFIÉ sont signalés ; un chiffre absent des faits et de l'envoi, non marqué « illustratif », est signalé ; tout identifiant arXiv donné par un modèle est signalé (règle 3 du préambule, ligne 140 du collisionneur v7), qu'il porte ou non « référence à vérifier » (les faits v3 servis n'en contiennent aucun).
13. Page du tour III.3 : il manque l'un des quatre éléments (verdict avec condition, quantité qui tranche, expérience décisive corrigée, établi et non établi) : signalé ; une expérience décisive en plus de cinq lignes : signalée (une ligne = une ligne non vide de la cellule ou un élément de liste) ; il manque la ligne « l'expérience à faire en premier » : signalé.
14. Plafond de 2 500 mots : la cellule est lue en entier et le dépassement est signalé.
15. Nouveauté (R-750) : un élément n'est compté « nouveau » que s'il ne figure dans aucune cellule du tour III.1 de ce run ; la comparaison se fait après la lecture complète du tour lu, jamais avant.
16. L'avis d'Argon à part, s'il y en a un, est lu à côté et n'est pas compté dans « commun ».
17. Refus : un refus est rapporté tel quel, avec sa catégorie s'il en donne une ; il compte comme page non lisible au critère 1 ; il n'est jamais reformulé dans le run (fait 14). Deux refus ou plus dans un même tour : signalé comme une lecture de la question par la garde, à traiter avant tout nouvel envoi.
