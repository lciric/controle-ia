# Contre-lecture CL1 de la prise « idéation » — orchestrateur du pôle v7, version 31

Contre-lecteur neuf (R2) : Opus 5.5, qui n'a rien écrit de ce qu'il relit (auteur : une instance Fable 5.1).
28 octobre 2026, 15:13 UTC (relevé `date -u`). Aucun appel payant, aucun réseau, aucune clé lue ni affichée ; rien
d'ouvert sous `donnees/` ni dans les zones interdites. Chemins relatifs au dossier relu
`…/envois/pole-scientifique-automatique-v1/` (« `pole/…` » = `orchestrateur-pole-v7/pole/…`).

## Verdict : **non lançable en l'état**

La panne qui a rendu nul le duel des proposeurs (R-599) n'est ni diagnostiquée ni gardée : le code du relais et de la
garde est identique à v30, aucun appel de contrôle de bout en bout n'est fait, et une course dont toutes les sessions
échouent se termine proprement, scellée, avec un classement vide et le code de sortie 0 (CL31-01, démontré). S'y
ajoutent des replis non bloquants (CL31-02) et des défauts de mesure qui interdisent de lire le classement : aucun témoin,
juges des mêmes modèles que les proposeurs sans mesure de l'auto-préférence, juges privés des pièces d'antériorité.

Devient **lançable** après correction de CL31-01, CL31-02, CL31-07, CL31-08 et CL31-10, un appel de contrôle réussi par
modèle à travers relais, kit d'agent et bac à sable, et une relecture ciblée du différentiel. CL31-03 à CL31-05 sont à
corriger avant toute lecture du classement (L2, L4) ; sans eux, la course ne vaut que pour la plomberie (L1) et l'accord
entre juges (L3).

## Ce qui a été vérifié

