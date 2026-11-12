# Contre-lecture R2 du programme d'entretien Transformative AI Fund v5 — rapport CL1

Contre-lecteur neuf (règle R2) : n'a écrit aucune version du programme d'entretien ni de la ventilation. Modèle servant déclaré
par l'environnement : Opus 5.5. Relevé `date -u` au début de la lecture : 10:57 UTC le 28 octobre 2026.

Pièce relue : `brouillons/entretien-taif-v3/programme-entretien-taif-v5.md`, empreinte recalculée `98434a581e7c…`, identique à
son compagnon `.sha256`. Pièces de contrôle : v4 (`8dbacfe53cfe…`, identique au compagnon), ventilation v2 (`8ab00ab52f4a…`,
identique au compagnon), note de dépenses (`93969946d9c1…`, identique à l'empreinte citée), notes de niveau 2 « collusion entre
agents » et « conscience d'évaluation », lignes R-614 à R-616 de `registres/decisions.md`.

Les numéros de ligne renvoient à la v5 telle qu'empreintée ci-dessus.

---

## (a) Verdict

**Scellable après corrections** — quatre constats bloquants et huit majeurs, tous corrigeables par des retouches locales du
texte ; aucun ne touche le fond du programme. Les corrections bloquantes et majeures doivent être appliquées dans une v6 et
vérifiées par différence avant scellement ; la v5 n'est pas opposable en l'état.

---

## (b) Constats

### Bloquants

**CL1-01 — bloquant — section 5 (anglais), l. 384.** « Our first real white-box test came back **null**, and we published the
null with its power ». Rien n'est publié : le dépôt est privé, la copie publique n'est pas en ligne (section 10, l. 531 et 534 :
« aucune diffusion sans GO » ; « sa mise en ligne est le geste de Lazar ») ; le français de la section 2 (H5) dit « audité, et sa
puissance est chiffrée », pas « publié ». Affirmation fausse, dite au fonds.
*Correction* : « came back null, and we recorded the null, audited and sealed, with its power ».

**CL1-02 — bloquant — section 5 (anglais), l. 386 ; section 3, front B, l. 150.** « Six further measurements are preregistered
on data we have already paid for » ; « six résultats préenregistrés, un signe annoncé d'avance ». Les pistes 7 et 8 (l. 285–286)
disent l'état réel : T0 en version 14, « éditions, contre-lecture, scellement » à venir ; T1 à T5 « à préenregistrer après T0 ».
Aucune des six n'est scellée. Devant un fonds, « préenregistré » se lit « scellé » : c'est le cœur de la crédibilité (R1).
*Correction* : anglais « Six further measurements are being preregistered, each to be sealed and read once, on data we have
already paid for » ; français « six mesures qui seront préenregistrées, chacune avec un signe annoncé d'avance ».

**CL1-03 — bloquant — section 8, l. 456, 475, 480, 484 ; en-tête, l. 10.** Trois défauts sur la demande, le chiffre central de
l'entretien :
- « **Options (chiffres envoyés, les seuls qui existent devant le fonds)** » puis option (c) « ≈ 176 550 USD » : 176 550 n'est
  pas un chiffre envoyé (la ventilation v2, section 1, le donne comme « la demande », nouvelle ; seuls 28 160, 58 630 et
  138 600 ont été envoyés). Même glissement dans l'en-tête, correction (1) : « les chiffres envoyés (58 630 / 138 600 / ≈ 176 550) ».
- « **Tranché (c) par Lazar** (28 octobre, 11:28) » est accolé à l'option (c) réécrite à ≈ 176 550. Or le « go » de 11:28 portait
  sur l'option (c) d'alors, « plancher plus extension » (ventilation v1, 86 130 — ventilation v2, l. 6–10) ; la portée sur le
  scénario ambitieux est une **lecture retenue** des mots de 11:33, que la ventilation v2 demande à Lazar de **confirmer**
  (section 5, point 3) et que l'en-tête de la v5 dit elle-même révocable (l. 42–44 : « un mot de Lazar si c'est une autre lecture »).
- La l. 484–485 ne liste que deux points restants (taux de la revue, nombre de paliers) et omet ce troisième.
Présenter comme décidé par Lazar un montant qu'il n'a pas confirmé, sur un nœud (contact externe, demande de financement),
n'est pas opposable.
*Correction* : titre des options « (paliers : deux envoyés, un nouveau) » ; l. 484 : « (c) tranché par Lazar à 11:28 sous la
forme "plancher plus extension" ; portée sur le scénario ambitieux (≈ 176 550) par lecture de ses mots de 11:33, **à confirmer**
(ventilation v2, section 5, point 3) » ; restaurer les trois points ; en-tête : « remplacé par les chiffres envoyés (58 630 /
138 600) et le palier nouveau ≈ 176 550 ».

