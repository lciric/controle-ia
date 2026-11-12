# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v6) — cl5

- **Rôle** : sous-agent neuf, cinquième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v6, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 à 4 (cl1 à cl4).
- **Heure** : 27 octobre 2026. Lecture commencée à 04:28:36 UTC, rapport écrit à partir de 04:57:43 UTC (`date -u`).
- **Empreintes (sha256)** des pièces lues :

  | pièce | sha256 |
  |---|---|
  | `prereg/brouillon-test-echelle-conscience-eval-v6.md` (texte relu ; conforme à son compagnon à 04:28 et à 04:57, inchangé pendant ma lecture) | `878958bf5de75d914efc24f2508ee33449dd50eaa014839d1d4eaf32f6c20032` |
  | `prereg/brouillon-test-echelle-conscience-eval-v5.md` | `1111d89a9b745ad043736aa65ce9bb6c86a6dfcbfcbde167b741a7016a8212ee` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v5-cl4.md` | `5728de4c2a4774ab3d96f267f91189dd6d860b4fb2fdef3edd41e910477ee592` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v4-cl3.md` | `a2f330f09df1d0cfb3188482331de3ba847133865f4764aa7a8b1cf11cf15896` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v3-cl2.md` | `9b476cf4b64a521f97cc7368ca60723e41390557291570fc6c08f30369b04803` |
  | `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md` | `70afa51997f66f882f79686765c9b1fdded6f0016007b626355b975abd9e673a` |
  | `echelle-v5/scripts/analyser_echelle_v5.py` (conforme au tableau, au compagnon et à l'objet du commit) | `191c9186c364b4b2ee3d7dd2d124aa044cd37eba93c46a82dc9c081a9266ff9f` |
  | `echelle-v4/scripts/analyser_echelle_v4.py` (comparaison) | `3e1c341a4ba97a148da9699c7550ce6fc85e92129e3a41b9c486efeff44c6c02` |
  | `src/controle_ia/prereg.py` (inchangé depuis cl4) | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
  | `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
  | `.claude/hooks/garde_calcul.py` (inchangé depuis cl4) | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` |
  | `registres/go.md` (registre vivant ; état lu, le même que celui de cl4) | `a157cd2f1feff106bfbc5687e55221d2015b7c640e6fc0f2c719a019f58cf580` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md` | `134040bd9a126dce4592aa3b357375f0209f987610d3be21a6848f647eaf59b4` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v2.md` | `fe1e93c1efe7c9117c9f0b22711912394c5b40d0180b904bf61e324cf0943d3a` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v3.md` | `9d03d3b212ca43d3eb905413f95f808ef2bc90376b284804a9ed1dbd28ddc3de` |
  | `docs/notes/echelle-conscience-eval/v5/extrait-R-530.txt` | `de548478fcc72cd66557062320305ea9f0f4eeed3f351185d8c8e878fa304c05` |
  | `docs/notes/echelle-conscience-eval/v5/consigne-contre-lecture-cl5.md` (ma consigne, identique au message reçu) | `33d30120cd185ac50433e5eeca3274cab0f4efc8ece5774aef483a2d69805b81` |
  | `docs/notes/echelle-conscience-eval/v5/contre-lecture-cl4/scripts/banc_v5.py` (banc de cl4, générateur repris) | `863b9c501f6f0e29be760dedd4b1fd36ace3d754f4f2656549e1ba93ef628387` |
  | `docs/notes/echelle-conscience-eval/v3/atteignabilite-echelle-v3.json` (comparaison) | `8d90b2e7ea5669ccd3f9bcdff9ce2f1e8f5231af4b5b4be12b37a03682fc77a3` |
  | `docs/notes/echelle-conscience-eval/v4/atteignabilite-echelle-v4.json` (comparaison) | `877a8e31d2b1e970eefb108a66b56af459a61f3813b00c98fd9b989cd93cbfa9` |
  | `docs/notes/echelle-conscience-eval/v5/tests-echelle-v5-600470b.txt` | `bf2a69272ecbfbce50e4f655f9e3954725fe0d4207d1d864f9967ac9a83e0d32` |

