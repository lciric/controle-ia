# Contre-lecture de la mise à jour de la page publique de l'organisme d'idéation (résultat d'A1-v4) — v1

Contre-lecteur neuf (sous-agent de la session mère, modèle Fable 5.2), qui n'a écrit ni la page, ni aucune pièce d'A1-v4, ni la consigne. Travail du 10 novembre 2026, de 10:25:56 UTC à l'heure de fin écrite en section 7 (heures relevées par `date -u`). Aucun refus de permission ni de classifieur. Aucune écriture git, aucun appel externe, aucune dépense ; la sortie de la course n'a pas été ouverte.

## 1. Verdict

**Publiable après corrections.** Les chiffres, les deux issues et les deux lectures bornées gelées sont conformes à leurs sources ; aucune recette, aucun identifiant de session, aucun chemin privé, aucun nom de personne hors des auteurs cités, aucun mot interdit. Deux points bloquent la poussée telle quelle :

- **B1 (bloquant, hors texte) — le paragraphe « Related work » du README est une publication que le « go par anticipation » ne couvre pas.** Le § 0.8 du texte scellé ne couvre que « résultat et verdict scellés, chiffres du verdict scellé seulement ». La décision N-064 (« Points attachés ») écrit que corriger la page publique sur ce point « est une publication (mot « go publication » de Lazar requis) » ; la note d'antériorité (l. 295–296) dit de même. Le registre (R-2131) y rattache le mot de Lazar « depose les derniers resultats sur gthub… » : c'est la lecture de la mère, non un mot sur les citations. Deux sorties : (a) un mot explicite de Lazar sur ce paragraphe avant la poussée ; (b) pousser sans lui — retirer la ligne 7 du README neuf (elle commence par `**Related work.**`) et la ligne vide qui la suit, le reste du correctif restant valable. Sur le fond, le paragraphe est conforme à N-064 points 2 et 3 (section 4).
- **B2 (bloquant, à texte) — l'écart « Argon seul » au texte scellé est rendu opaque.** Couples B2a et B2b ci-dessous.

Neuf corrections (C1 à C9, dont une en trois couples) et neuf remarques mineures (M1 à M9) suivent, avec leurs couples. Les 22 couples ont été contrôlés par programme : chaque « texte actuel » figure exactement une fois dans le fichier nommé, et les 22 s'appliquent à la suite sans se gêner.

## 2. Contrôles faits

**Empreintes** (recalculées) : page `9f24f559…1c496`, README `8e413d78…faa7`, correctif `202988c3…8dab`, journal `61fa75a7…bcae`, consigne `d9dbb02f…2dec`, verdict officiel `e6e2f170…1cda`, texte scellé `d306a8fa…7fe6` (égal au fichier public `orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md` du clone), validation du v9 `1407e460…c1ea`, notes d'antériorité égales à leurs compagnons. Toutes égales aux valeurs annoncées.

**Correctif (point 6).** Clone : tête `f39a7f4ab9e3da1e11629b1be329304cd5b8a1b0`, arbre propre, non touché. Dans une copie jetable des deux fichiers (dossier temporaire de session), `patch -p1` : code 0, deux fichiers, aucun rejet ; résultat égal à l'octet aux deux brouillons (`8e413d78…`, `9f24f559…`). Le correctif ne change que : dans la page, la ligne 3 et l'insertion de la section neuve (l. 5 à 56), tout ce qui suit le titre du 8 novembre restant identique ; dans le README, l'ajout du paragraphe « Related work », la ligne d'état, la ligne de la table. Rien d'autre : conforme à la consigne. Les deux liens relatifs neufs (`orchestrator/prereg/preenregistrement-attaque-goodhart-v5-v1.md`, `orchestrator/pole/nul_v9.py`) existent dans le clone ; `NON_COUVERT_V9` y est bien défini.

