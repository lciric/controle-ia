# Traitement de la vérification des corrections du brouillon 2 de l'addendum 2 de P3 — v1

Session 14, 2026-10-20 vers 10:50 UTC. Rapport : `verification/verification-corrections-brouillon2-addendum2-P3-v1.md`
(vérificateur neuf, « scellable après corrections », douze constats : sept mineurs, cinq pour information ; RB-01 à RB-13
traités, onze justes, RB-04 et RB-06 en partie). Corrections écrites dans le brouillon 3
(`P3-addendum2-audit-verdict-v1-brouillon3.md`) ; le brouillon 2 reste tel quel (R12). La session n'a calculé aucune
grandeur de B1 ni de B2. Le module, écrit en parallèle sur le brouillon 2 par un rédacteur neuf (orchestration
`wf_17375481-4c6`), sera mis au brouillon 3 avec les constats de ses deux contre-lectures (VB2-01 et VB2-02 touchent le
code et ses tests).

| constat | décision | où dans le brouillon 3 |
|---|---|---|
| VB2-01 (mineur) : gardes 7 et 9 contradictoires | accepté : garde 7 « même état que [L] (calculable, non calculable, en échec, même motif), sinon arrêt ; nombres comparés pour une entrée calculable seulement » ; test : entrée non calculable produite par `lecture.lire` sur des tables synthétiques, jamais en retouchant [L] (cas sain et artefact) | Liste d'arrêt, garde 7 ; Tests |
| VB2-02 (mineur) : règles ajoutées non testées | accepté : six cases de la table, borne décisive ≤ log10 3, réserves du témoin et de la mention sur leurs deux cibles, `reserve_B1_non_lue`, part « instable », comptes de contrôles | Tests (fin de la liste fermée) |
| VB2-03 (mineur) : RB-04 en partie | accepté : citations de l'objecteur 1 (l. 141), du répondeur (l. 312) et de la note (l. 51), avec empreintes ; phrase de lecture de B3 : « grandeur calculée avant le scellement, sur des nombres déjà lus (brainstorm) » | Statut ; Critères (B3) |
| VB2-04 (mineur) : attente sans fondement pour B2 | accepté : « cas attendu pour B2 » retiré ; règle unique (intervalle de `E0` qui contient 0 → « instable »), pour B1 et B2 | Métrique, M5 |
| VB2-05 (mineur) : décision 9 non écrite | accepté : imports limités (arbre gelé, numpy, bibliothèque standard ; aucun import du premier addendum ; aides de tests permises) ; deux contre-lecteurs du code nommés | Emplacement ; Contre-lecture |
| VB2-06 (mineur) : compte des contrôles | accepté : 13 écrits (détail) ; dans ce run 4 sans objet, 9 lus au plus ; sur une autre ligne, jusqu'à 11 | Plan, points 7 et 8 |
| VB2-07 (mineur) : réserves certaines | accepté : phrase sous la table des cas ; au plan, « au moins trois réserves certaines dans ce run » ; audit : « aucune réserve » impossible pour B1 | Seuil ; Plan 8 ; Audit de symétrie |
| VB2-08 (information) : décision 11 | accepté : verdict complété en v2 (`docs/verdicts/verdict-P3-premier-test-i-a-v2.md`), v1 inchangée | Plan, point 1 |
| VB2-09 (information) : suppression non listée | accepté : « sans objet dans ce run » redit pour `P3-P4/<p>` et `T3/<p>` | Seuil |
| VB2-10 (information) : vocabulaire | accepté : « élèvent » / « abaissent » ; « formes qui élèvent ou abaissent la différence » ; « sinon » indenté | Seuil ; Audit |
| VB2-11 (information) : empreintes à remplir, entrée « Contre-lecture 2 » | accepté : entrée ajoutée, marqueurs `<<SHA_VERIFICATION_2>>` et `<<SHA_TRAITEMENT_2>>` à remplir au versement | Contre-lecture |
| VB2-12 (information) : cas d'une borne décisive ≤ log10 3 | accepté : phrase ajoutée ; testé (VB2-02) | Seuil |
