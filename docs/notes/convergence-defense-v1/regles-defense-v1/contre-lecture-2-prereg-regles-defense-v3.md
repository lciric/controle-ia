# Contre-lecture 2 (R2, courte) — brouillon 3 du préenregistrement « quatre règles de mise à jour de la défense » — v2

- Contre-lecteur : sous-agent neuf, modèle Claude Fable 5.1 (`claude-fable-5-1`) ; n'a écrit ni les brouillons 1 à 3, ni le code v1 ou v2, ni les essais, ni le gel, ni la contre-lecture 1.
- Date (`date -u`) : dimanche 1er novembre 2026, début de lecture 15:42:41 UTC (temps universel coordonné), fin ≈ 15:52 UTC.
- Rien modifié, rien scellé, rien commité ; aucun appel réseau ni payant ; aucune racine de décision employée ; rien lu sous `donnees/` hors `argon-seul-convergence-v1/`. Exécutions sur processeur seulement : les 25 essais `pytest` du code v2, le validateur `controle_ia.prereg.problemes`, la garde `exiger_identite_prereg_regles` du code v2 sur le texte du brouillon 3, `git show` sur le commit cité.

## Empreintes sha256 recalculées

| Fichier (dossier `regles-defense-v1/`) | sha256 |
|---|---|
| `brouillon-prereg-regles-defense-v3.md` (brouillon relu) | `7862c944458425f096bfb926ebea3aa2abddee91d03afeb997a5d23b85c946b8` |
| `brouillon-prereg-regles-defense-v2.md` | `9629fa1e307934d6ae908841ab0675fc0c486ac2228a9196dbb3bae1c40eac97` |
| `arene_regles_defense_v2.py` | `9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3` |
| `test_arene_regles_defense_v2.py` | `78d979ab76bbe4b3ad6b55be77bf2b745a4457940eb9cb4c16a3ee87ef324b81` |
| `gel-regles-defense-v2.md` | `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` |
| `contre-lecture-prereg-regles-defense-v1.md` | `19ca1e283b579acadd4a91453e5d5268984f2aaabdea055e127d4de5a6938495` |

Toutes coïncident avec celles citées dans le brouillon 3 (lignes 3, 5, 15 à 19, 27 à 29) et dans le LISEZMOI v2. Le commit `ed3377bd` cité ligne 12 existe (1er novembre 2026, 11:04:31 UTC) et le code qu'il contient a bien l'empreinte `9f0dcf5e…` (`git show` recalculé).

## Verdict en une phrase

**Scellable après corrections mineures** : le brouillon 3 est le brouillon 2 plus les reports des décisions de Lazar, sans changement de fond ; les seuils sont cohérents entre eux et avec le code ; identité, essais et validateur passent ; il manque une phrase de déclaration (CL2-01) sur deux indications du pilote v2 de signe contraire à P13 et P14, à écrire dans la version suivante avec l'entrée « Contre-lecture 2 » (laquelle ne peut pas être écrite dans le fichier v3, déjà empreinté et commité : CL2-04).

## Points vérifiés (1) à (8)

**(1) Constats CL-01 à CL-16.** Tous traités comme la table des lignes 380 à 398 le dit ; vérifié dans le texte : CL-01 → HR1 par la Table A seule (ligne 146), déclencheur 1 sur ses lignes 5 et 6 (ligne 265) ; CL-02 → verdict de HR2 par la Table B′, « ? » ou « R2 ≳ R1 » = non tranchée (lignes 147, 311) ; CL-03 → HR3 en classes B8 et E8 (lignes 148, 298) ; CL-04 → Table D en cinq lignes (328 à 334), S15 défini (225) ; CL-05 → X̄ au § Métrique (186), Table B′ (300 à 311), réserve de parité (135), essai lent dans la liste d'arrêt (362) ; CL-06 → paragraphe « Déclaré (CL-06) » (174) ; CL-07 → grille retirée, cinq variantes fixées (251 ; `REGLES`, code ligne 130 ; commande `decision` à un seul λ, lignes 776 et 828 à 830) ; CL-08 → `exiger_gel_regles(RACINES_DECISION)` après l'autorisation (code, 818) et V0 (263) ; CL-09 → déployés / stockés (125, 190) ; CL-10 → R1 sans la cible (235) ; CL-11 → `cos_consecutif_par_tache` (code, 618) et écart « standard seul / renforcé seul » (code, 664 à 668) ; CL-12 → vocabulaire de la borne (134) ; CL-13 → saturation de I3 (191, 336) ; CL-14 → « puis « dernier » » (211) ; CL-15 → cinq familles, B8 exacte pour 8 tests (201, 248) ; CL-16 → rien à faire.

