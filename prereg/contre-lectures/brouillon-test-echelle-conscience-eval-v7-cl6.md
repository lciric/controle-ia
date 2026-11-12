# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v7) — cl6

- **Rôle** : sous-agent neuf, sixième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v7, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 à 5 (cl1 à cl5).
- **Heure** : 27 octobre 2026. Lecture commencée à 06:05:56 UTC ; rapport écrit à partir de 06:36 UTC, achevé à 06:43 UTC (`date -u`).
- **Empreintes (sha256)** des pièces lues :

  | pièce | sha256 |
  |---|---|
  | `prereg/brouillon-test-echelle-conscience-eval-v7.md` (texte relu ; conforme à son compagnon au début et à la fin de ma lecture) | `e6e8a864ea2b7865bbc658b5f9ed84e34b1bd62cb8223e90d23eb1177ccf2ee4` |
  | `prereg/brouillon-test-echelle-conscience-eval-v6.md` | `878958bf5de75d914efc24f2508ee33449dd50eaa014839d1d4eaf32f6c20032` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v6-cl5.md` | `4ea69784a824c2b05048fd9e794e8e9aede3b6b6739da62a515250cbc01fcb15` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v5-cl4.md` | `5728de4c2a4774ab3d96f267f91189dd6d860b4fb2fdef3edd41e910477ee592` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v4-cl3.md` | `a2f330f09df1d0cfb3188482331de3ba847133865f4764aa7a8b1cf11cf15896` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v3-cl2.md` | `9b476cf4b64a521f97cc7368ca60723e41390557291570fc6c08f30369b04803` |
  | `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md` | `70afa51997f66f882f79686765c9b1fdded6f0016007b626355b975abd9e673a` |
  | `echelle-v6/scripts/analyser_echelle_v6.py` (conforme au tableau, au compagnon et à l'objet du commit) | `da2fadad1b4748e99f80a59da5481159051005575001d55f2b22d9547d3b803c` |
  | `echelle-v6/scripts/surveiller_echelle_v6.sh` (idem) | `b83b907973c93cf73d1fc791f944734b36fbd6f14fd9a57366e22fc777366a02` |
  | `echelle-v6/scripts/lancer_echelle_v6.sh` (idem) | `344e6df8c246e09a56258b29a9c90362b7a343d167268358a3170651843ca706` |
  | `src/controle_ia/prereg.py` (inchangé depuis cl4 et cl5) | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
  | `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
  | `.claude/hooks/garde_calcul.py` (inchangé depuis cl4 et cl5) | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` |
  | `registres/go.md` (registre vivant ; état lu, le même que celui de cl5) | `a157cd2f1feff106bfbc5687e55221d2015b7c640e6fc0f2c719a019f58cf580` |
  | `docs/notes/echelle-conscience-eval/v6/consigne-contre-lecture-cl6.md` (ma consigne, identique au message reçu) | `8d2d6aa1e232d9b1f5cbc79d1571610c1af053dd55671aa4d325e3463c4a7ba0` |
  | `docs/notes/echelle-conscience-eval/v6/contre-lecture-cl5/scripts/banc_cl5.py` (générateur repris) | `2812e9985ded65eedcfb22b3e1cc35f32131d168e6425bdeadde7c4b7c052429` |
  | `docs/notes/echelle-conscience-eval/v6/contre-lecture-cl5/chaine-lanceur/LISEZ-MOI.txt` | `d29585910317a54f84c1a1b30f1dd955af9b0f967c2d10e5da55d435554f0545` |
  | `docs/notes/echelle-conscience-eval/v6/rejeu-bancs-cl5/rejeu_bancs_cl5_v6.py` | `df1cb6ecfb72ab152e3b284dc117c841fadbd3c8216d3a3b22bced0ebed935b8` |
  | `docs/notes/echelle-conscience-eval/v6/latence-surveillance/essai_latence_surveillance.py` | `a0972486aef4f8ea5a8afe1d5df9f183c6b690ff7d65604490b9b237a5df4a7c` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `-v2.md`, `-v3.md` | `134040bd…`, `fe1e93c1…`, `9d03d3b2…` (conformes à leurs compagnons) |
  | les 24 traces du tableau « Traces » du texte | toutes conformes (voir plus bas) |

- **Code relu** dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` :
  - branche `outils/echelle-conscience-eval-v6`, tête `b8b76650d29e213cf5da9b8fccee22cad9ba98c5` : c'est le commit attendu ; la branche de suivi `origin/outils/echelle-conscience-eval-v6` pointe au même endroit ; `origin` est `lciric/controle-ia-travail` ;
  - arbre propre avant et après mes essais (seuls les deux `__pycache__` ignorés de `echelle-v3/`, antérieurs) ; l'index de l'arbre de travail n'a pas bougé (heure de modification 05:39:13 UTC, avant ma lecture ; tous mes appels à l'analyse passaient `GIT_OPTIONAL_LOCKS=0`) ;
  - **44 empreintes complètes sur 44** concordent : les 20 outils avec le fichier, le compagnon et l'objet du commit ; les 24 traces avec le fichier et le compagnon ; et les 17 empreintes abrégées citées dans le corps du texte (`sorties/sortie-verif-empreintes-v7.txt`) ;
  - différence de chaque script et de chaque test v5 → v6 (`diffs/`) : la mesure, l'amorce, le script d'instance, le choix d'offre, le contrôle du prix, le contrôle du GO, le contrôle lexical et la répétition ne changent que de nom et de commentaires ; stimuli, constructeur et rapport de construction identiques à l'octet à ceux de `echelle-v5/` (`cmp`) ; l'analyse change dans `conditions`, `issues_tenues`, `premiere_etape`, `membres`, `lire_sens`, `reserves`, `lire` et le calcul des drapeaux de profondeur de la fuite de signe inverse ; la surveillance et le lanceur changent comme le texte le dit.
- **Lu en entier** :
  - les brouillons v7 et v6, et leur différence mot à mot (`diff-v6-v7-mots.txt`) ;
  - cl5 en entier, et ses pièces : `chaine-lanceur/LISEZ-MOI.txt`, les douze scripts, les sorties (cas limites, essai de correction, dépense au pire, chaîne du lanceur, bancs), les 69 compagnons vérifiés ;
  - les constats de cl1 à cl4, et en détail CLZ-05, CLZ-08 et CLW-02 (les plus proches de mes constats) ;
  - tout `echelle-v6/` : quinze scripts, quatre fichiers de tests ; les stimuli par Python seulement ;
  - les gardes héritées : `exiger_prereg_scelle` et ce qu'elle appelle (`verifier`, `lire_compagnon`, `problemes`, `sections`) ; `garde_calcul.py` en entier ; l'en-tête de `registres/go.md` et ses lignes de type « calcul » ;
  - les traces nouvelles de `docs/notes/echelle-conscience-eval/v6/` : simulation, audit de la simulation (script et sortie), rejeu des bancs de cl5 (script, sortie, résumé, `LISEZ-MOI.txt`), essai de latence (script, sorties), répétition (résumé, commit, empreintes, analyse du modèle minuscule ; 18 compagnons vérifiés), offre de référence v4, contrôle lexical v6, sortie des tests ;
  - les passages des cartes v1 à v3 que le texte cite (carte v1, l. 114, 268, 289, 313, 358 et 359 ; carte v2, l. 16, 18, 24 et 57 ; carte v3, l. 15, 17, 79 à 84, 157 et 201).
- **Interdits respectés** :
  - aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt (seulement des listes de dossiers nommés et des dossiers de traces) ;
  - aucun réseau ; aucune commande vastai réelle (deux faux outils dans mon bac à sable) ; aucun lancement ; aucune écriture git ; rien de modifié hors de mon bac à sable (vérifié en fin de lecture : brouillon v7 conforme à son compagnon, arbre de travail propre et index inchangé, aucun fichier de `prereg/` ni de `docs/notes/echelle-conscience-eval/v6/` plus récent que mon départ) ;
  - `registres/decisions.md` et `registres/etat.md` ont changé à 06:29 et 06:30 UTC, pendant ma lecture : ce n'est pas moi ; `registres/go.md`, que le contrôle du GO relit, n'a pas changé (`a157cd2f…`) ;
  - aucune clé ni aucun jeton cherché, affiché ou écrit ;
  - tous les essais avec `TMPDIR`, `HF_HOME` et `--basetemp` dans le bac à sable, `-B` et `PYTHONDONTWRITEBYTECODE=1`, fils de calcul à un.
- **Essais** (scripts jetables et sorties dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v7/`) :
  - tests du commit : **274 passed in 405.29s**, avec le modèle minuscule local (`sorties/tests-cl6.txt`) ; décompte par fichier : 187, 5, 8 et 74, comme le texte ;
  - lecture v6 sur les six cas fabriqués de cl5 et sur sept cas fabriqués nouveaux (`scripts/cas_limites_lire_v6.py`, `sorties/sortie-cas-limites-lire-v6.txt`) ;
  - rejeu des bancs de cl5, de deux façons indépendantes du script de l'auteur : `lire()` v6 appliquée aux intervalles que cl5 a consignés pour ses 106 analyses (`scripts/relire_bancs_cl5_v6.py`) ; et six analyses refaites au calcul complet, générateur de cl5 recopié à l'identique (`scripts/banc_cl6.py`, `banc/banc-cl6-rejeu-partiel.jsonl`) ;
  - bancs nouveaux, analyse v6 telle quelle (mode répétition) : 28 analyses en dimension 64, 32 en dimension 256 (26 puis 6), deux en dimension 256 à 2 000 tirages, 8 en dimension 64 au tau 0,4 (`banc/`) ;
  - reproduction de la simulation scellée au commit (`simulation/`) ; relecture de son tableau case par case ; comparaison avec la simulation v3 (prix de la symétrie) ; relecture de l'audit ;
  - surveillance v6 jouée telle quelle avec un faux outil, **aux réglages réels** (pause de 60 s, appels bornés à 30 s), et avec des réglages d'essai laissés dans l'environnement (`scripts/latence_reelle_v6.py`, `scripts/pas_s_illisible.py`) ;
  - forme exacte de la ligne du GO jouée contre le contrôle du GO et contre la garde de calcul, sur un faux registre (`faux-depot-go/`, `sorties/sortie-forme-go-v6.txt`) ;
  - choix d'offre v6 rejoué sur la trace des 45 offres (`offres/`) ; conformité du brouillon par `problemes()` ;
  - règle candidate pour CLU-01 évaluée sur les bancs existants (`scripts/ecart_entre_sens.py`).

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLU-01** : la règle du même modèle n'est appliquée qu'à la fuite de signe inverse. La classe d'artefacts que CLV-01 a ouverte (deux signatures d'un seul jeu, à des tailles différentes) fabrique encore « positif » et « inverse » quand les deux signatures sont **de signes opposés** et que les deux tailles fuient autant (vérité H_0). En dimension 256, sous H_0 (λ du concept 0,5 aux deux tailles) : **« positif » 6 fois sur 10, sans aucune réserve** ; « inverse » 2 fois sur 4 dans le miroir ; confirmé à 2 000 tirages. (En dimension 64, celle de la simulation du texte, où le recouvrement fortuit des signatures brouille le mécanisme, mes essais ne prononcent rien ; la lecture, elle, prononce « positif », « inverse » et « nul » sans réserve sur les intervalles fabriqués de cette classe.) L'écart d'échelle y est porté par le 8B dans un sens et par le 70B dans l'autre : c'est, mot pour mot, ce que l'hypothèse range dans H_0 (« chez des modèles différents d'un sens à l'autre », l. 87). Le texte affirme au contraire que « la règle du même modèle » écarte les signatures croisées (l. 324), et la phrase R3 (l. 212) ne porte que sur des signatures croisées de même signe sans fuite du concept.

