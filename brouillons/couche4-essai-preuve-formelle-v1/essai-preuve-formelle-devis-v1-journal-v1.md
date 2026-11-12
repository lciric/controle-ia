# Journal — dessin et devis de l'essai « preuve formelle contre suite bon marché » (couche 4, pas (b) de R-2199) — v1

- **Auteur** : sous-agent neuf (rédacteur), Opus 5.5 (`claude-opus-5-5`), session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-devis-essai-preuve-formelle-couche4-v1.md`
  (`5403571b05f6733a69ec8e26cbd6ecc53d2d8243fe1c77288ee058c77d45cfba`, égale au compagnon), lue en entier avant toute autre action,
  interdits communs v2 compris.
- **Produit** : `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon1.md`
  (`9ccc9ac01cb95db8184f87629e3b77eaa24820717ffa29a822f471ccf91bdade`, scellé à 13:20:29 UTC). Aucun commit.
- Toutes les heures ci-dessous sont relevées par `date -u`.

## Chronologie

| Heure UTC | Fait |
|---|---|
| 13:00:30 | Consigne vérifiée par son compagnon et lue ; bac à sable créé (`…/scratchpad/agents/redacteur-devis-couche4/`). Empreintes des quatre pièces nommées égales aux préfixes de la consigne et à leurs compagnons. |
| ≈ 13:00–13:01 | Lecture : synthèse du tour 2 (en entier, trois tranches) ; synthèse v2 (en entier) ; registre R-920, R-946, R-957, R-959, R-2199 ; R-2200 à R-2226 filtrées par mots (couche 4, preuve formelle, Lean, N12, suite bon marché, génération, mathématiques) ; programme complet v2 (en-tête, § 2.1–2.6, famille MAT, lignes « lean »). |
| 13:01:14 | Inventaire sans réseau des vérificateurs et de la machine (résultats ci-dessous). |
| ≈ 13:02–13:05 | Prix : table de `collisionneur_v8.py` (l. 60–95) ; référence locale `claude-api` chargée (lecture locale, aucun appel d'interface). Repérage de la carte des hypothèses v1 (sans ouverture). |
| ≈ 13:05–13:09 | Calculs v1 puis v2 (contrôle des graines déplacé vers Gemini 4 Argon, voir « Choix »). |
| 13:09:53 | Jalon 1 du journal écrit, puis scellé avec les calculs v1 et v2. |
| 13:12:52 | Calculs v3 (pilote à 140 items, options des décisions, durées) et variantes de modèle ; scellés. |
| 13:13:37 | Dossier de sortie créé ; sections 0 à 3 du brouillon écrites. |
| 13:16:05 | Jalon 2 (instantané des sections 0 à 3) scellé dans le bac à sable. |
| ≈ 13:16–13:20 | Sections 4 à 8 ; option D-1 (ii) chiffrée par script ; relecture complète et corrections (voir « Corrections ») ; source des prix précisée (`shared/models.md`) ; contrôle mécanique des tableaux (0 défaut). |
| 13:20:12 | Table des empreintes assemblée par script et ajoutée au brouillon. |
| 13:20:29 | Brouillon scellé et vérifié (`OK 9ccc9ac01cb9…`). |
| (fin) | Présent journal écrit, puis scellé. |

## Inventaire de l'outillage (sans réseau, 13:01:14 UTC)

- `which` : `lean`, `lake`, `elan`, `coqc`, `coqtop`, `isabelle`, `agda`, `z3`, `cvc5`, `cvc4`, `vampire`, `eprover`, `metis`, `hol`,
  `sage`, `maxima`, `gp`, `mathematica`, `wolfram`, `ghc`, `opam`, `leanblueprint` : **absents** ; `python3`, `gcc` : présents.
- Répertoires : `~/.elan`, `~/.lake`, `~/.cache/mathlib`, `/opt/lean*`, `/usr/local/lean*` : **absents**.
- `.venv` (Python 3.13.16) : sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6, scipy 1.17.1, networkx 3.6.1 ; **absents** : hypothesis, z3,
  cvxpy, pysmt, lean_dojo, pantograph, leanclient. Python du système : sympy, mpmath, hypothesis, z3 absents.
- Machine : 4 cœurs ; mémoire 15 Go ; `/dev/vda` : **2,7 Go disponibles**, 94 % d'occupation (sortie de `df -h` : 252G, 37G
  utilisés, 2,7G disponibles — colonnes incohérentes entre elles, sans doute un quota ; seul le disponible compte ici).

## Prix relevés (aucun réseau)

- Référence locale `claude-api` : table « Current Models (cached: 2026-11-03) » servie au chargement de la référence, et sur disque
  `…/claude-api/shared/models.md` (`74245a8d…`) l. 78 (Fable 5.2 : 8 / 40 ; lecture en cache 0,20), l. 80 (Fable 5.1 : 10 / 50),
  l. 83 (Opus 5.5 : 4 / 20 ; lecture en cache 0,20), l. 89 (Sonnet 5.5 : 2 / 10). **À vérifier** sur la page publique.
- `collisionneur_v8.py` (`22e5ed8a…`) : l. 76–77 Kimi K3.1 Pro 2 / 10 « Prix vérifiés le 30 octobre » ; l. 73–74 Gemini 4 Argon
  10 / 50, « valeur volontairement haute » ; l. 79–82 GPT-6 Astra 10 / 50, « Prix SUPPOSÉS », identifiant « rapporté, à confirmer ».
- Écart noté : la référence locale donne Opus 4.6 à 5 / 25 alors que `collisionneur_v8.py` l. 71 le supposait à 15 / 75 (« prix
  SUPPOSÉ haut ») ; sans effet sur ce devis (Opus 4.6 n'y figure pas), signalé pour la mère.

## Choix du rédacteur (routine de dessin, tous « proposé, non tranché » au programme)

1. **Objet vérifié = squelette de la preuve** (chaque étape en lemme de premier niveau `etape_i`) : sinon une preuve fausse d'un
   énoncé vrai serait « vérifiée » par un autre chemin.
2. **Définition d'un item fautif** : une assertion écrite fausse pour une instance admissible ; les assertions vraies mal justifiées
   sont exclues (aucun bras n'y est notable équitablement). Point soumis à la contre-lecture (§ 8, point 8 du brouillon).
3. **Jumelles saine et fautive** issues de la même version renotée, pour que seul l'écart planté les distingue ; analyse
   conditionnelle aux paires formalisables comme première mesure secondaire.
4. **Contrôle des graines par une famille hors des bras** (Gemini 4 Argon, calculs v2) : la famille des relecteurs de la suite
   (Kimi) sélectionnerait les graines qu'elle juge saines et abaisserait à tort les fausses alertes de la suite.
5. **Témoin numérique enregistré, jamais exigé** : l'exiger favoriserait la suite (biais de facilité).
6. **Règle du « ou »** dans les deux bras (agent ou relecteur d'une autre famille), pour la symétrie.
7. **Choix des classes de confirmation par le rang de Δ̂ du pilote, quel que soit le signe** : la classe la plus favorable à Lean
   rend le négatif le plus fort possible et expose un positif à une banque neuve.
8. **O2 lu avec le rappel conditionnel** (ajout de la relecture) : un écart né des seuls échecs de formalisation serait sinon
   lu comme une détection.
9. **Mode d'appel par interface au jeton** (M1) recommandé : seul mode qui mesure le coût apparié par item.
10. **Sceau par jalons dans le bac à sable** sous noms versionnés : `scellement sceller` refuse d'écraser une empreinte (R12) ;
    les deux fichiers de sortie sont scellés une fois.

## Corrections faites pendant la rédaction (avant le sceau)

- Calculs v1 → v2 : contrôle des graines déplacé de Kimi vers Gemini 4 Argon (choix 4). v2 → v3 : pilote porté de 130 à 140 items
  (10 saines renotées une seconde fois), options des décisions et durées ajoutées. Les sections 1 et 2 des sorties sont identiques
  d'une version à l'autre (vérifié par `diff`).
- Étapes formelles : « assertions intermédiaires » remplacées par des **lemmes de premier niveau** (des `have` locaux ne
  s'impriment pas par `#check`) ; garde des axiomes étendue à chaque `etape_i`.