**CL1-04 — bloquant — section 3, front D, l. 217–220 ; section 3 bis, piste 29, l. 310.** « Collusion entre agents : zone
**largement vierge** côté boîte blanche — […] **aucun résultat boîte blanche** publié ». La note citée
(`etat-art-niveau2-collusion-agents-v1.md`) décrit elle-même, section 1.8, HELIOS (arXiv 2604.01151, prépublication 2026) :
« sondes d'activation par agent, test composite d'hypothèse », et sa section 4 range « HELIOS (sondes) » dans la ligne
« Détection » de la littérature. Un résultat publié à sondes d'activation sur la collusion existe donc selon notre propre source
(la note est d'ailleurs incohérente avec elle-même : sa section 3, point 3, écrit « toute la littérature […] suppose un moniteur
textuel »). C'est exactement le cas que R8 demande de vérifier plus durement, et la v5 affirme l'avoir fait (« vérifiée plus
durement »). Un interlocuteur qui connaît HELIOS met en défaut l'argument entier.
*Correction* : « côté boîte blanche, un seul travail publié à sondes d'activation (HELIOS, prépublication 2026, modèles de
frontière, collusion émergente ; chiffres à vérifier sur PDF, R7) ; rien sur 8 milliards de paramètres, rien en moniteur
séquentiel, rien en production scientifique » ; lire HELIOS sur PDF avant l'appel pour établir s'il touche la zone revendiquée
(si oui : nœud « zone revendiquée trouvée occupée », à Lazar) ; signaler l'incohérence de la note à son auteur.

### Majeurs

**CL1-05 — majeur — section 7, question « about $20 », l. 438–439.** « about three hundred and fifty dollars in all ». La
réserve 2 (l. 549–550) prescrit : « Dire "a few hundred dollars", pas un nombre, tant que l'export de facturation n'est pas
rapproché » ; la note de dépenses, section 4, dit de même. La réponse préparée par la correction (6) viole la consigne de la
même pièce. Même tension, moindre, en section 6, message 3 (l. 407 : « ≈ 450 connus » dans un message « à faire passer »).
*Correction* : « a few hundred dollars in all, on our own ledger; the reconciliation against billing is not finished » ; en
section 6, mettre « ≈ 450 connus » entre parenthèses comme note interne, pas comme message.

**CL1-06 — majeur — section 7, question « about $20 », l. 436–438.** « What was added since the seventh is not more GPU » : faux
selon la note de dépenses — la carte graphique est passée de l'ordre de 20 (chiffre de la proposition, non vérifié ici) à ≈ 95,
dont ≈ 25 de lancements des 24–27 octobre (échelle ≈ 1,7 ; couche 1 bis ≈ 11,9 ; H-M1 ≈ 0,25 ; gradient ≈ 11,6) et P3 (6,42, le
23 octobre). Et « has stayed under about a hundred dollars, inside a 150-dollar cap » confond deux périmètres : le plafond de 150
(GO-2026-10-04-08) couvre la phase 0 stricte (≈ 70), pas les ≈ 95 (note, section 2, point 3 ; la réserve 2 de la v5 le dit
correctement, l. 545).
*Correction* : « GPU has stayed under about a hundred dollars; the phase-zero part, about seventy, sits inside a 150-dollar cap
set on the fourth of October. Most of what was added since the seventh is not GPU: it is multi-model idea-collider rounds and
organism pilots, each under its own capped, written authorisation. »

**CL1-07 — majeur — section 5 (anglais), l. 389–391.** « a brake that has already bitten us **twice** in one day: two attempts
[…] were halted […], **and** when one model refused a round […] » : trois événements annoncés comme deux ; le français dit
« trois fois en un jour » (l. 202) et « une troisième fois » (l. 192).
*Correction* : « a brake that has already bitten us three times in one day: two attempts […] were halted and recorded, and one
model refused its task in our idea collider, and the round stopped rather than being talked around. »

**CL1-08 — majeur — section 7, question « attack tooling », l. 427–430.** « We are not. […] two separate attempts to assemble
offensive tooling in this programme were halted ». A puis non-A dans la même réponse, la plus sensible de l'entretien.
*Correction* : « We do not build reusable attack tooling: our output stays at the level of mechanism and defence […]. And the
brake is not a policy document: on the twenty-eighth of October, two steps towards an offensive pipeline went past that level
and were halted by safety classifiers. »