- **Empreintes** : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v31.txt` → **138 sur 138 conformes**. De v30 à v31,
  changent seulement `pole/adaptateurs.py` (rôles et consignes), `pole/ideation.py`, `demonstrations/ideation_v1.py`,
  `essais/test_v7_ideation.py` et le LISEZMOI ; `pole/relais.py`, `pole/relais_reel.py`, `pole/garde_outils.py`,
  `pole/outils.py` sont identiques à v30.
- **Essais de l'idéation** : **15 sur 15 passent** (Python 3.13.17). La commande demandée
  `-m unittest essais.test_v7_ideation` échoue sous `-I` (« No module named 'essais' » : `-I` retire le dossier courant
  du chemin) ; je les ai lancés par découverte : `-m unittest discover -s essais -t . -p test_v7_ideation.py`. La suite
  complète n'a pas été relancée (consigne).
- **Course simulée** (moteur simulé, sans dépense). La question et les deux pièces de la commande demandée
  (`../question-collisionneur-priorites-sept-questions-v3.md`, `../conception-pole-scientifique-v1.md`,
  `../integration-proposeurs-ia-v1.md`) **n'existent pas dans la copie**. J'ai pris, dans le bloc-notes de la session,
  `collisionneur-priorites/tour/question-priorites-sept-questions-v3.md` et les deux pièces de `depot-lot-fable-v1/`,
  avec `--seconde-passe` et les deux matériaux du devis. Résultat : 7 fiches validées, 0 refusée, 0 en quarantaine,
  2 retenues, 2,80 dollars **simulés**, code 0 ; 22 fichiers scellés, 22 sceaux conformes. Sortie :
  `/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/ideation-simulee-cl1/`.
- **Démonstrations** sur faux moteur et fichiers factices (cibles nommées comme les zones interdites, sans contenu réel),
  dans des dossiers temporaires supprimés après usage ; rien d'écrit dans le dossier relu. Notées (a) à (h) ci-dessous.
- **Barème du relais** confronté à la référence locale de l'interface de programmation Claude : concordant.

## Réponses aux huit points (renvois)

1. **Intégrité.** Gabarit, grille et porte figés dans le code empreinté et dans chaque consigne scellée avant l'appel :
   oui. Manifeste de départ : non (CL31-10). Anonymisation des champs et de l'ordre : oui ; du style : non (CL31-04,
   CL31-17). « Médiane » de deux juges = moyenne (CL31-12). Refus : des replis non bloquants (CL31-02). Scellement des
   sorties : oui, mais moteur, bac à sable et empreintes des pièces non consignés (CL31-10).
2. **Indépendance des juges.** Lecture des fiches signées et de la clé bloquée sur le disque, sous condition que le kit
   honore ses réglages ; auto-préférence non traitée ; aucun juge non Claude possible (CL31-04).
3. **Témoins.** Aucun ; bloquant pour toute lecture du classement (CL31-03).
4. **Garde du niveau méthode.** 11 formes sur 13 passent ; une fiche en quarantaine n'atteint ni juge ni classement par
   le code, mais son texte est archivé et resservi à son auteur en seconde passe (CL31-06).
5. **Pièces interdites.** Liens symboliques, accents et variantes passent ; liste noire sur le chemin seulement (CL31-07).
6. **Coût.** Le plafond total de 20 dollars tient (≈ 5 à 10 attendus) ; celui de 3 par session est menacé pour Fable en
   seconde passe ; au plafond : fiches perdues, brouillon pris, ou repli silencieux sur la passe 1 (CL31-09, CL31-02).
7. **Clé et bac à sable.** Ce que la session qui lance doit monter : fin de CL31-01. Le cas R-599 n'est pas détecté avant
   de dépenser : il produit un résultat vide, propre et scellé (CL31-01) ; `/proc` neuf et utilisateur non root non
   vérifiés par le code (CL31-15).
8. **Autres défauts.** CL31-05, CL31-08, CL31-11 à CL31-18.

## Constats

### CL31-01 — bloquant — La panne du duel (R-599) peut se reproduire à l'identique : ni diagnostic, ni appel de contrôle, ni arrêt

**Preuves.**
- `registres/decisions.md:825` (R-599) : 16 requêtes rejetées par le relais (« Bad request version »), journal vide,
  0 dollar ; « le script a continué […] ce n'est pas un résultat » ; « Relance seulement sur sa correction ». Deux
  défauts y sont nommés : la forme des requêtes des agents vers le relais, et la course qui ne s'arrête pas quand le
  proposeur échoue. La clé avait pourtant passé un appel minimal : un essai direct de la clé ne suffit donc pas.
- v31 ne touche ni `pole/relais.py` ni `pole/relais_reel.py` (empreintes v30 = v31 : `b5a76343…`, `75d8f98a…`). Le
  devis retire seulement `/v1` de l'adresse (`ideation-organisme-approches-v1/devis-ideation-v1.md:61`). Or un mauvais
  chemin donnerait la réponse 404 « chemin non relayé » (`pole/relais_reel.py:211-213`), pas « Bad request version »,
  que la bibliothèque standard renvoie avant tout routage quand la ligne de requête n'est pas conforme (hypothèse :
  poignée de main chiffrée, ou autre protocole, envoyée à un serveur en clair). La cause reste inconnue.
- `pole/relais.py:35` accepte `https` alors que le relais ne sert qu'en clair (`pole/relais_reel.py:328`, aucun
  chiffrement de transport) ; `pole/relais.py:30-41` accepte aussi un chemin (`/v1`).
- `pole/ideation.py:387-391` : une session en erreur devient un refus « aucun bloc JSON {fiches} dans la réponse »
  (motif trompeur : le statut et l'erreur réels ne sont pas recopiés) et la course continue ; `pole/ideation.py:447` :
  juges sautés s'il n'y a aucune fiche ; `demonstrations/ideation_v1.py:141` : code de sortie 0 dans tous les cas.
- **Démonstration (a)** : faux moteur rendant pour les deux proposeurs `statut="erreur"`, texte « API Error: 400 Bad
  request version », coût 0, seconde passe demandée → aucune exception, `arret` vide, classement vide, tous les fichiers
  scellés, code 0. C'est le schéma exact de R-599.
- Ce que v31 détecte avant de dépenser : kit absent (`pole/adaptateurs.py:197-203`), bac à sable inactif
  (`pole/adaptateurs.py:115-131`), noms de variables de clé dans l'environnement (`pole/adaptateurs.py:222-225`), modèle
  non permis, adresse non locale. Ce qu'il ne détecte pas : relais injoignable ; amont injoignable (le relais ouvre une
  connexion directe, sans mandataire, `pole/relais_reel.py:237-238`) ; jeton refusé (401) ; chemin refusé (404) ;
  requête non conforme.

**Correction.**
1. **Appel de contrôle de bout en bout** avant la course, un par modèle (Opus 5.5, Fable 5.1), par le même adaptateur,
   les mêmes options et le même bac à sable : consigne « réponds exactement OK », un tour. Exiger statut `ok`, texte
   `OK`, coût déclaré > 0, et au relais (`GET /relais/etat`, `pole/relais_reel.py:200-202`) un appel de plus et une
   dépense > 0 concordante avec le coût déclaré. Sinon : arrêt, message explicite, code ≠ 0. Coût : quelques centimes.
2. Dans `executer_ideation` : toute session de statut ≠ `ok` ou porteuse d'une erreur arrête la course (voir CL31-02),
   avec le statut et l'erreur réels dans le refus et le manifeste. Le lanceur rend un code ≠ 0 si aucune fiche n'est
   validée ou si le classement est vide.
3. `valider_url_relais` : refuser `https` et tout chemin autre que vide ou `/` ; essais R5 (un cas sain, deux artefacts).
4. Ne relancer qu'après avoir établi, sur l'appel de contrôle, la cause de « Bad request version » (R-599).

**Ce que la session qui lance doit monter** (devis § 3 ; LISEZMOI v12) : clé tournée (R-589) dans un fichier d'une ligne
en mode 600 ; relais lancé sans aucune variable de clé
(`env -i PATH=… HOME=… $PY -I -B -m pole.relais_reel --fichier-cle F --plafond-usd … --port 0 --journal J`), qui lit
puis supprime le fichier et refuse si la variable est aussi présente (`pole/relais_reel.py:305-320, 363-367`) ; contrôle
`demonstrations/verification_cle_proc_v7.py --pid <identifiant du processus du relais>` au « cas sain », versé ;
environnement de l'orchestrateur sans aucun des onze noms de clé (`pole/relais.py:15-18`) ; kit d'agent (Claude Agent
SDK) et outil Claude Code en ligne de commande dans `$PY` ; `bwrap` et `socat` fonctionnels ; agents sous un utilisateur
non root distinct de celui du relais si le bac à sable ne monte pas un `/proc` neuf (non vérifié par le code, CL31-15) ;
adresse `http://127.0.0.1:PORT` sans chemin ; puis l'appel de contrôle ci-dessus.

