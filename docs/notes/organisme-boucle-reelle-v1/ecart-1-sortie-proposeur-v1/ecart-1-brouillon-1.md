# Écart 1 au texte scellé de la course réelle de l'organisme — sortie du proposeur — brouillon 1 (non scellé, non contre-lu)

**Statut : brouillon 1, non scellé, non contre-lu (règle R2 à faire par un sous-agent neuf), non soumis.** Écart écrit au
préenregistrement scellé `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v1.md`
(`46d7545b489a2037ede235d843ef8a0c504461a0a2d697af5db40de2400fd89d`). Un écart à un texte scellé est un nœud de décision :
rien ne se relance avant la contre-lecture, le scellement du texte neuf et une ligne de GO inscrite par Lazar.

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère `session_01VJdZpSMxSdk2SJ1ScmdfNv`
  (préparation confiée en R-2422) ; n'a écrit ni le texte scellé, ni le code v65 ou v66, ni leurs contre-lectures, ni le
  devis, ni les rapports de course. Aucun appel payant, aucune machine, aucune clé lue ; rien écrit dans `registres/`.
- **Heures** (temps universel, `date -u`) : tâche commencée vers 08:50 (heure non relevée), vérifications hors ligne à 08:57:15, texte écrit ensuite,
  le 12 novembre 2026.
- **Arbres lus** : dépôt de travail, `main` à `4ef91270` ; branche de données `origin/donnees/course-organisme-v66-poste-local-v1`
  à `24c25908` ; arbre de l'organisme reconstruit dans un dossier jetable : `94bfd92` (dépôt public) → paquet v65
  `organisme-v65-boucle-reelle-v2.bundle` (`4660197e…`, branche `prep/organisme-v65-v1`) → paquet v66
  `code-v66/organisme-v66-boucle-reelle-v1.bundle` (`84ab119f…`), tête `7e415cbaaa3ff602db43a44dad6b4307c08352c7`, `git bundle
  verify` des deux.

## 0. En bref

1. La borne qui a coupé Kimi n'est pas `--max-sortie-proposeur` (65 536, jamais atteinte) mais **le plafond de session du
   proposeur, 0,50 USD**, qui fixe `max_tokens` = 46 714 pour un corps de 15 405 octets (section 2).
2. La configuration v7 relève ce plafond à **1,50 USD** et la borne de sortie de Kimi à **131 072 jetons** (valeur par défaut
   documentée de `max_completion_tokens` pour `kimi-k3.1-pro` ; maximum documenté 1 048 576, incompatible avec la part de
   Kimi au pire cas, section 8). Le lanceur v66 l'accepte **sans changer le code**, sous un texte neuf dont le plan gelé la
   nomme (vérifié hors ligne, section 9).
3. **Réserve bloquante sur l'effet** : le code gelé v66 arrête toute commande externe à **1 800 s**
   (`pole/adaptateurs.py` l. 622, `DELAI_COMMANDE_S`), et `commandes_v64` (`pole/adaptateur_commande_v64.py` l. 166) reconstruit
   l'adaptateur sans lui passer `fournisseurs.<nom>.delai_s` : ce délai ne se règle pas par la configuration. La commande de
   Kimi s'arrête elle-même à 1 750 s. Au débit observé (46 714 jetons en 1 552,967 s, ≈ 30,1 jetons par seconde), un appel
   tient au plus **≈ 52 600 jetons** en 1 750 s. La v7 seule déplace donc la coupure des jetons vers la durée : elle ne donne
   qu'≈ 12 % de marge au proposeur. Lever vraiment la borne demande un changement du code gelé (option 2, section 11).
4. Critères de lecture : **aucun changement**. Dépense : pire cas des modèles sous les bornes **39,00 USD** (Kimi 32,30 ;
   Argon 6,70) contre 35,30 en v6 ; la ligne de 45 USD suffit, son montant ne change pas. Ligne de GO neuve proposée,
   **GO-2026-11-12-06** (identifiant provisoire), qui nomme la configuration v7, sans cumul (section 10).

