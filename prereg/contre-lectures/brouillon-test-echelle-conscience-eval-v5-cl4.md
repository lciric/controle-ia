# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v5) — cl4

- **Rôle** : sous-agent neuf, quatrième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v5, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 à 3 (cl1, cl2, cl3).
- **Heure** : 27 octobre 2026. Lecture commencée à 03:10:23 UTC, rapport écrit à partir de 03:38:52 UTC (`date -u`).
- **Empreintes (sha256)** :

  | pièce | sha256 |
  |---|---|
  | `prereg/brouillon-test-echelle-conscience-eval-v5.md` (texte relu ; conforme à son compagnon à 03:10 et à 03:38, inchangé pendant ma lecture) | `1111d89a9b745ad043736aa65ce9bb6c86a6dfcbfcbde167b741a7016a8212ee` |
  | `prereg/brouillon-test-echelle-conscience-eval-v4.md` | `8c0d19dc65d2e0bf2b51f248077a8bea861b266c7da9df081a6fc8d7d646f523` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v4-cl3.md` | `a2f330f09df1d0cfb3188482331de3ba847133865f4764aa7a8b1cf11cf15896` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v3-cl2.md` | `9b476cf4b64a521f97cc7368ca60723e41390557291570fc6c08f30369b04803` |
  | `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md` | `70afa51997f66f882f79686765c9b1fdded6f0016007b626355b975abd9e673a` |
  | `echelle-v4/scripts/analyser_echelle_v4.py` (conforme au tableau, au compagnon et à l'objet du commit) | `3e1c341a4ba97a148da9699c7550ce6fc85e92129e3a41b9c486efeff44c6c02` |
  | `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
  | `.claude/hooks/garde_calcul.py` | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md` | `134040bd9a126dce4592aa3b357375f0209f987610d3be21a6848f647eaf59b4` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v2.md` | `fe1e93c1efe7c9117c9f0b22711912394c5b40d0180b904bf61e324cf0943d3a` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v3.md` | `9d03d3b212ca43d3eb905413f95f808ef2bc90376b284804a9ed1dbd28ddc3de` |
  | `registres/decisions.md` (ligne R-530 ; registre vivant, sans compagnon) | `ce9b1bf9eff611ad0bf2a03f2aba7abe4a11bb34bf1cd0586d9e1df82a6931b1` |
  | `registres/go.md` (état lu par la garde de calcul pendant mes essais ; registre vivant) | `a157cd2f1feff106bfbc5687e55221d2015b7c640e6fc0f2c719a019f58cf580` |

- **Code relu** dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` :
  - branche `outils/echelle-conscience-eval-v4`, tête `f579930842ab633cdced18a13f82d77bb467ca7f` : c'est le commit attendu, et la branche distante locale pointe au même endroit ;
  - arbre propre avant et après mes essais : seuls les deux `__pycache__` ignorés de `echelle-v3/`, datés de 01:11 à 01:15 UTC, avant ma lecture ; l'index de l'arbre de travail n'a pas bougé depuis 02:56:37 UTC (mes appels passaient `GIT_OPTIONAL_LOCKS=0`, pour que le `git status` de l'analyse n'écrive rien) ;
  - les 34 empreintes complètes du texte (18 outils, 16 traces) concordent avec les fichiers et leurs compagnons ; pour les 18 outils, aussi avec les objets du commit (`scripts/verif_empreintes.py`, `sorties/sortie-verif-empreintes.txt`) ;
  - `diff` de `analyser_echelle_v3.py` à `analyser_echelle_v4.py` : le calcul est inchangé, sauf λ par profondeur, désormais dans les deux sens ; `lire()` est réécrite (`lire_sens`, `conditions`, `manquantes`). Stimuli, constructeur et rapport de construction identiques à l'octet à ceux de `echelle-v3/` (`cmp`).
- **Lu en entier** :
  - le brouillon v5 ; le brouillon v4 pour les différences ; cl3 et ses pièces (`banc_v4.py`, `banc.jsonl`, journaux, sorties) ; les constats et le traitement de cl2 et de cl1 ;
  - tout `echelle-v4/` : treize scripts, `.gitignore`, rapport de construction, quatre fichiers de tests ; les stimuli par Python seulement ;
  - les gardes héritées : `exiger_prereg_scelle` et ce qu'elle appelle (`problemes`, `sections`, `scellement.verifier`, `GardeArret`) ; `garde_calcul.py` en entier ;
  - les traces citées : accès, gabarits, contrôles lexicaux, offre de référence v2 et ses 45 offres (par Python), sortie des tests, répétition (résumé, empreintes, analyse du modèle minuscule, et six journaux sur quatorze : sain, délai atteint, création absente, création trop ancienne, compagnon faux, durée 4 499 ; tous les compagnons vérifiés), essai 1 de la répétition, atteignabilité v3 et v4, audit de la simulation (script et sortie) ;
  - les passages des cartes v1 à v3 que le texte cite ; la ligne R-530.
- **Non lus** : rien de ma liste. Hors liste, j'ai lu l'en-tête de `registres/go.md` et une quinzaine de ses lignes, dont celles des GO employés dans mon essai de la garde (CLW-03).
- **Interdits respectés** :
  - aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt (seulement des listes de dossiers nommés) ;
  - aucun réseau, aucune commande vastai (un faux outil, nommé `faux-outil`, dans mon bac à sable), aucun lancement, aucune écriture git ; rien de modifié hors de mon bac à sable ;
  - aucune clé ni aucun jeton cherché, affiché ou écrit ;
  - une transparence : mon premier lancement de la simulation créait ses dossiers temporaires sous `/tmp`, effacés par le script lui-même ; je l'ai arrêté au bout de deux minutes par son identifiant de tâche, et relancé avec `TMPDIR` dans le bac à sable. Tous les autres essais avaient `TMPDIR`, `--basetemp` et `HF_HOME` dans le bac à sable, `-B` et `PYTHONDONTWRITEBYTECODE=1`.
- **Essais** (scripts jetables et sorties dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5/`) :
  - tests du commit : **174 passed in 274.99s**, avec le modèle minuscule local (`sorties/tests-cl4.txt`) ;
  - simulation d'atteignabilité rejouée avec le script scellé, ses graines, trois processus et des fils de calcul à un (`reproduction-atteignabilite/`) ;
  - banc `scripts/banc_v5.py` : l'analyse v4 **telle quelle** (mode répétition, 300 tirages, d = 64), générateur de cl3 repris à l'identique ; 66 analyses, dont 26 rejeux de cl3 aux mêmes graines et 40 analyses de cas nouveaux (annexe) ;
  - cas limites de `lire()` sur des intervalles fabriqués (`scripts/cas_limites_lire.py`) ;
  - dépense réelle au pire balayée sur 30 358 offres admises, et choix d'offre rejoué sur la trace des 45 offres (`scripts/pire_domaine.py`) ;
  - gardes héritées éprouvées, cas sain et artefacts (`scripts/gardes_heritees.py`) ;
  - bords de l'amorce, chemins de la surveillance et du contrôle de prix non couverts par la suite de tests, avec un faux outil (`sorties/sortie-amorce-bords.txt`, `scripts/surveillance_bords.sh`).

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLW-01** : la combinaison des deux sens compare l'issue lue en premier dans chaque sens, et non les issues que chaque sens remplit. « Pas de fuite » et « fuite de signe inverse » se lisent avant « nul » et peuvent le masquer. Un « nul » rempli dans les deux sens devient alors « désaccord des deux sens », avec une phrase qui impute l'écart à la signature d'un jeu ou à la force du contexte. Banc, sous une fuite faible et égale aux deux tailles : 3 analyses sur 12 (fuite de 0,2, tau 0,15) et 5 sur 8 (fuite de 0,15, contexte du jeu b plus faible) ; 0 sur 8 dans deux autres réglages. Cela ne peut jamais arriver à « positif » ni à « inverse », qui excluent toute autre issue. C'est une asymétrie que R4 interdit, sur l'issue nulle principale de H_0.