- **Code relu** dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` :
  - branche `outils/echelle-conscience-eval-v5`, tête `8b4db5a6c8b109695fbf0a5394cc19c880d9041a` : c'est le commit attendu, et la branche de suivi `origin/outils/echelle-conscience-eval-v5` pointe au même endroit ; l'`origin` du dépôt est bien `lciric/controle-ia-travail` ;
  - `8b4db5a` n'ajoute à `600470b` que 49 lignes de `test_offre_et_surveillance_v5.py` (sept tests du lanceur) et son compagnon (`git diff --stat`) ;
  - arbre propre avant et après mes essais : seuls les deux `__pycache__` ignorés de `echelle-v3/`, antérieurs à ma lecture ; l'index de l'arbre de travail n'a pas bougé depuis 04:19:41 UTC (mes appels passaient `GIT_OPTIONAL_LOCKS=0`) ;
  - **38 empreintes sur 38** du texte concordent : les 20 outils avec le fichier, le compagnon et l'objet du commit ; les 18 traces avec le fichier et le compagnon (`sorties/sortie-verif-empreintes.txt`) ;
  - stimuli, constructeur et rapport de construction identiques à l'octet à ceux de `echelle-v4/` (`cmp`) ; `diff` de chaque script v4 → v5.
- **Lu en entier** :
  - les brouillons v6 et v5 (et leur `diff`, section par section) ; cl4 et ses pièces : `gardes/LISEZ-MOI.txt`, les neuf scripts, les treize sorties (résumés des bancs compris) et les lignes de banc par Python ; les sous-dossiers `amorce/` et `faux/` à travers leurs sorties résumées ; les 106 compagnons vérifiés ;
  - cl3 en entier ; ses pièces parcourues : générateur du banc (identique à celui de cl4 et au mien), essais de l'état de l'arbre, de l'amorce et de la tolérance du prix, détail « H1 ; tau 0,8 » ; les 32 compagnons vérifiés ;
  - les constats et le traitement de cl2 et de cl1 ;
  - tout `echelle-v5/` : quatorze scripts, `.gitignore`, rapport de construction, quatre fichiers de tests ; les stimuli par Python seulement ;
  - les gardes héritées : `exiger_prereg_scelle` et ce qu'elle appelle (`problemes`, `sections`, `scellement.verifier`, `GardeArret`) ; `garde_calcul.py` en entier ; l'en-tête de `registres/go.md` et les lignes de GO de type « calcul » ;
  - les traces citées : accès, tailles des modèles, gabarits, contrôles lexicaux v5, offre de référence v3 et ses 45 offres, sortie des tests, répétition (résumé, empreintes, commit, trois journaux : délai atteint, création trop ancienne, mauvais commit ; analyse du modèle minuscule ; les 18 compagnons vérifiés), atteignabilité v5 (et v3, v4 pour comparer), audit de la simulation (script et sortie), extrait R-530 ;
  - les passages des cartes v1 à v3 que le texte cite.
- **Interdits respectés** :
  - aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt (seulement des listes de dossiers nommés) ;
  - aucun réseau, aucune commande vastai (deux faux outils dans mon bac à sable), aucun lancement, aucune écriture git ; rien de modifié hors de mon bac à sable (vérifié en fin de lecture) ;
  - aucune clé ni aucun jeton cherché, affiché ou écrit ;
  - tous les essais avec `TMPDIR`, `--basetemp` et `HF_HOME` dans le bac à sable, `-B` et `PYTHONDONTWRITEBYTECODE=1`, fils de calcul à un.
- **Essais** (scripts jetables et sorties dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v6/`) :
  - tests du commit : **225 passed in 343.00s**, avec le modèle minuscule local (`sorties/tests-cl5.txt`) ;
  - simulation d'atteignabilité rejouée avec le script du commit, ses graines, trois processus (`reproduction-atteignabilite/`) ;
  - contrôle lexical rejoué (`lexique-reproduit/`) ;
  - bancs, analyse v5 **telle quelle** (mode répétition, 300 tirages, d = 64), générateur de cl4 repris à l'identique : 106 analyses, dont **66 rejeux de tous les cas de cl4 aux mêmes graines** et 40 cas nouveaux (`scripts/banc_cl5*.py`, `banc/`, `sorties/sortie-banc-cl5-lot*.txt`, `sorties/sortie-comparer-cl4-v5.txt`) ;
  - cas limites de `lire()` sur des intervalles fabriqués, et essai en mémoire de la correction proposée pour CLV-01 (`scripts/cas_limites_lire_v5.py`, `scripts/essai_correction_fsi.py`) ;
  - réserves « profondeur » nouvelles calculées par `principal` sur quatre couches, cas sain et artefact pour chaque issue (`scripts/profondeur_nouvelles_v5.py`) ;
  - dépense réelle au pire balayée sur 30 308 offres admises, et choix d'offre rejoué sur la trace des 45 offres (`scripts/pire_domaine_v5.py`) ;
  - chaîne du lanceur (préenregistrement scellé → empreinte → commit cité → GO relu) jouée telle quelle sur un faux dépôt (`chaine-lanceur/`) ; contrôle du GO joué sur le registre réel (`sorties/sortie-verifier-go-registre-reel.txt`) ;
  - retard d'arrêt de la surveillance mesuré avec un faux outil dont les appels durent 59 s (`surveillance-latence/`).

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLV-01** : la « fuite de signe inverse » se lit dans chaque sens « pour l'un des modèles au moins », puis les deux sens sont combinés par l'étiquette seule. Elle est donc prononcée quand le petit modèle fuit à rebours dans le seul sens a→b et le grand dans le seul sens b→a : aucun modèle ne la tient dans les deux sens. Deux signatures d'un seul jeu, de tailles différentes, la fabriquent : **16 lectures prononcées sur 20 analyses, dont 14 sans aucune réserve**. « Positif », « inverse » et « pas de fuite » exigent, eux, le même modèle dans les deux sens. C'est l'asymétrie que R4 interdit, et le principe que le texte pose (« une issue n'est prononcée que si elle tient dans les deux sens »).

Corrections à faire avant le scellement :

- CLV-01 (bloquant) : il touche `lire()` et l'analyse. Il faut donc, comme après cl2, cl3 et cl4 : des noms nouveaux (R12), un commit et des empreintes nouveaux ; les tests et la simulation rejoués ; un texte nouveau, et une contre-lecture neuve des parties changées (R2).
- Les remarques CLV-02 à CLV-08 sont à reprendre au passage.

