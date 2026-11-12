# Vérification du brouillon de synthèse v2 — collisionneur « protocelles », tour 1 — v1

Auteur : lecteur neuf, sous-agent, modèle : Claude Fable 5.1. Date : 31 octobre 2026, 18:35 UTC (`date -u`). Ce lecteur n'a écrit ni la question, ni les critères, ni la synthèse v1, ni la relecture, ni le brouillon v2. Travail au processeur seulement : aucun appel payant, aucun journal de la course 2 ouvert, aucun fichier existant modifié, brouillon non copié. Le texte servi du papier (confidentiel, non publié) est cité par page et ligne, jamais recopié.

## Pièces lues (empreintes recalculées le 31 octobre 2026)

| Pièce | Chemin | Empreinte sha256 |
|---|---|---|
| Critères gelés | `docs/notes/protocelles-collisionneur-v1/criteres-lecture-protocelles-tour1-v1.md` | `aed5f5933150a3ce786dad556e00dbc98c130ff1a7d1f82a5e0843a32baa9896` |
| Relecture indépendante (Opus) | `donnees/relecture-conv-audit-protocelles-v1/relecture-opus-synthese-tour1-protocelles-v1.md` | `66e1e2aca49d06217a4960cba3c2546f241695a37ebae74f47864d870e010df7` |
| Synthèse v1 | `docs/notes/protocelles-collisionneur-v1/synthese-protocelles-tour1-v1.md` | `dfd0d168ab1acbc8e90dd63019cf907b13ccfdf507dc51a0f1e7009cc15683fb` |
| Brouillon v2 vérifié (80 757 octets, 345 lignes) | `donnees/sauvegardes-restaurees-2026-10-31-v1/1810/brouillons-interrompus/synthese-protocelles-tour1-v2.md` | `0dc584bd7c2348600aafb4f23c59b5fd564529769174b6bc182b1250fad4fcd1` |
| Texte servi du papier (7 625 lignes, marqueurs `[page N]`) | `donnees/collisionneur-protocelles-v1/faits-protocelles-v2.md` | `0c963925c2cd321a8c430a515a1163ebdf14eb29f5106dd20c0eb3b5354d9a22` |
| B, conception (T1) | `donnees/collisionneur-protocelles-v1/run-protocelles-tour1-e3-v1/cellules/E3-T1-conception-B.md` | `c60235b7e82564cc79da9d540a3cafe5c0478a42a58e946a397e95a6c6ebfe12` |
| C, conception (T1) | `…/E3-T1-conception-C.md` | `3786d4be18aad803357b4a5d93a96238951b66b415e9e28b95a8c0abc5d17ed3` |
| D, conception (T1) | `…/E3-T1-conception-D.md` | `1c10cc61ef9194b77392d084554530ec1f88ff35a4ea2ac4b29735911a0f3d69` |
| B, critique croisée (T2) | `…/E3-T2-critique-croisee-B.md` | `1a55ab8c4c7c424ce70801f7488621539c1c7e0ca866c2b52e4bca14b529e968` |
| C, critique croisée (T2) | `…/E3-T2-critique-croisee-C.md` | `86a14a97d2a572d5c86c4a686ad87802abbc2d072a15282503f967d192960209` |
| D, critique croisée (T2) | `…/E3-T2-critique-croisee-D.md` | `fb160e9c70bc5ff3d46e0e12f985a07408be0a46bbf7c2abeaa013997345a659` |
| B, réponse (T3) | `…/E3-T3-reponse-B.md` | `8c53b7147138c8c744a32d9d9b77ceeb45fcc2849721bff6e1ac22b8a90ee8be` |
| C, réponse (T3) | `…/E3-T3-reponse-C.md` | `16331c7f03d225cf98e42a749e76307fb3bfe5b5c863497c60b59a7929144ef2` |
| D, réponse (T3) | `…/E3-T3-reponse-D.md` | `755f60909edeb7bdeaff7660ed5de3c7b818c811ceb2e90d0764ff022c273802` |

Les neuf compagnons `.sha256` des cellules ont été contrôlés par `sha256sum -c` avant lecture (neuf « OK »). Vérifié aussi : `donnees/collisionneur-protocelles-v1/question-collisionneur-protocelles-tour2-v1.md` a bien l'empreinte `88d18079cab27124954922e10680a4e2ba704ec6a1bdc95e99deffe43fe9b2ea` que donne le brouillon. Le PDF du papier n'est pas sur ce disque à `docs/sources/pdf/Ciric-protocells-fecundity-complete-v0.19.4.pdf` (dossier vide) : les lectures graphiques de la Fig. 7B faites par le brouillon ne sont pas revérifiables ici.