**CL1-09 — majeur — section 7, question « How much of this is you », l. 449 ; section 9, point 5, l. 497–498.** La réponse fait
dire à Lazar « The questions, every decision, and the gates are mine », alors que la section 9 signale comme **inexacte** la
formulation de la proposition v1 « I set the questions and take every decision ». Contradiction interne ; la hiérarchie de
décision du dépôt laisse en effet aux agents les décisions de routine.
*Correction* : « The questions, the gates and every decision that changes the programme or spends money are mine; routine
execution choices are the agents', logged and reviewable » — ou laisser la phrase en attente du point 5 de la section 9.

**CL1-10 — majeur — section 3, front C, l. 192–195 ; section 4, l. 361–362 ; section 5, l. 390–391 ; en-tête, l. 12–13.** Le
refus d'Opus 5.5 est présenté comme traité sans accroc : « rendu la main à l'arbitre, qui ne reformule pas la même question mais
applique R-609 ». R-615 consigne l'inverse : l'enchaîneur a pris l'arrêt pour « tour fini » et a lancé le tour 3 **sans
appliquer R-609** ; Lazar l'a relevé (« je croyais qu'on reposait une question plus spécifique en cas de refus ? ») ; la
récupération a été lancée après. Le texte invite le fonds à voir les entrées du registre (l. 432) : il y lira ce trou. Par
symétrie (R4) et parce que le trou relevé puis corrigé le jour même est un meilleur argument que son omission, il faut le dire.
*Correction* (section 3) : « […] l'instrument scellé a fermé le tour ; notre enchaîneur a d'abord enchaîné le tour suivant sans
appliquer R-609 — relevé par Lazar, corrigé le jour même : les autres espèces portent le tour, et une seule reprise, sous une
question plus étroite […] (R-615) ». Section 4 : « récupération selon R-609, lancée après un premier oubli (R-615) ».

**CL1-11 — majeur — section 8, l. 472–473.** « Trois points restent à Lazar (ventilation v2, **section 6**) » : la ventilation v2
n'a que cinq sections ; « Ce que Lazar tranche » est la section 5. Même défaut que la correction (2), resté dans la section 8 ;
la l. 485 et la section 9 disent bien « section 5 ».
*Correction* : « (ventilation v2, section 5) ».

**CL1-12 — majeur — section 10, l. 509, 516, 520 ; section 3 bis, l. 270.** « C'est le niveau approuvé par **R-339** » ; « (R-597,
**R-339**) » ; « Le contenu offensif sous le gel **R-342** ». Dans `registres/decisions.md`, R-339 (24 octobre) est « Essaim de
Gemini corrigé » et R-342 (24 octobre) « Décisions de Lazar relayées par conv-audit […] correction de P-027 et P-028 » : sans
rapport. Le gel du pipeline des étages 1 et 2 est R-611, cité ainsi partout ailleurs (l. 171, 192, 294, 296). La section 3 bis
explique probablement la cause : « mes registres (R-336 à R-342 […]) » — la lignée conv-audit numérote son propre registre dans
la même plage que `main`. C'est le défaut de la correction (3), resté en section 10.
*Correction* : remplacer « gel R-342 » par « gel R-611 » ; pour R-339, citer l'entrée de `main` qui approuve le niveau méthode,
ou préfixer explicitement le registre de conv-audit (chemin et empreinte) ; en section 3 bis, écrire « registre de conv-audit
(chemin), R-336 à R-342 » pour lever la collision.

### Mineurs

**CL1-13 — mineur — section 8, l. 467–468 contre l. 480 et en-tête l. 10.** « ≈ 176 500 » et « ≈ 176 550 » pour le même palier
(la ventilation v2 porte les deux : section 1 et section 2). *Correction* : 176 550 à l'écrit (somme exacte 138 600 + 37 950,
sans « ≈ ») ; « about 176,500 » seulement à l'oral.

**CL1-14 — mineur — section 11, réserve 2, l. 546.** « évasion ≈ 4 en cours » (note de dépenses : 4,4 à 10:50 UTC, 7 cellules
sur 9) contre piste 12 (l. 291) : tour 1 « 6,62 USD », tour 2 « 1,06 USD », tour 3 en cours. Écart dans la tolérance de ± 15 %,
mais deux chiffres différents pour le même poste. *Correction* : « évasion ≈ 4 au relevé de la note ; ≥ 7,7 depuis (R-615),
tour 3 en cours ; total inchangé à ± 15 % ».

**CL1-15 — mineur — section 3, front C, l. 190–191.** « dont l'équipe rouge est passée sans refus sur trois modèles », sans
préciser le tour, suivi trois lignes plus bas du refus au tour 2. *Correction* : « dont l'équipe rouge du tour 1 est passée sans
refus sur trois modèles ».

