# Journal du brouillon 2 du préenregistrement de la course réelle de l'organisme (code v66, configuration v6) — v1

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, sous-agent de la session mère
  `session_01VJdZpSMxSdk2SJ1ScmdfNv`. Je n'ai écrit ni le brouillon 1, ni le code v65 ou v66, ni leurs contre-lectures, ni le
  devis, la puissance ou l'essai à blanc v1.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-redaction-prereg-course-v66-b2-v1.md`,
  sha256 `bfdc52ad2309636e42f28cc565a8e4e9c1a94c1b89a229224b4c000f90f9ac6d`, vérifiée par `sha256sum` avant lecture (égale à
  celle donnée par la mère). Interdits communs v2 (`interdits-communs-v2.md`, `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`, empreinte vérifiée) recopiés dans la consigne : lus et tenus.
- **Heures** (temps universel, relevées par `date -u`, 10 novembre 2026) : début 14:29:39 ; lectures jusqu'à 14:41 ; couples
  écrits à partir de 14:41:50 ; script final joué à 14:49:38 ; journal écrit à partir de 14:49:50 (heure de fin dans le rapport
  à la mère).
- **Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit, aucune modification de l'index.** Arbre de
  l'organisme `/home/user/organisme-v65-cl` lu par `git show` seulement (et `git rev-parse`, `git branch --show-current`,
  `git status --short` en lecture, au début) : tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, `git status` vide ; aucun essai
  de l'organisme lancé, aucun de ses modules importé. Écrit seulement : les quatre fichiers ci-dessous (noms neufs) et mon bac à
  sable `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/prereg-course-v66/`.

## 1. Sorties (dossier `docs/notes/organisme-boucle-reelle-v1/`)

| fichier | sha256 | rôle |
|---|---|---|
| `preenregistrement-boucle-reelle-organisme-v1-brouillon2.md` | `f87ad0e40f1b2941e66d343bfb4b5eeaaefa22a3e2eeb448f852900de112b8a7` | brouillon 2 (non scellé au sens de R1 ; compagnon `.sha256`) |
| `couples-brouillon2-boucle-reelle-v1.json` | `43ba74e9db5ae92fe8da11cd460019640a91e24af9765d39420d991076db2edf` | 40 couples (textes ancien et nouveau, section, section gelée ou non, constat) et l'ajout B2-41 ; contrôles |
| `faire-brouillon2-boucle-reelle-v1.py` | `14011931026a3ab2d71720a1475d0e4af8b22d2107efc0aa2686b96b75012f45` | script qui vérifie les entrées, applique les couples, porte les blocs, contrôle |
| `journal-brouillon2-boucle-reelle-v1.md` | (ce fichier ; empreinte à son compagnon) | sources, couples, sections gelées touchées, nœuds, questions |

Brouillon 1 intact : `736e3fd63ad5ab4e1c5e9f930b0ce33b8a9d26a6ce87be7f0eea231f76e3a2db` avant et après.

Commande jouée (depuis `/home/user/controle-ia-travail`) :
`.venv/bin/python -I -B docs/notes/organisme-boucle-reelle-v1/faire-brouillon2-boucle-reelle-v1.py --depot /home/user/controle-ia-travail --brouillon2 docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-brouillon2.md --couples docs/notes/organisme-boucle-reelle-v1/couples-brouillon2-boucle-reelle-v1.json`
→ code 0. Le même script joué avant dans mon bac à sable a rendu le même brouillon, octet pour octet (`f87ad0e4…`).

