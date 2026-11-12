# Contre-lecture (R2) de « Choix de l'attaque publiée à reproduire et antériorité — v1, brouillon 1 »

- **Statut.** Contre-lecture, 10 novembre 2026. Sous-agent neuf, qui n'a pas écrit la note relue (R2). Non scellée.
- **Note relue.** `docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon1.md` (lue sur disque, non modifiée, R12).
- **Fichiers lus pour vérifier** (explicitement) : la note ci-dessus ; `docs/notes/anteriorite-P-041-v1/bailey-depot-public-parametres-v1.md` et son `erratum-bailey-depot-public-parametres-v1.md` ; `docs/etat-de-l-art-controle-ia-v1.md` ; la ligne GO-2026-10-31-05 de `registres/go.md` ; `docs/notes/anteriorite-P-041-v1/verification-bailey-2412.09565-v1.md` ; `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` ; `docs/sources/lecture-pdf-niveau2/rapport-lot3-Cc-evasion-quorum-v1.md` ; `docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneur-protocelles-v1.md` ; `docs/programme-controle-ia-v2.md` (modèles, l. 249) ; `docs/notes/anteriorite-P-041-v1/contre-lecture-prereg-malleabilite-v3.md` ; la première page du PDF `evade-from-feedback-2026-2609.36490.pdf` et les empreintes compagnons des deux copies du candidat 2.
- **Portée.** Je n'ai lu aucun contenu du coffre ni aucune valeur de clé. Niveau infrastructure et antériorité, comme la note relue.

## 0. Verdict

**Non scellable en l'état ; scellable après correction des points bloquants.**