**(2) Diff v2 → v3.** Sept blocs (lignes 1 à 16, 110 à 118, 123 à 131, 192 à 228, 246 à 257, 367 à 375, 400 à 403 du v3) : titre, note de version, statut, paragraphe de décision, auteur, date, commit, réglages de R4, Résumé 5 et 7, en-tête du § Seuil, S1 à S15, Plan 5 points (2) et (5), Historique point 7, Rôles, entrée « Contre-lecture 2 ». **Aucune ligne des sections Hypothèse, Prédiction, Métrique, Critères de lecture gelés (Tables A à E, V0, déclencheurs) ni Liste d'arrêt n'est touchée** ; le bloc d'identité (lignes 24 à 118) est identique au brouillon 2. Pour S1 à S15, chaque valeur retenue est égale à la recommandation conservée sous elle.

**(3) Seuils, entre eux et avec le code.** Configuration canonique (lignes 36 à 109) : `T` 8, `n_instances` 100, `deltas` (1,4 ; 1,6), `alpha` 0,01, `entrainement` « detection », plafond 600 s ; `v4.CONFIG_V4` chargée par le code rend les mêmes valeurs et la même empreinte `3fbb27fc…`. λ* = 0,3 et « moyenne » : bloc sous l'identité (114, 115), S6 (211), commande du Plan 5 ; m = 0,02 = S5 = S15 (199, 207, 225) ; S12 = 0,999 appliqué par le lecteur sur `cos_consecutif_par_tache` (aucun seuil dans le code, conforme à CL-11) ; `timeout 3600` = deux fois la projection de 30 minutes (129, 213, 252 ; recalculée : 17,3 s × 200 = 58 min de processeur, 30 min de mur à l'efficacité 0,96) ; cinq variantes = `REGLES` du code, codes de graine 20, 21, 1, 2, 24 (ligne 120 ; code, 130 et 131). Clé de rééchantillonnage de X̄ : 1000 + rang, hors des plages 200 à 402 et 500 à 799 (code, 593 et 594, assertion).

**(4) Bloc d'identité.** `exiger_identite_prereg_regles(texte_v3, v4.CONFIG_V4, "0:100", 0.3, "moyenne")` passe ; les artefacts λ = 1, référence « dernier », `--instances 0:50` sont refusés avec les motifs attendus ; `bloc_identite(v4.CONFIG_V4)` régénéré est identique, caractère pour caractère, au bloc des lignes 26 à 112.

**(5) Essais.** `pytest -q test_arene_regles_defense_v2.py` : 24 passés, 1 sauté (essai lent, `REGLES_ESSAIS_LENTS=1`), 14,8 s ; deux avertissements numpy bénins dans `test_X_barre_egale_X1_quand_T_vaut_1`.

**(6) Aucune prédiction tirée des pilotes.** Déclarations présentes : signe contraire du pilote v1 pour P2 et P5, coïncidences de P12 et de P6, indice contraire de P13 (lignes 150, 174, 271). Comparaison de P12 à P15 aux tables du pilote v2 (`pilote-essai-regles-defense-v2.md`, lignes 58 à 62, 97 à 101) : D̄(R1, R2) +0,013 ; +0,004 (P12 ≥ +0,02 : non recopié) ; Δ(R0, R2) sur V +0,029 ; −0,002 (P13 ≤ −0,02 : non recopié, **signe contraire au δ 1,4**) ; D̄(R0, R2) −0,006 ; −0,006 (P14 D̄ > 0 : non recopié, **signe contraire aux deux δ**) ; D̄(R3, R2) −0,055 ; −0,078 et D̄(R4, R2) −0,012 ; −0,010 (P15 : signes compatibles, ordres de grandeur non recopiés). Rien n'est recopié ; deux indications contraires ne sont pas déclarées (CL2-01).

**(7) Liste d'arrêt et critères.** Gelés et exécutables : V0 est une conjonction de faits vérifiables (263) ; Tables A, C, D lues de haut en bas, première ligne vraie (260) ; Tables B et B′ à classes ordonnées (la lecture de haut en bas lève le chevauchement entre « R_k > R2 » et « R_k ≳ R2 ») ; chaque déclencheur nomme son effet bloquant ; chaque ligne de la liste d'arrêt nomme garde et essai (346 à 367), les trois dernières étant des règles de conduite déclarées sans garde logicielle.

