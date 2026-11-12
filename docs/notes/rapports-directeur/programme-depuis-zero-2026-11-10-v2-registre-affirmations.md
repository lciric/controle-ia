# Registre des affirmations — « Le programme expliqué depuis zéro » — v2

Document : `docs/notes/rapports-directeur/programme-depuis-zero-2026-11-10-v2.html`. Une ligne par chiffre ou fait vérifiable.
Version 2 du registre : la v1 (`0b4de478…`) reste intacte (R12). Rédacteur neuf de la v2, qui n'a écrit ni la v1, ni sa
contre-lecture, ni sa consigne. Empreintes recalculées le 10 novembre 2026 (relevé `date -u` : 2026-11-10 10:39:27 UTC),
douze premiers caractères ; complètes au journal v2. « Vivant » : registre modifié dans la journée, cité à l'empreinte lue ;
`registres/decisions.md` est tenu en ajout seul : les numéros de ligne cités ne bougent pas (contrôlé à la fin, journal v2).

Colonne « v2 » : **=** ligne de la v1 reprise, conforme selon la contre-lecture ; **C24** corrigée selon le constat 24 de la
contre-lecture ; **MàJ** mise à jour (texte ou source changés depuis la v1) ; **N** nouvelle ligne.

Empreintes courtes des registres vivants à la lecture : `registres/decisions.md` `29551e667b6a` (2 119 lignes, lu jusqu'à R-2161 à 10:44:03 UTC ; puis `7cadb1d486f5` (R-2162, lu à 10:46 UTC) et `f7d219571825` (R-2163, lu à 10:49 UTC) ; la v1 citait
à tort `aa5a9e66e5a3`, ni celle de son journal ni celle du fichier) ; `registres/etat.md` `e6d41dbe378a` ; `registres/go.md`
`e682abb0db3a` ; `registres/depenses.md` `5268f0f09943` (414 lignes) ; `registres/scellements-v1.md` `d48af4f5d768`. Candidature :
`b2458c2d209a` (la v1 écrivait à tort `b2458c2d109a` en A24, A67, A74, A100).