### CL31-02 — majeur — Replis consignés mais non bloquants : la course rend un classement déséquilibré sans le dire

**Preuves** (démonstrations sur faux moteur).
- **(b)** Un proposeur en erreur en passe 1 est exclu (`pole/ideation.py:389-391`) ; seconde passe et tournoi se font
  sur l'autre modèle seul (classement de 2 fiches, toutes de « fable »).
- **(e)** Seconde passe en échec pour un proposeur (statut `budget_depasse`, texte vide) : ses fiches de passe 1 restent
  et sont jugées avec les fiches de passe 2 de l'autre (`pole/ideation.py:414-418, 425-426`) ; ni fiche ni ligne du
  classement ne porte sa passe.
- **(c)** Un juge sur deux rend une note invalide (2,5) : toutes ses notes sont rejetées (`pole/ideation.py:454-458`) et
  le classement est fait par un seul juge (`nombre_juges = 1`), sans marque « incomplet ». Non couvert par les essais
  (seul le cas d'un juge unique refusé l'est, `orchestrateur-pole-v7/essais/test_v7_ideation.py:266-273`).
- **(f)** Statut `budget_depasse` avec un bloc dans le texte : fiches acceptées comme normales, le statut n'étant jamais
  lu (`pole/ideation.py:383-400`) ; ce bloc peut être le brouillon d'un tour antérieur (texte concaténé de tous les tours,
  dernier bloc pris : `pole/adaptateurs.py:259`, `pole/outils.py:126-129`).
- **(d)** 14 fiches rendues pour `--nombre 8` : 12 acceptées, 2 perdues sans refus ni motif (`pole/ideation.py:393, 420` ;
  `MAX_FICHES_PAR_PROPOSEUR = 12`, `pole/ideation.py:45`), alors que la consigne dit « jamais plus » que 8
  (`pole/ideation.py:228`). Un proposeur prolixe a plus de chances au classement.
- **(h)** `{"fiches": []}` accepté sans refus : `MIN_FICHES_PAR_PROPOSEUR` (`pole/ideation.py:46`) n'est jamais appliqué.

**Correction.** Arrêt de la course à la première session de statut ≠ `ok`, avant toute dépense ultérieure ; classement
seulement si tous les juges ont rendu des notes valides, sinon `classement.json` marqué « incomplet, non lisible » ;
champ `passe` dans chaque fiche et chaque ligne ; au-delà de `nombre`, refus avec motif (pas de troncature) ; liste vide
refusée ; essais R5 pour chacun de ces cas.

### CL31-03 — majeur (bloquant pour toute lecture du classement) — Aucun témoin planté

**Preuves.** Les juges ne voient que les fiches des proposeurs (`pole/ideation.py:439, 450`) ; rien ne permet d'insérer
une fiche de vérité connue (`anonymiser`, `pole/ideation.py:270-282`) ; le devis ne prévoit aucun contrôle de la
verbosité ni de l'assurance (`devis-ideation-v1.md:65-71`). La boucle complète du pôle a des témoins plantés ; cette
prise n'en a pas.

Sans témoins, rien ne distingue ce classement d'un classement par la longueur, l'assurance ou le style (R4). Non bloquant
pour L1 (plomberie) et L3 (accord entre juges) ; bloquant pour L2 et L4 (« cinq premières »), donc pour l'usage annoncé :
servir de matériau à la décision de Lazar.

**Correction** (à sceller avant la course, R1). Trois ou quatre témoins écrits par un tiers (ni proposeur ni juge), au
gabarit et au niveau méthode, insérés avant le mélange, exclus du classement et rapportés à part :
- un **verbeux vide** : champs longs, ton assuré, prédiction non chiffrée ; attendu inéligible, falsifiabilité ≤ 1 ;
- un **assuré occupé** : idée occupée d'après une pièce d'antériorité, marquée « inédite » ; attendu originalité ≤ 1 ;
- un **sobre fort** : court et solide ; attendu éligible ;
- un **jumeau** du sobre fort sous un autre nom ; attendu signalé en doublon.