**(8) Validateur.** `controle_ia.prereg.problemes` sur le v3 rend une seule ligne : « section vide ou à remplir : Contre-lecture » (l'entrée « Contre-lecture 2 »). Aucun autre marqueur ; l'entrée « Contre-lecture 1 » porte ses deux empreintes.

## Constats

**CL2-01 (mineur, une phrase à ajouter) — indications contraires du pilote v2 non déclarées pour P13 et P14.** La ligne 174 déclare les indications du pilote v1 et dit que l'auteur a vu les tables du pilote v2 sans en tirer de prédiction, ce que je confirme ; mais le pilote v1 ne contient pas R0, et le pilote v2 (2 instances par δ, non opposable) indique Δ(R0, R2) sur V = +0,029 ; −0,002 et D̄(R0, R2) sur X̄ = −0,006 ; −0,006, signes contraires de P13 (δ 1,4) et de P14. Par la logique de CL-06 (le lecteur R13 doit pouvoir appliquer le déclencheur 7 dans les deux sens), il faut le déclarer. *Correction*, à la fin du paragraphe « Déclaré (CL-06) » : « Le pilote d'essai v2 (2 instances par δ, racine d'essai, non opposable, seul pilote où R0 existe) indique Δ(R0, R2) sur V +0,029 ; −0,002 et D̄(R0, R2) sur X̄ −0,006 ; −0,006, soit le signe contraire de P13 au δ 1,4 et de P14 aux deux δ ; P13 et P14 sont maintenues par principe ; une confirmation de P13 ou de P14 à la décision serait donc aussi une surprise au vu de ce pilote et relève du déclencheur 7. » Aucune hypothèse, prédiction ni table ne change.

**CL2-02 (forme) — citation de R-962 reconstruite.** Les lignes 3, 5 et 197 citent entre guillemets « Recommandation (b), confiance 0,7 ; défaut (b) sous 48 h : go ; go tout » ; le registre (R-962) porte « Recommandation (b) … : go ; go tout go ligne N » et, en point (4), « seuils S1 à S15 pris aux valeurs recommandées du brouillon 2 ». Même fond ; la citation mêle les mots de Lazar et ceux de la proposition soumise. *Correction facultative* : citer le registre tel quel ou retirer les guillemets.

**CL2-03 (forme) — restes du brouillon 2.** « ce brouillon 2 » (lignes 371, 378), « recommandation S8 : `timeout 3600` » (129, 252) alors que S8 est retenu. Sans effet ; à corriger dans la version suivante.

**CL2-04 (procédure, information) — le v3 est déjà commité avec son empreinte compagnon** (`.sha256`, commit `70885449`, 15:42:59 UTC, « scellé ; R-963 », un instant après le début de cette lecture). « Scellé » désigne l'empreinte compagnon (R6), non `sceller_prereg`, que le validateur refuserait tant que l'entrée « Contre-lecture 2 » est à remplir. Conséquence (R12) : cette entrée et la phrase CL2-01 s'écrivent dans un fichier nouveau (brouillon 4 ou préenregistrement final sous `prereg/`), jamais dans le v3 ; le bloc d'identité y est à recopier au caractère près et la garde d'identité à relancer sur ce fichier avant scellement.

**CL2-05 (information, hors du préenregistrement).** L'en-tête des tables de contrastes du pilote v2 (lignes 56 et 95) dit « n = 6 », hérité du script de résumé v1, alors que le pilote v2 compte 2 instances par δ ; le brouillon 3 dit correctement « 2 instances par δ ». Fichier déjà empreinté : à noter, rien à changer.

## Ligne pour l'entrée « Contre-lecture 2 »

Bloquant : aucun. Mineur : CL2-01. Forme : CL2-02, CL2-03. Information : CL2-04, CL2-05. Ligne à écrire dans la version suivante (`<empreinte du rapport>` = sha256 de ce fichier, recalculée après son écriture et donnée dans le compte rendu de cette contre-lecture) :

- **Contre-lecture 2** (courte, R2) — sous-agent neuf (modèle Claude Fable 5.1, `claude-fable-5-1`), 1er novembre 2026, 15:42 à ≈ 15:52 UTC ; brouillon relu : `brouillon-prereg-regles-defense-v3.md`, empreinte `7862c944458425f096bfb926ebea3aa2abddee91d03afeb997a5d23b85c946b8` ; rapport : `docs/notes/convergence-defense-v1/regles-defense-v1/contre-lecture-2-prereg-regles-defense-v3.md`, empreinte `<empreinte du rapport>` ; verdict « scellable après corrections mineures » ; traitement : CL2-01 (indications contraires du pilote v2 pour P13 et P14) : accepté, phrase ajoutée au paragraphe « Déclaré (CL-06) » du § Prédiction ; CL2-02 (citation de R-962) et CL2-03 (restes « brouillon 2 », « recommandation S8 ») : forme, acceptés ; CL2-04 (entrée écrite dans une version nouvelle, R12) et CL2-05 (« n = 6 » du pilote v2) : information, rien à changer.