Corrections à faire avant le scellement :

- CLW-01 (bloquant) ;
- CLW-02 à CLW-05 (à corriger) : réserves limitées à « positif » et « inverse », garde de calcul héritée qui accepte n'importe quel GO de calcul, commit lancé jamais relié au texte scellé, phrase « Prix de la symétrie » fausse.

CLW-01 et CLW-02 touchent `lire()` et l'analyse ; CLW-03 et CLW-04 touchent le lanceur et l'analyse ; CLW-05 touche le texte. Il faut donc, comme après cl2 et cl3 :

- des noms nouveaux (R12), un commit et des empreintes nouveaux ;
- les tests, la simulation et la répétition rejoués ;
- un texte nouveau, et une contre-lecture neuve des parties changées (R2).

Les remarques CLW-06 à CLW-10 sont à reprendre au passage.

## Ce qui tient

- **Empreintes et commit** : 34 sur 34 ; tête de branche = commit attendu ; arbre propre ; le nom scellé `prereg/test-echelle-conscience-eval-v5.md` est libre.
- **Tests** : 174 passent chez moi (274,99 s), comme la trace (279,13 s).
- **Simulation** : reproduite **à l'octet près** (`877a8e31…`), 25 cases et 100 analyses ; mêmes empreintes d'analyse, de simulation et de stimuli, même commit, mêmes versions, fils à un.
  - Le tableau du texte la transcrit fidèlement, case par case. 16 noms d'issue sur 20 sont atteints ; les quatre autres sont les miroirs annoncés.
  - La phrase R3 est exacte : 40 analyses sous H_0, sans fuite ou sous la signature d'un seul jeu, aucune « positif » ni « inverse ».
  - L'audit dit vrai sur ses propres chiffres : cosinus de −0,284 à +0,178 ; λ effectif de −0,352 pour la graine 3138 ; la règle v3 aurait prononcé « fuite de signe inverse » quatre fois et « nul » une fois là où la v4 n'en prononce aucune.