Critère de lecture gelé (par exemple : les deux premiers inéligibles chez chaque juge, le troisième éligible) ; s'il
échoue, L2 et L4 ne se lisent pas. Ajouter une lecture gelée : corrélation de rang entre longueur de la fiche et total.

### CL31-04 — majeur — Juges des mêmes modèles que les proposeurs : auto-préférence non mesurée, porte franchissable par un seul juge, aucun juge non Claude possible

**Preuves.**
- **Le disque** : la clé (`noyau/cle-anonymisation.json`) et les fiches signées sont sous la sortie, interdite en lecture
  au bac à sable (`demonstrations/ideation_v1.py:124` → `pole/adaptateurs.py:162, 189`) ; l'outil de lecture est borné
  au dossier de l'agent, liens résolus (`pole/garde_outils.py:288-299`, `pole/outils.py:140-145`) ; la consigne du juge
  ne contient aucun auteur (`essais/test_v7_ideation.py:224-227`). Si le kit honore ces réglages (non vérifiable ici),
  un juge ne lit ni les fiches signées ni la clé.
- **Le style** : rien ne le neutralise ; Opus juge des fiches d'Opus et Fable des fiches de Fable
  (`devis-ideation-v1.md:30-33`) ; le manifeste se contente de le consigner (`pole/ideation.py:473`). La docstring promet
  l'inverse : juges « un autre modèle que le proposeur dont ils lisent la fiche » (`pole/ideation.py:10`).
- **Démonstration (g)** : avec deux juges, la porte se franchit sur la note d'un seul ; originalité (3, 1) → 2,0 →
  éligible (`pole/ideation.py:327-329`). Un juge qui préfère son propre modèle suffit à rendre éligibles les fiches de ce
  modèle.
- **Juge non Claude** : impossible dans ce code. Modèles limités à Opus 5.5 et Fable 5.1 (`pole/adaptateurs.py:21,
  134-138` ; contrôle appliqué aux juges, `demonstrations/ideation_v1.py:122-123`) ; relais limité à `/v1/messages` de
  l'amont Anthropic (`pole/relais_reel.py:54, 347`) ; adaptateur réel fondé sur le kit Claude. N-053 point 4
  (`docs/decisions/decision-N-053-v1.md:33-37`) vise le juge des moniteurs (Qwen2.5-7B en bras rapporté), pas
  explicitement ce tournoi : l'étendre ici relève de Lazar (lecture du programme), et un juge local à poids ouverts
  serait une dépense de calcul (nœud).

**Correction.** Ajouter au devis, avant la course, des lectures gelées : écart de chaque juge entre ses notes aux fiches
de son propre modèle et à celles de l'autre, et différence entre les deux juges ; classements par juge rapportés à côté
du classement agrégé ; variante de porte « à l'unanimité » rapportée. Proposer à Lazar, avec recommandation, un juge
d'une autre lignée en bras rapporté. Mesure bon marché en complément : normaliser la typographie (guillemets, tirets,
espaces) avant de servir les fiches.

### CL31-05 — majeur — Les juges notent l'originalité « d'après les pièces » sans avoir les pièces

**Preuves.** Grille : « 0 : occupé d'après les pièces ou ce que tu sais » (`pole/ideation.py:238-239`). Les juges ne
reçoivent que `pieces_juge` (`pole/ideation.py:450`), vide par défaut (`demonstrations/ideation_v1.py:90`) et absent de
la commande du devis (`devis-ideation-v1.md:54-61`). Les proposeurs, eux, ont lu les rapports d'antériorité et peuvent
marquer « RAPPORTE » ce que le juge ne peut pas contrôler. Or l'originalité est la moitié de la porte.

**Correction.** Servir aux juges, par `--piece-juge`, les rapports d'antériorité (pièces B à D) ou un résumé scellé ;
sinon retirer « d'après les pièces » de la grille et le dire dans la lecture. Surcoût estimé pour ≈ 40 000 jetons :
≈ 0,2 dollar (juge Opus), ≈ 0,5 (juge Fable).

### CL31-06 — majeur — Garde lexicale très perméable ; la quarantaine protège le juge, pas l'archive

**Preuves.**
- Quatre motifs (`pole/ideation.py:53-58`). Essai sur des phrases de forme neutre : seuls « Étape 1 : » et le mot exact
  « exploit » sont signalés ; passent « Étape 1. », « Première étape — », « 1) … 2) … », « Phase 1 : », « afin de
  contourner le moniteur », « pour échapper au moniteur », « pour déjouer la surveillance », « pour tromper ce
  détecteur », « injection de consigne », « prompt injection », « exploiter ». Une fiche qui détaille une attaque sans
  ces mots passe, est jugée et classée.