**Contrôles du script** (sans importer l'organisme) : chaque texte ancien trouvé une seule fois au moment de son application ;
chaque marque des trois blocs une seule fois ; les trois blocs égaux à l'octet à `blocs-pour-le-texte-v66.md` (`9933ee11…`)
hors la ligne `go` ; plan aux 16 clés et aux valeurs du développeur hors `go`, sommes au centime (33 + 7 = 40 ; 40 + 5 = 45) ;
empreinte des octets JSON du bloc `jeu-plante-v65` = `21b4b0058672deb36a2312370324f2fcc5065576f18f2b69a97eda84f84eb41e` ;
98 empreintes de code gelé ; marqueurs restants exactement `GO_COURSE_V66` (3 occurrences) et `NOEUD_C1_SANS_RETENUE` (1),
au motif du lanceur (`<<[A-Z0-9_-]+>>`).

## 2. Sources lues (empreintes vérifiées)

- Brouillon 1 `736e3fd6…` ; devis `60643868de86bb5be71393283e6ecf8dc7c03998a072519bc479af8943a26437` ; puissance
  `a2afcdd3…` et `f552b1b9…`, sorties `a23959fa…` et `fe2bc502…` (sorties console lues) ; essai à blanc v1 (empreintes du
  dossier vérifiées ; journal non relu en entier).
- Code v66 : rapport `f6433d38c701934b6c2d04ed7011a4864088af4e4cb36e5b01f5ffdced62bd59` ; blocs `9933ee11…` ; héritage
  `93dcf517…` ; configuration v6 `4743ddbe…` (et ses commandes v6) ; journal de l'essai à blanc v66 ; heures de la suite et
  du banc.
- Contre-lectures : v65 `c4ddfc7ffd4b5cea1b0eb70e2a08ea551c8a8e8ef6f1a169ef8bebdab976ed03` ; v66
  `a28803689558e6813f24f625915c823b6a8c1c17802e351ae3f0f4dd9d3b7b00` (CLV66-01 à CLV66-08).
- Code de l'organisme, par `git show HEAD:…` : `demonstrations/boucle_reelle_v66.py` (`e2dd83ab…`, entier),
  `pole/lecture_boucle_reelle_v66.py` (`0152103a…`, entier), `pole/boucle_reelle_v66.py` (`ea17a4b8…`, en grande partie),
  `demonstrations/lire_boucle_reelle_v66.py` (`e2183565…`), `demonstrations/preparer_boucle_reelle_v66.py` (`c6a7e110…`),
  `pole/registre_go_v66.py` (en-tête et motifs), `pole/boucle_reelle_v65.py` (blocs, juge, copies), noms d'essais ; listes des
  fichiers des commits `cef5ea60`, `838fa68`, `3ba4727`, `7e415cb` (`git show --stat`).
- Registre (`registres/decisions.md` par `git grep` sur ce seul fichier) : R-1738, R-2206, R-2215, R-2220, R-2234, R-2243,
  R-2244 ; `registres/go.md` (`2c396b016d4ab86bd3f09cc7e21173f19d0c9765cc1a85b8efc08e59c2bc39f0`) : lignes GO-2026-11-07-11,
  GO-2026-11-08-02, GO-2026-11-08-05 (rendue par la même recherche), GO-2026-11-10-10, et l'en-tête du registre ; décisions
  N-058 (`854f2724…`), N-064 (`387c9d4e…`), N-065 (`f820e90d…`), lues en entier.
- Outils du dépôt de travail : `prereg/gabarit-preregistrement-v1.md` (`8cad4371…`), `src/controle_ia/prereg.py` (début) ;
  exemple de script de couples (`brouillons/T0.8-bases-boite-noire-v0-v1-brouillon2-faire-v1.py`, début) et
  `docs/notes/epreuve-etiqueteur-v1/appliquer_couples_brouillon6_v1.py` (début), pour la forme.

**Exposition déclarée (règle 9 des interdits communs)** : pour trouver un exemple de fichier de couples, j'ai lancé
`git ls-files docs/notes | grep -i couples`, qui parcourt les **noms** de `docs/notes/` sans exclure `docs/notes/bras-attaque/`.
Aucun contenu n'a été ouvert ; le filtre n'a affiché que des chemins de `docs/notes/epreuve-etiqueteur-v1/`. Rien n'en est
repris. Un essai ciblé a été joué : `controle_ia.prereg.problemes` sur le brouillon 1 puis sur le brouillon 2 (question Q-4).
Aucun refus de permission ni de classifieur rencontré.

## 3. Couples (41 : 40 par texte ancien ou bloc, plus l'ajout de la section 16)

| id | section | gelée | constat | objet |
|---|---|---|---|---|
| B2-01 | titre | non | brouillon 2 | titre : brouillon 2 |
| B2-02 | en-tête | non | brouillon 2 ; CLV66-04 ; CLV66-07 | statut du brouillon 2, marqueurs restants, ce qui précède toute course |
| B2-03 | en-tête | non | brouillon 2 | rédacteurs des brouillons 1 et 2 |
| B2-04 | en-tête | non | brouillon 2 | heures du brouillon 2 |
| B2-05 | en-tête | non | brouillon 2 ; CLV66-07 | consigne du brouillon 2, lignes de GO et de registre |
| B2-06 | en-tête | non | brouillon 2 | arbres du brouillon 2 ; code v66 |
| B2-07 | Documents qui font foi | non | brouillon 2 | pièces de l'organisme : code v66 et v65 réutilisé |
| B2-08 | Documents qui font foi | non | brouillon 2 | rangées neuves : code v66, v65 réutilisé, configuration v6 |
| B2-09 | Documents qui font foi | non | brouillon 2 ; N-064 ; N-065 | pièces du dépôt de travail : code v66, contre-lectures, dossier de course, N-064, N-065 |
| B2-10 | Documents qui font foi | non | brouillon 2 | pièces versées depuis le brouillon 1 |
| B2-11 | 0. En dix lignes | non | CLV66-04 | preuve de lecture de la sélection vide sans carte retenue |
| B2-12 | 0. En dix lignes | non | brouillon 2 | ce qui manque avant de sceller |
| B2-13 | 1. Question, motivation, ce qui existe | non | brouillon 2 | écrit pour la course depuis le brouillon 1 : code v65, v66, contre-lectures |
| B2-14 | 1. Question, motivation, ce qui existe | non | N-064 ; N-065 | voisins publiés cités (N-064, point 4) ; place de l'organisme (N-065) |
| B2-15 | 3. Dessin | non | brouillon 2 | règle des lois plantées : juge v65 et v66 |
| B2-16 | 3. Dessin | non | CLV65-09 ; rapport v66, section 9 | utilisateur 64097, lanceur en superutilisateur |
| B2-17 | 3. Dessin | non | CLV65-03 ; CLV65-13 ; CLV66-08 | génération 2 : vue servie vérifiée (garde 23) ; lois plantées promues aussi testées (cas de brèche) |
| B2-18 | 4. Prédictions | **oui** | CLV65-03 | P6 : la vue comparée est la vue servie (garde 23) |
| B2-19 | 5. Métriques | **oui** | CLV65-03 ; CLV66-02 | lecture de la sélection : empreinte relue sur disque, vue servie, vérifications V |
| B2-20 | 5. Métriques | **oui** | CLV65-08 ; rapport v66, section 9 | intervalles de Wilson : les six parts par fournisseur de P7 |
| B2-21 | 5. Métriques | **oui** | CLV65-08 ; rapport v66, section 9 | jetons : champ `usage` des commandes, sommes par relais |
| B2-22 | 7. Plan d'analyse | **oui** | CLV65-11 ; CLV66-01 à CLV66-04 | ordre : programme de lecture v66, empreinte du relevé exigée, oracle lu, vérifications V |
| B2-23 | 7. Plan d'analyse | **oui** | CLV65-08 ; rapport v66, section 9 | recherche de la loi plantée : échos de la loi gelée ; lignes de tranche servies |
| B2-24 | 8. Critères de lecture gelés | **oui** | CLV66-01 à CLV66-04 | programme et texte : l'issue du texte prime ; vérifications V-1 à V-8 |
| B2-25 | 8. Critères de lecture gelés | **oui** | CLV65-01 ; CLV66-01 ; contre-lecture v66, section 3 | ligne C5 : relevé incomplet défini ; arrêt de la garde 18 en génération 2 lu C5 et « C4 (partielle) » ; écart de membres en génération 2 lu C4 |
| B2-26 | 8. Critères de lecture gelés | **oui** | CLV65-03 ; CLV66-02 ; CLV66-03 | ligne C4 : vue servie ; écarts relevés par V-4, V-5, V-6 |
| B2-27 | 8. Critères de lecture gelés | **oui** | CLV66-02 ; CLV66-04 | ligne C1 : V-1 à V-7 exigées ; sélection vide dite en tête ; marqueur du nœud NL-1 |
| B2-28 | 8. Critères de lecture gelés | **oui** | CLV66-01 à CLV66-04 | table des vérifications V-1 à V-8 sur le relevé brut |
| B2-29 | 9. Audit de symétrie | **oui** | CLV65-01 ; CLV66-04 | A1 : champ absent jamais « vrai » ; sélection vide notée ; pièces brutes |
| B2-30 | 10. Liste d'arrêt | **oui** | CLV65-05 ; rapport v66, section 9 | texte scellé au chemin fixé ; garde 7 complète |
| B2-31 | 10. Liste d'arrêt | **oui** | CLV65-04 ; rapport v66 | gardes neuves essayées (artefact partout ; cas sain sauf garde 22, à jouer sur la machine) |
| B2-32 | 10. Liste d'arrêt | **oui** | CLV66-01 | garde 18 : lecture d'un arrêt en génération 2 |
| B2-33 | 10. Liste d'arrêt | **oui** | CLV65-09 ; CLV65-03 ; rapport v66 | garde 22 précisée ; garde 23 neuve |
| B2-34 | 10. Liste d'arrêt | **oui** | CLV65-02 (a) | arrêt : jugements déjà au relevé partiel |
| B2-35 | 11. Prémortem | non | CLV65-09 ; contre-lecture v66, section 6 | essai à blanc `--bac reel` avec 64097, en superutilisateur |
| B2-36 | 11. Prémortem | non | CLV65-03 ; CLV66-04 | sélection non lue : garde 23 ; preuve vide sans carte retenue |
| B2-37 | 12. (réécrite) | non | rapport v66 ; contre-lecture v66, section 6 ; CLV66-05 ; CLV66-07 | fait ; avant le scellement ; six préalables sur la machine ; commandes exactes |
| B2-38 | 13. Devis | non | CLV66-07 ; CLV65-10 | GO de la course : ligne neuve à identifiant neuf ; plafond de la machine |
| B2-39 | 14. Portée | non | CLV66-04 | portée : C1 sans carte retenue |
| B2-40 | 15. Contre-lecture | non | brouillon 2 ; contre-lectures v65 et v66 | contre-lecture du texte à faire ; traitement des constats du code |
| B2-41 | 16. Blocs gelés (neuve) | non (mais lue par le lanceur) | rapport v66, section 7 ; CLV66-07 | trois blocs du développeur à l'octet, ligne `go` portant le marqueur de la ligne de GO neuve |

## 4. Sections gelées touchées, une par une (consigne, point 6)

Sections gelées au sens du gabarit : 2, 4, 5, 6, 7, 8, 9 (rattachée aux critères), 10. **Aucune hypothèse (section 2), aucun
seuil (section 6), aucun signe ni chiffre de prédiction (section 4) ne change.** Dix-sept couples touchent une section gelée :

- **B2-18 (P6)** : « vue » devient « vue servie aux proposeurs (consignée au moment du service, garde 23) ». Alignement sur la
  correction CLV65-03 du code gelé (la lecture v66 compare déjà la vue servie) ; même signe, même réfutation. Voir Q-2.
- **B2-19 à B2-21 (métriques)** : précisions de ce que le code gelé mesure déjà (empreinte relue sur disque ; six parts de
  Wilson de P7 ; jetons lus dans `usage`, sommés par relais, appels sans `usage` comptés à part). Aucune métrique de
  décision changée ; rapport du développeur v66, section 9, point 2.
- **B2-22, B2-23 (plan)** : programme de lecture nommé, `--releve-sha256` exigé, `--sans-oracle` exclu de la lecture décisive,
  vérifications V après le programme ; règle des échos de la loi gelée (JSON canonique « dans », autre forme « hors », relue
  à la main) et mesure des lignes de tranche servies, sans issue.
- **B2-24 à B2-28 (critères)** : mandat de la consigne, points 2 et 3. Le texte prime sur le programme ; V-1 à V-8 ; ligne C5
  (CLV66-01 : V-3 ; clause recommandée par la contre-lecture v66, section 3, sur l'écart de membres en génération 2) ; ligne C4
  (vue servie, écarts V) ; ligne C1 (CLV66-02 : V-1, V-2, V-4 ; phrase de CLV66-04 ; marqueur du nœud). **V-5 à V-7, et la
  partie `lu_sur_disque` de V-4, viennent de CLV66-03 (mineur) et vont au-delà du mandat : Q-1.** Aucune de ces vérifications
  ne change l'issue d'un relevé que le cœur gelé peut produire, d'après la contre-lecture v66 ; vérifié à la lecture du cœur
  (`jouer_generation`, `jouer_boucle`) pour V-4 à V-7 : sur une course complète, `vues_servies[g].appels` porte un appel par
  proposeur, chaque texte reçu égal au texte bâti (sinon la garde 23 arrête), `lu` et `lu_sur_disque` égaux à `attendu`
  (bilan vérifié par `lire_heritage` puis relu), `selection_finale.lu` = `bilan_sha256`, `retenues["1"]` et `["2"]` écrites.
- **B2-29 (A1)** : note de la sélection vide ; un champ absent n'est jamais « vrai » (déjà dans la lecture v66).
- **B2-30 à B2-34 (liste d'arrêt)** : mandat (« gardes 23 et 7 dans la liste d'arrêt ») ; garde 22 telle que codée en v66 ;
  correction d'une phrase du brouillon 1 qui aurait été fausse (« à essayer ») et d'une affirmation que je ne pouvais pas
  tenir (cas sain de la garde 22 non joué sans `bwrap`, dit dans B2-31).

## 5. Nœuds pour Lazar

### NL-1 — Issue C1 quand la génération 1 ne retient aucune carte réelle (CLV66-04 ; arrêt sur ce point, consigne point 3)

- **Décision en une phrase** : quand la course tient P1, P4, P6 et V-1 à V-7 mais que la génération 1 n'a retenu aucune carte
  réelle, l'issue reste-t-elle C1 « la chaîne garde », ou devient-elle une issue à part qui dit que la fermeture de la boucle
  n'est pas éprouvée ?
- **Enjeu** : sans retenue, la génération 2 lit une sélection vide ; P5 n'a aucune copie à refuser et P6 compare {K1} à
  {K1} ∪ ∅. La partie (c) de H-boucle (« la génération suivante juge avec la sélection de la précédente ») n'est pas
  éprouvée sur un contenu : un défaut qui ignorerait le contenu de la sélection passerait. Les parties (a) et (b) restent
  éprouvées (vraies survivantes ; F1 à F4 refusées dans les deux générations, jugées avec une archive). Le cas arrive si les
  proposeurs ne rendent aucune carte lisible, ou si aucune carte n'est promue puis survivante ; sa probabilité n'est pas
  mesurée (premier passage de ces proposeurs dans ce monde) ; la contre-lecture v66 l'a produit par sonde, lu C1.
- **Ce que le brouillon 2 écrit sans attendre** (aucun critère changé : mandat de la consigne) : la phrase de résultat le dit
  en tête (ligne C1, V-8), A1 le note, la portée le dit. **Ce qui attend Lazar** : l'issue elle-même ; le marqueur
  `NOEUD_C1_SANS_RETENUE` empêche de sceller avant sa décision.
- **Options** :
  - (a) **Garder C1**, avec la phrase en tête. Avantage : aucun critère changé, rien à recoder, le programme rend déjà C1.
    Inconvénient : « la chaîne garde » et « ouvre la proposition de plusieurs générations » restent prononcés alors que la
    fermeture n'a pas été éprouvée ; risque d'une lecture trop belle (R4).
  - (b) **Issue à part, C7 « la chaîne garde, boucle non éprouvée »**, placée entre C6 et C1 : conditions de C1 et
    `retenues["1"]` vide ; elle dit que (a) et (b) de H-boucle tiennent et que (c) n'est pas éprouvée ; elle ouvre la
    proposition d'une course qui éprouve (c), non celle de plusieurs générations sur la foi de cette course. Prononcée par le
    lecteur du verdict sur V-8, le programme gelé rendant C1 (même mécanisme que V-1 à V-7, aucun code changé). Avantage :
    l'issue ne dit pas plus que ce qui est éprouvé ; même traitement que les autres vérités à vide (CLV65-01). Inconvénient :
    changement de critère de lecture ; une issue que le programme ne sait pas écrire.
  - (c) **Changer le dessin** pour que (c) soit toujours éprouvée (par exemple une loi « porteuse » que la génération 1 a le
    droit de retenir). Avantage : la fermeture est toujours éprouvée. Inconvénient : contredit la garde 7 (lois plantées
    jamais retenues) ; code v67, contre-lecture et texte neufs : plusieurs jours de retard, sans dépense.
- **Recommandation** : (b), confiance ≈ 0,6 (coût nul, aucune ligne de code, issue exacte ; si Lazar préfère ne toucher à
  aucune issue, (a) reste sûr à condition que le verdict tienne la phrase en tête).
- **Défaut** : aucun (changement de critère de lecture : nœud, pas de défaut à 48 heures).

### NL-2 — Ligne de GO neuve pour la course (CLV66-07 ; consigne point 4)

- **Décision en une phrase** : inscrire au registre une ligne de GO de calcul neuve, à identifiant neuf, de 45 USD, pour la
  course au code v66 et à la configuration v6.
- **Enjeu** : GO-2026-11-08-02 exige « le code v65 contre-lu » et GO-2026-11-10-10 « code v65 contre-lu » et une
  « configuration v5 (`995eb918…`) » qui n'existe pas (v5 = `bff138d8…`, v6 = `4743ddbe…`) ; la course jouerait donc hors des
  conditions écrites de l'un comme de l'autre. Une ligne d'extension ne convient pas : le lanceur v66 refuse tout GO qui en
  porte une.
- **Ligne proposée** (huit colonnes ; l'identifiant et la date sont ceux du jour de l'inscription ; aucune barre verticale
  dans les cellules ; la cellule du plafond doit rester un montant seul pour que le lanceur la lise) :

  `| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | **Organisme : plus petite course réelle de la boucle complète, code v66 et configuration v6** (remplace, pour cette course, GO-2026-11-08-02 et la part « organisme » de GO-2026-11-10-10, qui restent intactes et ne se cumulent pas avec elle) ; conditions toutes exigées : code v66 (7e415cbaaa3ff602db43a44dad6b4307c08352c7) contre-lu (contre-lecture-code-v66-courte-v1.md, a2880368…) ; configuration v6 (4743ddbe4d294643ac8e1924476dec056b1a08dac9f8010cd647dd1861160b0d) ; machine jetable à bwrap validée par l'essai à blanc --bac reel ; préenregistrement de la course scellé ; 40 USD de modèles (Kimi 33, Argon 7) et 5 USD de machine ; jamais de ligne d'extension | 45 USD | 2026-11-30 | Lazar | mot de Lazar (verbatim, heure relevée) |`

- **Options** : (a) ligne neuve à montant seul, 45 USD (ci-dessus) : avantage, lue sans ambiguïté par le lanceur et la garde ;
  inconvénient, une ligne de plus au registre. (b) ligne neuve en enveloppe (« 45 USD (organisme 45) ») : lue aussi, sans
  gain. (c) laisser les deux GO tels quels : la course ne se lance pas (conditions non tenues).
- **Recommandation** : (a), confiance ≈ 0,85. **Défaut** : aucun (dépense : nœud). Une fois la ligne inscrite, son
  identifiant remplace les trois occurrences de `GO_COURSE_V66` (sections 12.4, 13, 16) par un couple déclaré ;
  `preparer_boucle_reelle_v66.py` n'accepte pas d'autre GO que les deux anciens : remplacement à la main, puis contrôle de la
  forme (motif `GO-\d{4}-\d{2}-\d{2}-\d{2}`).

## 6. Questions pour la mère (avec recommandation)

- **Q-1 (CLV66-03 dans le texte)** : j'ai porté V-5, V-6, V-7 et la partie `lu_sur_disque` de V-4, venues du constat mineur
  CLV66-03 (que la contre-lecture renvoyait à une v67 éventuelle), parce qu'elles sont de la même famille que CLV66-02 (P6
  tenue à vide) et ne coûtent qu'une ligne au verdict. **Recommandation : les garder** (confiance 0,75). Sinon : retirer ces
  cellules des couples B2-26, B2-27, B2-28, sans autre effet.
- **Q-2 (alignements en sections gelées)** : B2-18 (P6 : « vue servie »), B2-19 à B2-23, B2-29 à B2-34 précisent ce que le
  code gelé et contre-lu fait déjà, ou sont demandés par la consigne ; aucun signe, seuil ni chiffre de prédiction ne change.
  **Recommandation : les tenir pour des alignements, non pour des changements de prédiction** (confiance 0,8) ; si la mère y
  voit un changement de prédiction, B2-18 se retire seul (la lecture gelée compare la vue servie quoi qu'il en soit).
- **Q-3 (ordre des préalables)** : j'ai placé la copie de `registres/go.md` (point 5 de la contre-lecture v66, section 6)
  **avant** la commande `--verifier-seulement` (point 4), parce que le lanceur vérifie le GO avant la machine, même en simple
  vérification. **Recommandation : garder cet ordre.**
- **Q-4 (titres de sections et validateur `controle_ia.prereg`)** : les titres numérotés (« ## 8. Critères de lecture
  gelés ») ne passent pas `prereg.problemes` (huit « section absente », brouillons 1 et 2), alors que la consigne fait sceller
  par `controle_ia.scellement`. Un texte scellé de l'organisme du dépôt de travail porte déjà des titres numérotés
  (`prereg/preenregistrement-attaque-goodhart-v3-v4.md`). **Recommandation : ne pas renommer** (les numéros sont cités par le
  code gelé, les contre-lectures et ce texte) ; sceller par `controle_ia.scellement` ; le dire au candidat.
- **Q-5 (plafonds des commandes)** : la configuration v6 (gelée par son empreinte) donne `--plafond-cumule-usd 40` aux deux
  commandes, et non les parts (33 et 7) comme le prévoyait le devis (section 5) ; les parts sont tenues par le compteur de
  l'orchestrateur (garde des parts) et, au brouillon 2, par le plafond de chaque relais (section 12.3, point 6, préalable que
  j'ajoute). **Recommandation : ne pas toucher la configuration ; garder le préalable** (confiance 0,7).
- **Q-6 (contrôle par le lanceur lui-même)** : mon script recopie les règles de forme du lanceur sans importer l'organisme ;
  je n'ai lancé aucun essai de l'organisme (consigne). **Recommandation** : au texte candidat, faire passer le texte réel à
  `lire_preenregistrement` du lanceur (sur la machine, c'est le point 5 de la section 12.3 ; avant, par le contre-lecteur, dans
  son bac à sable, s'il en a la permission).
- **Q-7 (citations de N-064)** : j'ai cité POPPER, Dwork et al., Blum et Hardt et Co-Scientist en section 1, avec les pages
  recopiées de N-064, déclarées non relues (aucun chiffre n'en est tiré). **Recommandation : garder.**

## 7. Écarts à la consigne, dits

- Au-delà du mandat : V-5 à V-7 et `lu_sur_disque` (Q-1) ; ordre des préalables 4 et 5 inversé (Q-3) ; préalable « plafond de
  chaque relais au plus égal à sa part » ajouté (Q-5) ; citations de N-064 (Q-7).
- CLV66-02, lettre de la contre-lecture (« sinon C5 ») : je garde C5 pour les **absences** (V-1, V-2) et lis une **inégalité**
  d'empreintes (V-4) en C4, comme le dit déjà la ligne C4 (« empreinte lue ≠ écrite ») ; les deux interdisent C1.
- Aucun nœud tranché par moi ; aucun seuil, signe ni chiffre de prédiction changé ; le brouillon 1 est intact.

## 8. Ce qui reste (pour la mère)

1. NL-1 et NL-2 à soumettre à Lazar.
2. Q-1 à Q-7.
3. Contre-lecture du brouillon 2 par un sous-agent neuf (fichiers et questions : section 15 du brouillon).
4. Après les décisions : couples de remplissage des deux marqueurs, texte candidat `…-v<N>.md`, scellement, dépôt, copie dans
   `orchestrator/prereg/` de la machine, six préalables, lancement.
