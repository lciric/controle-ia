# Contre-lecture 1 (R2, N-052) — socle de preuves de l'entretien, v3 — v1

- **Rôle** : contre-lecteur neuf au sens de R2, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni le socle (v1, v2, v3), ni ses journaux, ni la contre-lecture de la v1, ni aucun rapport de niveau 3, ni aucune pièce citée.
- **Modèle** : Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur de la v3 (Claude Opus 5.5) : N-052.
- **Heures** (relevées par `date -u`, le 2026-11-10) : début 12:14:37 UTC ; rapport écrit à 12:27:03 UTC.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-contre-lecture-socle-preuves-v3-v1.md` (`84328cc147d28e9b30f694c03ea8c363ec3cba4857f2c16b49dc9ea34aceb3a7`, égale à son compagnon), interdits communs v2 recopiés, lus en entier.
- **Texte relu** : `brouillons/entretien-taif-v3/socle-preuves-entretien-v3.md` (`b9377f1d…`, égale à son compagnon), lu en entier (719 lignes) ; son journal (`2276733f…`), lu en entier.
- **Lu aussi** : la v2 (`3f078bca…`), comparée à la v3 par programme ; la contre-lecture de la v1 (`48c7fcc2…`, empreinte vérifiée ; verdict et table des vingt-sept constats lus : ses deux bloquants et les constats 3 à 11, 13, 14, 16, 19 à 23 et 25 se retrouvent appliqués dans le texte de la v3) ; `registres/decisions.md` (`d10a422e…` à ma lecture) : R-2130, R-2133, R-2155 à R-2213, en entier.

## Verdict

**Utilisable pour l'entretien après corrections** : 50 couples exacts (C01 à C50, en fin de rapport), chacun trouvé une fois et une seule dans la v3 (blancs et retours à la ligne normalisés ; contrôle par programme).

Le fond de littérature tient : les 59 citations de PDF que j'ai recontrôlées sont à la page citée, les quatre corrections de B3 sont portées avec leur sens exact, les deux voies d'ouverture du témoin positif et l'entretien visé le 27 sont écrits, aucun taux de calibration ne figure, chaque résultat a sa réserve à côté, et rien n'est dit du bras au-delà des décisions inscrites.

**Mais la v3 n'est pas à jour, et quatre de ses états sont faux à l'heure de cette lecture** (elle le déclare en partie : en-tête et § 7 point 8) : la dépense d'A1-v4 est dite absente du registre alors qu'elle y est depuis 10:40 (CLS-01) ; la page publique d'A1-v4 est dite en attente d'un « go publication » alors qu'elle est publiée depuis 10:45 (CLS-02) ; les rendus de littérature de R-2181 et des lignes suivantes ne sont pas portés (CLS-03) ; calendrier, autorisations, concepts, T0.8, P3-bis et calibration sont à l'état de 10:34 (CLS-04).

## Ce que j'ai vérifié et trouvé juste

- **Empreintes** : 55 couples chemin-empreinte relevés par programme dans la v3. Tous les fichiers de `main` cités ont l'empreinte écrite, sauf les deux registres vivants (`registres/depenses.md` : `e7b83d37…` au socle, `5268f0f0…` à ma lecture ; `registres/go.md` : `e682abb0…` au socle, `2c396b01…` à ma lecture), ce que la convention du socle prévoit. Décisions N-029, N-054, N-055, N-056, N-063 v2, N-066 et note POPPER : empreintes justes. Les huit rapports de niveau 3 cités (B1, B3, C1 à C5, lot 1 sur HC2), extraits par `git show` de leurs branches, ont l'empreinte écrite et celle de leur compagnon. Les PDF de `docs/sources/pdf/` cités avec empreinte, les deux du dossier `c8` et les deux de la branche des pièces (MIRAGE, Karne) ont l'empreinte écrite.
- **Citations de PDF** : 59 citations ou chiffres du socle cherchés par programme à la page citée (`pdftotext`, avec et sans `-layout`, blancs et traits d'union normalisés) : 2606.10456 (p. 1, 3, 4, 6, 7, 8), 2606.08892 (p. 1, 2), 2512.03109 (p. 1, 4), 2512.07810 (p. 1, 3, 7, 16, 17, 43), 2610.12445 (p. 1, 6, 7, 8, 19), 2607.02510 (p. 1, 3), 2606.06223 (p. 5), 2606.17478 (p. 7, 30), 2610.04575 (p. 1, 4, 6, 7), 2604.01151 v5 (p. 18, 27, 30), 2604.16824 (p. 4, 7), 2605.15377 (p. 4, 8), 2609.27051 (p. 1, 2), 2606.10304 (p. 20). Cinq échecs au premier passage, tous levés à la main : trois sont des formes d'impression (« −.0263 » ; « 0.066 » et « 0.080 » dans un tableau), un est une page d'un intervalle (« 0,56 » est p. 7 de « p. 6-7 »), un n'est pas une citation (la conclusion de 2606.10456, p. 9, écrit « *provably blind to this attack by construction* », ce qui soutient « reprise à la conclusion »). **Aucune citation fausse ni mal paginée.** Les autres pages du socle (Qu et al. au-delà de la p. 2, Panin, 2603.15809, Karne, MIRAGE p. 2 à 19, 2601.20022, 2606.11417) sont reprises des rapports et non recontrôlées par moi.
- **Corrections de B3 (R-2177 : quatre corrections du socle v2)** : (1) « *less promising* » est une prémisse, non une conclusion, et vise toute surveillance : K2, K2b, sens exact (B3 l. 19-23) ; (2) 2512.07810 : dissimulation de capacités, p. 17-18, contre-résultat partiel : K3, K17 (B3 l. 25-30) ; (3) « échoue par construction » sous condition, avec la source : K1, mot pour mot la formulation de B3 l. 32 ; (4) E-valuator nommé : K4 (B3 l. 34). Le point 5 de B3 (pages revérifiées) : K5, K20. Rien de plus fort ni de plus faible que le rapport.
- **Rapports cités, lignes** : B1 l. 15-19, 49, 55, 56, 207-213 ; C1 l. 8-13, 367, 373, 397 ; C2 l. 11-18, 81-93, 107-113, 132, 163, 165 ; C4 l. 10-24, 183-186, 358-381 ; C5 l. 9-28, 136-186, 404-420 ; lot 1 l. 7-11, 176-186 : lues, le socle les rend fidèlement, sauf CLS-05 à CLS-07.
- **R-2180** : H1 et « Caught in the Act » (diffus écarté du banc, p. 6 et 19 ; échelle, p. 8), 2607.02510, HC2 et MIRAGE (résultat non opposable, reformulation non écrite) : portés. Non portés : voir CLS-03.
- **Voies d'ouverture du témoin positif (R-2133)** : voie normale (ouverture pleine sans rendez-vous ni mot de Lazar, « le rendez-vous tombe ») et voie du rendez-vous (20 novembre à 12:00, branches 1 et 2), conformes au brouillon 10 de P3-bis (`9038a015…`, l. 904-909 et 945-950) et à N-066 ; inchangées au brouillon 11 (`409c37ed…`, l. 1141, 1156, 1200-1206).
- **Entretien visé le 27 (R-2130)** : écrit au § 0, au § 2 et au § 4, avec « à confirmer par Lazar avec le fonds » ; les jours de la semaine du § 4 sont justes.
- **Chiffres repris de la v2, recoupés sur leurs pièces** : table des dépenses (645,42 sur 136 lignes ; 111,87 sur 50 ; 187 ; 624,09 sur 125 ; rangée « sans GO cité » 54,08 sur 12) ; verdict de P3 (1,5227 [1,2464 ; 1,8012] ; 0,6315 ; 0,5966 ; 0,5809 ; phrases gelées) ; audit de fuite (0,9967 [0,9930 ; 0,9991], 46 sur 600, 0,789, réserves 1 et 2) ; N-029 (0,8878) ; étiqueteur (11 sur 120, « non tranché ») ; verdict d'A1-v4 (1 sur 24, [0,0074 ; 0,2024] ; 10 sur 24, [0,2447 ; 0,6117] ; 10/17 ; 8 tenues sur 11 ; 114,0434) ; texte scellé de T0.6 (l. 510-514, 517-518, 536-541, 583 ; 0,394 ; 0,687 ; 0,800) ; texte envoyé (renvois de lignes du § 1.6 et du § 1.7) ; `registres/go.md` (quinze renvois de lignes) ; `registres/decisions.md` (vingt-cinq renvois de lignes, tous justes).
- **Aucun taux de calibration** (R-2185) : recherche de 0,783, 0,857 et de « 47 confirmées » : rien. « 31 sur 31 » (simulation) et « 8 sur 11 » (A1-v4) sont des décomptes propres à une épreuve, sans taux.
- **Réserves à côté des résultats** : présentes pour P3, l'audit de fuite, A1-v4 (lecture bornée, « jamais seul »), la simulation, les contre-résultats publiés (réserve de C1 l. 397) ; une manque pour les sondes de 7b (CLS-08).
- **Cloison du bras, niveau méthode** : le § 2.5 ne contient que des décisions inscrites (R-611, R-2047, R-2127, R-2145, R-2146) ; aucune attaque n'est décrite au-delà de sa forme (R-607). La phrase « monté ; rien n'a encore tourné » date de 10:34 et **je ne peux pas la revérifier** (cloison) : à faire confirmer par Lazar avant l'entretien (point ouvert 1).
- **Écart de la v2 à la v3** : la comparaison par programme ne montre de changement qu'aux passages marqués [Kn], à l'en-tête et aux deux sections neuves ; « tout le reste est la v2 mot pour mot » est exact.

## Constats

### Bloquants

**CLS-01 — La dépense d'A1-v4 est au registre depuis 10:40 ; la v3 la dit absente à neuf endroits.** `registres/depenses.md` l. 414 (commit `a2abc8e3`, 10:40:56, R-2158) : « A1-v4, appels d Argon : 114,0434 USD comptés par la course […] non rapproché d une facture ; machine de l hôte durable (GO-2026-11-08-12, plafond 35) non relevée ». La v3, écrite de 11:05 à 11:12, écrit « n'est toujours pas au registre » (§ 0), « 0 occurrence » (§ 1.4), « recompté : 0 » (§ 6). Dire au jury « une dépense connue hors registre » serait faux, et contre nous sans raison. Ce qui reste vrai : aucune facture, machine non relevée, aucune table scellée ne la compte. Couples C01 à C09.

**CLS-02 — La page publique d'A1-v4 est publiée ; la v3 la dit en attente.** R-2162 (10:45) : mot de Lazar « (a) go publication », commit public `6510199` sur le dépôt public de l'organisme, paragraphe des citations de N-064 compris ; pièces gardées sous `livrables/page-publique-organisme-2026-11-10-v1/` (présentes sur `main`). Un juré peut ouvrir ce dépôt. Conséquence de R-2177, à dire juste : la page **publiée** ne cite pas Qu, Chen, Wang (0 occurrence dans le `README.md` gardé) ; c'est sa mise à jour qui demande un nouveau mot. Couples C10 à C12.

**CLS-03 — Les occupations partielles de R-2181 ne sont pas portées, et le tableau de l'écart 9 est incomplet.** La consigne demande R-2180 et R-2181. R-2181 (11:07, pendant la rédaction) est absent : une occupation partielle de H2 de plus, en boîte noire, avec un contre-indice pour G1 (2606.20746) ; le squelette de la statistique spatio-temporelle du papier B occupé en partie (2601.05427 v3, 2605.11135 v2) (`rapport-lot5A-sequentiel-multi-agents-v1.md`, `aef81e6e…`, § 0, empreinte vérifiée). De R-2180 manquent quatre des cinq occupations partielles de C5 (HC1, H5, H7, HC3 ; le journal § 4 point 6 les déclare hors champ, mais l'écart 9 se donne pour le tableau à compléter) et la version 3 de 2606.08892. Depuis : « The Agent Knew » est lue sur PDF (R-2188) et ne peut plus figurer comme piste non lue ; H9 est occupée en partie sur son cœur ; la statistique de population du papier B l'est sur états internes, « déclencheur de bascule à examiner » (R-2190 ; complément 1 de la synthèse provisoire, `a4176d46…`), alors que le § 1.1 bis écrit « bascule du programme non déclenchée » sans réserve. Couples C13 à C18. **Limite** : la synthèse de niveau 3 n'est pas finale ; ces couples portent ce qui est inscrit au registre et renvoient à la synthèse finale pour le reste ; les pages du rapport du lot 5-A sont à recopier de son annexe, je ne les ai pas recontrôlées sur PDF.

**CLS-04 — État à 10:34, périmé sur six points.** (a) Calendrier resserré de R-2177 absent (scellements visés le 12 au soir, créations le 12 ou le 13, lecture des sondes vers le 16 au 18). (b) Autorisations du 10 absentes : GO-2026-11-10-07 (30, lecture large : R-2207), -08 (60), -09 (enveloppe 500, R-2182), -10 (120, inscrit sur mot direct de Lazar : R-2206) ; présentes à `registres/go.md` l. 297-300. (c) Concepts : « un second échec fermerait l'étape A » est dépassé : le second échec a eu lieu (R-2155) et l'option (c) rend la clé permise (R-2158, R-2166). (d) T0.8 : brouillon 1 rendu, contre-lu, « non scellable en l'état » ; base (A) scellée à part avant 7b (R-2175, R-2186, R-2209, R-2211). (e) P3-bis : brouillon 11 rendu et contre-lu (R-2167, R-2197). (f) Calibration : « recompte en cours » est dépassé par le choix (c) de Lazar, nombres bruts sans taux (R-2195 ; même constat que CLR-03 des sections de résultats, R-2213). Couples C19 à C33. **Limite** : je n'ai pas ouvert la pièce `bd994163…` (branche de la session-dépôt) ; 33, 7 et 6 sont recopiés de R-2195.

### À corriger

**CLS-05 — Qu, Chen, Wang : « trois des quatre composantes » est corrigé par la contre-lecture C7.** `rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md` (`63d83737…`, empreinte vérifiée ; R-2184), l. 49-53 et 445 : deux composantes de O2 en entier (statistique hors de l'agent ; comparaisons multiples), une dans son principe seulement (données postérieures au dépôt, sans sceau, non tenue en rejeu), une absente (nul des lois connues). Le § 2.4 demande de « dire que trois des quatre » : plus fort contre nous que la pièce. En sens inverse, « un sceau par empreinte » y figure parmi ce que Qu et al. ne font pas (exact : C7 l. 105), mais le geste est publié ailleurs (Masked Erosion, C7 l. 25-29) : ne pas le présenter comme neuf. Couples C34, C35.

**CLS-06 — « faible sous 27 milliards de paramètres » (§ 0, K0) dit plus que l'imprimé.** 2610.12445, p. 8 : mauvais chiffres à 2 milliards, bons à partir de 27 ; le point à 9 milliards n'est donné qu'en figure, non relevé (C5 l. 417-420). Le § 1.1 bis et Q1 le disent juste ; seule la ligne de verdict le durcit. Couple C36. Le journal (K17) porte la même formule : à corriger au journal de la version suivante.

**CLS-07 — « Trois erreurs de fait » : deux, plus une formulation contestable.** Sur « *synthetic* » (2606.10456), B1 dit « contredit par l'imprimé », C2 (l. 163) dit « exact », et B3 (table, n° 10) dit « confirmé » : deux lecteurs sur trois ne voient pas d'erreur. La rangée 2 du § 1.7 écrit elle-même « incomplet », non « faux », mais le titre, le § 0 et le § 6 annoncent « trois erreurs de fait » ; la synthèse provisoire de niveau 3 (`8adb561d…`, prononcé 4) écrit « deux erreurs de fait et une formulation contestable ». Annoncer au jury une erreur que nos propres lecteurs contestent serait plus fort que les pièces. Couples C37 à C41 ; ajouter B3 n° 10 à la « lecture divergente » de la rangée 2 (C39 le fait au chapeau).

**CLS-08 — Réserve manquante à côté du résultat attendu des sondes sur 7b.** Q1 présente l'organisme sans consigne et la règle « mots et coût » comme l'épreuve à venir, sans dire que le texte scellé de T0.6 n'a aucun témoin distillé honnête (R-2168) : une sonde au-dessus de son plancher n'y sépare pas, seule, le sabotage de l'adaptateur ; le contrôle est autorisé (GO-2026-11-10-07) et son texte n'est pas scellé (R-2210). Couple C42.

### Mineurs

**CLS-09** — (a) quatre renvois à `registres/etat.md` décalés de six lignes par les écritures du jour (173 → 179, 175 → 181, 184 → 190 deux fois, 239 → 245 ; contenu inchangé) : C43 à C47 ; (b) « R-1294 » n'est pas une ligne de `registres/decisions.md` mais du registre de la session « conv-audit », citée par le verdict d'A1-v4 (l. 82) : C48 ; (c) au § 1.4, « (l. 7) », « (l. 378-382, 393) » et « (l. 383) » suivent la mention du fichier de budget mais sont des lignes du texte envoyé : C49 ; (d) statut : C50 ; (e) l'en-tête nomme la session mère d'avant la reprise (R-2191, R-2201) : exact pour l'histoire, à compléter si la version suivante est rendue sous la session actuelle ; (f) l'empreinte `1a372523…` de l'addendum du bras B de l'audit de fuite correspond sur `main` au fichier `docs/notes/g0-deux-semaines-v1/scellement-course-t06-v1/pieces-apres-couples/addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md` : donner le chemin.

## Points ouverts

1. « Monté ; rien n'a encore tourné » (§ 2.5) : non vérifiable par moi ni par la mère (cloison) ; à confirmer par Lazar à la date de l'entretien.
2. La synthèse de niveau 3 est provisoire (`8adb561d…`, complément `a4176d46…` dont les verdicts de la session sœur sont « repris de ses messages ») : le § 1.1 bis, l'écart 9 et Q5 sont à réaligner sur la synthèse finale ; les nœuds de revendication de R-2190 attendent Lazar.
3. Lecture (c) de R-2195 (« nombres bruts sans taux ») « à confirmer par Lazar » : C32 et C33 la supposent.
4. Les couples d'état (CLS-04) sont justes à 12:13 UTC (R-2213) ; les statuts bougent d'heure en heure : à relever de nouveau au moment de l'application.
5. Le journal de la v3 est scellé et porte K17 (« faible sous 27 milliards ») et K19 (« recompte en cours ») : la version suivante a son propre journal.

## Ce que je n'ai pas fait, et gestes à déclarer

- Je n'ai relu aucun PDF en entier ; je n'ai pas recontrôlé les citations des rapports au-delà des 59 du socle ; je n'ai pas rejoué la simulation ni aucun calcul.
- Aucun fichier de T0.7 ouvert ; de P3-bis, seuls les brouillons 10 et 11 (lignes citées et recherche de sept motifs) et l'en-tête de la contre-lecture 4.
- Aucun chemin interdit ouvert ; aucun `diag/` ni `runs/` de 7a ; aucune branche `donnees/…` ; rien du bras (le fichier `brouillons/entretien-taif-v3/consigne-v19-pince-bras-attaque-sabotage-diffus-v1.md` a été haché avec le dossier par `sha256sum`, non ouvert). Le manifeste `runs/20261004-080257-t03/manifeste.json` (simulation T0.3, cité par le socle) a été haché, non lu.
- **Geste à déclarer** : pour chercher la pièce `bd994163…`, j'ai listé par `git ls-tree` les noms de fichiers du seul dossier `docs/notes/entretien-resultats-v1/` de la branche `origin/claude/upbeat-cray-dmauvv` (session-dépôt) et passé ses compagnons `.sha256` à une recherche d'empreinte ; un nom de fichier contenant « mesure-unanime » est apparu dans la liste ; aucun de ces fichiers n'a été ouvert, aucun contenu affiché hors la ligne d'empreinte cherchée.
- Recherches par `git grep` avec exclusions ou sur fichiers nommés ; aucune recherche récursive ; aucun appel de modèle, aucun réseau, aucune dépense, aucune écriture git ; aucun refus de contrôle de permissions ni de classifieur.

## Couples exacts (ancien → nouveau)

Chaque « ancien » figure une fois et une seule dans `socle-preuves-entretien-v3.md` (`b9377f1d…`), blancs et retours à la ligne normalisés. À appliquer dans une version neuve (règle 12), la v3 restant intacte.

### Couples de CLS-01

**C01** — § 0, ligne 2

~~~text
ANCIEN : **la dépense d'A1-v4 (114,0434 comptés par la course) n'est toujours pas au registre** [MANQUE].
~~~

~~~text
NOUVEAU : **la dépense d'A1-v4 (114,0434 comptés par la course) n'est au registre que depuis le 10 novembre, inscrite après coup (R-2158 ; `registres/depenses.md` l. 414), sans facture rapprochée, machine de l'hôte non relevée** [MANQUE].
~~~

**C02** — § 1.4, « chiffres exacts »

~~~text
ANCIEN : **sans aucune ligne au registre des dépenses** (0 occurrence de GO-2026-11-02-22 ni de GO-2026-11-08-12 dans `registres/depenses.md`) [MANQUE]
~~~

~~~text
NOUVEAU : **inscrits après coup au registre des dépenses le 10 novembre** (R-2158 ; `registres/depenses.md` l. 414, sous GO-2026-11-02-22 : « non rapproché d une facture » ; machine de l'hôte, GO-2026-11-08-12, « non relevée ») [MANQUE : facture, machine de l'hôte]
~~~

**C03** — § 1.4, « état »

~~~text
ANCIEN : ni table régénérée depuis le 8 novembre, une dépense connue hors registre.
~~~

~~~text
NOUVEAU : ni table régénérée depuis le 8 novembre ; la dépense d'A1-v4, inscrite après coup le 10 (R-2158), n'entre dans aucune table scellée.
~~~

**C04** — § 2.4, « Restent »

~~~text
ANCIEN : dépense à inscrire au registre [MANQUE] ;
~~~

~~~text
NOUVEAU : dépense inscrite au registre le 10 novembre, après coup (R-2158), à rapprocher d'une facture ; machine de l'hôte à relever [MANQUE] ;
~~~

**C05** — § 3, rangée « dépense »

~~~text
ANCIEN : table régénérée et scellée ; **ligne d'A1-v4 au registre** ;
~~~

~~~text
NOUVEAU : table régénérée et scellée ; rapprochement de la ligne d'A1-v4 (inscrite le 10 novembre, R-2158) avec sa facture ;
~~~

**C06** — § 4, rangée « 24 à 26 »

~~~text
ANCIEN : ligne d'A1-v4 au registre et tables de dépense régénérées et scellées
~~~

~~~text
NOUVEAU : tables de dépense régénérées et scellées, ligne d'A1-v4 (R-2158) comprise et rapprochée de sa facture
~~~

**C07** — § 5, Q2, « Aveu »

~~~text
ANCIEN : n'est pas encore au registre ; aucune facture n'est rapprochée.
~~~

~~~text
NOUVEAU : n'est au registre que depuis le 10 novembre, inscrite après coup (R-2158), et n'entre dans aucune table scellée ; aucune facture n'est rapprochée.
~~~

**C08** — § 5, Q2, « Ce qui manque »

~~~text
ANCIEN : ligne d'A1-v4, le rattachement de la rangée
~~~

~~~text
NOUVEAU : ligne d'A1-v4 rapprochée de sa facture, le rattachement de la rangée
~~~

**C09** — § 6, point 1

~~~text
ANCIEN : 1. **Dépense d'A1-v4 absente du registre** : 114,0434 comptés par la course (verdict `e6e2f170…` § 2.3) ; aucune ligne sous GO-2026-11-02-22 ni GO-2026-11-08-12 dans `registres/depenses.md` (recompté : 0) ; machine de l'hôte non relevée
~~~

~~~text
NOUVEAU : 1. **Dépense d'A1-v4 inscrite après coup, non rapprochée** : 114,0434 comptés par la course (verdict `e6e2f170…` § 2.3) ; ligne du 10 novembre sous GO-2026-11-02-22 (R-2158 ; `registres/depenses.md` l. 414) ; aucune facture ; machine de l'hôte non relevée
~~~

### Couples de CLS-02

**C10** — § 2.4, « Restent »

~~~text
ANCIEN : rédacteur neuf, contre-lecture par un autre modèle, puis poussée par la mère (R-2131) ; contre-lue : « publiable après corrections », mais le paragraphe des citations de N-064 n'est pas couvert par l'accord du texte scellé et attend un mot explicite de Lazar (« go publication ») ; deux variantes préparées, avec et sans ce paragraphe (R-2154, l. 2112) ; **[K16]** depuis le niveau 3, la page est **touchée par la collision Qu, Chen, Wang** : nouveau « go publication » requis (R-2177) ;
~~~

~~~text
NOUVEAU : **publiée le 10 novembre** sur le mot de Lazar « (a) go publication » (R-2162 : commit public `6510199`, paragraphe des citations de N-064 compris, 22 corrections de la contre-lecture appliquées ; texte exact gardé sous `livrables/page-publique-organisme-2026-11-10-v1/`) ; **[K16]** depuis le niveau 3, la page publiée est **touchée par la collision Qu, Chen, Wang**, qu'elle ne cite pas : sa mise à jour demande un nouveau « go publication » (R-2177) ;
~~~

**C11** — § 3, rangée « texte scellé d'A1-v4 »

~~~text
ANCIEN : **page publique** des chiffres du verdict scellé ; contre-lue, « publiable après corrections » ; le paragraphe des citations de N-064 attend un « go publication » de Lazar (R-2154) ; **[K16]** touchée par la collision Qu, Chen, Wang : nouveau « go publication » requis (R-2177)
~~~

~~~text
NOUVEAU : **page publique** des chiffres du verdict scellé : **publiée le 10 novembre** (R-2162, commit public `6510199`) ; **[K16]** touchée par la collision Qu, Chen, Wang, qu'elle ne cite pas : mise à jour sous un nouveau « go publication » (R-2177)
~~~

**C12** — § 6, point 13

~~~text
ANCIEN : 13. **Page publique d'A1-v4** : le paragraphe des citations de N-064 attend un « go publication » de Lazar (R-2154) ; **[K16]** touchée par la collision Qu, Chen, Wang : nouveau « go publication » requis (R-2177).
~~~

~~~text
NOUVEAU : 13. **Page publique d'A1-v4** : publiée le 10 novembre (R-2162) ; **[K16]** touchée par la collision Qu, Chen, Wang, qu'elle ne cite pas : sa mise à jour demande un nouveau « go publication » (R-2177).
~~~

### Couples de CLS-03

**C13** — § 1.1 bis, table, avant la rangée « papier C (Panin…) » : deux rangées neuves

~~~text
ANCIEN : | papier C (Panin, SSRN 7424179 ; 2603.15809 v1 ; 2607.08066 v1) |
~~~

~~~text
NOUVEAU : | **2606.20746 v1** (Corll ; PDF sur la branche `prep/etat-de-l-art-niveau3-pieces-v1`) — **occupation partielle de H2 de plus, en boîte noire** [repris du rapport du lot 5-A, pages à recopier de son annexe A ; non recontrôlé sur PDF pour ce socle] | somme cumulée de Page, dérive prise sur le bénin seul, de scores par événement, sur des trajectoires d'agents à outils, pour des directives dont chacune reste sous le seuil par événement ; comparée au maximum ; **non faits** : sondes ou états internes, garantie toujours valide (l'auteur l'exclut), sabotage par l'agent lui-même (textes greffés) ; **contre-indice** : l'accumulation amplifie une marge déjà présente sous le seuil, elle n'en crée pas ; résultat nul sur le second axe ; résultat positif sur quatre trajectoires et trois tâches, sans puissance | H2 ; G1 | `docs/sources/lecture-pdf-niveau3/rapport-lot5A-sequentiel-multi-agents-v1.md` (`aef81e6e…`) § 0 ; R-2181 |
| papier B : **2601.05427 v3** (Gauthier, Bach, Jordan) et **2605.11135 v2** (Helm, Priebe, Duderstadt) — **squelette de la statistique spatio-temporelle occupé en partie, en boîte noire** [même réserve] | un processus e par agent, garantie toujours valide, combinaison entre agents par la procédure e-BH arrêtée à un temps commun (2601.05427) ; une statistique de population suivie dans le temps par une carte de contrôle (2605.11135) ; aucun état interne lu ; **non faits** : sondes, copies d'un même modèle lues en parallèle, adversaire qui s'adapte au moniteur | papier B (statistique spatio-temporelle), H3, T | même rapport, § 0 ; R-2181 |
| papier C (Panin, SSRN 7424179 ; 2603.15809 v1 ; 2607.08066 v1) |
~~~

**C14** — § 1.1 bis, rangée HELIOS

~~~text
ANCIEN : quatre annonces seulement (p. 3, 18, 19, 26) : **bascule du programme non déclenchée** |
~~~

~~~text
NOUVEAU : quatre annonces seulement (p. 3, 18, 19, 26) : **bascule du programme non déclenchée par HELIOS v5** ; **à réexaminer par Lazar pour le papier B** depuis deux prépublications de novembre 2026 sur états internes d'agents à modèle partagé (2611.02153, 2611.10620 ; R-2190 ; complément 1 de la synthèse provisoire de niveau 3, `a4176d46…`, verdicts repris de messages, à contrôler sur le rapport du lot 7-B) |
~~~

**C15** — § 1.6, écart 9

~~~text
ANCIEN : **HC2 occupée en partie** (MIRAGE, 2606.10304) ; L et T occupés en partie
~~~

~~~text
NOUVEAU : **HC2 occupée en partie** (MIRAGE, 2606.10304) ; H2 une fois de plus, en boîte noire (2606.20746, R-2181) ; selon les rendus suivants (R-2180, R-2181, R-2188, R-2190 ; synthèse provisoire de niveau 3 `8adb561d…` et son complément `a4176d46…`, **non finale**), sont aussi occupés en partie HC1, H5, H7, HC3 (rapport C5), H9 sur son cœur, la statistique de population du papier B, HC5 et HC6, et la prémisse de HC4 est entamée — nœuds de Lazar, à porter d'après la synthèse finale ; L et T occupés en partie
~~~

**C16** — § 1.1, « pièces »

~~~text
ANCIEN : `docs/sources/pdf/2606.08892v2.pdf` (`aea0f2d1…`),
~~~

~~~text
NOUVEAU : `docs/sources/pdf/2606.08892v2.pdf` (`aea0f2d1…` ; une version 3 du 4 novembre existe, lecture comparée « sans changement de verdict », R-2180, R-2188 : citer la version lue),
~~~

**C17** — § 2.4, [K15], fin

~~~text
ANCIEN : et « The Agent Knew » (2610.17301, R-2177) sont **[NON OPPOSABLE]**.
~~~

~~~text
NOUVEAU : sont **[NON OPPOSABLE]** ; « The Agent Knew » (2610.17301), lue depuis sur PDF par le lot 7-A, n'occupe ni H1 ni H2 et porte un contre-indice (un classifieur de mots y égale la sonde) (R-2188 ; rapport `rapport-lot7A-sondes-agents-H1-H2-v1.md`, à citer avec son empreinte).
~~~

**C18** — § 6, point 10

~~~text
ANCIEN : Cooney et al. 2606.12618, 2609.19101 (C5 § 5) ; « The Agent Knew » 2610.17301 (R-2177) ;
~~~

~~~text
NOUVEAU : Cooney et al. 2606.12618, 2609.19101 (C5 § 5) ;
~~~

### Couples de CLS-04

**C19** — § 0, ligne 1

~~~text
ANCIEN : possible vers le 17 au 19 si tout tient [CE RÉDACTEUR])
~~~

~~~text
NOUVEAU : visé vers le 16 au 18 par le calendrier resserré de R-2177, les échéances écrites restant les replis)
~~~

**C20** — § 0, ligne 3

~~~text
ANCIEN : et les phrases des concepts, dont un second échec fermerait l'étape A (R-2125).
~~~

~~~text
NOUVEAU : et les phrases des concepts : deux concepts ont échoué une seconde fois (R-2155) ; sur l'option (c) accordée par Lazar (R-2158), leur clé devient permise dans T0.7, avec repli écrit et réserve, et un lot neuf est écrit sous une consigne v3 (R-2174, R-2183).
~~~

**C21** — § 4, rangée du 12

~~~text
ANCIEN : phrases des concepts scellées (clé exigée `SCELLEMENT-CONCEPTS-T07` : un second échec d'un concept arrête le lot pour ce concept et ferme l'étape A, R-2125)
~~~

~~~text
NOUVEAU : phrases des concepts : clé `SCELLEMENT-CONCEPTS-T07` **permise**, non plus exigée, depuis l'option (c) (R-2155, R-2158, R-2166) ; repli écrit (étape A sans témoins de concepts, avec réserve)
~~~

**C22** — § 6, point 5

~~~text
ANCIEN : phrases des concepts non scellées (deux concepts en réécriture ; un second échec fermerait l'étape A)
~~~

~~~text
NOUVEAU : phrases des concepts non scellées (deux concepts arrêtés après un second échec, R-2155 ; clé permise et lot neuf sous la consigne v3, R-2158, R-2174)
~~~

**C23** — § 4, chapeau

~~~text
ANCIEN : Bornes inchangées (R-2130) :
~~~

~~~text
NOUVEAU : **Calendrier resserré (R-2177, périmètre interne, aucune dépense nouvelle)** : T0.7, la règle « mots et coût », P3-bis et la consigne d'audit visés scellés le 12 au soir ; 7b et P3-bis créées le 12 ou le 13 ; lecture des sondes visée vers le 16 au 18 ; les dates du tableau restent les replis. Bornes inchangées (R-2130) :
~~~

**C24** — § 1.4, « chiffres exacts »

~~~text
ANCIEN : **après le 8 novembre, non sommé** :
~~~

~~~text
NOUVEAU : **autorisations inscrites le 10 novembre** (`registres/go.md`, `2c396b01…`) : GO-2026-11-10-07 (contrôle de l'artefact d'adaptateur, 30 ; lecture large accordée par Lazar, R-2207), -08 (saboteur à budget, 60, R-2175), -09 (autonomie de calcul jusqu'au 27, enveloppe 500, R-2182), -10 (120 jusqu'au 30 novembre : organisme 45, témoin de Bailey 75 ; mot direct de Lazar, R-2206) ; **après le 8 novembre, non sommé** :
~~~

**C25** — § 2.2, « Ce que la course peut établir »

~~~text
ANCIEN : **T0.8** : brouillon 1 en rédaction, scellement **visé vers le 18-19** (R-2131) ;
~~~

~~~text
NOUVEAU : **T0.8** : brouillon 1 rendu et contre-lu, « non scellable en l'état », trois bloquants (R-2165, R-2186) ; sa base (A) « mots et coût » est scellée à part, avant la création de 7b, sur le mot de Lazar (R-2175 ; brouillon 2 rendu, douze traits accordés, R-2209, R-2211) ; plafond proposé de 120 au-dessus du seuil de 60 de GO-2026-11-10-09 : retour à Lazar avant toute course (R-2186) ;
~~~

**C26** — § 4, rangée du 18

~~~text
ANCIEN : T0.8 scellé (visé vers le 18-19, R-2131)
~~~

~~~text
NOUVEAU : T0.8 scellé (visé vers le 18-19, R-2131 ; brouillon 1 « non scellable en l'état », R-2186 ; base (A) scellée à part avant 7b, R-2175)
~~~

**C27** — § 4, sous le tableau

~~~text
ANCIEN : T0.8 est désormais sur un chemin (brouillon 1, scellement visé vers le 18-19), sans date écrite pour sa lecture.
~~~

~~~text
NOUVEAU : T0.8 est désormais sur un chemin (brouillon 1 contre-lu, « non scellable en l'état », R-2186 ; base (A) scellée à part avant 7b, R-2175), sans date écrite pour sa lecture.
~~~

**C28** — § 5, Q4

~~~text
ANCIEN : le critère 4 (base boîte noire) a un premier brouillon, scellement visé vers le 18-19 (R-2131) ;
~~~

~~~text
NOUVEAU : le critère 4 (base boîte noire) a un premier brouillon, contre-lu et jugé « non scellable en l'état » (R-2186), dont la base « mots et coût » est scellée à part avant la course de confirmation (R-2175) ;
~~~

**C29** — § 6, point 4

~~~text
ANCIEN : 4. **T0.8 non scellé** (brouillon 1, scellement visé vers le 18-19) :
~~~

~~~text
NOUVEAU : 4. **T0.8 non scellé** (brouillon 1 contre-lu, « non scellable en l'état », trois bloquants, R-2186 ; base (A) « mots et coût » à sceller à part avant 7b, R-2175, R-2209, R-2211) :
~~~

**C30** — § 2.1, « État »

~~~text
ANCIEN : non scellé ; brouillon 11 en rédaction et contre-lecture courte du code proposé `a1de3915` en cours (R-2131) ;
~~~

~~~text
NOUVEAU : non scellé ; **brouillon 11 rendu** (`409c37ed…`, R-2167 ; code `a1de3915` contre-lu, R-2158) **et contre-lu** : « scellable après corrections », dix-sept couples, quatre bloquants de procédure hors du texte, dont celui du registre des autorisations levé (R-2197, R-2198) ; les renvois de lignes de cette section sont ceux du brouillon 10, les deux voies d'ouverture y étant inchangées ;
~~~

**C31** — § 7, point 2

~~~text
ANCIEN : le brouillon 11 est en rédaction.
~~~

~~~text
NOUVEAU : le brouillon 11 est rendu et contre-lu, non scellé (R-2167, R-2197).
~~~

**C32** — § 1.3, « chiffres exacts »

~~~text
ANCIEN : prédictions : **[K19] recompte en cours, aucun taux cité** (
~~~

~~~text
NOUVEAU : prédictions : **[K19] nombres bruts, sans taux** (choix (c) de Lazar, R-2195, lecture à lui faire confirmer : 33 confirmées, 7 réfutées, 6 non concluantes ; pièce `bd994163…` de la session-dépôt, sur sa branche, absente de `main` : à vérifier avant tout usage) ; aucun taux cité (
~~~

**C33** — § 6, point 15

~~~text
ANCIEN : 15. **[K19] Taux de calibration des prédictions** : recompte en cours ; aucun taux cité dans ce socle.
~~~

~~~text
NOUVEAU : 15. **[K19] Calibration des prédictions** : nombres bruts sans taux (R-2195 : 33 confirmées, 7 réfutées, 6 non concluantes ; pièce `bd994163…` hors de `main`, à vérifier) ; aucun taux cité dans ce socle (R-2185).
~~~

### Couples de CLS-05

**C34** — § 2.4, [K15]

~~~text
ANCIEN : dire que trois des quatre composantes de l'énoncé retenu de O2 sont publiées sur un autre objet, et que l'énoncé n'est pas occupé en entier dans les pièces lues.
~~~

~~~text
NOUVEAU : dire que, des quatre composantes de l'énoncé retenu de O2, deux sont publiées en entier et une dans son principe seulement, sur un autre objet, le nul formé des lois connues n'y étant pas (contre-lecture C7 de C4, `rapport-C7-contre-lecture-qu-chen-wang-dossier-c8-v1.md`, `63d83737…`, l. 49-53 et 445 ; R-2184), et que l'énoncé n'est pas occupé en entier dans les pièces lues ; ne pas présenter comme neuf le sceau par empreinte d'une prédiction avant les données (publié comme pratique d'auteurs : Masked Erosion, 2610.38392 ; C7 l. 25-29) ; la collision s'élargit à O11, O3, O17, O19 et O10 (PACE, Masked Erosion, REUSE, PROCTOR ; R-2184).
~~~

**C35** — § 0, ligne 4 [K0]

~~~text
ANCIEN : la portée de la revendication restante est un **nœud de Lazar non tranché** (R-2177, options (a) et (b))
~~~

~~~text
NOUVEAU : la portée de la revendication restante est un **nœud de Lazar non tranché** (R-2177, options (a) et (b) ; collision confirmée et précisée par une contre-lecture indépendante, R-2184)
~~~

### Couples de CLS-06

**C36** — § 0, ligne 4 [K0]

~~~text
ANCIEN : sur du sabotage **non diffus**, faible sous 27 milliards de paramètres ; nous sommes à 8)
~~~

~~~text
NOUVEAU : sur du sabotage **non diffus** ; sondes faibles à 2 milliards de paramètres, bonnes à partir de 27, rien d'opposable entre les deux ; nous sommes à 8)
~~~

### Couples de CLS-07

**C37** — en-tête, « Nouvelles sections »

~~~text
ANCIEN : nous-mêmes devant le jury** : trois erreurs de fait du texte déjà envoyé).
~~~

~~~text
NOUVEAU : nous-mêmes devant le jury** : deux erreurs de fait et une formulation contestable du texte déjà envoyé).
~~~

**C38** — § 0, ligne 4 [K0]

~~~text
ANCIEN : **trois erreurs de fait dans le texte déjà envoyé**, à corriger
~~~

~~~text
NOUVEAU : **deux erreurs de fait et une formulation contestable dans le texte déjà envoyé**, à corriger
~~~

**C39** — § 1.7, chapeau

~~~text
ANCIEN : Trois erreurs de fait sur des travaux d'autrui, dans le texte **déjà envoyé** au fonds
~~~

~~~text
NOUVEAU : Deux erreurs de fait (n° 1 et 3) et une formulation contestable (n° 2 : B1 la dit contredite par l'imprimé ; C2, l. 163, et B3, table, n° 10, la disent exacte) sur des travaux d'autrui, dans le texte **déjà envoyé** au fonds
~~~

**C40** — § 1.7, chapeau

~~~text
ANCIEN : Une ligne par erreur ; à dire **avant** qu'un juré ne les trouve.
~~~

~~~text
NOUVEAU : Une ligne par point ; à dire **avant** qu'un juré ne les trouve.
~~~

**C41** — § 6, point 14

~~~text
ANCIEN : correction devant le fonds des trois erreurs de la section 1.7
~~~

~~~text
NOUVEAU : correction devant le fonds des deux erreurs et de la formulation contestable de la section 1.7
~~~

### Couples de CLS-08

**C42** — § 5, Q1, « Réponse »

~~~text
ANCIEN : une règle qui ne juge les sondes de cet organisme qu'aux doses où un lecteur des seuls mots et du coût échoue.
~~~

~~~text
NOUVEAU : une règle qui ne juge les sondes de cet organisme qu'aux doses où un lecteur des seuls mots et du coût échoue. **Réserve à dire avec tout résultat de sonde sur cet organisme** : le texte scellé de T0.6 n'a aucun témoin distillé honnête (son seul adaptateur témoin est distillé du témoin instruit, à la dose 1) ; une sonde au-dessus de son plancher n'y sépare donc pas, à elle seule, le sabotage de l'effet de l'adaptateur (R-2168) ; un contrôle à part est autorisé (GO-2026-11-10-07 ; R-2175, R-2207), son texte n'est pas scellé (R-2210).
~~~

### Couples de CLS-09

**C43** — § 1.1, « état »

~~~text
ANCIEN : `registres/etat.md` l. 173 de la v2 ;
~~~

~~~text
NOUVEAU : `registres/etat.md` l. 179 à l'empreinte `1ef56d65…` ;
~~~

**C44** — § 1.6, écart 7

~~~text
ANCIEN : `registres/etat.md` l. 239)
~~~

~~~text
NOUVEAU : `registres/etat.md` l. 245)
~~~

**C45** — § 1.6, écart 8

~~~text
ANCIEN : | `registres/etat.md` l. 175 |
~~~

~~~text
NOUVEAU : | `registres/etat.md` l. 181 |
~~~

**C46** — § 4, rangée « jusqu'au 9 »

~~~text
ANCIEN : (`registres/etat.md` l. 184) ; P3 nul scellé
~~~

~~~text
NOUVEAU : (`registres/etat.md` l. 190) ; P3 nul scellé
~~~

**C47** — § 5, Q4

~~~text
ANCIEN : deux critères sur huit sont prouvés (`registres/etat.md` l. 184) :
~~~

~~~text
NOUVEAU : deux critères sur huit sont prouvés (`registres/etat.md` l. 190) :
~~~

**C48** — § 2.4, « Témoin négatif »

~~~text
ANCIEN : (dispense R-1294)
~~~

~~~text
NOUVEAU : (dispense R-1294 du registre de la session « conv-audit », citée par le verdict)
~~~

**C49** — § 1.4, « chiffres exacts »

~~~text
ANCIEN : demande 58 630 (l. 7), dont
~~~

~~~text
NOUVEAU : demande 58 630 (texte envoyé l. 7 ; de même pour les lignes 378 à 393 qui suivent), dont
~~~

**C50** — en-tête, « Statut »

~~~text
ANCIEN : - **Statut** : brouillon scellé, **non contre-lu** (vaut pour la v3).
~~~

~~~text
NOUVEAU : - **Statut** : brouillon scellé ; v3 contre-lue (`prereg/contre-lectures/socle-preuves-entretien-v3-cl1.md`), couples appliqués dans cette version.
~~~
