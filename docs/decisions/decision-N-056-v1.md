# Décision — N-056 : nœud 1 de G1 (option b), nœud 2 (option c, lue, non confirmée), traits internes (a), règle de H1 entre modes (a), GO « bras d'attaque » (montage, sans dépense), GO « autres mesures fortes » (v1)

- **Décisions de Lazar**, dans la session de « conv-audit » (27 octobre 2026, 23:10 à 23:47 heure de Paris, 22:10 à 22:47 UTC) ; provenance des mots cités : par relais (R-331).
- **Transcription** par la lignée « session-depot », le 27 octobre 2026 vers 22:56 UTC, de la note `envois/decision-N-056-noeuds-G1-bras-attaque-mesures-fortes-v1.md` (`canal/conv-audit-n04`, commit `36bb254`, sha256 `6aac9746543cd05d0fc4fb89b32938d272e9b9723dab820d191cbb8297669eff`, vérifiée contre son compagnon), reprise ci-dessous sans changement ; numéro retenu : N-056.
- **Portée** : lecture du programme en attendant une version nouvelle ; `docs/programme-controle-ia-v2.md` n'est pas modifié. **Nœud 2 (option c) : inscrit « lu, non confirmé »** tant que le mot de Lazar manque. **Le GO « lancer l'instance d'attaque » n'est pas tenu pour donné par cette note** (message coupé) : session-depot demande le mot direct de Lazar avant tout lancement. Aucune dépense n'est engagée par cette inscription.

---

# Décisions de Lazar : nœud 1 de G1 (option b), nœud 2 (option c, à confirmer), traits internes (a), règle de H1 entre modes (a), GO « bras d'attaque », GO « autres mesures fortes » — N-056 (proposé) — v1

Note écrite par conv-audit le 2026-10-27 après le relevé `date -u` de 22:51:47 UTC. Nœuds « modification de décision »
(N-007, N-008, N-054) et deux GO : Lazar décide, conv-audit relaie, session-depot inscrit (conv-audit n'écrit pas
`main`). Provenance des mots cités : par relais (R-331), session de conv-audit servie par Fable 5.1 à cette heure.
**Aucune dépense n'est engagée par cette note** : la seule dépense qu'elle ouvre (l'instance d'attaque, « quelques
dollars » selon N-054) passe par le mot direct de Lazar chez session-depot, qui lance.

## Mots de Lazar, verbatim (session de conv-audit, heure de Paris)

- **23:10** (en réponse au message de fin de session de conv-audit, fragments collés des options) :
  > (b) exiger aussi que la boîte blanche batte les deux bases boîte blanche : G1 dirait plus, mais mélangerait deux
  > questions et demanderait plusieurs centaines de tâches de plus. (c) le pari décide, le rééchantillonnage est rapporté
  > à côté. (a) Trois couches du réseau, toutes rapportées ; Dans quels modes de sabotage le gain doit-il se voir ? Je
  > recommande : dans chacun des autres modes, mode tenu à l'écart compris.
- **23:39** : « Inventer des modes de sabotage inédits, jamais documentés : il faut trouver de nouvelles failles dans les
  methodes actuelles d'alignment et ai control »
