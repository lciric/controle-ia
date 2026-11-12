# Contre-lecture CL10 du différentiel v42 → v43 — prise « idéation » (orchestrateur du pôle v7) et devis v7 octies, voie (β)

Contre-lecteur neuf (règle R2) : Opus 5.5. Je n'ai écrit ni le code (lignée conv-audit) ni les relectures précédentes (CL9
comprise). Relevés `date -u` : début **08:01 UTC**, fin **08:47 UTC**, le 29 octobre 2026. Aucun réseau, aucune clé, aucun
appel payant. « Argon » est toujours un faux local qui consigne chaque appel (`outils-cl10/argon_factice_cl10.py`, copie
étendue de celui de CL9 : facture chaque appel au tarif donné, entrée et sortie, **sans jamais se borner au plafond**). Les
sessions Claude sont celles du moteur simulé, mises au pire cas (coût = plafond) par `outils-cl10/lanceur_cl10.py` (repris de
`lanceur_pire.py`, plus deux pannes pilotées par fichier). Tout a tourné sur des copies (`cl10/copie/`). « Démontré » : exécuté
par moi ; « à la lecture » : non exécuté. `pole/…` et `demonstrations/…` désignent l'arbre `v43/orchestrateur-pole-v7/`.

## Verdict

**Voie (β) telle qu'écrite : non lançable.** Le lanceur la **refuse avant tout appel, sans dépense** : « somme des plafonds
externes 13.00 > total externe 12.8 » (CL43-01, démontré). Le code n'a **pas** de plafond propre à la passe 2 : la seule
option, `--budget "proposeur_ideation|gemini-argon=3.1"`, vaut pour les **deux** passes. La somme du code est donc
3,1 + 3,1 + 3,1 + 3,5 + 0,2 = **13,0**, et non 12,4.

**Lançable après une ligne changée**, au choix de Lazar (démontré, pire cas au plafond, classement à trois juges) :
- **(β-1) juge d'Argon à 3,3** (`--budget "juge_ideation|gemini-argon=3.3"`, à la course et au bras) : Argon 12,8, total
  **52,8**, marge **0** (et non 0,4) ; recommandé ;
- (β-2) passes d'Argon à 3,0 : Argon 12,8, total 52,8, marge 0, passes moins protégées ;
- (β-3) `--budget-externe-usd 13.0` : total **53,0** (+ 0,2 sur 52,8 : mot de Lazar).