- Par le code, une fiche en quarantaine n'atteint ni juge ni classement (`pole/ideation.py:427-442` ; essai
  `essais/test_v7_ideation.py:203-218`). Mais son texte est scellé dans la réponse brute (`pole/ideation.py:375`) et, en
  seconde passe, resservi à son auteur avant tout tri (`pole/ideation.py:409-411` ; la garde ne passe qu'après les deux
  passes, `pole/ideation.py:427`), qui peut la reformuler sous le seuil lexical. Le devis prévoit le versement de toute la
  sortie et une lecture humaine **de la quarantaine seulement** (`devis-ideation-v1.md:63`).

**Correction.** Élargir les motifs, en gardant leur statut de signal : suites numérotées, « première étape », « phase
n », « pour | afin de » suivi de « contourner | échapper | déjouer | leurrer | tromper | éviter » et de « moniteur |
surveillance | détecteur | sonde | juge », « injection », « exfiltr », « stéganograph », « porte dérobée », « exploiter ».
Appliquer la garde aussi aux réponses brutes et aux fiches de passe 1 avant de les resservir. Lecture humaine de
**toutes** les fiches validées avant tout versement ou envoi. Vérifier que `scripts/depot_expurge.py` exclut
`traces-*` et `fiches-en-quarantaine.json`. Essais R5 avec des paraphrases.

### CL31-07 — majeur — `verifier_pieces` se contourne : liens symboliques, accents, variantes ; liste noire sur le chemin seulement

**Preuves.** `pole/ideation.py:72-84` normalise par `abspath` et `normpath` sans résoudre les liens ; `os.path.isfile`
suit le lien ; aucun contrôle du contenu. Essai sur fichiers factices :
- **passent** : lien symbolique de fichier vers `donnees/`, lien de dossier vers `donnees/`, `données/` (formes composée
  et décomposée), `mode_tenu_a_l_ecart/`, `mode-tenu-à-l-écart/`, `bras_attaque/`, `bras-d-attaque/`, `banques/`,
  `banque_v3.json`, `carte-hypotheses-v1.md`, `prereg/P3-consignes-v1.md` ;
- **refusés** : seulement `DONNEES/` (majuscules) et `x/../donnees/` (chemin relatif remontant).

`lire_pieces` lit effectivement la cible du lien. Le fichier de la question n'est jamais contrôlé
(`demonstrations/ideation_v1.py:112-113`).

**Correction.** Liste blanche par empreinte : le devis fixe la liste exacte des pièces, de la question et du matériau,
avec leur SHA-256, scellée ; le noyau refuse tout fichier hors liste. En complément : `realpath` et refus de tout lien
sur le chemin ; normalisation Unicode (décomposition, accents retirés, `_` et espaces ramenés à `-`) avant comparaison ;
fragments élargis ; contrôle de la question ; essais R5 pour chacun des cas ci-dessus.

### CL31-08 — majeur — Les lectures des agents ne sont pas bornées à leur dossier ; outils et tours inutiles pour ces rôles

**Preuves.** Le lanceur n'interdit en lecture que la sortie (`demonstrations/ideation_v1.py:124` ;
`pole/adaptateurs.py:162, 189`). Le reste de la machine (dépôt, dossier personnel) reste lisible par les commandes du
terminal dans le bac à sable, et la garde par motifs se traverse avec un chemin construit à l'exécution, de l'aveu même
du code (`pole/garde_outils.py:3-6` ; `pole/adaptateurs.py:157-158` ; dans du code, `pole/garde_outils.py:198-201` ne
voit un chemin que si son premier composant existe littéralement). Le LISEZMOI et le lanceur affirment l'inverse
(« lectures bornées au dossier de chaque agent », `orchestrateur-pole-v7/LISEZMOI-orchestrateur-pole-v7-v31.md:17`,
`demonstrations/ideation_v1.py:8-9`).

Or ces deux rôles n'ont besoin d'aucun outil : tout est dans la consigne (`pole/ideation.py:211-232, 248-264`). Avec
lecture, écriture, édition et terminal permis (`pole/adaptateurs.py:23`) et six tours, un agent peut aussi écrire ses
fiches dans un fichier et ne rendre qu'un renvoi : le noyau ne lit que le texte final (`pole/ideation.py:388`) et ignore
les fichiers listés (`pole/adaptateurs.py:241`). Chaque tour de plus coûte (CL31-09).

**Correction.** Pour `proposeur_ideation` et `juge_ideation` : aucun outil (ni terminal, ni écriture, ni édition ;
lecture au plus dans le dossier vide), un ou deux tours ; interdire aussi en lecture la racine du dépôt et le dossier
personnel ; vérifier sur l'appel de contrôle (CL31-01) qu'aucun outil n'est utilisable ; corriger le LISEZMOI.