Renvois : « l. L » = ligne du fichier servi ; les pages commencent aux lignes 2846 (p. 42), 3001 (p. 43), 4950 (p. 68), 5432 (p. 75), par exemple.

## Verdict (une ligne)

**Versable après corrections (liste ci-dessous)** : le brouillon est complet et non tronqué, ses corrections sont justes sur le texte servi (toutes les valeurs recalculées concordent), chaque point de la relecture est traité ; il reste deux chemins de pièces propres à une autre session, un compte faux (« neuf présupposés » de D : il y en a dix), un comptage de concessions hérité de la v1 à préciser, et une dizaine de renvois de ligne décalés d'une à deux lignes.

## (i) Complétude

| Vérification | Résultat |
|---|---|
| Fin de fichier | non tronquée : la dernière ligne (« Questions secondaires : (4) … le débit RF ? ») se termine par un saut de ligne ; 345 lignes, 80 757 octets, empreinte recalculée égale à celle annoncée |
| Critère 18 (traçabilité) | juste : table des pièces avec empreintes ; cellules « revérifiées OK » ; chaque chiffre renvoie à une page et une ligne du texte servi ou à une cellule et sa section |
| Critère 19 (ordre des travaux) | juste : §8, processeur sans dépense (i à vi), puis préenregistrement, puis journaux de la course 2, puis devis et GO, pince et arène en dernier |
| Critère 20 (questions du tour 2 en duel) | juste : §12, trois duels H_A contre H_B avec la mesure décisive, sans chiffre choisi par le lecteur, plus sept questions secondaires ; la mention du « verdict par piste » de la question v3 est rapportée sans être vérifiée (§11.8) |
| Critère 21 (ordre, critères non modifiés) | juste : les critères gelés sont cités avec leur empreinte et jamais modifiés ; les sections 1 à 12 de la v1 sont toutes présentes, avec en plus la table « Corrections de la v2 », §1.1, §1.2 et §3.1 |
| Confidentialité (en-tête des critères) | juste : aucun passage du papier de plus d'une phrase n'est reproduit |

## (ii) Table « Corrections de la v2 » du brouillon, ligne par ligne

Chaque ligne a été relue sur le texte servi (page, ligne, valeur) et sur la cellule citée ; les valeurs simples ont été recalculées au processeur.

