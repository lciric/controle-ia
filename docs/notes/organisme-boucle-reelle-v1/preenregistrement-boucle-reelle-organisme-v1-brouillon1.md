# Préenregistrement — la plus petite course réelle de la boucle complète de l'organisme d'idéation, brouillon 1

**Statut : brouillon 1, non contre-lu, non scellé. Aucune course réelle avant : (i) le code v65 des pièces manquantes
(section 12), ses essais et son banc de mutations ; (ii) la contre-lecture par un sous-agent neuf (règle R2) ; (iii) le
scellement ; (iv) un feu vert de dépense du directeur sur le devis (`devis-boucle-reelle-organisme-v1.md`).**

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf : je n'ai écrit aucune pièce de l'organisme ni du
  programme de contrôle (texte scellé, code, analyse, verdict).
- **Heures** (temps universel, `date -u`, 7 novembre 2026) : début de la tâche 23:23:40 ; brouillon écrit de 23:44 à 23:54
  (dernière retouche relevée à 23:53:18).
- **Décision qui commande ce texte** : feu vert du directeur GO-2026-11-07-11 (`registres/go.md`, branche `main` à
  `a4ecc2e2`, ligne 271), verbatim : « Recommandation : (a), avec les fausses lois limitées à la classe couverte. Confiance
  moyenne, environ 0,6. : go ». Inscrit en R-1735 (`registres/decisions.md`, même commit).
- **Arbre** : `/home/user/wt-boucle`, branche `prep/organisme-boucle-reelle-v1`, partie de `main` à `b014b784`. Dépôt de
  l'organisme lu seulement : `/home/user/ideation-organism`, commit `94bfd92`.
- **Langue** : sans sigle. Termes définis à leur première occurrence. « Loi » : loi prédictive, objet qui donne la probabilité
  de chaque issue sachant les traits d'une instance. « Promue » : franchit le seuil du juge statistique. « Survivante » :
  promue puis « survit » à son test de mort. « Retenue » : survivante gardée dans la sélection scellée de sa génération.

## Documents qui font foi (chemin, empreinte sha256)

Dépôt de l'organisme (commit `94bfd92`) :