### CL31-09 — majeur — Coût : 20 dollars tiennent, 3 dollars par session non ; le devis est trop bas d'un facteur 2 à 3

**Barème** du relais (`pole/relais_reel.py:44-50`, concordant avec la référence locale), en dollars par million de
jetons :

| modèle | entrée | sortie | écriture de cache | lecture de cache |
|---|---|---|---|---|
| Opus 5.5 | 4 | 20 | 5 | 0,20 |
| Fable 5.1 | 10 | 50 | 12,5 | 0,25 |

**Hypothèses.**
- Entrée : 63 000 jetons en passe 1 (60 000 du devis, plus consigne système et définitions d'outils, estimées) ; 85 000
  en passe 2 (mesuré sur la course simulée : la consigne de passe 2 a ≈ 56 000 caractères de plus avec des fiches
  simulées courtes, ≈ 80 000 avec huit vraies fiches) ; 25 000 pour un juge.
- Sortie, réflexion comprise (toujours active sur ces deux modèles et facturée comme sortie) : 10 000 à 40 000 jetons
  par proposeur, 10 000 à 25 000 par juge. Le devis en suppose 6 000 (`devis-ideation-v1.md:39-42`).

| session (un tour, cache écrit une fois) | entrée | sortie | total |
|---|---|---|---|
| Opus, passe 1 | 0,32 | 0,20 à 0,80 | 0,52 à 1,12 |
| Opus, passe 2 | 0,43 | 0,20 à 0,80 | 0,63 à 1,23 |
| Fable, passe 1 | 0,79 | 0,50 à 2,00 | 1,29 à 2,79 |
| Fable, passe 2 | 1,06 | 0,50 à 2,00 | 1,56 à 3,06 |
| juge Opus | 0,13 | 0,20 à 0,50 | 0,33 à 0,63 |
| juge Fable | 0,31 | 0,50 à 1,25 | 0,81 à 1,56 |
| **course entière** | | | **≈ 5,1 à 10,4** |

**Ré-envoi de l'entrée à chaque tour.** Avec le cache vivant, chaque tour de plus ajoute ≈ 0,01 à 0,02 dollar de
lecture de cache : négligeable. Si le cache a expiré entre deux tours (plus de cinq minutes, plausible avec une longue
réflexion de Fable) : + 0,79 à 1,06 dollar par expiration pour Fable. Sans cache, six tours de Fable en passe 2
coûteraient ≈ 5,10 dollars d'entrée, et le plafond de 3 couperait la session vers le troisième tour.

**Conséquences.**
- Le plafond total de 20 tient (≈ 5 à 10 attendus). L'ordre de grandeur du LISEZMOI (« moins de 10 ») est le bon ; les
  « ≈ 3 USD attendus » du devis ignorent la réflexion et l'écriture du cache.
- Le plafond de 3 par session est atteignable par Fable en passe 2, et en passe 1 au haut de la fourchette. Un plafond
  vérifié entre deux tours (comportement habituel du kit, non vérifiable ici) ne coupe pas un tour unique coûteux ; une
  session de plusieurs tours est arrêtée en `budget_depasse` (`pole/adaptateurs.py:246`). Alors : fiches perdues si le
  bloc n'était pas encore écrit (refus, `pole/ideation.py:389-391`), brouillon pris (CL31-02 (f)), ou reprise silencieuse
  de la passe 1 (CL31-02 (e)) ; l'argent est dépensé.
- Le relais réserve 0,40 dollar par appel (`pole/relais_reel.py:129`) contre jusqu'à ≈ 3 pour un appel de Fable : son
  plafond peut être dépassé d'≈ 2,7 dollars (appels séquentiels, dernier appel admis).
- Le noyau compte le coût déclaré par le kit (`pole/ideation.py:372`, `pole/adaptateurs.py:252`), nul en cas d'exception
  (`pole/adaptateurs.py:245, 257-258`) et calculé par l'outil en ligne de commande avec sa propre table de prix (non
  vérifiable ici) ; un même `--budget-session-usd` vaut pour tous les rôles et tous les modèles.

**Correction.** Aucun outil et un ou deux tours (CL31-08) ; effort de réflexion fixé et consigné ; plafond par rôle et
par modèle (par exemple 5 pour Fable en passe 2, le total restant 20) ; `--reserve-par-appel 3,5` au relais (sans coût,
les appels étant séquentiels) ou plafond du relais à 17 ; après chaque session, lire `GET /relais/etat` et compter le
maximum du coût déclaré et de l'écart lu au relais ; refaire le devis avec la réflexion et l'écriture du cache.

### CL31-10 — majeur — Manifeste incomplet et écrit en fin de course