## 1. Motif

- **Rapport de la course 2** : `docs/notes/organisme-boucle-reelle-v1/course-v66/rapport-course-v66-poste-local-v2.md`, branche
  `donnees/course-organisme-v66-poste-local-v1` (tête `24c25908`), empreinte
  **`89b97faf2c7ec75350e44cd8b0ba3283645c84d47fa495350a8429206c407f28`** (vérifiée contre son compagnon). Lanceur code 3 au premier
  appel ; amont Kimi 200 après 1 552,967 s ; **46 714 jetons de sortie dont 46 711 de raisonnement** ; `finish_reason` « length » ;
  commande Kimi v6 code 5 (« réponse tronquée ») ; garde 13 ; issue C5 « non jugeable (arrêt) » ; 0,481706 USD.
- **Journal du relais** (même branche, `course-v66/poste-local-v2/journaux/journal-kimi.jsonl`) : `octets_corps` 15 405,
  `reserve_usd` 0,499998, `completion_tokens` 46 714, `reasoning_tokens` 46 711, `prompt_tokens` 7 283.
- **Registre** : R-2422 (`registres/decisions.md`) ; demande de Lazar dans la session du poste, verbatim : « enleve le plafond max
  tokens et relance » ; non exécutée par le poste, à juste titre (configuration v6 gelée par le bloc `plan-gele-v66`, section 16,
  et par les conditions de GO-2026-11-10-11).
- **Hypothèse du devis réfutée** : `devis-boucle-reelle-organisme-v1.md` (`60643868…`), ligne 36, comptait pour le proposeur
  Kimi 3 000 jetons de sortie « jusqu'à 15 000 s'il raisonne longuement ». Observé : plus de 46 711 de raisonnement sans
  réponse.

## 2. Comment la borne est calculée (code lu)