## Ce qui tient

- **Empreintes et commit** : 38 sur 38 ; tête de branche = commit attendu ; arbre propre ; les noms nouveaux sont libres (`prereg/test-echelle-conscience-eval-v6.md` absent ; aucune référence `donnees/echelle…` dans le dépôt).
- **Tests** : 225 passent chez moi (343 s), comme la trace (325 s). Les 53 cas fabriqués de `test_lire` et leurs 53 miroirs sont bien là.
- **Simulation** : reproduite **à l'octet près**, le commit mis à part. Ma sortie, faite au commit `8b4db5a`, ne diffère de la sortie scellée que par `commit_scripts` ; en y remettant `600470b…`, son empreinte est `29e2c66f…`, celle de la sortie scellée. 30 cases, 120 analyses.
  - Le tableau du texte la transcrit fidèlement, case par case, réserves comprises. 16 noms sur 20 sont atteints ; les quatre autres sont les miroirs annoncés.
  - La phrase R3 est exacte sur ses 44 analyses (aucun « positif » ni « inverse »).
  - L'audit dit vrai sur ses chiffres : cosinus de −0,284 à +0,178 ; λ effectif de −0,352 pour la graine 3138 ; composantes de −0,151 à +0,307 pour les neuf lectures des doubles signatures ; trois « désaccord » de la règle v4 devenus « nul ».
- **Contrôle lexical** : reproduit à l'octet près (`9250873a…`) ; sac de mots 0,5717 (a→b) et 0,5242 (b→a) ; aucun lemme d'un seul côté commun aux gabarits, dans a ni dans b.
- **CLW-01 levé, preuve rejouée** sur les 66 analyses des bancs de cl4, aux mêmes graines :
  - intervalles **identiques** à ceux de cl4 dans les 66 (même calcul, mêmes activations) ;
  - les huit « désaccord des deux sens » de cl4 (fuite faible et égale) deviennent « nul », avec la réserve « pas de fuite lu dans le seul sens … (non confirmé) » ;
  - une « fuite de signe inverse » (double signature négative, graine 9902) reçoit la réserve nouvelle ;
  - rien d'autre ne change, sinon le libellé de la réserve « fuite non spécifique » (même nombre de réserves).