**Preuves.** Clés du manifeste (course simulée et démonstration (a)) : budgets, critères, comptes de fiches, graine,
horodatage, journal, juges, modèles communs, matériau (noms), `max_tours`, nombre, note maximale, pièces (noms), porte,
proposeurs, seconde passe (`pole/ideation.py:469-477`). Manquent :
- le **moteur**, simulé ou réel. Le lanceur choisit `simule` par défaut (`demonstrations/ideation_v1.py:100`) et ses
  coûts fictifs (2,80 dollars ici) entrent dans le journal comme des coûts réels ;
- l'**état du bac à sable**, calculé (`demonstrations/ideation_v1.py:125-126`) mais jamais transmis, alors que
  `pole/adaptateurs.py:116` le dit « consigné au manifeste » ;
- l'adresse et l'état du relais, les versions du kit et de l'outil en ligne de commande ;
- le **nom et l'empreinte de la question**, les **empreintes des pièces et du matériau** (noms seuls,
  `pole/ideation.py:470-471` ; R6).

Le manifeste n'est écrit qu'à la fin (`pole/ideation.py:469`) et l'empreinte du code est calculée sur le disque à ce
moment (`pole/outils.py:161-162`) : une exception en cours de course ne laisse aucun manifeste. Les fichiers écrits par
les agents dans leur dossier ne sont ni listés au journal ni scellés (`pole/ideation.py:373-374`).

**Correction.** Un « manifeste de départ » scellé avant le premier appel (empreintes du code, de la question, de chaque
pièce et du matériau ; réglages, porte, grille, moteur, bac à sable, relais, versions), puis le manifeste de fin ; coûts
simulés marqués fictifs et non comptés ; fichiers des agents listés et scellés.

### CL31-11 — mineur — Les juges connaissent la porte d'éligibilité

**Preuve.** `pole/ideation.py:257-258` : « max(avantage, originalite) ≥ 2 ; le noyau l'applique, pas toi » (lignes
128-129 de la consigne simulée du juge). Un juge qui voit le seuil peut, même sans intention, porter à 2 l'avantage ou
l'originalité d'une fiche qu'il apprécie.

**Correction.** Retirer la porte de la consigne des juges ; elle reste fixée dans le code et le manifeste.

### CL31-12 — mineur — Agrégation : « médiane » de deux juges = moyenne ; même ordre pour les deux juges ; départage final tiré au sort

**Preuves.** `statistics.median` sur deux valeurs rend leur moyenne (`pole/ideation.py:327` ; totaux 8,5 et 5,5 dans la
course simulée). Une seule permutation pour tous les juges (`pole/ideation.py:439, 450`) : les consignes des deux juges
sont identiques après « ## Les fiches » (vérifié), donc l'effet de position est le même chez les deux. Dernier critère
de départage : l'étiquette Tnn tirée (`pole/ideation.py:332-333`).

**Correction.** Appeler l'agrégat par son nom (moyenne) ou passer à trois juges ; une permutation et un étiquetage par
juge (graine dérivée par juge), remis en correspondance par le noyau ; départage final documenté.

### CL31-13 — mineur (conception) — Seconde passe : le verdict d'un juge du même modèle est servi aux proposeurs, et la passe 2 remplace la passe 1

**Preuves.** Le matériau du devis comprend `tournoi-juge.md` (`devis-ideation-v1.md:59`), verdict d'un juge Opus 5.5 sur
la même grille (`preideation-interne-v1/tournoi-juge.md`, en-tête) ; le juge officiel « juge-opus » est du même modèle.
La passe 2 remplace la passe 1 (`pole/ideation.py:425-426`) : l'effet du matériau n'est pas mesurable, le risque de
conformité au goût d'un juge Opus est réel, et L4 (recoupement avec le tour interne) en est biaisée.

**Correction.** Juger ensemble, anonymes et mêlées, les fiches de passe 1 et de passe 2, passe consignée ; ou ne servir
que `fiches-anonymes.md`.

### CL31-14 — mineur — Les sections déclarées par la question ne sont pas servies telles quelles

**Preuves.** La question demande « section A seulement », « sections 1 à 3 de chacun », « section “Notre marque” »
(lignes 42-48 de la consigne simulée ; `devis-ideation-v1.md:13-16`) ; `lire_pieces` sert le fichier entier
(`pole/ideation.py:87-97`). D'où plus de jetons que prévu et un contenu qui dépasse l'intention.

**Correction.** Extraire les sections dans des fichiers nouveaux, versionnés et scellés (R12), et servir ceux-là (liste
blanche, CL31-07).

### CL31-15 — mineur — Bac à sable : la sonde n'essaie pas un `/proc` neuf ; l'utilisateur non root n'est pas exigé quand la sonde passe

**Preuves.** `etat_bac_a_sable` essaie `bwrap --ro-bind / / --dev /dev --unshare-net true` (`pole/adaptateurs.py:105`),
sans espace de processus propre ni `--proc /proc` ; `euid ≠ 0` n'est exigé qu'en cas d'acceptation sans bac à sable
(`pole/adaptateurs.py:128-130`). La condition du devis, « bac à sable qui monte un `/proc` neuf, agents sous un
utilisateur non root » (`devis-ideation-v1.md:49-50`), n'est gardée que par l'opérateur ; en (a) et (a) bis, relais et
agents tournaient sous root (R-589).

