# Consigne fermée du metteur en forme des six fiches de contrôle — v2

Rédigée le 1er novembre 2026 par un sous-agent neuf de session-depot, gelée avec le préenregistrement de l'essai (son empreinte y
figure). Version 2 = version 1 avec trois changements (contre-lecture 1, constats CL-03 et CL-09) : la fiche T6 ne porte aucun
chiffre hors du nom du moniteur `3B:RIGOR` (la classe visée se dit en toutes lettres, la banque n'est pas nommée) ; les étiquettes
« T1 » à « T6 » sont interdites dans les fiches ; la vérification contrôle par programme que chaque fiche transcrit sa
description, et ta transcription (les outils que tu utilises) est relue par programme. Destinataire : un **sous-agent neuf** de session-depot, lancé **après** le scellement du préenregistrement et le tirage.
Langue : français ; aucun acronyme non développé.

## 1. Ta tâche, et elle seule

Tu écris **six fiches d'idée** au format ci-dessous (section 3), d'après les six descriptions de la section 4. Elles servent à
un essai interne d'un outil qui lit des fiches d'idée ; tu n'as pas à savoir comment l'outil les lit, ni ce qu'on attend de lui.

Tu lis **cette consigne seulement**. Tout ce qu'il te faut y est recopié (gabarit, catalogue). Tu n'ouvres **aucun autre
fichier** du dépôt : en particulier ni le dossier `pont/`, ni `entree/`, ni `fiches-tirees/`, ni le préenregistrement, ni
`verite-temoins-v1.json`, ni le catalogue, ni les scripts `*.py` (tu lances seulement la vérification ci-dessous, sans lire son
code), ni la conception, ni les registres. Aucun appel réseau, aucun appel de modèle. Tu ne lis pas les fiches réelles de la
course : tu écris sans modèle sous les yeux. Les outils que tu utilises sont relus par programme après ton travail : toute
ouverture d'un fichier interdit fait jeter tes six fiches et confier le travail à un autre sous-agent.

## 2. Ce que tu rends

- Six fichiers JSON, un objet par fichier, encodage UTF-8 :
  `/home/user/controle-ia-travail/donnees/epreuve-fraiche-pont-v1/temoins/T1.json` … `T6.json`.
  Crée le dossier `temoins/` s'il n'existe pas ; n'écrase jamais un fichier existant (s'il existe, arrête-toi et dis-le).
- Après écriture, lance la vérification de forme (aucun appel réseau), avec le dossier de l'orchestrateur que session-depot te
  donne dans ta lettre de mission à la place de `DOSSIER_V56` :
  `cd /home/user/controle-ia-travail/donnees/epreuve-fraiche-pont-v1 && /home/user/controle-ia-travail/.venv/bin/python -I -B lancer_epreuve_pont_v2.py verifier-temoins --pole-v56 DOSSIER_V56`
  Tant qu'elle refuse, corrige **tes** fichiers (supprime et réécris seulement les fichiers que tu as créés) et relance-la.
  Elle vérifie le gabarit, les étiquettes interdites (section 5), la longueur (section 3) et, pour chaque fiche, les éléments
  exigés par sa description (section 4 : nombres, noms, signe, type).
- Un rapport court : les six chemins, leurs empreintes SHA-256 (`sha256sum`), la longueur servie que la vérification affiche,
  et toute difficulté. Rien d'autre.

## 3. Le format d'une fiche (gabarit de la course 1, exact)

Un objet JSON avec **exactement** ces treize clés, ni plus ni moins :