- **23:47** :
  > Les autres mesures proposées (synthèse « mesures fortes », `bed9107b…`, sur `main`) : go [...] Un mode candidat doit
  > venir d'une instance qui n'a vu aucun moniteur : mais pour inventer de nouveaux modes de sabotage ou de
  > désalignement, ne faudrait-il pas se mettre à la place du mode attaquant et donc connaître les moniteurs utilisés ou
  > les méthodes de contrôle mises en place ? Nœud 1 (contre qui G1 gagne) : : b ; monter le bras d'attaque pour que ça
  > se fasse proprement — brief, liste d'exclusions, témoins, juge, circuit de scellement. : go, Ce qui te revient. Le GO
  > pour lancer l'instance d'attaque — une instance neuve, dans une autre session que la mienne (session-depot ou une
  > lignée tierc
  (le message s'arrête là : coupé à l'envoi) ; puis : « reprends une autonomie de 8h avec depot ».

## Ce que cela fixe

1. **Nœud 1 — contre qui G1 doit gagner : option (b)** (`pari-de-signe/noeuds-pour-lazar-v1.md`, `d9a6ff1b…`). La porte
   G1 exige que le séquentiel boîte blanche batte **chaque moniteur boîte noire de la liste scellée** (N-007, N-008)
   **et** les deux bases boîte blanche de N-007 : **(ii) la cascade de portes** sur les mêmes sondes et **(iii) la sonde
   sur le dernier état**. Conséquences dites à Lazar et acceptées par lui : G1 porte deux questions à la fois (« lire
   l'intérieur apporte quelque chose » et « notre accumulation bat les autres façons de lire l'intérieur ») et un échec
   ne dira pas laquelle a échoué ; la puissance est celle du contraste le plus difficile (blanc contre blanc : écart
   probablement petit), soit **plusieurs centaines de tâches sabotées de plus par mode** au devis de la couche 2 ; dans
   le pari apparié borné, la liste d'intersection-union de G1 comprend (ii) et (iii) (D-S8 réécrite ; conception v9).
   Les planchers restent rapportés, hors décision. H2 garde ses propres tests de (ii) et (iii) (H2c).
2. **Nœud 2 — intervalle de l'expérience de lecture de N-054 point 4 : option (c)**, *lue dans les fragments de 23:10*
   (« (c) le pari décide, le rééchantillonnage est rapporté à côté ») — **à confirmer d'un mot par Lazar** ; session-depot
   l'inscrit comme « lue, non confirmée » tant que ce mot manque. Sous (c) : la décision « H1 restreinte au mode coût ou
   non » est prise par la borne basse du pari apparié (valide à tout nombre de tâches) ; les intervalles par
   rééchantillonnage des tâches prévus par N-054 sont rapportés à côté.
3. **Traits internes de l'agent comme traits du pôle : option (a)** (proposition du message n° 122) — trois couches
   (7, 15, 23), toutes rapportées, projection ajustée sur le seul calibrage ; c'était la recommandation et le défaut ;
   Lazar la retient avant le défaut. Lecture lancée par conv-audit sur processeur (zéro dépense).
4. **Règle de H1 entre modes (D-S29) : option (a)**, lue dans les fragments de 23:10 (« dans chacun des autres modes,
   mode tenu à l'écart compris ») : nœud de porte, fixé au préenregistrement de G1 ; conséquence : le mode tenu à l'écart
   doit être dimensionné comme les autres modes (poste de devis de la couche 2, conception v6 et suivantes).
5. **GO « autres mesures fortes »** (23:47 : « go ») : conv-audit prépare les mesures de la synthèse partielle
   (`docs/notes/collisionneur-mesures-fortes-v1/synthese-mesures-fortes-v1.md`, `bed9107b…`) **dans l'ordre : préenregistrement,
   contre-lecture (R2), scellement, puis seulement lecture** (R1) ; la mesure unanime (fausses alertes de l'agrégateur
   séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée) d'abord, sur les sondes figées de P3 et
   les vecteurs de T0.5 (processeur, zéro dépense) ; les autres au plan `mesures-fortes-plan-v1.md`, celles qui demandent
   des épisodes sabotés allant au devis de la couche 2.
6. **GO « monter le bras d'attaque »** (23:47 : « go ») : conv-audit écrit les briefs, les listes d'exclusions, les témoins
   par renvoi, la spécification du juge et le circuit de scellement (`pole-scientifique-automatique-v1/bras-attaque-v1/`),
   **sans produire aucune recette**. Deux bras, à la suite de la question de Lazar (23:47) et de la réponse de conv-audit
   (23:5x) : **(A) le mode tenu à l'écart, aveugle aux moniteurs** (N-054 point 3, inchangé) ; **(B) le bras d'attaque
   informé** (programme de conception section 3, point 3 : « go » du 27 à 14:32), dont le concepteur **connaît** les
   conceptions des moniteurs et le protocole de contrôle, mais pas les épisodes d'épreuve, les notes ni les seuils
   calibrés ; quarantaine dans le sens attaquant → concepteurs de moniteurs (recettes scellées, lues par le seul juge,
   révélées à l'évaluation ; N-053 point 5 : invariant « aucun score de moniteur dans un signal d'entraînement, hors bras
   d'attaque déclaré »). Conv-audit, concepteur des moniteurs, ne conçoit ni ne lit les recettes.
7. **GO « lancer l'instance d'attaque »** : le message de Lazar cite la phrase de conv-audit « Le GO pour lancer l'instance
   d'attaque — une instance neuve, dans une autre session que la mienne (session-depot ou une lignée tierce) » et
   s'interrompt. Conv-audit **lit un GO** ; comme le lancement est une dépense (petite) et que le texte est coupé,
   **session-depot demande à Lazar le mot direct dans sa propre session avant de lancer** ; sans ce mot, les briefs sont
   prêts et rien ne tourne.
8. **« Reprends une autonomie de 8h avec depot »** (23:47) : conv-audit repart pour huit heures (programme au message
   n° 124), en coordination avec session-depot ; rien ne dépense sans mot direct chez session-depot.

## Ce que cela ne fixe pas (reste à proposer)

- Les textes à modifier à la prochaine version du programme : § 13 (critère de G1 avec les bases (ii) et (iii)) ; le
  brouillon 3 du préenregistrement de G1 ; D-S8 et le dimensionnement de la couche 2 (conception v9 du pari).
- La confirmation du nœud 2 (option c) et, si Lazar le veut, celle de D-S29 (a).
- Qui héberge l'instance d'attaque (session-depot ou une lignée tierce), et le dépôt des recettes scellées (branche de
  données non lue par conv-audit, empreinte au registre).

Numéro proposé : N-056. Aucune dépense n'est engagée par cette note.