| pièce | chemin | empreinte |
|---|---|---|
| présentation (sections 2 à 5 ; ligne « Death tests and generation-to-generation loop : implemented, tested offline, never run for real ») | `README.md` | `bdd6516f18ec0cf44ba7fa173df519d8f88b3ee89ab8892454822babbe05b1df` |
| nul v8 et sa classe couverte (docstring, lignes 75 à 92) | `orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| validation scellée du nul v8 | `orchestrator/prereg/preenregistrement-validation-nul-v8-v2.md` | `7f37631d4f5de481d618bba151eed9d7fe30e38a6276cbbd0d2397babc0de4c5` |
| attaque de Goodhart A1-v3, texte scellé v4 | `orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v4.md` | `0b35494b7533c67b4aacb0cadc7820c825c82c046e641928df7641db8a381773` |
| validation scellée du nul v9 (sans sortie connue ; lue pour la portée seulement) | `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` | `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb` |
| tour fermé, étage 1, brouillon 6 (non scellé ; source des gardes et du devis) | `orchestrator/prereg/preenregistrement-tour-ferme-v1-brouillon6.md` | lu au commit `94bfd92` |
| rapport de code de la boucle fermée v59 | `orchestrator/prereg/rapport-code-boucle-fermee-v1.md` | lu au commit `94bfd92` |
| cœur du tour fermé v64 | `orchestrator/pole/tour_ferme_v64.py` | `35a8294e24c870685435b990d6c03cd33cb5b2e288bcb2cc91cd9af04679c2da` |
| lanceur du tour fermé v64 | `orchestrator/demonstrations/tour_ferme_v64.py` | `98c1a1a205cfe58ec277b64fbf4778e567246cfb1f0cc6882c1071704c01ae01` |
| boucle fermée v59 (lecture de la sélection) | `orchestrator/pole/boucle_fermee_v59.py` | `a2de486592fc98c14e13bb9071d272fb65d4f49de38dd188ee64857698177681` |
| juge du mode à blanc v59 (`juger_carte`) | `orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| étage des tests de mort v5 (verdict du noyau) | `orchestrator/pole/tests_de_mort_v5.py` | `da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1` |
| exécuteur du bac à sable (`bwrap`) | `orchestrator/pole/tests_de_mort_v2.py`, `orchestrator/pole/tests_de_mort_v3.py` | `363a3725…`, `ea05eb55…` |
| sélection entre générations v57 | `orchestrator/pole/etage_entre_generations_v57.py` | `e4bf36819d18844079a2bb4996991fd65c233a51d76b7d3daf5b866a71328318` |
| oracle du monde planté v60 | `orchestrator/pole/oracle_tour_ferme_v60.py` | `514864b7879e5131ee37f7a57951db5ece514abe9acbd90b1294e0d914041669` |
| juge par pari (bibliothèque aveugle) | `orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| monde planté | `orchestrator/exemples/temoins-pari-demo-v1.json` | `fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877` |

Dépôt de travail (`main` à `b014b784`, sauf mention) :

| pièce | chemin | empreinte |
|---|---|---|
| verdict d'A1-v3, troisième course | `docs/verdicts/verdict-attaque-goodhart-v3-troisieme-course-v1.md` | `7dade9ef12a4dfa4c1ce3345d35ce9b533e8696ebdf9882443a20ad5a5e78135` |
| état critique du 7 novembre (section 2) | `docs/notes/etat-critique-v1/etat-critique-programme-v1.md` | `b72fa3818948583d058672a26b499242d164ddbb62247205565dccf67c2ca192` |
| rapport au directeur (section 7, dessin et prémortem) | `docs/notes/rapport-directeur-v1/rapport-directeur-v1.md` | `a1de3d86b0a661fc241e401c835275ef8b277925851b62b423c2c77fdb76e800` |
| décision N-044 (universalité) | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` |
| décision N-045 (composition), version 2 qui prime | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` |
| décision N-049 (tâches fraîches) | `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` |
| décision N-050 (lecture unique de `test_final`) | `docs/decisions/decision-N-050-v1.md` | `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58` |
| décision N-058 (composition jugée sur l'oracle et le coût) | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |
| gabarit | `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` |
| configuration du tour fermé v4 (fournisseurs, barème prudent) | `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/configuration-tour-ferme-v4.json` | `15b34adf9329a33d9f8135160a6ea2443dc17ce786dc28fa0b5c61c4560a2e6b` |

Pièces neuves de ce dossier (`docs/notes/organisme-boucle-reelle-v1/`, non scellées) : `puissance-boucle-reelle-v1.py`
(`a2afcdd3851323000a44fced1df0ce629bcbaee0de6a7a5bcc861b83ff0571c2`) et sa sortie à 1 000 répétitions
(`a23959fa07f4c76fbd85e4bfbac7b5e6edc9ac612ad91a449f1ac10c96cef990`) ; `puissance-boucle-reelle-v1-generation2.py`
(`f552b1b980d3a9fe4e4ecb8fbe5b8067380b52c572f76f9619583bbfd05877e0`) et sa sortie
(`fe2bc5027cd4f4eb7f4a96f286b7b37687b7b8fcfe608da3e186b75d75e7c111`) ; essai à blanc `essai-a-blanc-v1/` (journal, script,
copies des sorties).

## 0. En dix lignes

1. **Question** : de la proposition à la génération suivante, tests de mort dans le vrai bac à sable compris, la chaîne de
   l'organisme garde-t-elle, avec de vrais agents, des lois vraies plantées, et refuse-t-elle des lois fausses plantées
   **toutes dans la classe que le nul v8 couvre** ?
2. **Dessin** : une génération complète, puis la génération 2 jusqu'à la lecture de la sélection et au jugement ; deux
   fournisseurs (Kimi et Argon) ; douze fiches réelles (six par fournisseur) ; une loi connue déclarée d'avance (K1) ; quatre
   lois vraies (V1 à V4) et quatre fausses (F1 à F4) plantées ; deux cas d'instrument (T-ELIM, T-MAL).
3. **Les fausses** sont des recombinaisons de K1 seule, chacune membre du nul v8 d'une loi jugée avec l'archive {K1} : copie
   renommée, mélange à l'uniforme, mélange à une loi aveugle fixe, K1 tempérée et inclinée (section 3.4).
4. **Prédiction principale (P1, signe +)** : au moins une vraie promue puis survivante en génération 1, et aucune fausse
   promue en génération 1 ni en génération 2. Puissance recalculée par simulation sur ce dessin exact : **1 000 sur 1 000,
   intervalle de Wilson à 95 % [0,9962 ; 1]** (et non 0,93 : section 4.2).
5. **Ce que la course éprouve vraiment** : la plomberie avec de vrais agents et un vrai bac à sable. Sous une chaîne correcte,
   P1 est presque certaine par construction ; un échec désigne un défaut de chaîne, pas une faiblesse statistique.
6. **Preuve que la génération 2 lit la sélection** : empreinte lue = empreinte écrite ; vue des proposeurs = lois retenues ;
   archive de jugement = K1 plus retenues ; et des copies plantées des cartes réelles retenues, refusées par construction
   si et seulement si la sélection est lue (section 3.7).
7. **Gardien mécanique, aucun juge d'idées à modèle** : rien ne décide sur la note d'un modèle ; Claude ne joue aucun rôle.
8. **Ce qui manque avant de sceller** : le code v65 (héritage de départ, jeu planté, lois plantées jugées avec l'archive,
   bras réel seul, lecture gelée), les commandes v6 des relais versées dans l'arbre, et une machine avec `bwrap` (section 12).
9. **Coût** : attendu ≈ 1,5 à 2 dollars pour les modèles (≈ 31 appels ; ≈ 8 dollars si chaque test prend ses 12 tours) ;
   plafond proposé 40 dollars pour les modèles (Kimi 33, Argon 7) et 5 pour la machine (devis).
10. **Portée** : un monde jouet (3 issues, 2 traits), une génération et demie, la classe couverte. Rien sur la classe non
    couverte, sur la puissance aux effets faibles des données réelles, ni sur l'universalité (N-044).

## 1. Question, motivation, ce qui existe

**Motivation.** Le rapport au directeur (section 7) et l'état critique (section 2) disent la même chose : « la boucle tests de
mort → sélection → génération suivante n'a jamais tourné pour de vrai » ; le juge tient dans la classe de tricheries qu'il
couvre (nul v8 : 0 sur 1 000 pour chacune des 11 lignes fatales du banc) et cède hors d'elle (A1-v3, monde W2 : 24 sur 24,
« brèche hors classe établie »). Le directeur a choisi (GO-2026-11-07-11) de courir **maintenant** la plus petite boucle
complète, en limitant les fausses lois plantées à la classe couverte, plutôt que d'élargir d'abord le nul.

**Ce qui existe dans l'organisme, et que ce dessin réutilise sans le modifier** :
- la boucle fermée v59 : la génération g+1 lit le bilan scellé de g, vérifie sceau et empreinte de la sélection, des cartes et
  des verdicts du noyau, refuse sinon (`SelectionNonVerifiee`, `HeritageRefuse`) ; la vue servie aux proposeurs ne porte que
  des lois, jamais un verdict (`VueAvecVerdict`) ;
- le tour fermé v64 (étage 1, brouillon 6 de son texte, non scellé) : proposeurs Kimi et Argon par commande externe, gardien
  mécanique, juge sous le nul v8, étage des tests de mort v5 (expérimentateur Kimi, vérificateur Argon d'une autre famille),
  contre-calcul par l'orchestrateur, lecture de la sélection par la génération suivante, oracle du monde planté ; seize
  gardes de la liste d'arrêt, chacune essayée sur un cas sain et un artefact ;
- l'essai à blanc de ce jour (`essai-a-blanc-v1/journal-essai-a-blanc-v1.md`) : toute la boucle v64, deux générations,
  fournisseurs simulés, code 0, empreintes lues égales aux écrites ; le vrai bac à sable refusé faute de `bwrap` (code 2,
  aucun repli) ; 169 essais réussis.

**Ce qui distingue ce dessin du tour fermé** : un seul bras (réel) au lieu de trois ; une génération et demie au lieu de
trois ; des lois plantées **dans la classe couverte**, jugées **avec** l'archive (le tour fermé juge ses témoins sans
archive, et trois de ses quatre fausses, S-F1, S-F2, S-F4, ainsi que T-ANTI, sont des lois inconnues du pôle, donc hors de la
classe couverte : l'essai à blanc montre S-F2 promue par le juge à la graine 20261107, log e = 9,77, puis éliminée par son
test de mort) ; une archive de départ non vide.

## 2. Hypothèse

**H-boucle** : la chaîne complète de l'organisme (proposition par deux fournisseurs réels, gardien mécanique, juge statistique
sous le nul v8, tests de mort exécutés par un expérimentateur réel dans le vrai bac à sable, verdict calculé par
l'orchestrateur sur le fichier brut, sélection scellée, lecture de la sélection par la génération suivante) conserve les
propriétés que ses éléments ont hors ligne : (a) elle laisse passer au moins une loi vraie plantée jusqu'à la survie ; (b) elle
ne promeut aucune loi fausse plantée de la classe couverte ; (c) la génération suivante juge avec la sélection de la
précédente.

Renvoi : objet « organisme d'idéation » du programme ; rapport au directeur, section 7 (« Organisme : la plus petite course
réelle de la boucle complète ») ; ce n'est pas une hypothèse du programme de contrôle (H1 à H9) et aucune revendication n'en
dépend. Hypothèses de travail : le monde planté est le monde S-V1 ; les relais tiennent les clés ; aucun agent ne voit la loi
plantée (mesuré : section 7, point 6).

## 3. Dessin

### 3.1 Monde planté

La loi S-V1 de `exemples/temoins-pari-demo-v1.json` (`fdf4d5c1…`) : softmax à 3 issues sur 2 traits réels (z0, z1), 2
sous-populations (la loi ne dépend pas de la sous-population) ; c'est le monde du tour fermé et de la boucle v59. Notée L*.
Gain d'information par épisode de L* sur sa marginale, selon l'oracle (4 000 instances ; ici et plus bas, valeurs de la sortie
à 1 000 répétitions, `a23959fa…`, champ `oracle`) : 0,520 nat.

### 3.2 Archive de départ (« génération 0 », déclarée, scellée)

Une loi connue, **K1** : la meilleure loi softmax du seul trait z0, ajustée une fois au maximum de vraisemblance attendue
sous L* sur les 4 000 instances de l'oracle (script `essai-a-blanc-v1/ajuster_k1_v1.py`, `6a8607b4…`, sortie reproduite à 23:52), arrondie et gelée :

`{"type": "softmax", "poids": [[0.0, 0.0], [-0.834964, 0.0], [-0.242046, 0.0]], "biais": [0.0, 0.941698, 0.721847]}`

Gain oracle 0,052 nat par épisode (0,051 sur les instances de l'ajustement) : K1 est **informative mais faible**. Elle est posée comme héritage de départ (bilan de
génération 0 scellé, pièce M1) : visible des proposeurs dans la vue (comme toute loi retenue), membre du nul de toute loi
jugée en génération 1. Pourquoi elle : sans loi connue, la classe couverte se réduit à la bibliothèque aveugle et les
fausses lois « couvertes » seraient des lois fixes, refusées trivialement ; avec K1, les fausses portent de l'information sur
le monde (elles seraient promues si le juge ne connaissait pas K1 : section 4.2) et ne sont refusées que parce qu'elles
n'apportent rien au-delà de l'archive.

### 3.3 Lois vraies plantées (V1 à V4)

| loi | définition | gain oracle (nat par épisode) | gain au-delà de l'archive {K1} |
|---|---|---|---|
| V1 | L* elle-même | 0,520 | 0,468 |
| V2 | softmax du seul trait z1, poids et biais de L* (colonne z0 à zéro) | 0,399 | 0,347 |
| V3 | L* tempérée, puissance 0,08 (`transformee`) | 0,091 | 0,038 |
| V4 | mélange 0,15 L* + 0,85 uniforme (`melange`) | 0,084 | 0,032 |

Chacune est une « vraie découverte » au sens gelé de l'oracle v60 (gain ≥ 0,02 et gain au-delà de l'archive ≥ 0,02). V1 et V2
sont fortes, V3 et V4 faibles (près du seuil de détection à 200 tirages) : la course mesure aussi une puissance non triviale.

### 3.4 Lois fausses plantées (F1 à F4), toutes dans la classe couverte — et comment je l'établis

| loi | définition | ligne du banc des tricheurs | membre du nul v8 qui la contient | gain oracle | au-delà de {K1} |
|---|---|---|---|---|---|
| F1 | copie renommée de K1 | T17s | « ajuste_lineaire:archive » (poids 1 sur K1) | 0,052 | −0,00003 |
| F2 | mélange 0,8 K1 + 0,2 uniforme | T03u | « ajuste_lineaire:archive » (uniforme = mélange des lois certaines) | 0,046 | −0,006 |
| F3 | mélange 0,8 K1 + 0,2 loi fixe (0,3 ; 0,4 ; 0,3) | T03b | « ajuste_lineaire:archive » (loi fixe = mélange des lois certaines) | 0,047 | −0,005 |
| F4 | K1 tempérée (puissance 1,2) et inclinée (0 ; 0,05 ; −0,05) | T05s | « ajuste_log:archive:K1 » | 0,048 | −0,005 |

**Comment j'établis l'appartenance à la classe couverte** (trois sources, puis une vérification) :
1. *Texte du nul v8* (`pole/nul_v8.py`, docstring, « Classe d'attaque couverte ») : sont couvertes « chaque loi connue seule,
   tout mélange de lois connues …, tout mélange de lois connues avec une loi aveugle fixe quelconque » (F1, F2, F3) et
   « chaque survivante … tempérée et inclinée (S(k)^a·exp(β_k)) » (F4). Pour une telle loi, « sa loi est elle-même un membre,
   donc W_t ≤ 1 à chaque instant quel que soit le monde (classe linéaire : par construction, aux arrondis flottants près) » ;
   pour le membre log-linéaire, la valeur calculée domine le vrai maximum « au second ordre près de l'optimum, sans preuve ».
   « Loi connue » = survivante de l'archive : d'où K1 posée en génération 0 et **le jugement des fausses avec l'archive**.
2. *Validation scellée du nul v8* (`README.md` de l'organisme, lignes 98 à 106 ; texte `7f37631d…`) : T17s, T03u, T03b, T05s, 0 promotion sur
   1 000 chacune sous v8 (borne haute de Clopper-Pearson 0,003).
3. *Verdict d'A1-v3* (`7dade9ef…`, sections 1 et 3) : sur W1, monde membre du nul v8 (mélange de deux lois de l'archive),
   « résiste (à cette taille) », 1 promotion sur 24, rejouée 200 fois et promue 2 fois (« par multiplicité ») ; sur W2,
   recombinaison par morceaux, classe déclarée non couverte, 24 sur 24. J'en tire la liste de ce qu'aucune fausse ne doit
   être : aucune recombinaison par morceaux (si/sinon sur un trait ou une sous-population), aucun produit de deux lois,
   aucune composition d'étapes, aucune loi inconnue du pôle. Le nul v9 (`54c5713d…`), qui ferme le trou par morceaux, n'est
   pas validé (aucune sortie connue) : ce dessin reste sous le nul v8.
4. *Vérification hors ligne* (section 4.2) : jugées avec l'archive {K1}, F1 à F4 ne sont jamais promues sur 4 000 jugements, et
   leur plus grand log W maximal est −0,004 ; jugées **sans** l'archive (canal des témoins de la v64), au moins une est promue
   dans 994 répétitions sur 1 000. La protection vient donc de l'appartenance à l'archive : la chaîne doit les juger dans ce
   canal (pièce M3), et la course le vérifie (garde 18).

### 3.5 Cartes réelles, fournisseurs et modèles

- **Proposeurs** : Kimi (`kimi-k3.1-pro`, comptes existants, relais local `127.0.0.1:8804`, commande externe v6) et Argon
  (`gemini-4-argon`, clé existante, relais local `127.0.0.1:8805`, commande externe v6) ; un appel par fournisseur et par
  génération, au plus 6 lois chacun, au gabarit fermé de la v64 (énoncé, loi de la grammaire servie, bornes ±4). Les relais
  tiennent les clés ; l'orchestrateur refuse toute variable de clé dans son environnement (annexe A de la v64).
- **Expérimentateur des tests de mort** : Kimi (commande externe ; « Kimi par protocole » ne tient pas ce rôle et est refusé
  avant tout appel). **Vérificateur** : Argon, autre famille (garde 9), témoin seulement, jamais décisif.
- **Gardien** : mécanique (décision D9 « mecanique » de la v64 : grammaire, bornes, évaluation sur un jeu factice fixe) ;
  aucun appel de modèle.
- **Aucun juge d'idées à modèle** : les juges croisés de l'organisme sont hors de la chaîne (ils étaient au plafond à la
  deuxième course réelle, `README.md` de l'organisme, ligne 125 ; leur version 2 n'est pas scellée). **Claude ne joue aucun rôle** : les textes de
  l'organisme mettent hors portée les proposeurs de la famille Claude (tour fermé, section 11) et excluent un juge de cette
  famille sur des témoins écrits par un modèle de la famille Claude (juges d'idées v2, brouillon 3) ; les lois plantées de ce
  texte sont écrites par un modèle de la famille Claude.
- **Composition** (N-045, N-058) : aucune décision de composition ne se prend sur une génération ; la course rapporte, par
  fournisseur, les vraies découvertes selon l'oracle et le coût, jamais le verdict du juge comme critère de composition.

### 3.6 Jugement

- **Cartes réelles** : nul v8 avec les membres d'archive de leur génération (génération 1 : {K1} ; génération 2 : {K1} plus
  les cartes réelles retenues en génération 1), 200 tirages frais par carte, graines des tirages dérivées de la tâche et de
  l'empreinte de l'engagement gelé ; règle de Benjamini et Hochberg sur les valeurs e (« e-BH » dans le code), m fixé à 22.
- **Lois plantées** (V, F, T-ELIM, et en génération 2 les copies de la section 3.7) : même nul v8, **avec** l'archive de
  jugement de leur génération (pièce M3), hors de la famille des cartes réelles (elles ne pèsent pas sur le nombre de cartes
  retenues), comptées promues si le juge les promeut et si leur log e atteint log(m/α) = log(22/0,05) ≈ 6,09 (règle « hors famille »
  de `tour_ferme_v64.juger`). Elles sont servies à l'aveugle (identifiant opaque `F-<12 hexadécimaux>`, titre et hypothèse
  neutres) et **jamais retenues ni servies aux proposeurs** (garde 7 de la v64).
- **T-MAL** (L* sans statistique) : doit être refusée au gardien. **T-ELIM** (L* à la puissance 1,25, seuil de test « au moins
  2,0 ») : doit être promue puis éliminée par son test de mort.

### 3.7 Tests de mort dans le vrai bac à sable ; sélection ; génération 2

- **Tranche** : 400 épisodes tirés de L* par génération (graine de la tâche), écrits par l'orchestrateur avec l'évaluateur de
  référence `evaluateur_lois_v62.py` ; liste blanche et index vérifiés (dossier fermé).
- **Test imposé** : gain moyen par épisode du log-score de la loi gelée sur la marginale empirique de la tranche (comptes
  + 0,5), seuil « au moins 0,02 » nat ; la loi gelée est servie dans le préenregistrement court ; l'expérimentateur écrit
  `gains.csv` ; **le verdict est calculé par l'orchestrateur sur ce fichier brut** (`verdict_du_noyau`, étage v5) ; le nombre
  imprimé par le script n'est qu'un témoin ; contre-calcul indépendant (`statistique_hors_bac`) égal à 10⁻⁶ près, sinon arrêt.
- **Bac à sable** : `bwrap` (bubblewrap), réseau et espaces de noms isolés (`--unshare-all --unshare-net`), aucune capacité
  de superutilisateur, utilisateur dédié sans privilège sur l'hôte (par exemple 64097) avec son dossier racine en 0700,
  un seul dossier de travail, groupe de contrôle mémoire borné à 768 Mo, filtre d'appels système (`--seccomp`), limites de
  fichiers, de processus et de temps processeur, aucune clé, environnement pris dans une liste blanche fermée, fichier témoin
  vérifié sur l'hôte (`pole/tests_de_mort_v2.py`, lignes 1 à 70 et 1251 et suivantes ; v3 : borne de 768 Mo). Isolement
  vérifié par la sonde du bac avant le premier test ; sur une machine sans `bwrap`, refus (code 2), jamais l'exécuteur factice
  (garde 3, rejouée dans l'essai à blanc). **La course exige une machine jetable qui a `bwrap`** (section 12, M0).
- **Sélection** (étage v57) : seules les cartes réelles « survit » au verdict du noyau sont retenues ; bilan de génération
  scellé (sélection, cartes, verdicts nommés par empreinte).
- **Génération 2** : (i) lit le bilan de la génération 1 par son empreinte (`lire_heritage`, contre-vérification des
  retenues) ; (ii) sert aux proposeurs la vue {K1} plus les lois retenues ; (iii) deux appels de proposeurs, gardien, juge
  avec l'archive {K1} plus retenues ; tests de mort des seules cartes réelles promues ; (iv) replante F1 à F4 et, **si au moins
  une carte réelle a été retenue en génération 1, une copie renommée de chacune des quatre premières retenues par log e** (au
  plus quatre ; ligne T17s du banc, classe couverte). Ces copies sont la preuve, au niveau des verdicts, que la génération 2
  juge avec la sélection : membres du nul, elles sont refusées par construction ; jugées sans la sélection, elles seraient
  promues aussi souvent que leur original (simulation, section 4.2). V1 à V4 et T-ELIM ne sont pas replantées en génération 2
  (elles ne sont jamais retenues : elles se jugeraient de nouveau contre la même archive, sans rien prouver).
- **Arrêt après le jugement et les tests de mort de la génération 2** : sa sélection est scellée, aucune génération 3.

## 4. Prédictions chiffrées et signes attendus

### 4.1 Prédictions

| repère | prédiction (signe) | probabilité simulée sous une chaîne correcte | réfutation |
|---|---|---|---|
| **P1** (principale) | au moins une vraie (V1 à V4) promue puis survivante en génération 1 **et** aucune fausse (F1 à F4, et copies de la génération 2) promue (+) | 1 000 / 1 000, Wilson [0,9962 ; 1] | aucune vraie survivante, ou une fausse promue |
| P2 | V1 et V2 promues puis survivantes chacune (+) | 1 000 / 1 000 chacune | l'une manque |
| P3 | V3 et V4 (faibles) : mesurées, sans seuil | promues puis survivantes 617 et 501 / 1 000 ; les quatre ensemble 318 / 1 000 | — (mesure) |
| P4 | T-ELIM promue puis éliminée ; T-MAL refusée au gardien (+) | 1 000 / 1 000 ; T-MAL par construction | T-ELIM survivante, ou T-MAL jugée |
| P5 | génération 2 : chaque copie d'une carte réelle retenue est refusée ; F1 à F4 refusées (+) | refus par construction ; simulé sur des lois retenues tenant lieu de cartes réelles : 0 promotion sur 1 000, 1 000 / 1 000 promues si la sélection n'est pas lue | une copie promue |
| P6 | lecture de la sélection : empreinte lue = écrite ; vue = {K1} ∪ retenues ; nombre de membres d'archive des cartes de la génération 2 = celui qu'impose {K1} ∪ retenues (+) | par construction (essai à blanc : égalité vue sur les trois bras) | un écart |
| P7 | cartes réelles : aucune prédiction ; mesurées (proposées, refusées au gardien, promues, testées, survivantes, retenues, vraies et fausses découvertes selon l'oracle, par fournisseur ; coût par rôle et par fournisseur) | — | — |

Signe : tout est « + » (la chaîne fait ce que ses éléments font hors ligne). **Aucune prédiction n'est ouverte dans un seul
sens** : une issue « trop belle » déclenche l'audit de symétrie (section 9) comme une issue « trop laide ».

### 4.2 Puissance, recalculée par simulation hors ligne sur ce dessin exact

Script `puissance-boucle-reelle-v1.py` (`a2afcdd3…`), 1 000 répétitions, graine 20261107 dérivée par
`numpy.random.SeedSequence(20261107).spawn(1000)`, tâches par `boucle_fermee_v59.graine_de_tache` ; il appelle le juge de la
boucle (`a_blanc_v59.juger_carte`, nul v8, 200 tirages) et recopie en mémoire la statistique gelée du test de mort (tranche de
400 épisodes, seuil 0,02 nat). Sortie `sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json` (`a23959fa…`), 23:32:51 →
23:35:15. Complément `puissance-boucle-reelle-v1-generation2.py` (`f552b1b9…`), sortie `fe2bc502…`, 23:37:09 → 23:42:45.

| mesure | valeur |
|---|---|
| P1 : au moins une vraie promue puis survivante et aucune fausse promue | **1 000 / 1 000** [0,9962 ; 1] |
| au moins une vraie promue puis survivante | 1 000 / 1 000 |
| toutes les vraies | 318 / 1 000 [0,290 ; 0,348] |
| V1, V2, V3, V4 promues puis survivantes | 1 000 ; 1 000 ; 617 ; 501 |
| fausses promues avec l'archive (4 000 jugements) | 0 ; plus grand log W maximal −0,004 (F4), −0,005 (F1) |
| **artefact** : fausses jugées sans l'archive, au moins une promue | 994 / 1 000 (725 à 810 chacune) |
| T-ELIM promue puis éliminée | 1 000 / 1 000 |
| génération 2 : loi retenue en génération 1, replantée, promue | 0 / 1 000 (avec la sélection) ; 1 000 / 1 000 (sans) |

**Pourquoi 1,00 et non 0,93.** Le rapport au directeur composait des puissances publiées sur la banque d'épisodes réels
(forces 0,8 et 0,5 : 0,95 et 0,71 ; fausses à 0,018 par carte). Ici le monde est le monde jouet du tour fermé, où une loi qui
porte 0,4 à 0,5 nat par épisode atteint un log W de 70 à 100 sur 200 tirages ; et les fausses de la classe couverte sont
refusées par construction, non à 1,8 %. Le chiffre de 1,00 n'est donc **pas** une puissance de détection d'effets réels :
c'est la probabilité que la chaîne rende la bonne issue si elle est correcte. Toute la valeur informative de la course est
dans l'écart à ce chiffre (un défaut de plomberie, d'expérimentateur, de bac ou de lecture de la sélection).

**Limite de la simulation (dite)** : les cartes réelles ne sont pas simulées (seul m = 22 les représente) ; l'expérimentateur
est supposé écrire exactement le script servi ; en génération 2, des lois vraies retenues tiennent lieu des cartes réelles
retenues (en course, les lois plantées ne sont jamais retenues : garde 7) ; une seule tranche par génération ; interpréteur
numpy 2.4.6.

## 5. Métriques

- **Promue** (par loi) : juge du pari apparié, nul v8, membres d'archive de la génération, 200 tirages frais, promotion au
  sens de `selection_pari` (richesse ≥ 1/α à un instant lu, marge des filles comprise) ; pour les lois plantées, log e ≥
  log(m/α) en plus ; pour les cartes réelles, règle de Benjamini et Hochberg sur les valeurs e à m = 22.
- **Survivante** : verdict du noyau « survit » sur `gains.csv` (statistique moyenne ≥ 0,02 nat ; T-ELIM : ≥ 2,0) ; « non
  concluant » n'est pas « survit ».
- **Classe** (audit) : vraie découverte, fausse découverte et fausse promotion du juge au sens gelé de
  `oracle_tour_ferme_v60.classer` (seuil g₀ = 0,02 nat ; gain au-delà de l'archive avec l'archive de jugement de la carte).
- **Lecture de la sélection** : égalité des empreintes ; identité ensembliste vue = {K1} ∪ retenues ; nombre de membres
  d'archive par carte ; issue des copies (P5).
- **Intervalles** : Wilson à 95 % pour les parts ; aucune moyenne sur des jetons.
- **Coût** : dollars par rôle et par fournisseur relevés au registre cumulé des relais ; appels ; jetons d'entrée et de sortie.

## 6. Seuils

α = 0,05 (juge) ; m = 22 (fixé d'avance : 12 cartes réelles, 8 lois plantées, 2 cas d'instrument ; en génération 2 : 12, 4
fausses, au plus 4 copies, toujours ≤ 22) ; seuil des lois plantées log(22/0,05) ; seuil du test de mort 0,02 nat (T-ELIM :
2,0) ; tolérance du contre-calcul 10⁻⁶ ; seuil de l'oracle g₀ = 0,02 nat. Aucun seuil ne se lit après la course.

## 7. Plan d'analyse

1. **Graines** (règle R9) : racine E = entier de l'empreinte sha256 du texte scellé (≥ 2⁶⁴, garde 6 de la v64) ; chaque tâche
   par `graine_de_tache(E, tâche)` = `SeedSequence(E, spawn_key=(clé de la tâche,))` ; tirages frais dérivés de la tâche et de
   l'empreinte de l'engagement gelé ; manifeste de course (configuration et empreinte, versions, graines, commit).
2. **Ordre** : génération 0 lue (empreinte du bilan de départ au texte) → génération 1 (propositions, gardien, juge, tests de
   mort, sélection, bilan scellé) → génération 2 (lecture, vue, propositions, gardien, juge, tests de mort des cartes réelles
   promues, copies et fausses replantées, sélection scellée) → relevé scellé → lecture gelée par un programme à part, par un
   lecteur neuf (règle R13).
3. **Oracle lu une seule fois** (dans l'esprit de N-050) : gains et classes des lois ne sont calculés qu'après la course, par
   la lecture gelée ; rien de l'oracle n'est servi à un agent ni ne nourrit la sélection.
4. **Tâches fraîches** (N-049) : les épisodes de développement servis aux proposeurs et la tranche sont tirés à neuf à chaque
   génération (graines par tâche).
5. **Multiplicité** : règle de Benjamini et Hochberg sur les valeurs e pour les cartes réelles ; lois plantées hors famille au
   seuil log(m/α) ; aucune correction supplémentaire entre P1 et P6 : la lecture est une conjonction gelée (section 8).
6. **Recherche de la loi plantée dans ce qui est servi** (mesurée, v62 C16) : les paramètres de L*, exacts ou à deux
   décimales, dans les consignes et contextes servis aux proposeurs, à l'expérimentateur et au vérificateur ; attendu : aucun
   touché hors de la loi gelée servie au test de mort (que l'expérimentateur doit voir).
7. **Comptes pour l'audit** (repris du tour fermé, section 9 du rapport v59) : par génération, proposées, refusées au gardien
   (motifs), jugées, m, promues, testées, verdicts, survivantes, retenues ; par loi : log W maximal, log e, membre dominant du
   nul, nombre de membres d'archive, empreinte d'engagement, graines ; sessions et coût par rôle.

## 8. Critères de lecture gelés

Lus dans cet ordre ; la première ligne qui s'applique donne l'issue.

| ordre | condition observée | issue | ce qu'elle dit |
|---|---|---|---|
| C5 | course arrêtée (code 3) ou relevé incomplet | **« non jugeable (arrêt) »** | rien sur la chaîne ; chiffres partiels rapportés comme tels ; cause écrite (infrastructure ou garde) ; **si le relevé partiel montre déjà une fausse ou une copie promue, ou une lecture de sélection en écart, C2 ou C4 s'écrit aussi, marquée « partielle »** : un arrêt ne masque jamais une brèche |
| C4 | P6 manquée (empreinte lue ≠ écrite, vue ou archive de la génération 2 ≠ {K1} ∪ retenues), ou une copie de la génération 2 promue | **« boucle non fermée »** | la génération suivante ne lit pas la sélection : corriger la chaîne avant toute autre course |
| C2 | une fausse F1 à F4 promue en génération 1 ou 2 (une copie promue relève de C4) | **« brèche dans la classe couverte »** | audit A2 (section 9) : jugée sans archive (défaut de chaîne) ou membre du nul promu (défaut numérique) ; arrêt de toute promotion réelle jusqu'à correction |
| C3 | aucune vraie promue puis survivante en génération 1 (et aucune fausse promue) | **« sans dents »** | audit A3 : vraies non promues (juge ou plomberie) ou promues puis non survivantes (expérimentateur, bac, verdict du noyau) |
| C6 | P4 manquée (T-ELIM survivante ou non promue, T-MAL jugée) | **« instrument en défaut »** | le test de mort ou le gardien ne fait pas ce qu'il dit ; l'issue C1 ne se prononce pas |
| C1 | P1, P4 et P6 tenues | **« la chaîne garde (classe couverte, ce monde, cette taille) »** | ouvre la proposition au directeur de plusieurs générations ; ne dit rien de la classe non couverte ni des données réelles |

Mesures sans issue : P3 (puissance aux vraies faibles), P7 (cartes réelles), coût, recherche de la loi plantée. **Une fausse
découverte d'une carte réelle** (promue puis survivante, gain au-delà de l'archive < 0,02 nat) ne change pas l'issue (elle
est hors du dessin, et peut venir de la classe non couverte) mais **s'écrit en tête du rapport** et déclenche l'audit A2 sur
sa forme (par morceaux, produit, composition, autre).

## 9. Audit de symétrie (règle R4), écrit d'avance

- **A1 « trop beau »** : déclenché d'office si C1 (l'issue est presque certaine par construction) : vérifier sur les fichiers
  bruts que chaque vraie survivante a été jugée avec le bon nombre de membres d'archive, que son `gains.csv` vient du bac
  réel (fichier témoin, journal de `bwrap`), que le contre-calcul est égal, que l'expérimentateur a bien été appelé (registre
  du relais apparié appel par appel), que les fausses ont des log W maximaux ≤ 0 aux marges près, que la vue de la
  génération 2 ne contient aucune loi plantée.
- **A2 « fausse promue »** : rejouer la loi promue 200 fois sur des tirages neufs (`auditer_promues` de l'attaque) ; vérifier
  ses membres d'archive ; classer sa forme ; une fausse jugée sans archive est un défaut de chaîne, non une brèche du nul.
- **A3 « sans dents »** : pour chaque vraie, séparer non promue / promue non survivante / non concluante ; relire les traces de
  l'expérimentateur (tours, fin des tours, « rien envoyé ») ; rejouer son jugement hors ligne à la même graine.
- **A4 « copie promue »** : comparer les membres d'archive de la copie à ceux qu'impose la sélection lue.
- Le même audit s'applique quelle que soit l'issue ; ses constats s'écrivent avant toute phrase de résultat.

## 10. Liste d'arrêt

Reprise de la liste du tour fermé, brouillon 6, section 7 (gardes 1 à 10 et 13 à 16, chacune déjà essayée sur un cas sain et
un artefact dans `essais/test_tour_ferme_v64.py` et `essais/test_gardes_tour_ferme_v64.py`) : lecture vérifiée de l'héritage ;
vue sans verdict ; vrai bac à sable sans repli ; graines dérivées de la tâche ; plafond et parts des relais (arrêt avant un
étage si la part restante est sous son pire cas) ; texte scellé exigé (nom sans « brouillon », sceau, aucun marqueur, code
gelé conforme) ; lois plantées jamais retenues ni servies ; gabarit du test de mort imposé ; familles séparées ; contre-calcul
(désaccord → arrêt) ; modèle servi inconnu, session en échec, rôles tenus ; machine jetable et liste blanche de
l'environnement ; « rien envoyé » lu « budget dépassé » pour la seule session ; durée 72 heures (garde contre une boucle
folle, jamais un couperet). **Gardes neuves (code v65, à essayer sur cas sain et artefact avant le scellement)** :

| # | garde | cas sain | artefact |
|---|---|---|---|
| 17 | héritage de départ | bilan de génération 0 à l'empreinte écrite au texte | autre empreinte, K1 altérée, loi plantée dans l'héritage → refus, code 2 |
| 18 | lois plantées jugées avec l'archive | nombre de membres d'archive de chaque loi plantée = celui de l'archive de sa génération | loi plantée jugée avec 0 membre → arrêt, code 3 |
| 19 | jeu planté du texte | huit lois et deux cas d'instrument égaux à l'octet au bloc du texte scellé | une loi changée → refus, code 2 |
| 20 | bras réel seul | un seul bras joué | bras de référence demandé → refus, code 2 |
| 21 | copies de la génération 2 | copies des quatre premières retenues par log e, ou aucune si rien n'est retenu | copie d'une carte non retenue → refus |
| 22 | machine | `bwrap` ≥ 0.9, sonde du bac réussie, utilisateur dédié | sonde refusée → code 2 avant tout appel payant |

Arrêt = relevé partiel scellé, code 3, aucune issue lue sauf C5 (et C2 ou C4 « partielle », section 8). **Panne d'un relais**
(le bras Kimi de la première attaque A1 a été perdu, par un plafond de dépense partagé selon la correction du `README.md` de l'organisme, ligne
129 ; le brouillon 3 des juges d'idées v2 compte, pour le relais Kimi à A1, 5 appels réussis et 616 en échec) : arrêt pour
infrastructure, jamais de bascule silencieuse vers l'autre fournisseur ; une reprise demande un texte neuf contre-lu.

## 11. Prémortem du rapport au directeur, et réponse du dessin

| risque nommé | réponse |
|---|---|
| juges d'idées au plafond | aucun juge d'idées à modèle dans la chaîne ; le juge statistique seul décide |
| classe non couverte | fausses limitées à la classe couverte, jugées avec l'archive (gardes 18 et 19) ; une fausse découverte réelle hors classe est rapportée en tête, sans changer l'issue |
| vrai bac à sable jamais lancé | `bwrap` exigé, sonde avant tout appel payant, aucun repli (gardes 3 et 22) ; essai à blanc `--bac reel` rejoué sur la machine de la course avant le lancement |
| sélection non lue par la génération suivante | P6 et P5 (copies refusées par construction si et seulement si la sélection est lue) ; issue C4 |
| témoins reconnaissables | identifiants opaques, titre et hypothèse neutres, lois plantées jamais servies aux proposeurs ; recherche de la loi plantée mesurée ; reste : l'expérimentateur voit la loi gelée qu'il éprouve (nécessaire au test) et K1 est visible des proposeurs (loi connue, voulue) |

## 12. Ce qui manque avant de sceller (pièces et décisions)

| repère | pièce | qui |
|---|---|---|
| M0 | machine jetable avec `bwrap` ≥ 0.9 et utilisateur dédié (le conteneur de ce jour n'a pas `bwrap`) ; essai à blanc `--bac reel` rejoué dessus | session de dépôt, sur devis |
| M1 | héritage de départ scellé (génération 0, K1 « connue, déclarée ») accepté par `lire_heritage` | développeur neuf, code v65 |
| M2 | jeu planté V1 à V4, F1 à F4, T-ELIM, T-MAL lu dans le texte scellé (remplace `TEMOINS` de la v64) | code v65 |
| M3 | lois plantées jugées avec l'archive de jugement de leur génération (la v64 les juge sans) | code v65 |
| M4 | bras réel seul ; génération 2 avec copies et fausses replantées | code v65 |
| M5 | lecture gelée des critères C1 à C6 et des audits A1 à A4, essayée sur cas sain et artefact | code v65 |
| M6 | commandes v6 de Kimi et d'Argon (`outils/commandes-tour-ferme-v1`, `12f9e0e3`, R-1129) versées dans l'arbre ; configuration v5 qui les nomme, avec plafond et parts du devis | session de dépôt |
| M7 | interpréteur de la machine (numpy 2.5.3 documenté ; 2.4.6 ici ; huit jugements du dessin égaux à l'octet sous les deux, journal de l'essai, étape 7) ; essais et banc de mutations v65 rejoués dessus | développeur, puis contre-lecteur |
| D1 | décision du directeur : bras réel seul (recommandé) ou les deux bras de référence en plus (devis, variante) | directeur |
| D2 | décision du directeur : génération 2 complète comme ici, ou réduite à la lecture et au jugement sans appel de proposeur (− 2 appels) | directeur |
| D3 | feu vert de dépense sur le devis | directeur |

Bloc d'empreintes du code gelé v65 et commandes exactes : à écrire avec le code (marqueur volontaire : <<BLOC-V65>>).

## 13. Devis

`devis-boucle-reelle-organisme-v1.md` : attendu ≈ 1,5 à 2 dollars pour les modèles (≈ 31 appels), ≈ 8 si chaque test prend
ses 12 tours ; pire cas sous les bornes par carte 28,10 dollars (chaîne correcte) et 35,30 (chaîne cassée : fausses et
copies promues puis testées) ; plafond proposé 40 dollars pour les modèles (parts : Kimi 33, Argon 7), qui couvre le pire cas
de la chaîne cassée pour qu'aucun arrêt de dépense ne masque une brèche ; 5 dollars pour la machine.

## 14. Portée

Un monde jouet (3 issues, 2 traits, la loi S-V1), une archive de départ d'une loi, deux fournisseurs, une génération complète
et une seconde jusqu'à sa sélection, la classe couverte du nul v8. **Rien** sur : la classe non couverte (recombinaisons par
morceaux, produits, compositions : l'issue C1 ne la couvre pas) ; la puissance aux effets faibles des données réelles (`README.md` de l'organisme,
ligne 122) ; la qualité des idées ; l'universalité sur des familles inédites (N-044) ; la composition des proposeurs (N-045,
N-058). Une issue C1 se rapporte toujours avec A1-v3 (brèche hors classe établie) et avec cette portée.

## 15. Contre-lecture (règle R2)

À faire par un sous-agent neuf, qui n'a écrit ni ce texte ni le code v65, sur : ce brouillon ; `puissance-boucle-reelle-v1.py`
et `-generation2.py` et leurs sorties ; `essai-a-blanc-v1/` ; `devis-boucle-reelle-organisme-v1.md` ; les pièces de la table
« Documents qui font foi » ; le diff v64 → v65. Questions à lui poser : les fausses sont-elles bien dans la classe couverte,
et jugées dans le bon canal ? la preuve de lecture de la sélection est-elle suffisante si aucune carte réelle n'est retenue ?
le chiffre de 1,00 est-il présenté sans ambiguïté ? les gardes 17 à 22 sont-elles essayées ?