| maillon | où | ce qu'il fait |
|---|---|---|
| plafond de session des proposeurs | configuration v6, `plafonds_session.proposeur` = 0,5 | lu par `reglages_de_configuration` (`demonstrations/attaque_goodhart_v2.py` l. 212-230) comme « budget par appel », le **même pour Kimi et Argon** ; passé à `ProposeurAdaptateur` (`demonstrations/tour_ferme_v64.py` l. 288 et 301) |
| variable de la commande | `pole/adaptateurs.py` l. 659 | `PLAFOND_SESSION_USD` = ce budget |
| borne de Kimi | `commande_kimi_v6.py` (`889309305aeb…`) l. 229-233 et 315-335 | `max_tokens` = min(`--max-sortie-proposeur`, (plafond − (octets du corps + 1 024) × prix d'entrée) / prix de sortie) ; refus sous `--sortie-min-jetons` (4 096) ; jetons de raisonnement compris dans `completion_tokens` |
| prix de Kimi | défauts de la commande (`--prix-entree 2`, `--prix-sortie 10`, non passés par la configuration) ; relais `--prix-entree 2 --prix-sortie 10 --prix-cache 2` (section 12.3 du texte scellé) | 2 et 10 USD par million de jetons, du devis, « à vérifier » ; cache compté au prix d'entrée |
| calcul de la course 2 | | (0,5 − 16 429 × 2·10⁻⁶) / 10⁻⁵ = **46 714** : la borne atteinte, au jeton près |
| borne d'Argon | `commande_argon_v56_nuit_v6.py` (`5eae1a04…`) l. 234, 492-494 | `max_tokens` = min(`--max-sortie-proposeur` 32 000, (plafond − caractères / 3 × 10·10⁻⁶) / 50·10⁻⁶) |
| délai | `pole/adaptateurs.py` l. 622 et 735 ; `pole/adaptateur_commande_v64.py` l. 166 ; `demonstrations/ideation_v8.py` l. 72 | l'adaptateur v56 est d'abord construit avec `fournisseurs.<nom>.delai_s`, puis `commandes_v64` le remplace par un adaptateur v64 **sans** ce délai : défaut de classe, 1 800 s, groupe de processus tué (SIGKILL) au-delà ; la commande de Kimi s'arrête elle-même à `--delai-s` 1 750 (code 6, coût compté au pire cas réservé) |

Mesure hors ligne (faux relais local, aucun appel ; `verifications-v1/mesurer-max-tokens-kimi-v6-v7-v1.py`, sortie
`verifications-v1/sortie-mesure-max-tokens-v1.txt`) : sous v6, corps de 15 424 octets → `max_tokens` 46 710 (la course 2 :
46 714 pour 15 405 octets) ; corps de 17 919 octets (génération 2, estimé du devis) → 46 211. Sous v7 : 131 072 pour les
deux, pire cas réservé 1,343618 et 1,348608 USD.

## 3. Changement exact (configuration v6 → v7)

Dossier de course v7 : `ecart-1-sortie-proposeur-v1/configuration-v7/` = `configuration-boucle-reelle-v7.json`
(**`e45f3a7199c5d16428a3b4f2b31f1b18ee82594cabbf2b5ec26a6168b1655df6`**) + `pieces/` et `commandes-v6/` **copiés à l'octet** du
dossier v6 (neuf fichiers, empreintes vérifiées contre leurs compagnons). Produite par
`verifications-v1/faire-configuration-v7-v1.py` à partir du fichier v6 (`4743ddbe…`), même sérialisation (JSON, retrait 1,
caractères non échappés, fin de ligne finale). `diff` v6 → v7, trois lignes :

```
2c2   "_lisez_moi": texte v6 → texte v7 (dit le motif, les deux changements et la réserve du délai)
165c165
<   "proposeur": 0.5,
>   "proposeur": 1.5,
252c252   (fournisseurs.kimi.commande, valeur de --max-sortie-proposeur)
<     "65536",
>     "131072",
```

Effets, valeur par valeur :

| valeur | v6 | v7 | effet |
|---|---|---|---|
| `max_tokens` du proposeur Kimi (génération 1 ; 2) | 46 714 ; ≈ 46 211 | 131 072 ; 131 072 | borne de jetons relevée ; borne effective = durée (≈ 52 600 jetons en 1 750 s au débit observé) |
| pire cas réservé d'un appel du proposeur Kimi | 0,50 USD | 1,344 ; 1,349 USD | réservé au registre et au relais ; réel ≤ ≈ 0,56 USD tant que la durée borne |
| `max_tokens` du proposeur Argon (consigne de 13 552 ; 15 730 caractères, devis) | 9 096 ; 8 951 | 29 096 ; 28 951 | **effet de bord dit** : Argon partage le plafond de session ; pire cas 1,50 USD par appel |
| expérimentateur Kimi, vérificateur Argon | 0,80 et 0,10 USD par carte | inchangés | code gelé (`BUDGET_EXPERIMENTATEUR_PAR_CARTE_USD`), non touché |

Valeurs choisies : **131 072** est la valeur que Moonshot applique quand on ne borne pas (`max_completion_tokens`, documentation
versée `docs/notes/ideation-organisme-v1/relais-kimi-v1/doc-moonshot-lue-2026-10-30-v1/api_chat.md`, `67b8b5fd…`, l. 1081-1096 ;
`guide_kimi-k3-1-pro-quickstart.md`, `3f1860a6…`, l. 470 : « defaults to 131072 and can be set up to 1048576 ») — c'est le sens
le plus fidèle d'« enlever le plafond » qui reste une borne explicite. La commande envoie le champ `max_tokens`, déclaré
« Deprecated » mais respecté (la course 2 a été coupée exactement à sa valeur). Le maximum documenté, 1 048 576, coûterait
10,49 USD par appel au pire cas et ferait passer Kimi au-dessus de sa part de 33 USD (section 8). **1,50 USD** est le plus petit
plafond rond qui laisse 131 072 jetons entiers jusqu'à un corps de ≈ 93 600 octets (génération 2 comprise) et garde Kimi et Argon
sous leurs parts au pire cas de la chaîne cassée (section 8). Au-delà de ≈ 166 000 jetons (pire cas d'un appel > 1,70 USD), Kimi franchirait sa part au pire
cas.

## 4. Ce qui ne change pas

- **Code** : v66, tête `7e415cba`, les 98 fichiers du bloc `empreintes-du-code-v66` (section 16 du texte scellé), lanceur, cœur,
  lecture gelée, lecteur du registre des GO ; aucun fichier de l'organisme n'est touché.
- **Commandes et relais** : `commande_kimi_v6.py`, `commande_argon_v56_nuit_v6.py`, `registre_depense_cumulee_v1.py` (mêmes
  empreintes) ; relais Kimi `relais_kimi_v3.py` (`d54ed2bc…`) et relais Argon lancés avec **les mêmes options** qu'à la
  section 12.3 (Kimi 33 USD, 446 appels ; Argon 7 USD, 39 appels ; délais par défaut).
- **Délais** : commande de Kimi 1 750 s, `fournisseurs.kimi.delai_s` 1 800 (non lu par le chemin v64, dit section 2), relais
  1 800 s, durée de course 72 heures.
- **Plan gelé** : générations, cartes, m = 22, bras réel seul, D9 mécanique, plafonds (40 de modèles, Kimi 33, Argon 7, machine
  5), montant 45, monde, jeu planté, héritage de départ. Seules changent les lignes `configuration_sha256` et `go`.
- **Pièces** (consignes, liste de concepts, canaris), prix, modèles (`kimi-k3.1-pro`, `gemini-4-argon`), graines, sections 2 à 11
  et 14 du texte scellé, préalables 1 à 7 de la section 12.3 (rejoués en entier sur une machine neuve).

## 5. Texte neuf à sceller

Le lanceur exige un texte au nom `prereg/preenregistrement-boucle-reelle-organisme-v1-v<N>.md`, sans « brouillon »
(`demonstrations/boucle_reelle_v66.py` l. 77 et 170-174) : le texte neuf s'appelle
**`preenregistrement-boucle-reelle-organisme-v1-v2.md`**, égal au v1 octet pour octet sauf :

1. En-tête : statut (texte v2, écart 1), rédacteur et heures de l'écart, lien vers ce brouillon et vers sa contre-lecture.
2. Documents qui font foi : rangée du dossier de course v7 (configuration `e45f3a71…`, mêmes commandes et pièces) ; rangée du
   rapport de la course 2 (`89b97faf…`) ; rangée de cet écart scellé.
3. Section 0, point 9, et section 13 : la phrase du coût ajoute le pire cas v7 (39,00 USD) et l'attendu révisé (section 8).
4. Section 12.4 : `DOSSIER_COURSE` = le dossier `configuration-v7/` ; `--configuration DOSSIER_COURSE/configuration-boucle-reelle-v7.json` ;
   `--preenregistrement prereg/preenregistrement-boucle-reelle-organisme-v1-v2.md` ; `--go GO-2026-11-12-06`.
5. Section 13 : la ligne de GO neuve recopiée à l'octet après son inscription ; GO-2026-11-10-11 nommée comme remplacée pour la
   suite, ses deux arrêts dits.
6. Section 16, bloc `plan-gele-v66` : `configuration_sha256: e45f3a7199c5d16428a3b4f2b31f1b18ee82594cabbf2b5ec26a6168b1655df6`
   et `go: GO-2026-11-12-06` ; les deux autres blocs inchangés à l'octet.
7. Section 10 (panne d'un relais) : la reprise se fait sous ce texte neuf contre-lu, comme le texte le demande ; la course 2,
   relancée sans texte neuf sur mot direct de Lazar, est dite.

## 6. Effet sur les critères de lecture

**Aucun.** Les prédictions (section 4), métriques (5), seuils (6), plan d'analyse (7), critères de lecture gelés et issues C1 à C7
(8), audit de symétrie (9), liste d'arrêt (10) et portée (14) ne changent pas ; le programme de lecture
(`pole/lecture_boucle_reelle_v66.py`, `demonstrations/lire_boucle_reelle_v66.py`) ne lit ni la configuration ni le GO (vérifié
par recherche). Le gardien est mécanique et aucun juge d'idées à modèle ne décide : la longueur du raisonnement des
proposeurs ne touche aucun critère. Deux choses à dire au rapport, sans changer une issue : (i) **c'est la troisième tentative**
sous ce dessin (deux arrêts C5 avant) : les trois relevés se rapportent ensemble (R4) ; (ii) Argon reçoit une borne de
sortie plus haute (≈ 9 000 → ≈ 29 000 jetons) par le plafond partagé.

## 7. Vérification : le lanceur v66 accepte la configuration v7 sans changer le code

Fait hors ligne sur l'arbre jetable `7e415cba` (`verifications-v1/verifier-lanceur-v66-configuration-v7-v1.py`, sortie
`verifications-v1/sortie-verifier-lanceur-v1.txt`) :

- un texte v2 simulé (le v1 avec les deux lignes du plan changées, scellé dans l'arbre jetable) passe `lire_preenregistrement`
  (nom, sceau, 98 empreintes du code égales, plan conforme, jeu planté) ;
- la ligne de GO proposée, ajoutée à une copie de `registres/go.md` de `main`, passe `verifier_go_v66` (45 USD, montant seul,
  aucune extension) ;
- la configuration v7 passe `lire_configuration_v56` et `verifier_configuration_v66` (section `boucle_reelle_v66`, plafonds
  et parts égaux au plan, commandes v6 à leur empreinte, chemins relatifs) puis `exiger_machine_jetable_reel` et
  `roles_reels(..., transmettre=False)` (budget d'appel 1,5 USD, aucune porte, aucun appel) ; la v6 sous son texte v1, cas sain,
  passe aussi ; la v7 sous le texte v1 est refusée (empreinte), artefact attendu.
- Non joué : la garde 22 (machine, `bwrap`, utilisateur 64097), que la v7 ne touche pas ; elle se rejoue sur la machine.

**Conclusion : aucun changement de code pour la configuration v7.** En revanche, relever le délai de 1 800 s **est** un
changement du code gelé (option 2).

## 8. Effet sur la dépense

Bornes (code et configuration) ; chaîne cassée = 37 cartes testées (17 en génération 1, 20 en génération 2), comme au devis
(section 3.4) et à la section 12.3 :

| poste | v6 | v7 |
|---|---|---|
| un appel du proposeur Kimi, pire cas réservé | 0,50 | 1,35 |
| un appel du proposeur Argon, pire cas réservé | 0,50 | 1,50 |
| Kimi, chaîne correcte (29 cartes × 0,80 + 2 appels) | 24,20 | 25,90 |
| Kimi, chaîne cassée (37 × 0,80 + 2 appels) | 30,60 | **32,30** ≤ 33 |
| Argon, chaîne correcte (29 × 0,10 + 2 appels) | 3,90 | 5,90 |
| Argon, chaîne cassée (37 × 0,10 + 2 appels) | 4,70 | **6,70** ≤ 7 |
| modèles, pire cas chaîne cassée | 35,30 | **39,00** ≤ 40 |

Garde C13 (part restante ≥ pire cas de l'étage, avant chaque étage), au pire : Kimi avant l'étage de génération 2, dépensé
1,35 + 13,60 + 1,35 = 16,30, reste 16,70 ≥ 16,00 ; Argon, dépensé 1,50 + 1,70 + 1,50 = 4,70, reste 2,30 ≥ 2,00. Aucun arrêt de
dépense ne masque une brèche, comme en v6. Plafonds des relais et de la ligne : **inchangés** (Kimi 33, Argon 7, modèles 40,
machine 5, ligne 45).

Attendu (prix de 2 et 10 USD par million pour Kimi, « à vérifier ») : un appel du proposeur Kimi coûte au moins ≈ 0,48 USD
(il a dépassé 46 711 jetons) et, borné par la durée, au plus ≈ 0,56 USD réels sous v7 (≈ 1,35 sous l'option 2). Course
complète ≈ **2,5 à 3 USD** de modèles (devis ≈ 1,5 à 2, où les deux appels Kimi comptaient 0,16 ; ≈ 5,5 si Argon raisonne
jusqu'à sa borne), ≈ 9 à 11,5 si chaque test prend ses 12 tours ; machine ≈ 0,07 USD par course de moins d'une heure. **Échec
le plus probable sous v7 seule** : coupure à 1 750 s, code 6, arrêt ; ≈ 0,53 USD réels, 1,35 comptés au registre (pire cas
réservé), plus ≈ 0,07 de machine.

Déjà dépensé sous GO-2026-11-10-11 : ≈ 1,19 USD au plus (R-2422). Exposition totale si la ligne neuve est accordée sans cumul :
≈ 1,19 + 45 = **46,19 USD au plus**, attendu ≈ 3,7 à 4,2.

## 9. Ligne de GO proposée

GO-2026-11-10-11 ne peut pas servir : ses conditions nomment la configuration v6 (`4743ddbe…`), et elle « ne reçoit jamais de
ligne d'extension ». Ligne neuve, à identifiant neuf (provisoire : **GO-2026-11-12-06**, le prochain libre au registre de `main`
à `4ef91270` ; s'il est pris à l'inscription, le texte v2 prend l'identifiant inscrit avant son scellement), texte dans
`ligne-go-proposee-v1.txt` :

```
| GO-2026-11-12-06 | 2026-11-12 | calcul | **Course réelle de l'organisme d'idéation (boucle réelle, code v66), sous l'écart 1 (sortie du proposeur)** : 40 USD de modèles (Kimi 33, Argon 7 ; plafond de chaque relais égal à sa part) et 5 USD de machine jetable (Hetzner CPX32) **louée sous cette ligne et validée par l'essai à blanc `--bac reel` avant tout appel payant** ; conditions toutes exigées : code v66 contre-lu (`7e415cbaaa3ff602db43a44dad6b4307c08352c7`, contre-lecture `a2880368…`), **configuration v7 (`e45f3a71…`)**, texte neuf `preenregistrement-boucle-reelle-organisme-v1-v2.md` (texte scellé v1 `46d7545b…` plus l'écart 1) contre-lu et scellé ; **remplace GO-2026-11-10-11 pour la suite de cette course, sans cumul** (GO-2026-11-10-11 reste intacte, sa dépense, ≈ 1,19 USD au plus, reste comptée sous elle) ; ne reçoit jamais de ligne d'extension (le lanceur la refuserait) ; arrêt par identifiant (R10), consignation dans `registres/depenses.md` et `registres/arrets.md` | 45 USD | 2026-11-30 | Lazar | écart 1 (`docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/`), R-2422 ; mot direct de Lazar à recopier verbatim à l'inscription |
```

Sous l'option 2, la même ligne nommerait le code v67 contre-lu et la configuration v8 à la place.

## 10. Réserves

- **Durée (bloquante pour l'effet, section 0, point 3)** : sous la v7 seule, la coupure se déplace des jetons vers les 1 750 s ;
  la réussite exige que Kimi finisse sa réponse entre ≈ 46 700 et ≈ 52 600 jetons, ou serve plus vite qu'en course 2.
- **Débit** : un seul point mesuré (≈ 30,1 jetons par seconde, latence comprise) ; il peut varier selon la charge de Moonshot.
- **Argon** : son délai reste 1 750 s pour une borne relevée à ≈ 29 000 jetons ; aucun débit d'Argon n'est mesuré dans cette
  course (zéro appel). Option possible si le contre-lecteur le demande : garder Argon à ≈ 9 000 par `--max-sortie-proposeur`
  9000 dans sa commande ; non retenu ici (le motif de l'écart, un modèle qui raisonne coupé, vaut aussi pour lui).
- **Prix** : 2 et 10 USD par million pour Kimi, du devis, « à vérifier » ; aucune facture lue.
- **Expérimentateur Kimi** : borne de 16 000 jetons par tour, réponses coupées admises en code 0 (« non concluant ») ; non touché ;
  avec un raisonnement au niveau « max » par défaut, des tests « non concluants » sont possibles : à surveiller au rapport.

## 11. Options (pour la décision de Lazar)

1. **v7 seule (ce brouillon)** : aucun changement de code ; contre-lecture courte et scellement du texte v2, puis relance.
   Avantage : relance rapide (quelques heures), sans développement. Inconvénient : la borne devient la durée (≈ 52 600 jetons) ;
   probabilité de réussite faible si Kimi raisonne plus longtemps ; un nouvel échec coûte ≈ 0,6 USD et une session de poste.
2. **Code v67 + configuration v8** : un fichier neuf (R12) remplace `commandes_v64` pour passer `fournisseurs.<nom>.delai_s` à
   l'adaptateur ; configuration v8 = v7 + `fournisseurs.kimi.delai_s` 7 200, commande `--delai-s` 7 150 ; relais Kimi lancé avec
   `--delai-amont-s 7200` (option existante). Un appel du proposeur peut alors aller à 131 072 jetons (≈ 73 minutes au débit
   observé). Avantage : lève vraiment la borne demandée. Inconvénient : changement du code gelé (nouveau bloc d'empreintes,
   essais, banc de mutations, contre-lecture) : ≈ une journée avant la relance ; mêmes bornes de dépense (pire cas 39,00 USD).
3. **v7 + commande Kimi v7 qui envoie `reasoning_effort` « high »** (documenté : `low`, `high`, `max`, défaut `max`) : aucun
   changement du code gelé (la commande est nommée et empreintée par la configuration). Avantage : raisonnement plus court,
   relance en une demi-journée. Inconvénient : change le réglage du proposeur (le texte scellé ne le fixe pas, mais c'est un
   changement de conduite du modèle), toujours borné par 1 750 s, transmission du champ par le relais v3 à vérifier ; code neuf
   à contre-lire.

**Recommandation** : option 2, confiance moyenne (≈ 0,6) ; l'option 1 n'est raisonnable que comme essai rapide assumé, en
sachant qu'elle échoue probablement de la même façon, à la durée. **Défaut sous 48 heures** : aucune relance (nœud : écart et
dépense) ; le développement du code v67, sans dépense, peut commencer comme travail de routine.

## 12. Ce qui reste avant toute relance

1. Contre-lecture de ce brouillon par un sous-agent neuf (R2), fichiers à lui donner : ce brouillon, la configuration v7 et son
   dossier, le texte scellé v1, le rapport v2 de la course, `verifications-v1/`, et l'arbre `7e415cba` (paquets v65 et v66).
2. Décision de Lazar sur l'option (section 11) ; inscription de la ligne de GO par Lazar.
3. Texte v2 écrit (section 5), contre-lu, scellé, copié à l'octet sous `orchestrator/prereg/` de l'arbre de la course.
4. Dossier `configuration-v7/` versé sur la machine avec `heritage-depart-v65.json` et son compagnon ; préalables 1 à 7 rejoués.