- **Concordance du texte et du code** (`lire`, `issues_tenues`, `conditions`, `reserves`, `principal`) :
  - ordre de lecture, conditions P(s) et I(s), inégalités strictes ou larges, certification ≥ 0,70 dans chaque sens ;
  - étape 2 : échecs de certification combinés, première issue commune, réserves des issues placées avant elle, désaccord, non confirmé ; essayé sur mes cas fabriqués ;
  - réserves « fuite non spécifique » (dont −λ − ν) et « profondeur » pour chaque issue ; `SEUILS`, `ATTENDUS`, choix de L\* (plus petite des deux aires, arrondie, puis plus petit des deux d', puis la plus basse), tirage conditionné, graines, rejets, mode décisif (commit, arbre, numpy, nom et empreinte du script de mesure) ;
  - une phrase par issue ; commandes du lancement, de la surveillance et de l'analyse ; liste d'arrêt conforme au code, ligne à ligne.
- **Réserves « profondeur » nouvelles** : calculées par `principal` sur quatre couches, elles se déclenchent sur l'artefact et pas sur le cas sain, pour « nul », « pas de fuite » et « fuite de signe inverse » (`sorties/sortie-profondeur-nouvelles-v5.txt`).
- **Dépense** :
  - le pire calculé tient sous 8 USD par construction, sur 30 308 offres admises ; la dépense réelle au pire, au prix majoré de 5 % avec 80 s de retard d'arrêt, vaut 7,88 USD au plus ;
  - rejeu du choix sur les 45 offres de la trace : offre 50510069, 7 200 s ; pire 7,0311, estimé 5,40 et attendu 3,81 USD, comme la trace et le texte (7,03 ; 5,40 ; ≈ 3,8) ; seconde offre conforme à 8,00 USD tout juste.
- **Lanceur** : la chaîne nouvelle tient, jouée telle quelle sur un faux dépôt : texte scellé et conforme → empreinte extraite → commit cité → GO relu « conforme ». Un commit cité seulement en abrégé (`600470b…`) arrête ; un GO au plafond « 8 USD au pire, tout compris » arrête (voir CLV-05).
- **GO relu sur le registre réel** : le registre se lit sans erreur (aucun code 2) ; tout GO de type « calcul » du registre est refusé, dont `GO-2026-10-26-08` (plafond 2 USD) et `GO-2026-10-04-08` (plafond illisible pour ce contrôle).
- **Gardes héritées** : code inchangé depuis cl4 (mêmes empreintes).
- **Répétition** : 25 lignes conformes, dont les six lignes de fin des refus précoces ; commit `600470b…` ; compagnons vérifiés.
- **Gabarit** : le rendu porte une date fixe (« Today Date: 26 Jul 2024 ») ; il ne dépend pas du jour de la mesure.
- **R7** : citations conformes aux cartes (carte v1, l. 114, 289, 358 et 359 ; carte v2, l. 16, 24 et 57 ; carte v3, l. 14, 17, 81 à 84, 157 et 201), réserve de circularité de Xiong et al. comprise.
- **R9, R10, R12** : `SeedSequence`, versions, commit et fils consignés par l'analyse et la simulation ; arrêts par identifiant partout ; noms neufs (`…_v5`, `analyse-echelle-v5.json`, branche `donnees/echelle-conscience-eval-v5`).
- **R3** : aucune issue n'est visée ; la lecture est mécanique, les graines fixées, et l'analyse décisive est déterministe à commit, numpy et entropie donnés. Je n'ai trouvé aucun degré de liberté qui permette de viser un signe.

## Traitement des constats de cl4

| constat de cl4 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLW-01 « nul » masqué par la combinaison des deux sens | bloquant | **traité** | Chaque sens rend l'ensemble de ses issues ; la première issue commune est prononcée ; le cas « fuite de signe inverse dans un seul sens, nul dans les deux » est tranché par écrit. Rejeu des 66 analyses de cl4 : intervalles identiques, les huit « désaccord » deviennent « nul » avec réserve, rien d'autre ne change. Tests (cinq cas compatibles et leurs miroirs), intégration et simulation conformes. Mais la combinaison par étiquette laisse passer une « fuite de signe inverse » tenue par deux modèles différents (CLV-01) |
| CLW-02 réserves limitées à « positif » et « inverse » | à corriger | **traité en partie** | Réserves −λ − ν et « profondeur » pour chaque issue : codées, testées sur drapeaux fabriqués, et justes sur quatre couches (mon essai). Mais : sur la double signature négative de cl4 (`sig_ab_neg`), la v5 prononce encore « fuite de signe inverse » 4 fois sur 4, dont **3 sans réserve** (le texte dit « en partie », d'après 2 cas sur 2 de la simulation) ; la limite ne couvre pas les signatures croisées (CLV-01, CLV-04) ; la phrase R3 ne parle toujours que de « positif » et d'« inverse » ; « peut masquer un écart vrai » n'est pas écrit (CLV-04) ; le calcul des drapeaux nouveaux n'a pas de test (CLV-08) |
| CLW-03 GO non contrôlé | à corriger | **traité** | `verifier_go_v5.py` appelé avant toute création ; 11 cas et les codes testés ; chaîne complète jouée par moi ; registre réel : tout GO de type « calcul » refusé. Format du plafond non dit (CLV-05) |
| CLW-04 commit lancé et script de mesure | à corriger | **traité** | Le lanceur exige que le texte scellé cite le commit (testé ; et par moi : un commit cité en abrégé arrête) ; l'analyse décisive relit nom et empreinte du script de mesure (deux artefacts testés) |
| CLW-05 « Prix de la symétrie » faux | à corriger | **traité**, un reste | « Positif » et « inverse » se lisent bien comme en v3 (vérifié sur les simulations v3 et v5). Reste : un gain d'information est compté comme un prix, et un compte est incomplet (CLV-03) |
| CLW-06 phrase de « désaccord » | remarque | **traité** | Variabilité près des seuils ajoutée ; « aucune issue ne tient dans les deux » |
| CLW-07 grandeurs dans un seul sens | remarque | **traité** | ΔA_ctx_fixe, ΔA_conf, sac de mots et marge dans les deux sens ; contrôle lexical b→a (0,5242, reproduit) ; L\* sur la plus petite des deux aires et le plus petit des deux d' |
| CLW-08 liste d'arrêt et codes | remarque | **traité**, un reste | Code 7 et conduite écrite ; GO refusé à la liste ; ligne de fin des refus précoces (répétition : 6 sur 6) ; appels bornés à 60 s. Reste : avec ces bornes, l'arrêt peut venir 291 s après le plafond (mesuré), au-delà des 196 s que couvre la marge ; cl4 proposait 30 s (CLV-02) |
| CLW-09 manques de tests | remarque | **traité** | « Création différente » et « conteneur sorti sans ligne de fin » testés ; signature négative au 70B en test et en simulation. Les gardes héritées restent sans test dans la suite `echelle-v5` ; le texte s'appuie sur l'essai de cl4, et le dit |
| CLW-10 renvois et détails | remarque | **traité** | Extrait empreinté de R-530 (0,98) ; « de 8 à 11 fois plus petit, pour des directions aléatoires » ; tailles et volume tracés (157,19 Go ; 0,302 Go) ; commit en tête de la trace des tests ; version de vastai vérifiée et testée ; miroir de l'exemple de R4 |

Bilan : 10 constats traités, dont 3 avec un reste (CLW-02 en partie, CLW-05, CLW-08) ; aucun non traité.

## Constats nouveaux

### CLV-01 — BLOQUANT — « Fuite de signe inverse » prononcée sans qu'aucun modèle ne la tienne dans les deux sens : deux signatures d'un seul jeu, à des tailles différentes, la fabriquent

- **Localisation** :
  - `analyser_echelle_v5.py` : `conditions`, l. 446–447 (« borne haute de λ_s(petit) ou de λ_s(grand) < −δ », sens par sens) ; `issues_tenues`, l. 474–478 ; `lire`, l. 541–550 (issues communes comparées par leur seule étiquette) ; `reserves`, l. 517–520 ;
  - brouillon v6 : étape 1, l. 234 ; étape 2, l. 244 ; phrase permise, l. 269 ; Hypothèse, l. 70 ; Mesures, l. 127–128 ; R3 et audit, l. 193–201 ; limites, l. 298–302.
- **Constat** :
  - Dans chaque sens, « fuite de signe inverse » tient dès que **l'un des modèles** a une borne haute de λ sous −δ. La combinaison ne regarde ensuite que l'étiquette. L'issue est donc « commune » quand le petit modèle est sous −δ dans le seul sens a→b et le grand dans le seul sens b→a.
  - Pour chacun des deux modèles, la fuite ne tient alors que dans un sens. C'est exactement ce que le texte exclut : « une issue n'est prononcée que si elle tient dans les deux sens » (l. 70) ; « Une fuite du concept, elle, se retrouve dans les deux sens. D'où la lecture symétrique » (l. 128).
  - **Asymétrie (R4)** : « positif » exige λ_s(8B) > δ dans chaque sens, « inverse » λ_s(70B) > δ dans chaque sens, « pas de fuite » les deux modèles dans chaque sens. Ces issues exigent donc, par construction, le même modèle dans les deux sens. Seule la « fuite de signe inverse », issue de signe négatif, en est dispensée.
  - **Mécanisme** : une poussée négative du format sur la signature du jeu a, à une taille, ne déplace que le sens a→b ; une autre sur la signature du jeu b, à l'autre taille, ne déplace que le sens b→a. Chacune est une signature d'un seul jeu, que le texte range dans H_0 (« toute issue qui ne se retrouve que dans un sens », l. 80). Aucune n'est la « poussée alignée à la fois sur les signatures des deux jeux » de la limite écrite (l. 298).
  - Les réserves ne le voient pas : le témoin ν est aveugle aux poussées sur une signature (CLY-01), et les réserves sont calculées modèle par modèle et sens par sens.
  - La phrase permise devient fausse : « Dans les deux sens, à une taille au moins, le gabarit de banc d'essai déplace la lecture vers le pôle "usage réel" » ; à aucune taille ce n'est vrai dans les deux sens. Dans ces cas, les intervalles de Δλ sont le plus souvent de signes opposés d'un sens à l'autre, zéro exclu (13 fois sur 16 dans mon banc).
  - Ni la simulation ni les tests n'ont ce cas : dans tous les cas de test où cette issue est prononcée, le même modèle est sous −δ dans les deux sens.
- **Preuve** :
  - Cas fabriqué (`sorties/sortie-cas-limites-lire-v5.txt`) : a→b, λ(petit) [−1,0 ; −0,6], λ(grand) [−0,1 ; 0,1] ; b→a, λ(petit) [−0,1 ; 0,1], λ(grand) [−1,0 ; −0,6]. Lecture : « fuite de signe inverse », aucune réserve, aucune condition manquante rapportée.
  - Banc, analyse v5 telle quelle, générateur de cl4, aucune fuite du concept aux deux tailles (`sorties/sortie-banc-cl5-lot1.txt`, `-lot2.txt`) :

    | cas (graines) | lectures |
    |---|---|
    | signature du jeu a de −2 au 8B, du jeu b de −2 au 70B, tau 0,4 (11000 à 11014) | **fuite de signe inverse 8 sur 8**, dont 6 sans réserve |
    | signature du jeu b de −2 au 8B, du jeu a de −2 au 70B, tau 0,4 (11100 à 11114) | **fuite de signe inverse 7**, toutes sans réserve ; non confirmé 1 |
    | signature du jeu a de −2 au 8B, du jeu b de −2 au 70B, tau 0,15 (12300 à 12306) | fuite de signe inverse 1 (sans réserve) ; non confirmé 2 ; indécis 1 |
    | miroir positif : jeu a de +2 au 8B, jeu b de +2 au 70B, tau 0,4 (11200 à 11206) | indécis 2 ; inverse non confirmé 2 : rien n'est prononcé |

    Dans les 16 lectures prononcées, **aucun modèle n'est sous −δ dans les deux sens** (a→b : le modèle poussé sur a ; b→a : celui poussé sur b). Exemple, graine 11000 : λ_a→b(petit) [−1,18 ; −0,50], λ_a→b(grand) [−0,27 ; 0,33] ; λ_b→a(petit) [−0,52 ; 0,17], λ_b→a(grand) [−1,11 ; −0,65] ; Δλ_a→b [−1,22 ; −0,53] et Δλ_b→a [0,23 ; 1,08].
  - Le miroir positif ne fabrique rien : l'asymétrie est réelle.
  - Correction essayée en mémoire, sans toucher l'arbre (`sorties/sortie-essai-correction-fsi.txt`) : en scindant l'issue par modèle, le cas croisé devient « désaccord des deux sens », le cas du même modèle reste « fuite de signe inverse (petit) », les autres cas ne changent pas.
- **Correction** :
  - ne prononcer « fuite de signe inverse » que si **le même modèle** a sa borne haute sous −δ dans les deux sens, par exemple en scindant l'issue en « fuite de signe inverse (petit) » et « (grand) » dans l'ordre de lecture ; un modèle sous −δ dans un seul sens devient une réserve « lu dans le seul sens » ;
  - nommer la taille dans la phrase permise (« à la taille X, dans les deux sens, … ») ; restreindre les réserves « fuite non spécifique » et « profondeur » à ce modèle ;
  - tests : le cas croisé et son miroir ; simulation : signatures croisées négatives, dans les deux ordres (attendu : aucune « fuite de signe inverse » prononcée) ;
  - texte : étapes 1 et 2, phrase permise, limites et audit (classe d'artefact « signatures d'un seul jeu, à des tailles différentes », écartée par la règle du même modèle).

### CLV-02 — REMARQUE — La surveillance peut demander l'arrêt jusqu'à environ 300 s après le plafond, au-delà des 196 s que couvre la marge

- **Localisation** : `surveiller_echelle_v5.sh`, l. 47–61 (l'heure est lue en tête de boucle, l. 48, avant deux appels bornés à 60 s, puis comparée au plafond, l. 59 ; pause de 60 s, l. 60) ; brouillon v6, l. 49 (« la marge de 0,20 USD couvre la latence de la surveillance : environ 196 s ») et l. 349.
- **Constat** : le test du plafond utilise l'heure lue avant les deux appels. Au pire de ses bornes : une boucle part juste avant le plafond, deux appels de 60 s, la pause de 60 s, puis deux appels encore avant le test. L'arrêt est alors demandé environ 300 s après le plafond. La marge de 0,20 USD n'en couvre que 196 au prix maximal admis.
- **Preuve** :
  - faux outil dont `show` et `logs` répondent en 59 s, sous la borne de 60 s : arrêt demandé **291 s** après le plafond (`surveillance-latence/resultat.txt`) ;
  - balayage (`sorties/sortie-pire-domaine-v5.txt`) : à 196 s de retard, 8,00 USD au plus ; à 230 s, 1 633 offres admises sur 30 308 dépassent 8 USD (8,03 au plus) ; à 300 s, 3 473 offres (8,11 USD au plus).
- **Portée** : l'amorce arrête le calcul d'elle-même à « création + durée − 600 s » (plus 2 min). Sous l'hypothèse dite (une instance sortie n'est facturée que pour son stockage), le plafond tient donc. Mais la phrase « la marge couvre la latence de la surveillance » n'est pas vraie aux bornes du code. Les appels du lanceur (`create`, `search`, `show`) ne sont pas bornés non plus.
- **Correction** : relire l'heure juste avant le test du plafond (ou tester le plafond avant et après les appels), ou borner chaque appel à 30 s comme cl4 le proposait ; ou écrire qu'au-delà de 196 s de retard, le plafond repose sur la borne de l'amorce et sur l'hypothèse de facturation.

### CLV-03 — REMARQUE — « Prix de la symétrie » : un gain d'information compté comme un prix, et un compte incomplet

- **Localisation** : brouillon v6, l. 202.
- **Constat** :
  - « Sous H_0 au tau 0,8, un "indécis" devient "nul non confirmé" » : la v3 lisait déjà « indécis » ici ; rien n'est perdu, la lecture en dit plus. Ce n'est pas un prix. Le seul prix sur les issues nulles, dans la simulation, est le « pas de fuite » perdu sur quatre, au tau 0,8.
  - « Sous H_A faible, deux "indécis" de la v3 deviennent "positif non confirmé (a→b)" » : c'est deux au tau 0,4 et deux de plus au tau 0,8, soit quatre.
- **Preuve** : simulation v3 (`8d90b2e7…`) : H0 au tau 0,8, indécis 4 ; H1 faible, tau 0,4, positif 2 et indécis 2 ; tau 0,8, indécis 4. Simulation v5 (`29e2c66f…`) : H0 au tau 0,8, indécis 3 et nul non confirmé (a→b) 1 ; H1 faible, tau 0,4, positif 2 et positif non confirmé (a→b) 2 ; tau 0,8, indécis 2 et positif non confirmé (a→b) 2.
- **Correction** : « Le prix porte sur les issues nulles : sans fuite au tau 0,8, un "pas de fuite" sur quatre devient "non confirmé". Ailleurs, la lecture en dit plus sans rien prononcer : sous H_0 au tau 0,8, un "indécis" devient "nul non confirmé" ; sous H_A faible, quatre "indécis" (deux au tau 0,4, deux au tau 0,8) deviennent "positif non confirmé (a→b)". »

### CLV-04 — REMARQUE — Portée des phrases R3 et de la limite des doubles signatures

- **Localisation** : brouillon v6, l. 193 (R3), l. 197–201 (audit), l. 298–302 (limite).
- **Constat** :
  - R3 annonce « la signature d'un seul jeu (a ou b, de l'un ou l'autre signe, au 8B ou au 70B ; 44 analyses) ». La simulation en a cinq combinaisons sur huit : a+ et a− au 8B, a+ et a− au 70B, b+ au 8B. Les signatures b− au 8B, b+ et b− au 70B ne sont couvertes que par la symétrie de la règle et les miroirs des tests.
  - La limite ne couvre qu'une poussée alignée sur les deux jeux à une même taille. Les signatures d'un seul jeu à deux tailles différentes en sont une autre classe (CLV-01 : évitable par la règle du même modèle ; à écrire une fois corrigée).
  - CLW-02 demandait d'écrire que la double signature « peut masquer un écart vrai » : ce n'est pas écrit. Mes bancs n'ont produit aucun « nul » faux sous H_A vraie : double signature négative au 8B, indécis 4 sur 4 au tau 0,4 ; signatures croisées de signes opposés, indécis, positif non confirmé ou positif (lot 2). Le risque paraît être une perte de puissance plutôt qu'un nul faux ; il suffit de le dire.
- **Correction** : écrire les combinaisons simulées telles qu'elles sont ; compléter la limite (signatures croisées ; perte de puissance sous H_A).

### CLV-05 — REMARQUE — Le format exigé de la ligne du GO n'est pas dit

- **Localisation** : `verifier_go_v5.py`, l. 35–37 (plafond lu seulement sous la forme « N USD ») et l. 54–64 ; brouillon v6, l. 39–43.
- **Constat** : la cellule du plafond doit valoir exactement « N USD » (virgule admise). L'usage du registre est d'y ajouter une mention (« 150 USD (alerte à 120 USD) », « 10 USD au plus (…) », « 25 USD (`--plafond-usd 25`, …) »). Un GO écrit ainsi serait refusé. L'arrêt est sûr (aucune création), mais il coûte un aller et retour avec Lazar. Le périmètre doit aussi porter le nom exact et les seize premiers caractères de l'empreinte.
- **Preuve** : chaîne du lanceur jouée sur un faux dépôt : un GO au plafond « 8 USD au pire, tout compris » donne « plafond illisible », code 2 (`sorties/sortie-chaine-lanceur.txt`) ; sur le registre réel, le plafond de plusieurs GO serait illisible pour ce contrôle, par exemple `GO-2026-10-04-08` (« 150 USD (alerte à 120 USD) ») et `GO-2026-10-25-03` (« 10 USD au plus (… ») (`sorties/sortie-verifier-go-registre-reel.txt`).
- **Correction** : écrire dans « Dépense » la forme exacte de la ligne attendue (périmètre : `test-echelle-conscience-eval-v6.md` et les seize premiers caractères de l'empreinte ; plafond : « 8 USD », seul), ou lire un nombre suivi d'une mention.

### CLV-06 — REMARQUE — Le lanceur et la surveillance ne vérifient pas qu'ils sont ceux du commit

- **Localisation** : `lancer_echelle_v5.sh`, l. 47 (empreinte du lanceur consignée, non comparée) et l. 66–70 (amorce, choix d'offre, prix et GO extraits du commit) ; `surveiller_echelle_v5.sh` : rien.
- **Constat** : tout ce que le lanceur appelle vient du commit, mais le lanceur lui-même et la surveillance tournent depuis le disque local. Une copie modifiée contournerait les gardes ; seule l'empreinte du lanceur est consignée. C'est consigné, pas gardé (comme CLY-06).
- **Correction** : comparer `sha256sum "$0"` à `git show "$COMMIT:echelle-v5/scripts/lancer_echelle_v5.sh" | sha256sum`, et arrêter sinon ; faire écrire par le lanceur l'empreinte attendue de la surveillance, que celle-ci vérifie. À défaut, inscrire la vérification de ces empreintes contre le tableau dans la lecture.

### CLV-07 — REMARQUE — Conditions manquantes rapportées pour la première issue de chaque sens seulement

- **Localisation** : `lire`, l. 551–558 ; brouillon v6, l. 250 (« Les conditions qui manquent à chaque issue non confirmée sont rapportées »).
- **Constat** : pour « X non confirmé » et « désaccord », seule la première issue de chaque sens reçoit ses conditions manquantes. Une seconde issue tenue dans un seul sens (« nul » à côté de « pas de fuite », par exemple) figure dans `issues_tenues_par_sens`, mais ce qui lui manque dans l'autre sens n'est pas rapporté.
- **Preuve** (`sorties/sortie-cas-limites-lire-v5.txt`) : « pas de fuite et nul en a→b, b→a indécis » ne rapporte que « pas de fuite (a→b), dans le sens b→a » ; « fuite de signe inverse et nul en a→b, pas de fuite en b→a » ne rapporte rien pour « nul ».
- **Correction** : rapporter les conditions manquantes de chaque issue tenue dans un seul sens, ou écrire « de la première issue de chaque sens ». Dire aussi que « X non confirmé » et « désaccord » ne portent pas de réserve, comme les échecs de certification et « indécis ».

### CLV-08 — REMARQUE — R5 : deux chemins nouveaux n'ont pas de test dans la suite (éprouvés par moi : conformes)

- **Localisation** : `analyser_echelle_v5.py`, l. 678–688 (drapeaux « profondeur » de « nul », « pas de fuite » et « fuite de signe inverse ») ; `lancer_echelle_v5.sh`, l. 49–55 (empreinte du texte scellé extraite, puis passée au contrôle du GO, l. 82–83).
- **Constat** :
  - les drapeaux nouveaux ne sont testés qu'au travers de `lire`, sur des drapeaux fabriqués ; le test d'intégration à quatre couches ne couvre que « positif », et la simulation n'a que deux couches, si bien que ces drapeaux n'y sont jamais calculés ;
  - aucun test ne joue l'extraction de l'empreinte du texte scellé : le test du GO la reçoit toute faite.
- **Preuve** : quatre couches, un cas sain et un artefact par issue : la réserve se déclenche sur l'artefact seulement, pour chacune des trois issues (`sorties/sortie-profondeur-nouvelles-v5.txt`) ; chaîne du lanceur sur un faux dépôt : conforme, et les deux artefacts arrêtent (`sorties/sortie-chaine-lanceur.txt`).
- **Correction** : ajouter ces tests au prochain tour, que CLV-01 impose de toute façon.

## Annexe — bancs cl5 (analyse v5 telle quelle, 300 tirages, d = 64)

Générateur de cl4 repris à l'identique (`banc_cl5.py` ; seule la docstring diffère de `fabriquer` de cl4) : x = contenu + s_f·F + s_c·κ·C + cadrage + bruit, avec F = α·C + F⊥ + signature_a·sig_a + signature_b·sig_b ; |C| = 4 ; signatures normées à |C|, multipliées par le facteur indiqué.

| cas (graines) | vérité (8B ; 70B) | lectures v5 | v4 (cl4) |
|---|---|---|---|
| faible_egal_t015 (9600 à 9622) | (0,2 ; 0,2), tau 0,15 | nul 12, dont 3 avec la réserve « pas de fuite lu dans le seul sens » | nul 9 ; désaccord 3 |
| faible_forceb06_t015 (10200 à 10214) | (0,15 ; 0,15), contexte b × 0,6 | nul 8, dont 5 avec la réserve | désaccord 5 ; nul 3 |
| sig_ab_neg (9900 à 9906) | signatures a et b de −2 au 8B | fuite de signe inverse 4, dont **3 sans réserve** | fuite de signe inverse 4, sans réserve possible |
| sig_ab_grand (10000 à 10006) | signatures a et b de +2 au 70B | inverse 4, dont 2 sans réserve | idem |
| sig_ab_pos (9200 à 9206) | signatures a et b de +2 au 8B | positif 4, dont 3 avec réserve | idem |
| les neuf autres cas de cl4 (34 analyses) | — | mêmes lectures et même nombre de réserves que cl4 (une seule réserve change de libellé) | — |
| croise_neg_8a_70b (11000 à 11014) | a de −2 au 8B, b de −2 au 70B | **fuite de signe inverse 8**, dont 6 sans réserve | — (CLV-01) |
| croise_neg_8b_70a (11100 à 11114) | b de −2 au 8B, a de −2 au 70B | **fuite de signe inverse 7**, toutes sans réserve ; non confirmé 1 | — (CLV-01) |
| croise_neg_8a_70b_t015 (12300 à 12306) | idem, tau 0,15 | fuite de signe inverse 1 ; non confirmé 2 ; indécis 1 | — (CLV-01) |
| croise_pos_8a_70b (11200 à 11206) | a de +2 au 8B, b de +2 au 70B | indécis 2 ; inverse non confirmé 2 | — |
| masque_double_t04 (11300 à 11306) | (1,0 ; 0,2), a et b de −2 au 8B | indécis 4 | — (CLV-04) |
| masque_croise_HA, trois réglages (12000 à 12206) | (1,0 ; 0,2), a négatif au 8B, b positif au 70B | indécis 7 ; positif non confirmé 3 ; positif 2 | — (CLV-04) |

Sur les 66 rejeux des cas de cl4, les intervalles sont identiques à ceux de cl4 ; 51 lectures sont identiques, réserves comprises ; 8 « désaccord » deviennent « nul » avec réserve ; une « fuite de signe inverse » reçoit la réserve nouvelle ; 6 ne diffèrent que par le libellé de la réserve « fuite non spécifique » (`sorties/sortie-comparer-cl4-v5.txt`).

Pièces, dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v6/` :

- `scripts/` : `verif_empreintes.py`, `cas_limites_lire_v5.py`, `essai_correction_fsi.py`, `banc_cl5.py`, `banc_cl5_lot2.py`, `banc_cl5_lot3.py`, `resumer_banc_cl5.py`, `comparer_cl4_v5.py`, `comparer_atteignabilite.py`, `profondeur_nouvelles_v5.py`, `pire_domaine_v5.py`, `surveillance_latence.sh` ;
- `banc/` : `banc-cl5-lot1.jsonl`, `banc-cl5-lot2.jsonl`, `banc-cl5-lot3.jsonl`, journaux et heures ;
- `reproduction-atteignabilite/` : `sortie/atteignabilite-echelle-v5.json` et son compagnon, `journal.txt`, `comparaison.txt`, heures ;
- `sorties/` : `tests-cl5.txt`, `sortie-verif-empreintes.txt`, `sortie-cas-limites-lire-v5.txt`, `sortie-essai-correction-fsi.txt`, `sortie-banc-cl5-lot1.txt`, `sortie-banc-cl5-lot2.txt`, `sortie-banc-cl5-lot3.txt`, `sortie-comparer-cl4-v5.txt`, `sortie-profondeur-nouvelles-v5.txt`, `sortie-pire-domaine-v5.txt`, `sortie-chaine-lanceur.txt`, `sortie-verifier-go-registre-reel.txt` ;
- `lexique-reproduit/`, `offres/`, `chaine-lanceur/` (faux dépôt et registre d'essai), `surveillance-latence/` (faux outil, sortie, `resultat.txt`), `profondeur-essai/`.