**Correction.** Sonde avec `--unshare-pid --proc /proc` ; si elle échoue, exiger un utilisateur non root distinct de
celui du relais ; consigner le résultat au manifeste (CL31-10). Avec CL31-08 (aucun outil), le risque résiduel devient
faible.

### CL31-16 — mineur — Affirmations fausses ou confuses dans le code et le LISEZMOI

**Preuves.**
- `pole/ideation.py:10` : juges « un autre modèle que le proposeur dont ils lisent la fiche » (faux, CL31-04) ;
- `pole/ideation.py:354-356` : docstring en forme de question-réponse ;
- `demonstrations/ideation_v1.py:8-9` et `LISEZMOI-orchestrateur-pole-v7-v31.md:17` : « lectures bornées au dossier de
  chaque agent » (faux, CL31-08) ;
- `pole/adaptateurs.py:116` : état du bac à sable « consigné au manifeste » (faux pour l'idéation, CL31-10) ;
- `LISEZMOI-orchestrateur-pole-v7-v31.md:13` : juges « aveugles aux auteurs » (vrai pour les champs, pas pour le style).

**Correction.** Réécrire ces passages pour dire ce que fait le code.

### CL31-17 — mineur — Hygiène de l'anonymisation et des étiquettes

**Preuves.**
- Clé d'anonymisation écrite avant le passage des juges (`pole/ideation.py:439-442`).
- Champ `empreinte` servi aux juges (7 occurrences dans la consigne simulée), inutile pour eux.
- Aucune normalisation typographique.
- Étiquettes des proposeurs et des juges non contrôlées (`demonstrations/ideation_v1.py:77-82, 108-111` ;
  `pole/ideation.py:382, 449`) : une étiquette en double donne le même dossier, puis `EcrasementInterdit` en cours de
  course, après dépense ; une étiquette avec `..` sort de la sortie en moteur simulé.

**Correction.** Écrire la clé après les juges ; retirer `empreinte` des fiches servies ; normaliser la typographie ;
valider les étiquettes au départ (`^[a-z0-9-]+$`, uniques).

### CL31-18 — mineur — Essais manquants

**Preuves.** Aucun essai des rôles `proposeur_ideation` et `juge_ideation` dans `construire_options` (aucune mention hors
`essais/test_v7_ideation.py`) ; aucun essai de session en échec, de juge invalide parmi deux, de passe 2 en échec, de
fiches en trop, de liste vide, de lien symbolique, de variantes de chemin ni de paraphrase devant la garde ; la commande
nommée `-m unittest essais.test_v7_ideation` échoue sous `-I`.

**Correction.** Ajouter ces cas (un cas sain et un artefact chacun, R5) ; documenter la commande par découverte.

## Ce que je n'ai pas pu vérifier

- **Le comportement réel du kit d'agent** : `claude_agent_sdk` n'est installé dans aucun environnement Python disponible
  ici, et `$PY=/opt/venv-essaim-sim-v1/bin/python` est absent. Donc non vérifié : que `ClaudeAgentOptions` accepte
  `verbatim_prompts`, `sandbox` sous cette forme, `failIfUnavailable`, `filesystem.denyRead` et `allowRead` ; que ces
  interdictions s'appliquent aux commandes du terminal ; que le bac à sable monte un `/proc` neuf ; comment et quand
  `max_budget_usd` et `max_turns` coupent ; si l'outil en ligne de commande connaît les prix d'Opus 5.5 et de Fable 5.1
  (sinon coût déclaré faux) ; si le cache fonctionne à travers le relais.
- **La cause de « Bad request version »** (R-599) : non établie. Dans ce conteneur, les variables de mandataire réseau
  excluent bien 127.0.0.1, ce qui ne dit rien de l'environnement de session-depot.
- **La taille réelle des pièces** (60 000 jetons) : six des huit pièces nommées et la question citée sont absentes de la
  copie ; l'estimation de coût repose sur l'hypothèse du devis.
- **Le contenu des pièces**, que je n'ai pas lues : en particulier, si les fichiers entiers (CL31-14) contiennent plus
  que le niveau méthode.
- **Le script d'expurgation** du dépôt public (`scripts/depot_expurge.py`) : non lu.
- **La suite complète des 294 essais** : non relancée (consigne) ; seuls les 15 de l'idéation l'ont été.

Fichiers produits : ce rapport, et la sortie de la course simulée demandée
(`/tmp/claude-0/-home-user-controle-ia-travail/75a1275d-b838-5015-909e-b2bfadb395f9/scratchpad/ideation-simulee-cl1/`).
Les dossiers temporaires des démonstrations ont été supprimés.
