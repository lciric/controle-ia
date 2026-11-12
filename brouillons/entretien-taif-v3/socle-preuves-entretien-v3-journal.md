# Journal — socle de preuves pour l'entretien avec le Transformative AI Fund — v3

- Rédacteur : sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, Claude Opus 5.5 (`claude-opus-5-5`) ;
  je n'ai écrit ni les v1 et v2 du socle, ni leurs journaux, ni la contre-lecture de la v1, ni aucun rapport de niveau 3.
- Heures (`date -u`) : interdits communs v2 lus et hachés 11:01:44 ; PDF cités vérifiés contre leurs compagnons 11:04:51 ;
  citations recontrôlées 11:05:19, 11:07:28 ; début de la rédaction 11:05:24 ; message de la mère (C5, lot 1 sur HC2) reçu vers
  11:07 ; message de la mère (taux de calibration) reçu vers 11:10 ; fin du journal : voir la dernière ligne (heure relevée
  dans la commande qui l'écrit, juste avant le scellement des deux fichiers).
- Sorties : `brouillons/entretien-taif-v3/socle-preuves-entretien-v3.md` et ce journal, scellés par
  `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller` (compagnons `.sha256`). La v2 (`3f078bca…`) et son
  journal (`e84fcb19…`) restent intacts (règle 12 ; empreinte de la v2 recalculée après rédaction : inchangée). Aucune autre
  écriture au dépôt ; outils et copies de travail dans le dossier temporaire de la session.
- Mandat : la v2 plus les corrections établies sur PDF par le niveau 3 ; rien de plus fort qu'une pièce lue sur PDF ; pistes
  non lues sur PDF marquées **[NON OPPOSABLE]** et tenues hors des affirmations ; sur l'organisme, n'écrire que ce qui vaut
  sous les deux options de Lazar. Ajouts de la mère pendant la rédaction : intégrer C5 et le rapport du lot 1 sur HC2 (n'écrire
  que ce qui vaut sous les deux issues de HC2) ; n'écrire aucun taux de calibration.

## 1. Corrections : texte v2 → texte v3, source, rapport

Abréviations des rapports (empreintes complètes au § 2) : B1, B3, C1, C2, C3, C4, C5 = `docs/etat-de-l-art/niveau3-v1/rapports/rapport-<lot>-…-v1.md`
(branche `prep/etat-de-l-art-niveau3-v1`) ; L1-HC2 = `docs/sources/lecture-pdf-niveau3/rapport-lot1-HC2-mirage-karne-v1.md`
(branche `prep/etat-de-l-art-niveau3-pieces-v1`). « l. » = ligne du rapport. Pages = pages du fichier PDF.

| Kn | lieu v3 | texte v2 | texte v3 (abrégé) | source (chemin, page) | rapport, ligne |
|---|---|---|---|---|---|
| K0 | § 0, ligne 4 (neuve) | — (verdict en trois lignes) | quatrième ligne : trois erreurs du texte envoyé ; contre-résultats ; H1, H2, HC2 occupées en partie ; organisme : séparer proposeur et juge n'est pas à nous ; nœud non tranché | résumé de K1 à K21 | R-2177 ; B1 l. 15 ; C1 l. 12 ; C4 l. 10-46 ; C5 l. 11-13 ; L1-HC2 l. 7 |
| K1 | § 1.1, énoncé | « un moniteur qui note chaque action seule échoue par construction » | « un moniteur qui compare chaque action seule à un seuil peut être mis en échec par construction par une attaque qui garde la loi de chaque score (2606.10456 v2, proposition 1, p. 3 ; résumé, p. 1) — sur sa construction, vrai pour le maximum et le seuil, faux pour la somme » | `docs/sources/pdf/2606.10456v2.pdf`, p. 1 (« *defeated by construction* »), p. 3 (proposition 1) | B3 l. 32, l. 82 (n° 1), annexe Q1, Q2 (l. 176-177) ; C2 l. 81-87 |
| K1b | § 1.1, énoncé | « n'est établi dans aucune source vérifiée à ce jour » | « … sur du sabotage diffus, n'est établi dans aucune pièce lue à ce jour » ; renvoi aux comparaisons publiées, de signes contraires (§ 1.1 bis) | 2606.17478 p. 30 ; 2610.12445 p. 7, 19 | C1 l. 307-336 ; C5 l. 90-142 ; **correction de ce rédacteur**, appuyée sur ces rapports |
| K2 | § 1.1, « la soutiendrait » | « sa conclusion que la surveillance y paraît « *less promising* » » | prémisse, non conclusion ; reprise de trois travaux ; vise toute surveillance et l'incrimination ; le papier ne mesure aucun moniteur ; joue aussi contre un moniteur interne | `docs/sources/pdf/2606.08892v2.pdf`, p. 2 | B3 l. 19-23, l. 71-76, l. 84 (n° 3), annexe T1 (l. 127) |
| K2b | § 1.1, « la réfuterait » | « une base boîte noire bon marché qui attrape un sabotage réellement diffus » | ajout « à savoir » : une consigne d'un modèle faible résiste à l'attaque de Terekhov et al. (p. 1) ; signal d'entraînement, borné par les auteurs (p. 2) | 2606.08892v2, p. 1 (T4), p. 2 (T8) | B3 l. 23, annexe T4, T8 (l. 130, 178) |
| K3 | § 1.1, « chiffres exacts » | « 2512.07810 […] contre-résultat (les sondes manquent le sabotage agentique d'Oak, p. 17) » | « *sandbagging* » verrouillé par mot de passe, pas sabotage ; p. 17-18 ; contre-résultat partiel (Cedar vu, Oak manqué) ; moyenne sur les jetons (p. 16) ; équipe rouge sans droit d'entraîner contre les sondes (p. 7) ; aucun chiffre pour Oak ; « voisin le plus direct » = jugement de la synthèse | `docs/sources/pdf/2512.07810v1.pdf`, p. 1, 7, 16, 17, 18 | B3 l. 25-30, l. 53-69, l. 86-87 (n° 5, 6), annexe A1, A3, A5, A8, A10, A12 ; C1 l. 65-123 |
| K4 | § 1.1, « la soutiendrait », « la réfuterait » | « la conjonction revendiquée nulle part » ; conjonction sans voisin nommé | « dans aucune pièce lue » ; E-valuator nommé (garantie valable à chaque pas d'une trajectoire d'agent, boîte noire, p. 1) ; SafeDream nommé | `docs/sources/pdf/2512.03109v2.pdf`, p. 1 ; `2604.16824v1.pdf`, p. 4-5 | B3 l. 34, l. 106, annexe E1, E2 ; C1 l. 223-249 |
| K5 | § 1.1, « pièces » et « état » | « pages … non revérifiées ici » | rapports de niveau 3 et PDF ajoutés aux pièces ; pages contrôlées sur PDF par B3 (55 citations, 0 échec) ; critère 8 toujours non clos | B3 tableau des pièces | B3 l. 13, l. 36, l. 40-51 |
| K6 | § 1.1 bis (neuve) | — | table des contre-résultats publiés, avec la réserve de C1 (sondes par réponse, sans accumulation) : 2512.07810, StateWitness, Gao, HELIOS, SafeDream, papier C | 2512.07810 p. 3, 7, 16, 17, 18, 27, 43 ; 2606.17478 p. 7, 30 ; 2610.04575 p. 1, 6, 7 ; 2604.01151v5 p. 18, 27, 30 ; 2604.16824 p. 3-7, 14 ; Panin p. 6 ; 2603.15809 p. 15, 17 | C1 l. 8-13, 65-336, 364-397 ; B3 l. 111-115 ; C3 l. 11-26, 390-416 |
| K7 | § 1.6, écart 9 | « exacte à la lettre … HELIOS … POPPER » | toujours exacte pour les énoncés du texte envoyé, mais plus un tableau fidèle : à dater (« au 7 octobre ») ; H1, H2, HC2, L, T occupés en partie ; E-valuator ; collision élargie de l'organisme ; pièce mal décrite des « huit pièces » | B1 § 7 ; C1 § 3 ; C2 § 0 ; C5 § 3 ; L1-HC2 § 3 | B1 l. 207-213 ; C1 l. 12, 351 ; C2 l. 11-12 ; C5 l. 9-13 ; L1-HC2 l. 7 |
| K8 | § 1.6, écart 11 | « pour la somme, non pour le maximum » | plus : proposition 1 vide à la lettre, c'est la proposition 2 (a) (p. 4), le résumé (p. 1) et la conclusion (p. 9) qui ne tiennent pas ; écart petit au point mis en avant (0,072 contre 0,05) ; calcul en forme close concordant ; tableau de l'article : 0,048 pour la moyenne à 1 % (p. 6) ; attaquant adaptatif déjà montré (p. 6-7) | `docs/sources/pdf/2606.10456v2.pdf`, p. 1, 3, 4, 6, 7, 9 | C2 l. 16-17, 48-93 ; B1 l. 49, 173-188 |
| K9 | § 1.6, écart 13 | organisme absent du texte envoyé | si présenté : citer Qu, Chen, Wang ; ne jamais présenter comme nôtre la séparation proposeur / juge | 2609.27051 p. 1, 2 | C4 l. 10-46 ; R-2177 |
| K10 | § 1.6, écart 15 (neuf) | — | « *Thresholds are therefore calibrated on whole honest episodes* » (texte envoyé l. 91-92) : méthode publiée d'E-valuator, à citer, non à revendiquer | `docs/sources/pdf/2512.03109v2.pdf`, p. 3, 4, 8 | C2 l. 18, 132, 165, annexe G1-G3 |
| K11 | § 1.6, écart 16 (neuf) | — | Ramtin et al. « *covers neither total budgets* » : ne borne pas le budget, chiffre le dommage cumulé avant détection | `docs/sources/pdf/2601.20022v2.pdf`, p. 3, 10, 11 | B1 l. 55 ; C2 l. 107-113 |
| K12 | § 1.1 bis, lignes neuves | — | « Caught in the Act » (2610.12445) : voisin le plus proche de H1, diffus écarté du banc par construction (p. 6, 19), contre-résultat de taille (0,585-0,781 à 2 milliards ; 0,963-0,986 à partir de 27 ; p. 8 ; nous à 8) ; réserves (refus 2 638 sur 5 014, p. 7 ; consigne invisible au moniteur, p. 48 ; 98,8 % du résumé non retrouvé) ; 2607.02510 (seuil unique au niveau d'un test séquentiel, p. 1, 3) ; 2606.06223 (p. 5) ; plafond d'information de Gao (p. 4) | `docs/sources/pdf/2610.12445v1.pdf` (`7e141758…`), `2607.02510v1.pdf`, `2606.06223v2.pdf`, `2610.04575v1.pdf` | C5 l. 11-13, 90-186, 406-420 |
| K13 | § 1.1 bis, ligne neuve | — | HC2 occupée en partie par MIRAGE (2606.10304 v1), résultat non opposable (6 réussites sur 120, p. 20 ; catalogue non itératif) ; Karne : contre-indice pour la sonde du lecteur seulement ; **reformulation de HC2 non écrite** (en attente de Lazar) | branche `prep/etat-de-l-art-niveau3-pieces-v1`, `docs/sources/pdf/niveau3-v1/2606.10304v1.pdf` (`677fe278…`), `2609.05797v3.pdf` (`eb7be6ca…`) | L1-HC2 l. 7-11, 75-92, 161, 176-186 |
| K14 | § 1.7 (neuve) | — | « Ce que nous corrigeons nous-mêmes devant le jury » : trois erreurs du texte envoyé, une ligne chacune, avec la page (voir § 3 de ce journal) | 2605.15377v2 p. 4, 8 ; 2606.10456v2 p. 8 ; 2512.03109v2 p. 1, 4 | B1 l. 15-19 ; C2 l. 163 (divergence) |
| K15 | § 2.4, puce neuve | — (« leur principe est publié depuis 2015 ») | collision Qu, Chen, Wang lue sur PDF (faits, pages, ce qu'elle ne fait pas, réserves) ; ce qui vaut sous les options (a) et (b) ; ce qui attend Lazar ; pistes non opposables | `docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf` (`2a8ded01…`), p. 1, 2, 6, 8, 14, 15, 16, 30 ; 2606.11417 | C4 l. 10-46, 161-186, 330-369, 371-381 ; R-2177 |
| K16 | § 2.4 « Restent », § 3, § 6 point 13 | « go publication » attendu pour le paragraphe des citations | plus : page touchée par la collision, nouveau « go publication » requis | — | R-2177 |
| K17 | § 5, Q1 | « le voisin publié le plus proche rapporte que des sondes manquent un sabotage d'agent (synthèse de niveau 2, l. 56 ; page non revérifiée ici) » | dissimulation de capacités, p. 17-18, Cedar vu ; StateWitness 0,571 contre 0,000 (p. 30) ; 2610.12445 : diffus écarté, faible sous 27 milliards, nous à 8 ; « À ne pas dire » complété | comme K3, K6, K12 | B3 l. 25-30 ; C1 l. 372-373 ; C5 l. 412-420 |
| K18 | § 5, Q5 | « Réponse » et « À ne pas dire » | occupations partielles au niveau 3 à dire ; conjonction de H2 non trouvée ; interdits ajoutés (séparation proposeur / juge, « premier », MIRAGE, formulations en attente) | comme K6, K12, K13, K15 | C1 l. 351 ; C5 l. 26 ; C4 l. 363-369 ; L1-HC2 l. 178 |
| K19 | § 1.3 « chiffres exacts » et « pièces », § 1.2 « pièces », § 6 point 15 | « prédictions : 47 confirmées sur 60 tranchées (0,783), 5 réfutées, 8 non concluantes, sur 235 lignes ; hors du taux : … (`0f1bca5a…` l. 251-268) » | « recompte en cours, aucun taux cité » (réserve « non fidèle » de la session-dépôt sur les tables v4 et v5) ; mention « aucun taux n'en est repris » à côté de `calibration-v3.md` | consigne de la mère | — (réserve de la session-dépôt relayée par la mère, non lue ici) |
| K20 | § 6, point 10 | « Pages de la littérature … non revérifiées ici » | levé par le niveau 3 ; restent les appuis de « *less promising* » et les pistes non opposables, listées | — | B3 l. 36, 117-121 ; C1 § 7 ; C4 § 5, § 9 ; C5 § 5 ; R-2177 |
| K21 | § 6, point 14 (neuf) ; § 7, points 7 et 8 (neufs) | — | décisions de Lazar attendues sur la littérature ; réserves de ce rédacteur v3 | — | R-2177 ; C1 l. 249, 351 ; C4 l. 358-361 ; L1-HC2 l. 180 |

**Compte** : 21 corrections numérotées (K1 à K21), plus K0 (ligne de verdict), K1b et K2b (sous-corrections) — 24 marques en
tout ; les sept points minimaux de la consigne sont couverts : (1) K2 ; (2) K3, K17 ; (3) K1 ; (4) K4 ; (5) K6, K12, K17, K18
(et SafeDream en K4, K6, K7) ; (6) K9, K15, K16, K18 ; (7) K14.

**Écrit sous les deux issues, rien de tranché** : O2 (options (a) et (b) de R-2177 : seul « citer », la non-nouveauté de la
séparation et les faits imprimés sont écrits) ; HC2 (reformulation du lecteur non écrite ; seuls les faits imprimés et la
non-opposabilité de MIRAGE sont écrits).

## 2. Sources lues, avec empreintes

| pièce | chemin | sha256 | contrôle |
|---|---|---|---|
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | égal à la consigne |
| socle v2 | `brouillons/entretien-taif-v3/socle-preuves-entretien-v2.md` | `3f078bcaae8f146e69c99b8a437c7f368616fdaffade7e5336e8f385ddacf766` | compagnon conforme ; inchangé après rédaction |
| journal v2 (en-tête lu) | `brouillons/entretien-taif-v3/socle-preuves-entretien-v2-journal.md` | `e84fcb190d4614a625d566579294e041c32928453d3dfc0034ad667c5238b38e` | compagnon conforme |
| B3 | `…/rapport-B3-tracabilite-socle-v1.md` (branche, `01f6c2f9` puis `8850e438`) | `30f409c944ca1de5f5d001f5e83104696f9e3f70049f2cb2064c8dff16649966` | compagnon conforme ; lu en entier |
| B1 | `…/rapport-B1-tracabilite-programme-texte-envoye-v1.md` | `812f1b535427595c2d8216d7d63a6aa06e34ffac7bfbe8c2bfcba0be0c63e6aa` | compagnon conforme ; lu en entier |
| C1 | `…/rapport-C1-voisin-proche-helios-H1-H2-H3-v1.md` | `89e2edad5dd6c08d6a81bc856d729df2d5f961bf98c2b1d8d93d8ba2c685b452` | compagnon conforme ; lu en entier |
| C2 | `…/rapport-C2-lemme-theoreme-v1.md` | `76475485116b026fd1c966c70f924eb021a8fb1764347e9db85d37e263fcad73` | compagnon conforme ; lu en entier |
| C3 | `…/rapport-C3-loi-de-deference-papier-C-v1.md` | `d7efc7f252b6c9416702952871e5b67a2327ef61f1e4598135602bfa90266bba` | compagnon conforme ; lu l. 1-127 et 337-461 |
| C4 | `…/rapport-C4-organisme-ideation-O1-O20-v1.md` | `164502a3ed94e0adf177e4e15bfd61fc95ea24633dc1c4a2b0cacf9effab1245` | compagnon conforme ; lu en entier |
| C5 | `…/rapport-C5-pieces-recentes-au-depot-v1.md` (commit `8850e438`) | `804cd3a77202d4841d310328ea7b4d7ca7afdd794953aa496f411351173aeddc` | compagnon conforme ; lu en entier |
| lot 1 sur HC2 | `docs/sources/lecture-pdf-niveau3/rapport-lot1-HC2-mirage-karne-v1.md` (branche `prep/etat-de-l-art-niveau3-pieces-v1`, `4e4ad4d0`) | `9996f40cf5614e32c74bc4c97c79a8e88d65c76c6c4635d8ea38d034315c0f4b` | compagnon conforme ; lu en entier |
| texte envoyé | `docs/sources/candidature-taif-2026-10-07/proposal_v2_TAIF_2026-10-07.txt` | `b2458c2d209aaa817ca3c77bfc8ef99288d489ae7b58b747fd8cda6a71e33ca0` | compagnon conforme ; l. 30-37, 84-92, 128-144, 196-202, 258-266 relues |
| synthèse de niveau 1 | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` | `b0b519fe250a839d904e75c66945326d30e47687093852c85eae6355add2cd72` | l. 30 et 103 (E-valuator) ; même empreinte sur `main` et sur la branche |
| registre des décisions (R-2177, l. 2135) | `registres/decisions.md` | `5eed0d05894e0c6837ebd9f58c39b37ff2bf80daa88390f0b99e68e4397e9a9b` (11:03) | registre vivant |
| PDF (compagnons « OK » à 11:04:51 ; non relus en entier) | `docs/sources/pdf/` : 2606.08892v2 `aea0f2d1…`, 2512.07810v1 `77e64bcd…`, 2604.01151v5 `02527fd4…`, 2512.03109v2 `b7a46e4c…`, 2606.10456v2 `aaeedd1e…`, 2604.16824v1 `ad860956…`, 2606.17478v1 `deda43a6…`, 2610.04575v1 `ef50ec54…`, 2605.15377v2 `fe591700…`, 2609.36490v1 `eb6d5bbe…`, 2603.15809v1 `29316c29…`, 2607.02510v1 `eefdaeae…`, 2606.06223v2 `a95da1d5…`, 2610.12445v1 `7e141758…` ; `anteriorite-P-041-v2/c8/` : 2609.27051 `2a8ded01…`, 1506.02629 `dcfbb9aa…`, 1502.04585 `957ef473…`, 2606.11417 `7ae148be…` ; branche des pièces : `docs/sources/pdf/niveau3-v1/2606.10304v1.pdf` `677fe278…`, `2609.05797v3.pdf` `eb7be6ca…` (blobs hachés par `git show`, égaux aux compagnons) | — | — |

## 3. Recontrôle des citations clés (règle 7, règle 5)

Script `/tmp/claude-0/-home-user-controle-ia-travail/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/outils/chk.py`
(hors dépôt) : `pdftotext` de la page, avec puis sans `-layout`, normalisation NFKC, apostrophes, blancs et traits d'union
retirés. Un premier essai sans normalisation des césures échouait sur 7 citations justes (artefacts d'extraction) : écarté.

- **Cas témoins** (attendus en échec, obtenus en échec) : « more promising » au lieu de « less promising » (2606.08892, p. 2) ;
  bonne citation de 2512.07810 à la mauvaise page (p. 9 au lieu de 7) ; bonne citation de 2610.12445 à la mauvaise page (p. 9
  au lieu de 8).
- **33 citations distinctes retrouvées à la page citée** : 2606.08892 p. 2 ; 2512.07810 p. 3, 7, 16, 17, 18 ; 2605.15377
  p. 4, 8 ; 2606.10456 p. 1, 3, 6, 8 (deux) ; 2512.03109 p. 1, 4 ; 2609.27051 p. 1, 2, 6 ; 2606.17478 p. 30 ; 2604.16824 p. 4,
  7 ; 2610.04575 p. 1 ; 2604.01151v5 p. 18 ; 2610.12445 p. 6, 7 (deux), 8 (deux), 19 ; 2607.02510 p. 1 ; 2606.10304 p. 4, 13,
  20. Aucun échec hors des trois cas témoins.
- Les autres citations du socle v3 sont reprises des rapports, qui les ont contrôlées par programme (B3 : 55 ; B1 : 75 ; C1 :
  88 ; C2 : 60 ; C3 : 93 ; C4 : 105 ; C5 : 89 ; lot 1 : 115 ; 0 échec déclaré par chacun).

## 4. Points d'attention, divergences, non-intégrés

1. **Divergence B1 / C2 sur « *synthetic* »** (2606.10456) : B1 (l. 18) le dit contredit par l'imprimé (p. 8, « *real
   traces* ») ; C2 (l. 163) le dit exact (scores de moniteur réels, attaque construite). La ligne 2 du § 1.7 dit « incomplet »
   et donne les deux phrases de la p. 8 : vrai sous les deux lectures. À trancher par Lazar si la phrase est corrigée devant le
   fonds.
2. **Lignes de B1 pour la synthèse de niveau 1** : B1 écrit l. 28 et 80 ; le fichier (`b0b519fe…`, identique sur `main` et
   sur la branche) porte les passages aux l. 30 et 103. Sans effet sur le fond.
3. **Quorum entre familles** : C3 (§ 6, HC5) range le « quorum entre familles de juges » comme occupé par 2607.08066 (p. 1,
   2, 6 : vérificateur d'une autre famille qui annote le contenu) ; C5 (l. 314-315) relève 2610.34435 (« *a reviewer from a
   second vendor catches about two thirds of a Claude reviewer's misses* », p. 1, postérieur à l'envoi). L'erreur 1 du § 1.7
   porte sur l'**attribution** à 2605.15377, qui reste fausse ; si la pièce est dite publiée ailleurs, citer 2607.08066 ou
   2610.34435, pas 2605.15377. Non écrit au socle au-delà de l'erreur elle-même (non demandé, à décider).
4. **E-valuator « additif »** : le processus e d'E-valuator est un produit, dont le logarithme est une somme ; la correction
   s'en tient à ce que le PDF imprime (règle de décision, seuil sur le maximum de la statistique, p. 1, 4) et à la synthèse de
   niveau 1 (« pas de somme cumulée ») ; elle ne dit pas que toute lecture additive serait fausse.
5. **Non intégré, hors mandat** : R-2155 à R-2177 (en dehors de ce que R-2177 dit de la littérature), dont le **calendrier
   resserré de R-2177** (T0.7, la règle « mots et coût », P3-bis et la consigne d'audit visés scellés le 12 au soir ; 7b et
   P3-bis créées le 12 ou le 13 ; lecture des sondes visée vers le 16 au 18) : le § 4 du socle est celui de la v2 et n'en tient
   pas compte. R-2175 (décisions D-1 à D-4) et R-2176 (dossier de l'entretien) non lues.
6. **Non intégré, hors champ du socle** : les autres verdicts de C5 (H5, H7, HC1, HC3 énoncé 1) et de C3 (HC1 à HC6) au-delà
   d'une ligne de contre-résultat ; ils relèvent des préenregistrements. D1, D2, D3 et B2 non lus (non nommés par la consigne).
7. **Taux de calibration** : la réserve « non fidèle » de la session-dépôt n'a pas été lue ici ; elle est rapportée telle que
   la mère l'a transmise. Restent au socle, parce qu'ils ne viennent pas des tables de calibration : « 31 prédictions sur 31 »
   de la simulation (R-025) et « 8 prédictions tenues sur 11 » d'A1-v4 (verdict `e6e2f170…` § 3).
8. **Refus** : aucun contrôle de permissions ni classifieur n'a refusé d'action. Aucun appel externe, aucune dépense, aucune
   écriture git, aucune valeur de clé lue. Aucun chemin interdit ouvert ; aucune recherche récursive (recherches par `git grep`
   avec exclusions, ou sur fichiers nommés).

Fin du journal et de la rédaction (`date -u`, juste avant le scellement) : **2026-11-10 11:12:51**.
