# Contre-lecture (règle R2) des commandes externes v5 de Kimi et d'Argon — tour fermé, étage 1

Contre-lecteur neuf (Opus 5.5, sous-agent), le 3 novembre 2026, de 07:37:57 à 08:17:25 UTC (heures relevées par `date -u`).
Je n'ai écrit ni les commandes, ni les essais, ni le banc, ni le LISEZMOI. Aucun appel payant, aucun modèle, aucun réseau hors de
127.0.0.1 (ports éphémères seulement ; le port 8805, occupé pendant ma lecture par une autre tâche, n'a jamais été touché), aucune
clé lue, cherchée ni affichée, aucun fichier existant modifié (`git status` de l'arbre vide avant et après), aucun commit, aucun
`.sha256` écrit, rien ouvert sous un dossier `donnees/` du disque (la v2 d'Argon a été lue par `git show` d'une branche : code seul).
Ce rapport est le seul fichier neuf de l'arbre ; il n'est ni scellé ni commis (session-depot le fera). Mes scripts, sorties et
dossiers de travail : `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/cl5-v5/` (`outils/`, `sorties/`,
`travail-*`) ; empreintes en section 9.

Objet : arbre `wt-commandes-tf`, branche `outils/commandes-tour-ferme-v1`, commit `f9da51b9`, dossier
`docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/`.

## 1. Verdict

**Scellable après corrections — aucune dans le code des deux v5.** La règle demandée est appliquée exactement : les deux
commandes ne sortent en code 4 qu'aux deux contrôles du plafond de session (`cause_refus = plafond_session`), et ces deux contrôles
ne sortent jamais autrement qu'en code 4 ; tout autre refus sort en code 3 au plancher, `envoye: false` ; la dernière ligne d'un
code 4 ne porte ni `modele_servi`, ni `refus`, ni `stop_reason` (I33). Lu dans le code (toutes les sorties), rejoué sur 27 cas par
la vraie commande de la configuration et l'adaptateur v64 (copie neuve de `eaa74ca`) : « budget_depasse » pour les deux seuls
`plafond_session`, « erreur » pour les 21 autres cas, jamais « refus ». Diffs v4 → v5 minimaux et exacts ; `servir` identique
à l'octet (bloc de 8 573 octets égal en v2, v3, v4 et v5). Essais : 136 passés sur 136 sous les deux interpréteurs.

**0 bloquant ; 2 majeurs ; 6 mineurs.**

- **CL5-01 (majeur)** — I34 et T128 : la v5 rend toujours en code 5 (arrêt de la course) une réponse coupée de
  l'expérimentateur et du vérificateur, ne contrôle pas la fenêtre et n'écrit pas la cause au registre ; le brouillon 7 annoncé
  par le n° 393 gèlera T128, qui exige le contraire : le constat A.6 bis sera non conforme. Décision à demander à conv-audit
  **avant** le brouillon 7 ; la réserve 1 du LISEZMOI attribue à « la demande » des mots (« avec seulement ») que le n° 393 ne
  contient pas — il renvoie au contraire à I33, I34 et T128.
- **CL5-02 (majeur)** — trois mutations neuves sur la règle survivent aux 136 essais (CL5-M1, CL5-M2b, CL5-M3b), et chacune
  recrée B11 : un 413 ou un 400 du relais, ou un 429 de Gemini, lu « budget_depasse » par la v64 (rejoué). La lecture statique
  se contourne par une constante nommée ; aucun essai ne fait passer un 400, 411 ou 413 par une commande, ni un échec de quota
  par Argon.
- Mineurs : CL5-03 (registre aux octets non UTF-8 : code 1 sans ligne, pas code 3), CL5-04 (`envoye: false` sur une erreur de
  Moonshot partie vers l'amont, et sens différent chez Argon), CL5-05 (réglages des relais : chiffres exacts, `--prix-cache`
  manquant, prix déjà accepté), CL5-06 (fenêtre : chiffres à compléter), CL5-07 (cause d'un arrêt : remède bon marché),
  CL5-08 (LISEZMOI : état et sources à remettre à jour).

Les corrections tiennent dans un LISEZMOI neuf (ou un addendum scellé), un constat A.6 bis v2, une décision de conv-audit et des
essais à ajouter à la version suivante des commandes, si elle se fait.

## 2. Pièces lues et empreintes

| pièce | vérification |
|---|---|
| les 7 fichiers v5 du dossier et leurs compagnons | `sha256sum -c` des 25 compagnons du dossier : 25 OK ; `EMPREINTES-commandes-tour-ferme-v3.txt` : 7 OK ; v1 : 8 OK ; v2 : 7 OK ; `commande_kimi_v5.py` `5d9d6620…`, `commande_argon_v56_nuit_v5.py` `0b52aba8…` (attendues) |
| base de comparaison | `commande_kimi_v4.py` `10afdab5…`, `commande_argon_v56_nuit_v4.py` `5c6d5149…`, LISEZMOI v2 `80370160…` (compagnons OK) ; v3 d'Argon `95fa4064…` |
| n° 393 de conv-audit, § 4 | `git show origin/canal/conv-audit-n04:…/conv-audit_2026-11-03_n393.md` : `49f5a8d1f0c0d7d010fdf2c1ddaffea064da677ec5f624278f0e8a428ae4e234` (attendue) ; lu en entier |
| contre-lecture courte du brouillon 6 | `ideation-organism`, `d54b85c` : `6c57a849af5f53932f497376508680b7aa0a3255cea0200b5e8675d3d6f7ba81` (aucun compagnon dans le dépôt à ce commit, vérifié) ; sections 0 à 5 lues, B11 l. 88-118, I33 l. 122-132, I34 l. 134-151, T115, T121, T126 à T128 l. 311-507 |
| brouillon 6 du préenregistrement | même commit : `cdcb44706e7b3c62ccd028680cf633c1651a56a93d7de129449150b47b45aef5` ; A.6 bis l. 857, plan et devis l. 130-150 et 560-588 |
| adaptateur v64 et classe gelée | copie neuve `git archive eaa74ca orchestrator/pole` dans un dossier vide : `diff -r` identique à la copie fournie (123 fichiers) ; `adaptateur_commande_v64.py` `adb73287…`, `adaptateurs.py` `a1a8ede8…`, `adaptateurs_v56.py` `d36c79b2…` ; lus : v64 en entier, `adaptateurs.py` l. 554-778, v56 l. 1-220, `tests_de_mort_v5.py` l. 380-415 |
| commande d'Argon v2 (sert le relais 8805) | `git show origin/donnees/recuperation-collisionneur-v8-v1:donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` : `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` (celle que cite l'en-tête de la v3) |
| relais Kimi | `relais-kimi-v1/relais_kimi_v3.py` `d54ed2bc…`, `relais_kimi_v4.py` `67f36951…` (compagnons et empreintes du dossier OK) ; lus : en-tête, `Bareme.pire_cas`, `Compteur`, refus et relais de l'amont (l. 251-335, 476-625) |
| n° 300 de session-depot | `origin/canal/session-depot-reprise-n130` : `c85a1807223196cdb5156cc18f02b76fd4e0028e6ba1b48dd7d0c1beeba09198` (la proposition de v5, § 3) |
| constat A.6 bis v1 | `docs/notes/ideation-organisme-v1/tour-ferme-etage1-v1/constat-a6bis-tour-ferme-v1.md` (dépôt de travail) : `61bc404bd2518dda6ecf7b8034e982db417f8390731cd4c74ec3205064147893` (compagnon égal) |

## 3. La règle à sa source, et le code (point 1)

**Source.** n° 393, § 4 : « le code 4 « rien envoyé » est réservé aux refus que la session porte en elle-même (`cause_refus =
plafond_session`, ou une consigne au-delà de la fenêtre d'entrée du modèle si la commande la contrôle) ; tout autre refus
(`relais_plafond`, `relais_max_appels`, `garde_etape`, `garde_cumulee`, `registre_illisible`, 402 et 429 du relais ou du
fournisseur) sort en code 3 au plancher, rien parti […] ; la dernière ligne d'un code 4 ne porte ni `modele_servi` (sauf
exactement le modèle demandé), ni `refus`, ni `stop_reason` (I33) ; garde `cause_refus` sur la ligne pour le registre et
l'audit ». B11 (l. 104-109) et I33 (l. 131-132) de la contre-lecture courte disent la même chose ; la v5 ne contrôle pas la
fenêtre, donc seul `plafond_session` peut sortir en code 4 — conforme.

**Code, toutes les sorties.** Kimi v5 : code 2 l. 280 ; **code 4 l. 289-290 et l. 298-299 seulement**, chacun avec
`cause_refus="plafond_session"` et les seules clés `texte` (vide), `cout_usd` (1e-6), `version`, `erreur`, `envoye` (faux),
`role`, `cause_refus` ; code 3 du registre l. 306-307 ; bloc des erreurs HTTP l. 330-341 (code 3, ou 5 pour un 502 ; la signature
ne décide plus que la cause, l. 338-339) ; relais absent et autres erreurs de transport l. 342-347 (3 ou 6) ; réponse l. 348-372
(5 ou 0) ; signal l. 319-320 (6). Argon v5 (`appeler`) : code 2 l. 455 et l. 565 ; **code 4 l. 459-461 et l. 463-465
seulement**, mêmes clés ; code 3 du registre l. 472-473 ; bloc HTTP l. 498-503 (toujours 3) ; transport l. 504-509 (3 ou 6) ;
échec de l'interface l. 519-521 (3) ; réponse l. 522-532 (5 ou 0) ; signal l. 485-486 (6). `fin` n'est jamais appelée avec 4 ;
aucune autre sortie de l'interpréteur ne vaut 4 (une exception non capturée sort en 1 : voir CL5-03). Aucun chemin ne sort
`plafond_session` en code 3 : les deux contrôles précèdent le registre et l'envoi. Les lignes de code 3 ne portent jamais
`modele_servi`, `refus` ni `stop_reason` (Argon retire `modele_servi` sur un échec, l. 520 ; Kimi ne pose `modele_servi` qu'en
code 5, l. 335-336) : la classe gelée les lit « erreur », pas « refus ».

**Rejoué** (section 5) : la lecture par la v64 de chaque cause, et des cas voisins, sur de vraies sorties.

## 4. Diffs v4 → v5 et sous-commande `servir` (point 2)

- `diff -u` refait par moi : corps identique aux deux patches livrés (111 et 116 lignes, 63 et 66 lignes changées, comme annoncé) ;
  `patch -o` sur des copies neuves des v4 : **égal octet pour octet** aux deux v5.
- Changements de comportement, et seulement eux : Kimi — `rendre(4 → 3)` des refus du registre (l. 307) et suppression du passage
  en code 4 d'un 402 ou 429 signé (l. 339 : la cause seule reste) ; Argon — `rendre(4 → 3)` du registre (l. 473) et
  `fin(4 if e.code in (402, 429) else 3 → 3)` (l. 502). Le reste : `VERSION`, commentaires, en-têtes, lignes d'usage (la première
  ligne de l'en-tête, description d'argparse, n'est affichée que par `--help`). Aucun autre champ de ligne, aucune garde, aucun pire
  cas, aucun registre ne change.
- `servir` : bloc entre les deux lignes-marqueurs **identique à l'octet (8 573 octets) en v2 (`221df610…`), v3, v4 et v5** ;
  `principal` et la fin du fichier identiques entre v4 et v5 ; au-dessus du bloc, seule `VERSION` change entre v3, v4 et v5 (et
  `ROLES` en plus depuis la v2, que `servir` ne lit pas). Script : `outils/bloc_servir_v1.py`. Le relais réellement servi en 8805
  (v2) se comporte donc comme celui que la suite joue.

## 5. Lecture par l'adaptateur v64 (point 3)

**Essais de la suite, rejoués** (commande du LISEZMOI, copie neuve sur `PYTHONPATH`, Python 3.13.18, pytest 9.1.1) :

| interpréteur des commandes | résultat | heures (`date -u`) |
|---|---|---|
| celui du dépôt (`.venv/bin/python`) | **136 passés, 0 échoué**, 75,75 s, code 0 | 07:46:07 → 07:47:23 |
| `PY_COMMANDES=/usr/bin/python3` (`-I -B`) | **136 passés, 0 échoué**, 78,95 s, code 0 | 07:47:23 → 07:48:42 |
| sans la copie du dépôt public (`-k v64`) | **25 erreurs, 0 sauté** (garde R5 de la suite : « copie … absente du PYTHONPATH ») | pendant mon banc de mutations (07:54:45 → 07:59:25) |

**Mon rejeu, indépendant de la suite** (`outils/rejeu_causes_v64_v1.py`, 07:52:49 → 07:53:04) : commande de la configuration
(options du LISEZMOI, `/usr/bin/python3 -I -B`, registre neuf par cas), faux relais local à moi, porte « environnement » réelle
(`ETAPE_POLE=tour_ferme_v64`, part 44.00 ou 6.00), modèle servi exigé, rôle de l'étage (Kimi expérimentateur à 0,80 USD, Argon
vérificateur à 0,10 USD), lecture par `AdaptateurCommandeExterneV64.lancer` de la copie neuve.

| cas | code | dernière ligne (`envoye` ; `cause_refus` ; coût) | lecture v64 | coût compté |
|---|---|---|---|---|
| Kimi `plafond_session` (plafond 0,02) | 4 | faux ; `plafond_session` ; 1e-6 | **budget_depasse**, `rien_envoye` | 0 |
| Kimi `garde_etape` (part presque épuisée) | 3 | faux ; `garde_etape` ; 1e-6 | erreur | 1e-6 |
| Kimi `garde_cumulee` (49,99 réglés) | 3 | faux ; `garde_cumulee` ; 1e-6 | erreur | 1e-6 |
| Kimi `registre_illisible` (ligne non JSON) | 3 | faux ; `registre_illisible` ; 1e-6 | erreur | 1e-6 |
| Kimi registre aux octets non UTF-8 | **1** | aucune ligne (trace Python) | erreur, coût inconnu | **0,80** |
| Kimi 402 signé du relais | 3 | faux ; `relais_plafond` ; 1e-6 ; registre `debut`, `fin` code 3 | erreur | 1e-6 |
| Kimi 429 signé du relais | 3 | faux ; `relais_max_appels` ; 1e-6 | erreur | 1e-6 |
| Kimi 429 de Moonshot transmis (quota) | 3 | faux ; — ; 1e-6 | erreur | 1e-6 |
| Kimi 402 de Moonshot transmis | 3 | faux ; — ; 1e-6 | erreur | 1e-6 |
| Kimi 400 de Moonshot transmis (fenêtre) | 3 | faux ; — ; 1e-6 | erreur | 1e-6 |
| Kimi 413 signé du relais | 3 | faux ; — ; 1e-6 | erreur | 1e-6 |
| Kimi 401 de Moonshot transmis | 3 | vrai ; — ; pire cas 0,162 | erreur | 0,162 |
| Kimi réponse coupée (`length`) | 5 | vrai ; — ; usage | erreur | 7e-5 |
| Kimi sain | 0 | vrai | ok | 7e-5 |
| Argon `plafond_session` (60 000 caractères) | 4 | faux ; `plafond_session` ; 1e-6 | **budget_depasse**, `rien_envoye` | 0 |
| Argon `garde_etape` | 3 | faux ; `garde_etape` ; 1e-6 | erreur | 1e-6 |
| Argon `garde_cumulee` | 3 | faux ; `garde_cumulee` ; 1e-6 | erreur | 1e-6 |
| Argon `registre_illisible` | 3 | faux ; `registre_illisible` ; 1e-6 | erreur | 1e-6 |
| Argon registre aux octets non UTF-8 | **1** | aucune ligne | erreur, coût inconnu | **0,10** |
| Argon 402 du relais | 3 | faux ; `relais_plafond` ; 1e-6 | erreur | 1e-6 |
| Argon 429 du relais | 3 | faux ; `relais_max_appels` ; 1e-6 | erreur | 1e-6 |
| Argon 429 de Gemini (échec rendu par le relais) | 3 | **vrai** ; — ; **pire cas 0,050** | erreur | 0,050 |
| Argon 413 du relais | 3 | faux ; — ; 1e-6 | erreur | 1e-6 |
| Argon réponse coupée (`TRONQUE`) | 5 | vrai ; — ; usage | erreur | 3,5e-4 |
| Argon sain | 0 | vrai | ok | 3,5e-4 |
| témoin v4 : Kimi 429 signé | 4 | faux ; `relais_max_appels` | budget_depasse | 0 |
| témoin v4 : Argon `garde_etape` | 4 | faux ; `garde_etape` | budget_depasse | 0 |

**Comptes : v5 — 2 « budget_depasse » (les deux `plafond_session`), 21 « erreur », 2 « ok », 0 « refus » ; v4 — 2
« budget_depasse » (B11 reproduit, R5).** Le motif d'un « erreur » est « commande externe : code 3 : » sans rien après (sortie
d'erreur vide), sauf le code 1 (trace Python).

## 6. Essais et mutations (point 4)

**Nature des essais.** Ce sont des essais de comportement : chaque commande est lancée en sous-processus comme en production
(`-I -B`, environnement minimal, consigne sur l'entrée standard) contre un faux relais local, avec le vrai registre gelé et, pour
25 d'entre eux, la vraie classe v64 ; `invariants_v5` contrôle la règle sur chaque sortie produite. Un seul essai lit le texte
(`test_code_4_seulement_aux_deux_controles_du_plafond_de_session`, module `ast`), en complément ; et `test_bloc_servir_identique_a_la_v4`
compare des octets (identité voulue).

**Mes mutations neuves** (`outils/mes_mutations_v1.py` : copie neuve des sept fichiers que copie le banc, remplacements exacts
— chaque motif présent une fois —, fichier muté relu par `ast.parse`, suite v5 avec `-x`, copie neuve de `eaa74ca` sur
`PYTHONPATH`) : 07:54:45 → 07:59:25 puis 07:59:50 → 08:02:26 UTC.

| id | fichier | mutation | sort | suite | premier essai qui échoue |
|---|---|---|---|---|---|
| CL5-M1 | Kimi | 400, 411 et 413 du relais rendus en code 4 par une constante nommée (`CODE_LIMITE = 4` ; l. 337 : `code = CODE_LIMITE if e.code in (400, 411, 413) else …`) | **SURVIT** | 136 passed in 76.33s | — |
| CL5-M2 | Argon | même chose, constante posée sous `PLANCHER` (au-dessus du bloc `servir`) | « tuée » pour une raison étrangère | 1 failed, 133 passed | `test_bloc_servir_identique_a_la_v4` (identité du prologue) |
| CL5-M2b | Argon | même chose, constante posée dans la partie `appeler` | **SURVIT** | 136 passed in 77.99s | — |
| CL5-M3 | Argon | échec de l'interface portant « 429 » rendu en code 4, `envoye` faux (constante sous `PLANCHER`) | « tuée » pour une raison étrangère | 1 failed, 133 passed | `test_bloc_servir_identique_a_la_v4` |
| CL5-M3b | Argon | même chose, constante dans `appeler` | **SURVIT** | 136 passed in 76.72s | — |
| CL5-M4 | Kimi | relais absent (connexion refusée) rendu en code 4 par une constante nommée (témoin) | tuée | 1 failed, 83 passed in 50.62s | `test_cause_refus_absente_hors_des_six_refus[kimi]` |

**Conséquence des survivantes, rejouée** par mon rejeu sur leurs dossiers mutés (08:00:01 → 08:03:27) : CL5-M1 — 400 de Moonshot
(fenêtre) et 413 du relais Kimi → code 4 → **« budget_depasse »**, coût compté 0 (v5 : 4 « budget_depasse » au lieu de 2) ;
CL5-M2b — 413 du relais Argon → « budget_depasse » ; CL5-M3b — 429 de Gemini → « budget_depasse », coût déclaré 0,050 USD
compté 0 alors que l'appel est parti. Chacune recrée B11 (fin des tours silencieuse) sans qu'un des 136 essais échoue.

**Banc livré, rejeu partiel** (mutations propres à la règle R1 à R20 et X5, `--seulement`, fichiers temporaires dans mon dossier) :
21 mutations jouées (08:03:42 → 08:16:48 UTC ; cas sain d'abord : 136 passed in 77.98s) : **21 tuées sur 21**, chacune par
le même premier essai que la table du LISEZMOI (par exemple R1 `test_registre_cumule_plein_code_3[kimi]`, R3
`test_six_causes_code_ligne_et_registre[kimi-relais_plafond]`, R6 `test_sortie_minimale_du_lecteur_est_la_sienne[kimi]`, R20
`test_plafond_session_second_controle_code_4[kimi]`) ; code 0. Les 70 autres mutations du banc ne sont pas rejouées ici.

## 7. Les réserves du LISEZMOI (point 5)

Le LISEZMOI en numérote neuf : sept de fond (1 à 7), deux de procédure (8, 9).

1. **I34** — exacte sur le fond (rejoué : `length` chez Kimi, `TRONQUE` chez Argon → code 5 → « erreur ») ; **source inexacte** :
   les mots « avec seulement » ne figurent pas au n° 393 (0 occurrence, `49f5a8d1…`), qui répond « Oui à ta v5 » à la proposition du
   n° 300 (« une v5 des commandes qui rendrait les refus 402 et 429 des relais en code 3 ») et demande de lire « aussi I33, I34 et le
   couple T128 » ; le brouillon 7 annoncé (« brouillon 6 + couples T113 à T128 ») gèlera T128. → CL5-01.
2. **Fenêtre** — exacte. Chiffre refait avec les fonctions mêmes de la commande : **378 402** caractères ASCII au plus à 0,80 USD
   (344 002 pour un texte avec un caractère accentué sur dix, 369 173 avec une fin de ligne sur quarante) ; une consigne de
   393 000 caractères est refusée en code 4 (`plafond_session`). À compléter → CL5-06.
3. **Cause à la seule dernière ligne** — exacte (rejoué : motif vide après « code 3 : ») ; remède bon marché possible → CL5-07.
4. **Prix et réglages des relais** — chiffres exacts, recalculés ; prix déjà accepté par écrit ; `--prix-cache` manquant → CL5-05.
5. **402 et 429 de Moonshot en `envoye: false`** — exacte mais incomplète et trompeuse pour l'audit de la dépense → CL5-04.
6. **Effets dans l'étage non rejoués** — exacte ; je n'ai rejoué que l'adaptateur et la porte, moi aussi (le motif d'un « erreur »
   va bien à `journal["arret"]`, `pole/tests_de_mort_v5.py` l. 411-412, lu).
7. **Copie du dépôt public à refaire** — exacte ; refaite (copie neuve égale, garde R5 de la suite constatée : 25 erreurs).
8. **Contre-lecture à faire** — c'est ce rapport.
9. **Rien de commis ni de scellé** — vrai à l'écriture (07:34), dépassé : `f9da51b9` (07:37:09 UTC) commet les huit fichiers (les sept v5
   et l'empreinte v3) et leurs huit compagnons `.sha256` → CL5-08.

Il manque : le registre aux octets non UTF-8 (CL5-03) ; la différence de sens de `envoye` entre Kimi et Argon pour une erreur du
fournisseur (CL5-04) ; l'absence d'essai pour les autres refus du relais (CL5-02).

## 8. Constats

### CL5-01 — majeur — I34, fenêtre et cause au registre : la v5 ne tiendra pas le constat A.6 bis que T128 fera geler

- Fichiers : `commande_kimi_v5.py` l. 366-367 (`finish_reason` « length » → code 5) ; `commande_argon_v56_nuit_v5.py` l. 527-529
  (`TRONQUE` → code 5) ; `LISEZMOI-commandes-tour-ferme-v3.md` l. 339-343 (réserve 1), l. 344-348 (réserve 2), l. 349-355 (réserve 3).
- Fait : T128 (contre-lecture courte, l. 506) demande à la session-depot de vérifier que, pour `experimentateur_test` et
  `lecteur_test`, une réponse coupée est rendue en code 0 avec son texte, son coût et `modele_servi`, « et jamais en code non nul,
  qui arrêterait la course » ; que la plus longue consigne tient dans la fenêtre ou que la commande la refuse en code 4 ; de
  préférence que la cause soit « écrite aussi à son registre » (T128 nomme la clé `cause`, le n° 393 et les commandes `cause_refus`).
  Le n° 393, § 4, renvoie à I34 et T128 et annonce le brouillon 7 = brouillon 6 + T113 à T128. La v5 ne fait aucun des trois.
  Rejoué : réponse coupée → code 5 → « erreur » (arrêt de la course entière, propositions déjà payées), pour Kimi comme pour Argon.
- Pourquoi c'est majeur : le risque n'est pas théorique — le vérificateur est borné à 1 000 jetons de sortie
  (`--max-sortie-lecteur 1000`), et la commande d'Argon compte les jetons de raisonnement dans la sortie (`thoughtsTokenCount`,
  en-tête l. 152-154) : si la borne de sortie les comprend aussi, 1 000 jetons peuvent ne pas suffire à un modèle qui raisonne ; l'expérimentateur, en fin de borne, descend jusqu'à 4 096 jetons, raisonnement compris dans
  `completion_tokens` (en-tête de Kimi l. 121-124). I34 le disait déjà ; la v5 garde ce risque d'arrêt sans le faire décider.
- Correction proposée : (1) **avant le brouillon 7 et la configuration**, porter à conv-audit une décision en une phrase :
  (a) une v6 des deux commandes qui rend en code 0 la réponse coupée de `experimentateur_test` et de `lecteur_test` (texte, coût,
  `modele_servi`, `finish_reason` ou `fin` gardés ; le proposeur reste en code 5, A.5), avec ses essais et mutations — recommandée,
  confiance moyenne à élevée ; ou (b) l'arrêt accepté par écrit et T128 récrit en conséquence ; dans les deux cas, dire au constat
  A.6 bis v2 ce qui est tenu pour la fenêtre (CL5-06) et pour la cause au registre (CL5-07) ; (2) dans le LISEZMOI neuf, retirer
  « hors de la demande : « avec seulement » la règle » et citer la source exacte (n° 300 § 3, n° 393 § 4).

### CL5-02 — majeur — trois mutations neuves sur la règle survivent ; la lecture statique se contourne

- Fichiers : `test_commandes_tour_ferme_v5.py` l. 819-833 (seuls un 403 et le relais absent sont joués comme « autres codes 3 »),
  l. 919-939 (seul un échec « TimeoutError » est joué chez Argon), l. 1289-1299 (411 et 413 envoyés à la main au relais, jamais lus
  par `appeler`), l. 1029-1038 (`_constantes` rend l'ensemble vide pour tout nom, l. 1036-1037) ; `mutations_commandes_tour_ferme_v5.py`
  l. 294 (« tuée » = tout échec, sans raison attendue).
- Fait : CL5-M1, CL5-M2b, CL5-M3b survivent (136 passés chacune) ; leur conséquence rejouée est exactement B11 (section 6). Le
  LISEZMOI (l. 117-118) affirme que `cause_refus` est absente des autres codes 3 « relais absent, 400, 403, 411, 413, échec de
  l'interface » : vrai à la lecture du code et à mon rejeu, mais la suite ne l'éprouve que pour 403, le relais absent et un échec de
  transport. CL5-M2 et CL5-M3 montrent aussi que toute mutation posée dans le prologue d'Argon est « tuée » par l'essai d'identité
  de `servir`, quel que soit son effet : le banc ne vérifie pas la raison.
- Effet aujourd'hui : aucun (le code v5 est juste) ; demain : une v6 (CL5-01) touchera le même bloc de lecture de la réponse.
- Correction proposée (version suivante de la suite et du banc) : faire passer par chaque commande, contre le faux relais, les
  statuts 400, 403, 411, 413 (signés et non signés chez Kimi), 500, 503 et 504, et chez Argon un échec portant 429 ou
  `RESOURCE_EXHAUSTED` : code 3 (ou 5 pour 502), jamais 4, `cause_refus` absente ; plus simplement, une boucle sur tous les statuts
  de 400 à 599 hors 402, 429 et 502 ; faire résoudre par `_constantes` les constantes de module (ou refuser tout nom autre que
  `code`) ; vérifier au banc l'essai attendu de chaque mutation (comme `--raisons` du banc v64) ; ajouter CL5-M1, CL5-M2b et
  CL5-M3b au banc.

### CL5-03 — mineur — un registre aux octets non UTF-8 sort en code 1, sans ligne, plafond de session compté

- Fichiers : `registre_depense_cumulee_v1.py` l. 57-64 (la lecture des lignes est hors du `try`, qui ne prend que `json.loads` ;
  `UnicodeDecodeError` n'est pas `RegistreIllisible`) ; `commande_kimi_v5.py` l. 306 et `commande_argon_v56_nuit_v5.py` l. 472
  (seules `PlafondCumule`, `RegistreIllisible` et `OSError` sont prises).
- Fait (rejoué, v5 et v4) : code 1, sortie standard vide, trace Python sur la sortie d'erreur ; la v64 lit « erreur », coût
  inconnu, plafond de session compté (0,80 ou 0,10 USD). C'est bien un arrêt (le sens voulu par B11), jamais un code 4 ; mais ni
  code 3 au plancher ni `cause_refus`, contrairement à la lettre du n° 393 et à la table du LISEZMOI (l. 112 : « ligne illisible »
  → code 3). Même famille, non rejouée : toute autre exception d'un registre corrompu (par exemple une étape non hachable).
- Probabilité : très faible (registre neuf, écrit sous verrou par les deux seules commandes).
- Correction proposée : sans code, l'écrire au LISEZMOI neuf et au constat A.6 bis v2 comme résidu accepté ; dans une v6,
  prendre aussi `ValueError` (et toute exception de `reg.reserver`) comme `registre_illisible`, code 3 au plancher, avec un essai.

### CL5-04 — mineur — `envoye: false` sur une erreur de Moonshot partie vers l'amont ; sens différent chez Argon

- Fichiers : `commande_kimi_v5.py` l. 333 (`avant_amont` : 400, 402, 403, 411, 413, 429, quel que soit l'émetteur) ;
  `relais_kimi_v3.py` l. 30-31 (une erreur de l'amont est relayée telle quelle, statut et corps) et l. 590-595 (coût lu dans son
  usage, sinon pire cas) ; `commande_argon_v56_nuit_v5.py` l. 519-521 ; LISEZMOI l. 363-364 (réserve 5).
- Fait (rejoué) : 400 (fenêtre), 402 et 429 de Moonshot → code 3, `envoye: false`, 1e-6 compté par le noyau et le registre, quand
  la consigne est partie chez Moonshot et que le relais compte le pire cas ; chez Argon, le même événement (429 de Gemini) revient
  en échec → code 3, `envoye: true`, pire cas compté. La lettre du n° 393 (« 402 et 429 … du fournisseur … au plancher, rien
  parti ») est suivie chez Kimi ; Argon, qui ne voit pas le statut du fournisseur, garde le sens prudent. Aucun effet sur la lecture
  v64 (code 3 = « erreur »). Effet sur l'audit : pour l'appel qui arrête la course, trois compteurs divergent d'au plus le plafond de
  la session (relais : pire cas ; registre et noyau : 1e-6) et `envoye` y dit « rien parti » à tort.
- Correction proposée : au LISEZMOI neuf et au constat A.6 bis v2, écrire que, sur un code 3, `envoye: false` veut dire « compté
  au plancher par la commande », non « rien n'est sorti du relais » ; étendre la réserve 5 aux 400, 403 et 413 non signés ; dire le
  cas d'Argon ; l'audit de la dépense se fait au compteur et au journal du relais (`GET /relais/etat`, `statut_amont`) et à la facture
  du fournisseur. Aucun changement de code sans décision (la lettre du n° 393 veut « rien parti »).

### CL5-05 — mineur — réglages des relais : chiffres exacts, `--prix-cache` manquant, prix déjà accepté

- Fichiers : LISEZMOI l. 356-362 (réserve 4) ; constat A.6 bis v1 (`61bc404b…`) l. 23-26 ; `relais_kimi_v3.py` l. 45, 139-143,
  227, 718, 750.
- Recalcul, depuis le brouillon 6 : maximum de l'étage 144 cartes et témoins testés = 36 + 36 + 24 + 6 témoins × 8 passes (l. 588) ;
  **Kimi 1 731 = 3 propositions + 12 sessions × 144** ; **Argon 147 = 3 + 144** (A.6 bis, l. 857) : exacts. Plafond du relais Kimi
  ≥ 44 + `--reserve-par-appel` : la dépense vue du relais reste ≤ 44 USD (parts du noyau) et chaque appel réserve
  max(0,40 ; pire cas) avec dépense + pire cas ≤ 44, donc dépense + réserve ≤ 44,40 : **suffisant et exact** si le relais compte
  comme la commande (même formule de pire cas, `Bareme.pire_cas` l. 251-259, au barème 2 et 10) ; la marge d'≈ 1 USD couvre les
  jetons hors compte. Argon ≥ 6 : exact au rond près (relais non arrondi, commande à 10⁻⁸, tolérance 10⁻⁹) ; le constat v1 dit 10.
- Manques : `--prix-cache` est obligatoire au relais Kimi (sans défaut : refus de démarrer, code 2 ; l. 45, 750) et doit valoir au
  plus 2 (I1 de la contre-lecture v4) ; ni la réserve 4 ni le constat v1 ne le donnent ; `--modeles-permis kimi-k3.1-pro` non plus.
  La réserve 4 dit le prix de B11 « à accepter par écrit » : il l'est (n° 393, § 4 : « Prix accepté par écrit »).
- Correction proposée : constat A.6 bis v2, pour les v5 : chemins et empreintes v5, règle B11 et I33, réglages complets des relais
  (`--prix-entree 2 --prix-sortie 10 --prix-cache` ≤ 2, `--modeles-permis`, `--plafond-usd` ≥ 44,40 et ≥ 6, `--max-appels`
  ≥ 1 731 et ≥ 147), relevé `GET /relais/etat` avant le premier appel.

### CL5-06 — mineur — fenêtre d'entrée : réserve exacte, chiffres à compléter

- Fichiers : LISEZMOI l. 93-96 et l. 344-348 ; `relais_kimi_v3.py` l. 142.
- Fait : limite refaite (section 7, point 2) ; le relais Kimi porte lui-même, comme borne haute « à revoir », une fenêtre annoncée
  de 262 144 jetons pour les modèles Kimi récents (l. 142) : une consigne acceptée par la commande (au plus 378 496 octets de corps)
  ne la dépasse que si le texte fait en moyenne moins de ≈ 1,45 caractère par jeton ; au-delà, l'erreur de Moonshot reviendrait
  vraisemblablement en 400 relayé → code 3, `envoye: false` (cas rejoué) → arrêt. Pour Argon, la borne de session (≈ 27 000
  caractères au vérificateur) rend la question sans objet.
- Correction proposée : donner ces chiffres au constat A.6 bis v2 avec la fenêtre documentée du modèle servi, et ranger la décision
  avec CL5-01.

### CL5-07 — mineur — cause d'un arrêt : la réserve 3 est exacte, un remède sans registre v2 ni v65 existe

- Fichiers : `pole/adaptateurs.py` l. 752-753 (le motif d'un code non nul porte les 300 premiers caractères de la sortie d'erreur) ;
  `pole/tests_de_mort_v5.py` l. 411-412 (ce motif va à `journal["arret"]`) ; test l. 808 (`err == ""` exigé pour les six causes).
- Fait : les commandes laissent la sortie d'erreur vide ; le motif rendu est « commande externe : code 3 : » sans rien après
  (rejoué) ; la cause d'un arrêt n'est donc ni au relevé, ni au registre pour les quatre refus d'avant l'envoi.
- Correction proposée : dans une v6, écrire avant chaque sortie en code 3 une ligne courte sur la sortie d'erreur
  (`cause_refus=…` et le motif borné, jamais de texte de consigne) ; la classe gelée la met au motif, l'étage au relevé ; l'essai
  des six causes changerait en conséquence. À défaut, le dire au constat (la cause n'est lisible qu'à la dernière ligne, perdue).

### CL5-08 — mineur — LISEZMOI : état et sources à remettre à jour

- Fichier : `LISEZMOI-commandes-tour-ferme-v3.md` l. 4-6 et l. 370 (« Rien n'est scellé, rien n'est commis… aucun fichier
  `.sha256` créé » : dépassé à `f9da51b9`) ; l. 339 (« avec seulement », CL5-01) ; l. 356 (prix « à accepter », CL5-05) ; T128
  nomme `cause`, la v5 `cause_refus` (à dire).
- Correction proposée : LISEZMOI v4 (fichier neuf, R12) ou addendum scellé, qui porte aussi CL5-01 à CL5-07.

### Remarques sans correction

- Le code 4 `plafond_session` dépend aussi des options de la commande (sortie minimale, prix) : une option mal réglée donnerait des
  refus d'apparence légitime, donc des fins de tours ; les options sont gelées par l'empreinte de la configuration, et l'audit S6
  (T115) attrape une fin des tours au premier tour.
- Le passage d'un 402 ou 429 du relais du code 4 au code 3 change le prix d'un vérificateur (témoin « non concluant » en v4, arrêt en
  v5) : c'est le prix accepté au n° 393.

## 9. Ce qui reste, dans l'ordre

1. Décision de conv-audit sur CL5-01 (v6 pour les réponses coupées, ou arrêt accepté et T128 récrit) **avant** le brouillon 7.
2. Session-depot : LISEZMOI neuf ou addendum (CL5-01 à CL5-08) ; constat A.6 bis v2 pour les v5 (CL5-03 à CL5-07) ; si une v6 se
   fait, les essais et mutations de CL5-02 dans la même version.
3. Au lancement : réglages complets des relais (CL5-05), relevés `GET /relais/etat` avant et après.

Aucun point de ce rapport ne demande d'appel payant.

**Empreintes de mes pièces** (hors du dépôt, dossier `/tmp/claude-0/-home-user/70605ed3-c649-5b49-861d-ab74970b173c/scratchpad/cl5-v5/`) :
- `outils/bloc_servir_v1.py` : `af0302765b7ed84a2fa0fa64a80070793809dc41d725769e4c7ee16d54eb6d20`
- `outils/rejeu_causes_v64_v1.py` : `c8815ee79905a5810d2628036692fb3bfe579507d58e9ba5ebce539433e75080`
- `outils/mes_mutations_v1.py` : `5bc76b329b38229f8ad52bc7d7f8ef070181b3645ce3a1143735525fa684b444`
- `sorties/pytest-v5-depot.txt` : `615db15f7e1dfa79ce37b318ea6a38b005b81623c44fb393215d27ac2726f03e`
- `sorties/pytest-v5-usr-bin.txt` : `a9e7876fb8d94d9b9a60cdc7c53d9fbe386550af4c1dc62b7738cb2e44898972`
- `sorties/pytest-v64-sans-copie.txt` : `2f87233ef6e65c42e57e720ceb53163a03be5366ce0e5ee42626854002ad2aef`
- `sorties/rejeu-causes-v64.txt` : `c78380bba2051ac108917aa9b05de15629fe4fce1477302c7e933d839beaff32`
- `sorties/mes-mutations.txt` : `e2755fa019d1941996d3bd0b70dff93c90c5dc9a52f1a8a06731c81964f78b20`
- `sorties/mes-mutations-b.txt` : `1f045cb8fba64c81d0582d73cb851289f1fb5ef5f2b17386ddbc7befad3e9b4a`
- `sorties/rejeu-M1-v64.txt` : `140e127643f1101a88c8856e2f1c0bb1158a9bad743fd19f5dcd7a3a4accd09e`
- `sorties/rejeu-CL5-M2b-v64.txt` : `6364a37dfeff2c0c27c3b799076fadef1d76830cbb461eddf473596923bd99c4`
- `sorties/rejeu-CL5-M3b-v64.txt` : `fb9de05b5d21c1ca74cbb32fb4b53ed6e15d6f2e7b8503419d0e26fc23f71f76`
- `sorties/banc-v5-R1-R20-X5.txt` : `99e8df5f9799c1134e25595f5f33e49577406915dd3ddf7184109a724b373cdc`
