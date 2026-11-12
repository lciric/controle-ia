# Journal — note de conception du pilier « génération » de la couche 4, v1

- **Rôle** : rédacteur neuf, sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; modèle Opus 5.5
  (`claude-opus-5-5`). Je n'ai écrit ni la synthèse du tour 2, ni le dessin de l'essai Lean, ni le programme de l'organisme,
  ni aucune pièce lue. Conflits : même famille que les espèces A et B du collisionneur ; même modèle que le lecteur du tour 2,
  le rédacteur de l'essai Lean et le rédacteur du programme de l'organisme v3.
- **Heures** (relevées par `date -u`, le 2026-11-10) : début 14:11:52 UTC ; lectures jusqu'à ≈ 14:19 ; écriture de la note à
  partir de 14:19:32 ; journal commencé à 14:26:46 UTC.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-note-pilier-generation-v1.md`,
  empreinte vérifiée par `sha256sum` **avant** lecture : `61ec586c07037c7db3ab86fec9821df787de081a2f6d5083aa3ce625cf2bdce5`,
  égale à celle donnée par la mère. Interdits communs v2 recopiés dans la consigne ; leur fichier source a l'empreinte
  annoncée (`1ee3b370…`).
- **Note** : `note-conception-pilier-generation-v1.md` (même dossier) ; son empreinte est en fin de ce journal.

## 1. Sources lues (empreintes calculées ; préfixes de la consigne vérifiés)

| pièce | chemin | sha256 | ce qui a été lu |
|---|---|---|---|
| consigne | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-note-pilier-generation-v1.md` | `61ec586c07037c7db3ab86fec9821df787de081a2f6d5083aa3ce625cf2bdce5` | en entier |
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` | haché seulement (texte recopié dans la consigne, lu là) |
| registre des décisions (vivant) | `registres/decisions.md` | à la lecture (14:12 UTC) `8a06c09316e58fbe1369849cbb6d8f96fe0d84ba406a3ffdb00e65c55256dfde` ; à l'assemblage (≈ 14:24) `d0f731bc1e767ea820dc0565d6adfdd98c3120120d7b89cac37b650a1c2ddcd0` | lignes R-920 (l. 1149), R-959 (l. 1188), R-2199 (l. 2157), R-2221 (l. 2179, venue avec le filtre), R-2226 (l. 2184), R-2230 (l. 2188), R-2236 (l. 2194), R-2240 (l. 2198) ; R-2026 (l. 1984) et R-2133 (l. 2091) par `git grep -n "N-065" -- registres/decisions.md` ; après l'assemblage, contrôle filtré des lignes neuves (§ 5) |
| N-044 | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` | en entier |
| N-045 v2 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` | en entier |
| N-058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` | en entier (hors de la liste « À lire » ; nommée par le mandat de la consigne, point 3, et citée par le programme v3) |
| N-064 | `docs/decisions/decision-N-064-v1.md` | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97` | en entier |
| N-065 | `docs/decisions/decision-N-065-v1.md` | `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4` | en entier |
| synthèse du tour 2 N12-N13 | `docs/notes/ideation-organisme-v1/course-2/collisionneur-n12-n13-v1/synthese-n12-n13-tour2-v1.md` | `6ef6bc2e1cbea69b0b47f20508fa09391e7c2271785287c470dc632de5a2b1ce` | l. 1–51 (en-tête, réserve, décompte), l. 214–259 (§ E), l. 423–442 (« Ce qui reste chez Lazar », traçabilité) ; titres ; recherche de « Lean », « couche 4 » dans § F–G |
| essai Lean, brouillon 3 | `brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md` | `717259ed1dfd5e4e9c591b3c7d22a4316ec1fe1195ea83bb887ca3f60fd2ac37` | l. 1–368 (verdict, § 0 à 3), l. 369–405 et 471–654 (§ 4.1, 4.2, 4.4 à 9) ; § 4.3 (tableaux du devis) non lu en détail |
| essai Lean, contre-lecture 1 | `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon1-cl1.md` | `f565d51cd39ae047d50a1774e79c67301f54ab5c1c107c4cba50193d33ba7744` | l. 1–85 (corps) ; couples et annexe non lus |
| essai Lean, vérification courte | `prereg/contre-lectures/essai-preuve-formelle-devis-v1-brouillon2-verification-courte-v1.md` | `38e40d21e60f7588233b3fda27b365c6a48abb97ecb9dd3a5ff94cb44ad73d8a` | l. 1–98 (corps) ; scripts et sorties en annexe non lus |
| programme de l'organisme v3 | `docs/notes/rapports-directeur/programme-organisme-complet-v1/programme-organisme-complet-v3.md` | `bbde32b7eedc05eb5c3bc1f67c2282e4ef01fef61fd88c5afac6c11be93064fc` | l. 1–92, 145–286 (§ 0, 2), 354–432 (§ 4.1–4.3), 511–595 (§ 5–7), 1373–1430 (MAT, REC, PAC) ; filtre de mots sur 1109–1372 (JUG, ATQ, VER) ; table des pièces (l. 940–1012) filtrée |
| inventaire des idées v4 | `docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v4.md` | `66e05f31f56a239f437c338fa89f4de02589344ee59b36a4ddb24679ed79be2e` | titres ; famille MAT (7 entrées) et lignes filtrées sur « Lean », « conjecture », « nouveauté » ; la v7 finale (R-2221) n'est lue qu'à travers sa copie dans la partie II du programme v3 (MAT : 8 entrées, MAT-008 en plus) |
| programme d'entretien v16 (hors liste ; carte des hypothèses citée par l'essai) | `brouillons/entretien-taif-v3/programme-entretien-taif-v16.md` | `186173d9d9b949bfb3922503adff1be9d60f49f07fb975750de4c88bd60a060e` | l. 322–335, 410–450, 760–770, 800–812, et lignes filtrées sur « lemme », « Lean », « f7dfe5fd » |
| programme de conception de l'organisme v1 (clé PCO du programme v3) | `origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v1.md` | `72fa0e609258d1a208195440c645f2b7f250c5c5bba70e304407ded09de3c6ff` (sortie de `git show`, égale à la table du programme v3) | l. 1–100, par `git show` (règle 4) |
| consignes de la maison | `CLAUDE.md` | `b4cbc66a422a6246df0479fe0c886eccb92cd3410d6a8b742eddea5325098eae` | servie par le système ; N-062 lue l. 13 |
| module de scellement | `src/controle_ia/scellement.py` | non haché | l. 1–90 (usage) |
| registre des GO | `registres/go.md` | non haché | recherche « preuve formelle », « lean », « D-1a » : aucune ligne |

## 2. Affirmations de la note et leur renvoi

| n° | affirmation (dans la note) | renvoi (chemin, ligne) | statut |
|---|---|---|---|
| J-1 | mandat, sorties, interdits | consigne, en entier | VÉRIFIÉ |
| J-2 | N12 (b) : couches 3 et 4 fermées jusqu'aux résultats de l'étape 2 ; seul pas : l'essai | `registres/decisions.md` l. 1188 (R-959) ; programme v3 l. 1376 (MAT-001) | VÉRIFIÉ |
| J-3 | ordre (a), (b), (c) ; (c) = note de conception du pilier, nœud chez Lazar | `registres/decisions.md` l. 2157 (R-2199) | VÉRIFIÉ |
| J-4 | (a) fait ; aucune espèce ne parle de génération de mathématiques nouvelles | `registres/decisions.md` l. 2184 (R-2226) | VÉRIFIÉ |
| J-5 | essai : brouillon 3 rendu, D-1a présenté à Lazar (65 USD), D-1b après préenregistrement, phase 2 plafond indicatif 1 950 USD ; aucun GO au registre des GO | `registres/decisions.md` l. 2188, 2194, 2198 ; `registres/go.md` (recherche vide) | VÉRIFIÉ |
| J-6 | aucune espèce ne parle de conjectures, de juge de nouveauté, de Lean comme arbitre d'objets produits ; « qui décide l'ouverture de la couche 4 » non nommé (E en général) | synthèse du tour 2 l. 245–247, l. 431 ; table E.1 l. 222–228 | VÉRIFIÉ |
| J-7 | vérificateur externe hors organisme, tenu par les cinq espèces, réserve R4 | synthèse du tour 2 l. 251 ; l. 14–16 | VÉRIFIÉ |
| J-8 | une preuve ne valide pas une spécification empirique (MAT-004) | programme v3 l. 1380 | VÉRIFIÉ |
| J-9 | invariant de N-053 (aucun score de moniteur ni de juge dans un signal d'entraînement ou de sélection de l'agent) ; juge d'une autre lignée (point 4) | `decision-N-058-v1.md` l. 25 ; programme v3 l. 559 | RAPPORTÉ (N-053 non lue) |
| J-10 | composition des proposeurs jugée sur l'oracle du monde planté et le coût ; l'interdit porte sur la sélection d'agents, pas des fiches | `decision-N-058-v1.md` l. 20, l. 39 | VÉRIFIÉ |
| J-11 | rôles 1 et 2 de N-065 ; invariants et citations obligatoires | `decision-N-065-v1.md` l. 15–20, 23–24 | VÉRIFIÉ |
| J-12 | gardes G-L1 à G-L7 ; artefact « étape à hypothèses contradictoires » ; prix (Opus 5.5 4 / 20 « à vérifier », Kimi 2 / 10 « vérifiés le 30 octobre », Astra 10 / 50 « SUPPOSÉS », Argon 10 / 50 prudent) ; item L 1,162 attendu, 3,082 pire réaliste, plafond 4 | essai b3 l. 270–276 ; l. 377–382 ; l. 393, 402 | VÉRIFIÉ (dans le texte de l'essai ; prix non vérifiés à leur source) |
| J-13 | classe K5 « énoncé voisin » ; spécification altérée ; audit sur l'énoncé imprimé par Lean (50 % pilote, 30 % confirmation) ; relecteur de fidélité d'une autre famille | essai b3 l. 176, 224, 230, 277 | VÉRIFIÉ |
| J-14 | isolement : sans clé ni dépôt, réseau coupé et éprouvé avant tout code de modèle, lecture seule, dossier neuf par item | essai b3 l. 494, 499 | VÉRIFIÉ |
| J-15 | lien de l'essai au pas (c) : carte de couverture par domaine, taux de base sans pression, ce qu'il n'apprendra pas (nouveauté) ; O0 ; score apparié et marqueur `<<SOURCE_TANGO>>` ; question « temps des sous-agents = dépense ? » | essai b3 l. 532–556 ; l. 136 ; l. 331 ; l. 528 ; l. 620 | VÉRIFIÉ |
| J-16 | carte des hypothèses v1 hors de `main`, corrections annoncées, lemmes sans étiquette ; D-6 « non pour l'instant » | essai b3 l. 157, l. 604 | VÉRIFIÉ (dans l'essai) ; carte non lue |
| J-17 | « go » du pôle théorie le 27 octobre : « ne pas promettre de révolution, mesurer ce qui sort » ; questions ouvertes visées : agrégateur sous corrélation adverse, théorème négatif | PCO l. 18–19, l. 61–63 | VÉRIFIÉ |
| J-18 | règle « le rôle qui produit un artefact ne tient jamais la clé qui l'évalue » | programme v3 l. 81 | VÉRIFIÉ |
| J-19 | aucune partie de l'organisme ne produit de mathématiques nouvelles ; la couche 4 prévue vérifie | programme v3 l. 242–245 | VÉRIFIÉ (dans le programme) |
| J-20 | juge : richesse contre nul composite, seuil 1/α ; nul v9 : recombinaisons par morceaux à un niveau, borne de Ville tenue quel que soit le nombre de membres, preuve contre-lue et éprouvée sur mondes neufs | programme v3 l. 358, 375, 522 | RAPPORTÉ |
| J-21 | attaque A1 (proposeur qui lit la règle du juge, mondes où toute promotion est fausse) ; brèche de W2 sous v8 (42 des 48 lois promues = la loi du monde) ; règle de lecture gelée de la série d'attaques | programme v3 l. 513, 519, 521, 1227 | RAPPORTÉ |
| J-22 | nœud ouvert n° 2 : le sens de « rien au-delà de l'archive » ; une réponse contraire demanderait un nul v10 | programme v3 l. 534 | VÉRIFIÉ (dans le programme) |
| J-23 | niveau méthode, aucune recette (R-607) | programme v3 l. 28 | VÉRIFIÉ (dans le programme) |
| J-24 | citations obligatoires (POPPER, Dwork et al., Blum et Hardt, Co-Scientist) ; principe des attaques occupé depuis 2015, seule la forme revendiquée ; collision Qu, Chen et Wang | `decision-N-064-v1.md` l. 13–15 ; programme v3 l. 386–388 | VÉRIFIÉ (décision) ; RAPPORTÉ (collision) |
| J-25 | nouveauté du « nul formé des lois connues » à durcir (JUG-013, JUG-046) | programme v3 l. 1125, 1158 | RAPPORTÉ |
| J-26 | carte des hypothèses : 23 hypothèses, lemme maître L0 (invariance, proximité en variation totale, strate, impossibilité), 21 lemmes ; A7 plafond d'horizon ; A18 ; A13 sonde qui ne lit que l'indication | programme d'entretien v16 l. 386, 418–427, 437–438 | RAPPORTÉ (carte non lue) |
| J-27 | H2 : l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque | programme v3 l. 192 ; PCO l. 67 | VÉRIFIÉ (dans les pièces) |
| J-28 | matrice « statistique × union de classes d'écart » | programme d'entretien v16 l. 444–446 | RAPPORTÉ |
| J-29 | prédiction du papier C : juges génératifs à gain positif, agrégations robustes à gain nul ou négatif ; rôle 1 | programme v3 l. 1409 (PAC-002), l. 574 | VÉRIFIÉ (dans le programme) |
| J-30 | « δ > 0 sur organismes réels ? — lemme, ou théorème négatif », se tranche à G1 | programme d'entretien v16 l. 809 | RAPPORTÉ |
| J-31 | l'organisme n'est pas sur le chemin critique de G0 | programme v3 l. 589 | VÉRIFIÉ (dans le programme) |
| J-32 | question de Lazar du 31 octobre (concepts mathématiques inédits, Lean en soutien) ; couche 4 = pôle théorie et Lean, n'existe pas | `registres/decisions.md` l. 1149 (R-920) | VÉRIFIÉ |
| J-33 | témoin « un modèle, vote à k, coût apparié » | `decision-N-045-v2.md` l. 112 (et l. 69) | VÉRIFIÉ |
| J-34 | N-062 : l'échec de G1 commande la reconception, jamais l'arrêt sur un résultat négatif | `CLAUDE.md` l. 13 | VÉRIFIÉ |

Chiffres de la note qui ne sont pas des renvois : ceux du § 5, tous sortis de
`calculs-v1/sortie-ordres-de-grandeur-pilier-generation-v1.txt` (arrondis dans la note : 1,836 → ≈ 1,8 ; 11,104 → ≈ 11 ;
367,20 → ≈ 370 ; 2 220,80 → ≈ 2 220 ; 199,20 → ≈ 200 ; 532,20 → ≈ 530 ; 616,40 → ≈ 620 ; 2 953,00 → ≈ 2 950 ; 27,8 et
102,8 heures → ≈ 28 et 103 ; 2,78 → ≈ 3 ; 41,11 → ≈ 41 ; 133,61 → ≈ 134 ; 2,5 et 20 heures). Le verdict arrondit encore
(« ≈ 600 à 3 000 », « ≈ 3 à 130 »).

## 3. Choix du rédacteur (proposés, aucun dans les pièces lues)

1. Six maillons et leurs gardes (§ 2.1) ; classes E1 à E7 (§ 2.2) ; trois issues ACCEPTE, RÉFUTÉ, OUVERT.
2. Gardes G-V (témoin de non-vacuité), G-T (sonde de trivialité), G-C (contre-exemple exact), G-E (épreuve du contre-exemple
   déclaré), G-N (plancher mécanique de nouveauté).
3. Trois étiquettes de nouveauté, jamais « nouveau » ; banque B1 stratifiée (célèbre, obscur, publié après la date de coupure).
4. Utilité définie par des cibles formelles scellées avec table de décision.
5. Oracles B1 à B4 ; mondes mathématiques plantés (B3) comme oracle de composition ; mondes où toute promotion est fausse (B4)
   par cibles fausses plantées et archive complète.
6. Les cinq questions Q1 à Q5 et la cible d'étalonnage (score apparié de l'essai) ; le rattachement de Q3 à la prédiction du
   papier C (la prédiction porte sur des juges, Q3 sur un panel de moniteurs : rapprochement signalé comme tel).
7. Les conventions de Mathlib comme source d'infidélité (division par zéro, soustraction tronquée des entiers naturels, racine
   et logarithme hors domaine) : connaissance du rédacteur, **à vérifier sur la version épinglée**.
8. Placement : proposeurs dans l'organisme, arbitre et juges hors de l'organisme.
9. Prédiction du verdict, point 5 (SUPPOSÉ).

## 4. Hypothèses de chiffrage (toutes non vérifiées)

- Prix et profils de l'essai, repris tels quels avec leur statut (J-12).
- **S-01** plafond de 10 USD par énoncé neuf (choix de dessin) ; **S-02** proposition à 10 k d'entrée et 3 k de sortie ;
  **S-03** rétro-traduction au profil du relecteur de l'essai ; **S-04** une ou deux recherches de nouveauté à 8 k et 4 k ;
  **S-05** juge d'utilité, un appel à 6 k et 3 k ; **S-06** pilote de 200 candidats et 100 connus plantés, non dimensionné ;
  **S-07** attaque adaptative de 50 à 200 USD (ordre de grandeur, aucune pièce de dimensionnement) ; **S-08** 15 à 60 minutes
  de processus par énoncé, 5 par tricheur, 3 processus, 0,10 à 0,40 USD l'heure sans source, borne haute 1,30 (prix horaires de
  l'essai, § 4.5) ; **S-09** 5 % à 20 % des candidats franchissent toutes les gardes, 15 à 30 minutes de relecture chacun.

## 5. Exposition, cloison, interdits

- Aucun chemin des interdits communs ouvert : rien sous `diag/`, `runs/`, `donnees/`, `docs/notes/bras-attaque/`, aucune
  branche interdite, aucun item de l'étiqueteur. Aucune valeur de sonde de la course 7a sous mes yeux.
- **Recherches** : `grep` sur des fichiers nommés ; un `git grep -n -l "f7dfe5fd"` sur l'arbre de travail **avec exclusions**
  `docs/notes/bras-attaque`, `scripts/extraire_mesures_epreuve_t06_v1.py`, `diag`, `runs`, `donnees` (noms de fichiers
  seulement en sortie) ; `ls` de dossiers nommés (`docs/sources/`, `docs/sources/pdf/` filtré par noms, dossier de la
  consigne, dossiers de l'essai et du programme).
- **Git** : `git rev-parse`, `git log --oneline -3`, `git grep` (lecture) ; `git show` de la pièce PCO sur la branche
  `origin/canal/conv-audit-n04` (règle 4) ; aucune autre commande, aucune écriture git, aucun commit.
- **Carte des hypothèses v1** : **non ouverte** (hors de `main`, branche du canal ; hors de la liste de la consigne ; le
  rédacteur de l'essai ne l'avait pas ouverte non plus) ; tout ce qui la concerne est RAPPORTÉ par le programme d'entretien v16.
- **Exposition déclarée** : en contrôlant les lignes ajoutées au registre après ma lecture, le début de la ligne **R-2241**
  (« T0.7, brouillon 22 rendu », 200 caractères) et un fragment de **R-2242** (qui consigne le lancement de cette note) sont
  passés sous mes yeux ; rien n'en est repris ; aucune valeur numérique n'y figurait dans ce que j'ai vu.
- **Exécutions** : `.venv/bin/python -I -B` pour le calcul des ordres de grandeur et la table des empreintes (processeur ;
  le second lance `git show` en lecture) ; scripts de retouche et d'ajout de table dans le bac à sable
  (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/pilier-generation/`), non versés.