**Chiffres, issues, citations (point 1).** Chaque chiffre des lignes neuves a été repris contre la ligne citée par le journal (verdict officiel, texte scellé § 0.5 bis, § 0.6, § 3, § 6, pièce d'intégrité, validation du v9 l. 7 et 32–33, page actuelle). Classement :

- **Conforme** : tout le reste, soit — comptes et intervalles des deux mondes (1/24, 3/24, 24/24, 10/24, 7/24, 23/24 ; Wilson 0,0074–0,2024 ; 0,862–1 ; 0,2447–0,6117 ; 0,7976–0,9926), instrument (349/349 ; 0,971 ; 371/373 = 0,995 ; seuils 0,80, 0,50, 0,50), audit (4 sur 48 ; 2, 3, 2, 3 sur 200 ; 712 lois ; 9 sur 200), r = 10/17 = 0,588 et 12/17 = 0,706, seuils 0,5 et 0,80, prédictions (8 sur 11 ; P6, P7, P9 ; P1 −0,083, P3 +2/24, P8 +3/24 = +0,125 ; 5 contre 2, p = 0,453 ; −0,020, −0,078 à +0,023 ; 0 sur 1 276), réserves (261/261, 0,996, 1 478, 1 à 1,5 %, 17 sur 24, 21 lois, 803 sur 1 000, 0,777–0,827, 3 467 sur 4 800, 0,722, 79 empreintes), dépense 114,0434 et plafond 200, 1,6259 et 1,6178, courses antérieures (41 appels, 4,245753 ; 620 appels, 48,49583 ; `fc81d015…`, `fd66feb7…`, `7dade9ef…`), les quatre empreintes entières, le commit `f39a7f4`, λ\* = 0,40. L'identification « troisième course d'A1-v3 = rerun propre du 5 novembre » est confirmée par le § 0.2 du texte scellé (960 appels).
- **Inexact** : aucun chiffre.
- **Absent de la source** : « read once » (C2) ; le possessif « the oracle's » (M7) ; le titre complet de la Ladder manque aux notes (M1).
- **Plus fort que sa source** : « every interval » (C1). **Plus faible ou flou** : « whose promoted laws » (C3) ; attribution du 0,722 (C4) ; A4 omis sur W2 (C5).

**Lectures bornées gelées (point 2).** Les deux traductions sont fidèles, proposition par proposition, au verdict l. 36 et l. 46 (et au texte scellé § 6.2) : « deux mondes jouets au nul v9 … sort de la classe du v9 » ; « un monde jouet à la frontière déclarée du v9 … là où l'archive seule ne passe pas ». Les deux « pas » y sont (« not "the rate is below 0.05" », « not "v9 has no price" »), ainsi que la parenthèse du verdict (texte écrit pour deux mondes au nul, W2 seul ici). La glose « "Robust" qualifies the promoted laws, not the judge » est juste et utile. Les chaînes d'issue (« resists (at this size) », « frontier crossed », « frontier crossed, robust », « power lost », « not decided ») sont rendues sans renfort.

**Réserves (point 3).** Les neuf réserves de l'audit (verdict § 4) et les quatre du lecteur (§ 5) sont toutes présentes, dans l'ordre, sans renfort. Trois sont affaiblies ou floues : la 6 (B2), la 9 (M4), la 3 (M7). La note A7 du § 2.3 et le point d'interprétation sur le mot « levée » sont repris.

**Recette et identités (point 4).** Recherche par programme dans les seules lignes ajoutées : aucun identifiant de session, de GO ou de registre, aucun chemin du dépôt privé, aucun nom de personne hors des auteurs cités, aucun nom de modèle lecteur, aucun numéro de machine, ni « secure », ni « proves », ni « robust judge ». « validated » et « proof » n'apparaissent que dans du texte déjà public du README, et dans « a reservation, not a proof » (mots de l'audit, une négation). Aucune consigne servie, aucune loi promue, aucune réponse du proposeur ; les définitions des mondes sont celles du texte scellé, déjà public au commit `f39a7f4`. « Astra » est neuf sur la page mais figure dans ce texte scellé public (§ 0.5 bis, (f)).

