# Journal — sections de résultats v3 (programme ; organisme d'idéation)

- Rédacteur : sous-agent neuf (Claude Opus 5.5), session mère reprise le 10 novembre 2026 (R-2191, R-2192). Je n'ai écrit ni la v1 ni la v2 de ces sections.
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-sections-resultats-v3-v1.md`, sha256 `9db81855aebe778dd73fe225cacf1d18ea9d26e737d93f9d83306c264288b9ff`, égale à son compagnon (vérifié à 11:39:52 UTC). Interdits communs v2 lus dans la consigne.
- Heures (relevées par `date -u`) : début 11:39:52 UTC ; sections scellées à 11:48:36 ; registre scellé à 11:50:42 ; journal écrit ensuite.
- Aucun commit, aucune poussée, aucun appel de modèle ni d'interface externe, aucune dépense.

## 1. Sorties

| fichier | rôle | empreinte |
|---|---|---|
| `section-resultats-programme-v3.html` | fragment HTML autonome, section « Résultats » du programme | `35589b8299cf7f4dab5fcc8fc654174581ea000ab4672682e4b407c1f600b8c1` |
| `section-resultats-organisme-v3.html` | fragment HTML autonome, section « Résultats » de l'organisme | `d6d702f5383347f16c894065ce45d96745a20f6016243d5f3b956828b3a3d9fd` |
| `registre-affirmations-v3.md` | renvois [A0] à [A100], [B1] à [B53] → chemin, empreinte, ligne | `38c24c925e151dc50f8b5b59eee9d8ff04c9b08e2cc4f52a9d9206553905780e` |
| `journal-v3.md` | ce journal | compagnon `.sha256` |

Les v2 (`resultats-pour-documents-v2/`, non scellées, interrompues) sont restées intactes ; je ne les ai que lues.

## 2. Méthode

1. Lecture entière des deux v2, du registre v1 (`49b166e9…`) et des lignes R-2100 à R-2192 de `registres/decisions.md` (par `grep -n '^| R-2\(1[0-9][0-9]\) '`, plus lecture complète des lignes longues R-2163, R-2164, R-2171, R-2175, R-2177, R-2179, R-2180, R-2184, R-2187, R-2188, R-2190, R-2191).
2. Rehachage des 34 pièces du registre v1 : toutes égales (aucun écart).
3. Vérification point par point de chaque affirmation neuve de la v2 (renvois A55 à A82, B46 à B50, dont la v2 n'avait pas de registre) contre la pièce : note 2a, rapport des prémisses, liste « ce qui manque », `registres/go.md`, synthèse provisoire de l'état de l'art de niveau 3 et son complément, rapports B1, B3, C1, C2, C3, C4, C5, C7 (branche `prep/etat-de-l-art-niveau3-v1`, tête `f0aaf0d1b`), rapports de lot 1, 5-A, 7-A, 7-B, 7-C, 7-D de la session à réseau (branche `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61c`), rapport du développeur v65 (branche `prep/organisme-v65-v1`, tête `3daf08e24`), verdict formel de T0.3 (branche `claude/upbeat-cray-dmauvv`, tête `8e1e751d8`). Lecture par `git show <branche>:<chemin>`, empreinte égale au compagnon de la même branche.
4. Ajout des rendus R-2180 à R-2190 et des décisions R-2130, R-2175, R-2182, avec R-2186 (T0.8) et R-2191 (relances).

## 3. Ce que j'ai retiré ou corrigé des v2, et pourquoi

1. **Collision Qu, Chen, Wang : « trois composantes sur quatre sont occupées » (v2, organisme § 7) → corrigé** en « deux en entier, une dans son principe seulement, une absente ». La contre-lecture C7 (l. 49-53) corrige C4 et R-2177 sur ce point : le jugement sur données postérieures n'est tenu que par construction, sans sceau, et pas dans le bras sur données réelles.
2. **« ni le sceau de la proposition par empreinte » (v2, liste de ce qui reste libre) → retiré.** C7 rattache le scellement par empreinte avant lecture (O17) et les prédictions scellées (O3) à « Masked Erosion », occupés dans leur principe ; ce qui reste non trouvé est le « tirage semé par l'empreinte » (N3S l. 83), que j'écris à la place.
3. **« un attaquant scripté contre un arbitre par e-valeurs, un proposeur qui reçoit les verdicts » (v2) → remplacé** par l'élargissement établi par C7 (trois arbitres fautifs, attaquant scripté, plan préenregistré ; REUSE et son adversaire théorique ; PROCTOR ; PACE).
4. **« Un contre-lecteur d'une autre lignée a été lancé » (v2, code v65) → précisé** : lancé, interrompu par le quota (passation, § 4), aucune contre-lecture rendue (constat : aucun fichier `contre-lecture-code-v65*` sur `main` ni sur les branches distantes, hors branches interdites, le 10 vers 11:43 UTC). Ajout des réserves du développeur lui-même (relevé non reproductible à l'octet ; issue à blanc « trop belle » ; bac réel non montré).
5. **T0.3 : « verdict annoncé sur une autre branche, non lu ici » (v2) → remplacé** : le verdict (`bc53b746…`) a été lu sur sa branche ; il dit « confirmé avec réserves », réserve principale citée. Il n'est pas fusionné dans `main` : dit tel quel.
6. **2606.10456 « synthétique »** : ajout de la divergence des lecteurs et de la lecture retenue par la synthèse (N3S l. 128-130), au lieu de la seule erreur.
7. **SafeDream, pages « 7, 14 » (v2) → « p. 5, 7 »**, pages que donne C1 (l. 347) pour 6,6 à 8,0 %.
8. **MIRAGE « 6 exfiltrations réussies seulement sur 120 essais » (v2) → « fidélité de l'encodage 6 sur 120, d'où un dénominateur réel de 6 »**, mots du rapport de lot 1 (l. 76) ; la v2 disait plus que la pièce.
9. **Gao « 5 % de fausses alarmes par pas » → « par occasion »** : C1 parle de lignes ou d'occasions d'alarme par unité, pas de pas.
10. **Statuts périmés** : « saboteur à budget, code non rendu » gardé mais daté (aucune branche poussée constatée) ; texte « accumulation » dit lancé, interrompu, non relancé ; consigne de l'audit des fuites dite au brouillon 2 ; T0.8 dit contre-lu, non scellable, dépense au directeur ; calendrier R-2177 dit antérieur à l'arrêt sur quota, sans pièce qui dise s'il tient.
11. **Retiré du tableau « Changements depuis 10:46 UTC » la ligne 10 que j'avais d'abord écrite** : la réécriture refusée du jeu J-C (R-2135, 10:06 UTC) est antérieure à 10:46, et la liste la porte déjà.
12. **Ajouté, sur pièces seulement** : décisions de R-2175 avec leurs états ; autonomie de calcul et enveloppe de 500 dollars (R-2182, GO-2026-11-10-09) ; enveloppe de 120 dollars **rapportée mais non inscrite**, donc non tenue pour accordée (R-2188) ; incidents du bras externe NARCBench (R-2184, R-2190) ; verdicts par revendication du niveau 3, avec les collisions partielles H9, papier B, HC2 et organisme ; prémisse de Terekhov et collègues ; Corll (2606.20746) ; contre-indice du classifieur de mots ; décisions de gouvernance du bras d'attaque, au seul niveau de ce qui est inscrit (R-2127, R-2145, R-2146) ; lien des deux lignées « organisme » (R-2152) ; lecture bornée d'A1-v4 donnée au directeur (R-2115).

## 4. Ce qui n'est pas dans le texte, exprès

- **Aucun taux de calibration** (R-2185), y compris ceux qu'écrit R-2173. Les décomptes de prédictions d'une expérience (31 sur 31 pour T0.3 ; 8 sur 11 pour A1-v4) viennent de leurs verdicts et sont gardés ; aucun agrégat sur plusieurs expériences n'est écrit. **Point à trancher par la mère** : si elle tient même ces décomptes par expérience pour couverts par R-2185, les deux phrases sont à retirer.
- Aucun résultat de la mesure unanime, de la lecture B de 7a, des sondes de 7a, ni du bras d'attaque au-delà des décisions inscrites.
- La réponse d'Argon à la question mère v3 n'est pas citée (la consigne de cette question n'a pas été versée, R-2191).
- Le nœud H6 (2605.26047) est seulement nommé dans la liste des nœuds de R-2190 : je n'ai pas lu de rapport qui le traite, je ne dis rien de son contenu.

## 5. Réserves et points ouverts

- **Non contre-lu.** Les deux sections et le registre attendent la contre-lecture par un autre modèle (R-2192, point 2).
- **Synthèse de l'état de l'art provisoire** : les verdicts du § 7 de la section programme peuvent changer à la version finale ; le complément 1 reprend des verdicts de la session sœur « sans relecture de ses rapports » (N3C l. 11-12) ; j'ai, moi, vérifié dans ses rapports les chiffres que je cite (88,2 % ; 6/120 ; TF-IDF ; Corll), pas tous les verdicts.
- Intervalle de λ* : la lecture scellée donne Wilson [0,777 ; 0,826] (EPL) ; le verdict officiel d'A1-v4 écrit [0,777 ; 0,827] (A4V l. 72). Écart d'arrondi ; j'ai gardé la lecture scellée, comme la v1 et la v2.
- Les lignes de `registres/decisions.md` sont citées sur le registre vivant relevé à 11:42 UTC ; le dépôt a avancé pendant le travail (`HEAD` relevé `d365995fa` vers 11:46 UTC).
- **Gestes à déclarer** : (a) une boucle `git ls-tree -r --name-only` sur les branches distantes, limitée au chemin `docs/notes/organisme-boucle-reelle-v1/code-v65/`, en excluant par motif les branches nommées par la règle 1 et la branche de quarantaine de la mesure unanime ; la liste a inclus la branche de la session du bras d'attaque (`claude/compassionate-meitner-d4ryyk`, non interdite par son nom) : seuls des noms de fichiers sous ce chemin de l'organisme ont été cherchés, rien n'a été affiché ni ouvert (sortie vide). (b) Disque plein vers 11:46 UTC (0 Mo libre) : une modification a échoué puis a été rejouée ; mon propre fichier de travail dans le bac à sable a été vidé ; rien d'autre n'a été supprimé ; la place est revenue d'elle-même.
- Aucune recherche récursive sur un dossier contenant un chemin interdit ; `verifier-arbre` non lancé.
