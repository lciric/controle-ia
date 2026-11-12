# Journal de la consigne v3 du jeu de phrases des concepts de T0.7 — v1

- **Objet** : `docs/procedures/consigne-concepts-sans-lien-T0.7-v3.md` (empreinte dans son compagnon `.sha256`, scellé à
  la remise) ; elle remplace la v2 (`79f2c89cc0763f187734e7487e837ab179fa91126a40e61dbef20f33603f1ee4`, intacte) pour le
  seul troisième tour de `chats` et `geographie` (R-2155, option (c) accordée par Lazar, R-2158 point 3).
- **Rédacteur** : Claude Opus 5.5, sous-agent neuf de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` ; n'a lu aucune
  phrase écrite pour le jeu ; a lu des fichiers de T0.7 : exclu de tout rôle de lecteur de P3-bis. Heures relevées par
  `date -u` : début vers 10:42 UTC, rédaction à partir de 10:47:27 UTC, le 2026-11-10.
- **Pièces lues** (empreintes vérifiées, égales aux compagnons) : interdits communs v2 `1ee3b370…` (tenus en entier, règle 9
  comprise) ; consigne v2 `79f2c89c…` (en entier) ; contre-lecture de la v1 `4d759557…` ; rapports des lecteurs
  `a7c17e7e…` et `e741c2e5…` (en-têtes et constats seulement ; les réponses par item et les « raisons » du second rapport
  n'ont pas été ouvertes) ; journaux de décompte `2d10525d…` et `6e23b105…` ; contre-lecture du script v2 `9d024078…` ;
  module au commit `8dc1cb09` (`sondes_neuves_v1.py` `b1c59783…`, l. 58-69, 200-220, 330-372) ; `temoins.py` `3b051b6f…`
  l. 36-89 ; `empans.py` l. 41-61 et `formats.py` l. 19-68 ; script v2 au commit `220c7c7f` (`a858c40c…`) : liste des
  définitions, constantes, `lire_consigne`, `motifs_c2` ; `registres/decisions.md`, R-2101 à R-2105, R-2118, R-2125,
  R-2149, R-2150, R-2155, R-2158.

## Changements de la v2 à la v3 (une ligne chacun, avec sa raison)

1. **Portée** : la v3 ne vaut que pour un lot neuf de `chats` et `geographie` (72 paires chacun) ; `meteo` et `sports`
   restent ceux du premier tour sous la v2 — acceptés sous la règle gelée, ils ne se rouvrent pas (R12, R1).
2. **Phrase neutre écrite librement**, naturelle d'abord, appariée par la longueur en jetons et le registre seulement ;
   « même structure grammaticale » retiré de [v2 § 4.2] — cause commune des deux échecs (Q5) relevée par les deux lecteurs ;
   la direction n'emploie que les moyennes des deux côtés, pas l'appariement phrase à phrase (module l. 59-88 de
   `temoins.py`).
3. **Anti-calque C14 (neuf, dur)** : aucune suite de quatre mots consécutifs commune aux deux phrases d'une paire — rend
   mécanique l'interdit de reprendre la charpente.
4. **Énoncé général des deux côtés, au présent** ; ni scène particulière ni article défini sans antécédent — constat 6 du
   second lecteur (fait général contre scène particulière, lisible sans le sujet).
5. **C2 : aucune majuscule hors du premier caractère, sans exception**, géographie comprise ; liste d'exceptions de la v2
   ôtée pour ce tour — noms propres d'un seul côté (les deux lecteurs) ; une direction de « majuscules » se lirait aussi
   sur les actions de l'agent.
6. **C2 : ni ` ,` ni ` .`** — tolérance de la v2 relevée par la contre-lecture du script v2 (section 5).
7. **Annexe C (neuve) et contrôle C15** : mots interdits dans la phrase du concept du troisième tour, primant sur
   l'annexe B — `chats` : états, sons, mouvements à risque, liens, âge, caractère, noms de race à majuscule (Q4 « oui » au
   second tour : chute, ronronnement au repos) ; `geographie` : noms propres, volcans, frontières, histoire, lieux dits
   hostiles.
8. **Règles de `chats` réécrites en « notice »** (corps, robe, types de robe, toilette, nourriture, objets) et de
   `geographie` en noms communs — mêmes constats ; écrit en français (4.1) et en anglais (section 5).
9. **Exemples neufs E9 à E12** (deux par concept du tour, phrases neutres écrites à part), vérifiés par le rédacteur
   (tokeniseur réel, annexes, C2, C4, C8, C9, C14, C15) ; exemples E1 à E8 de la v2 non remis à l'écrivain — ils
   montraient la reprise de charpente ; gardés pour C9 seulement.
10. **C9 contre les exemples de la v2 et de la v3** — aucune reprise d'aucun des douze.
11. **C13 étendu** : part des paires à suite commune de trois mots (réserve au-delà d'un quart), rapport des `the` par rôle
    (réserve au-delà de 1,5), part moyenne de mots communs (réserve au-delà de 0,25) — compensent par programme la perte
    du contrôle de forme.
12. **C0 étendu** : annexe C bien formée, disjointe de A et des autres lexiques, au moins huit entrées de noyau libres par
    concept ; annexes A, B et ligne de format égales à celles de la v2 — garde que le seul changement des listes est
    l'annexe C.
13. **Q2 réécrite** (même registre et même nature, la construction n'y entre plus) — elle contrôlait la règle retirée ;
    elle n'a fait échouer aucune paire aux deux tours (aucun motif Q2 dans les journaux de décompte).
14. **Q6 neuve, rapportée hors conformité** (une phrase imite-t-elle l'autre ?) — mesure si le remède a pris, sans rien
    décider.
15. **Q1, Q3, Q4, Q5 et la règle d'acceptation (au plus une non conforme sur sept, aucun « oui » à Q4, trois branches)
    inchangées mot pour mot** — R1, R3 : le remède porte sur l'écriture, jamais sur le juge ; même barre que `meteo` et
    `sports` (justification, section 10 point 8).
16. **Remise au lecteur autonome** : sections 1 et 7 réécrites sans renvoi nécessaire à la v2 ; l'histoire des échecs et la
    justification des seuils sont hors des sections extraites — le lecteur ne doit lire ni la v2 ni les motifs des échecs.
17. **Second lecteur de Q4 à écrire dans le script** (mode `echantillon-q4`, `decompter-q4`) — branche de la v2 jamais
    écrite (D2-8 de la contre-lecture du script v2) ; sans elle, un « oui » à Q4 laisserait le tour sans voie.
18. **Plancher : n < 56 = échec du tour**, plus de remise complémentaire — jamais écrite dans le script et elle ouvrirait un
    quatrième passage d'écriture.
19. **Troisième échec : repli écrit, sans quatrième tour** (section 9.1) — rien d'assemblé, ligne `SCELLEMENT-CONCEPTS-T07`
    non écrite, T0.7 suit son repli à clé permise avec réserve déclarée ; pas d'assemblage à deux ou trois concepts (le
    module en exige quatre).
20. **Échéance** : sans ligne à l'ouverture de l'étape A, repli — accord de l'option (c) de R-2155 (témoins utilisés s'ils
    sont acceptés avant l'ouverture).
21. **Modèles de l'écrivain et du lecteur fixés dans la commande avant le lancement de l'écrivain** — au deuxième tour le
    modèle de l'écrivain a été choisi après la lecture du décompte (R-2125).
22. **Script v3** : nom neuf, à partir du v2 `220c7c7f` ; liste fermée de 17 changements (section 6), dont D2-1 et D2-2 de
    la contre-lecture du v2 corrigés ; C4 gardé.
23. **Fichiers du troisième tour en `-v3`**, sélection finale `selection-v3.json` (`selection-v2.json` jamais écrit), fichier
    final inchangé `phrases-concepts-v1.jsonl` — R12, et le nom final est celui que cite la ligne de registre.
24. **Réserves neuves** (section 10, points 2 à 9) : perte du contrôle de forme et ce qui la compense ; sujet du côté
    neutre (vivant contre objet, grande échelle contre petit objet) non corrigé ; annexe C liste de mots ; deux règles dans un
    même fichier ; lecteurs différents ; tour borné ; justification des seuils ; portée du seuil.

## Divergence avec la commande de la mère (une)

- La commande attribue la phrase neutre « calquée mot à mot » au contrôle C4, « gabarit et identité des jetons ». **Dans la
  v2, C4 ne contraint pas la forme** : il vérifie que la phrase lue dans le gabarit de dialogue (`message_utilisateur`) a le
  même nombre de jetons que la phrase seule ([v2 § 6.1], `jetons_message_utilisateur`). Le calque vient de « même structure
  grammaticale » ([v2 § 4.2] et § 5), des exemples de la v2 et de l'ancienne Q2. **C4 est donc gardé**, inchangé (sans lui
  une phrase pourrait être lue tronquée ou décalée dans le format D-4) ; ce que la v3 retire est l'exigence de forme.

## Points à trancher par la mère

1. **`meteo` et `sports` gardés tels quels** (recommandé, confiance 0,75) ou réécrits sous la v3 pour que les quatre
   directions soient construites de la même façon. Garder : aucun concept accepté rouvert, réserve « deux règles » déclarée.
   Réécrire : homogénéité, mais deux concepts acceptés courent un tour de plus, sans quatrième tour, et le jeu entier peut
   tomber. Défaut : gardés.
2. **Règles d'écriture plutôt que changement de concept** pour `chats` (recommandé, 0,7). Un concept inanimé « sans affect »
   serait plus sûr à Q4 mais change la liste de P-013 (b) (R-168) que cite T0.7 au moment même de son scellement, exige un
   lexique neuf dans l'annexe B, donc un nouveau C0 et **un nouveau C7 sur les 142 paires gardées de `meteo` et `sports`**
   (retraits possibles dans des concepts acceptés) ; et un changement de concept après deux lectures ressemble à un choix
   fait sur le résultat. Défaut : `chats` gardé, avec l'annexe C.
3. **Géographie sans noms propres** plutôt que noms propres admis des deux côtés (impossible : la phrase neutre ne peut nommer
   un lieu) ; coût nul pour `meteo` et `sports`. Défaut : sans noms propres.
4. **Modèles du troisième tour** : recommandation, **écrivain Opus 5.5 neuf et lecteur Fable neuf**, comme au deuxième tour,
   pour que la consigne soit la seule chose qui change d'un tour à l'autre (confiance 0,6) ; à fixer dans la commande avant
   l'écrivain. Les lecteurs des deux premiers tours et ce rédacteur sont exclus.
5. **Seuils neufs sans étalonnage** (C14 : quatre mots ; C13 : un quart, 1,5, 0,25 ; huit entrées de noyau libres) : à
   accepter comme choix déclarés, ou à durcir avant le scellement définitif ; jamais après une lecture.
6. **Annexe C** : son ampleur (132 entrées pour `chats`, 34 pour `geographie`) coûte des renvois (homographes comme
   `land`, `rest`, `drop`, `quiet` refusés dans la phrase du concept) ; la contre-lecture R2 peut la compléter ou l'alléger
   avant le scellement définitif.
7. **Contre-lecture R2** : par un modèle autre qu'Opus (Fable, comme pour la v1), avec les pièces de la section 9, étape 1.
8. **Calendrier** : script v3, contre-lecture courte, écrivain, deux passes, lecteur — au moins une demi-journée de travail
   d'agents ; si l'ouverture de l'étape A de T0.7 vient avant, le repli s'applique (section 9.1) sans autre décision.

## Gestes déclarés, interdits tenus, refus

- Lu sous `donnees/t07-concepts-v1/` : les deux rapports des lecteurs (lignes d'en-tête et de constats : `sed` borné ; les
  constats citent des fragments de phrases des échantillons, **non recopiés** dans la consigne), les deux journaux de
  décompte, la liste non récursive du dossier et les empreintes de ces quatre fichiers. **Jamais ouverts** : remises des
  écrivains, sélections, échantillons, clés, réponses, `/home/user/lot3-concepts/`.
- Tokeniseur : trois fichiers pris par `git show` au commit `03e3cbd9` dans le bloc-notes de la session (empreintes égales à
  celles de [v2 § 6]) ; `git ls-tree --name-only` borné au dossier du tokeniseur. Script v2 lu par `git show 220c7c7f:…` dans
  le bloc-notes. `git log` et `git branch --list` sur les branches du script.
- Jamais ouverts : tout `lecture-sondes-t06.json` ; la lecture B et sa branche ; tout `diag/` et `runs/` de 7a ;
  `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; l'étiqueteur ;
  `scripts/extraire_mesures_epreuve_t06_v1.py` ; les textes d'actions de P3 ; tout fichier de P3-bis. Aucune recherche
  récursive ; aucun `env`, `printenv`, `set`, `export -p`, `/proc/*/environ` ; aucun appel externe, aucune dépense ;
  aucune écriture git ; suite d'essais non lancée.
- Écrits : la consigne v3, ce journal et leurs deux compagnons `.sha256` ; brouillons et vérifications dans le bloc-notes.
- **Refus rencontrés** : aucun.