Le *choix final* (reproduire Bailey comme témoin d'ancrage) est probablement défendable pour de bonnes raisons — code public au commit identifié, protocole = la boucle adverse exacte mesurée par le programme, vérification R7 ciblée déjà faite sur le PDF. Mais la **justification écrite est fausse sur trois faits vérifiables**, et deux de ces faits portent précisément sur la comparaison entre les deux candidats et sur la vérification R7. Une note destinée à faire foi ne peut pas être scellée avec des faits faux ; les trois corrections sont identifiées et faisables.

Avant les reproches, pour l'équilibre (R4) : la note est **correcte** sur le devis (test (a) 31 attendus / 74 pire cas / plafond 75 ; `devis-…-v1.md` l. 15, 19, 23), sur la carte du devis à corriger (40 → 80 Go), sur la date d'expiration du GO (14 novembre), sur la description de la sonde de Bailey (perceptron multicouche à couche cachée de 64, ensemble incrémental à différence de moyennes, activation du dernier jeton — `verification-bailey…` l. 27), sur le fait que Bailey est « pris » dans l'état de l'art v1 (l. 134, 154), et sur le statut « rapportée, pas revendiquée » de la mesure supplémentaire.

Décompte : **3 bloquants, 5 majeurs, 6 mineurs.**

## 1. Points bloquants

### B1 — Le modèle est inversé entre les deux candidats

- **Passage visé.** §0 Verdict (« modèle identique au nôtre (Llama-3-8B-Instruct) ») ; §1 tableau l. 22 (« identique au modèle du programme ») ; §1 avantage 2 (l. 37) ; §2 tableau l. 54 (« à distinguer de notre Llama-3-8B-Instruct ») ; §2 inconvénient 4 (l. 71).
- **Fait vérifié.** Le modèle du programme est **Llama-3.1-8B-Instruct** (`docs/programme-controle-ia-v2.md` l. 249 : « Modèles : Llama-3.1-8B-Instruct (agents, sondes)… »). Bailey tourne sur **Llama-3-8B-Instruct**, soit la version 3.0 (état de l'art v1 l. 134 ; `verification-bailey…` l. 26). Le candidat 2 tourne sur **llama-3.1-8b** (`rapport-lot3-Cc…` [C89] p. 20 : « The adapter is trained against a probe at one layer around three quarters of the model depth, 24 of 32 on llama-3.1-8b » ; tableaux [C66] p. 23). **C'est donc le candidat 2, écarté, qui partage le modèle du banc du programme ; Bailey en diffère d'une version mineure.**
- **Pourquoi c'est bloquant.** L'« avantage » le plus fort attribué à Bailey (« modèle identique au nôtre ») est faux, et il est l'exact miroir d'un « inconvénient » attribué au candidat 2 (« un écart supplémentaire ») qui est faux aussi. La comparaison est renversée sur ce critère, dans le Verdict qui fait foi.
- **Correction attendue.** Retirer « modèle identique au nôtre » des avantages de Bailey. Clarifier ce que « le nôtre » désigne : si c'est le banc du programme, il est en 3.1 et Bailey (3.0) en diffère ; si c'est le modèle de la reproduction P-041 (celui de Bailey par construction), alors « identique » est une tautologie, pas un avantage, et l'écart 3.0/3.1 avec le reste du programme doit être **nommé comme un écart**. Retirer l'« écart de modèle » des inconvénients du candidat 2 (et noter qu'il est, lui, aligné sur 3.1).

### B2 — Le document du candidat 2 est déclaré absent, alors qu'il existe, est empreinté et a été lu en entier

- **Passage visé.** §0 (« absent de l'état de l'art v1, et les chiffres cités ne sont pas vérifiés sur un document empreinté ») ; §2 tableau l. 58 (« Document empreinté : Absent du dépôt ») ; §2 inconvénient éliminatoire 1 (l. 68, « Aucun document empreinté dans le dépôt ») ; §4 l. 101 (« Non — aucun document empreinté »).
- **Fait vérifié.** Le PDF existe en **deux copies empreintées**, empreinte conforme et identique (`eb6d5bbe…`) : `docs/sources/pdf/anteriorite-P-041-v2/c3/evade-from-feedback-2026-2609.36490.pdf` (+ `.sha256`) et `docs/sources/pdf/2609.36490v1.pdf` (+ `.sha256`). Il a été **lu en entier** et dépouillé page par page dans `rapport-lot3-Cc-evasion-quorum-v1.md` (en-tête « en entier », empreinte contrôlée). Il figure dans l'antériorité de niveau 2 (`etat-de-l-art/niveau2-v1/anteriorite-v1.md`) sous HC5 (l. 14), H7 et H5 (l. 20), L (l. 122) et la transposition jeton→action (l. 138, avec chiffres 0,25 ; 0,04).
- **Pourquoi c'est bloquant.** Les deux inconvénients éliminatoires du candidat 2 (« aucun document empreinté », « antériorité non établie ») reposent sur un fait faux. C'est aussi une violation de R11 (déclarer un fichier absent sans vérifier sur disque et par empreinte). L'élimination du candidat 2 peut rester la bonne décision, mais plus pour ces motifs-là.
- **Correction attendue.** Corriger l'affirmation. Refonder l'écartement du candidat 2 sur des motifs exacts s'il en reste (voir ci-dessous : code public non confirmé ; coût de calcul non chiffré par les auteurs, `lot3-Cc` « Coût de calcul : Non chiffré » ; méthode = réglage fin des poids, pas seulement contexte). Supprimer « l'antériorité n'est pas établie » (voir m1, R8).

### B3 — « A100 80 Go » est attribué à la p. 26 du papier et coché « vérifié », contre l'erratum

- **Passage visé.** §1 tableau l. 28 (« Bailey déclare 80 Go, p. 26 ») ; §4 tableau l. 98 (« A100 80 Go | Bailey, note de bas de page p. 26 | Oui »).
- **Fait vérifié.** `erratum-bailey-depot-public-parametres-v1.md` (dans le même dossier que la fiche citée par la note) : « Le papier ne nomme **aucune** carte : la note de bas de page donne seulement les durées. » La source de l'A100 80 Go est le **dépôt public** (README l. 96 ; `evaluate_defenses.sh` l. 7), « provenance par lecture de dépôt, non opposable seule (R7) ». De plus, `contre-lecture-prereg-malleabilite-v3.md` (CL3-m8, l. 129) note que ces fichiers du dépôt **n'ont pas pu être lus** (accès GitHub refusé) et qu'« aucune copie empreintée n'est sur disque ».
- **Pourquoi c'est bloquant.** La note présente comme **vérifié sur PDF empreinté (« Oui », p. 26)** un chiffre qui n'est ni dans le PDF ni empreinté depuis le dépôt. C'est exactement l'erreur que l'erratum a corrigée, répétée ; c'est une violation directe de R7 (chiffre opposable → chemin + empreinte + page).
- **Correction attendue.** Retirer « p. 26 » et l'attribution au papier. Attribuer la carte au dépôt public (non opposable seule) ; marquer la ligne « non opposable en l'état — à empreindre au scellement » ; citer l'erratum. La cible A100 80 Go reste valable comme choix de matériel ; seule sa **provenance** est fausse.

## 2. Points majeurs

### M1 — Le chiffre du candidat 2 est déclaré « non vérifié » alors qu'il est opposable

- **Passage visé.** §2 tableau l. 56 (« 96 % … R7 : non vérifié sur un document empreinté ») ; §4 l. 101.
- **Fait vérifié.** Le chiffre est vérifié sur le PDF empreinté : `rapport-lot3-Cc…` [C32] p. 6 « the resulting model organism reduces the monitor's TPR to 0.040 (95% CI [0.005, 0.100]) » et [C10] p. 1 « reducing TPR further to 4% on held-out concept monitors » — soit 96 % d'évasion, et ce sont des **chiffres de texte** (opposables), pas des lectures de figure. Ironie à relever : la solidité R7 des deux candidats est inversée dans la note (voir M2).
- **Correction attendue.** Corriger la mention R7 du candidat 2. Si on l'écarte, le faire sur un motif exact, pas sur « chiffres non vérifiés ».

### M2 — Les chiffres de Bailey retenus sont « lus sur figure » mais cochés « vérifié : Oui »

- **Passage visé.** §1 tableau l. 30 (oscillation 100 %/0 %, évasion ≈ 85-90 %, « lu sur la figure ») ; §4 tableau l. 94-96 (colonne « Vérifié sur document empreinté ? » = « Oui »).
- **Fait vérifié.** `verification-bailey…` l. 99 (Réserves) : « Les chiffres lus sur figure (oscillation 100 %/0 %, environ 72 et 91 époques, environ 85 à 90 % d'évasion pour la MLP) sont des lectures d'image à basse résolution, pas des chiffres du texte ; **ils ne sont pas opposables en l'état (R7)**. » Les cocher « Oui » dans la colonne de vérification est trop fort. À l'inverse, Bailey fournit des **chiffres de texte** opposables qui serviraient mieux la mesure (b) : p. 26, « 35 % d'évasion et rappel nul à 1 % de fausses alertes après 16 384 pas contre 95 % et 256 pas sans durcissement » (`verification-bailey…` l. 83).
- **Correction attendue.** Marquer ces chiffres « lu sur figure — non opposable (R7) ». Pour tout chiffre destiné à l'entretien, préférer les chiffres de texte (p. 26), qui forment en plus un couple de coûts directement utile à HC4.

### M3 — La mesure (b) est survendue comme « la taxe de déplacement »

- **Passage visé.** §0 (« Mesure supplémentaire recommandée : la première ligne du tableau de coût de HC4 ») ; §3 l. 83 et 86 (« Directement la taxe de déplacement promise au jury » ; « Il n'exige rien en plus du test (a) »).
- **Analyse.** Un **point de coût unique** n'est pas une taxe de déplacement : une « taxe » suppose une comparaison sur au moins deux régimes (avec/sans durcissement, ou selon le nombre de couches obfusquées — c'est le sens de « croissante avec le nombre de couches » dans l'état de l'art v1 l. 134, et de la ligne « Aucune comparaison de coût publiée » l. 243). La note le concède (« un seul régime, pas un tableau complet ») puis l'appelle quand même « la taxe ». Les grandeurs d'un régime (pas, mémoire, taux d'évasion) sont bien des sous-produits du run — donc (b) est un **point de coût citable sans travail en plus**, ce qui est juste —, mais pas « la taxe », et pas inédit : Bailey publie déjà un couple de coûts (p. 26), et le candidat 2 est un **contre-indice publié à HC4** sur les axes calcul/requêtes/succès (`lot3-Cc` : « Contre-indice principal — HC4 … rang 1, une époque, 32 verdicts binaires, 96 % d'évasion »). Tension interne : la note choisit de mesurer HC4 tout en écartant, sur des bases fausses (B2, M1), le papier le plus pertinent pour HC4.
- **Correction attendue.** Appeler (b) « un point de coût » (un régime), pas « la taxe ». Le situer par rapport aux coûts déjà publiés (Bailey p. 26 ; candidat 2 comme contre-indice HC4 connu). Garder « rapportée, pas revendiquée » (déjà dit, bon).

### M4 — La licence du code de Bailey n'est pas vérifiée, et ne l'est pas dans l'état actuel

- **Passage visé.** §1 tableau l. 24 ; §1 inconvénient 3 (l. 46) ; §4 l. 100 ; §5 point 1.
- **Analyse.** La note met la licence en « à vérifier au scellement » — honnête — mais elle **verrouille Bailey comme « candidat retenu »** en s'appuyant sur « code public » comme avantage décisif (§1 avantage 3) sans licence connue. `contre-lecture-prereg-malleabilite-v3.md` (CL3-m8/m9, l. 129, 147) indique que l'accès GitHub au dépôt a été refusé à une session, qu'aucune copie n'est empreintée sur disque, et qu'un accès sous licence (poids, code) est un nœud « compte » pour Lazar. Une licence absente ou restrictive (dépôt sans fichier `LICENSE` = tous droits réservés par défaut) **invaliderait l'usage du code** et donc le choix. Je n'ai pas pu vérifier la licence moi-même dans cette session (dépôt non présent, pas d'accès).
- **Correction attendue.** Traiter la vérification de licence comme un **préalable au verrouillage du choix**, pas comme une formalité de scellement ; l'inscrire au nœud « compte/accès dépôt » pour Lazar. Tant qu'elle n'est pas connue, écrire le choix comme « retenu sous réserve de licence ».

### M5 — Le risque d'expiration du GO est sous-estimé

- **Passage visé.** §1 inconvénient 1 (l. 44) ; §5 point 3 (« Renouveler ou confirmer le GO **si** le préenregistrement n'est pas scellé avant le 14 novembre »).
- **Analyse.** Nous sommes le 10 novembre ; GO-2026-10-31-05 expire le **14 novembre** (4 jours). Le chemin critique restant (§5 : vérifier la licence, corriger le devis, écrire un préenregistrement complet, le faire contre-lire R2, le sceller, le déposer chez le tiers, lancer un pilote, épingler StrongREJECT) est **quasi impossible en 4 jours**. Dépenser sans GO valide est un interdit dur. Le renouvellement n'est donc pas une éventualité « si », c'est le cas quasi certain.
- **Correction attendue.** Mettre la demande de renouvellement/extension du GO en **tête** du §5 et la traiter comme attendue, pas conditionnelle. (C'est un nœud de décision pour Lazar : dépense/GO.)

## 3. Points mineurs

- **m1 — Faux-gap R8 sur l'antériorité (rattaché à B2).** §2 inconvénient 2 (l. 69) : « Absent de l'état de l'art v1 : l'antériorité n'est pas établie. » L'absence du *fichier v1* (`etat-de-l-art-controle-ia-v1.md`, vérifié : 2609.36490 n'y figure pas) est vraie, mais en tirer « antériorité non établie » est un faux-gap : l'antériorité **est** établie au niveau 2 (`niveau2-v1/anteriorite-v1.md`) et dans les notes P-041. *Correction* : « absent de l'état de l'art **v1** (mais traité au niveau 2) » — ne pas en faire un motif d'élimination.
- **m2 — Coût-performance SQL sur un autre modèle.** La « taxe d'obfuscation SQL » de Bailey est mesurée sur **Gemma-2-2b** (`verification-bailey…` l. 84), pas sur Llama-3-8B. Si la mesure (b) évoque un coût en performance, ne pas mélanger les modèles. *Correction* : préciser le modèle de chaque chiffre de coût repris.
- **m3 — « Écart de prix négligeable » à vérifier au pire cas.** §1 inconvénient 2 (l. 45) et §5 point 2 (l. 106) : « +0,21 USD/h… négligeable ». La durée peut dépasser 24 h (§1 l. 29 ; `bailey-depot-…` l. 39). Au pire cas, le poste carte doit rester sous le plafond 75. *Correction* : le devis v2 vérifie que le pire cas tient sous 75, pas seulement constater +0,21 USD/h.
- **m4 — « Sonde publiée » : recette, pas poids figé.** Chez Bailey la sonde n'est pas un artefact de poids distribué mais une **recette réentraînée dans la boucle** (perceptron 64 ; ensemble à différence de moyennes). *Correction* : écrire qu'on reproduit la recette de sonde + la boucle, pour que « témoin d'ancrage contre une sonde publiée » soit exact.
- **m5 — PDF de StrongREJECT manquant, omis du §5.** `docs/notes/inventaire-pdf-manquants-v1.md` (l. 45, 69) classe le PDF de StrongREJECT (Souly et coll. 2024, 2402.10260) **manquant et bloquant** pour le scellement des préenregistrements (citer la validité du juge). Le §5 liste « épingler version et empreinte de StrongREJECT » mais pas « verser le PDF manquant ». *Correction* : ajouter le versement du PDF de StrongREJECT au §5.
- **m6 — Témoins R5 nommés mais non définis.** §5 point 4 nomme « témoin à faille plantée » et « honnête contre honnête » — bonne direction (R5), mais sans dire ce qu'ils seraient ici (cas sain = sonde à bon rappel sur activations non camouflées ; artefact = évasion factice que la mesure doit attraper). *Correction* : les définir au préenregistrement, avec le tableau « garde → cas sain qui passe → artefact qui arrête » demandé par CL3 de la malléabilité (l. 87).
- **m7 (pour mémoire) — Vérification R7 déjà faite, à citer telle quelle.** Bon point de la note ; veiller seulement à reprendre les **deux surévaluations** signalées par `verification-bailey…` (« réfutée » → « contrainte » ; « publié » pour la boucle, pas pour les lois synthétiques de P-041), ce que la note fait déjà en §1 l. 21.

## 4. Renvois vérifiés par moi-même

**15 renvois vérifiés sur la source primaire ou le fichier cité :**

1. GO-2026-10-31-05 — `registres/go.md` l. 170 (plafond 210 ; test (a) 75 ; expire 14 nov ; A100 80 Go ; conditions).
2. Modèle du programme = Llama-3.1-8B-Instruct — `docs/programme-controle-ia-v2.md` l. 249.
3. Modèle du candidat 2 = llama-3.1-8b — `rapport-lot3-Cc…` [C89] p. 20 et PDF p. 1 (rang-1 LoRA).
4. PDF du candidat 2 présent + empreinte compagnon (deux copies, `eb6d5bbe…`) — `anteriorite-P-041-v2/c3/evade-from-feedback-…` et `docs/sources/pdf/2609.36490v1.pdf`.
5. Candidat 2 dans l'antériorité niveau 2 — `niveau2-v1/anteriorite-v1.md` l. 14, 20, 122, 138.
6. Carte A100 non nommée par le papier, source = dépôt — `erratum-bailey-depot-public-parametres-v1.md`.
7. Chiffres de Bailey lus sur figure = non opposables (R7) — `verification-bailey…` l. 99.
8. Chiffre 96 %/0,040 du candidat 2 opposable — `rapport-lot3-Cc…` [C32] p. 6, [C10] p. 1.
9. Devis test (a) 31/74/75 + carte 40 Go — `devis-…-v1.md` l. 15, 19, 23.
10. État de l'art v1 cite Bailey (l. 134, 154) ; 2609.36490 absent du fichier v1 (recherche plein texte).
11. Description de la sonde de Bailey (perceptron 64 ; ensemble à différence de moyennes ; dernier jeton) — `verification-bailey…` l. 27.
12. Coût-performance SQL sur Gemma-2-2b — `verification-bailey…` l. 84.
13. PDF de StrongREJECT manquant et bloquant — `inventaire-pdf-manquants-v1.md` l. 45, 69.
14. Licence de Bailey jamais relevée + accès GitHub au dépôt refusé à une session — recherche plein texte + `contre-lecture-prereg-malleabilite-v3.md` l. 129, 147.
15. Chiffres de texte de Bailey p. 26 (16 384 pas vs 256 ; 35 % vs 95 %), opposables — `verification-bailey…` l. 83.

**Non vérifiable dans cette session :** la licence du dépôt `LukeBailey181/obfuscated-activations` elle-même (dépôt non présent sur disque, accès non disponible ici) — signalée comme à combler avant le verrouillage du choix (M4).