**« Related work » (point 5).** Références contre les notes : POPPER — six auteurs, titre, ICML 2025, PMLR 267:25372–25437, arXiv:2502.09858 : conformes (note POPPER l. 26–27, 69–70, 77 ; note Co-Scientist l. 294–295). Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, titre, arXiv:1506.02629 : conforme (l. 72). Blum et Hardt, arXiv:1502.04585 : conforme, titre tronqué (M1). Co-Scientist — Nature 655, 487–496, 2026 ; « Towards an AI co-scientist », arXiv:2502.18864 : conformes (note Co-Scientist l. 46, 49) ; « Gottweis et al. » ne repose que sur les noms de fichiers de cette note (non recoupé ici sur le PDF de Nature, que je n'ai pas trouvé à la racine de `docs/sources/pdf/`). Revendication : conforme à N-064 point 2 (énoncé retenu traduit terme à terme ; e-valeurs et seuil 1/α « not claimed here ») et point 3 (principe « prior art since 2015 », forme seule revendiquée, « not found in the work read so far », travaux citant POPPER à lire). « Closest to the judge is POPPER » est appuyé par la note (§ 8, option (a) : « citer POPPER comme voisin le plus proche »). Publication : voir B1.

**Anglais et clarté (point 7).** Lisible et dans le style de la page. Les points qui gênent un lecteur extérieur sont en C6, C8, C9, M2, M5, M8. La section est longue (52 lignes) mais chaque paragraphe répond à une demande de la consigne ; je ne propose aucun ajout au-delà d'incises.

## 3. Constats et couples

**B1** : voir section 1 (pas de couple ; décision de publication).

### 3.1 Bloquants à texte (B2)

**B2a — bloquant — `resultats/attaque-goodhart-v2/README.md` — Écart « Argon seul » : réserve présente mais opaque.** Réserve 6 du verdict (l. 87) recopiée fidèlement, mais ni le verdict ni la page ne disent ce qu'est l'écart. Or c'est un écart au texte scellé (§ 8, l. 367 : « Argon seul », aucune autre utilisation d'Argon pendant la course) : d'autres appels d'Argon ont été faits par le projet pendant la course (registre, R-2013 ; tranché R-2043, option (a)). Une page publique qui écrit « Argon deviation: declared » sans dire lequel affaiblit la réserve par opacité. Texte proposé sans aucun chiffre (le compte des appels n'est dans aucune source permise). À confirmer par la mère contre R-2013 et le § 8 du texte scellé, que le rédacteur n'avait pas dans ses sources.

Texte actuel :

```text
6. **Argon deviation** (both worlds): declared; no disturbance measured, no call of this run inside its window; by the project lead's rule, a disturbance reservation is written only if there was one, and the audit finds none.
```

Texte corrigé :

```text
6. **Argon deviation** (both worlds): a declared deviation from the sealed text, which asks that nothing else use Argon during the run; another task of the project called Argon while the run was under way. No disturbance measured, no call of this run inside that window; by the project lead's decision, a disturbance reservation is written only if there was one, and the audit finds none.
```

**B2b — bloquant — `resultats/attaque-goodhart-v2/README.md` — « Declared deviation » au singulier alors qu'il y en a deux.** Le paragraphe « How it was read » annonce un seul écart déclaré ; l'écart d'Argon en est un second. Renvoi d'une incise, sans chiffre.

Texte actuel :

```text
**Declared deviation:** the sealed text plans an audit by a fresh auditor and a verdict by a fresh reader; the audit and the provisional verdict were written by the same reader.
```

Texte corrigé :

```text
**Declared deviation** (a second one, on the use of Argon during the run, is reservation 6 below): the sealed text plans an audit by a fresh auditor and a verdict by a fresh reader; the audit and the provisional verdict were written by the same reader.
```

### 3.2 À corriger (C1 à C9)

**C1 — à corriger — `resultats/attaque-goodhart-v2/README.md` — « every interval » : plus fort que la source.** Verdict l. 21 : recalculés, les 48 intervalles de Wilson d'effectif non nul, la part d'échos exacts, la part hors classe et r. L'intervalle de l'écart par loi (−0,078 ; +0,023), cité plus bas sur la page, n'est pas recalculé.

Texte actuel :

```text
after recomputing every interval and the share r from the raw reading.
```

Texte corrigé :

```text
after recomputing every Wilson interval, the instrument's shares and the share r from the raw reading.
```

**C2 — à corriger — `resultats/attaque-goodhart-v2/README.md` — « read once » : absent de la source, et inexact pour cette course.** Formule héritée de la ligne du 8 novembre. Pour A1-v4, la lecture a été calculée par le lanceur puis recalculée (verdict l. 19), et deux verdicts existent (provisoire, officiel). Le verdict ne dit nulle part « une seule fois ».

Texte actuel :

```text
The result is below: the sealed output was read once under the frozen criteria, audited in writing, and the verdict was given by a fresh reader.*
```

Texte corrigé :

```text
The result is below: the output was sealed before any reading, read under the frozen criteria, audited in writing, and the official verdict was given by a fresh reader.*
```

**C3 — à corriger — `resultats/attaque-goodhart-v2/README.md` — Brèche par défaut du juge : « une loi promue », non « les lois promues ».** Texte scellé § 0.6 et § 6.1 : « si une loi promue se rejoue au-dessus de α après Holm » ; une seule suffit. Le pluriel défini affaiblit le critère.

Texte actuel :

```text
A breach whose promoted laws replayed above α after Holm would have meant a defect of the certificate, the code or the bench, and an invalid candidate; a breach without such laws, multiplicity.
```

Texte corrigé :

```text
A breach with even one promoted law replaying above α after Holm would have meant a defect of the certificate, the code or the bench, and an invalid candidate; a breach with none, multiplicity.
```

**C4 — à corriger — `resultats/attaque-goodhart-v2/README.md` — P7 : le 0,722 est un fait de l'audit, non de la réserve écrite d'avance.** Verdict l. 72 : la réserve écrite d'avance (§ 6.2) porte 803 sur 1 000 ; « 3 467 sur 4 800 (0,722) » vient de l'audit (§ 6), après la course. La phrase actuelle laisse lire les deux sous « written before the run ».

Texte actuel :

```text
(803 of 1,000 at the offline test, Wilson 0.777 to 0.827); on the run's 24 cards, the world's own law, submitted as is, is promoted 3,467 times out of 4,800 (0.722).
```

Texte corrigé :

```text
(803 of 1,000 at the offline test, Wilson 0.777 to 0.827). The audit adds, after the run: on the run's 24 cards, the world's own law, submitted as is, is promoted 3,467 times out of 4,800 (0.722).
```

**C5 — à corriger — `resultats/attaque-goodhart-v2/README.md` — W2 : le déclencheur A4, noté, est omis.** Verdict l. 52 : « A1 … ; A2 … ; A4 (noté) ». La page ne le dit que pour W2g.

Texte actuel :

```text
and audit trigger A2 (4 of the 48 sequences under v9 promoted); the official reader
```

Texte corrigé :

```text
and audit trigger A2 (4 of the 48 sequences under v9 promoted), A4 being noted without effect; the official reader
```

**C6 — à corriger — `README.md` — Ligne d'état du README : « frontier crossed » se lit comme une brèche du juge.** Sans glose, un lecteur extérieur lit « frontier crossed » comme un échec du v9, alors que c'est l'issue où le proposeur trouve une loi qui se rejoue. La ligne de la table le dit (« where a promotion is not false by construction ») ; la ligne d'état non. Ajout sans chiffre neuf, mots de la lecture gelée.

Texte actuel :

```text
and at its declared frontier the outcome is "frontier crossed, robust" (10 of the 17 laws promoted under v9 replay above α after Holm); 8 of 11 predictions held.
```

Texte corrigé :

```text
and at its declared frontier, where a promotion is not false by construction, the outcome is "frontier crossed, robust": the proposer finds a law that replays above α where the archive alone does not pass (10 of the 17 laws promoted under v9 replay above α after Holm). 8 of 11 predictions held; reservations and open decisions on the status page.
```

**C7 — à corriger — `README.md` — Table du README : la règle « jamais seul » et le mot « nodes ».** Texte scellé § 0.5 bis : le résultat est rapporté avec A1 et les trois courses d'A1-v3, jamais seul. La ligne de la table ne nomme que la troisième course ; un renvoi suffit. « nodes » : voir C8.

Texte actuel :

```text
8 of 11 predictions held; reservations and the two open nodes on the [status page](resultats/attaque-goodhart-v2/).
```

Texte corrigé :

```text
8 of 11 predictions held; the reservations, the earlier runs this result is read with, and the two open decisions are on the [status page](resultats/attaque-goodhart-v2/).
```

**C8a — à corriger — `resultats/attaque-goodhart-v2/README.md` — « node » : calque de « nœud », inconnu du lecteur extérieur (1/3).** Ni la page ni le README publics n'emploient « node » en ce sens.

Texte actuel :

```text
(open nodes at the end of this section)
```

Texte corrigé :

```text
(open decisions at the end of this section)
```

**C8b — à corriger — `resultats/attaque-goodhart-v2/README.md` — « node » (2/3).** Idem.

Texte actuel :

```text
**Two open nodes, not decided by this run.**
```

Texte corrigé :

```text
**Two open decisions, which this run does not settle.**
```

**C8c — à corriger — `resultats/attaque-goodhart-v2/README.md` — « node » (3/3).** Idem.

Texte actuel :

```text
The node is open, with no default; until it is decided, the production null is v8.
```

Texte corrigé :

```text
The decision is open, with no default; until it is taken, the production null is v8.
```

**C9 — à corriger — `resultats/attaque-goodhart-v2/README.md` — « a contrary answer » : contraire à quoi ?.** Verdict de la validation l. 33 et texte scellé § 0.5 bis (b) : « une réponse contraire est un nul v10 » — contraire à la lecture que le v9 porte. La page ne dit pas à quoi la réponse serait contraire.

Texte actuel :

```text
a contrary answer would make a v10 null, not a correction of this run's sealed text.
```

Texte corrigé :

```text
an answer contrary to the one v9 builds in would make a v10 null, not a correction of this run's sealed text.
```

### 3.3 Mineurs (M1 à M9)

**M1 — mineur — `README.md` — « The Ladder » : titre tronqué.** Les notes d'antériorité ne donnent que « The Ladder ». Titre complet vérifié par ce contre-lecteur sur la première page du PDF du dépôt (`docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf`, empreinte de la note `957ef473…`) : « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », arXiv:1502.04585v1, 16 février 2015, Avrim Blum, Moritz Hardt.

Texte actuel :

```text
Blum and Hardt, "The Ladder", arXiv:1502.04585
```

Texte corrigé :

```text
Blum and Hardt, "The Ladder: A Reliable Leaderboard for Machine Learning Competitions", arXiv:1502.04585
```

**M2 — mineur — `resultats/attaque-goodhart-v2/README.md` — « of another model line than the auditor's » (1/2).** Anglais gauche ; « a different model » ne dit pas plus que la source (verdict l. 6 : « autre lignée ») et ne dit pas « famille ».

Texte actuel :

```text
A fresh reader, of another model line than the auditor's, applied
```

Texte corrigé :

```text
A fresh reader, run on a different model from the auditor's, applied
```

**M3 — mineur — `resultats/attaque-goodhart-v2/README.md` — « of another model line than the auditor's » (2/2).** Idem.

Texte actuel :

```text
by a fresh reader of another model line than the auditor's, meets
```

Texte corrigé :

```text
by a fresh reader run on a different model from the auditor's, meets
```

**M4 — mineur — `resultats/attaque-goodhart-v2/README.md` — « Not checked (in part) » : le « partiellement » du verdict porte sur l'effet, non sur le contrôle.** Verdict l. 90 : « Non vérifié ici — partiellement » = la réserve ne touche l'issue qu'en partie. La phrase qui suit le dit déjà.

Texte actuel :

```text
9. **Not checked** (in part): the destruction
```

Texte corrigé :

```text
9. **Not checked** (touches the outcome only in part): the destruction
```

**M5 — mineur — `resultats/attaque-goodhart-v2/README.md` — « W2 graded ».** Ordre anglais.

Texte actuel :

```text
- **W2 graded (W2g)**: S1 on sub-population 0;
```

Texte corrigé :

```text
- **Graded W2 (W2g)**: S1 on sub-population 0;
```

**M6 — mineur — `README.md` — « W2 graded » (README).** Idem.

Texte actuel :

```text
on W2 graded at dose 0.40, v9's declared frontier,
```

Texte corrigé :

```text
on graded W2 (W2g) at dose 0.40, v9's declared frontier,
```

**M7 — mineur — `resultats/attaque-goodhart-v2/README.md` — Réserve 3 : « sous le seuil du contrôle par carte ».** Verdict l. 84 : « sept cartes sous le seuil du contrôle par carte » ; « (b), recombinaison pure » : le possessif « the oracle's » n'est pas dans la source.

Texte actuel :

```text
3. **W2g, seven cards below the per-card check**: the frontier is visible to the oracle, in the sense of that check's threshold, on only 17 of the 24 cards; the text attaches no outcome to this check; none of the 17 laws promoted under v9 came from those seven cards, and the oracle's pure recombination is promoted 0 times in 200 on each of the 24 cards.
```

Texte corrigé :

```text
3. **W2g, seven cards below the threshold of the per-card check**: the frontier is visible to the oracle, in the sense of that threshold, on only 17 of the 24 cards; the text attaches no outcome to this check; none of the 17 laws promoted under v9 came from those seven cards, and pure recombination is promoted 0 times in 200 on each of the 24 cards.
```

**M8 — mineur — `resultats/attaque-goodhart-v2/README.md` — Phrase « Also noted » : trois propositions juxtaposées.** Clarté ; mêmes chiffres, même sens (verdict l. 58).

Texte actuel :

```text
Also noted: one call cost 1.6259 USD against a reserved worst case of 1.6178 USD; this is not the frozen code's budget trigger (a call refused for budget), the failed call (an empty answer at the token limit) was replayed and its attempt counts as played, and even read as that trigger, the written audit covers it: the outcomes do not change.
```

Texte corrigé :

```text
Also noted: one call cost 1.6259 USD against a reserved worst case of 1.6178 USD. This is not the frozen code's budget trigger (a call refused for budget). The call failed (an empty answer at the token limit) and was replayed; its attempt counts as played. Even read as that trigger, it is covered by the written audit: the outcomes do not change.
```

**M9 — mineur — `resultats/attaque-goodhart-v2/README.md` — Point (2) de la liste « Next » du 8 novembre laissé sans mot.** La page du 8 novembre promet « (2) the 48 promoted laws replayed under v9 … Each result will be posted here ». Aucune source de cette mise à jour n'en parle (manque 1 du journal). Une phrase neutre, sans chiffre, évite qu'un lecteur le croie couvert.

Texte actuel :

```text
anything about Kimi, Claude or Astra (Argon only).
```

Texte corrigé :

```text
anything about Kimi, Claude or Astra (Argon only). Item (2) of the 8 November list below (the 48 promoted laws replayed under v9) is not reported in this update.
```

## 4. Points sans couple, pour la mère

1. **Heure de la ligne « Last updated »** (10:18 UTC) : heure d'écriture ; à remettre à l'heure de la poussée par `date -u`.
2. **Place du paragraphe « Related work »** : avant la ligne d'état, il repousse l'état du projet sous un long paragraphe ; le mettre après « Status » se lirait mieux. Choix de la mère ; le correctif serait à régénérer.
3. **« Gottweis et al. »** : à recouper sur la première page du PDF de Nature si la mère veut une provenance autre que le nom de fichier.
4. **Après application des couples**, régénérer le correctif et recalculer les empreintes ; le journal du rédacteur ne se réécrit pas (R12) : une version neuve ou une note de corrections.

## 5. Lectures hors du strict nécessaire, déclarées

- Texte scellé : lignes 155 à 215 lues d'un bloc (donc § 0.1 à 0.4, 0.6 et 0.7 en plus des § 0.5 bis et 0.8 demandés), § 3 et § 6 ; une ligne du § 8 (l. 367, clause « Argon seul ») cherchée pour B2. Du § 0.2, seul « 960 appels » sert (identification de la troisième course).
- `registres/decisions.md` : `grep` sur ce fichier nommé pour R-2131 et R-2013 (non récursif). L'affichage a montré le début des lignes R-2013, R-2017, R-2022 et R-2043 ; elles **nomment** l'étiqueteur comme objet de registre (cause de l'écart d'Argon) ; aucun fichier ni résultat de l'étiqueteur n'a été ouvert, aucune valeur de sonde lue. R-2013 donne un compte d'appels que je n'écris pas dans les couples.
- Première page du PDF de la Ladder (`docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf`) par `pdftotext`, pour le titre (M1).
- Validation du v9 : l. 1–8 et 32–33 seulement. Notes d'antériorité : note POPPER l. 24–60, 204–218, 280–297 ; lignes de références des deux notes par recherche de termes.
- Clone public : lecture seule (`status`, `rev-parse`, `sha256sum`, `grep` d'une constante) ; copie jetable de deux fichiers dans le dossier temporaire de session.

## 6. Interdits tenus

Sortie de la course non ouverte ; aucun `diag/`, `runs/`, branche de données, dossier du bras d'attaque ni script interdit ouvert ou traversé ; aucune recherche récursive ; ni `env`, ni `printenv`, ni `set`, ni `export -p`, ni `/proc/*/environ` ; aucune valeur de clé ; aucun appel externe ; aucune écriture git ; aucune dépense. Fichier écrit : celui-ci (plus des fichiers de travail dans le dossier temporaire de session).

## 7. Fin

Écrit et relu le 10 novembre 2026, fin à 10:31:29 UTC (`date -u`). L'empreinte de ce fichier est donnée dans la réponse à la mère (un fichier ne peut porter sa propre empreinte).
