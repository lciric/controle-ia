# Registre des affirmations — « Le programme expliqué depuis zéro » — v1

Document : `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v1.html`. Une ligne par chiffre ou fait vérifiable.
Empreintes recalculées par le rédacteur le 10 novembre 2026 (relevé `date -u` : 2026-11-10 09:48:55 UTC), douze premiers caractères ;
complètes au journal. « Vivant » : registre modifié dans la journée, cité à l'empreinte lue.

| id | phrase (abrégée) | valeur | source | empreinte | ligne ou section |
|---|---|---|---|---|---|
| A01 | agent Llama-3.1-8B-Instruct | 8 milliards | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 14 |
| A02 | épisode de dix actions, un agent | N = 1, T = 10 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Plan d'analyse, point 2 |
| A03 | seuil de fausses alertes de référence | 1 % | docs/decisions/decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 1, § 2 |
| A04 | couches lues 7, 15, 23 sur 32 | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Hypothèse, hypothèses de travail |
| A05 | vecteur de 4 096 nombres par jeton | 4 096 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Plan d'analyse, point 5 (« × 4 096 ») |
| A06 | consigne privée : ≈ 3 fois l'estimation honnête | ≈ 3 | docs/verdicts/verdict-P3-premier-test-i-a-v2.md | 05e896daed17 | En tête, réserve B1 |
| A07 | facteur ≈ 33 | 10^1,5227 ≈ 33,3 (calcul) | docs/verdicts/verdict-P3-premier-test-i-a-v2.md | 05e896daed17 | En tête, P3-P1 |
| A08 | δ = 0,5 σ : une action dépasse le seuil 3,4 % ; maximum 3,9 % ; somme 88,7 % | 0,0339 ; 0,0393 ; 0,8867 | sortie du script (journal) | voir journal | partie A, m = 100 |
| A09 | forme du processus e unilatéral, inégalité de Ville | formule | docs/notes/note-mathematique-lemme-theoreme-v3.md | dfe4fe0fc4d0 | § 2 |
| A10 | L1, L2, L3 (a)–(d), L4, L5 | énoncés | note v3 ; docs/decisions/decision-N-003-N-004-v1.md | dfe4fe0fc4d0 ; cc1be39369bc | note § 3 ; décision § 2 |
| A11 | « la puissance ne dépend que de B et de la variance » (programme) | citation | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 56 |
| A12 | budget total borné = choix de modélisation déclaré | — | docs/decisions/decision-P-008-v1.md | ac9551b044c1 | § 2 |
| A13 | L4 non testé en simulation | — | note v3 ; resultats-T0.3 | dfe4fe0fc4d0 ; 9ab618edae17 | § 7 ; « Lecture des énoncés » 1 |
| A14 | preuves contre-vérifiées par un sous-agent neuf | — | note v3 | dfe4fe0fc4d0 | en-tête |
| A15 | lemme dit « candidat » au programme | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 54 |
| A16 | énoncé du théorème du programme, citation | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 62 |
| A17 | T1–T4, classes C et K, Slepian | énoncés | note v3 ; decision-N-003-N-004-v1.md | dfe4fe0fc4d0 ; cc1be39369bc | note § 4 ; décision § 1 |
| A18 | hypothèse pivot δ > 0, deux issues publiables | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 64 |
| A19 | T0.3 : 31/31 ; 342 et 544 cellules ; 0 contraire ; audit non déclenché | 31 ; 342 ; 544 ; 0 | docs/notes/resultats-T0.3-v1.md | 9ab618edae17 | Prononcé |
| A20 | T0.3 sans verdict de lecteur neuf | — | brouillons/entretien-taif-v3/socle-preuves-entretien-v1.md | b8a97629e837 | § 1.2 « chiffres exacts » ; § 6 manque 7 |
| A21 | calendrier : 1,000 / 0,160 / 0,158 (n0 = 200, B = 25, m = 10) | — | resultats-T0.3-v1.md | 9ab618edae17 | Magnitudes, 1 |
| A22 | e cumulé 0,09–0,25 ; Page 0,57–1,00 | — | resultats-T0.3-v1.md | 9ab618edae17 | Magnitudes, 2 |
| A23 | 2606.10456 : somme 0,253 (φ1 = 0,9) ; maximum 0,027 ; vraie et pessimiste pour le maximum | 0,253 ; 0,027 | resultats-T0.3-v1.md ; note v3 | 9ab618edae17 ; dfe4fe0fc4d0 | Magnitudes, 4 ; note § 4 |
| A24 | candidature : « its central statement does not hold for its own construction » | citation | docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt | b2458c2d109a | l. 87-88 |
| A25 | Ville sous effet épisode : 0,21 ; 0,35 ; calibrage conforme 0,046–0,055 sur 17 réglages | — | resultats-T0.3-v1.md | 9ab618edae17 | Magnitudes, 6 |
| A26 | exemple chiffré : toutes les valeurs des deux tables, 0,32 %, 0,971, 0,591, 0,886, 8,9 %, 0,93 % | voir sortie | docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v1.py, sortie au journal | ee221d75738a | parties A et B |
| A27 | trois papiers, problèmes, thèses | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 2 |
| A28 | probabilités d'originalité (0,55 ; 0,50 ; 0,75 ; 0,66 ; 0,40 ; 0,75 ; 0,65 ; 0,15 ; 0,70 ; 0,55 ; 0,85 ; 0,60 ; 0,80 ; 0,45 ; 0,30 ; 0,70 ; 0,68) | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 5, l. 93-114 |
| A29 | révisions : L ≈ 0,4 ; HC1 0,4–0,5 ; H2 ≈ 0,35 ; HC3 ≈ 0,35 | — | N-003-N-004 ; N-005-N-006 ; N-007-N-008 ; N-013 | cc1be39369bc ; cd49afbc924c ; ab7dc9bb2c96 ; 157d388ef5d0 | sections « Originalité » |
| A30 | H1a porte la revendication ; H1b information | — | docs/decisions/decision-N-055-v1.md | 371879d5bd44 | Nœud H1b |
| A31 | G1 par mode ; « coût » seul ne porte pas H1 | — | docs/decisions/decision-N-054-v1.md | c8a00b3f885a | points 2 et 3 |
| A32 | gain dans chaque mode, tenu à l'écart compris ; bases (ii) et (iii) | — | docs/decisions/decision-N-056-v1.md | 3592c1e977e8 | points 1 et 4 |
| A33 | contre-résultat 2512.07810 p. 17 | — | docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md | bbe0c1f523ad | § 1, point 4 (H1) |
| A34 | H2 énoncé retenu ; Doomed 2607.06503, E-valuator 2512.03109 | — | decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 1 |
| A35 | réserve « dérive de l'honnête sous revers » | — | docs/decisions/decision-N-034-v1.md | 97e33e971a8f | § 2 |
| A36 | L occupé en partie 2608.02698 p. 5 ; T moitié négative 2607.11751 | — | note v3 | dfe4fe0fc4d0 | § 8 |
| A37 | H6 énoncé retenu (trois interventions) ; 2412.01784 ; Poser 2405.05466 | — | docs/decisions/decision-N-015-v1.md ; N-013 | 462785b33310 ; 157d388ef5d0 | § 1 ; § 6 |
| A38 | H8 devient diagnostic | — | docs/decisions/decision-N-062-v1.md | 63f426903e6d | point 2 |
| A39 | H8 prémisse en partie occupée 2605.27958 | — | etat-de-l-art niveau 2 | bbe0c1f523ad | § 1, point 3 (H8) |
| A40 | conscience d'évaluation du dispositif avant H8 | — | docs/decisions/decision-N-053-v1.md | 2204256d7442 | point 3 |
| A41 | loi Δv = g·(ĉ − v0), prédictions 1–4, cinq familles | — | docs/decisions/decision-N-005-N-006-v1.md | cd49afbc924c | § 1 |
| A42 | probabilité du jeton retirée des pièces revendiquées | — | decision-N-013-v1.md | 157d388ef5d0 | § 1 |
| A43 | Where Empathy Goes Wrong cité | — | docs/decisions/decision-N-023-v1.md | 1297f509a0fc | § 1 |
| A44 | Panin non lu, papier C non scellé avant | — | decision-N-005-N-006-v1.md | cd49afbc924c | § 2, réserves |
| A45 | HC2b renommée ; HC3, HC4, HC5 énoncés retenus | — | decision-N-013-v1.md | 157d388ef5d0 | § 2 à § 5 |
| A46 | sondes du lecteur déplacées 2511.00554, 2601.11516 | — | decision-N-013-v1.md | 157d388ef5d0 | § 8 |
| A47 | porte GC réécrite | — | decision-N-005-N-006-v1.md | cd49afbc924c | § 2 |
| A48 | H3 : 2607.07368 | — | etat-de-l-art niveau 2 | bbe0c1f523ad | § 1, point 3 (H3) |
| A49 | H9 ; antériorité non vérifiée ; papier B hors des sept mois | — | docs/decisions/decision-N-035-v1.md | 55df073d6918 | § 2, § 3 |
| A50 | Terekhov et al. reconstruit, sans code ni données | — | decision-P-008-v1.md | ac9551b044c1 | § 3 |
| A51 | 96 articles : 64 évaluation, 32 réserve | 96 ; 64 ; 32 | registres/etat.md | 096d57c18cba (vivant) | tâche T0.5 |
| A52 | pilote : coût seul retenu, accord 0,04 à 0,17 pour 0,6, juges en nœud | — | docs/verdicts/verdict-T0.5-pilote-v1.md | b9a072302d65 | § 1 |
| A53 | adaptateur rang 16 ; doses 0,25–1 ; dose 0 = base au bit près | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Plan, point 3 ; Hypothèse |
| A54 | (ii-b) conçu, contre-lu une fois, ni code ni GO | — | rapport v3 du 10 novembre ; registres/etat.md | 7d610de18c82 ; 096d57c18cba | § 4 ; en-tête 9 nov. 21:17 (« P-066 → (b) ») |
| A55 | famille (iv) sur devis | — | decision-N-053-v1.md | 2204256d7442 | point 2 |
| A56 | prédiction de validité | — | docs/programme-controle-ia-v2.md ; N-053 | 2fd63badb5af ; 2204256d7442 | § 7 ; point 2 |
| A57 | « diffus » défini comme mesure | — | P-066 ; N-007 | 012ddc44baca ; ab7dc9bb2c96 | « Les faits » 3 ; § 1 |
| A58 | familles et concepts de sondes | — | docs/brief-claude-code-programme-complet-v2.md | 9261932a11f2 | T0.7 |
| A59 | jamais moyenne ; bras de diagnostic permis | — | docs/decisions/decision-N-026-v1.md | 85bd40235f36 | § 1 |
| A60 | plancher : 200 directions, quantile 0,95, borne basse stricte | 200 ; 0,95 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Métrique |
| A61 | juge par action, juge 3B, TRACE-lite, accumulation boîte noire | — | brief v2 T0.8 ; programme § 8.3 ; registres/etat.md | 9261932a11f2 ; 2fd63badb5af | T0.8 |
| A62 | prédicteur sur traits du texte ; aire 0,8878 | 0,8878 | docs/decisions/decision-N-029-v1.md | 084e30523c0a | § 1, point 2 |
| A63 | base « mots et coût » ; seuil 0,70 ; gain + 0,05 | 0,70 ; 0,05 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Règle « mots et coût » |
| A64 | préenregistrement de T0.8 inexistant | — | socle de preuves | b8a97629e837 | § 6, manque 4 |
| A65 | invariants de protocole ; invariant N-053 | — | programme § 9 ; N-053 | 2fd63badb5af ; 2204256d7442 | § 9 ; point 5 |
| A66 | oracle « affaiblir les contrôles », non construit | — | docs/decisions/decision-N-060-v3.md ; P-066 | 2b448f696503 ; 012ddc44baca | § 1–3 ; « Les faits » 4 |
| A67 | relecteurs d'une même famille | — | candidature | b2458c2d109a | l. 257-258 |
| A68 | G0 huit critères | — | brief v2 | 9261932a11f2 | Porte G0 |
| A69 | G0 fin novembre ; report au 31 janvier 2027, mot relayé | — | registres/decisions.md | aa5a9e66e5a3 (vivant) | N-027 l. 462 ; R-749 l. 977 |
| A70 | critère 3 jugé aux doses où la base échoue | — | docs/decisions/decision-N-063-v2.md | b2d9f0354380 | points 1-2 |
| A71 | critères 1 et 5 prouvés, aucune porte franchie | — | registres/etat.md | 096d57c18cba | Derniers verdicts de porte |
| A72 | G1 : bras F1 retiré ; planchers rapportés | — | decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 2 |
| A73 | G1 : le pari décide, rééchantillonnage rapporté | — | decision-N-055-v1.md ; CLAUDE.md (confirmé le 28 octobre) | 371879d5bd44 | D-S11 |
| A74 | G1 fin M2 (programme) ; fin du mois 4 (candidature) | — | programme ; candidature | 2fd63badb5af ; b2458c2d109a | § 10 ; l. 157 |
| A75 | N-062 : reconception, sans borne, famille neuve, tout rapporté | — | decision-N-062-v1.md | 63f426903e6d | points 1-6 |
| A76 | bascules | — | programme § 13 ; N-062 | 2fd63badb5af ; 63f426903e6d | § 13 ; point 6 |
| A77 | bras d'attaque : deux bras, cloisons | — | decision-N-056-v1.md ; N-054 | 3592c1e977e8 ; c8a00b3f885a | points 6-7 ; point 3 |
| A78 | lancement décidé le 10 novembre, rien n'a tourné | — | message de la session mère (relais), 10 novembre ; non vérifié dans main | — | — |
| A79 | classifieur de sûreté le 27 octobre, sans contournement | — | registres/decisions.md | aa5a9e66e5a3 (vivant) | R-597 l. 823 |
| A80 | pince : définition, hypothèse, dans aucun préenregistrement | — | brouillons/entretien-taif-v3/consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md | 5609fc655b5e | § 1 |
| A81 | juge O2 énoncé retenu ; citations obligatoires | — | docs/decisions/decision-N-064-v1.md | 387c9d4eda5a | points 2-4 |
| A82 | rôles 1, 2 adoptés ; 3 à trancher | — | docs/decisions/decision-N-065-v1.md | f820e90da092 | points 1-3 |
| A83 | composition jugée sur l'oracle et le coût | — | docs/decisions/decision-N-058-v1.md | 854f2724864f | point 1 |
| A84 | tâches fraîches ; test_final lu une fois ; contre-lecteur | — | N-049 ; N-050 ; N-052 | 8a5bf5e57e2b ; a54b128df955 ; 817d218b22b8 | — |
| A85 | objectif ultime ; régimes en attente ; composition apprise, coût, héritage | — | N-044 ; N-045 v2 | 2b70bdac014d ; c7b05e39de38 | Énoncés retenus |
| A86 | A1-v4 : W2 1/24 [0,0074 ; 0,2024] ; v8 24/24 ; W2g 10/24 [0,2447 ; 0,6117] ; r = 10/17 ; 8/11 ; lecture bornée ; réserves | — | docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md | e6e2f17076fa | § 2, § 3, § 4 |
| A87 | se rapporte avec A1-v3 ; absent de la candidature | — | socle de preuves | b8a97629e837 | § 2.4 ; § 1.1 |
| A88 | état de l'art : 13 et 98 PDF ; 24 rapports ; 3 497 citations ; 0 échec ; 147 lignes | — | etat-de-l-art niveau 2 ; niveau 1 | bbe0c1f523ad ; b0b519fe250a | Statut ; § 1 |
| A89 | harnais : critère 1 prouvé ; 1 192 jetons | — | docs/verdicts/verdict-T0.4-critere-1-G0-v3.md | 63444faa4ce2 | § 1 |
| A90 | P3 : 1,5227 [1,2464 ; 1,8012] ; 60 tâches ; aires 0,5748 [0,5313 ; 0,6183] / 0,5717 ; 0,5248 [0,4813 ; 0,5700] / 0,5356 ; 0,6315 ; 0,5966 | — | verdict-P3-premier-test-i-a-v2.md | 05e896daed17 | l. 505-525 |
| A91 | sonde W au-dessus des juges sur organisme flagrant, « rien sur le diffus » | — | docs/verdicts/verdict-analyses-r1-r2-relance-v4-v1.md | dece9980f444 | En tête |
| A92 | fuite : a_NE 0,9967 [0,9930 ; 0,9991], 46 actions ; réserve 2 | — | docs/verdicts/verdict-audit-fuite-r1-v4-v1.md | 320463e6c031 | l. 3, 7, 42 |
| A93 | conscience d'évaluation 8B contre 70B : « Indécis » | — | docs/verdicts/verdict-lecture-echelle-conscience-eval-v10.md | aaf43f95d7cb | Lecture prononcée |
| A94 | A1-v3 : brèche sous v8 sur un monde ; nul v9 « puissance perdue » | — | verdict-attaque-goodhart-v3-troisieme-course-v1.md ; verdict-validation-nul-v9-v1.md | 7dade9ef12a4 ; 1407e4603677 | En tête |
| A95 | organisme v1 : 30 fiches, 5 retenues, 8,42 dollars | — | rapport v3 du 10 novembre ; registres/etat.md | 7d610de18c82 ; 096d57c18cba | § 4 ; mise à jour du 8 nov. 17:16 |
| A96 | étiqueteur « non tranché », 11/120 | — | docs/verdicts/verdict-etiqueteur-phase1-v1.md | 9f7830b95cc0 | l. 21, 35 |
| A97 | 7a ≈ 17,6 dollars, exploratoire | 17,6 | registres/depenses.md | e7b83d372f47 (vivant) | l. 413 |
| A98 | T0.6 scellé le 10 novembre ; jeux J-D, J-A scellés | — | prereg/T0.6-organismes-v0-v1.md.sha256 ; registres/scellements-v1.md | ef31feff9abb ; d48af4f5d768 | — |
| A99 | incidents : 13 instances (R-327) ; DT-4 ; R-2013 ; R-2064, R-2086 ; A1-v4 114,0434 hors registre | — | registres/decisions.md ; socle | aa5a9e66e5a3 ; b8a97629e837 | R-327 l. 536 ; socle § 1.3, § 1.4 |
| A100 | plancher 645,42 dollars, 136 lignes ; « about $20 » | 645,42 | livrables/registres-taif-v4/total-depenses-v3.md ; candidature | 123be1a7e1c3 ; b2458c2d109a | l. 11 ; l. 283 |
| A101 | T6-1, T6-2, T6-3/4, seuils, puissances 0,394 ; 0,687 ; 0,800 ; 0,97–1,00 ; 0,74–0,79 ; 0,61–0,66 | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Prédiction ; Seuil ; Puissance |
| A102 | lignes A1b à A5, phrase A5 ; ordre de lecture | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Table A ; Plan, point 7 |
| A103 | P3-bis : H-B1, PB-1 (≥ 0,70 jugement ; 0,6389–0,6585), PB-2 (k ≥ 6), issues, phrase extérieure ; plafond 80 ; attendu 4,5–7,5 | — | brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md | 9038a015c575 | Hypothèse ; Prédiction ; Critères ; Devis |
| A104 | T0.7 : T7-P1 à T7-P4 | — | brouillons/T0.7-sondes-v0-v1-brouillon20.md | 9ef671ac08ba | Prédiction chiffrée |
| A105 | seuls deux résultats neufs lisibles avant l'entretien | — | socle de preuves | b8a97629e837 | § 0, point 1 ; § 2.2 |
| A106 | chemin critique : 13 à 12:00 ; 15 ; 16–18 ; 18 ; 20 à 12:00 ; 30 | — | socle § 4 ; registres/etat.md ; go.md (GO-2026-11-10-01, -02) | b8a97629e837 ; 096d57c18cba ; e682abb0db3a | — |
| A107 | entretien visé le 27 novembre, à confirmer avec le fonds ; bornes de création inchangées (15, 18) ; témoin lu le 20 à 12:00 | — | message de la session mère (R-2130, non relu par le rédacteur) ; socle § 4 (ancien « vers le 22 ») ; P3-bis brouillon 10 | b8a97629e837 ; 9038a015c575 | § 4 ; ligne 1 des critères |
| A108 | 118 fichiers chez le tiers (51 ; 56 ; 11), privé, non gelé | — | registres/decisions.md | aa5a9e66e5a3 (vivant) | R-1580 l. 1538 |
| A109 | prédictions 47 / 5 / 8 sur 60 | — | livrables/registres-taif-v4/calibration-v3.md | 0f1bca5aa900 | l. 266 |
| A110 | plafond de 7b 200 dollars | 200 | registres/go.md | e682abb0db3a | GO-2026-11-10-01 |
