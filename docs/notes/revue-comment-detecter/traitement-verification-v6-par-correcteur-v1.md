# Traitement de la vérification « fidélité » de la synthèse v6 « comment détecter », par le correcteur v7 — v1

Session 16, 2026-10-21, vers 00:45 UTC. Correcteur neuf : je n'ai écrit ni la revue (v1 à v6), ni ses extractions, ni ses
vérifications, ni leurs traitements. Consigne : `…/revue-detection/consigne-correcteur-v7-v1.md` (`af2084cf…`,
compagnon égal). `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Pièces lues, empreintes recalculées, égales à la consigne et à leur compagnon :
- v6 `…/revue-detection/synthese-comment-detecter-v6.md` (`124d06f821f5780dbc810d710d08a3d00239ae34e8545fe69c3ea683177511e8`) ;
- vérification `…/revue-detection/verification-v6-fidelite/verification-v6-fidelite-v1.md`
  (`30c79b0f708e92553acb0cce788bb84141a1be817a13463e3bae64cd8fcc6d39`), « conforme après corrections », 4 constats
  (1 mineur, 3 de forme) et cinq « remarques non comptées » ;
- pour la v2 du traitement du correcteur v5 : `…/revue-detection/traitement-verification-v4-par-correcteur-v1.md`
  (`21e1d56c…`) et `…/revue-detection/verification-v5-fidelite/verification-v5-fidelite-v1.md` (`05472092…`,
  constat VV5-fidelite-08) ;
- une ligne du dépôt, lecture seule : `registres/decisions.md` à `9ecd952` (`e8b73c64…`, par `git show`), l. 394 (P-017,
  options (A), (B), (C)).

Sortie : v7 `…/revue-detection/synthese-comment-detecter-v7.md`
(`d96ca2dc2f4945667ab24138e537190f9842f54a746c125113c6f6a2107f5052`, 698 lignes). Script :
`…/revue-detection/correction-v7/appliquer_corrections_v7.py` (v6 et rapport contrôlés par empreinte ; textes des quatre
constats extraits du rapport par analyse, jamais recopiés ; **7 remplacements**, chacun trouvé une seule fois, blancs
normalisés ; lignes touchées de plus de 120 caractères repliées, jamais une ligne de table). « l. » ci-dessous = ligne
de la v7, prise sur la v7 finale (`sortie-verifier-v7.txt`, section E) ; le journal `sortie-appliquer-v7.txt` donne les
lignes au moment de chaque remplacement, avant les décalages des suivants.

## Une ligne par correction

| correction | gravité | décision | passage de la v7 | écart aux mots exacts |
|---|---|---|---|---|
| VV6-fidelite-01 | mineur | appliqué : la parenthèse (avantage, inconvénient) suit l'option (c) ; la lecture « double comptabilité » dite à part, pour toutes les options | section 5, nœud « Revendication », option (c), l. 463-465 | aucun |
| VV6-fidelite-02 | forme | appliqué : « bras de production : » rattache la règle des nombres avant le champ | table E1, « contrôle obligatoire », l. 399 | aucun |
| VV6-fidelite-03 | forme | appliqué : « La v5 employait T4 « à coût déclaré égal » » | « Décisions prises depuis la v4 », puce R-295 (1), l. 609-610 | aucun |
| VV6-fidelite-04 | forme | appliqué : convention des Sources, exception « P-015 l. 392 » de la liste « v5 » (ligne du registre) | en-tête, Sources, convention, l. 91-93 | aucun |
| remarque 1 (N-030) | non comptée | appliqué, plus petite correction (consigne, point 2) : « ; **[Décision de Lazar en attente : N-030]** » dans la parenthèse de la puce | « Décisions prises depuis la v4 », puce N-030, l. 602 | texte du correcteur (le rapport ne donne pas de mots) |
| remarque 1 (nœud « Revendication ») | non comptée | appliqué, de même : « ; **[Décision de Lazar en attente : nœud « Revendication »]** » dans la parenthèse du titre du nœud ; libellé repris des mentions déjà présentes (l. 395, 396) | section 5, nœud « Revendication et voie de R-262 (2) », l. 446 | texte du correcteur |
| remarque 2 (P-017, en-tête) | non comptée | appliqué, de même : « options (A), (B), (C), (C') de P-017 » devient « (C') et la mise en options de P-017 (…) ; les options (A), (B) et (C) sont celles de P-017 (`registres/decisions.md` l. 394) » ; la mention d'attente P-017 est gardée | en-tête, puce « v6 », l. 51-52 | texte du correcteur ; l. 394 relue à `e8b73c64…` |

Non appliqués (la consigne n'en demande pas ; « aucune autre modification ») : remarque 3 (section « Décisions » écrite
du point de vue de la v5, « à dater si la section est reprise ») ; remarque 4 (note v2 de transmission à P3b, après la
v6) ; remarque 5 (erreur de la vérification « fidélité » de la v5 sur le compagnon de MA : elle vise ce rapport, pas la
synthèse).

**Déclaré, pour la session.** Par la même règle, la v7 n'a ni titre neuf ni puce « v7 » dans l'en-tête : son titre dit
encore « synthèse v6 », et sa provenance tient dans ce traitement et dans `…/revue-detection/correction-v7/`. Si une
v8 est écrite, y ajouter le titre et la puce « v7 ».

## Différentiel v6 → v7 rejoué

`…/revue-detection/correction-v7/verifier_v7.py`, sortie `sortie-verifier-v7.txt` (0 faute) :
- rejeu du script vers une copie : v7 identique octet pour octet ; `corrections-v7.json` égal à une nouvelle extraction ;
- blancs normalisés : v6 plus les 7 remplacements égale la v7 : **rien d'autre ne change** ;
- structure : lignes vides (32), lignes de table (59, même nombre de barres chacune), titres (10) égaux ; 694 → 698 lignes
  (quatre replis) ;
- 7 blocs de différentiel ligne à ligne (`differentiel-lignes-v6-v7.txt`), chacun rattaché à un seul remplacement ;
- mentions « [Décision de Lazar en attente » : 15 → 17 ;
- épreuve R5 des gardes du script : cas sain accepté ; ancien texte changé d'un mot (0 trouvé) et ancien texte doublé
  (2 trouvés) arrêtés ; garde d'empreinte : copie saine acceptée, compagnon faux, octets ajoutés avec compagnon
  recalculé, nom faux dans le compagnon, compagnon absent arrêtés (dossier d'épreuve supprimé après usage).

## v2 du traitement du correcteur v5 (VV5-fidelite-08)

`…/revue-detection/traitement-verification-v4-par-correcteur-v2.md` (`663f2b300c113ca7efec87e88b906b17b5a402eddf07eba83c30720844a1baf6`),
par `…/revue-detection/correction-v7/traitement_v4_v2.py` (v1 contrôlée par empreinte ; 2 remplacements exacts) : titre
« v2 » et une note de version ; colonne « écart » de VV4-sens-04 = « aucun (le constat demande une phrase ; elle est
faite de ses mots) », mots exacts de VV5-fidelite-08. Contrôle par script : écart rempli pour **13** constats sur 28,
VV4-sens-04 n'y est plus ; le « 13 » du bilan, juste, n'est pas touché. La v1
(`21e1d56c587867d277ca534105a2e6a61ab4f4ac9d03580fd1ac8d5758ddeecb`) reste intacte (R12, compagnon égal).

## Cadre tenu

Écrit seulement : la v7, ce traitement, la v2 ci-dessus, leurs sceaux, et `…/revue-detection/correction-v7/`. Non ouverts :
`R/prereg/P3-consignes-v1.md`, fichiers `textes-actions-*`, `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`. Aucune
recherche récursive, aucun réseau, aucune commande git d'écriture, aucun sous-agent, aucune dépense, aucune clé
affichée. Scripts lancés par `python3 -I -B`, `PYTHONDONTWRITEBYTECODE=1` : aucun `__pycache__`.

## Fichiers (sous `…/revue-detection/`)

- `synthese-comment-detecter-v7.md`, `traitement-verification-v6-par-correcteur-v1.md`,
  `traitement-verification-v4-par-correcteur-v2.md`, chacun avec son sceau `.sha256` ;
- `correction-v7/` : `appliquer_corrections_v7.py`, `verifier_v7.py`, `traitement_v4_v2.py`, `corrections-v7.json`,
  `sortie-appliquer-v7.txt`, `sortie-verifier-v7.txt`, `sortie-traitement-v4-v2.txt`, `differentiel-lignes-v6-v7.txt`,
  chacun avec son sceau `.sha256` (format `sha256sum`, nom relatif).
