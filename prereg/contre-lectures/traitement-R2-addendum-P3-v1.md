# Traitement de la contre-lecture R2 du brouillon 1 de l'addendum de lecture complémentaire de P3, v1

- Rapports traités : `contre-lecture-R2-brouillon1-addendum-P3-v1.md` (23 constats, brouillon 2), puis `verification-corrections-brouillon2-addendum-P3-v1.md` (16 constats) et la relecture externe du brouillon 2 par Gemini (réponse 005, 9 constats), brouillon 3.
- Auteur du traitement : la session (auteur du brouillon). Tous les constats sont acceptés.

| constat | décision | où dans le brouillon 2 |
|---|---|---|
| RA-01 (bloquant) | accepté : A5 réécrit sur la règle réelle de `lire_action` (`_nettoyer` puis `_CLE`, première occurrence non vide, aucune puce) ; comparaison des valeurs, non des positions ; règle « puces et dernière occurrence » gardée en sensibilité descriptive, propre à l'addendum ; erreur de G-05 signalée dans l'hypothèse (à reporter dans le traitement de la relecture de Gemini) | Hypothèse ; Métrique, A5 ; Écarts |
| RA-02 | accepté : lignes 415-416 du texte gelé citées ; nœud posé à Lazar et tranché (N-024 : « Oui, réserves au verdict ») | en-tête ; Critères |
| RA-03 | accepté : gardes de la lecture décisive (`exiger_lecture_sous_prereg`, manifeste décisif, lien, run source, unicité) et d'antériorité (ancêtre) | Liste d'arrêt 2 et 3 |
| RA-04 | accepté : issue et états recalculés par les fonctions gelées et comparés aux valeurs écrites, avant toute analyse | Plan 7 ; Liste d'arrêt 6 |
| RA-05 | accepté : verrou mécanique (`conclusions_etablies`, cible de chaque réserve, clés interdites, `controle_contraire`) | Plan 5 |
| RA-06 | accepté : tranche (tâche, copie) dans les tirages ; deux tâches mixtes et dix paires au moins ; borne basse à 95 % contre le quantile ; « échec » au-delà de 1 % | A4 (b) |
| RA-07 | accepté : estimateur observé = moyenne des 50 différences d'aires ; interdiction écrite de moyenner des scores de fenêtres ; longueur commune `L = min(c, L_cout)` ; bornes des départs, ordre et clés écrits | A2 (b) ; Règles communes |
| RA-08 | accepté : table fermée des niveaux | Règles communes |
| RA-09 | accepté : même population que `cout` ; expression exacte et cas testés ; deux réserves distinctes avec leurs cibles ; `P3-P1_milliers_joints` sans réserve, raison écrite | A6 ; Seuil |
| RA-10 | accepté : formes du coût en descriptif sur les jeux avec saboteur, contrôle par restriction aux actions sans la forme ; condition « aire au-dessus de 0,5 » portée sur la sonde ; corrélations précisées ; longueur en jetons, caractères en descriptif | A7 ; Seuil |
| RA-11 | accepté : lignes lisibles par machine (commit, entropie, empreintes du module et des tests avec marqueurs qui bloquent le scellement tant qu'ils restent) | en-tête |
| RA-12 | accepté : liste fermée des gardes et de leurs tests ; tests hors de `tests/`, chemin explicite, compte écrit | Liste d'arrêt |
| RA-13 | accepté : garde d'alignement des textes | Liste d'arrêt 5 |
| RA-14 | accepté : garde du second passage | Liste d'arrêt 9 |
| RA-15 | accepté : table des signes attendus ; A8 et A9 dans l'hypothèse | Hypothèse ; Prédiction |
| RA-16 | accepté : table de lecture ; audit de symétrie de l'addendum ; multiplicité et taille écrites ; contre-lecture remplie ; requête 004 | Critères ; Plan 8 ; Contre-lecture |
| RA-17 | accepté : nombre de tranches variable rapporté | A4 (a) |
| RA-18 | accepté : populations et segments de A8 définis ; famille « attention » définie et contrôlée | A8 ; Règles communes |
| RA-19 | accepté : seule `GardeArret` donne « échec » ; unité écrite | Liste d'arrêt |
| RA-20 | accepté : section « Écarts à la spécification de Gemini » | Écarts |
| RA-21 | accepté : durée attendue écrite | Plan 9 |
| RA-22 | accepté : référence par `cout_de_tache` ; étiqueteur neuf testé contre `etiquettes_gonflement` | A4 (c) |
| RA-23 | accepté : « réserves sans objet » | Plan 6 ; Critères |

## Vérification des corrections du brouillon 2 (VB-01 à VB-16) et relecture du brouillon 2 par Gemini (GB2-01 à GB2-09)

| constat | décision | où dans le brouillon 3 |
|---|---|---|
| VB-01 (majeur) | accepté : valeur selon `bornes_champs` définie (retrait de `_FERMETURE_GRAS` chaque fois que la clé est en gras fermé après les deux-points, puis `strip`) ; tests des quatre formes | A5 |
| VB-02 (majeur) | accepté : table fermée de `conclusions_etablies` qui suit la hiérarchie de `issue()`, identifiants en chaînes ; test du run « organisme non établi » | Plan 5 ; Liste d'arrêt, tests |
| VB-03 | accepté : `a_au_dessus_de_b` interdit ; sorties gelées versées sans clés interdites ; « sans objet » | Règles communes ; Plan 5 |
| VB-04 | accepté : liste de contrôles par entrée, cible par contrôle ; correspondance jeu → cible de A1 rétablie ; cible de A7 = conclusion du jeu ; A6 et A9 : une entrée | Règles communes ; A1 ; A6 ; A7 ; A9 |
| VB-05 | accepté : entrée décisive en échec ou non calculable → « non lu » ; arrêt seulement pour une clé absente d'une entrée valide | Entrées ; Liste d'arrêt 7 |
| VB-06 | accepté : population et blocs de A4 (b) = tâches mixtes ; test des copies doublées | A4 (b) ; tests |
| VB-07 | accepté : gardes avant le manifeste ; configuration du manifeste ; critères d'une lecture décisive et d'un manifeste d'addendum | Plan 3 et 4 ; Liste d'arrêt 2 et 9 |
| VB-08 | accepté : commit de scellement défini ; dépôt non superficiel exigé (`git fetch --unshallow` au besoin) ; tests sur dépôt jouet | Plan 1 ; Liste d'arrêt 3 |
| VB-09 | accepté : « huit mineurs » ; R-243 corrigée par une ligne nouvelle du registre | Contre-lecture |
| VB-10 | accepté : deux entrées « Contre-lecture k » avec deux empreintes chacune ; marqueurs `<<EMPREINTE_VERIFICATION_B2>>` et `<<NOMBRE_TESTS>>` ; requêtes 004 et 005 | en-tête ; Contre-lecture |
| VB-11 | accepté : `r ∈ {0, …, 49}`, `b ∈ {0, …, 1 999}`, ordre des tirages | A2 (b) ; Règles communes |
| VB-12 | accepté : expression en échappements, points de code nommés, U+2009 ajouté, référence `cout` | A6 |
| VB-13 | accepté : lecture de `reserve_A7_forme_du_cout` écrite ; dix de chaque côté sur le sous-ensemble ; longueur hors de la restriction ; ligne A7 (ii) dans la table des signes | A7 (ii) ; Critères ; Prédiction |
| VB-14 | accepté : liste fermée des gardes et des tests complétée ; trois cas du verrou nommés | Liste d'arrêt, tests |
| VB-15 | accepté : « valeur absolue » | Prédiction ; Seuil |
| VB-16 | accepté : `audit_symetrie_addendum` écrit par le module | Plan 6 ; Critères |
| GB2-01 | accepté : la condition se lit sur la borne basse | Prédiction ; Seuil |
| GB2-02 | accepté : tirage sans paire après recalcul des tranches compté dégénéré | A4 (a) |
| GB2-03 | accepté : `δ̄(b)` moyenne des 50 répliques dans chaque tirage (la réplique unique `b mod 50` gonflait l'intervalle) | A2 (b) |
| GB2-04 | accepté : plancher conjoint `Δ_intra(b)` dans A4 (b) ; paires comptées `Σ n1 × n0` à l'observé | A4 (b) ; Seuil |
| GB2-05 | accepté : marge sans condition sur l'aire de la sonde | A7 (i) |
| GB2-06 | accepté : réserve nommée `reserve_A7_forme_quasi_totale` | A7 (ii) ; Seuil ; Critères |
| GB2-07 | accepté : longueur du champ définie, non définie ailleurs | A7 (iii) |
| GB2-08 | accepté : règle stricte des trois premiers jetons ; part des maxima uniques | A8 |
| GB2-09 | accepté (même point que VB-08) | Liste d'arrêt 3 |

## Relecture externe des ajouts du brouillon 6 par Gemini (GB6-01 à GB6-05, requête 006, non opposable)

Réponse : `canal/gemini`, `brouillons/canal_gemini/inbox_pour_claude/reponse_a_006_relecture_precisions_brouillon6_addendum_P3.md`
(2026-10-20 03:02 UTC). Chaque constat vérifié sur le texte avant décision (R7, R8).

| constat | décision | où dans le texte final |
|---|---|---|
| GB6-01 (majeur) | accepté : critère lexical du manifeste illisible (chaînes nommées, ou moins de 64 octets) ; aujourd'hui, 40 manifestes sous `runs/`, aucun illisible | Liste d'arrêt 16 |
| GB6-02 | refusé : restreindre l'audit de symétrie aux cas où la moitié des contrôles sont lus l'affaiblirait (R4 : un résultat suspect de propreté déclenche le même audit) ; le nombre de contrôles « non lus » est déjà rapporté à côté, et la garde 11 couvre le cas où plus de la moitié des entrées sont en échec | — |
| GB6-03 | accepté pour la garde 13 (« à 1e-9 près ») ; pour la précision 7, le cas `c < L` n'existe pas (`L = min(c, L_cout) ≤ c`, A2) : fenêtre `[c − L, c)` écrite pour lever le doute | Liste d'arrêt 13 ; Précision 7 |
| GB6-04 | accepté : le verrou de fin vérifie les cibles des contrôles lus et des réserves, et l'absence de clés interdites, contre la liste recalculée | Précision 16 |
| GB6-05 | accepté (clarification) : la règle de sensibilité est nommée ; le filtre des actions valides et sans divergence sert à `T2_propre` | Précision 9 |

## Code : contre-lectures du module synthétisé (CB1, CB2, CB3) et décisions de la session

Module relu : `final/complements_p3_v1.py` (`daf95459…`), tests `01b5faea…` (117 tests), face au brouillon 3. Corrections
faites dans une copie neuve (`final-b4/`), décrites constat par constat, avec le test qui prouve chacune, dans les notes de
correction (`prereg/contre-lectures/notes-corrections-code-addendum-P3-v1.md`, table des mutants
`prereg/contre-lectures/table-mutants-code-addendum-P3-v1.md`). Module final et tests : empreintes en tête du
texte ; 165 tests.

| constat | décision | où dans le texte final ; preuve |
|---|---|---|
| CB1-01 (majeur), CB3-01 (majeur) | accepté : fichier des textes découpé sur le seul saut de ligne ; U+2028, U+2029, U+0085 restent dans les textes ; ligne illisible : arrêt, avec son numéro, sans texte | Liste d'arrêt 14 ; test des séparateurs Unicode |
| CB1-02 (majeur) | accepté : recommandation en deux listes, « non robuste aux contrôles de l'addendum » (contrôle contraire) et « non contrôlée par l'addendum » (réserve non lue ou générale), à la lettre des critères gelés, avec les lectures gelées des deux réserves de forme de A7 | Critères de lecture gelés ; tests de la recommandation |
| CB1-03 | accepté : l'audit de symétrie ne compte que les contrôles contraires ; nombre de « non lu » rapporté ; cas « aucune » lu à la lettre (décision de la session) | Critères (audit de symétrie) |
| CB1-04 | accepté : arrêts ajoutés écrits dans la liste fermée (gardes 12 à 16) ; règle du manifeste illisible | Liste d'arrêt 12 à 16 |
| CB1-05 | accepté : silences du texte comblés par le code écrits au texte | Précisions d'application 1 à 15 |
| CB1-06 | accepté : 33 gardes jamais éprouvées ont désormais cas sain et artefact (107 gardes exécutées par la suite) | Liste d'arrêt (R5) ; tests |
| CB1-07, CB3-06 | accepté : aucun cache dans le dossier versé | — |
| CB1-08 | noté (ce qui tient) | — |
| CB3-02 | accepté : garde 10 et localisation contrôlées avant le manifeste | Liste d'arrêt, phrase d'en-tête (gardes 1 à 10 et 12 à 16 avant le manifeste) |
| CB3-03 | accepté : mémoire mesurée (environ 650 Mo) et durée (environ 7 minutes sur un cœur, banc à taille réelle) écrites | Plan d'analyse, point 9 |
| CB3-04 | accepté : graines vérifiées clé par clé | Liste d'arrêt 15 |
| CB3-05 | accepté : dépôt rendu non superficiel avant la lecture décisive (fait) ; garde 3 l'exige | Liste d'arrêt 3 |
| CB2 (revue « verrou et preuves », rapport inachevé ; preuves archivées) : 51 mutants (familles verrou ouvert, cible fausse, niveau changé, moyenne sur les jetons, réserve mal câblée, réserve non lue omise, garde affaiblie, seuil changé), 15 survivants parmi les 20 lancés | accepté : chacun des 51 mutants est tué par un test nommé (table des notes, § 5) ; verrou de fin sur la liste recalculée des conclusions (CB2-06) ; réserve calculée jamais effacée par un échec ultérieur de l'entrée (CB2-09) ; drapeaux bruts recoupés avec la lecture (CB2-11) ; recommandation à la lettre des critères gelés | Précisions 16 à 18 ; Critères |
| Points ouverts de la correction (session) | garde 15 : paramètres de tirage égaux au texte, contrôlés par le point d'entrée en ligne de commande ; précision 18 : `P3-P1.etablie` recoupé avec `calculable` et `bas > 0` ; garde 16 : manifeste hors de forme traité comme illisible ; numéros de garde des messages alignés sur le texte | Liste d'arrêt 15 et 16 ; Précision 18 |

## Relecture externe du module final par Gemini (requête 007, non opposable)

Réponse : `canal/gemini`, `brouillons/canal_gemini/inbox_pour_claude/reponse_a_007_relecture_module_final_addendum_P3.md`
(2026-10-20 05:03 UTC), sur le module `2b16179d…` : « bon pour scellement tel quel », un constat pour information (GM-01 :
message de la garde 3 sur une altération du préenregistrement après scellement ; aucun artefact ne passe). **Aucun poids
donné à cette relecture** : ses renvois de ligne ne correspondent pas au fichier relu (par exemple `conclusions_etablies`
citée l. 351-361, en réalité l. 564 ; `exiger_verrou` l. 934, en réalité l. 1868 ; `charger_textes` l. 975, en réalité
l. 2164 ; `creer_manifeste` l. 1018, en réalité l. 2224) ; ses « RAS » ne sont donc pas vérifiables (R7, R8). GM-01 : noté,
sans changement.

## Vérification finale du module (VF1, VF2, VF3) : trois sous-agents neufs, module `2b16179d…`, texte `411eb334…` (brouillon 6)

Verdicts : texte face au code (VF1) « scellable après corrections » ; mutants et pannes (VF2) « scellable après
corrections » ; calculs refaits et verrou par propriétés (VF3) « scellable après corrections ». Aucun défaut du module :
calculs exacts à 1,1e-16 (1 114 comparaisons), verrou sans violation (281 lectures, 5 000 synthèses, 150 sorties
altérées), 51 mutants de CB2 tués, sortie identique octet pour octet entre processus et entre dépôts. Toutes les
corrections portent sur le texte (brouillon 7) et sur les tests ; le module ne change pas.

| constat | décision | où |
|---|---|---|
| VF1-01, VF2-03, VF3-01 (précision 17 : « non lu » d'entrée entière même après tous les contrôles) | accepté, texte : la précision 17 écrit ce que fait le module (sens prudent : une réserve en plus, jamais en moins) ; le module n'est pas changé (une nouvelle empreinte rouvrirait la vérification) | Précision 17 |
| VF1-02 (graines de la garde 15 contrôlées après la création du manifeste) | accepté, texte : exception écrite au plan (point 3), à l'en-tête de la liste d'arrêt et à la garde 15 ; sans effet au réel (le manifeste dérive ses graines par la même fonction) | Plan 3 ; Liste d'arrêt ; garde 15 |
| VF1-03 (précision 8 et cas « aucune ») | accepté, texte | Précision 8 |
| VF1-04 (garde 12 : aire vectorisée du module) | accepté, texte | Garde 12 |
| VF1-05 (banc : chemin et empreinte, module mesuré) | accepté : rapport CB3, `essai_07.log` (`063661ac…`) et `essai_07b_import.log` (`baaf517e…`) cités et versés ; module mesuré nommé (`daf95459…`) | Plan 9 ; versement |
| VF1-06 (liste des tests, gardes 12 à 16) | accepté, texte | Liste d'arrêt, tests |
| VF1-07 (garde 15 : forme `…-addendum-p3`, préenregistrement de la commande) | accepté, texte | Garde 15 |
| VF1-08 (« ce brouillon 3 », requêtes 006 et 007, titre) | accepté, texte | Contre-lecture ; titre |
| VF1-09, VF2-08, VF3-05 (texte cité par les notes `77bc2fe0…`) | établi par reconstruction : `77bc2fe0…` est `411eb334…` sans le troisième vérificateur dans l'entrée « Contre-lecture 4 » (deux sous-agents au lieu de trois) ; aucune règle ne diffère. Le texte scellé est le brouillon 7, marqueurs remplis | ce traitement |
| VF1-10 (précision 15, intervalles du module) | accepté, texte | Précision 15 |
| VF1-11 (référence construite après le manifeste, hors du `try`) | noté, sans changement : inatteignable (fichier vérifié juste avant) ; changer le module rouvrirait la vérification | — |
| VF1-12, VF2-09 (règles du code non écrites ; motif « garde 4 » d'une ligne illisible) | accepté, texte : ligne exactement vide ignorée, ligne d'espaces illisible, motif « garde 4 » écrit à la garde 14 ; le reste noté | Garde 14 |
| VF2-01, VF2-02, VF2-04, VF2-05, VF2-06 (8 mutants neufs survivants : M09 à M14, M19, M24) | accepté, tests seulement : un artefact ou un cas sain de plus par mutant, chacun prouvé sur sa copie mutée ; le module ne change pas | tests ; notes § 3 ter |
| VF2-07, VF2-10, VF3-04, VF3-06 | notés | — |
| VF3-02 (liste fermée des clés de graines) | accepté, texte : 69 clés nommées | Précision 12 |
| VF3-03 (conventions de tirage) | accepté, texte | Précision 12 |

## Contre-lecture 5, partie A : brouillon 7 face au brouillon 6 (VB7-01 à VB7-07)

Rapport : `prereg/contre-lectures/verification-corrections-brouillon7-addendum-P3-v1.md` (partie A, « scellable après
corrections » ; la partie B, sur le brouillon 8 et les tests corrigés, est dans le même rapport). Les corrections vont au
brouillon 8 ; le brouillon 7 relu (`c3e9c27f…`) reste tel quel (R12).

| constat | décision | où dans le texte final |
|---|---|---|
| VB7-01 (précision 17 : « entrée en échec » couvre aussi un calcul en échec) | accepté : la précision 17 vise la `GardeArret` levée hors d'un calcul ; un calcul en échec rend « non lu » le seul contrôle qui en dépend ; effet sur l'audit de symétrie et double mention au verdict écrits | Précision 17 |
| VB7-02 (« Contre-lecture 4 » : brouillon relu non cité) | accepté : « relu face au brouillon 6 (`411eb334…`) » | Contre-lecture 4 |
| VB7-03 (procédure : brouillon 8, empreintes citées, outils, copies des tests) | accepté : brouillon 8 ; l'entrée 5 cite le brouillon 7 relu et le brouillon 8 ; remplisseur et versement adaptés (brouillons 1 à 8) ; version des tests relue par la vérification finale gardée sous un nom versionné (`test_complements_p3_v1-7605c205.py`) | Contre-lecture 5 ; outils |
| VB7-04 (`<jeu>` de A7 en mots ; portée de « Tirages comme `intervalle_blocs` ») | accepté : identifiants `saboteur-honnete`, `saboteur-temoin`, `saboteur-mention` ; « tirages propres au module » | Précision 12 |
| VB7-05 (garde 15 : le code dépasse un peu la lettre, sans effet) | accepté en partie : « forme exacte du plan, point 2 » écrit ; le reste noté (module figé) | Garde 15 |
| VB7-06 (date et auteur de l'en-tête) | accepté : date = commit de scellement, rédaction du 2026-10-19 au 2026-10-20 ; contre-lectures renvoyées à leur section | En-tête |
| VB7-07 (précision 1 et la fenêtre de VF1-11) | accepté : exception écrite | Précision 1 |

## Contre-lecture 5, partie B : brouillon 8 et tests corrigés (VB7-08, VB7-09)

Verdict global du rapport (parties A et B) : « scellable », pour le brouillon 8 (`bde1b243…`) une fois rempli, les tests
`7387910d…` (165 tests ; six tests étendus, aucun retiré ni affaibli ; les huit mutants de VF2 tués, chacun par son
artefact ou son cas sain neuf) et le module `2b16179d…`, inchangé. Suite complète lancée par le correcteur sur ces
fichiers : `165 passed in 1049.77s` (notes de correction, § 6).

| constat | décision | où |
|---|---|---|
| VB7-08 (précision 17 : « le seul contrôle » ; un calcul en échec peut rendre « non lus » zéro, un ou deux contrôles) | noté, sans correction : le sens est clair et l'écart ne joue que dans le sens prudent ; un calcul en échec rend « non lus » les contrôles qui en dépendent | — |
| VB7-09 (remplisseur : empreintes relues non comparées ; nombre de tests à la main ; traitement et rapport à achever avant de remplir) | accepté : le remplisseur exige les empreintes relues du brouillon 8, des tests et du module, et 165 tests ; traitement et rapport achevés avant le remplissage | outil de remplissage |