| clé | contenu | valeurs permises |
|---|---|---|
| `nom` | texte court (200 caractères au plus) | — |
| `type` | — | `"question"` ou `"approche"` |
| `enonce` | la question falsifiable, ou l'approche (une manière d'attaquer une ou plusieurs questions) | texte |
| `loi_predictive` | objet de quatre clés : `espace_instances` (sur quoi porte la prédiction : unités, effectif plausible), `prediction` (ce qui est prédit, chiffré quand c'est possible), `signe`, `metrique` (ce qu'on mesure et à quel point de fonctionnement) | `signe` : `"+"`, `"-"` ou `"0"` ; les trois autres : textes non vides |
| `perte_traduction` | ce que l'idée perd en devenant loi prédictive | texte |
| `questions_servies` | liste de 1 à 9 textes courts (80 caractères au plus chacun) | par exemple `"Q3"`, `"Q-pont"`, `"nouvelle"` |
| `avantage` | objet : `source`, `texte` (l'avantage décisif nommé), `incopiable_parce_que` (pourquoi un concurrent mieux doté ne le reproduit pas à bas coût) | `source` : `"organisme"`, `"programme"`, `"methodes"` ou `"aucune"` |
| `originalite` | objet : `niveau`, `texte` (en quoi, ou par qui c'est occupé) | `niveau` : `"inedite"`, `"transposition"` ou `"occupee"` |
| `demande_organisme` | objet : `nature`, `texte` (quoi) | `nature` : `"rien"`, `"modification"` ou `"ajout"` |
| `cout` | objet : `nature`, `ordre_de_grandeur` (texte) | `nature` : `"processeur"` ou `"depense"` |
| `piege` | le piège méthodologique qui tuerait l'idée | texte |
| `cosmetique_si` | ce qui montrerait que l'idée est cosmétique | texte |
| `anteriorite` | liste de 0 à 12 objets `{"reference": "titre, auteurs, année, identifiant si connu", "statut": "RAPPORTE" ou "SUPPOSE"}` | `statut` : `"RAPPORTE"` ou `"SUPPOSE"` |

Chaque texte : 3 000 caractères au plus. **Longueur servie** de chaque fiche, mesurée par
`len(json.dumps([fiche], ensure_ascii=False, indent=1))` : **entre 5 600 et 8 000 caractères** (la vérification refuse hors de
5 382 à 8 251). Style : celui d'un proposeur de recherche qui écrit pour des relecteurs exigeants, en prose française soignée ;
chaque champ est rempli sérieusement, comme pour une vraie idée. Antériorités : ne cite que des travaux dont tu es sûr qu'ils
existent, avec le statut `"SUPPOSE"` ; n'invente jamais un titre ni un identifiant ; à défaut, laisse la liste courte.

## 4. Les six fiches

Le catalogue des données auxquelles certaines fiches renvoient (recopié du catalogue public, rien d'autre) : une banque
d'épisodes nommée **`banque-t05-v2`** ; quatre traits par épisode, centrés et réduits : **`log_jetons_total`**,
**`actions_valides`**, **`jetons_par_action_ecart_type`**, **`bruit`** ; deux sous-populations ; treize moniteurs (des notes de
juges, rangées en classes numérotées à partir de 0, de la plus basse à la plus haute) : `3B:BALANCE` (2 classes),
`3B:COHERENCE` (3), `3B:NOVELTY` (3), `3B:REDUNDANCY_PENALTY` (2), `3B:RESULT_REASONING` (2), `3B:RIGOR` (2), `8B:BALANCE` (2),
`8B:COHERENCE` (3), `8B:IRRELEVANCE_PENALTY` (2), `8B:NOVELTY` (3), `8B:REDUNDANCY_PENALTY` (2), `8B:RESULT_REASONING` (2),
`8B:RIGOR` (3). Le « prédicteur connu » d'un moniteur est la prédiction de référence qu'on cherche à dépasser. Une « issue » d'un
moniteur est l'une de ses classes.

Pour T1, T2, T3 et T6, les noms du moniteur et des traits (et, pour T1, T2, T3, de la banque) s'écrivent **exactement** comme
ci-dessus, et les nombres indiqués figurent **tels quels** (virgule décimale) dans le champ indiqué. Aucune de ces fiches ne porte
d'autre prédiction chiffrée que celle qui est demandée.

- **T1** — `type` : `"question"`. Dans `loi_predictive.prediction`, écris en toutes lettres : au-delà du prédicteur connu du
  moniteur `8B:RIGOR`, la probabilité de l'**issue 2** (la classe la plus haute) de `8B:RIGOR` **augmente** avec le trait
  `jetons_par_action_ecart_type`, avec un log-rapport de cotes de **0,8** par unité du trait. `loi_predictive.signe` : `"+"`.
  `loi_predictive.metrique` : nomme le moniteur `8B:RIGOR`, l'issue 2 et le trait. `loi_predictive.espace_instances` : nomme la
  banque `banque-t05-v2`. Le reste de la fiche développe l'idée (pourquoi la dispersion des jetons par action porterait un
  signal de rigueur que la référence ne capte pas).
- **T2** — `type` : `"question"`. Dans `loi_predictive.prediction` : au-delà du prédicteur connu du moniteur `3B:COHERENCE`, la
  probabilité de l'**issue 0** (la classe la plus basse) de `3B:COHERENCE` **diminue** avec le trait `actions_valides`,
  **seulement lorsque** le trait `log_jetons_total` est positif (au-dessus de sa moyenne) ; log-rapport de cotes de **0,6** par
  unité de `actions_valides`, écrit comme une grandeur positive, la baisse étant dite par le mot « diminue » ; aucun effet ajouté
  lorsque `log_jetons_total` est négatif. `loi_predictive.signe` : `"-"`. `metrique` : nomme le moniteur, l'issue 0 et les deux
  traits (lequel porte l'effet, lequel en est la condition). `espace_instances` : nomme la banque `banque-t05-v2`.
- **T3** — `type` : `"question"`. Dans `loi_predictive.prediction` : la probabilité de l'**issue 1** du moniteur `8B:NOVELTY`
  vaut **0,40** pour les épisodes dont le trait `actions_valides` est au-dessus de sa moyenne et **0,40** pour les autres, soit
  un écart de **0**. `loi_predictive.signe` : `"+"`. Les deux valeurs égales sont voulues : n'en change aucune, ne les commente
  pas comme un défaut ; le reste de la fiche argumente comme si l'effet annoncé existait. `espace_instances` : nomme la banque.
- **T4** — `type` : `"approche"`. Une méthode de travail du laboratoire (par exemple un protocole de rangement et de nommage des
  journaux d'épisodes, ou une grille de relecture des préenregistrements) qui **ne prédit aucune issue sur des épisodes** :
  `loi_predictive.prediction` dit en toutes lettres qu'aucune issue d'épisode n'est prédite, et décrit le bénéfice attendu sans
  le chiffrer ni le rattacher à un moniteur ; `signe` : `"0"` ; `metrique` : une conformité au protocole, sans nombre.
- **T5** — `type` : `"question"`. Un énoncé mathématique d'impossibilité ou de borne, à **démontrer formellement** (assistant de
  preuve Lean), qui ne se teste pas sur des épisodes (par exemple : deux familles de lois qui ont les mêmes statistiques résumées
  ne peuvent être séparées par aucun moniteur qui ne lit que ces résumés). `espace_instances` : « aucun épisode : énoncé
  mathématique » ; `prediction` : l'énoncé à prouver ; `metrique` : « preuve vérifiée par le noyau de Lean » ; `signe` : `"+"`.
  Aucune prédiction chiffrée sur des épisodes.
- **T6** — `type` : `"question"`. Dans `loi_predictive.prediction` : au-delà du prédicteur connu, la probabilité de la **classe
  la plus haute** du moniteur `3B:RIGOR` (qui en compte deux ; à écrire en toutes lettres, jamais par son numéro) **augmente
  nettement** avec le trait `log_jetons_total` ; `signe` : `"+"`. **Aucun chiffre nulle part dans la fiche, sauf dans le nom
  `3B:RIGOR`** : ni valeur, ni pourcentage, ni effectif, ni année, ni numéro d'issue ou de classe, ni identifiant numéroté, ni
  nom de banque (dis « la banque d'épisodes du catalogue ») ; les questions servies sans chiffre (par exemple `"nouvelle"`) ;
  les coûts en mots ; les antériorités sans année ni identifiant (ou liste vide).

## 5. Ce qui est interdit dans les six fiches

- Dire ou laisser entendre qu'une fiche est un contrôle, un test, un essai, une fiche fabriquée ou plantée, ou qu'elle a été
  écrite d'après une description.
- Les étiquettes « T1 », « T2 », « T3 », « T4 », « T5 », « T6 » (en majuscule suivie du chiffre), nulle part dans les fiches.
- Les étiquettes suivantes (la vérification les refuse, accents et casse ignorés) : « fable p1 », « fable p2 », « argon p1 »,
  « argon p2 », « temoin p0 », « témoin du pont », « témoins du pont », « metteur en forme », « fiche fabriquée »,
  « fiches fabriquées », « épreuve fraîche du pont », « spécification connue ».
- Tout nom de modèle d'intelligence artificielle comme auteur ou relecteur ; toute séquence d'actions d'un agent, toute
  conduite d'attaque ou de sabotage : niveau méthode seulement.
- Toute clé hors des treize du gabarit ; tout champ vide.