**CL1-16 — mineur — section 4, l. 358–362.** « rotation de 3 triplets sur 8 modèles », puis les triplets nommés : Opus 4.6,
Fable 5.1, Gemini ; Opus 5.5, Opus 4.8, Gemini ; Opus 5, Fable 5, Gemini — sept noms distincts. *Correction* : préciser les
versions de Gemini si elles diffèrent, sinon « sur 7 modèles ».

**CL1-17 — mineur — en-tête l. 40 et 44 ; l. 129, 270, 289 (piste 11), 460, 491.** Restes de la v4 : « Fait dans cette v4 » (à
lire « dans la v4 ») ; première personne de conv-audit dans un texte désormais corrigé par session-depot (« mes registres »,
« mes versions antérieures », « à ma connaissance », et piste 11 « résultats versés, non relus par moi », qui devient absurde
sous la plume de session-depot, auteur de ces résultats). *Correction* : « dans la v4 » ; « conv-audit » ou « session-depot » à
la place de « je/mes/moi » là où l'attribution compte (au moins l. 270 et piste 11).

**CL1-18 — mineur — en-tête, l. 5.** « Écrit à partir du relevé `date -u` de 10:55 UTC » ; le fichier et son empreinte ont pour
date de modification 10:52:25 UTC. Le relevé cité est postérieur à l'écriture. *Correction* : citer le relevé réel.

**CL1-19 — mineur — section 5, l. 385 ; section 2, H5, l. 95 ; section 7, l. 422–423.** « at eighty per cent » sans « power »
(la section 7 le dit) ; « does not rule out an effect below about 0.6 » : pour la sonde « tromperie », l'aire minimale
détectable est 0,6315, donc le nul n'exclut pas non plus une aire entre 0,60 et 0,63. *Correction* : « at eighty per cent power
[…] below about 0.6 to 0.63 ».

**CL1-20 — mineur — section 2 (tableau) contre pistes 9, 31, 32.** Les lignes « H1 » à « H7 » du tableau des résultats entrent
en collision avec les hypothèses du programme (H1a/H1b, « 2603.02798 pour H2 », H9 ; la note de conscience d'évaluation désigne
par « H6 » la zone revendiquée, pas la carte). *Correction* : renuméroter le tableau « résultat 1 » à « résultat 7 ».

**CL1-21 — mineur — section 2, l. 101 ; section 3, front A, l. 132.** A7 est à la fois un des « trois lemmes les plus parlants »
(borne prouvée) et l'une des « 7 questions ouvertes ». Pas une contradiction si « question ouverte » veut dire « aucune instance
dans la littérature auditée » (l. 96), mais un interlocuteur y verra un lemme non prouvé. *Correction* : une incise « (question
ouverte = classe sans instance publiée, non lemme non prouvé) », à confirmer sur la carte v1, que je n'ai pas lue.

**CL1-22 — mineur — section 3, front D, l. 218.** « l'audit textuel en rate l'essentiel » repose sur le chiffre HELIOS
« 2 des 229 épisodes » (note collusion, section 1.8 et section 2, point 4), qui figure dans la liste des chiffres à vérifier
sur PDF (section 5 de la note). *Correction* : « selon une prépublication à vérifier (R7) ».

**CL1-23 — mineur — section 5, l. 397.** « the part that is cheap in dollars and expensive in care » juste avant une demande au
triple du formulaire (≈ 176 550). *Correction* : réserver la formule aux fronts A et B, ou la retirer.

**CL1-24 — mineur — section 5, l. 388–389.** « a held-out attack mode already designed by an instance that has never seen a
monitor » : le français dit trois proposeurs indépendants, deux convergents (l. 168–169), et un scellement définitif en attente
du mot de Lazar (piste 16). *Correction* : « designed by fresh instances that have never seen a monitor, to be sealed before
the gate ».

### Registre de sûreté (point 4)

Aucune phrase ne franchit le niveau méthode. Le document nomme des classes d'attaque (six classes cibles), des mécanismes au
niveau des lois de probabilité (lemmes A7, A13, A18) et des défenses ; il ne contient ni recette, ni code, ni séquence d'actions
d'un mode d'évasion ; les pièces adversariales sont citées par chemin et empreinte, jamais reproduites ; la section 10 exclut
explicitement recettes, candidats non vérifiés et contenu du document de synthèse. Observation sans correction exigée : la
phrase « plusieurs protocoles publiés de contrôle ont cette forme » (A18, l. 106) désigne une faille structurelle de protocoles
publiés sans les nommer — c'est le niveau de la divulgation responsable ; ne pas les nommer à l'oral sans la carte sous les yeux.