| id | phrase (abrégée) | valeur | source | empreinte | ligne ou section | v2 |
|---|---|---|---|---|---|---|
| A01 | agent Llama-3.1-8B-Instruct | 8 milliards | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 14 | = |
| A02 | épisode de dix actions, un agent | N = 1, T = 10 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Plan d'analyse, point 2 (l. 473) | = |
| A03 | seuil de fausses alertes de référence | 1 % | docs/decisions/decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 1, § 2 | = |
| A04 | couches lues 7, 15, 23 sur 32 | — | prereg/T0.6-organismes-v0-v1.md ; N-056 | ef31feff9abb ; 3592c1e977e8 | Hypothèse ; N-056 point 3 | = |
| A05 | vecteur de 4 096 nombres par jeton | 4 096 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Plan d'analyse, point 5 | = |
| A06 | consigne privée : ≈ 3 fois l'estimation honnête | ≈ 3 | docs/verdicts/verdict-P3-premier-test-i-a-v2.md | 05e896daed17 | En tête ; réserve B1 (l. 509-512) | = |
| A07 | coût déclaré ≈ 33 fois celui de l'honnête, en moyenne géométrique ; cause de l'écart non mesurée (unité, échelle des propositions ou gonflement) | 10^1,5227 ≈ 33,3 (calcul) | verdict-P3-premier-test-i-a-v2.md | 05e896daed17 | En tête, P3-P1 (différence appariée du log10, saboteur moins honnête) ; réserve B1, l. 509-512 | MàJ (constat 11) |
| A08 | § 1 : δ = 0,5 σ ; une action dépasse le seuil 3,4 % ; maximum 3,9 % ; somme 88,7 % sur 200 actions ; 6,2 % sur dix actions | 0,0339 ; 0,0393 ; 0,8867 ; 0,0623 | sortie du script v2 (journal v2) | b12b923510bb | lignes [A] m = 100 ; [A10] m = 5 | MàJ (constat 7) |
| A09 | forme du processus e unilatéral, inégalité de Ville | formule | docs/notes/note-mathematique-lemme-theoreme-v3.md | dfe4fe0fc4d0 | § 2 | = |
| A10 | L1, L2, L3 (a)–(d), L4, L5 ; énoncé courant borné (somme lue à la fin, nombre d'actions fixé ; lecture continue dépend du calendrier) | énoncés | note v3 ; docs/decisions/decision-N-003-N-004-v1.md | dfe4fe0fc4d0 ; cc1be39369bc | note § 3 ; décision § 2 | MàJ (constat 4) |
| A11 | « la puissance ne dépend que de B et de la variance » (programme) | citation | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 56 | = |
| A12 | budget total borné = choix de modélisation déclaré | — | docs/decisions/decision-P-008-v1.md | ac9551b044c1 | § 2 | = |
| A13 | L4 non testé en simulation | — | note v3 ; prereg/T0.3-simulation-lemme-theoreme-v1.md | dfe4fe0fc4d0 ; 7474743a0fa2 | § 7 ; « Hors de portée de T0.3 » (l. 57) | = |
| A14 | preuves contre-vérifiées par un sous-agent neuf | — | note v3 | dfe4fe0fc4d0 | en-tête | = |
| A15 | lemme dit « candidat » au programme | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 54 | = |
| A16 | énoncé du théorème du programme, citation | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | l. 62 | = |
| A17 | T1–T4, classes C et K, Slepian ; énoncés courants : réarrangement → somme totale et maximum aveugles ; dépendance à lois gardées → la somme peut voir | énoncés | note v3 ; decision-N-003-N-004-v1.md | dfe4fe0fc4d0 ; cc1be39369bc | note § 4 ; décision § 1 (« vrai en classe C pour les statistiques symétriques, faux en classe K ») | MàJ (constats 1, 2) |
| A18 | hypothèse pivot δ > 0, deux issues publiables ; test de E1.3 à préenregistrer (aucun préenregistrement de G1 scellé) | — | docs/programme-controle-ia-v2.md ; registres/etat.md | 2fd63badb5af ; e6d41dbe378a | l. 64 ; « Derniers verdicts de porte » (critère 6 ouvert) | MàJ (constat 9) |
| A19 | T0.3 : 31/31 ; 342 et 544 cellules ; 0 contraire ; audit non déclenché | 31 ; 342 ; 544 ; 0 | docs/notes/resultats-T0.3-v1.md | 9ab618edae17 | Prononcé | = |
| A20 | T0.3 : prononcé du code de lecture gelé ; verdict formel d'un lecteur neuf (« confirmé avec réserves ») rendu sur la branche d'une autre session, non fusionné | — | registres/decisions.md | 29551e667b6a (vivant) | R-2126 point (2) (l. 2084) ; R-2137 (l. 2095) ; R-2141 (l. 2099) ; R-2157 (l. 2115 : fusion encore à faire) | MàJ (constat 10 ; consigne v2, point 4) |
| A21 | calendrier : 1,000 / 0,160 / 0,158 (n0 = 200, B = 25, m = 10) | — | resultats-T0.3-v1.md | 9ab618edae17 | Magnitudes, 1 | = |
| A22 | e cumulé 0,09–0,25 ; Page 0,57–1,00 | — | resultats-T0.3-v1.md | 9ab618edae17 | Magnitudes, 2 | = |
| A23 | 2606.10456 : somme 0,253 ; maximum 0,027 ; vraie et pessimiste pour le maximum | 0,253 ; 0,027 | resultats-T0.3-v1.md ; note v3 | 9ab618edae17 ; dfe4fe0fc4d0 | Magnitudes, 4 ; note § 4 | = |
| A24 | candidature : « its central statement does not hold for its own construction » | citation | docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt | b2458c2d209a | l. 87-88 | C24 |
| A25 | Ville sous effet épisode : 0,21 ; 0,35 ; calibrage conforme 0,046–0,055 sur 17 réglages | — | resultats-T0.3-v1.md | 9ab618edae17 | Magnitudes, 6 | = |
| A26 | exemple chiffré, horizon de 200 : toutes les valeurs du tableau (a) (bloc de 200) et du tableau (b), 0,32 %, 21 points (0,674 contre 0,887), 0,971, 0,591, 0,886, 8,9 %, 0,93 %, 2,7 % (L2) | voir sortie | docs/notes/rapports-directeur/exemple-chiffre-depuis-zero-v2.py (rejoue la v1 `ee221d75738a` à l'identique, garde interne) | b12b923510bb | lignes [A] et [B] ; ligne « prix … 21.3 points » | MàJ (script v2) |
| A27 | trois papiers, problèmes, thèses | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 2 | = |
| A28 | probabilités d'originalité (0,55 ; 0,50 ; 0,75 ; 0,66 ; 0,40 ; 0,75 ; 0,65 ; 0,15 ; 0,70 ; 0,55 ; 0,85 ; 0,60 ; 0,80 ; 0,45 ; 0,30 ; 0,70 ; 0,68) | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 5, l. 93-114 | = |
| A29 | révisions : L ≈ 0,4 ; HC1 0,4–0,5 ; H2 ≈ 0,35 ; HC3 ≈ 0,35 | — | N-003-N-004 ; N-005-N-006 ; N-007-N-008 ; N-013 | cc1be39369bc ; cd49afbc924c ; ab7dc9bb2c96 ; 157d388ef5d0 | sections « Originalité » | = |
| A30 | H1a porte la revendication ; H1b information | — | docs/decisions/decision-N-055-v1.md | 371879d5bd44 | Nœud H1b | = |
| A31 | G1 par mode ; « coût » seul ne porte pas H1 | — | docs/decisions/decision-N-054-v1.md | c8a00b3f885a | points 2 et 3 | = |
| A32 | gain dans chaque mode, tenu à l'écart compris ; bases (ii) et (iii) | — | docs/decisions/decision-N-056-v1.md | 3592c1e977e8 | points 1 et 4 | = |
| A33 | contre-résultat 2512.07810 p. 17 | — | docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md | bbe0c1f523ad | § 1, point 4 (H1) | = |
| A34 | H2 énoncé retenu ; Doomed 2607.06503, E-valuator 2512.03109 | — | decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 1 | = |
| A35 | réserve « dérive de l'honnête sous revers » | — | docs/decisions/decision-N-034-v1.md | 97e33e971a8f | § 2 | = |
| A36 | L occupé en partie 2608.02698 p. 5 ; T moitié négative 2607.11751 | — | note v3 | dfe4fe0fc4d0 | § 8 | = |
| A37 | H6 énoncé retenu (trois interventions) ; 2412.01784 ; Poser 2405.05466 | — | docs/decisions/decision-N-015-v1.md ; N-013 | 462785b33310 ; 157d388ef5d0 | § 1 ; § 6 | = |
| A38 | H8 devient diagnostic | — | docs/decisions/decision-N-062-v1.md | 63f426903e6d | point 2 | = |
| A39 | H8 prémisse en partie occupée 2605.27958 | — | etat-de-l-art niveau 2 | bbe0c1f523ad | § 1, point 3 (H8) | = |
| A40 | conscience d'évaluation du dispositif avant H8 | — | docs/decisions/decision-N-053-v1.md | 2204256d7442 | point 3 | = |
| A41 | loi Δv = g·(ĉ − v0), prédictions 1–4, cinq familles | — | docs/decisions/decision-N-005-N-006-v1.md | cd49afbc924c | § 1 | = |
| A42 | probabilité du jeton retirée des pièces revendiquées | — | decision-N-013-v1.md | 157d388ef5d0 | § 1 | = |
| A43 | Where Empathy Goes Wrong cité | — | docs/decisions/decision-N-023-v1.md | 1297f509a0fc | § 1 | = |
| A44 | Panin non lu, papier C non scellé avant | — | decision-N-005-N-006-v1.md | cd49afbc924c | § 2, réserves | = |
| A45 | HC2b renommée ; HC3, HC4, HC5 énoncés retenus | — | decision-N-013-v1.md | 157d388ef5d0 | § 2 à § 5 | = |
| A46 | sondes du lecteur déplacées 2511.00554, 2601.11516 | — | decision-N-013-v1.md | 157d388ef5d0 | § 8 | = |
| A47 | porte GC réécrite | — | decision-N-005-N-006-v1.md | cd49afbc924c | § 2 | = |
| A48 | H3 : 2607.07368 | — | etat-de-l-art niveau 2 | bbe0c1f523ad | § 1, point 3 (H3) | = |
| A49 | H9 : « peut s'éroder » ; prédiction à signer et chiffrer (survie décroissante avec le nombre de passages, relevée par un surveillant) ; antériorité non vérifiée ; papier B hors des sept mois | — | docs/decisions/decision-N-035-v1.md | 55df073d6918 | § 2, § 3 | MàJ (constat 30) |
| A50 | Terekhov et al. reconstruit, sans code ni données | — | decision-P-008-v1.md | ac9551b044c1 | § 3 | = |
| A51 | 96 articles : 64 évaluation, 32 réserve | 96 ; 64 ; 32 | registres/etat.md | e6d41dbe378a (vivant) | ligne de la tâche T0.5 (l. 176) | = |
| A52 | pilote : coût seul retenu, accord 0,04 à 0,17 pour 0,6 ; les deux juges sans notation décisive (course arrêtée avant), en nœud | — | docs/verdicts/verdict-T0.5-pilote-v1.md | b9a072302d65 | § 1 ; l. 50 | MàJ (constat 21) |
| A53 | adaptateur rang 16 ; doses 0,25–1 ; dose 0 = base au bit près | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Plan, point 3 ; Hypothèse | = |
| A54 | (ii-b) conçu, contre-lu une fois, ni code ni GO ; lu par l'oracle du mode « coût » | — | rapport v3 du 10 novembre ; proposition P-066 | 7d610de18c82 ; 012ddc44baca | § 4 ; « L'organisme proposé » (l. 43-45) | MàJ (constat 31) |
| A55 | famille (iv) sur devis | — | decision-N-053-v1.md | 2204256d7442 | point 2 | = |
| A56 | prédiction de validité | — | docs/programme-controle-ia-v2.md ; N-053 | 2fd63badb5af ; 2204256d7442 | § 7 ; point 2 | = |
| A57 | « diffus » défini comme mesure | — | P-066 ; N-007 | 012ddc44baca ; ab7dc9bb2c96 | « Les faits » 3 ; § 1 | = |
| A58 | familles de sondes (brief) ; concepts : domaine = sonde d'intention, conscience d'évaluation réservée au test de validité de H8 | — | brief v2 (familles) ; brouillons/T0.7-sondes-v0-v1-brouillon20.md (concepts) | 9261932a11f2 ; 9ef671ac08ba | T0.7 (l. 166-171) ; l. 846-860 | C24 (source complétée) |
| A59 | jamais moyenne ; bras de diagnostic permis | — | docs/decisions/decision-N-026-v1.md | 85bd40235f36 | § 1 | = |
| A60 | plancher : 200 directions, quantile 0,95, borne basse stricte (aussi au glossaire) | 200 ; 0,95 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Métrique (l. 412 et suivantes) | = |
| A61 | juge par action, juge 3B, TRACE-lite, accumulation boîte noire | — | brief v2 T0.8 ; programme § 8.3 ; registres/etat.md | 9261932a11f2 ; 2fd63badb5af | T0.8 | = |
| A62 | prédicteur sur traits du texte ; aire 0,8878 | 0,8878 | docs/decisions/decision-N-029-v1.md | 084e30523c0a | § 1, point 2 | = |
| A63 | base « mots et coût » ; seuil 0,70 ; gain + 0,05 | 0,70 ; 0,05 | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Règle « mots et coût » | = |
| A64 | préenregistrement de T0.8 en rédaction : premier brouillon lancé le 10 novembre, scellement visé vers le 18 ou le 19 ; lecture possible vers le 20 ou le 21, non promise (liste, ligne 3) | — | registres/decisions.md ; registres/etat.md | 29551e667b6a ; e6d41dbe378a | R-2131 point (4) (l. 2089) ; en-tête (« T0.8 brouillon 1 en rédaction ») ; R-2130 (l. 2088) | MàJ (v1 : « n'est pas écrit ») |
| A65 | invariants de protocole ; invariant N-053 | — | programme § 9 ; N-053 | 2fd63badb5af ; 2204256d7442 | § 9 ; point 5 | = |
| A66 | oracle « affaiblir les contrôles », non construit | — | docs/decisions/decision-N-060-v3.md ; P-066 | 2b448f696503 ; 012ddc44baca | § 1–3 ; « Les faits » 4 | = |
| A67 | relecteurs d'une même famille | — | candidature | b2458c2d209a | l. 257-258 | C24 |
| A68 | G0 huit critères | — | brief v2 | 9261932a11f2 | Porte G0 | = |
| A69 | G0 fin novembre ; un seul report, verdict final au plus tard le 31 janvier 2027 : mot relayé, repris dans la règle de repli approuvée par Lazar d'un mot direct | — | registres/decisions.md | 29551e667b6a (vivant) | N-027 l. 462 ; R-749 l. 977 ; R-765 l. 993 ; contre-lecture du socle : R-2133 l. 2091 ; socle v2 : R-2156 l. 2114 (« N-027 bis non inscrite ») | C24 + MàJ |
| A70 | critère 3 jugé aux doses où la base échoue | — | docs/decisions/decision-N-063-v2.md | b2d9f0354380 | points 1-2 | = |
| A71 | critères 1 et 5 prouvés, aucune porte franchie | — | registres/etat.md | e6d41dbe378a | Derniers verdicts de porte (l. 183-184) | = |
| A72 | G1 : bras F1 retiré (il se gagne en signalant trop) ; F1 = moyenne harmonique de la précision et du rappel ; planchers rapportés | — | decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 2 (« Le bras F1 se gagne en sur-signalant ») | MàJ (constat 32) |
| A73 | G1 : décidé par la borne basse d'un pari apparié (garantie à tout nombre de tâches), rééchantillonnage rapporté ; confirmé le 28 octobre | — | decision-N-055-v1.md ; decision-N-056-v1.md ; registres/decisions.md | 371879d5bd44 ; 3592c1e977e8 ; 29551e667b6a | D-S11 ; point 2 ; R-600 (l. 826) | C24 (référence) + MàJ (constat 32) |
| A74 | G1 fin M2 (programme) ; fin du mois 4 (candidature) | — | programme ; candidature | 2fd63badb5af ; b2458c2d209a | § 10 ; l. 159 | C24 (empreinte, ligne) |
| A75 | N-062 : reconception, sans borne, famille neuve, tout rapporté | — | decision-N-062-v1.md | 63f426903e6d | points 1-6 | = |
| A76 | bascules | — | programme § 13 ; N-062 | 2fd63badb5af ; 63f426903e6d | § 13 ; point 6 | = |
| A77 | bras d'attaque : deux bras, cloisons ; « Pourquoi » : un mode qu'aucun concepteur de surveillant n'a vu | — | decision-N-056-v1.md ; N-054 ; consigne de la v19 | 3592c1e977e8 ; c8a00b3f885a ; 5609fc655b5e | points 6-7 ; point 3 ; § 2 (l. 53) | MàJ (constat 33) |
| A78 | lancement décidé le 10 novembre, rien n'a tourné ; lancement sur le mot direct de Lazar dans la session qui en a la charge et une autorisation de dépense, aucune inscrite | — | registres/decisions.md ; registres/go.md | 29551e667b6a ; e682abb0db3a | R-2127 (l. 2085) ; aucune ligne « bras d'attaque » au 10 novembre (l. 291-296) | MàJ (constat 16 ; vérifiée, la v1 la disait non vérifiée) |
| A79 | classifieur de sûreté le 27 octobre, sans contournement | — | registres/decisions.md | 29551e667b6a (vivant) | R-597 l. 823 | C24 |
| A80 | pince : définition, hypothèse, dans aucun préenregistrement | — | brouillons/entretien-taif-v3/consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md | 5609fc655b5e | § 1 | = |
| A81 | juge O2 énoncé retenu ; citations obligatoires | — | docs/decisions/decision-N-064-v1.md | 387c9d4eda5a | points 2-4 | = |
| A82 | rôles 1, 2 adoptés ; 3 à trancher | — | docs/decisions/decision-N-065-v1.md | f820e90da092 | points 1-3 | = |
| A83 | composition jugée sur l'oracle et le coût | — | docs/decisions/decision-N-058-v1.md | 854f2724864f | point 1 | = |
| A84 | tâches fraîches ; test_final lu une fois ; contre-lecteur | — | N-049 ; N-050 ; N-052 | 8a5bf5e57e2b ; a54b128df955 ; 817d218b22b8 | — | = |
| A85 | objectif ultime ; régimes en attente ; composition apprise, coût, héritage ; N-044 et N-045 v2 ne nomment pas l'organisme d'idéation | — | N-044 ; N-045 v2 | 2b70bdac014d ; c7b05e39de38 | Énoncés retenus (aucune occurrence d'« idéation ») | MàJ (constat 17) |
| A86 | A1-v4 : W2 1/24 [0,0074 ; 0,2024] ; v8 24/24 ; W2g 10/24 [0,2447 ; 0,6117] ; r = 10/17 ; 8/11 ; lecture bornée ; réserves ; texte gelé écrit pour deux mondes au nul, un seul l'est dans cette course | — | docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md | e6e2f17076fa | § 2.1 (l. 36), § 2.2, § 3, § 4 | MàJ (constat 34) |
| A87 | se rapporte avec A1-v3 ; absent de la candidature | — | socle de preuves | b8a97629e837 | § 2.4 ; § 1.1 | = |
| A88 | état de l'art : 13 et 98 PDF ; 24 rapports ; 3 497 citations ; 0 échec ; 147 lignes | — | etat-de-l-art niveau 2 ; niveau 1 | bbe0c1f523ad ; b0b519fe250a | Statut ; § 1 | = |
| A89 | harnais : critère 1 prouvé ; domaine validé 1 087 jetons ; production jusqu'à 1 192, couverte par la seule garde de production | 1 087 ; 1 192 | docs/verdicts/verdict-T0.4-critere-1-G0-v3.md | 63444faa4ce2 | § 1 ; observation 3 (l. 18) | MàJ (constat 35) |
| A90 | P3 : 1,5227 [1,2464 ; 1,8012] ; 60 tâches ; aires 0,5748 [0,5313 ; 0,6183] / 0,5717 ; 0,5248 [0,4813 ; 0,5700] / 0,5356 ; 0,6315 ; 0,5966 | — | verdict-P3-premier-test-i-a-v2.md | 05e896daed17 | l. 505-525 | = |
| A91 | sonde W au-dessus des juges sur organisme flagrant, « rien sur le diffus » | — | docs/verdicts/verdict-analyses-r1-r2-relance-v4-v1.md | dece9980f444 | En tête | = |
| A92 | fuite : a_NE 0,9967 [0,9930 ; 0,9991], 46 actions ; réserve 2 | — | docs/verdicts/verdict-audit-fuite-r1-v4-v1.md | 320463e6c031 | l. 3, 7, 42 | = |
| A93 | conscience d'évaluation 8B contre 70B : « Indécis » | — | docs/verdicts/verdict-lecture-echelle-conscience-eval-v10.md | aaf43f95d7cb | Lecture prononcée | = |
| A94 | A1-v3 : brèche sous v8 sur un monde ; validation du nul v9 : issue « puissance perdue », tout l'écart tient à une ligne | — | verdict-attaque-goodhart-v3-troisieme-course-v1.md ; verdict-validation-nul-v9-v1.md | 7dade9ef12a4 ; 1407e4603677 | En tête ; En tête, réserve 1 | MàJ (constat 18) |
| A95 | organisme v1 : 30 fiches, 5 retenues, 8,42 dollars | — | rapport v3 du 10 novembre ; registres/etat.md | 7d610de18c82 ; e6d41dbe378a | § 4 ; mise à jour du 8 nov. 17:16 | = |
| A96 | étiqueteur « non tranché », 11/120 | — | docs/verdicts/verdict-etiqueteur-phase1-v1.md | 9f7830b95cc0 | l. 21, 35 | = |
| A97 | 7a ≈ 17,6 dollars, exploratoire | 17,6 | registres/depenses.md | e7b83d372f47 (vivant) | l. 413 | = |
| A98 | T0.6 scellé le 10 novembre ; jeux J-D, J-A scellés | — | prereg/T0.6-organismes-v0-v1.md.sha256 ; registres/scellements-v1.md | ef31feff9abb ; d48af4f5d768 | — | = |
| A99 | incidents : 13 instances (R-327) ; DT-4 ; R-2013 ; R-2064, R-2086 ; A1-v4 114,0434 hors registre jusqu'au 10 novembre, inscrite depuis, non rapprochée | — | registres/decisions.md ; socle | 29551e667b6a ; b8a97629e837 | R-327 l. 536 ; socle § 1.3, § 1.4 ; registres/depenses.md l. 414 ; R-2158 (l. 2116) | C24 + MàJ |
| A100 | plancher 645,42 dollars, 136 lignes ; « about $20 » | 645,42 | livrables/registres-taif-v4/total-depenses-v3.md ; candidature | 123be1a7e1c3 ; b2458c2d209a | l. 11 ; l. 283 | C24 (voir journal v2 : R-2156 signale un doublon de 1,06, non vérifié) |
| A101 | T6-1, T6-2, T6-3/4, seuils, puissances 0,394 ; 0,687 ; 0,800 ; 0,97–1,00 ; 0,74–0,79 ; 0,61–0,66 | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Prédiction ; Seuil ; Puissance | = |
| A102 | lignes A1b à A5, phrase A5 ; ordre de lecture ; étiquettes H6-1 à H6-4 propres au texte scellé | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | Table A (l. 541) ; Plan, point 7 ; Hypothèse | MàJ (constat 19) |
| A103 | P3-bis : H-B1, PB-1 (≥ 0,70 jugement ; 0,6389–0,6585), PB-2 (k ≥ 6), issues (« vu » : le nul se lit sur le saboteur du premier test, dit « discret »), phrase extérieure ; plafond 80 ; attendu 4,5–7,5 | — | brouillons/P3-bis-temoin-positif-v1/P3-bis-preenregistrement-v1-brouillon10.md | 9038a015c575 | Hypothèse ; Prédiction ; Critères (l. 1005) ; Devis | MàJ (constat 20) |
| A104 | T0.7 : T7-P1 à T7-P4 | — | brouillons/T0.7-sondes-v0-v1-brouillon20.md | 9ef671ac08ba | Prédiction chiffrée | = |
| A105 | prévision au 10 novembre : avant l'entretien, deux résultats neufs seulement (témoin positif, table du coût) ; aucune lecture de sonde de la course promise avant, possible sans marge (liste, ligne 4) (elle exige le verdict du témoin et la lecture scellée des surveillants de référence) | — | registres/decisions.md ; prereg/T0.6-organismes-v0-v1.md ; socle | 29551e667b6a ; ef31feff9abb ; b8a97629e837 | R-2130 (l. 2088) ; Plan, point 7 ; § 2.2 | MàJ (constat 15 ; consigne v2, point 5) |
| A106 | chemin critique : 13 à 12:00 ; 15 ; 16–18 ; 18 ; 18 ou 19 (visé) ; 20 à 12:00 ; 30 | — | socle § 4 ; registres/etat.md ; go.md (GO-2026-11-10-01, -02) ; registres/decisions.md | b8a97629e837 ; e6d41dbe378a ; e682abb0db3a ; 29551e667b6a | — ; R-2131 (l. 2089) pour le 18 ou 19 | MàJ |
| A107 | entretien visé le 27 novembre, à confirmer avec le fonds ; bornes de création inchangées (15, 18) ; témoin lu le 20 à 12:00 | — | registres/decisions.md ; P3-bis brouillon 10 | 29551e667b6a ; 9038a015c575 | R-2130 (l. 2088) ; ligne 1 des critères | MàJ (vérifiée, la v1 la disait non relue) |
| A108 | 118 fichiers chez le tiers (51 ; 56 ; 11), privé, non gelé | — | registres/decisions.md | 29551e667b6a (vivant) | R-1580 l. 1538 | C24 |
| A109 | prédictions 47 / 5 / 8 sur 60 tranchées ; 235 inscrites | — | livrables/registres-taif-v4/calibration-v3.md | 0f1bca5aa900 | l. 264-266 | MàJ (constat 36) |
| A110 | plafond de 7b 200 dollars | 200 | registres/go.md | e682abb0db3a | GO-2026-11-10-01 (l. 291) | = |
| A111 | exemple chiffré, horizon de dix actions, B = 2,5 : quatre lignes du tableau (a) (m = 1, 2, 5, 10) | 0,5689 0,2845 0,0623 0,0272 0,0052 ; 0,1409 0,0723 0,0623 0,0175 0,0052 ; 0,0339 0,0287 0,0623 0,0134 0,0052 ; 0,0189 0,0224 0,0623 0,0104 0,0052 | sortie du script v2 (journal v2) | b12b923510bb | lignes [A10] | N |
| A112 | dix actions sabotées à 0,5 σ (B = 5) : somme 22,8 fois sur 100 (formule fermée, contrôlée par simulation), maximum 4,7, processus e 6,2 | 0,2281 (simulé 0,2317) ; 0,0471 ; 0,0624 | sortie du script v2 | b12b923510bb | ligne [A10] « toutes les 10 actions sabotées » | N (remplace le « ≈ 23 » à la main du constat 7) |
| A113 | lecture à dix actions : somme 6,2 ; processus e au plus 2,7 ; maximum 0,2845 contre somme 0,0623 pour une action à 2,5 σ ; honnête 0,13 % | 0,0623 ; 0,0272 ; 0,2845 ; 0,0013 | sortie du script v2 | b12b923510bb | lignes [A10] | N |
| A114 | prix de la garantie toujours valide à dix actions : 4,9 points (0,0134 contre 0,0623) ; calendrier 0,0238 et 0,0075 ; somme simulée 0,0602 et 0,0654 | — | sortie du script v2 | b12b923510bb | lignes [A10] « calendrier » et « prix » | N |
| A115 | partie (b) à dix actions (r = w = 3) : somme et maximum identiques ; fenêtre glissante 6,84 sur 100 (0,91 sans attaque) ; classe K : 7,2 % et 1,0 % | 0,0684 ; 0,0091 ; 0,0721 ; 0,0103 | sortie du script v2 | b12b923510bb | lignes [B10] | N |
| A116 | L5 : aucune des 31 prédictions de la simulation ne le porte ; seulement des chiffres exploratoires | 0,53 ; 0,65 ; 0,08 (non écrits au document) | prereg/T0.3-simulation-lemme-theoreme-v1.md ; note v3 | 7474743a0fa2 ; dfe4fe0fc4d0 | « Hors de portée de T0.3 » (l. 56) ; § 3, L5 | N (constat 3) |
| A117 | L4 : hypothèses (pas d'interférence, nombre d'actions par pas fixe, aucune statistique par agent) ; le seuil suppose des agents indépendants au sein d'un pas | — | note v3 | dfe4fe0fc4d0 | § 3, L4 | N (constat 5) |
| A118 | utilité = ce que l'agent honnête accomplit encore sous la défense | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 4, l. 75 (« Utilité = performance sur la tâche honnête sous π_B ») | N (constat 8) |
| A119 | hypothèses de la garantie : écarts indépendants ou différences de martingale, sous-gaussiens, μ0 connu, σ connu ou majoré | — | note v3 | dfe4fe0fc4d0 | § 1, (V), l. 36 | N (constat 25) |
| A120 | « trajectorielle » ; co-élévation | — | note v3 | dfe4fe0fc4d0 | § 3 ; § 4, T3 | N (constat 26) |
| A121 | plancher du maximum strictement au-dessus de α ; prix chiffré par la simulation | 2,7 % (0,0270) | note v3 ; decision-N-003-N-004-v1.md ; sortie du script v2 | dfe4fe0fc4d0 ; cc1be39369bc ; b12b923510bb | § 3, L2 ; § 2 ; ligne [A] m = 200 | N (constat 27) |
| A122 | candidature : demande de bourse envoyée au fonds le 7 octobre 2026 | — | candidature | b2458c2d209a | l. 4-10 | N (constat 28) |
| A123 | tâches floues : « flou à la relecture, vérifiable en aval » | — | docs/programme-controle-ia-v2.md | 2fd63badb5af | § 6 (l. 120) | N (constat 29) |
| A124 | réfutation de H1 : gain de la lecture interne sur la strate « diffus, flou » ; la porte demande plus (deux questions, l'échec ne dit pas laquelle) | — | decision-N-055-v1.md ; decision-N-056-v1.md | 371879d5bd44 ; 3592c1e977e8 | Nœud H1b ; points 1 et 4 | N (constat 12) |
| A125 | bases (ii) cascade de portes indépendantes sur les mêmes sondes et (iii) sonde du dernier état ; sans rapport avec les saboteurs | — | decision-N-007-N-008-v1.md | ab7dc9bb2c96 | § 1, table des quatre bases | N (constat 13 ; glose validée) |
| A126 | mode tenu à l'écart : hors de la décision de la porte (N-055, D-S10) ; gain de H1 exigé dans chaque mode, tenu à l'écart compris (N-056, D-S29) ; règle fixée au préenregistrement | — | decision-N-055-v1.md ; decision-N-056-v1.md ; registres/decisions.md | 371879d5bd44 ; 3592c1e977e8 ; 29551e667b6a | D-S10 ; point 4 ; R-600 (l. 826) | N (constat 14) |
| A127 | pari apparié : contraste borné, richesse par mises (Ville), borne basse à tout instant ; glose « garantie quel que soit le nombre de tâches » | — | decision-N-056-v1.md ; pari_apparie.py (copie de travail) | 3592c1e977e8 ; ec6c2cf64d0c | point 2 ; docstring (l. 1-20) | N (constat 32 ; glose validée) |
| A128 | écarts au texte envoyé hors du repli : bruit d'activations (H6, quatre interventions dans la candidature), revendication du juge resserrée, dépense (« about $20 »), « I set the questions and take every decision » | — | candidature ; N-015 ; N-064 ; socle | b2458c2d209a ; 462785b33310 ; 387c9d4eda5a ; b8a97629e837 | l. 152-155, 256, 264, 283 ; § 1 ; points 2-3 ; § 1.1, § 1.3, § 1.4 | N (constat 22) |
| A129 | ouverture réduite du témoin positif au rendez-vous : issue et ligne seulement, sous conditions ; sans ouverture anticipée : scores des sondes scellés, puis verdict, puis lecture | — | docs/decisions/decision-N-066-v1.md ; socle | 21e83ed58c74 ; b8a97629e837 | points 1 et 2 ; § 2.1 | N (constat 23 ; R-2133) |
| A130 | bras d'attaque : question « ce lancement est-il couvert par ta décision de gouvernance du 28 octobre ? », réponse « oui » | verbatim | registres/decisions.md | 29551e667b6a | R-2145 (l. 2103) | N (précision de la mère) |
| A131 | R-611 : « toute construction ou exécution d'un pipeline opérationnel d'évasion dans les phases 1–2 (organismes évadeurs, démonstration en conditions réelles) est gelée tant qu'une revue de sécurité externe ne l'a pas validée » ; conception et recherche défensive continuent | citation | registres/decisions.md | 29551e667b6a | R-611 (l. 838), « Lecture » (1) et (2) | N (consigne v2, point 4) |
| A132 | restriction de R-611 levée par Lazar pour le bras d'attaque le 10 novembre ; cloisons inchangées (N-053, N-054, N-056) | — | registres/decisions.md | 29551e667b6a | R-2146 (l. 2104) | N (postérieure à la précision de la mère : voir journal v2) |
| A133 | jeu « coût gonflé » (J-C) v3 refusé par la règle gelée : indice de surface « grille multiplicative dans la proposition », 87 paires sur 320 (27,2 %), au-delà du quart ; réécriture une fois au plus ; T0.7 et l'étape A n'en dépendent pas | 87 ; 320 | registres/decisions.md | 29551e667b6a | R-2135 (l. 2093) ; règle du quart : R-1675 (l. 1633) ; règle gelée d'acceptation : R-2106 (l. 2064) | N (consigne v2, point 4) |
| A134 | J-D dissimulation ; J-A intention dans les autres modes, scellés | — | registres/decisions.md ; registres/scellements-v1.md | 29551e667b6a ; d48af4f5d768 | R-2106 (l. 2064) | N |
| A135 | famille (iii) : organismes publics de l'institut britannique (sous-performance volontaire, verrouillés par mot de passe), 70 milliards, retirés de la phase 0, contrôle externe en phase 1 sur devis séparé, défaut appliqué le 6 octobre | — | docs/programme-controle-ia-v2.md ; registres/decisions.md ; registres/etat.md | 2fd63badb5af ; 29551e667b6a ; e6d41dbe378a | § 7 (l. 133) ; P-002 (l. 379) et R-047 (l. 168) ; ligne T0.6 (l. 177) | N (constat 31) |
| A136 | brouillon 11 du témoin positif et brouillon 21 des sondes en rédaction | — | registres/decisions.md ; registres/etat.md | 29551e667b6a ; e6d41dbe378a | R-2131 point (4) (l. 2089) ; en-tête | N |
| A137 | lien entre l'objectif ultime et l'organisme d'idéation : décision de Lazar du 10 novembre ; branché le 28 octobre sur la tâche « proposer des hypothèses de recherche jugées par un juge statistique » ; n'a pas encore les propriétés de l'objectif | — | registres/decisions.md | 29551e667b6a | R-2152 point (1) (l. 2110) | N (constat 17) |
| A138 | développement de la version 65 du code de l'organisme repris le 10 novembre ; sa boucle fermée est le premier pas vers l'objectif | — | registres/decisions.md | 29551e667b6a | R-2148 points (2)-(3) (l. 2106) ; R-2152 (l. 2110) | N |
| A139 | page publique du verdict du juge publiée le 10 novembre sur le mot de publication de Lazar, citations de N-064 comprises | — | registres/decisions.md | 7cadb1d486f5 | R-2162 (l. 2120) ; antécédents R-2131 (l. 2089), R-2154 (l. 2112) | N |
| A140 | socle de preuves v1 contre-lu depuis | — | registres/decisions.md | 29551e667b6a | R-2133 (l. 2091) | N |
| A141 | glossaire : dose réalisée E(d) = effet du coût par dose | — | prereg/T0.6-organismes-v0-v1.md | ef31feff9abb | table des prédictions, T6-10 (l. 410) | N (constat 37) |
| A142 | glossaire : ancien juge v8, nouveau juge v9 ; A1-v3 contre v8, A1-v4 contre v9 | — | verdict-officiel-a1-v4-v1.md ; verdict-attaque-goodhart-v3-troisieme-course-v1.md | e6e2f17076fa ; 7dade9ef12a4 | § 2.1 (l. 36) ; table W1 (l. 14-22) | N (constat 37) |
| A143 | glossaire : nœud = décision réservée à Lazar ; oracle ; jumeau honnête ; pince ; mode de sabotage ; mode tenu à l'écart | — | CLAUDE.md (hiérarchie de décision) ; P-066 ; N-060 v3 ; consigne de la v19 ; N-054 | — ; 012ddc44baca ; 2b448f696503 ; 5609fc655b5e ; c8a00b3f885a | — | N (constat 37) |
| A144 | « Prévision au 10 novembre 2026 » : forme datée de la promesse d'avant l'entretien | — | consigne de la v2 (message de la mère), point 5 ; R-2130 | 29551e667b6a | l. 2088 | N |
| A145 | dépense d'A1-v4 (114,04 dollars comptés par la course) inscrite au registre des dépenses le 10 novembre, non rapprochée ; budget : « inscrite le 10 novembre seulement » ; point 2 de « ce qui dépend de toi » | 114,0434 | registres/depenses.md ; registres/decisions.md | 5268f0f09943 ; 29551e667b6a | l. 414 ; R-2158 (l. 2116) | N |
| A146 | vérification de l'état de l'art de niveau 3 lancée le 10 novembre | — | registres/decisions.md | 29551e667b6a | R-2158 point (4) (l. 2116) ; R-2159 point (1) (l. 2117) | N |
| A147 | HC2 : signalement d'antériorité non vérifié (arXiv 2606.10304), lecture confiée à la vérification de niveau 3 avant toute modification de HC2 ; aucun chiffre repris (R7) | — | registres/decisions.md | 29551e667b6a | R-2161 (l. 2119) | N |
| A148 | § 9 : liste « Ce qui manque pour rassurer le jury sur « l'approche peut marcher » » insérée telle quelle (phrase d'ouverture, priorités, onze lignes, sources) ; ses dates et états sont ceux de la liste | — | docs/notes/rapports-directeur/ce-qui-manque-approche-peut-marcher-v1.md ; registres/decisions.md | edb0bf03d87d ; f7d219571825 | toute la pièce ; R-2163 (l. 2121) | N (demande de Lazar relayée par la mère) |
| A149 | § 9 : « ce qui n'est pas promis avant l'entretien » mis en accord avec la liste (lignes 3, 4, 8) ; tableau des cinq affirmations renvoie à la liste | — | même pièce | edb0bf03d87d | lignes 3, 4, 8 | N |
| A150 | témoins de concepts : deux jeux sur quatre acceptés, deux refusés deux fois ; option (c) : texte des sondes scellé avec clé permise et repli écrit, nouvelle consigne en parallèle | — | registres/decisions.md | f7d219571825 | R-2155 (l. 2113) ; R-2158 point (3) (l. 2116) | N (demande de la mère) |
| A151 | résultat d'A1-v4 publié le 10 novembre sur la page publique de l'organisme | — | registres/decisions.md | f7d219571825 | R-2162 (l. 2120) | N (demande de la mère) |