| N° | Verdict | Détail de la vérification |
|---|---|---|
| R1 | juste | Table S1a : colonnes n = 2, 3, 4, 5, 8 aux l. 2870-2878, valeurs 0,450266 ; 0,644415 ; 0,681632 ; 0,690313 ; 0,693103 aux l. 2880, 2884, 2888, 2892, 2896 ; contrôle par la ligne « ln 2 − U_c » : 0,693147 − 0,644415 = 0,048732 (l. 2885 : 4,87 × 10⁻²) et 0,693147 − 0,450266 = 0,242881 (l. 2881 : 2,43 × 10⁻¹) ; ligne 2^(1−2n)/ln 2 : 0,0451 à n = 3 (l. 2886), 0,1803 à n = 2 (l. 2882). B-T1 (h)1 écrit bien « U_c ≈ 0,450 (Table S1a) », « q > e^(−0,450) ≈ 0,638 », et (h)2 « R > e^U ≈ 1,57 » ; e^(−0,644415) = 0,5250 recalculé. C-T1 (c)1 cite seulement U_c(5) et U_c(8), justes |
| R2 | juste | Théorème 1, l. 350-354 (« as n → ∞ at fixed replicase number » ; « if θ ≥ 2 … U_c = 0 ») ; l. 1640 (décroissance en 1/n pour θ ≥ 2) ; Table S1c, l. 2985 (1,459 à θ = 2, colonne « n U_c(200) ») ; Table S1b, l. 2937 (0,0073 à θ = 2) ; C-T1 (c)2 écrit « U_c(∞) = 0 … Theorem 3 » ; B-T1 (g)3 cite le Théorème 1 sans la condition |
| R3 | juste | l. 2808-2813 : la borne n/5 est énoncée « for every n ≥ 2, R > 0 and θ > 0 » dans le modèle principal, sans mention d'une autre règle de division ; l. 2832 : « at every R ≤ n/5 when n ≤ 12, the bound ln(2R/(R + 1)) above is the better one » ; l. 2786 : cette dernière borne vaut pour toute règle aveugle. C-T3 §3 affirme bien les quatre bornes « pour toute règle de division aveugle (même non binomiale !) » |
| R4 | juste sur le texte ; lecture graphique non revérifiable | l. 935-937 : la Fig. 7B trace « nτc against their template advantage θ′ (n = 5, 10, 20) » et dit « beyond θ′ = 2 … depends only weakly ». Les valeurs lues sur la figure (10 → 1,6 pour n = 20 ; 5 → 1,85 pour n = 10) ne peuvent être revérifiées ici (PDF absent) ; elles sont cohérentes avec le texte à θ′ = 2 (1,61 et 1,85, l. 866) |
| R5 | juste | l. 5028 : « λ*(p) = ½ log₂(2/(1 + p)) » ; r̄ = (1 + p)/2 à la l. 5027 |
| R6 | juste | l. 155-156 : pour U = 0,3 la loi repose sur (H2) ; B-T1 (h)2 écrit « R > 3,1 × 3 ≈ 9,3 pour U + ln θ = 0,6 » ; recalcul : e^0,6/(2 − e^0,6) = 10,24 ; 9,3 < 10,24 |
| R7 | juste | l. 4280 : « more viable than lost copies would (τc = 0.208 against 0.103 at n = 20) » ; le comparateur « with fast truncated copies alone » est à la l. 4282 ; l. 863 : « A lost truncated copy costs nothing » |
| R8 | juste | C-T1, l. 65 : « ψ(3,1) ≈ 0,346 » (écrit `\psi(3,1)` ; seule occurrence de ψ(3 dans les neuf cellules) ; l. 130 : « ψ(y) ≤ 0,35 à 0,43 ». Texte : l. 803 (« below half of it near y ≈ 3.1 »), l. 675-676 (ajustement ln 2/(1 + y/0,823)^0,443, précision 0,002). Recalculé : ψ(3) = 0,3510 ; ψ(3,1) = 0,3470 ; ψ(1,5) = 0,4377 |
| R9 | juste sur le texte ; réserve | l. 935 : n = 5 est calculé ; C-T1 (e) cas 1 : « τc ≈ 0,25 à 0,30 pour n = 6 » = 1,53/6 et 1,85/6 (recalculé : 0,255 ; 0,308). La valeur « nτc ≈ 1,6 à 1,7 pour n = 5 » est une lecture graphique non revérifiable ici ; le texte (l. 866-867) donne nτc décroissant en n (1,85 ; 1,61 ; 1,53 pour n = 10, 20, 30), ce qui rend une valeur inférieure à 1,85 à n = 5 surprenante. Le verdict « retirée » ne dépend pas de cette valeur (extrapolation non marquée, non recalculée) |
| R10 | juste | l. 5349 : « S12.3. Self-copying, total or partial » ; l. 5537 : « S12.4 » ; B1 aux l. 5473-5477 (p. 75), inégalité λc(ln 2 + ℓy) > ℓy à la l. 5477 ; même inégalité l. 3385 (p. 45). C-T1 (b-bis) Exp. 1 cite « page 75, Appendix S12.3, Section B1 » |
| R11 | juste | Table 1, l. 517-522 (« fusion between protocells … ln 2 for invasion ») et l. 547-552 (« invasion threshold unchanged, proved; no fusion raises it above the ceiling, proved ») ; l. 1174-1176 (seuil = terme du pool + constante du compartiment) ; l. 1184-1186 (θ < 1 ajoute ln(1/θ) au terme du pool, les protocelles ajoutent ln 2) ; l. 1195-1197. C-T3 (c)1.2 : « Trois seules soupapes … La fusion aveugle … ne relève jamais le seuil d'invasion » |
| R12 | juste | B-T1 (g)3 : « cohérent avec le papier (θ ≥ 2 → aucune fidélité ne suffit, Théorème 1, page 4) » sans la condition « noyau limite » ; l. 350-354 et l. 1640 |
| R13 | juste | B-T1 (e) : « tout moniteur doit survivre à au moins 70 tours » tiré de Bailey et collègues « RAPPORTÉ » ; le critère 8 range « 70 tours de Bailey » parmi les chiffres du contexte |
| R14 | juste | B-T1 (f) : « déposés avec le code (Appendice S7, pages 52–55) », sans « public » ; l. 3905 (S7), l. 3912 (« deposited with the code »), l. 3942 et l. 3967 (« are deposited with their scripts and logs ») ; futur seulement aux l. 1853-1855 et 1860-1865 |
| R15 | juste | C-T1 (b-bis) Exp. 1 : trans strict contre hybride fertile (q_vf) ; D-T1 E0 : noyau à un modèle contre noyau à deux parents, « un seul parent » en contrôle négatif ; C-T2 (c)1 (parent unique) → B-T3 « C-B (contrôles négatifs) 1 : acceptée », E-B2 ; B-T2 note finale (consommation, noyau à deux parents) → D-T3 §1 (« Acceptée ») et E0 (bras un parent, deux parents) |
| R16 | juste | la réserve de symétrie est désormais dans la ligne 2 du verdict et le §11.2 dit « Cette réserve porte sur les lignes 1 et 2 du verdict » |
| R17 | juste | C-T3 §5 (estimateur par moyenne de filles par mère reconnu faux, « acceptée en totalité ») ; C-T3 (c)2.3 ne rattache aucune mesure ; l. 2786 : U_c ≤ ln(2R/(R + 1)) + max(0, ln(1/θ)) ; recalculé : ln(4/3) = 0,2877 < 0,40 |
| R18 | juste | C-T1 (e), règle de décision : archiver hors du vivier, mesurer q_B, réinjecter sous quota θ′_eff ≤ 1 si q_B > 0 ; D-T1 (a), fin : « quarantaine hors vivier, sans réinjection, avec conservation probatoire » ; D-T1 E1 : « sans autoriser leur réinjection non contrôlée » ; D-T3 E1 et §3 (« quarantaine réversible ») ; C-T3 Exp. 2 (quarantaine, bain contrôlé) |
| R19 | juste | §1.2 consolide pire cas, garde et vérification extérieure ; les sources citées (C-T1 (f) table ; D-T1 (a), (d) ; B-T1 (c) P3 ; sections (c) des trois T2 ; B-T3, C-T3, D-T3) contiennent bien ce qui leur est attribué (douze lignes recoupées, voir (iv)) |
| R20 | juste (renvoi à une ligne près) | l. 2855-2858 : biais à 200 protocelles, « All thresholds reported here come from exact kernels » ; le contrôle par Monte Carlo est aux l. 1591-1592 (« against a Monte Carlo simulation of the branching process »), non 1589-1591 |
| R21 | juste sur le fond ; un compte faux | §1.1 restitue B-T1 (a)1-6 et C-T1 (a) fidèlement ; mais D-T1 (a) compte **dix** présupposés (lignes 11 à 20 de la cellule), non neuf : le brouillon fond « H2 ou les méthodes adversariales » et « Weitzman » en un seul item. Correction C3 |
| R22 | juste | l. 1557 (« The total copying rate is thus RF ») ; l. 2539 (« rate RF p(F, N) ») ; l. 2784-2785 (générateur en RF) ; C-T1 (a) (« opérateur externe fixe ») ; D-T1 (a) 2e ligne ; D-T2 (a)1 (loi du taux d'événements) ; D-T3 §1 (B(a)4) et E2 (« budget constant ») ; B-T1 (h)1 (« espaces éloignés ») ; C-T1 (c-bis) (« sans saut d'espace éloigné ») ; D-T1 (c) (appariement « par espace ») ; B-T2 (a)4 sur D (« au taux RF ») |
| R23 | juste | Table S1a l. 2869-2898 ; Table S2 : colonne « n = 5 » l. 3009, valeurs à θ = 1 pour R = ∞, 160, 40, 10 : 0,690 ; 0,678 ; 0,645 ; 0,536 aux l. 3051-3054 ; plus petite fécondité tabulée 10 (l. 3034-3045) ; l. 1641-1644 (ln 2 exactement sans fille d'une seule molécule) ; Table 1 l. 446-451 ; l. 2786-2790 |
| R24 | juste | C-T1 (e) et D-T1 (a), fin, citent « jetées, jamais archivées » ; B-T1 (a)5 cite « doivent être jetées » ; la forme complète de la note reste rapportée, non vérifiée (pièce hors liste) |
| R25 | juste (renvoi à deux lignes près) | l. 355-356 : « ρ < 1 for all q ≤ min(θ, 1)/2 » ; l. 1607-1610 ; l. 1184-1186 ; la condition « max(q, q/θ) ≤ 1/2 » de la p. 32 est à la l. 2365 (la l. 2363 est un fragment de formule « P ») ; C-T3 (c)2.3 : « soit un tri par un juge (r̄ > 1/2 ou θ < 1) » ; D-T3 §3 : « validé avec θ = 1, alors q ≤ 1/2 implique extinction » |
| R26 | juste | B-T1 (a)4 et la déclaration d'intégrité de C-T1 confirment que la note et la relecture n'étaient pas servies ; le critère 20 gelé impose les duels |
| R27 | juste (renvoi à une ligne près) | l. 1529-1531 ; l. 1555 (modèle tiré parmi les N − 1 autres) ; l. 1557 (RF) ; « all molecules decay at the same rate » est à la l. 1797, non 1795-1796 (la l. 1558 dit déjà « Each molecule decays at rate 1 ») ; C-T2 (b)2 : cinq statuts plantés |
| R28 | juste | raisonnement refait : sous paires mixtes stériles, une fiche vraie ne naît que d'une paire vraie–vraie ; si un parent est consommé et qu'au plus un enfant naît, F ne croît pas |
| R29 | juste | l. 4049-4052 : « The identity requires that τ be the same for all templates present … A partial loss … is not a rescaling of τ » ; D-T3 §3 (« une même probabilité d'arrêt pour tous les modèles ») ; C-T2 (c)3 (censure par difficulté) |
| R30 | juste | rapporté comme non vérifié ; cohérent avec R24 |
| R31 | juste | l. 2358-2365 (division aveugle : toute affectation équiprobable à tailles données, densité de paires non accrue) ; l. 5020-5023 (α_d²) ; l. 5027-5028 (r̄ = (1 + p)/2) ; l. 4043-4052 (identité (i), R(1 − τ), même τ) |
| R32 | juste | recalcul de ce lecteur : avec φ = F(F − 1)/(N − 1), tirage uniforme d'une paire, parents gardés, paires mixtes stériles, E[φ′]/φ = (N − 1)/N + 2 q_vv F/N² ; ≤ 1 dès que 2 q_vv F ≤ N, donc dès que q_vv ≤ 1/2 ; dérive du papier à θ = 1 : (N − 1)/N + 2q/N (l. 1607-1610), jamais moins favorable puisque F ≤ N ; retrait uniforme : E[φ′] = F(F − 1)/N = φ (N − 1)/N ; retrait d'une fausse à N = 6, F = 2 : 2/5 → 2/4. C-T3 Exp. 1 affirme bien la surmartingale « quel que soit le taux d'événements a(F, P) et la fécondité R » en citant le Théorème 2 |
| N1 | juste | C-T1 (e), règle de décision : « coût nul sur U et sur R tant qu'on n'y puise pas, exactement équivalent au sort « lost » » ; C-T1 (e) cas 3 et C-T3 Exp. 2 H_A : « coût exact 1/(1 − τ) sur R » ; l. 703 et l. 4048-4049 |
| N2 | juste | l. 4078-4080 : « U_c(n) < max(0, ln(1/θ)) + ln 2 + ln(1 − τ) whenever θ′ ≥ min(θ, 1) » |
| N3 | juste | l. 1554-1557 : noyau de copie (modèle tiré parmi N − 1, poids 1 et θ, RF) ; l. 1577-1580 : critère de seuil (Crump–Mode–Jagers, matrice K) |
| N4 | juste sur ce disque | `docs/sources/pdf/` ne contient pas le PDF ; la relecture d'Opus l'avait trouvé à ce chemin sur sa machine, avec l'empreinte `ba59c254…` que reprend le brouillon |

## (iii) Points de la relecture : traités ?

| Point | Traité ? | Où, et comment |
|---|---|---|
| E1 (U_c(3) = 0,450266 est la valeur de n = 2) | traité, juste | R1 ; §4 (« q > e^(−0,644415) = 0,525 … non q > 0,638 ») ; §9 (vérifiées : U_c(5), U_c(8) ; I21 majeure attribuée à B) ; verdict ligne 3 ; §10 ; §11.3 |
| E2 (Théorème 1 sans sa condition) | traité, juste | R2 ; §9 (« pour le noyau limite … à taille finie le seuil reste positif et décroît en 1/n ») ; I6 reformulée (condition omise) |
| E3 (R ≤ n/5 « pour toute division aveugle ») | traité, juste | R3 ; §3 « Conséquence commune » ; §9 (vérifiée avec sa portée ; I23 mineure sur C-T3 §3) |
| Critère 3 (I6, I7, I15, E1, E2) | traité | R12, R13, R9, R1, R2 ; décompte §9 refait : 17 inexactes, 1 non trouvée, 5 retirées |
| Critère 5 (« un parent contre deux parents » est une convergence du T3) | traité, juste | R15 ; verdict ligne 2 ; §10 : retiré des accords indépendants (11 au lieu de 13), compté dans les convergences avec « qui a cédé à qui » |
| Critère 9 (réserve de symétrie attachée au verdict) | traité, juste | R16 ; verdict ligne 2 ; §11.2 |
| Critère 10 (P1 non signée, mesure invalidée) | traité, juste et complété | R17 ; §4 P1 « non signée (mesure) » ; §8.2 (« P1 n'y entre pas en l'état ») |
| Critère 15 (« archiver plutôt que détruire » : conditions divergentes) | traité, juste | R18 ; §6 (« même option par défaut, conditions divergentes (non compté comme accord) », sous-tours de D donnés) ; §10 |
| Critère 16 (contenu du point (f)) | traité, juste | R19 ; §1.2 (table de dix lignes, incomplétudes de B et D nommées) |
| Critère 17 (étalonnage « déjà présent ») | traité, juste | R20 ; §7 ; §8 (ii) |
| Omission (a) | traité, un compte faux | R21 ; §1.1 ; « neuf présupposés » de D à corriger en dix |
| Omission (b) (bisociateur catalyseur ; paires bipartites) | traité, juste | R22 ; §2 (« Deux traits du contexte ») ; §3 (deux hypothèses ajoutées) ; §12 question (7) |
| Omission (c) (tables de seuils exacts) | traité, juste | R23 ; §4 (Tables S1a, S2, règle de division, bornes) ; §8 (iv) |
| Omission (e) (règle citée tronquée) | traité, juste | R24, R30 ; §6 « La règle en question » (rapporté, non vérifié) |
| Omission (f) | traité, juste | R19 ; §1.2 |
| Omission (h) (θ < 1 : q ≤ θ/2) | traité, juste | R25 ; verdict ligne 1 ; §4 « Prédiction globale » (q ≤ min(θ, 1)/2) ; §5 ; §12 |
| Tour 2 : verdict par piste | traité, rapporté | R26 ; §12 ; §11.8 |
| §4 de la relecture (liste trop courte, trop longue, θ) | traité, juste | R27, R28, R25 ; verdict ligne 1 ; §3 (« Le plafond comme borne demande moins que l'application exacte ») |
| §5 de la relecture (même τ ; règle complète compatible) | traité, juste | R29, R30 ; §6 ; §12 question 2 |
| §6 de la relecture (trois correspondances qui survivent) | traité, juste | R31, R32 ; §3.1 ; §8 (i) et (vi) ; l'esquisse est marquée « à contre-lire (R2), jamais un résultat » |
| Nuances I2, I3, I4, I12, I17 | traitées, justes | R4, R5, R6, R7, R8 |
| I15, I16, I20 contestées ; I5 indécidable | traitées, justes | R9, R10, R11, R14 : retirées sur le texte ou sur la cellule |
| Omissions (d) et (g) | non soulevées par la relecture | §5 et §7 inchangés sur le fond |

## (iv) Sondage de traçabilité (quinze affirmations chiffrées, sections différentes)

| N° | Section du brouillon | Affirmation | Verdict | Renvoi vérifié |
|---|---|---|---|---|
| 1 | §1.2 | juge disqualifié si â_g − b̂_g ≤ 0,20 | juste | C-T3, Protocole 0, point 2 |
| 2 | §1.2 | puissance nulle à trois lots, plus petite valeur atteignable 0,10 | juste | C-T2 (b)1 ; recalculé 2/C(6,3) = 0,10 |
| 3 | §1.2 | matrices connues à ρ = 0,95 et 1,05 | juste | C-T2 (c)1 ; D-T3 E0 |
| 4 | §2 | « aveugle » = toute affectation équiprobable à tailles données (p. 32, l. 2358-2360) | juste | l. 2358-2360 |
| 5 | §4 P4 | τ = 0,20 ; θ′ = 1,2 ; θ′ = 2,5 ; 40 lots par bras ; seuil + 0,02 | juste | C-T3 Exp. 2 |
| 6 | §4 | R > e^U/(2 − e^U) : 2,08 ; 2,94 ; 3,63 ; 10,24 à U = 0,3 ; 0,40 ; 0,45 ; 0,6 | juste | l. 2788-2789 ; recalculé 2,076 ; 2,936 ; 3,633 ; 10,243 |
| 7 | §4 | à n = 3, R = 10, θ = 1, règle sans fille d'une molécule : U_c entre ln(20/12,5) = 0,470 et ln(20/11) = 0,598 | juste | l. 2786-2788 ; recalculé 0,4700 et 0,5978 |
| 8 | §4 | C interpole U_c(6) = 0,69244 par ln 2 − 2^(1−2n)/ln 2 « suivi à partir de n = 4 » | juste | l. 2863-2864 ; recalculé 0,692443 ; C-T1 (c)1 |
| 9 | §4 | 6,6 et 18,6 de C ne contredisent pas la borne | juste | C-T1 (c)1 ; bornes recalculées 4,69 (U = 0,5) et 10,24 (U = 0,6) |
| 10 | §6 | nτ entre 1,53 et 1,85 aux tailles n = 10 à 30, θ = 1 (p. 10, l. 866-867) | juste | l. 866-867 |
| 11 | §7 | 61 boîtes couvrent [1, 23/8] et [47/16, 95/32] ; trois restent ; 64 − 61 = 3 | juste (renvoi à une ligne près) | l. 2759-2760 et l. 2767 (« three remaining boxes ») ; marge 0,0061 à la l. 2765 |
| 12 | §9 | r̄ = 71 % pour ln 4 (p. 13, l. 1190 ; p. 68, l. 5028-5031) | juste | l. 1190 ; l. 5031 (0,7071 pour b = 2) ; recalculé 2^(−2^(1−2)) = 0,7071 |
| 13 | §9 | ≈ 3,41 réplicases à la division au seuil (p. 28, l. 2108-2109) ; « pour toute taille » inexact (n = 20 à 200, l. 2122-2123) | juste | l. 2109 ; l. 2122-2123 ; C-T2 (a)3 sur B dit « pour toute taille n » |
| 14 | §9, I21 | B : « q > 0,638 », « R > e^U ≈ 1,57 » ; D-T2 (a)1 et B-T3 discutent q > 0,638 sans voir l'erreur | juste | B-T1 (h)1-2 ; D-T2 (a)1 sur B ; B-T3 D-B.1 |
| 15 | §10 | accords indépendants 11 (5 + 3 + 1 + 2) ; convergences 10 ; divergences 10 dont 6 non résolues ; inexactes 17 dont 5 majeures ; par espèce B 7 + 1, C 10 | juste | comptes refaits sur les listes du §9 et du §10 : I1, I3, I4, I6, I8, I9, I21 (B) ; I10 à I14, I17 à I19, I22, I23 (C) |

Deux affirmations hors chiffres relevées au passage :
- §11.2 « B accepte toutes les critiques sauf une en partie ; D toutes sauf deux en partie » (hérité de la v1) : B-T3 compte trois acceptations partielles (C-B.4, D-B.1, D-B.4) ; D-T3 en compte deux en partie (B(a)1 ; B(a)3 avec B(b)E1), une rejetée comme affirmation universelle et transformée en test (B(b)E4), une acceptée pour la course 2 seule et rejetée comme impossibilité générale (C(b)1). Inexact, mineur (correction C4).
- Verdict ligne 2 : « les trois espèces placent en premier une épreuve … précédée d'un audit du code de l'orchestrateur et d'un étalonnage de l'estimateur » : exact pour C (Protocole 0) et D (E0 avec calibration) ; B-T3 place E-B2 en premier sans audit ni étalonnage. Imprécision mineure (correction C5, facultative).

## (v) Descriptif, et règle « rien du bras d'attaque »

- Aucune recommandation nouvelle : la « réponse consolidée » du §6 reste « proposée, à trancher au tour 2 » comme en v1 ; le §8 est l'ordre des travaux exigé par le critère 19 ; le §11.5 (« À refuser tant que… ») et le §12 sont ceux de la v1. Les ajouts (esquisse du §3.1, I21 à I23, règle de division au §4) sont marqués « à contre-lire (R2) avant tout usage » (§11.10).
- Rien du bras d'attaque : le brouillon ne cite aucun fichier de `donnees/bras-attaque-*`, `donnees/mode-tenu-a-l-ecart-v1`, `donnees/collisionneur-evasion-moniteurs-v1`, `quarantaine/`, `donnees/runs/` ni `diag/` ; l'« arène P-041 » et les « attaques » dont il parle sont celles du contexte de la question, reprises des cellules. Aucun chiffre de la course 2 n'est cité (critère 2).

## Corrections à faire avant versement

Obligatoires (C1 à C3) :
- **C1** — Table « Pièces et empreintes », ligne « Relecture indépendante (Opus) de la v1 » : remplacer le chemin `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/protocelles-synthese-v2/relecture-opus-synthese-tour1-protocelles-v1.md` par `donnees/relecture-conv-audit-protocelles-v1/relecture-opus-synthese-tour1-protocelles-v1.md` (même empreinte `66e1e2ac…`, vérifiée).
- **C2** — Même table, ligne « PDF du papier » : remplacer « trouvé avec la même empreinte à `/tmp/claude-0/…/scratchpad/protocelles-v1/v0194/papier-v0.19.4.pdf` (R11) » par « absent du dépôt ; la Fig. 7B a été lue sur une copie de même empreinte dans le brouillon de la session précédente, non versée (R11) » ; et au §11.9, remplacer « il a été trouvé dans le brouillon de session avec l'empreinte attendue (R11) » par « il a été lu dans une copie de même empreinte, non versée au dépôt (R11) ; les lectures graphiques ne sont pas revérifiables sur le texte servi ».
- **C3** — §1.1, ligne D : remplacer « **D-T1 (a)** dresse neuf présupposés, tous « hypothèse » ou « rapporté » : … transfert numérique du plafond et du prix ; transfert de H2 et de Weitzman. » par « **D-T1 (a)** dresse dix présupposés, tous « hypothèse » ou « rapporté » : … transfert numérique du plafond et du prix ; transfert automatique de H2 et des méthodes adversariales ; Weitzman comme modèle de remplacement (référence à vérifier). »

Recommandées, mineures (C4 à C6) :
- **C4** — §11.2 : remplacer « (B accepte toutes les critiques sauf une en partie ; D toutes sauf deux en partie ; C la plupart) » par « (B accepte toutes les critiques, trois en partie seulement ; D toutes sauf une rejetée comme affirmation universelle et une acceptée pour la course 2 seule, deux autres en partie ; C la plupart) ».
- **C5** — Verdict ligne 2 : remplacer « précédée d'un audit du code de l'orchestrateur et d'un étalonnage de l'estimateur du rayon spectral » par « précédée, chez C et D, d'un audit du code de l'orchestrateur et d'un étalonnage de l'estimateur du rayon spectral ».
- **C6** — Renvois décalés d'une à deux lignes (le passage cité est bien là) : « p. 21, l. 1795-1796 » → « p. 21, l. 1797 » (§3 intro, §3.1 point 3, R27) ; « p. 32, l. 2363 » → « p. 32, l. 2365 » (R25, §4 « Prédiction globale ») ; « p. 17, l. 1589-1591 » → « p. 17, l. 1591-1592 » (R20, §7) ; « p. 40, l. 2764, 2772-2773 » → « p. 40, l. 2765, 2773-2774 » (§9, 57 boîtes) ; « p. 21, l. 1808-1810 » → « p. 21, l. 1810-1812 » et « (l. 1804) » → « (l. 1805) » (§9, session d'intelligence artificielle) ; « p. 40, l. 2766 » → « p. 40, l. 2767 » (§9, décompte, D-T1 (a) jusqu'à y = 16) ; « p. 40, l. 2759-2766 » → « p. 40, l. 2759-2767 » (§7, trois boîtes restantes).

Réserve à consigner (sans correction de texte) : la lecture graphique « nτc ≈ 1,6 à 1,7 pour n = 5 » (R9, I15) va contre la décroissance en n que le texte donne à θ′ = 2 (1,85 ; 1,61 ; 1,53) ; elle n'est pas revérifiable ici et le verdict « I15 retirée » n'en dépend pas.

## Réserves de ce lecteur

- Le PDF n'étant pas sur ce disque, les trois lectures graphiques de la Fig. 7B (R4, R9, I2, I15) sont prises telles quelles, marquées non revérifiables.
- Les pièces hors de ma liste (question v3, question du tour 2, note de conv-audit) n'ont pas été lues ; les empreintes seules ont été recalculées.
- Le sondage (iv) porte sur quinze affirmations et les 36 lignes de la table des corrections ; il ne revérifie pas chacune des lignes du §9 héritées de la v1 que la relecture avait confirmées (I8, I9, I13, I14, I18, I19), dont les renvois ont toutefois été recoupés au passage et tiennent.
