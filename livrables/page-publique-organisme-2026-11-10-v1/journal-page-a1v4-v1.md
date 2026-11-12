# Journal — mise à jour de la page publique de l'organisme d'idéation avec le résultat scellé d'A1-v4 — v1

Rédacteur neuf (sous-agent de la session mère), qui n'a écrit aucune pièce d'A1-v4. Travail du 10 novembre 2026, de 10:02:34 à environ 10:25 UTC (heures relevées par `date -u`). Rien n'est commité, rien n'est poussé ; le clone public n'est pas modifié (hors du `fetch` nommé). Aucun refus de permission ni de classifieur.

## 1. Consigne, interdits, sources lues (empreintes vérifiées avant lecture)

| pièce | chemin | sha256 | vérification | lu |
|---|---|---|---|---|
| consigne | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/consigne-page-publique-a1-v4-v1.md` | `d9dbb02ff51314c7606bfed4194d8deb33529a0e0b27e7bbf58aa9ed29132dec` | égale à celle de la mère | en entier |
| interdits communs v2 | `…/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | égale | en entier, tenus (règle 9 comprise) |
| texte scellé (TS) | `docs/notes/ideation-organisme-v1/a1-v4-reprise-v9/preenregistrement-attaque-goodhart-v5-v1.md` | `d306a8faa45b3d77f1edb653406ced1facd4752b2aa00c2e77593538399a7fe6` | égale à la consigne ; même empreinte que `orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md` du clone public (commit `f39a7f4a`) et son compagnon | § 0.1 (l. 159–169), § 0.5 bis (l. 191–195), § 0.6 (l. 197–203), § 0.7 (l. 205–209, lu en passant), § 0.8 (l. 211–213), § 3 (l. 228–253), § 6 (l. 318–341) ; titres seuls ailleurs |
| verdict officiel (VO) | `…/a1-v4-reprise-v9/verdict-a1-v4-v1/verdict-officiel-a1-v4-v1.md` | `e6e2f17076fab16f2684553765517937d528c657367075c126945c3ae3741cda` | égale à la consigne et au compagnon | en entier (101 lignes) |
| pièce d'intégrité (INT) | `…/verdict-a1-v4-v1/integrite-versement-a1-v4-v1.txt` | `f8af025701e57c93860d7a47bf6dfad15f744ef1de8e982b122431b4617cabe9` | préfixe `f8af0257…` de la consigne ; égale au compagnon | en entier ; elle suffit : la branche de sortie n'a pas été touchée |
| validation du v9 (VV9) | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` | égale à la consigne | l. 1–8 (issue) et l. 30–34 (nœud l. 32–33 ; l. 30, 31, 34 vues en trop, rien n'en est pris) |
| décision N-064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | pas d'empreinte dans la consigne ; égale au compagnon `.sha256` | en entier |
| note POPPER (NP) | `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-popper-evaluator-v1.md` | `d1ab704927b938aab631451b01ea2f197969f627dec32dcf63087bbc42ad0998` | préfixe `d1ab7049…` de la consigne ; égale au compagnon | l. 1–87, 153–158, 186–218, 247–297 |
| note Co-Scientist (NCS) | `…/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md` | `08a3738af518f59790936995cda714210c749f20e1891195343b2c3e2b132312` | pas d'empreinte dans la consigne ; égale au compagnon | l. 1–58, 286–320 |
| page publique actuelle (PA) | clone `/home/user/lciric/ideation-organism`, `resultats/attaque-goodhart-v2/README.md` | `dc2a3d6685f03f72d86c2f943e0d3fe69b3ddfa35463c7696ea99f7422d782bc` | égale à celle que cite TS § 0.8 (`dc2a3d66…`) | en entier |
| README public actuel (RA) | clone, `README.md` | `1105f573e9c47ea90abf08c577aa357409398f3105823ea227d63ecce4512704` | blob `e072e092…` égal à `HEAD:README.md` | en entier |

**Clone public.** Avant : `main` = `origin/main` = `HEAD` = `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0`, arbre propre (`git --no-optional-locks status`). `fetch` nommé lancé à 10:07:09 UTC : `git -C /home/user/lciric/ideation-organism fetch origin refs/heads/main:refs/remotes/origin/main`, code 0. Après : `main` = `origin/main` = `f39a7f4a…` (égaux ; rien de neuf sur le dépôt public), arbre propre. Seul commit visible (clone superficiel) : `f39a7f4` du 9 novembre 2026, 01:48:53 UTC, « A1-v4: sealed preregistration v5-v1 … ». Le correctif s'applique à blanc (`patch --dry-run -p1` dans le clone : code 0, aucune écriture) ; arbre propre ensuite.

## 2. Sorties

| sortie | sha256 | taille |
|---|---|---|
| `/home/user/page-a1v4/resultats/attaque-goodhart-v2/README.md` | `9f24f5598ac2838be648a38485c6c961ff0d5700319dbaa46266bff5d2b1c496` | 129 lignes, 27 286 octets |
| `/home/user/page-a1v4/README.md` | `8e413d7801897c43dae849f712c6cdb1ac875e0532355208f03eba56cb37faa7` | 239 lignes, 47 431 octets |
| `/home/user/page-a1v4/diff-page-a1v4-v1.patch` (`diff -u`, étiquettes `a/` `b/`, à appliquer par `patch -p1` depuis la racine du dépôt) | `202988c3cc66fa1d68d4f68dd74f47562a2c0831cf2f094b4458ae9528c28dab` | 84 lignes, 28 582 octets |
| ce journal | donnée dans la réponse à la mère (un fichier ne peut porter sa propre empreinte) | — |

Ce qui change : page, ligne 3 (« Last updated ») et section neuve insérée l. 5–55, au-dessus de « Update (8 November 2026) », dont la suite est identique à l'octet (`cmp` du titre du 8 novembre à la fin : identique, 73 lignes). README : paragraphe « Related work » ajouté (l. 7) ; ligne d'état (l. 9) : date et une proposition remplacées, une phrase ajoutée ; ligne de la table (l. 131) : dernière phrase remplacée, une phrase ajoutée. Trois lignes retirées en tout, chacune remplacée ; rien d'autre (contrôle mot à mot).

## 3. Chaque chiffre des lignes neuves, avec sa source et sa ligne

Lignes du fichier neuf. VO = verdict officiel ; TS = texte scellé ; INT = intégrité ; VV9 = validation du v9 ; PA = page actuelle ; RA = README actuel ; NP, NCS = notes d'antériorité ; N064 = décision.

**Page (`resultats/attaque-goodhart-v2/README.md`)**

| ligne | chiffres | source |
|---|---|---|
| 3 | 10 November 2026, 10:18 UTC | `date -u` (10:18:00 UTC) |
| 3 | 8 November, 2 November | PA l. 3, 5, 18 |
| 5 | 10 November 2026 (titre) | `date -u` ; VO l. 6 (verdict écrit le 10 novembre) |
| 7 | v9 candidat, v8 juge de production | TS l. 166 (§ 0.1, point 5) |
| 7 | un fournisseur (Argon), une forme d'optimisation | VO l. 36, 46, 87 ; TS l. 194 (f) |
| 7 | 24 cards per world | VO l. 72, 84 ; PA l. 7 |
| 7 | ancien juge v8 = dents | VO l. 33, 44 |
| 7 | four cells per world, 24 units per cell | VO l. 25, 32 |
| 7 | up to 16 attempts | VO l. 31, 36, 46 |
| 7 | 1,478 calls | VO l. 82 |
| 10 | sous-populations 0 et 1 ; « toute promotion sous v9 est fausse » ; ce que W2 éprouve | TS l. 200 ; PA l. 10 |
| 10 | 8 November update | PA l. 5 |
| 11 | (1 − λ)·S2 + λ·N ; λ = 0 ; log W ≤ 0 ; ce que W2g éprouve ; épreuve hors ligne sous son texte scellé | TS l. 201 |
| 11 | λ\* = 0.40 | VO l. 4, 72 ; TS l. 201 |
| 13 | 114.0434 USD ; cap 200 USD | VO l. 54 |
| 13 | `d306a8fa…7fe6` | VO l. 12 ; consigne ; `sha256sum` (copie privée et fichier public) |
| 13 | commit `f39a7f4` | VO l. 17, 96 ; tête du clone |
| 13 | `e72893ef…0129` | INT l. 12 (et l. 8) |
| 13 | `e6e2f170…1cda` | consigne ; compagnon ; `sha256sum` |
| 15 | lecture égale clé pour clé à celle du lanceur | VO l. 19 |
| 15 | audit A1 à A9 ; lecteur neuf d'une autre lignée, verdict provisoire non lu, intervalles et r recalculés | VO l. 6, 15, 21 |
| 15 | écart déclaré (audit et verdict provisoire du même lecteur) | VO l. 88 |
| 15 | 1.6259 USD ; 1.6178 USD ; appel rejoué | VO l. 58 |
| 17 | 1 of 24 ; Wilson 0.0074 to 0.2024 | VO l. 31, 34 |
| 17 | sans retour 3 of 24 | VO l. 66, 83 |
| 17 | ≤ 0.25 (≤ 1 of 24) | VO l. 25, 34 ; TS l. 326 |
| 17 | v8 : 24 of 24 ; 0.862 to 1 | VO l. 33 |
| 17 | 349 of 349 ; 0.971 ; 371 of 373 = 0.995 ; 0.80, 0.50, 0.50 | VO l. 34 |
| 17 | A1, A2 ; 4 of 48 ; 2, 3, 2, 3 of 200 ; 712 lois, 200 rejeux, aucune au-dessus de α, plus grand 9 of 200 ; citation « aucun défaut … » | VO l. 52 |
| 17 | levée lue par le lecteur officiel | VO l. 56, 94 |
| 17 | lecture gelée ; « pas « le taux est sous 0,05 » » ; parenthèse (deux mondes au nul) | VO l. 36 |
| 19 | 10 of 24 ; 0.2447 to 0.6117 ; ≥ 4 of 24 | VO l. 42 |
| 19 | sans retour 7 of 24 | VO l. 73 |
| 19 | v8 : 23 of 24 ; 0.7976 to 0.9926 | VO l. 44 |
| 19 | 10 of 17 = 0.588 ; ≥ 0.5 ; 12 of 17 = 0.706 | VO l. 46 |
| 19 | 17 lois promues sous v9 | VO l. 84 |
| 19 | A4 seul, sans effet | VO l. 4, 53 |
| 19 | lecture gelée de « robuste » ; « pas « le v9 n'a pas de prix » » ; 16 | VO l. 46 |
| 21 | 8 of 11 ; P1 à P5, P8, P10, P11 | VO l. 78 |
| 22 | P6 : 0 of 24 prédit, 1 of 24 observé ; 16 | VO l. 71 |
| 23 | P7 : ≥ 12 of 24 ; 10 of 24 ; 0.40 ; « quatre fois sur cinq » ; 803 of 1,000 ; 0.777 to 0.827 ; 24 cartes ; 3,467 of 4,800 (0.722) | VO l. 72 |
| 24 | P9 : ≥ 0.80 ; 0.588 ; 0.706 | VO l. 74 |
| 26 | P1 : −0.083, 2 of 24 | VO l. 66 |
| 26 | P3 : +2 of 24 (de 1 à 16 tentatives) | VO l. 68 |
| 26 | P8 : +3 of 24 = +0.125 | VO l. 73 |
| 26 | 5 contre 2 ; McNemar p = 0.453 ; −0.020 ; −0.078 to +0.023 ; « non tranché » | VO l. 78 |
| 26 | 0 violation sur 1,276 verdicts appariés | VO l. 54 (et l. 69, 76) |
| 29 | réserve 1 : 349/349, 261/261, 0.995, 0.996, 1 sur 1,478 | VO l. 82 |
| 30 | réserve 2 : 1 of 24, 3 of 24, 1 to 1.5 % | VO l. 83 |
| 31 | réserve 3 : sept cartes ; 17 of 24 ; 17 lois ; 0 of 200 sur chacune des 24 cartes | VO l. 84 |
| 32 | réserve 4 : famille de 21 lois ; 10/17, 12/17 ; 0.5 ; 0.80 | VO l. 85 ; « 21 lois » VO l. 21 |
| 33 | réserve 5 : 0.40 ; 803 of 1,000 ; 0.777 to 0.827 ; 0.722 | VO l. 86 |
| 34–37 | réserves 6 à 9 ; « 79 empreintes » (réserve 8) | VO l. 87–90 |
| 40–43 | réserves du lecteur ; `d306a8fa…`, `f39a7f4` | VO l. 94–97 |
| 45 | 200 USD ; compteur, registre, étape, relais neufs | TS l. 193 |
| 46 | A1 : `fc81d015…`, 2 November ; W1 « instrument en défaut », W2 brèche sous v8 | TS l. 193 ; PA l. 18 (« not judgeable (instrument failure) ») |
| 47 | 41 calls ; 4.245753 USD ; arrêt d'infrastructure | TS l. 193 |
| 48 | 620 calls ; 48.49583 USD ; `fd66feb7…` non lu | TS l. 193 |
| 49 | troisième course lue, verdict `7dade9ef…` | TS l. 193 |
| 49 | « clean rerun of 5 November », « 8 November update » | PA l. 5, 7 (identification : voir choix 18) |
| 52 | « power lost » | VV9 l. 7 ; « attendue par écrit » : PA l. 13 et consigne |
| 52 | `1407e460…c1ea` | consigne ; `sha256sum` ; TS l. 166, 194 (forme courte) |
| 52 | proposable seulement si le responsable accepte le prix, que la description publique dirait ; sinon nul moins coûteux (v10) ; nœud ouvert sans défaut ; v8 en production | VV9 l. 32 ; TS l. 166 |
| 53 | sens de « nothing beyond the archive » ; réponse contraire = nul v10, non une correction | TS l. 194 (b) ; VV9 l. 33 ; renvoi à PA l. 14 |
| 55 | (c) à (f) ; `NON_COUVERT_V9` dans `orchestrator/pole/nul_v9.py` | TS l. 194 ; fichier public, l. 118 (grep dans le clone) |

**README**

| ligne | chiffres | source |
|---|---|---|
| 7 | POPPER : Huang, Jin, Li, Li, Candès, Leskovec ; ICML 2025, PMLR 267:25372–25437 ; arXiv:2502.09858 | NP l. 26–27, 69–70, 77 |
| 7 | titre de POPPER, « Automated hypothesis validation with agentic sequential falsifications » | NCS l. 294–295 (relevé dans E-valuator, p. 11, réf. 8) |
| 7 | e-valeurs et seuil 1/α hors des agents : non revendiqués ; énoncé O2 retenu | N064 l. 13 ; NP l. 26–41 |
| 7 | Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, « Generalization in Adaptive Data Analysis and Holdout Reuse », arXiv:1506.02629 | NP l. 72 ; N064 l. 14 |
| 7 | Blum et Hardt, « The Ladder », arXiv:1502.04585 | NP l. 73 ; N064 l. 14 |
| 7 | principe occupé depuis 2015 ; seule la forme revendiquée ; forme non trouvée dans les pièces lues, travaux qui citent POPPER à lire | N064 l. 14 |
| 7 | Co-Scientist : Nature 655, 487–496, 2026 ; « Towards an AI co-scientist », arXiv:2502.18864 ; « Gottweis et al. » | NCS l. 46, 49 (premier auteur : noms des fichiers de la table, l. 46–50) ; N064 l. 15 |
| 7 | sections 3.1 et 4 | RA l. 78, 110 |
| 9 | 10 November 2026 | `date -u` |
| 9 | « power lost » ; attendue par écrit | VV9 l. 7 ; PA l. 13 |
| 9 | 10 of the 17 ; 8 of 11 | VO l. 46, 84 ; VO l. 78 |
| 9 | 29, 17, 11, 3.1, 5 November, 3 November | RA l. 7 (inchangés) |
| 131 | 10 Nov 2026 ; 1,478 ; 114.0434 USD ; 1 of 24 ; 24 of 24 ; 0.40 ; 10 of 24 ; 10 of 17 ; 8 of 11 | VO l. 6, 82, 54, 31, 33, 4, 42, 46, 78 |
| 131 | chiffres de la clean rerun, du v9 et de sa validation (960, 58.45, 31 lines × 1,000, …) | RA l. 129 (inchangés) |

Aucun chiffre ne vient d'ailleurs ; aucun ne vient de la sortie (non ouverte).

## 4. Choix

1. Anglais, style de la page : paragraphes à tête grasse, listes, guillemets droits, « 1 of 24 », « 95% Wilson interval ». Ordre de la section : celui de la consigne.
2. « of another model line than the auditor's » et non « another model family » : VO l. 6 dit « d'une autre lignée » ; selon N-052 (CLAUDE.md), Opus et Fable sont « même famille, autre modèle ». « Famille » aurait surestimé l'indépendance. À trancher par la mère si elle préfère la lettre de la consigne.
3. Chaînes gelées traduites : « résiste (à cette taille) » → "resists (at this size)" (déjà sur la page) ; « frontière franchie » → "frontier crossed" ; « robuste » → "robust" ; « frontière non franchie » → "frontier not crossed" ; « puissance perdue » → "power lost" (déjà sur la page) ; « rien au-delà de l'archive » → "nothing beyond the archive" (déjà sur la page) ; « non tranché » → "not decided" ; « levée » → "lifted". Les deux lectures bornées sont traduites phrase pour phrase, avec leur « pas … » (« not "the rate is below 0.05" », « not "v9 has no price" »).
4. « Robust » glosé dans le texte : il qualifie les lois promues (rejeu), pas le juge.
5. « a reservation, not a proof » gardé : mots de l'audit (« C'est une réserve, non une preuve »), une négation. Les autres « proof » et « validated » des lignes modifiées sont du texte existant du README.
6. Note A7 (1,6259 contre 1,6178 USD) mise sous « How it was read » : elle est au VO § 2.3, hors des § 4 et § 5 ; gardée par transparence.
7. Omis : numéro de la machine (59845811) et numéros des sept cartes ; identifiants GO ; nom des modèles lecteurs.
8. Réserve du lecteur sur le texte scellé hors de `prereg/` : réécrite sans le chemin privé (« not filed with the working repository's preregistrations »). « private working repository » figure déjà dans le README (l. 112, 123, 125 actuelles).
9. Empreintes entières pour le texte, la liste de la sortie, le verdict officiel et le verdict de la validation du v9 ; formes courtes `fc81d015…`, `fd66feb7…`, `7dade9ef…` comme au § 0.5 bis.
10. `λ\*` échappé (sinon Markdown ouvre une emphase avec le `**` du titre gras) ; contrôlé : 0 occurrence non échappée.
11. « Last updated » : date et heure par `date -u` (10:18:00 UTC) ; la parenthèse nomme aussi la mise à jour du 8 novembre gardée inchangée.
12. README, ligne d'état : « Status (8 November 2026) » → « Status (10 November 2026) » ; la proposition « is running » remplacée et une phrase ajoutée. Ligne de la table : la dernière phrase remplacée (référence de la validation gardée), une phrase ajoutée. Lien vers la page dans les deux.
13. « Related work » : paragraphe à tête grasse placé après « Why it exists », comme « What it is » et « Status » ; pas de titre neuf, donc table des matières et numérotation inchangées. Pages de renvoi (p. 2-5, p. 20-21, p. 10-12 de N-064) omises : pages de PDF, ambiguës à côté de la pagination des actes ; elles restent dans N-064.
14. « aucune des six pièces lues » (N-064) → « not found in the work read so far » : même sens, sans chiffre hors des sources permises.
15. Co-Scientist cité sans le titre de l'article de Nature (absent du texte des notes ; seul le nom de fichier le suggère) ; « Gottweis et al. » tiré des noms de fichiers de la table de la note.
16. A1 : « W1 « instrument en défaut » » rendu comme sur la page, "not judgeable (instrument failure)".
17. Mondes : définitions du § 0.6 reprises (dont « (1 − λ)·S2 + λ·N » et « log W ≤ 0 »), comme la consigne le demande ; ces constantes de formule ne sont pas des résultats.
18. « Troisième course d'A1-v3 = rerun propre du 5 novembre » : déduit de TS § 3, l. 253 (valeurs de la troisième course, verdict `7dade9ef…` : W2 sous v8 24/24 dans les quatre cases ; W1 1/24 avec retour, 0/24 sans), égales à la mise à jour du 8 novembre (PA l. 9–10). Aucun chiffre de TS § 3 n'est écrit sur la page.

## 5. Manques

1. Le point (2) de la liste « Next » du 8 novembre (les 48 lois promues rejouées sous v9) : aucune de mes sources ne le rapporte ; la section n'en dit rien et la page le laisse en suspens.
2. « Argon deviation » (R-2013) n'est pas expliqué par le verdict ; la ligne garde ses mots.
3. Dates de la course : le verdict ne donne qu'un appel du 9 novembre ; la section n'en donne aucune.
4. Ni le verdict ni l'audit ne sont publics : seules leurs empreintes (verdict) figurent ; « exact echoes » reste le terme du verdict, sans définition sur la page.
5. **Publication du paragraphe « Related work ».** N-064 (« Points attachés ») et NP l. 295–296 : retoucher le README public est une publication, « go publication » de Lazar requis. `registres/decisions.md` l. 2089 (R-2131) consigne « citations de N-064 point 4 incluses » sous le mot (3) de Lazar (« depose les derniers resultats sur gthub pour le mentor kirhner ») : c'est la lecture de la mère ; à confirmer avant la poussée.
6. L'heure « 10:18 UTC » est celle de l'écriture ; la mère la remettra à l'heure de la poussée si elle le veut.
7. Les traductions des lectures gelées n'ont pas été contre-lues (la consigne prévoit une contre-lecture par un autre modèle).

## 6. Lectures hors du strict nécessaire, déclarées

- VV9 : lignes 30, 31 et 34 vues (plage 30–34 au lieu de 32–33) ; aucun chiffre pris (perte de puissance, lignes du banc).
- `registres/decisions.md`, `registres/go.md`, `registres/etat.md` : `grep -n "N-064"` (fichiers nommés, non récursif), puis la seule ligne R-2131 (l. 2089) en entier, pour vérifier le nœud de publication de N-064. Le grep a affiché les 420 premiers caractères de R-2133 (contre-lecture d'un socle ; aucune valeur de sonde de 7a) ; R-2131 nomme une session du bras d'attaque : rien n'en est utilisé.
- Clone public : `grep NON_COUVERT_V9 orchestrator/pole/nul_v9.py` (4 lignes affichées, dont un fragment de la description du v9, code public) ; seul le nom de la constante et sa ligne sont utilisés.
- `ls` (non récursif) des dossiers de la course et du verdict : noms de fichiers seulement.

## 7. Interdits tenus

Aucun chemin interdit ouvert ni parcouru ; aucune recherche récursive ; ni `env`, ni `printenv`, ni `set`, ni `export -p`, ni `/proc/*/environ` ; aucune valeur de clé ; aucun appel externe hors du `fetch` nommé ; aucune autre commande git qui écrive (lectures par `rev-parse`, `ls-tree`, `log`, `status --no-optional-locks`, `hash-object` sans `-w`) ; aucune dépense ; aucune suite d'essais lancée ; heures par `date -u`. Fichiers écrits : les quatre sorties de `/home/user/page-a1v4/`, rien d'autre.