- Aucun appel de modèle ni d'interface, aucun réseau, aucune installation, aucune dépense, aucune suite d'essais lancée.
- Aucun refus de contrôle de permissions ni de classifieur. Une commande refusée par l'interpréteur (apostrophe dans une
  chaîne) a été refaite par un script, sans effet sur le contenu.
- **Écrit** : sous `docs/notes/ideation-organisme-v1/pilier-generation-v1/` seulement (note, journal, `calculs-v1/` : deux
  scripts et une sortie, et leurs compagnons) ; bac à sable.

## 6. Questions ouvertes

1. **Qui décide l'ouverture de la couche 4**, sur quelles pièces : non nommé par les espèces ni par les décisions lues.
2. **Date des résultats de l'étape 2** : aucune pièce lue ne la donne.
3. **Carte des hypothèses** : chemin de lecture sur `main`, version corrigée ; les formes de Q2 à Q5 en dépendent.
4. **N-053** : texte non lu ; son point 4 (juge d'une autre lignée) et son point 5 ne sont lus qu'à travers N-058 et le
   programme v3. L'acceptation par Lean comme signal d'entraînement d'un proposeur est-elle couverte par l'invariant ?
5. **Conventions de Mathlib** à la version épinglée : liste exacte à établir sur la chaîne installée (D-1a).
6. **Date de coupure** des modèles : une source lisible existe-t-elle pour la strate « publié après » de B1 ?
7. **Temps des sous-agents** : dépense ou non (question de l'essai, § 8, point 6) ; il conditionne le défaut de DP-6.
8. **Antériorités** du § 6.3 de la note : aucune lue ; noms donnés de mémoire.
9. **Inventaire** : la consigne nomme la v4 ; la v7 est la version finale (R-2221) ; la famille MAT de la v7 (8 entrées) est lue
   dans sa copie du programme v3. Rien dans la v4 ni dans la v7 ne parle de génération de mathématiques nouvelles au-delà de
   MAT-002 et MAT-008.
10. **Q1** : la clôture de l'archive (recombinaisons par morceaux à un niveau) est-elle définissable dans Lean sans
    reproduire tout le code du nul ? À poser au moment de la carte de cible.

## 7. Empreinte de la note (calculée au scellement)

| pièce | sha256 |
|---|---|
| `note-conception-pilier-generation-v1.md` | `94532165d1b80dd32832556f372e37dfe82b5c9af5c442193c4b43e7320fb44e` |
| `calculs-v1/ordres-de-grandeur-pilier-generation-v1.py` | `11c98699471539f2db5810c32144c8a8ceef098483e645096dfa82b4c83cb480` |
| `calculs-v1/sortie-ordres-de-grandeur-pilier-generation-v1.txt` | `c2240177a29a1b9374f3f08a67642a8ea5bb05d422073f51331e6b0370164f93` |
| `calculs-v1/table-empreintes-note-v1.py` | `1d65e917bbb06f76af53b1b0563cfc6d2a10907dcc125ec8ad7a0849d72e168e` |

Calculées par `sha256sum` au scellement, 14:28:45 UTC (heure relevée par `date -u`) ; chaque fichier a son compagnon `.sha256`.