Corrections à faire avant le scellement :

- CLU-01 (bloquant) : soit une garde mécanique (condition ou réserve obligatoire sur l'écart du λ d'un même modèle entre les deux sens), soit, au minimum, la limite, la phrase R3, la phrase des mesures et un déclencheur R4 réécrits, avec la classe ajoutée à la simulation. Si `lire()` change : des noms nouveaux (R12), un commit et des empreintes nouveaux, les tests et la simulation rejoués. Dans tous les cas : un texte nouveau, et une contre-lecture neuve des parties changées (R2).
- CLU-02 (à corriger) : les réglages d'essai de la surveillance, lus dans l'environnement sans contrôle, peuvent ôter la borne des appels ou tuer la surveillance en silence.
- Les remarques CLU-03 à CLU-05 sont à reprendre au passage.

## Ce qui tient

- **Empreintes et commit** : 44 sur 44, et les 17 abrégées ; tête de branche = commit attendu ; arbre propre ; noms nouveaux libres (`prereg/test-echelle-conscience-eval-v7.md` absent ; aucune référence `donnees/echelle…` dans le dépôt local) ; le brouillon n'a qu'un manque pour `problemes()` : la section « Contre-lecture » à remplir.
- **Tests** : 274 passent chez moi (405 s), comme la trace (403 s). Les 67 cas de `test_lire` et leurs 67 miroirs sont là ; les trois tests des conditions manquantes aussi ; les décomptes du tableau R5 (5, 8, 67, 12, 11, 10 refus de partir, six réponses illisibles, onze artefacts d'offre) concordent avec le code.
- **CLV-01 levé pour la fuite de signe inverse, preuve rejouée** :
  - le cas fabriqué de cl5 (petit sous −δ en a→b seulement, grand en b→a seulement) rend « désaccord des deux sens », avec les conditions manquantes modèle par modèle ; le témoin (même modèle dans les deux sens) rend « fuite de signe inverse (petit) » ;
  - `lire()` v6 appliquée aux intervalles consignés par cl5 : **105 lectures sur 106** identiques au rejeu versé (lecture, réserves, issues tenues). L'écart restant (graine 10100) tient à l'arrondi de cl5 : sa borne basse de spécificité est consignée « 0,0 », la valeur exacte est positive ; refaite au calcul complet, cette analyse rend la lecture du rejeu versé ;
  - six analyses refaites au calcul complet (11000, 11002, 11102, 11104, 9902, 10100) : intervalles **identiques** à ceux de cl5, lectures identiques au rejeu versé ;
  - les 16 « fuite de signe inverse » de la v5 sous signatures croisées de même signe deviennent « désaccord des deux sens » ; les autres lectures ne changent que de nom de taille (comparaison faite par mes soins sur les 106).
- **Concordance du texte et du code** (`conditions`, `issues_tenues`, `premiere_etape`, `membres`, `lire_sens`, `manquantes`, `reserves`, `lire`, `principal`) :
  - ordre de lecture en cinq étapes, les deux fuites de signe inverse dans la même étape ; conditions P(s) et I(s), inégalités strictes (bornes de λ, de Δλ), larges (bandes de « pas de fuite » et de « nul », certification ≥ 0,70) ;
  - étape 2 : échecs de certification combinés ; issue commune par modèle pour la fuite de signe inverse ; « (petit et grand) » ; réserve obligatoire pour une issue d'un seul sens placée avant l'étape prononcée **ou dans la même** ; désaccord ; non confirmé ; aucune réserve pour « non confirmé », « désaccord », « indécis » et les échecs ; conditions manquantes de **chaque** issue tenue dans un seul sens ;
  - réserves « fuite non spécifique » et « profondeur » restreintes aux modèles prononcés, et qui les nomment (vérifié sur des cas fabriqués : la réserve du grand nomme « (grand) » ; un drapeau de profondeur du grand est sans effet quand seul le petit est prononcé) ;
  - `SEUILS`, `ATTENDUS` (couches 8, 12, 16, 20 et 20, 30, 40, 50), choix de L\*, tirage conditionné (≈ 1 sur 7 776 par jeu), graines par `SeedSequence`, mode décisif ; une phrase par issue ; commandes du lancement, de la surveillance et de l'analyse ; liste d'arrêt conforme au code, ligne à ligne.
- **Simulation** : le tableau du texte transcrit fidèlement la sortie scellée, case par case, réserves comprises (41 cases, 164 analyses) ; 20 noms sur 26 sont atteints ; la phrase R3 est exacte sur ses 80 analyses ; l'audit dit vrai (cosinus de −0,284 à +0,324 ; λ effectif −0,352 pour la graine 3138 ; composantes de −0,151 à +0,307 pour les neuf lectures des doubles signatures ; huit lectures changées, toutes sous les signatures croisées négatives au tau 0,4) ; l'audit refait bien les tirages du générateur de la simulation. **Reproduite à l'octet près** : ma sortie, faite au commit `b8b7665` avec le script du commit, trois processus et des fils à un (06:29:33 à 06:42:11 UTC), a l'empreinte de la sortie scellée, `bb7b867e…` (`simulation/sortie/`).
- **Prix de la symétrie** (CLV-03) : sur les 17 cases communes avec la v3, quatre changent (H_0 et « pas de fuite » au tau 0,8, H_A faible aux tau 0,4 et 0,8) exactement comme le texte le dit ; les treize autres gardent leur décision (une seule change de nom : « fuite de signe inverse » devient « (petit) »).
- **Surveillance aux réglages réels** (CLV-02), faux outil, plafond placé juste après le départ : appels de 29 s, arrêt demandé **56,5 s** après le plafond ; appels bloqués (300 s) coupés à 30 s, **58,6 s** ; appels instantanés et plafond 40 s après le départ, la pause s'arrête au plafond, **0,7 s**. La borne « deux appels, soit 60 s, puis 30 s pour l'arrêt » tient donc, avec les réglages par défaut (voir CLU-02 pour les autres).
- **Lanceur et surveillance du commit** (CLV-06) : comparaison des empreintes faite avant toute création ; empreinte attendue de la surveillance écrite dans `lancement.txt` et relue avant toute action ; tests du lanceur modifié et des empreintes fausse ou absente.
- **Forme du GO** (CLV-05) : la ligne écrite dans « Dépense », jouée sur un faux registre, passe le contrôle du GO (« conforme ») et la garde de calcul ; « 8,00 USD » passe ; « 8 USD au pire » et « 8 $ » sont refusés (« plafond illisible ») ; le registre réel est inchangé depuis cl5.
- **Dépense** :
  - choix d'offre v6 rejoué sur les 45 offres : offre 50510069, 7 200 s, pire 7,0311 USD, estimé 5,4044, attendu 3,8072, comme la trace et le texte ; la seconde offre conforme est à 8,00 USD tout juste ;
  - calcul inchangé depuis la v5 (différence de commentaires seulement) : le balayage de cl5 (30 308 offres, 196 s de retard au plus pour tenir sous 8 USD) vaut donc pour la v6 ; avec la borne de 90 s de la surveillance, il reste 106 s pour que l'arrêt prenne effet ;
  - téléchargement limité à `*.json` et `model-*.safetensors` (pas le dossier `original/` des dépôts Llama) : les 157,19 Go tracés sont bien ce qui descend.
- **Répétition** : résumé identique à l'octet à celui de la v5, mais bien produit au commit `b8b7665` (`COMMIT.txt`, journaux sous `travail-echelle-v6`) ; 18 compagnons conformes ; l'analyse du modèle minuscule lit « non certifiable » dans les deux sens.
- **Gardes héritées** : code inchangé depuis cl4 (mêmes empreintes) ; `exiger_prereg_scelle` exige le compagnon conforme et toutes les sections remplies.
- **R7** : les citations du texte (inchangées depuis le v6) concordent avec les cartes, pages comprises, réserve de circularité de Xiong et al. comprise.
- **R9, R10, R12** : `SeedSequence`, versions (Python, torch, transformers, numpy, cartes) et commit consignés par la mesure, l'analyse et la simulation ; arrêts par identifiant partout ; noms neufs (`…_v6`, `analyse-echelle-v6.json`, branche `donnees/echelle-conscience-eval-v6`, texte scellé `…-v7.md`).
- **R3, hors CLU-01** : la lecture est mécanique, les graines fixées, l'analyse décisive déterministe à commit, numpy et entropie donnés ; je n'ai trouvé aucun autre degré de liberté qui permette de viser un signe.

## Traitement des constats de cl5

| constat de cl5 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLV-01 fuite de signe inverse sans qu'aucun modèle ne la tienne dans les deux sens | bloquant | **traité pour la fuite de signe inverse** ; la classe d'artefacts reste ouverte pour « positif », « inverse » et « nul » (CLU-01) | Lecture modèle par modèle, réserves restreintes et nommées, phrase qui nomme la taille. Cas fabriqué de cl5 : « désaccord des deux sens ». Rejeu : 105 lectures sur 106 identiques au rejeu versé (la 106e : arrondi), six analyses refaites au calcul complet, intervalles identiques à cl5. Les 16 fuites croisées deviennent « désaccord ». Mais la même classe, de signes opposés, sous une fuite égale non nulle, fabrique « positif » sans réserve, et le texte dit cette classe écartée (l. 324) |
| CLV-02 retard d'arrêt de la surveillance | remarque | **traité**, un reste | Heure relue, plafond testé deux fois, pause bornée, appels bornés à 30 s : 56,5 s, 58,6 s et 0,7 s aux réglages réels (mon essai). Restes : la borne dépend d'une variable d'environnement non contrôlée (CLU-02) ; l'essai versé et le test sont faits avec une pause de 1 s, qui ne joue pas le cas réel (CLU-03) |
| CLV-03 « prix de la symétrie » | remarque | **traité** | Phrase exacte sur les simulations v3 et v6 |
| CLV-04 portée des phrases R3 et de la limite | remarque | **traité en partie** | Les huit signatures d'un seul jeu simulées, phrase R3 et limite réécrites, perte de puissance écrite. Restes : la limite sur les signatures croisées est fausse pour « positif » et « inverse » (CLU-01) ; le compte des bancs rejoués omet un cas de double signature sous H_A (CLU-05) |
| CLV-05 forme du GO | remarque | **traité** | Ligne exacte jouée : conforme pour les deux gardes ; « 8 USD au pire » refusé |
| CLV-06 lanceur et surveillance hors du commit | remarque | **traité** | Comparaisons d'empreintes avant toute création et avant toute action ; tests du lanceur modifié et de l'empreinte attendue fausse ou absente |
| CLV-07 conditions manquantes de la première issue | remarque | **traité** | Chaque issue tenue dans un seul sens reçoit ses conditions manquantes (mes cas fabriqués et les trois tests) ; « non confirmé » et « désaccord » sans réserve, et le texte le dit |
| CLV-08 deux chemins sans test | remarque | **traité** | Huit tests d'intégration sur quatre couches (cas sain et artefact, « nul », « pas de fuite », chaque fuite de signe inverse) ; trois tests de l'extraction de l'empreinte du texte scellé |

Bilan : 8 constats traités, dont 3 avec un reste (CLV-01 pour les autres issues, CLV-02, CLV-04) ; aucun non traité.

## Constats nouveaux

### CLU-01 — BLOQUANT — La règle du même modèle ne vaut que pour la fuite de signe inverse : deux signatures d'un seul jeu, à des tailles différentes et de signes opposés, fabriquent « positif » ou « inverse » sous H_0, sans réserve

- **Localisation** :
  - `analyser_echelle_v6.py` : `conditions`, l. 459–470 (« positif », « inverse » et « nul » ne regardent, dans chaque sens, que Δλ_s et des bornes de λ_s par modèle, jamais l'accord d'un même modèle entre les deux sens) ; `lire`, l. 562 (issue commune comparée par son nom) ; `reserves`, l. 534–549 (aucune réserve sur cet accord) ;
  - brouillon v7 : Hypothèse, l. 77 (« pour la fuite de signe inverse, chez le même modèle ») et l. 87 (H_0 : « ou chez des modèles différents d'un sens à l'autre ») ; Mesures, l. 135 ; R3, l. 212 ; audit, l. 215 ; limites, l. 318–324, surtout l. 324 ; traitement de CLV-01, l. 433.
- **Constat** :
  - Le principe que pose le texte : « Une fuite du concept, elle, se retrouve dans les deux sens, **chez le même modèle** » (l. 135). Sous un effet d'échelle vrai, λ_a→b(8B) ≈ λ_b→a(8B) et λ_a→b(70B) ≈ λ_b→a(70B).
  - La v6 n'applique ce principe qu'à la fuite de signe inverse. « Positif » se juge sens par sens sur Δλ_s et sur des bornes de chaque modèle, puis par son seul nom.
  - **Mécanisme** : les deux tailles fuient autant le long du concept (λ = 0,5 aux deux : vérité H_0) ; le format pousse en plus, au 8B, la signature du jeu a (vers le haut), et au 70B, la signature du jeu b (vers le bas). La première ne déplace que le sens a→b : λ_a→b(8B) monte, Δλ_a→b > δ. La seconde ne déplace que le sens b→a : λ_b→a(70B) baisse, Δλ_b→a > δ. Dans chaque sens, toutes les conditions de « positif » tiennent : λ(8B) reste au-dessus de δ grâce à la fuite commune, λ(70B) reste entre −δ et 1. « Positif » est donc commun, et prononcé.
  - L'écart d'échelle est alors porté par le 8B dans un sens, par le 70B dans l'autre : c'est le cas que H_0 nomme (l. 87), et celui que CLV-01 a fermé pour la seule fuite de signe inverse. Le miroir (signes inversés) fabrique « inverse ». Le témoin ν ne voit pas les poussées sur une signature (CLY-01) : la réserve « fuite non spécifique » ne se déclenche pas.
  - **Pourquoi la simulation ne l'a pas vu** : ses signatures croisées sont toutes de même signe, sans fuite du concept (α = 0, l. 198–201), et le seul cas de signes opposés est sous H_A (l. 206). À α = 0, « positif » ne peut pas tenir : dans le sens que la signature du 8B ne touche pas, λ(8B) ≈ 0 < δ. Or H_0 avec une fuite égale non nulle est le H_0 le plus plausible au vu de la prédiction (λ(8B) ≈ 0,5 à 1). De plus, en dimension 64, le recouvrement fortuit d'une signature avec le contexte (cosinus jusqu'à ±0,32, l. 214) brouille ce mécanisme ; le texte rappelle lui-même qu'en 4 096 ou 8 192 dimensions ce recouvrement serait 8 à 11 fois plus petit.
  - Conséquences sur le texte : la limite « la règle du même modèle les écarte » (l. 324) est fausse pour « positif » et « inverse » ; la phrase R3 (l. 212) ne couvre que des signatures croisées de même signe sans fuite ; l'hypothèse (l. 77) et les mesures (l. 135) réservent la règle du même modèle à la fuite de signe inverse ; la lecture mécanique contredit H_0 tel qu'il est écrit.
- **Preuve** :
  - Cas fabriqués, `lire()` v6 telle quelle (`sorties/sortie-cas-limites-lire-v6.txt`) :
    - a→b : λ(8B) [0,85 ; 1,15], λ(70B) [0,40 ; 0,60], Δλ [0,35 ; 0,65] ; b→a : λ(8B) [0,40 ; 0,60], λ(70B) [−0,10 ; 0,10], Δλ [0,35 ; 0,65] : **« positif », aucune réserve** ;
    - le miroir : **« inverse », aucune réserve** ;
    - a→b : les deux modèles à [0,05 ; 0,35] ; b→a : les deux à [0,85 ; 1,15] ; Δλ dans la bande des deux côtés : **« nul », aucune réserve**, alors que chaque modèle change de 0,8 d'un sens à l'autre.
  - Banc, analyse v6 telle quelle, générateur de cl5 recopié à l'identique, dimension 256, tau 0,15, 300 tirages (`banc/banc-cl6-d256.jsonl`, `banc/banc-cl6-d256-suite.jsonl`, `banc/banc-cl6-d256-n2000.jsonl`) :

    | cas (graines) | vérité | lectures |
    |---|---|---|
    | témoin H_0 : λ 0,5 et 0,5, sans signature (22000 à 22004) | H_0 | nul 3 |
    | témoin H_A : λ 1,0 et 0,2, sans signature (22100 à 22104) | H_A | positif 3 |
    | H_0 (0,5 et 0,5) ; jeu a +1,3 au 8B, jeu b −1,3 au 70B (22200 à 22218) | H_0 | **positif 6, sans réserve** ; positif non confirmé 2 ; indécis 2 |
    | idem, signes inversés : jeu a −1,3 au 8B, jeu b +1,3 au 70B (22400 à 22406) | H_0 | **inverse 2, sans réserve** ; inverse non confirmé 2 |
    | H_0 (0,5 et 0,5) ; jeu b +1,3 au 8B, jeu a −1,3 au 70B (22300 à 22306) | H_0 | indécis 3 ; positif non confirmé 1 |
    | H_A (1,0 et 0,2) ; jeu a −2,3 au 8B, jeu b +2,3 au 70B (22500 à 22506) | H_A | indécis 4 (aucun « nul ») |
    | H_A (1,0 et 0,2) ; jeux a et b −2,3 au 8B (22600 à 22606) | H_A | indécis 4 (aucun « nul ») |

    - à **2 000 tirages** (la taille du bootstrap décisif) : la graine 22200 rend **« positif »**, sans réserve ; la graine 22400 rend **« inverse »**, sans réserve ;
    - exemple, graine 22200 (2 000 tirages) : a→b, λ(8B) [0,84 ; 1,12], λ(70B) [0,32 ; 0,52], Δλ [0,38 ; 0,72] ; b→a, λ(8B) [0,48 ; 0,69], λ(70B) [−0,12 ; 0,11], Δλ [0,42 ; 0,71] ; spécificités [0,25 ; 0,69] et [0,29 ; 0,74] : le témoin ne voit rien.
  - En dimension 64 (celle de la simulation du texte), je n'ai pas obtenu de lecture prononcée : au tau 0,4, λ 0,5 et 0,5, jeu a +0,9 au 8B et jeu b −0,9 au 70B (graines 23000 à 23014), indécis 6, positif non confirmé 1, nul non confirmé 1 ; au tau 0,15 avec ±3, indécis et non confirmés. Les intervalles y sont plus larges et le recouvrement fortuit des signatures avec le contexte y brouille le mécanisme. Je le dis franchement : la fréquence de l'artefact dépend de la dimension et du bruit, et je ne sais pas la chiffrer pour un vrai flux résiduel. Mais le texte soutient lui-même que ce recouvrement fortuit y est 8 à 11 fois plus petit qu'en dimension 64 (l. 214) ; c'est le cas de la dimension 256, pas de la dimension 64, qui s'en approche. Et les cas fabriqués montrent que rien, dans la lecture, n'écarte cette classe.
  - Une mesure simple les sépare (`sorties/sortie-ecart-entre-sens.txt`, estimations ponctuelles, analyses qui prononcent une issue) : l'écart |λ_a→b(m) − λ_b→a(m)| du modèle le plus touché vaut **0,41 à 0,57** dans les « positif » et « inverse » croisés ci-dessus (0,43 à 1,39 dans les fuites croisées de cl5) ; **0,04 à 0,14** sous H_A sans signature ; 0,02 à 0,10 sous H_0 et pour les fuites faibles et égales ; 0,10 à 0,20 avec un contexte du jeu b plus faible (λ 0,15) ; 0,03 à 0,27 sous les doubles signatures, que cette mesure ne voit pas (c'est la limite écrite). Une signature d'un seul jeu sous H_A vrai donne 0,22 à 0,40 : la mesure la signalerait aussi, à juste titre.
- **Correction** :
  - **(a) Garde mécanique (préférée)** : étendre le principe du même modèle aux issues prononcées sur Δλ. Calculer, sur les mêmes tirages (le bootstrap est déjà apparié entre les sens), l'intervalle de λ_a→b(m) − λ_b→a(m) pour chaque modèle ; puis :
    - soit une **condition** de « positif », « inverse » et « nul » : pour chaque modèle, cet intervalle rencontre [−δ ; δ] (ou y est inclus) ;
    - soit une **réserve obligatoire** « écart porté par des modèles différents d'un sens à l'autre (modèle nommé) », quand l'intervalle d'un modèle est hors de [−δ ; δ] ; elle signale aussi, à juste titre, une différence de force du contexte entre les jeux (CLZ-02) ;
    - tests : les trois cas fabriqués ci-dessus et leurs miroirs (sens échangés), un cas sain (H_A sans signature) ; intégration : signatures croisées de signes opposés sous une fuite égale, dans les deux ordres ; simulation : la même classe sous H_0 (0,5 et 0,5), aux tau 0,15 et 0,4, en dimension 64 et, si possible, plus grande ; H_A avec un contexte du jeu b plus faible, pour mesurer les fausses alertes.
  - **(b) À défaut, correction du texte seulement** : réécrire la limite l. 324 (la règle du même modèle n'écarte les signatures croisées que pour la fuite de signe inverse ; de signes opposés, sous une fuite égale, elles fabriquent « positif » ou « inverse », et peuvent en principe masquer un écart vrai en « nul ») ; borner la phrase R3 (l. 212) à ce qui est simulé ; dire en l. 77 et 135 que la règle n'est appliquée qu'à la fuite de signe inverse ; ajouter à R4 un déclencheur d'audit et de réserve : « λ d'un même modèle qui diffère de plus de δ d'un sens à l'autre » ; ajouter la classe à la simulation.
  - Dans les deux cas : texte nouveau et contre-lecture neuve des parties changées ; avec (a), noms, commit, tests et simulation nouveaux.

### CLU-02 — À CORRIGER — Les réglages d'essai de la surveillance sont lus dans l'environnement sans contrôle : la borne de 30 s peut sauter en silence, et la surveillance peut mourir sans arrêter l'instance

- **Localisation** : `surveiller_echelle_v6.sh`, l. 29–31 (`PAS_S`, `ATTENTE_ARRET_S`, `APPEL_S` pris tels quels), l. 47, 62, 72 et 75 ; brouillon v7, l. 55, 373 (« chaque appel à vastai de la surveillance est borné à 30 s »), l. 434.
- **Constat** :
  - `APPEL_S` sert de borne à `timeout`. Or `timeout 0` n'impose **aucune** borne. Une valeur laissée dans l'environnement par un essai suffit, et rien ne la consigne : ni `etats.txt` ni `arret.txt` ne disent la borne employée.
  - Une valeur illisible de `PAS_S` fait sortir la surveillance dès la première pause, avec un code 1 que l'en-tête ne documente pas (codes 0, 2, 5, 6, 7), sans demander l'arrêt et sans écrire `arret.txt`. L'instance n'est plus bornée que par l'amorce. C'est le repli silencieux que R5 interdit.
  - Les valeurs par défaut sont justes : le défaut n'apparaît que si l'environnement de la session porte ces variables. Mais le texte présente la borne comme une garde (liste d'arrêt, l. 373).
- **Preuve** (`sorties/sortie-latence-reelle-v6.txt`, `sorties/sortie-pas-s-illisible.txt`) :
  - `APPEL_S=0`, appels de 45 s : arrêt demandé **88,8 s** après le plafond (au lieu de 60 s au plus) ; `arret.txt` ne dit rien du réglage ; avec des appels plus longs, aucune borne ;
  - `PAS_S=abc`, plafond 20 s après le départ : sortie en 0,1 s, **code 1**, aucun arrêt demandé, aucun `arret.txt`.
- **Correction** : contrôler ces réglages au départ (entiers ; `APPEL_S` dans [1 ; 30], `PAS_S` dans [1 ; 60], `ATTENTE_ARRET_S` dans [0 ; 60]), sinon refus de partir (code 2) ; écrire les valeurs employées en tête d'`etats.txt` et dans `arret.txt` ; tester `APPEL_S=0`, `APPEL_S=31` et `PAS_S=abc` comme artefacts. La surveillance change de toute façon de nom si CLU-01 impose un commit nouveau.

### CLU-03 — REMARQUE — L'essai de latence versé et le test des appels lents ne jouent pas la configuration réelle ; le test du plafond garde une latence de 80 s

- **Localisation** : `docs/notes/echelle-conscience-eval/v6/latence-surveillance/essai_latence_surveillance.py` et `resultat-latence.txt` ; `test_offre_et_surveillance_v6.py`, `surveiller` (l. 222 : `PAS_S="1"`), `test_surveillance_appels_lents` (l. 275–284), `depense_reelle_au_pire` (l. 63 : `latence_s=80`) ; `choisir_offre_v6.py`, l. 31 (commentaire « latence de la surveillance, ≈ 0,08 USD ») ; brouillon v7, l. 55, 402 et 411.
- **Constat** :
  - L'essai versé reprend la fonction `surveiller` des tests, donc une pause de **1 s**. Le défaut de la v5 tenait surtout à la pause de 60 s placée entre la lecture de l'heure et le test du plafond : avec une pause de 1 s, la v5 ne retarde que de 8,2 s (cl5 mesurait 291 s aux réglages réels). La comparaison « 8,2 s contre 3,3 s » ne montre donc ni le défaut corrigé, ni la borne réelle de la v6. Le test des appels lents a le même réglage ; dans ses deux cas, la pause bornée par le temps qui reste n'est jamais exécutée.
  - Le test du plafond de dépense sur tout le domaine compte 80 s de retard, sous les 90 s que la surveillance v6 admet ; le texte le dit (l. 402) et s'appuie sur le balayage de cl5 (196 s), mais la garde n'est pas testée à la borne qu'elle revendique.
- **Preuve** : mon essai aux réglages réels (pause 60 s, appels bornés à 30 s ; `sorties/sortie-latence-reelle-v6.txt`) : 56,5 s (appels de 29 s), 58,6 s (appels bloqués coupés à 30 s), 0,7 s (pause qui rencontre le plafond). La v6 tient sa borne ; c'est la preuve versée qui est faible.
- **Correction** : verser un essai aux réglages réels (ou citer celui-ci), avec un cas où la pause rencontre le plafond ; porter la latence du test de dépense à 196 s (la borne de la marge) ; mettre à jour le commentaire de `MARGE`.

### CLU-04 — REMARQUE — Le clonage sur l'instance n'est pas borné : l'hypothèse « l'amorce borne quand même le calcul » ne couvre pas cette étape

- **Localisation** : `amorce_echelle_v6.sh`, l. 59–60 (`git clone`, avant le `timeout` de la l. 64) ; brouillon v7, l. 57 et 63 (hypothèses dites).
- **Constat** : le délai de l'amorce ne borne que `echelle_instance_v6.sh`. Le clonage le précède, sans borne (git n'a pas de délai par défaut sur une liaison qui stagne). Si le clonage se bloque **et** que la surveillance ne tourne pas (session morte, ou CLU-02), les cartes restent louées sans borne jusqu'à la session suivante, bien au-delà de 8 USD. Le texte dit : « si la session locale meurt, l'amorce borne quand même le calcul » ; c'est vrai du calcul, pas du clonage. Le défaut est antérieur à la v6 (inchangé depuis la v4) ; aucune contre-lecture ne l'a relevé.
- **Correction** : `timeout 600 git clone …` (puis `refus`, qui écrit la ligne de fin) ; ou ajouter aux hypothèses dites « le clonage ne se bloque pas ». Les appels `git ls-remote`, `git fetch` et `vastai --version` du lanceur ne sont pas bornés non plus, mais ils précèdent toute création : sans coût.

### CLU-05 — REMARQUE — Phrases et tests à préciser

- **Issues atteintes** (l. 210) : « « fuite de signe inverse (grand) » et « (petit et grand) », prononcées ou non confirmées : il y faut un λ du 70B sous −δ dans les deux sens ». Or « (grand) non confirmé » est atteint (6 analyses, dans les deux sens), et « (petit et grand) non confirmé » demande les deux modèles sous −δ dans un même sens, pas le 70B dans les deux. Proposition : « « (grand) » prononcée, et « (petit et grand) », prononcée ou non confirmée : il y faut un λ du 70B sous −δ dans les deux sens, ou des deux modèles dans un même sens. »
- **Perte de puissance** (l. 323) : le compte des bancs de cl5 rejoués (« indécis 11, positif non confirmé 3, positif 2, sur 16 ») omet `masque_double_t015`, une double signature négative au 8B sous H_A (« positif » 3, « nul non confirmé » 1). Avec lui : 20 analyses ; et un « nul » y est lu dans un sens. « Aucune n'a fabriqué de « nul » » reste vrai des issues prononcées : le dire ainsi.
- **Prix de la symétrie** (l. 222) : « les 13 autres cases communes ne changent pas » ; l'une change de nom (« fuite de signe inverse » devient « (petit) ») : écrire « ne changent pas de décision ».
- **Tests des réserves** : `test_lire` et `test_lire_miroir` ne vérifient que le **nombre** de réserves. Le modèle que nomme la réserve « fuite non spécifique (petit | grand) », et le sens que nomme « lu dans le seul sens s », ne sont vérifiés par aucun test (je les ai vérifiés à la main : justes). Ajouter l'assertion du texte des réserves dans les cas restreints aux modèles et dans les cas de réserve de même étape.

## Annexe — bancs et essais de cl6

- Générateur : `fabriquer` de `banc_cl5.py`, recopié à l'identique (contrôle par comparaison du corps de la fonction, docstring mise à part) ; l'analyse est `analyser_echelle_v6.py` du commit, importée par chemin, mode `--repetition`, 300 tirages sauf mention.
- Bancs en dimension 64 (`banc/banc-cl6-cas.jsonl`, 28 analyses) : les signatures croisées de signes opposés de forte amplitude (±3 au tau 0,15) y sont dominées par le recouvrement fortuit des signatures avec le contexte ; aucune issue n'y est prononcée sous H_0 (indécis, non confirmés, une « fuite de signe inverse (grand) non confirmé ») ; témoin H_0 sans signature : « nul » 4 sur 4.
- Rejeu partiel au calcul complet (`banc/banc-cl6-rejeu-partiel.jsonl`) : 6 analyses de cl5, intervalles identiques à ceux de cl5, lectures identiques au rejeu versé.
- Pièces, dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v7/` :
  - `scripts/` : `verif_empreintes_v7.py`, `cas_limites_lire_v6.py`, `relire_bancs_cl5_v6.py`, `banc_cl6.py`, `latence_reelle_v6.py`, `pas_s_illisible.py`, `ecart_entre_sens.py` ;
  - `sorties/` : `tests-cl6.txt`, `tests-cl6-debut.txt`, `sortie-verif-empreintes-v7.txt`, `sortie-cas-limites-lire-v6.txt`, `sortie-relire-bancs-cl5-v6.txt`, `sortie-latence-reelle-v6.txt`, `sortie-pas-s-illisible.txt`, `sortie-forme-go-v6.txt`, `sortie-ecart-entre-sens.txt`, `index-avant.txt` ;
  - `banc/` : six fichiers `banc-cl6-*.jsonl`, leurs journaux et heures ;
  - `simulation/` : reproduction de la simulation (sortie, journal, heures) ;
  - `latence-reelle/`, `latence-pas-s/` (faux outil, `lancement.txt`, sorties de la surveillance) ; `faux-depot-go/` (faux registre et copie de la garde) ; `offres/` (choix d'offre rejoué) ; `diffs/` (v5 → v6) ; `diff-v6-v7-mots.txt`.