---

## (c) Les sept corrections annoncées (R-614)

| n° | correction | état | constat lié |
|---|---|---|---|
| 1 | Section 8 : options réécrites avec les chiffres envoyés | **partielle** — options réécrites, mais (c) ≈ 176 550 rangé parmi les « chiffres envoyés » et attribué au « go » de 11:28 ; ≈ 176 500 et ≈ 176 550 coexistent | CL1-03, CL1-13 |
| 2 | Section 9 : renvoi à la ventilation v2, section 5 | **appliquée** en section 9 ; le même renvoi faux (« section 6 ») reste en section 8 | CL1-11 |
| 3 | Front C : second arrêt cité R-611, non R-341 | **appliquée** au front C ; le même défaut de numéro reste en section 10 (R-342, R-339) | CL1-12 |
| 4 | « cette v3 » → cette v5 | **appliquée** (l. 31) ; restes « Fait dans cette v4 » (l. 40, 44) | CL1-17 |
| 5 | État réel du collisionneur en sections 3, 3 bis, 4, 5, 6 | **partielle** — présent partout, mais « twice » en section 5, équipe rouge non datée, coût « évasion ≈ 4 » non mis à jour, trou de R-615 omis | CL1-07, CL1-10, CL1-14, CL1-15, CL1-16 |
| 6 | Question « about $20 » préparée en section 7 | **partielle** — la question existe, mais la réponse donne un nombre contre la consigne de la réserve 2 et affirme « not more GPU » | CL1-05, CL1-06 |
| 7 | Contre-lecture R2 lancée (réserve 5) | **appliquée** — le présent rapport | — |

---

## (d) Ce que je n'ai pas pu vérifier

- La carte des hypothèses (`carte-des-hypotheses-v1.md`) : 23 hypothèses, 21 lemmes, 2 esquisses, 1 conjecture, 15 / 1 / 7, la
  liste des sept questions ouvertes et le statut d'A7. Seule la cohérence interne a été contrôlée (15 + 1 + 7 = 23 ; mêmes nombres
  en français et en anglais). La valeur 0,049 du plafond d'A7 a été recalculée de la formule citée (Φ(0,3/√0,2 − 2,326) ≈ 0,049) ;
  la formule elle-même n'a pas été vérifiée.
- Les verdicts P3 (0,6315 et 0,5966, « au plus 0,58 ») : seule la cohérence avec l'arrondi anglais (0,63 et 0,60) est contrôlée.
- La proposition envoyée et son budget (`737c482c…`, `037765b0…`) : « about $20 », 58 630, 28 160, 138 600 comme montants
  envoyés, G1 « fin du mois 4 », formulations inexactes de la v1. Contrôlé seulement par accord avec la ventilation v2.
- `registres/depenses.md` : les sous-totaux de la note (≈ 95, ≈ 70, ≈ 156,3, ≈ 179,9, ≈ 12,1, ≈ 4,4, ≈ 352,7, ≈ 450) ont été
  additionnés et concordent entre eux et avec la v5 (≈ 353, ≈ 156, ≈ 180, ≈ 12, ≈ 4) ; les lignes sources ne sont pas relues.
- La ventilation v2 : arithmétique vérifiée (7 500 + 4 000 + 5 000 + 12 000 + 6 000 = 34 500 ; + 3 450 = 37 950 ;
  138 600 + 37 950 = 176 550 ; 58 630 + 27 500 = 86 130 ; 176 550 / 58 630 ≈ 3,0) ; les montants E1 à E8 sont des ordres de
  grandeur de leur auteur.
- Le registre propre de conv-audit (R-336 à R-342) : non lu ; CL1-12 suppose une collision de numérotation, à confirmer.
- Les entrées R-597, R-599, R-604 à R-606, R-610, R-612, R-613, les GO cités, les décisions N-xxx, la composition exacte des
  triplets (versions de Gemini) et les heures des mots de Lazar.
- HELIOS et les autres travaux de niveau 2 : je m'appuie sur la description de la note ; aucun PDF lu (R7).
- Écarts au périmètre de lecture, déclarés : `tail -n 2 registres/decisions.md` rend R-615 et **R-616**, non R-614 et R-615 ; j'ai
  donc lu en plus la ligne R-614 (liste des sept corrections), puis les seules lignes R-339, R-341, R-342, R-609 et R-611 du même
  registre, pour contrôler les citations (point 3). Aucun autre fichier lu ; aucun fichier modifié ; pas d'empreinte compagnon
  écrite pour ce rapport (un seul fichier demandé) — à sceller par l'appelant.