Avec trois réserves à dire au devis : la sortie d'Argon n'est pas provisionnée sous la garde donnée (CL43-02 : course perdue
après dépense si les fiches d'Argon dépassent ≈ 8 000 caractères) ; la reprise des contrôles Claude se fait sur un relais
forcément relancé (CL43-03) ; `--taille-max-consigne-externe-bras 1686000` retire la provision du juge, mieux vaut le défaut
(CL43-04).

**Le code v43 corrige ce qu'il annonce**, sous les réglages par défaut. 405 essais sur 405, deux exécutions. CL42-01, 03, 05,
06 et 07 sont corrigés ; CL42-02 n'a plus d'objet ; CL42-04 est appliqué (borne retirée). CL40-01 (c) fait ce que Lazar a
décidé, fichiers changés compris. J'ai réintroduit 40 défauts : 27 sont tués, 13 survivent à la suite entière (6 anciens déjà déclarés, 2 équivalents neufs, 5 trous neufs dont un vrai : X01, changement de fichiers entre deux tentatives jamais essayé).

| réglage (pièce 750 000, matériau 350 000, question 19, huit fiches, seconde passe) | le lanceur accepte ? | pire cas au plafond | barème 8,3 (sortie au rapport 5) | barème haut du code (10 / 50) |
|---|---|---|---|---|
| **(β) du devis** : contrôle 3,1, `--budget proposeur…=3.1`, externe 12,8, garde 1 490 000, bras 1 686 000, prix 8,3 | **non** : 13,00 > 12,8, code 2, avant tout appel ; Claude 0, Argon 0, aucun fichier | — | — | — |
| (β) sans `--budget` (passes à 2,5) | oui (11,8) | Claude 40,00, Argon 11,8, total **51,8**, trois juges | fiches réelles (≈ 4 500) : **passe 2 = 2,74 > 2,5**, course perdue après Claude 0,4 et Argon 7,70, aucun classement | — |
| **(β-1)** juge 3,3 | oui (12,8) | Claude 40,00, Argon **12,8** (3,1 + 3,1 + 3,1 + 0,2 + 3,3), total **52,8**, trois juges | fiches réelles : Argon 7,97, total 47,97, trois juges | contrôle 3,64 > 3,1 : refusé **après** 3,64 payés, Claude 0, non relançable (à la lecture : même chemin que β-3) |
| (β-2) passes 3,0 | oui (12,8) | Claude 40,00, Argon 12,8, total 52,8, trois juges | fiches réelles : Argon 7,98, total 47,98, trois juges | idem |
| **(β-3)** externe 13,0 | oui (13,0) | Claude 40,00, Argon **13,0**, total **53,0**, trois juges | fiches ≈ 4 500 : 47,97 ; ≈ 7 300 : 48,56 ; **≈ 8 950 : passe 2 = 3,18 > 3,1**, perdue après Claude 0,4 et Argon 8,51 ; **fiches au maximum par champ : passe 1 = 5,21 > 3,1**, perdue après Claude 0,4 et Argon 8,23 | contrôle **3,64 > 3,1** : refusé après 3,64 payés, Claude 0, non relançable (16,64 > 13,0) |

Le seuil de barème du contrôle à 3,1 est **8,51 dollars par million de jetons d'entrée** (1 457 167 caractères, 4 par jeton).
Lazar a lu ≤ 8,3 : la marge est de 2,5 % sur le contrôle.

## 1. Comptes vérifiés (démontré)

- **Empreintes** (08:01) : `sha256sum -c EMPREINTES-orchestrateur-pole-v7-v43.txt` → **156 sur 156 conformes**. Compagnons de
  la liste et du LISEZMOI v43 conformes. Liste v43 `f23cc576…`, LISEZMOI v43 `a9fca6ac…` : ce sont les empreintes du devis.
  Liste v42 : 154 sur 154. Devis v7 octies : `43fc1d2a34e89f88…` (conforme à l'annonce). Relevé de début de 542 fichiers :
  `outils-cl10/empreintes-debut.txt`.
- **Différentiel** : `diff -rq v42 v43` → changent `pole/ideation.py`, `demonstrations/ideation_v1.py`,
  `essais/test_v7_ideation.py` ; s'ajoutent la liste d'empreintes et le LISEZMOI v43. Le patch couvre exactement ces fichiers.
- **Essais** : `env -i PATH=… HOME=… python3 -B -m unittest discover -s essais -t . -p 'test_*.py'`, deux exécutions
  simultanées sur deux copies : **Ran 405 tests in 739,8 s, OK** et **Ran 405 tests in 734,2 s, OK**, code 0
  (`outils-cl10/essais-sortie-a.txt`, `-b.txt` ; la durée vient de la charge : mes scénarios tournaient en même temps).

## 2. Scénarios de CL9 rejoués sur la v43 (démontré)

Outils de CL9 copiés sans changement dans `outils-cl10/` ; sorties sous `cl10/simulee-cl9/`.

| scénario | v43 (démontré) | annonce de l'auteur |
|---|---|---|
| S1 pire cas, pièces de 2 000 | code 0 ; Claude **40,00** ; Argon course 7,5, bras 3,7, **11,2** ; trois juges | — |
| S2 Argon « KO » au contrôle (0,15) | Claude **0** partout ; tentatives 1 et 2 relançables ; la 3ᵉ non (« 3 tentatives faites ») ; la 4ᵉ refusée sans rappeler Argon. Argon cassé sans coût lisible : 2,5 comptés, non relançable | — |
| S3, S4 SIGTERM (contrôle d'Argon, passe d'Argon) | code 2 ; processus et petits-enfants morts | — |
| S5b, S6, S10 | code 0 aux deux étages ; S6 : contrôle du bras court, juge réel | — |
| S8 SIGTERM au bras après envoi | bras code 2, relance code 2 ; processus morts | — |
| **D-a-devis, D-a-haut, D-c-plafond, D-c-devis, D-base, D-b, D-a-q2000** | **tous refusés par la garde, avant tout appel** : Claude 0, Argon 0 | concorde (tableau du LISEZMOI) |
| S12 interruption entre SORTIE et manifeste de départ | code 2 puis 0 ; tentative-1 relançable | — |
| **S14** repli en panne au 3ᵉ bras non joué | code 2 ; `classement-sans-bras-impossible-3.json` scellé ; l'échec est dit sur la sortie d'erreur | concorde |
| `sondes_nan.py` | **0 acceptation fautive** (29 « ACCEPTÉ », tous sur les cas sains) | — |
| `sonde_relais_relance.py` | relance « relais gardé (dépense 0,4) » : **refus** ; « relais relancé à neuf » : acceptée | — |

## 3. CL42-01 à 07

| constat | verdict | preuve |
|---|---|---|
| **CL42-01** passe 2 non couverte par la garde | **corrigé sous la garde par défaut ; pas sous la garde donnée** (CL43-02) | défaut 520 000 (10) et 724 819 (8,3) ; `--budget-controle-externe-usd 3.0` seul refusé sans dépense (D-a-devis, D-a-haut) ; chaque passe gardée avant envoi, gardes au journal (`gardes_taille_sessions`, tous les B-*). Mais avec `--taille-max-consigne-externe` (que β exige), les passes sont gardées contre **cette valeur**, provision 0, sans leur plafond : B-p25-b83-reelles (2,74 > 2,5) et B-p31-b83-g700-x130 (3,18 > 3,1) partent et cassent après dépense. Défauts X10 à X14 et X26 : tous tués |
| CL42-02 option (b) | sans objet (devis) | le devis v7 octies ne la reprend pas ; D-b refusé sans dépense |
| **CL42-03** mesurer avant le GO | **corrigé** | `--mesurer-consignes` aux réglages β : passe 1 **752 440**, passe 2 maximale **1 456 692**, contrôle **1 457 167**, juge au maximum **2 131 096** (52 fiches), contrôle du bras **41** ; coût du contrôle 3,0236 à 8,3 ; aucun appel, **aucun dossier créé** (le dossier `mesure` nommé n'existe pas après), code 0. Rien n'est scellé : rediriger et sceller (R6), comme l'auteur le dit |
| **CL42-04** borne de 12 000 retirée | **appliqué** | phrase absente de la consigne ; fiche de **44 259** caractères admise (`valider_fiche_ideation`, et 16 fiches d'Argon de 44 259 validées dans BJ, 0 refus) ; champ de 3 001 → `FicheTropLongue`, compté par proposeur et par passe |
| **CL42-05** garde du bras, W07 | **corrigé** | option propre au bras ; `--taille-max-consigne-externe` au bras : refus de l'analyseur, code 2 ; option du bras sans `--bras-rapporte-differe` : refus. BJ-defaut : consigne de juge de 1 473 221 > 1 166 746 → `manifeste-bras-refus-taille-1.json`, classement sans bras, code 5, **rien payé**. Mais l'option donnée retire la provision (CL43-04) |
| **CL42-06** repli silencieux | **corrigé** | S14 ; X23 (échec du repli non scellé) tué |
| **CL42-07** survivants de CL9 | **corrigé pour W07, W30, W36, W35b** (tués) ; W03, W28, W35, M28, N28, V27 survivent, comme déclaré | § 6 |

## 4. Voie (β) aux réglages exacts, pire cas et barèmes (démontré)

Outil : `outils-cl10/scenarios_cl10.py`, scénarios `B-<passes>-<tarif>-<fiches>[-x130][-j33]`. Réglages : pièce de 750 000
caractères (exactement), matériau de 350 000, question de 19, témoins de CL9 (4), seconde passe, Argon proposeur et juge, huit
fiches. Course : `--budget-controle-externe-usd 3.1 --budget-externe-usd 12.8 --taille-max-consigne-externe 1490000
--prix-entree-usd-par-million-jetons 8.3` (+ `--budget "proposeur_ideation|gemini-argon=3.1"` pour « p31 »). Bras :
`--taille-max-consigne-externe-bras 1686000 --prix-entree-usd-par-million-jetons 8.3 --budget-externe-usd 12.8`. Tarifs :
« plafond » (chaque session coûte son plafond), « b83 » (8,3 et 41,5 dollars par million de jetons, 4 caractères par jeton :
la sortie au rapport 5 du barème du code, **hypothèse**, Lazar n'a lu que l'entrée), « haut » (10 et 50). Fiches d'Argon :
« petites » (≈ 800 caractères), « reelles » (≈ 4 500, dans la fourchette de CL8), « g560 » (≈ 7 300), « g700 » (≈ 8 950),
« max » (44 259, bornes par champ). Résumé : `simulee/resume-B.txt`.

Détail par session (coûts déclarés par le faux Argon ; « > » : au-dessus du plafond de la session) :

| scénario | contrôle (1 457 167) | passe 1 (752 440) | passe 2 | bras : contrôle, juge | Claude | Argon | issue |
|---|---|---|---|---|---|---|---|
| B-p31-plafond-petites (**β exacte**) | — | — | — | — | 0 | 0 | **refus « 13.00 > 12.8 »**, code 2, avant tout appel, aucun fichier |
| B-p25-plafond-petites | 3,1 | 2,5 | 2,5 (1 110 020) | 0,2 ; 3,5 | 40,00 | 11,8 | trois juges |
| B-p25-b83-petites | 3,0236 | 1,63 | 2,37 | 0,0001 ; 0,16 | 40,00 | 7,19 | trois juges |
| B-p25-b83-reelles | 3,0236 | 1,94 | **2,74 > 2,5** (1 139 628) | — | 0,4 | 7,70 | **perdue après dépense**, aucun classement |
| B-p25-b83-max | 3,0236 | **5,21 > 2,5** | — | — | 0,4 | 8,23 | perdue après dépense |
| B-p25-haut-reelles | **3,64 > 3,1** | — | — | — | 0 | 3,64 | tentative scellée, non relançable (15,44 > 12,8) |
| **B-p31-plafond-petites-j33** (β-1) | 3,1 | 3,1 | 3,1 | 0,2 ; **3,3** | 40,00 | **12,8** | **total 52,8**, trois juges ; garde du bras 1 590 000 |
| B-p31-b83-reelles-j33 | 3,0236 | 1,94 | 2,74 | 0,0001 ; 0,27 | 40,00 | 7,97 | 47,97, trois juges |
| B-p30-plafond-petites (β-2) | 3,1 | 3,0 | 3,0 | 0,2 ; 3,5 | 40,00 | 12,8 | 52,8, trois juges |
| B-p30-b83-reelles | 3,0236 | 1,94 | 2,74 | 0,0001 ; 0,28 | 40,00 | 7,98 | 47,98, trois juges |
| **B-p31-plafond-petites-x130** (β-3) | 3,1 | 3,1 | 3,1 | 0,2 ; 3,5 | 40,00 | **13,0** | **total 53,0**, trois juges |
| B-p31-b83-petites-x130 | 3,0236 | 1,63 | 2,37 | 0,0001 ; 0,14 | 40,00 | 7,17 | 47,17, trois juges |
| B-p31-b83-reelles-x130 | 3,0236 | 1,94 | 2,74 | 0,0001 ; 0,27 | 40,00 | 7,97 | 47,97, trois juges |
| B-p31-b83-g560-x130 | 3,0236 | 2,16 | 3,01 (1 161 612) | 0,0001 ; 0,35 | 40,00 | 8,56 | 48,56, trois juges |
| **B-p31-b83-g700-x130** | 3,0236 | 2,30 | **3,18 > 3,1** (1 175 148) | — | 0,4 | 8,51 | **perdue après dépense** |
| B-p31-b83-max-x130 | 3,0236 | **5,21 > 3,1** | — | — | 0,4 | 8,23 | perdue après dépense |
| B-p31-haut-reelles-x130 | **3,64 > 3,1** | — | — | — | 0 | 3,64 | non relançable (16,64 > 13,0) |

**Concordance du devis avec le code.**
- Concordent : 752 440 ; 1 456 692 ; **1 457 167** ; 2 131 096 ; 41 ; 3,02 à 8,3 et 3,64 à 10 ; 44 259 ; garde par défaut
  724 819 à 8,3 (passes à 2,5) ; bras 1 686 000 (= 1 686 746 arrondi bas) ; défaut du bras 1 166 746 à 8,3 ; Claude 40 ;
  `--mesurer-consignes` sans appel.
- **Seuil 1 493 976** : le code calcule **1 493 975** (troncature de 1 493 975,9). Sans effet : la garde donnée vaut 1 490 000
  (marge de 32 833 caractères sur le contrôle mesuré, 2,3 %).
- **« Argon 12,8 (3,1 + 2,5 + 3,1 + 3,5 + 0,2 = 12,4, marge 0,4) »** : faux pour le code (CL43-01).
- **« plafond de la passe 2 à 3,1 (option du lanceur) »** : l'option n'existe pas (CL43-01).
- **Point 3, « chaque passe d'Argon est gardée sur sa consigne réelle avant envoi »** : vrai, mais contre 1 490 000, sans
  provision ni plafond de passe (CL43-02).
- **Point 4, « la phrase “trois tentatives” est retirée ; une relance est possible tant que les contrôles à refaire
  tiennent dans les sommes »** : faux pour le code, qui garde trois tentatives au plus (CL43-05).

## 5. CL40-01 (c) : reprise des contrôles réussis (démontré)

Scénarios `R-*` (petites pièces, réglages par défaut du lanceur, contrôle d'Argon à 0,15, contrôles Claude à 0,2, sessions au
plafond ; panne du cœur avant son départ pilotée par un fichier ; même ligne de commande d'une tentative à l'autre).

| scénario | T1 | T2 | T3 / T4 | lecture |
|---|---|---|---|---|
| R-reprise | Argon 0,15, Claude 2 × 0,2, panne : relançable, `controles_a_refaire` [] | **aucun contrôle rejoué**, course complète : coûts imputés Claude 0,4 et Argon 0,15, trois reprises au manifeste (tentative 1, empreintes du fichier et de la consigne) | — | conforme |
| **R-fichiers-changes** | idem | **pièce changée** (liste blanche refaite) : **Argon rejoué** (consigne d'empreinte différente), « KO » à 0,15 ; Claude **non rappelé** ; relançable, à refaire `externe:argon` | Argon rejoué, « OK » ; Claude toujours non rappelé ; course complète ; contrôles externes imputés 0,45 (3 × 0,15), Claude 0,4 | **conforme** : un contrôle d'Argon dont la consigne a changé n'est jamais repris. Le contrôle Claude (consigne courte et fixe) est repris, ce qui est juste : il ne dépend pas des fichiers |
| **R-relais-casse** | idem | Claude « cassé » à la même adresse (simulé) : contrôles Claude **repris**, contrôle d'Argon repris ; **passes 1 et 2 d'Argon payées (2,5 + 2,5)**, puis la première session Claude échoue ; SORTIE écrite, course perdue | — | **danger réel** (CL43-03) |
| R-quatre-tentatives | panne | panne (rien rejoué, rien payé) | T3 non relançable (« 3 tentatives faites ») ; **T4 refusée** | contredit le point 4 du devis (CL43-05) |
| R-reprise-journal-en-argument | idem, mais la commande d'Argon nomme son journal (un fichier qui change) | **Argon rejoué** (0,15 repayé) alors que T1 disait `controles_a_refaire` [] | — | CL43-06 |

## 6. Défauts réintroduits (démontré)

Outil : `outils-cl10/mutations_cl10.py` (moteur de CL7 à CL9). Une copie neuve par défaut ; chaque remplacement est vérifié
unique avant le jeu. Premier passage sur `test_adaptateurs` et `test_v7_ideation` (les six modules du pari apparié pour N28).
Chaque survivant est confirmé sur la **suite entière** (405 essais, OK, 334 à 463 secondes chacun).

| groupe | réintroduits | tués | survivants à la suite entière |
|---|---|---|---|
| survivants de CL9, réexprimés sur la v43 | 10 | **4** : W07, W30, W36, W35b (réexprimé : la phrase de 12 000 remise dans la consigne) | M28 (incertain), N28 (équivalent), V27 (presque équivalent), W03 (égalité, sans effet pratique), W28 (course concurrente, déclarée), W35 (presque équivalent) — tous déjà déclarés |
| CL40-01 (c) : clé, réussite, sommes de la relance (X01 à X04, X06 à X09, X27, X28, X32) | 11 | 8 | **X01** (clé sans l'empreinte de la consigne : **vrai trou**, CL43-07) ; X04 (contrôle non lancé tenu pour réussi : **équivalent**, un contrôle non lancé porte toujours un problème ou un statut autre que « ok ») ; X27 (clé d'Argon sans identité dans le chemin d'exception : **équivalent**, ce chemin ne porte que des contrôles d'Argon échoués, jamais repris) |
| CL42-01 : gardes de la course et des passes (X10 à X14, X26) | 6 | **6** | — |
| CL42-04 b : prix (X15, X16, X30) | 3 | 0 | **X15**, **X16** (prix non transmis au cœur ou au bras : garde plus stricte, sens sûr) ; **X30** (NaN admis par le cœur appelé directement ; le lanceur refuse avant) |
| CL42-05 : bras (X17, X18, X25, X29, X35, X36) | 6 | **6** | — |
| CL42-03, 06, 07 (X19, X20, X23, X34) | 4 | 3 | **X34** (« passerait » toujours vrai dans la sortie de `--mesurer-consignes`) |
| **total** | **40** | **27** | **13** : 6 anciens déjà déclarés ; 2 équivalents neufs (X04, X27) ; 5 trous neufs (X01, X34, et X15, X16, X30 sans danger en production) |

Sorties : `outils-cl10/mutants/mutations-premier-passage.json`, `mutations-complet.json`, une sortie par défaut ; résumés
dans `outils-cl10/mutations-premier-passage-sortie.txt` et `mutations-complet-sortie.txt`. L'auteur annonçait six défauts
tués sur le code neuf ; je confirme les siens (aucun contrôle repris, prix ignoré par la garde, borne rétablie, relance
comptée sur tous les contrôles, passes jamais gardées, refus de taille au bras non compté : X06/X32, X10/X26, W35b, X09,
X14, X17 sont tués).

## 7. Constats neufs

### CL43-01 — bloquant pour (β) telle qu'écrite (sans risque d'argent) — Le code n'a pas de plafond propre à la passe 2 ; la somme externe de (β) vaut 13,0 > 12,8

**Endroit.** `roles_et_budgets` (lanceur) : un plafond par clé (rôle, modèle), `--budget "proposeur_ideation|<Argon>=…"`.
Cœur, `lancer` : `plafond = budgets[(role, modele)]` pour les deux passes. `verifier_reglages` : somme externe =
contrôles prévus + **passes ×** plafond du proposeur + juge + contrôle du bras.

**Défaut** (démontré, B-p31-plafond-petites). Le devis écrit « plafond de la passe 2 à 3,1 (option du lanceur) » et
« 3,1 + 2,5 + 3,1 + 3,5 + 0,2 = 12,4 ». L'option qui existe met **les deux passes** à 3,1 : la somme vaut 13,0. Le lanceur
refuse : « somme des plafonds externes 13.00 > total externe 12.8 », code 2, avant tout appel, rien payé, aucun fichier. Sans
cette option, les passes restent à 2,5 (somme 11,8, acceptée), mais la passe 2 casse au barème 8,3 dès que les fiches
d'Argon dépassent ≈ 2 100 caractères (calcul ; démontré à ≈ 4 500 : 2,74 > 2,5, course perdue après Claude 0,4 et Argon
7,70, aucun classement).

**Correction** (devis, une ligne ; choix de Lazar) :
- **(β-1), recommandé, confiance 0,7** : `--budget "proposeur_ideation|gemini-argon=3.1" --budget
  "juge_ideation|gemini-argon=3.3"` à la course, `--budget "juge_ideation|gemini-argon=3.3"` au bras. Argon 3,1 + 3,1 + 3,1 +
  0,2 + 3,3 = **12,8**, total **52,8**, marge **0**. Démontré : pire cas 52,8, trois juges ; barème 8,3, fiches réelles :
  47,97. Le juge réel coûte 0,14 à 0,35 (consigne de 31 000 à 133 000 caractères) : 3,3 laisse une marge de ×10.
- (β-2) passes à 3,0 : 12,8, marge 0 ; la passe 2 tient jusqu'à ≈ 7 100 caractères par fiche (calcul) au lieu de ≈ 8 100.
- (β-3) `--budget-externe-usd 13.0` : total **53,0**, au-dessus des 52,8 (mot de Lazar).
- Dans le code (plafond par passe), plus tard : nouvelle version, nouvelle contre-lecture.

### CL43-02 — majeur — Sous la garde donnée, les passes d'Argon sont gardées sans provision de sortie ni plafond de passe : une passe peut partir et casser après dépense

**Endroit.** Cœur, `garder_session_externe` : si `taille_max_consigne_externe` est donné, `tmax, prov =
taille_max_consigne_externe, 0` ; le plafond de la passe et la provision ne servent que sans taille donnée. Or (β) **doit**
donner la taille : la garde par défaut, avec provision, vaudrait 1 013 975 (passes à 3,1) ou 724 819 (passes à 2,5), sous le
contrôle de 1 457 167.

**Défaut** (démontré). La passe 2 réelle (1,11 à 1,18 million) passe toujours sous 1 490 000 ; sa sortie n'est comptée
nulle part. Au barème 8,3 (sortie au rapport 5), avec des passes à 3,1 :
- fiches d'Argon de ≈ 7 300 caractères : passe 2 = 3,01, tout passe (B-p31-b83-g560-x130) ;
- fiches de ≈ 8 950 : **passe 2 = 3,18 > 3,1**, `budget_depasse`, course arrêtée après Claude 0,4 et Argon 8,51, aucun
  classement, SORTIE écrite (relance : mot de Lazar) (B-p31-b83-g700-x130) ;
- fiches aux bornes par champ (44 259) : **passe 1 = 5,21 > 3,1** (B-p31-b83-max-x130).

Le seuil est ≈ **8 000 caractères par fiche d'Argon** (≈ 7 100 sous β-2). CL8 relevait 3 000 à 5 000 pour d'autres
proposeurs ; la consigne ne dit plus de borne de fiche (CL42-04). La phrase du devis « chaque passe d'Argon est gardée sur sa
consigne réelle avant envoi » est vraie, mais sous (β) cette garde est celle du contrôle, sans rien de plus. La « provision
de huit fiches de 12 000 » du devis (point 3) **ne s'applique pas** sous la garde donnée.

**Correction.**
- Devis : dire le seuil (≈ 8 000 caractères par fiche d'Argon au barème 8,3, sortie au rapport 5) et l'issue (course perdue,
  ≈ 8,9 dollars dépensés).
- Avant le GO : vérifier que la vraie commande d'Argon **s'arrête à `PLAFOND_SESSION_USD`** (sortie bornée). Sinon, la somme
  des plafonds ne borne pas la dépense réelle (§ 8).
- Code (proposition) : sous taille donnée, garder chaque passe contre min(taille donnée ; plafond de la passe / prix −
  provision), avec une taille de fiche provisionnée réglable (par exemple 8 000 : passe 2 réelle 1 139 628 + 320 000 ≤
  1 493 975). Essai : passe 2 refusée sans envoi sous garde donnée quand la provision ne tient pas.

### CL43-03 — majeur — La reprise d'un contrôle Claude se fait, par construction, sur un relais relancé ; s'il est mal réglé, les deux passes d'Argon sont payées avant la panne

**Endroit.** Lanceur : `identite_claude = {"moteur": args.moteur, "url_relais": args.url_relais}` ; clé de reprise sur la
consigne courte et fixe. `verifier_relais` exige plafond − réserve − dépense ≥ total − plus petit juge. Cœur : « un
proposeur externe joue sa passe 2 juste après sa passe 1, avant toute passe Claude ».

**Défaut** (démontré).
1. Aux réglages du devis (relais `--plafond-usd 40 --reserve-par-appel 4`, total 40, plus petit juge 4), toute dépense
   Claude d'une tentative (0,2 ou 0,4 de contrôles) fait refuser le relais gardé : « 40 − 4 − 0,4 < 40 − 4 ». **Toute
   relance après des contrôles Claude payés exige donc de relancer le relais**, en général à la même adresse. La réserve de
   l'auteur (« relais relancé à la même adresse non vu ») décrit donc le cas normal, pas un cas rare.
2. R-relais-casse : tentative 1 réussie aux contrôles, panne du cœur ; tentative 2 avec un Claude qui échoue à la même
   « adresse ». Les contrôles Claude et d'Argon sont repris ; la course part ; **passes 1 et 2 d'Argon payées (2,5 + 2,5 ;
   sous β : 3,1 + 3,1)**, puis la première session Claude échoue. SORTIE écrite : course perdue, relance sur mot de Lazar.
   Sans la reprise (v42), le contrôle Claude (0,2) aurait échoué avant toute passe.

Le gain de la reprise côté Claude est ≤ 0,4 dollar ; le risque est ≤ 6,2 dollars d'Argon et la course. `verifier_relais`
voit un relais qui répond, pas un relais qui sert les modèles.

**Correction** (dans la décision (c) de Lazar : un contrôle sur un autre relais n'est pas « le même contrôle »).
- Ne reprendre un contrôle Claude que si le relais n'a pas été relancé : la lecture scellée porte `relais_apres.depense_usd` ;
  si la dépense lue au départ est **plus basse**, le relais a été relancé → rejouer les contrôles Claude (0,4 au plus, dans
  les sommes). Mieux : un identifiant d'instance dans l'état du relais (`relais_reel.etat`), mis dans la clé.
- Essai : relais relancé (dépense remise à 0) → contrôles Claude rejoués ; relais gardé → repris.
- À défaut, le dire au devis comme risque accepté par Lazar.

### CL43-04 — mineur — `--taille-max-consigne-externe-bras 1686000` retire la provision de sortie du juge

**Défaut** (démontré, BJ-option contre BJ-defaut ; consigne du juge de 1 473 221 caractères, obtenue avec une pièce de juge de
750 000 et des fiches d'Argon au maximum ; notes de ≈ 2 000 caractères).
- Avec l'option : consigne admise, juge **3,76 > 3,5** après envoi ; classement sans bras écrit, code 5 ; 3,76 dépensés pour
  rien ; externe 9,3 + 3,76 = **13,06 > 13,0** (le faux Argon ne se borne pas).
- Sans l'option (défaut à 8,3 : 1 166 746) : refus de taille **sans dépense**, tentative comptée, classement sans bras.
- 1 686 000 × 2,075 × 10⁻⁶ = 3,4985 : toute sortie de plus de ≈ 145 caractères dépasse 3,5.

Les consignes de juge réelles font 31 000 à 133 000 caractères (B-*) : le défaut suffit largement.

**Correction.** Retirer l'option du lancement (garder le défaut avec provision : 1 166 746 ; 1 070 361 si le juge est à
3,3), ou la chiffrer moins la provision.

### CL43-05 — mineur (devis) — « La phrase “trois tentatives” est retirée » : le code garde trois tentatives au plus

**Défaut** (démontré, R-quatre-tentatives). Trois tentatives scellées (dont deux qui ne rejouent rien et ne coûtent rien) :
la troisième est « non relançable : 3 tentatives faites » ; la quatrième est refusée, « 3 tentatives de contrôle déjà
faites … plus de relance sans un mot de Lazar ». Le point 4 du devis dit le contraire.

**Correction.** Corriger la phrase du devis ; ou, si Lazar veut la règle du devis, changer le code (nouvelle version).

### CL43-06 — mineur — L'identité de la commande d'Argon porte l'empreinte de chaque argument fichier : un fichier qui change empêche toute reprise, et `relancable` a supposé la reprise

**Défaut** (démontré, R-reprise-journal-en-argument). `description()` prend l'empreinte de tout argument qui est un fichier.
Une commande qui nomme un fichier qui change (son journal) n'est jamais reprise : le contrôle d'Argon est repayé (0,15),
alors que la tentative scellée disait `controles_a_refaire` []. Sous (β), la relance compterait 3,1 de plus et serait
refusée sans dépense : pas de perte d'argent, mais une prévision fausse.

**Correction.** Avant le GO, vérifier que la vraie ligne de commande d'Argon ne nomme aucun fichier qui change. Ou bien ne
prendre l'empreinte que de l'exécutable et des scripts ; essai.

### CL43-07 — mineur — Essais : survivants neufs sur le code de la v43

Voir § 6. Le vrai trou est **X01** : aucun essai ne change les fichiers entre deux tentatives, si bien qu'une clé de reprise
sans l'empreinte de la consigne (Argon repris après un changement de pièce) passe la suite entière. Mon scénario
R-fichiers-changes montre que le code est juste ; rien ne le garde. Les autres : X34 (« passerait » de
`--mesurer-consignes`, que Lazar lira avant le GO, jamais vérifié) ; X15 et X16 (prix du devis non transmis au cœur ou au
bras : la garde devient plus stricte, sens sûr) ; X30 (prix non fini admis par le cœur appelé directement ; le lanceur le
refuse avant).

**Correction.** Un essai par trou : pièce changée entre deux tentatives → Argon rejoué ; `passerait` faux quand la garde
refuse ; prix de 8,3 retrouvé au journal des passes et au bras ; NaN au cœur.

### CL43-08 — information — Seuil 1 493 976 du devis : le code calcule 1 493 975

Troncature (3,1 / 2,075 × 10⁻⁶ = 1 493 975,9). Sans effet : la garde donnée vaut 1 490 000.

**Compte des constats neufs.** Un bloquant pour (β) telle qu'écrite, sans risque d'argent (CL43-01). Deux majeurs : CL43-02
(course perdue après dépense au-delà de ≈ 8 000 caractères par fiche d'Argon) et CL43-03 (relance sur relais relancé). Quatre
mineurs : CL43-04, 05, 06, 07. Une information : CL43-08.

## 8. Ce que je n'ai pas pu vérifier

- Le vrai barème d'Argon, **sa sortie** (le rapport 5 est une hypothèse du code) et **si la vraie commande s'arrête à
  `PLAFOND_SESSION_USD`**. Mon faux Argon ne se borne jamais : il dépasse jusqu'à 5,21 pour un plafond de 3,1. Si la vraie
  commande se borne, CL43-02 devient une sortie tronquée (fiches invalides) au lieu d'un dépassement ; sinon, les sommes de
  plafonds ne bornent plus la dépense réelle (BJ-option : externe 13,06 > 13,0).
- La taille réelle des fiches d'Argon sans borne de fiche (CL8 : 3 000 à 5 000 caractères pour d'autres proposeurs).
- La vraie ligne de commande d'Argon (arguments fichiers qui changent : CL43-06).
- Le vrai relais, son état après relance, les sessions Claude réelles.
- Toute décision de dépense : β-1, β-2 ou β-3 est un mot de Lazar.

## 9. Fin de relecture

- **Empreintes** après relecture (08:47 UTC) : liste v43, 156 sur 156 conformes. Les 542 fichiers de `v42/` et `v43/` sont
  identiques au relevé du début (`cmp` entre `outils-cl10/empreintes-debut.txt` et `empreintes-fin.txt`, sans écart). Aucun
  `__pycache__` dans les arbres relus.
- **Processus** : aucun processus de mes essais, scénarios ou défauts n'est actif (`ps`). Les commandes et petits-enfants des
  scénarios d'interruption sont morts (S3, S4, S8 : `vivants_apres` faux partout).
- Les deux copies des essais sont supprimées ; reste `copie/v43s` (3,4 Mo). Aucun dépôt git créé. Aucun réseau.

## 10. Fichiers produits

Sous `relecture-v43/cl10/` :
- `contre-lecture-v43-cl10.md` (ce rapport) et son compagnon `.sha256`.
- `outils-cl10/` :
  - neufs : `argon_factice_cl10.py`, `lanceur_cl10.py`, `scenarios_cl10.py` (B-*, BJ-*, R-*), `resumer_b.py`,
    `mutations_cl10.py` ;
  - copiés de CL9 sans changement : `argon_factice.py`, `argon_factice_cl9.py`, `lanceur_pire.py`, `scenarios_cl9.py`,
    `scenarios_cl8.py`, `scenario_fenetre.py`, `lanceur_fenetre.py`, `sonde_repli_silencieux.py`, `sonde_tailles.py`,
    `sondes_nan.py`, `sonde_relais_relance.py`, `sonde_fiche_12000.py`, `mutations_cl9.py`, `mutations.py`, `garde_puissance.py` ;
  - sorties : `essais-sortie-a.txt`, `essais-sortie-b.txt`, `empreintes-debut.txt`, `empreintes-fin.txt`,
    `mutations-premier-passage-sortie.txt`, `mutations-complet-sortie.txt`, `mutants/` (une sortie par défaut, deux JSON).
- `simulee/` : un dossier par scénario B-*, BJ-*, R-* (fichiers, configurations, journal d'Argon, `rapport.json`) et
  `resume-B.txt`.
- `simulee-cl9/` : scénarios et sondes de CL9 rejoués sur la v43.
- `copie/` : copies de la v43 sur lesquelles tout a tourné (à supprimer à volonté).