- **CLZ-01 levé, preuve rejouée** (annexe) :
  - les bancs de cl3, aux mêmes graines, donnent avec l'analyse v4 des intervalles identiques à ceux de cl3 (même calcul) ;
  - les lectures sur un seul sens ont disparu : « fuite de signe inverse » 4 sur 4 devient 0 (3 non confirmées, 1 désaccord) ; le « nul » de la graine 9306 devient « désaccord » ; le « pas de fuite » de la graine 9306 devient « non confirmé ».
- **Concordance du texte et du code** :
  - étape 1 : ordre de `lire_sens`, conditions P(s) et I(s), inégalités strictes ou larges, certification ≥ 0,70 dans chaque sens ;
  - étape 2 : les cinq règles de combinaison, sur tous les cas que j'ai fabriqués ;
  - réserves, `SEUILS`, `ATTENDUS`, choix de couche (aire arrondie, puis d', puis la plus basse), graines, rejets, mode décisif ;
  - une phrase par issue, les vingt noms couverts ;
  - commandes du lancement, de la surveillance et de l'analyse ;
  - liste d'arrêt conforme au code, ligne à ligne, aux manques de CLW-08 près.
- **Dépense** :
  - le pire calculé tient sous 8 USD par construction ; balayage de 30 358 offres admises : la dépense réelle au pire, au prix majoré de 5 % et avec 80 s de latence, vaut **7,88 USD au plus** ; 7,90 USD en comptant 4 Go de roues et d'image en plus de la descente ;
  - rejeu du choix sur les 45 offres de la trace : offre 50510069, 7 200 s ; pire 7,0174, estimé 5,3914 et attendu 3,7942 USD, comme la trace et le texte (7,02 ; 5,39 ; ≈ 3,8) ; seconde offre conforme à 8,00 USD tout juste.
- **Amorce** (essais au bord, dans le bac à sable) : 2 699 s restants → refus ; 2 700 s → départ, délai 2 700 s ; création dans le futur → délai plafonné à 3 900 s ; durée « abc », création à neuf chiffres et délai d'essai illisible → refus.
- **Contrôle du prix** : relecture de l'instance en échec → arrêt par identifiant, puis code 6 (état illisible). Aucun repli silencieux.
- **Garde de délestage** (CLZ-11) : le test de délestage réel sur le disque passe ; la garde relit l'appareil de chaque paramètre, avec ou sans carte des couches.
- **R7** : pages et chiffres de Xiong et al. conformes à la carte v3 (l. 15, 79, 81 à 84, 201), réserve de circularité comprise. Les autres citations concordent aussi : carte v1, l. 114, 205, 289, 358 et 359 ; carte v2, l. 16, 24, 57 et 161 ; carte v3, l. 14.
- **R9, R10, R12** :
  - `SeedSequence`, versions, commit et fils consignés par l'analyse et la simulation ; le manifeste de mesure consigne versions et empreinte du script, et le commit est dans le journal poussé ;
  - arrêts par identifiant partout ; `timeout` n'agit que sur son propre groupe de processus ; la répétition relit `/proc` sans rien tuer ;
  - noms neufs : scripts `…_v4`, `analyse-echelle-v4.json`, branche `donnees/echelle-conscience-eval-v4` (absence vérifiée par le lanceur).

## Traitement des constats de cl3

| constat de cl3 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLZ-01 lecture sur un seul sens | bloquant | **traité** | Rejeu des bancs de cl3 (même calcul, intervalles identiques) : plus aucune issue prononcée sur un seul sens (annexe). Simulation reproduite à l'octet. Restent : la combinaison des deux sens masque « nul » (CLW-01) ; la signature négative au 70B, que cl3 demandait, manque à la simulation et aux tests (CLW-09) ; la phrase « Prix de la symétrie » est fausse (CLW-05) |
| CLZ-02 phrase de « non confirmé » | à corriger | **traité** | Trois causes nommées, aucune imputée. Conditions manquantes chiffrées, certification comprise : testé, et vu dans mes bancs. La phrase de « désaccord » n'a pas reçu le même soin (CLW-01, CLW-06) |
| CLZ-03 tolérance du prix relu | à corriger | **traité** | Durée et pire au prix majoré, tous postes. Balayage du domaine admis : 7,88 USD au plus. Marge : environ 196 s de retard d'arrêt au prix maximal (CLW-08) |
| CLZ-04 gardes nouvelles non éprouvées | à corriger | **traité** | Contrôle du prix extrait et testé (égal, +4 %, +6 %, un seul prix, six réponses illisibles ; codes 4 et 6). Répétition : 19 lignes conformes (4 499, 7 201, création absente, création trop ancienne, compagnon faux, délai atteint, aucun processus restant). Bords de l'amorce éprouvés par moi |
| CLZ-05 hypothèses de l'amorce et du devis | remarque | **traité** | Délai compté depuis la création, refus sous 2 700 s ; session sous 24 h dite ; remontée comptée ; débit d'au moins 2 000 Mb/s ; risque du « 8B seul » dit |
| CLZ-06 chiffres et renvois | remarque | **traité**, un reste | Comptes repris de la simulation v4 (40 analyses : exact) ; devis sur une trace qui porte ses nombres ; rapport de construction au tableau. Le « 0,98 » renvoie à R-530, une ligne de registre sans empreinte (CLW-10) |
| CLZ-07 Xiong et al. | remarque | **traité** | Réserve de circularité écrite ; pages conformes à la carte v3 |
| CLZ-08 portée du contrôle symétrique | remarque | **traité**, à étendre | Limite dite, cas ajouté à la simulation. Mais la même double signature fabrique aussi « inverse » et « fuite de signe inverse », celle-ci sans réserve possible (CLW-02) |
| CLZ-09 A_conf à 1,00 | remarque | **traité** | Exemple de R4 restreint à λ ≥ 0,5. Le miroir manque (CLW-10) |
| CLZ-10 phrases, commande, petits écarts | remarque | **traité** | Une phrase par issue ; commit écrit dans la commande et dans le mode décisif ; « ≈ 2 sur 7 776 » |
| CLZ-11 petits manques | remarque | **traité** | Test à quatre couches (avec et sans signe contraire) ; refus en miroir pour « inverse » ; surveillance (plafond, création, identifiant, code de fin) ; délestage relu paramètre par paramètre. Deux chemins de la surveillance restent sans test, éprouvés par moi : conformes (CLW-09) |

Bilan : 11 constats traités, dont 2 avec un reste mineur (CLZ-06, CLZ-08) ; aucun non traité.

## Constats nouveaux

### CLW-01 — BLOQUANT — La combinaison des deux sens masque « nul » : une équivalence remplie dans les deux sens est lue « désaccord des deux sens »

- **Localisation** :
  - `analyser_echelle_v4.py` : `ISSUES` (l. 406), `lire_sens` (l. 440–453, première issue dont toutes les conditions tiennent), `lire` (l. 474–496, comparaison des deux étiquettes) ;
  - brouillon v5 : étape 1 (l. 209–218), étape 2 (l. 220–226), phrase de « désaccord » (l. 242).
- **Constat** :
  - Chaque sens ne rend que la **première** issue de l'ordre de lecture dont les conditions tiennent. Or les issues ne s'excluent pas toutes :
    - « positif » et « inverse » excluent toute autre issue (bornes incompatibles) ;
    - « fuite de signe inverse » se lit la première ;
    - « pas de fuite » exclut « fuite de signe inverse », et se lit avant « nul » ;
    - **« nul » peut tenir en même temps que « pas de fuite » ou que « fuite de signe inverse »**.
  - Quand un sens lit « pas de fuite » (« nul » y tenant aussi) et l'autre « nul », la combinaison voit deux étiquettes différentes et prononce « désaccord des deux sens ». Le détail rapporte pourtant, pour « nul », **aucune condition manquante** dans l'autre sens.
  - La phrase permise est alors fausse : « Les deux sens lisent deux issues différentes […] L'écart peut tenir à la signature des cadrages d'un jeu ou à une différence de force du contexte […] ; aucune issue n'est établie », alors que les deux sens établissent l'équivalence.
  - Seule l'issue « nul » peut être perdue ainsi. Un « positif » ou un « inverse » rempli dans les deux sens est toujours prononcé. Un résultat nul se prononce donc plus difficilement qu'un positif, sous la même vérité : c'est l'asymétrie que R4 interdit, et que CLZ-01 visait.
  - Le cas n'est pas rare. λ_s est relatif à l'effet du contexte sur le jeu mesuré : λ_a→b ≈ α/κ_b et λ_b→a ≈ α/κ_a (CLZ-02). Une fuite faible et égale aux deux tailles, avec des jeux de force inégale, place un sens dans la bande de « pas de fuite » et l'autre juste au-dehors. C'est une configuration plausible de H_0 : l'auteur attend λ(70B) ≈ 0 à 0,3, et les indices contraires disent que le 70B suit aussi le format.
- **Preuve** :
  - Cas fabriqué (`scripts/cas_limites_lire.py`, `sorties/sortie-cas-limites-lire.txt`). Sens a→b : λ(petit) [0,05 ; 0,22], λ(grand) [0,00 ; 0,20], Δλ [−0,10 ; 0,15], donc « pas de fuite » et « nul ». Sens b→a : λ [0,10 ; 0,32] et [0,08 ; 0,30], Δλ [−0,12 ; 0,14], donc « nul » seul. Lecture : « désaccord des deux sens » ; conditions manquantes de « nul » dans le sens a→b : `[]`. Même chose avec « fuite de signe inverse » + « nul » d'un côté et « nul » de l'autre.
  - Banc, analyse v4 telle quelle (annexe) :
    - fuite de 0,2 aux deux tailles, tau 0,15 : « nul » 9, **« désaccord » 3 sur 12**, et dans les trois « nul » tient dans les deux sens (graines 9604, 9610, 9612) ;
    - fuite de 0,15 aux deux tailles, contexte du jeu b à 0,6, tau 0,15 : **« désaccord » 5 sur 8**, « nul » 3. Dans les cinq, « nul » tient dans les deux sens ; par exemple, graine 10204 : Δλ_a→b [−0,185 ; 0,142], Δλ_b→a [−0,142 ; 0,057], λ_b→a(petit) [0,038 ; 0,179].
  - Ni les 40 cas de `test_lire`, ni leurs miroirs, ni la simulation ne contiennent deux issues compatibles : la simulation ne présente jamais la paire « pas de fuite / nul ».
- **Correction** :
  - Lire chaque sens comme l'**ensemble** des issues dont toutes les conditions tiennent ; prononcer la première issue, dans l'ordre de lecture, qui tient **dans les deux sens** ; rapporter les autres comme « non confirmées », avec leurs conditions manquantes.
  - Trancher par écrit le cas « fuite de signe inverse dans un sens, "nul" dans les deux ». Par exemple : « nul », avec « fuite de signe inverse non confirmé (sens …) » ; ou un « désaccord » motivé, puisque la règle dit que la comparaison d'échelle n'est pas lue sous une fuite de signe inverse.
  - Réécrire l'étape 2 et la phrase de « désaccord ».
  - Tests : ajouter les cas à issues compatibles et leurs miroirs.
  - Simulation : ajouter une fuite faible et égale aux deux tailles, avec des forces de contexte inégales entre les deux jeux.

### CLW-02 — À CORRIGER — R4 : les réserves ne protègent que « positif » et « inverse » ; la double signature fabrique une « fuite de signe inverse » sans réserve possible

- **Localisation** : `lire` (l. 479–481 : `reserves()` n'est appelée que pour « positif » et « inverse ») ; `reserves` (l. 463–471) ; brouillon v5, réserves (l. 234–238), limites (l. 264), R3 (l. 176), R4 (l. 268).
- **Constat** :
  - (a) **Spécificité.** CLZ-08 a montré qu'une poussée du format alignée sur les signatures des deux jeux passe les deux sens. Le texte le dit, avec l'exemple de « positif » et de sa réserve « fuite non spécifique ». La même poussée de signe négatif au 8B fabrique « fuite de signe inverse » dans les deux sens. Or cette issue n'a **aucune** réserve. Au 70B, de signe positif, elle fabrique « inverse », dont la réserve ne se déclenche qu'une fois sur deux.
  - (b) **Profondeur.** La réserve « profondeur » répond au choix de L\* à saturation (CLY-08), qui peut placer les deux modèles à des profondeurs différentes. Ce risque vaut aussi pour « nul » et « pas de fuite ». Un « nul » lu à L\*, que trois profondeurs appariées sur quatre contredisent, ne reçoit pourtant aucune réserve ; un « positif » dans la même situation en reçoit une.
  - La phrase R3 (l. 176) ne parle que de « positif » et d'« inverse », et la limite (l. 264) n'illustre que « positif ».
- **Preuve** (banc, annexe) :
  - double signature de −2 au 8B, aucun concept (`sig_ab_neg`) : **« fuite de signe inverse » 4 sur 4**, dans les deux sens, bornes hautes de λ(petit) entre −0,47 et −1,37 ;
  - la même de +2 au 8B (`sig_ab_pos`, graines de cl3) : « positif » 4 sur 4, dont 3 avec réserve ;
  - de +2 au 70B (`sig_ab_grand`) : « inverse » 4 sur 4, dont **2 sans réserve**.
- **Correction** :
  - une réserve « fuite non spécifique » en miroir pour « fuite de signe inverse » : par exemple, pour le modèle dont λ_s est sous −δ, si la borne basse de (−λ_s − ν_s) est ≤ 0 dans un sens au moins ; les tirages le permettent déjà ;
  - une réserve « profondeur » pour « nul » (trois Δλ appariés sur quatre hors de [−δ ; δ] dans un sens) et pour « pas de fuite » (trois λ appariés sur quatre hors de la bande, pour un modèle) ; ou bien écrire pourquoi ces issues n'en ont pas besoin ;
  - étendre la limite et la phrase R3 à toutes les issues : la double signature fabrique aussi « inverse » et « fuite de signe inverse », et peut masquer un écart vrai ;
  - tester chaque réserve nouvelle sur un cas sain et sur un artefact.

### CLW-03 — À CORRIGER — Garde de calcul héritée : tout GO « calcul » en cours passe, quels que soient son périmètre et son plafond

- **Localisation** : `garde_calcul.py`, `decider` (l. 87–112 : type, « accordé par », dates et révocation seulement ; le plafond et le périmètre ne sont jamais lus) ; `lancer_echelle_v4.sh`, l. 34 (`PLAFOND_GO=8.00` écrit en dur) et l. 71 ; brouillon v5, l. 35 (« un GO nouveau, sur devis […] Rien ne part avant ce GO ») et l. 192.
- **Constat** : le lanceur passe le GO à la garde, qui accepte n'importe quel GO de type « calcul » accordé par Lazar et en cours de validité. Rien ne vérifie que le GO cité est celui de cette expérience, qu'il est nouveau, ni que son plafond couvre les 8 USD. Une erreur d'identifiant ferait partir la dépense sous un GO étranger, éventuellement plus petit.
- **Preuve** (`scripts/gardes_heritees.py`, `sorties/sortie-gardes-heritees.txt`, registre `a157cd2f…`), même entrée JSON que le lanceur :
  - `GO-2026-10-26-08` (pré-autorisation conditionnelle d'une autre expérience, **plafond 2 USD**, échéance le 31 octobre) : **passe** (code 0) ;
  - `GO-2026-10-04-08` (devis général de la phase 0, 150 USD) : passe ;
  - GO inconnu, GO de type « dépôt distant », commande sans GO : refusés (code 2). La garde fait donc bien ce qu'elle dit ; elle ne dit pas assez.
- **Correction** : dans le lanceur, lire la ligne du GO dans `registres/go.md` et arrêter avant toute création si :
  - le périmètre ne cite pas `test-echelle-conscience-eval-v5` ou son empreinte ;
  - le plafond du GO est inférieur à `PLAFOND_GO` (ou bien le lanceur prend le plus petit des deux comme plafond) ;
  - le GO est antérieur au scellement.
  - Tester un cas sain et deux artefacts (GO d'une autre expérience, plafond plus petit).
  - À défaut, écrire dans « Dépense » que ce point repose sur l'opérateur seul.

### CLW-04 — À CORRIGER — Rien ne relie le commit lancé au texte scellé, et l'analyse ne vérifie pas le script de mesure

- **Localisation** : `lancer_echelle_v4.sh`, l. 46–51 (`exiger_prereg_scelle`, puis la tête de branche comparée à l'argument COMMIT, sans plus) ; `analyser_echelle_v4.py`, `charger_modele` (l. 130–163 : modèle, révision, couches, dimension, type, stimuli, limite, identifiants ; pas `sha256_script`, que la mesure écrit, `mesurer_echelle_v4.py` l. 184).
- **Constat** :
  - `exiger_prereg_scelle` garantit un texte scellé, conforme et intact, mais ne lit pas son contenu.
  - Le lanceur accepte tout commit égal à la tête de la branche d'outils. Si cette tête avance après le scellement (un correctif, par exemple) et que la session lance avec la tête nouvelle, l'instance mesure avec un script que le texte n'a pas scellé.
  - L'analyse ne le voit pas : elle vérifie son propre commit, pas celui de la mesure.
- **Preuve** : une copie scellée du brouillon, dont le commit est remplacé partout par `000…0`, passe `exiger_prereg_scelle` (`sorties/sortie-gardes-heritees.txt`) ; aucune ligne du lanceur ne compare COMMIT au texte (vérifié par lecture et par recherche dans le script).
- **Correction** :
  - lanceur : arrêter si le texte scellé ne contient pas COMMIT (`grep -qF "$COMMIT" "$DEPOT/$PREREG"`, ou mieux une ligne « commit » lue) ;
  - analyse : exiger dans chaque manifeste `sha256_script` = `1cfb85b1…` (mesure v4) en mode décisif ;
  - tester un cas sain et un artefact.

### CLW-05 — À CORRIGER — « Prix de la symétrie » : aucun « positif » n'est perdu

- **Localisation** : brouillon v5, l. 182.
- **Constat** : le texte écrit que « sous H_A faible au tau 0,4, deux "positif" sur quatre deviennent "positif non confirmé" » et que « la puissance baisse ».
  - Or « positif » et « inverse » se lisent exactement comme en v3, qui exigeait déjà P dans les deux sens et la certification b→a. P et I excluant toute autre issue, la v4 prononce « positif » si et seulement si la v3 le prononçait.
  - Le prix de la symétrie ne porte que sur « fuite de signe inverse », « pas de fuite » et « nul ». La phrase fausse la puissance annoncée.
- **Preuve** : simulation scellée v4, case « H1 faible ; tau 0,4 » : par sens « positif / positif » 2 et « indécis / positif » 2. Simulation scellée v3, mêmes graines : « positif 2, indécis 2 ». L'audit v4 lui-même (section 2) écrit : « règle v3 "indécis" → v4 "positif non confirmé (sens a→b)" (4) ».
- **Correction** : « "Positif" et "inverse" se lisent comme en v3. Sous H_A faible, deux "indécis" deviennent "positif non confirmé (a→b)". Le prix porte sur les issues nulles : sans fuite au tau 0,8, un "pas de fuite" sur quatre devient "non confirmé" ; et voir CLW-01. »

### CLW-06 — REMARQUE — Phrase de « désaccord des deux sens »

- La phrase (l. 242) ne nomme que la signature d'un jeu et la force du contexte. Deux issues différentes peuvent aussi naître de la variabilité près des seuils : par exemple, un Δλ vrai proche de δ, lu « nul » d'un côté et « positif » de l'autre.
- CLZ-02 a ajouté le manque de puissance pour « non confirmé » seulement. L'ajouter ici, et corriger la phrase selon CLW-01.

### CLW-07 — REMARQUE — Grandeurs rapportées et choix de couche dans un seul sens

- Ne sont calculés que dans le sens a→b : ΔA_ctx_fixe et ΔA_conf (`delta_…_ab`, l. 595–597), la marge sur le sac de mots (l. 588), le sac de mots lui-même (appris sur a, appliqué à b, l. 359–377).
  - Or « certification asymétrique » se lit dans les deux sens, et sa phrase annonce « ΔA_ctx_fixe est rapporté ».
  - Il manque aussi le contrôle lexical b→a, appris sur b et appliqué à a.
- L\* est choisie sur l'aire A_ctx du seul sens a→b (l. 324–332, l. 127 du texte). La certification b→a, désormais exigée pour toutes les issues, n'y entre pas. Cela rend « X non confirmé (sens b→a) » par certification manquante plus probable que son miroir. C'est une perte de puissance, pas un biais de signe.
- Correction : calculer ces grandeurs dans les deux sens ; choisir L\* sur le minimum des deux aires, ou dire pourquoi non.

### CLW-08 — REMARQUE — Liste d'arrêt et codes de sortie

- **Création douteuse.** Le lanceur rend 4 aussi quand la création est douteuse : réponse illisible, statut non nul ou identifiant illisible (l. 157 et 160). L'instance n'est alors ni arrêtée, ni contrôlée en prix, ni surveillée.
  - Le texte ne donne au code 4 qu'un sens, « arrêt relu » (l. 281), et ce cas manque à la liste d'arrêt.
  - Donner un code distinct, et écrire la conduite : retrouver l'instance (champs filtrés), l'arrêter par son identifiant, et ne lire aucun résultat poussé sans décision de Lazar.
- **GO refusé par la garde** : arrêt prévu par le code, absent de la liste du texte.
- **Refus précoces de l'amorce.** Durée, création, moins de 2 700 s, clonage, tête différente ou dossiers présents : l'amorce sort par 1 sans ligne « fin, code » (`amorce_echelle_v4.sh` l. 27–57). La surveillance voit alors le conteneur sorti et rend 5, non 7, et ne consigne aucun code ; seul le message reste, dans le journal (essayé : `sorties/sortie-surveillance-bords.txt`). Le texte dit « code de fin de l'amorce relu et consigné » (l. 199, l. 299) : préciser.
- **Appels sans délai propre.** La surveillance appelle `show` et `logs` sans délai propre (l. 35 et 50). Un appel bloqué retarde la relève du plafond ; la borne de l'amorce couvre ce cas sous l'hypothèse dite (instance sortie = stockage seul). Un `timeout 30` sur chaque appel suffit.
  - La marge de 0,20 USD couvre environ 196 s de retard d'arrêt au prix maximal (balayage : 8,00 USD à 196 s), et non 80 s seulement.

### CLW-09 — REMARQUE — R5 : manques de tests

- Surveillance : « création différente de celle du lanceur » et « conteneur sorti sans ligne de fin » (code 5) n'ont pas de test. Je les ai éprouvés avec un faux outil : code 2 sans arrêt, puis code 5 avec arrêt par identifiant. Ajouter les deux tests.
- Gardes héritées : aucun test dans la suite `echelle-v4`. Éprouvées par moi : `exiger_prereg_scelle` passe le cas sain et arrête trois artefacts (« À REMPLIR », compagnon absent, texte modifié après scellement) ; la garde de calcul arrête trois artefacts. Elles tiennent dans leur périmètre ; ce périmètre est trop étroit (CLW-03, CLW-04).
- CLZ-01 demandait une signature **négative au 70B** : elle manque à la simulation et aux tests. La règle est symétrique par construction, mais un test fermerait la question.

### CLW-10 — REMARQUE — R6 et détails

- Écart 6 : « 0,98 » renvoie à R-530, une ligne de registre vivant sans empreinte. Mieux : un extrait empreinté, ou une mention « non tracé ».
- « Environ huit fois plus petit » (l. 180) : le rapport des racines vaut 8 pour 4 096 dimensions et environ 11 pour 8 192, et seulement pour des directions aléatoires isotropes, ce que le texte exclut lui-même. Écrire « pour des directions aléatoires ».
- « ≈ 141 Go » (l. 49) sans trace. « ≈ 0,3 Go » se recalcule : 3 072 × 4 × (4 096 + 8 192) × 2 octets ≈ 0,30 Go.
- La trace des tests ne contient pas le commit ; seul son nom le porte. La version 1.8.3 de vastai n'est vérifiée par aucun script.
- R4 (l. 268) : l'exemple « A_conf à 1,00 avec λ ≥ 0,5 » n'a pas de miroir. Une inversion trop nette, « A_conf à 0,00 avec λ < 1 », est aussi « trop propre ».

## Annexe — banc cl4 (analyse v4 telle quelle, 300 tirages, d = 64)

Générateur de cl3 repris à l'identique (`docs/notes/echelle-conscience-eval/v4/contre-lecture-cl3/scripts/banc_v4.py`) : x = contenu + s_f·F + s_c·κ·C + cadrage + bruit, avec F = α·C + F⊥ + signature_a·sig_a + signature_b·sig_b ; |C| = 4 ; les signatures sont normées à |C| et multipliées par le facteur indiqué ; « contexte b × k » multiplie l'effet du contexte sur les stimuli du jeu b.

| cas (graines) | vérité (8B ; 70B) | lectures v4 | remarque |
|---|---|---|---|
| sig_a_neg (9100 à 9106) | signature a de −2 au 8B, aucun concept, tau 0,4 | désaccord 1 ; fuite de signe inverse non confirmé (b→a) 3 | v3 (cl3) : fuite de signe inverse 4. Intervalles identiques à cl3 |
| masque_HA_fort_t015 (9300 à 9306) | (1,0 ; 0,2), signature a de −2 au 8B, tau 0,15 | positif 3 ; désaccord 1 | v3 : positif 3, nul 1 |
| masque_pasdefuite_t015 (9300 à 9306) | (0,6 ; 0), signature a de −1,4 au 8B, tau 0,15 | positif 3 ; pas de fuite non confirmé (b→a) 1 | v3 : positif 3, pas de fuite 1 |
| masque_HA_fort (9200 à 9206) | (1,0 ; 0,2), signature a de −2 au 8B, tau 0,4 | positif non confirmé (a→b) 4 | v3 : indécis 4 |
| sig_ab_pos (9200 à 9206) | signatures a et b de +2 au 8B, aucun concept | positif 4, dont 3 avec réserve | comme cl3 (CLZ-08) |
| sig_b_pos (9400 à 9404) | signature b de +2 au 8B, aucun concept | positif non confirmé (a→b) 3 | v3 : indécis 3 |
| HA_kappa (9400 à 9404) | (1,0 ; 0,1), forces de paires inégales (0,5) | positif 1 ; positif non confirmé (b→a) 1 ; positif non confirmé (a→b) 1 | v3 : la troisième lue « certification asymétrique (petit) » |
| faible_egal_t015 (9600 à 9622) | (0,2 ; 0,2), tau 0,15 | nul 9 ; **désaccord 3** | « nul » tient dans les deux sens dans les trois (CLW-01) |
| faible_egal_forceb_t015 (9700 à 9706) | (0,2 ; 0,2), contexte b × 0,75, tau 0,15 | nul 4 | — |
| faible_egal_t04 (9800 à 9806) | (0,2 ; 0,2), tau 0,4 | nul 4 | — |
| faible_forceb06_t015 (10200 à 10214) | (0,15 ; 0,15), contexte b × 0,6, tau 0,15 | **désaccord 5** ; nul 3 | « nul » tient dans les deux sens dans les cinq (CLW-01) |
| sig_ab_neg (9900 à 9906) | signatures a et b de −2 au 8B, aucun concept | **fuite de signe inverse 4**, sans réserve possible | CLW-02 |
| sig_ab_grand (10000 à 10006) | signatures a et b de +2 au 70B, aucun concept | **inverse 4**, dont 2 sans réserve | CLW-02 |
| masque_double_t015 (10100 à 10106) | (1,0 ; 0,2), signatures a et b de −2 au 8B, tau 0,15 | positif 3, dont 1 avec réserve ; nul non confirmé (a→b) 1 | à tau 0,15, la signature pèse peu dans ĉ |
| reproduction de la simulation v4 | 100 analyses, mêmes graines | identique à l'octet (`877a8e31…`) | 25 cases sur 25 |

Pièces, dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v5/` :

- `scripts/` : `verif_empreintes.py`, `cas_limites_lire.py`, `banc_v5.py`, `lancer_banc.sh`, `resumer_banc.py`, `comparer_cl3.py`, `pire_domaine.py`, `gardes_heritees.py`, `surveillance_bords.sh` ;
- `banc/` : `banc-lot1.jsonl`, `banc-lot2a.jsonl`, `banc-lot2b.jsonl`, `banc-lot3a.jsonl`, `banc-lot3b.jsonl`, journaux par scénario ;
- `reproduction-atteignabilite/` : `sortie/atteignabilite-echelle-v4.json` et son compagnon, `journal.txt`, `comparaison.txt` ;
- `sorties/` : `tests-cl4.txt`, `sortie-verif-empreintes.txt`, `sortie-cas-limites-lire.txt`, `sortie-pire-domaine.txt`, `sortie-gardes-heritees.txt`, `sortie-amorce-bords.txt`, `sortie-surveillance-bords.txt`, `sortie-surveillance-prix-bords.txt`, `sortie-comparer-cl3-lot1.txt`, `sortie-comparer-cl3-lot2.txt`, `sortie-banc-resume-lots-1-2.txt`, `sortie-banc-resume-lot3.txt` ;
- `gardes/` (copies scellées du brouillon pour l'essai de `exiger_prereg_scelle`), `amorce/`, `faux/` (faux outil et essais), `offres/` (rejeu du choix).