- Tableau du § 2.1 : une citation contenait des barres verticales qui cassaient le tableau ; reformulée.
- A8 : étalonnage reformulé par graines (deux items vus par les deux bras) et **blocs équilibrés** pour qu'une coupure garde
  l'équilibre des classes.
- Option D-1 (ii) : montant ajouté par script (`option_pilote_reduit_v1.py`) pour respecter R6.
- § 4.1 : source des prix précisée (`shared/models.md`, lignes) et note sur le cache (0,05 fois pour Opus 5.5 : l'attendu est
  prudent sur ce point).

## Fichiers du bac à sable (scellés ; non versés au dépôt)

Chemin : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/redacteur-devis-couche4/`.
`calculs_devis_essai_v1.py` (`6f374d0c…`), `sortie-calculs-devis-v1.txt` (`7fb79ee3…`), `calculs_devis_essai_v2.py` (`d57e176b…`),
`sortie-calculs-devis-v2.txt` (`d6492d79…`), `calculs_devis_essai_v3.py` (`236371fd…`), `sortie-calculs-devis-v3.txt`
(`18221e7b…`), `variantes_modele_bras_v1.py` (`25ff8f46…`), `sortie-variantes-modele-bras-v1.txt` (`3651c56c…`),
`option_pilote_reduit_v1.py` (`cb8a5dc2…`), `sortie-option-pilote-reduit-v1.txt` (`6a4d0ae6…`), `jalon1-journal-v1.md`
(`966949d5…`), `jalon2-brouillon-sections-0-3-v1.md` (`4b98b352…`). Empreintes complètes : table du brouillon, calculée par
script. **Point pour la mère** : les chiffres du brouillon renvoient à ces scripts ; s'ils doivent survivre au bac à sable (R6), il
faut les verser au dépôt (je ne l'ai pas fait : la consigne ne nomme que deux chemins de sortie).

## Exposition, cloison, interdits

- **Aucun chemin des interdits communs ouvert** : rien sous `diag/`, `runs/`, `donnees/`, `docs/notes/bras-attaque/`, aucune
  branche de quarantaine, aucune cellule de collisionneur (seules les synthèses ont été lues).
- Recherches : `git grep` avec exclusions de `docs/notes/bras-attaque`, `scripts/extraire_mesures_epreuve_t06_v1.py`, `diag`, `runs`,
  `donnees` ; `grep` et `sed` dans des fichiers nommés ; `git ls-files` filtré ; **aucune** recherche récursive non exclue.
  `git log --all --name-only -- '*carte-des-hypotheses*' '*carte-hypotheses*'` a listé des **noms** de fichiers d'une branche du
  canal (`brouillons/canal-reprise-releve-v1/envois/theorie-v1/carte-des-hypotheses-v1/…`) et deux messages de commit (dont
  celui de `9778cd6f3`, qui annonce des amendements de la carte) ; aucun fichier n'a été ouvert.
- Dans le registre, R-2200 à R-2226 ont été filtrées par mots-clés ; les débuts de ligne affichés (R-2200, R-2215, R-2221, R-2223,
  R-2226) ne portent rien du bras ni du mode tenu à l'écart au-delà de ce que le programme complet cite déjà ; un premier
  affichage brut de ces lignes a été tronqué par l'outil (enregistré par lui dans un fichier de sortie que je n'ai pas relu).
- **Aucun appel de modèle ni d'interface externe, aucune installation, aucun réseau, aucune dépense, aucune opération git
  d'écriture** (ni commit, ni index). La référence locale `claude-api` a été chargée comme compétence (lecture locale) ;
  aucune de ses procédures n'a été exécutée.
- Aucun refus de contrôle de permissions ni de classifieur rencontré.
- Aucune valeur numérique d'une sonde de la course 7a n'est passée sous mes yeux ni n'est citée.
- **Même famille** : je suis du modèle Opus 5.5, que le brouillon recommande pour les deux bras ; conflit déclaré en tête du
  brouillon et à faire vérifier par la contre-lecture (R2).
