# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v8) — cl7

- **Rôle** : sous-agent neuf, septième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v8, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 à 6.
- **Consigne** : `docs/notes/echelle-conscience-eval/v7/consigne-contre-lecture-cl7.md` (`dcc528795947e139eb5ac19d3b9eb628f135eaa49cd20120571edd84b0990743`), conforme à son compagnon ; suivie à la lettre.
- **Heure** (`date -u`) : 27 octobre 2026 ; lecture commencée à 09:09:07 UTC ; rapport achevé à 09:59 UTC.

## Empreintes des pièces lues (sha256)

| pièce | sha256 |
|---|---|
| `prereg/brouillon-test-echelle-conscience-eval-v8.md` (texte relu ; conforme à son compagnon au début et à la fin de ma lecture) | `a6dcd579d9ff2d16e51412347ba8b6fe291c668f520577f38eed2f0460636717` |
| `prereg/brouillon-test-echelle-conscience-eval-v7.md` | `e6e8a864ea2b7865bbc658b5f9ed84e34b1bd62cb8223e90d23eb1177ccf2ee4` |
| `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v7-cl6.md` | `3d7a60fcb8c7cebe083c0e27b060554203b6817f78250553d217df9efe00e583` |
| `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v6-cl5.md` | `4ea69784a824c2b05048fd9e794e8e9aede3b6b6739da62a515250cbc01fcb15` |
| `…-v5-cl4.md`, `…-v4-cl3.md`, `…-v3-cl2.md`, `test-…-v2-cl1.md` | `5728de4c…`, `a2f330f0…`, `9b476cf4…`, `70afa519…` (conformes à leurs compagnons et au tableau « Traces ») |
| les 20 outils du tableau du texte (`echelle-v7/…`) | les 20 empreintes concordent avec le fichier, le compagnon et l'objet du commit `b54da1f…` |
| les 36 traces du tableau « Traces » du texte | toutes conformes au fichier et à leur compagnon |
| les 26 empreintes abrégées du corps du texte | toutes conformes : 22 vérifiées directement, 4 citées par leur seul nom de fichier et vérifiées par leur chemin complet au tableau « Traces » (`sorties/sortie-verif-empreintes-v8.txt` : 78 sur 78) |
| `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (inchangé depuis cl4) |
| `src/controle_ia/scellement.py` | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` (inchangé) |
| `.claude/hooks/garde_calcul.py` | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` (inchangé) |
| `registres/go.md` (registre vivant, lu vers 09:21 UTC ; modifié à 08:26 UTC, avant ma lecture, par des lignes d'autres projets ; aucune ne cite `test-echelle-conscience-eval-v8`) | `68e3b4c38a52d861ab8faf1e30ef42cd67d1243d9b1e3d9b99da73ae8365211a` |
| `docs/notes/echelle-conscience-eval/v7/contre-lecture-cl6/scripts/banc_cl6.py` (générateur repris) | `a7a58a7f22e3a912020bc91b3294f3206c7e38cf512bcc32b469b2f112858622` |
| `…/contre-lecture-cl6/scripts/cas_limites_lire_v6.py` | `790c11d6e14717ead0d71e1a6376b1b0f9aeaf77f20fe70e0a556ee7b44a4b21` |
| `…/contre-lecture-cl6/faux-depot-go/LISEZ-MOI.txt` | `08bdd9319b168d8a841b8037741d0d6b1adef57c7a073d162bdd80f325094a5c` |
| `…/v7/exploration-coherence/explorer_regles.py` | `1ab624c0956d71b7d4553ed94b1d6545a34d0709041c769b301f404c1a83ec56` |
| `…/v7/simulation-tableau/tableau_atteignabilite_v7.py`, `comptes_atteignabilite_v7.py` | `7d22f343…`, `c50a123f…` |
| cartes `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `-v2.md`, `-v3.md` | `134040bd…`, `fe1e93c1…`, `9d03d3b2…` (conformes à leurs compagnons) |

## Ce qui a été lu et essayé

- **Code** : arbre de travail `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/`, branche `outils/echelle-conscience-eval-v7`, tête `b54da1fe41e26360cb5410bfd2fdc0614537de1d` (le commit attendu), parent `b8b7665` (la v6 relue par cl6) ; arbre propre avant et après mes essais (seuls les `__pycache__` ignorés de `echelle-v7/`, datés de 07:59 à 08:05 UTC, antérieurs à ma lecture) ; index de l'arbre de travail inchangé (07:59:12 UTC) ; tous mes appels git en lecture, avec `GIT_OPTIONAL_LOCKS=0`.
  - Lu en entier : `analyser_echelle_v7.py`, `surveiller_echelle_v7.sh`, `amorce_echelle_v7.sh`, `lancer_echelle_v7.sh`, `test_analyser_echelle_v7.py` (cas de lecture et intégration), les parties nouvelles de `test_offre_et_surveillance_v7.py`, `choisir_offre_v7.py` (calcul) ; différences v6 → v7 de chaque script et de chaque test (`diffs/`) : la mesure, le script d'instance, le contrôle du prix, le contrôle du GO, le contrôle lexical, le choix d'offre et le lanceur ne changent que de noms, de chemins et de commentaires ; stimuli, constructeur et rapport de construction identiques à l'octet à ceux de `echelle-v6/` ; l'analyse ne change que par `coherence`, `lire` et le calcul de `ecart_sens` ; la surveillance par le contrôle des réglages ; l'amorce par la borne du clonage ; la répétition par le cas « clonage bloqué » ; la simulation par ses cas nouveaux.
  - Les stimuli n'ont été lus que par Python.
- **Texte** : brouillons v8 et v7 en entier, et leur différence mot à mot (`diffs/diff-v7-v8-mots.txt`) ; cl6 en entier et ses pièces (bancs, scripts, `faux-depot-go/LISEZ-MOI.txt`) ; constats et traitement de cl5 ; constats de cl1 à cl4 (en détail CLZ-02, CLZ-08, CLV-01, CLV-04) ; les traces nouvelles de `v7/` (exploration de la cohérence, simulation, tableau et comptes, audit, rejeu des bancs, latence, répétition, lexique, offre de référence, tests) ; les passages des cartes v1 à v3 cités (contrôle par sondage des chiffres et des pages : inchangés depuis la v7, déjà vérifiés par cl6).
- **Gardes héritées** : `exiger_prereg_scelle` et ce qu'elle appelle (`verifier`, `problemes`, `sections`) ; `garde_calcul.py` (empreinte inchangée) ; en-tête de `registres/go.md` et lignes « calcul ». `problemes()` sur le brouillon v8 : un seul manque, « section vide ou à remplir : Contre-lecture », comme attendu. `prereg/test-echelle-conscience-eval-v8.md` est absent (nom libre).
- **Essais** (scripts jetables et sorties dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v8/`, avec `TMPDIR`, `HF_HOME` et `--basetemp` dedans, `-B`, `PYTHONDONTWRITEBYTECODE=1`, fils de calcul à un) :
  - tests du commit avec le modèle minuscule local : **344 passed in 440.68 s** (`sorties/tests-cl7.txt`, de 09:11:36 à 09:18:58 UTC) ; décompte collecté : 243, 5, 8 et 88 par fichier ; `test_lire` 85, `test_lire_miroir` 85, `test_texte_des_reserves` 12, `test_go` 11, artefacts d'offre 11, réglages hors bornes 10 : ceux du tableau R5 ;
  - contrôle de toutes les empreintes citées (`scripts/verif_empreintes_v8.py`) ;
  - contrôle indépendant du rejeu versé des bancs de cl5 et cl6 (`scripts/verifier_rejeu.py`) et de la simulation (tableau, comptes, R3, issues atteintes, prix ; `scripts/verifier_tableau.py`) ;
  - cas fabriqués de cl5 et cl6 rejoués contre `lire()` v7, et cas fabriqués nouveaux (`scripts/cas_limites_lire_v7.py`) ;
  - banc nouveau, analyse v7 du commit telle quelle (mode répétition, 300 tirages), générateur de cl6 recopié à l'identique (`scripts/banc_cl7.py`, contrôle : la graine 22200 de cl6 redonne e(m) = 0,384 et 0,411, comme le rejeu versé) : 162 analyses (`banc/` : 4 de calibrage, 158 du banc principal), plus 4 confirmations à 2 000 tirages ;
  - essai de latence versé rejoué sur la surveillance du commit, avec deux cas de plus (`scripts/latence_cl7.py`) ;
  - forme exacte de la ligne de GO du texte v8 jouée contre `verifier_go_v7.py` sur un faux registre (`faux-go/`) ;
  - choix d'offre rejoué sur les 45 offres versées, et balayage de la dépense réelle au pire en fonction du retard d'arrêt (`offres/`) ;
  - simulation scellée reproduite au commit, avec le script du commit, trois processus et des fils à un, de 09:31:40 à 09:57:39 UTC (`simulation/`) : sortie **identique à l'octet** à la sortie versée (`84fd1638…`).
- **Interdits respectés** : aucun fichier interdit ouvert, lu ou haché ; aucune recherche récursive dans le dépôt (listes de dossiers nommés seulement) ; aucun réseau ; aucune commande vastai réelle (faux outils dans mon bac à sable) ; aucun lancement ; aucune écriture git ; rien de modifié hors de mon bac à sable (vérifié en fin de lecture : brouillon v8 conforme à son compagnon ; arbre de travail propre, index inchangé ; aucun fichier de `prereg/` ni de `docs/notes/echelle-conscience-eval/v7/` plus récent que 09:08:10 UTC, avant mon départ) ; `registres/etat.md`, `decisions.md` et `passations/` ont changé à 09:08–09:09 UTC, au départ de ma lecture : ce n'est pas moi ; aucune clé ni aucun jeton cherché, affiché ou écrit.

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLT-01** : la cohérence des deux sens ferme la classe de cl6 **en son centre seulement** (fuite exactement égale aux deux tailles, deux jeux de cadrages de même force de contexte). Elle tolère, par modèle et par sens, un écart de λ jusqu'à δ, la largeur même de la décision. Ses voisins, que le texte range lui-même dans H_0, la rouvrent :
  - un écart vrai d'échelle **sous δ** (0,15 à 0,2), plus des signatures d'un seul jeu croisées, de signes opposés, chacune sous δ : **« positif » 8 fois et « inverse » 2 fois sur 46 analyses, sans réserve**, cohérence tenue (|e(m)| de 0,13 à 0,24) ; le témoin sans signature lit « indécis » 4 fois sur 4 ;
  - une fuite **égale** (la classe de cl6 elle-même) avec un contexte d'un jeu **plus fort de 33 %** : **« inverse » 4 fois sur 6, sans réserve**, dont une fois avec |e(m)| sous 0,09 chez les deux modèles ;
  - et, en miroir sous H_A (écart vrai 0,3 à 0,35), des signatures croisées qui compensent l'écart : **« nul » 4 fois sur 12, sans réserve** ; témoin sans signature : « indécis » 4 fois sur 4.
  - Confirmé à 2 000 tirages, la taille du bootstrap décisif : les quatre artefacts essayés (un « positif » et un « inverse » de la première famille, un « nul » sous H_A, un « inverse » sous fuite égale) gardent leur lecture, sans réserve.
  - Le texte présente la classe comme écartée, au bruit près (« Seuil », l. 179 ; limites, l. 371–372 ; R3, l. 249), par un argument qui ne vaut que pour une fuite égale et des jeux de même force : « l'écart e(m) d'un modèle vaut, au bruit près, le Δλ du sens que sa signature déplace ». En général, e(m) vaut ce Δλ **moins l'écart vrai**, plus l'effet d'une différence de force du contexte.

Corrections à faire avant le scellement :

- CLT-01 (bloquant) : au minimum, écrire la classe dans les limites, la phrase R3 et la justification du « Seuil », et l'ajouter à la simulation ; mieux, une garde mécanique ou une réserve obligatoire, simulée avant d'être choisie (pistes chiffrées plus bas). Dans tous les cas : un texte nouveau et une contre-lecture neuve des parties changées (R2) ; si `lire()` change : noms, commit, tests et simulation nouveaux (R12).
- CLT-02 (à corriger) : le prix de la cohérence sous H_0 (« nul » perdu) n'est chiffré qu'au seul réglage où il ne coûte rien.
- Les remarques CLT-03 à CLT-05 sont à reprendre au passage.

## Ce qui tient

- **Empreintes et commit** : 78 empreintes sur 78 concordent (20 outils avec le fichier, le compagnon et l'objet du commit ; 36 traces avec le fichier et le compagnon ; 22 abrégées, les 4 autres citées par leur seul nom et couvertes par les traces) ; tête de branche = commit attendu ; arbre propre ; nom scellé `prereg/test-echelle-conscience-eval-v8.md` libre ; `problemes()` ne relève que la section « Contre-lecture » à remplir.
- **Tests** : 344 passent chez moi (440,7 s), comme la trace (440,3 s) ; les décomptes du tableau R5 concordent avec la collecte (85, 85, 12, 11, 11, 10, 3 et 1 pour la cohérence rapportée).
- **CLU-01 pour la classe telle que cl6 l'a décrite** (fuite égale, jeux de même force) :
  - les trois cas fabriqués de cl6, rejoués contre `lire()` v7 avec l'écart pris au milieu des intervalles, rendent « désaccord des deux sens » (la v6 lisait « positif », « inverse » et « nul ») ; les six cas de cl5 et les quatre autres cas de cl6 rendent exactement les lectures et le nombre de réserves de la v6 consignés par cl6 (`sorties/sortie-cas-limites-lire-v7.txt`) ;
  - **rejeu versé des bancs de cl5 et cl6, vérifié et non cru** (`scripts/verifier_rejeu.py`) : intervalles de λ identiques à ceux que les bancs ont consignés, 176 sur 176 ; e(m) du rejeu égal, à l'arrondi près (écart maximal 0,001 sur 352), à la différence des λ ponctuels consignés par les bancs ; les 27 différences d'issues tenues entre bancs et rejeu ne sont que le nom « fuite de signe inverse » de la v5 devenu « (petit) » ou « (grand) » ; 16 lectures changent, toutes « positif » ou « inverse » tenus dans les deux sens sans la cohérence : les 10 artefacts de cl6 (7 « positif », 3 « inverse » ; les deux modèles incohérents dans les 10, |e| de 0,338 à 0,572) et 6 « positif » vrais. Une analyse refaite par mon propre banc (graine 22200) redonne e = 0,384 et 0,411 ;
  - mon banc sur la classe elle-même, à des amplitudes et une dimension nouvelles (±1,6 et ±2,0 sous λ 0,5 ; ±1,2 sous λ 0,7 ; dimension 512 à ±1,3 ; 22 analyses) : **aucune issue prononcée** (désaccord 8, non confirmé 10, indécis 4) ; dans la simulation scellée, 144 analyses, aucune ;
  - le choix du point contre « l'intervalle qui rencontre » est juste pour l'objet qu'il vise : l'exploration versée le montre (sur 7 artefacts, 1 passe avec « rencontre », 0 avec le point ; 18, 17 et 15 « positif » sous H_A) et mes chiffres le confirment ; mais voir CLT-01 pour la classe voisine.
- **Concordance du texte et du code** :
  - `coherence` (l. 488–497) : |e(m)| ≤ δ en point, inégalité large, pour chacun des deux modèles ; intervalle rapporté ; `lire` (l. 591–594) : « positif », « inverse » et « nul » tenus dans les deux sens ne sont communs que si aucun modèle ne rompt la cohérence ; fuite de signe inverse et « pas de fuite » non concernées ; conditions manquantes de chaque issue incohérente = les énoncés des modèles qui la rompent ; aucune réserve sur « désaccord » ;
  - « une issue tenue dans les deux sens sans la cohérence ne précède jamais l'étape prononcée » est exact : « positif » exclut toute autre issue d'un sens (borne basse de λ(petit) > δ, de Δλ > δ, de λ(grand) > −δ, et donc borne haute de λ(grand) > −δ), « inverse » de même, et « nul » est la dernière étape ;
  - le reste (cinq étapes, inégalités, réserves, mode décisif, `SEUILS`, commandes du lancement, de la surveillance et de l'analyse, liste d'arrêt) est inchangé depuis la v6 et conforme, ligne à ligne ; la liste d'arrêt de la surveillance dit les bornes du code (`borne` : entier sans zéro de tête, [1 ; 30], [1 ; 60], [0 ; 60]).
- **Simulation** : le tableau du texte est identique, ligne à ligne, au tableau versé (57 lignes), lui-même tiré de la sortie ; les comptes se recalculent depuis le détail des 386 analyses ; 21 noms sur 26 atteints, les cinq autres ceux que le texte nomme ; phrase R3 exacte sur ses comptes (48, 32, 24, 144 analyses sans « positif » ni « inverse » ; doubles signatures : 12 analyses, « positif » 3, « inverse » 4) ; audit exact (27 lectures fausses de la règle v6 = 12 « positif » + 15 « inverse », 10 en dimension 64 et 17 en 256, 25 à deux modèles incohérents et 2 à un seul ; 37 « positif » vrais perdus : 18 + 10 + 5 + 2 + 1 + 1) ; 41 cases communes avec la v6, 3 changent, comme le texte le dit ; 17 cases communes avec la v3, comme le texte le dit. **Reproduite à l'octet près** : ma sortie, faite au commit `b54da1f` (arbre propre), a l'empreinte de la sortie versée, `84fd1638…`.
- **Prix sous H_A** : chiffré honnêtement (contexte du jeu b × 0,6 : 18 sur 18 perdus ; × 0,8 : 10 sur 18 ; signature d'un seul jeu sous H_A : 5 sur 6, et dans les bancs 6), et la règle « les deux modèles » écartée est chiffrée.
- **Surveillance** (CLU-02, CLU-03), essai versé rejoué sur la surveillance du commit (`sorties/sortie-latence-cl7.txt`) : appels de 29 s, arrêt demandé 56,6 s après le plafond ; appels bloqués coupés à 30 s, 58,7 s ; pause qui rencontre le plafond, 0,8 s et 0,9 s ; `APPEL_S=0` et `PAS_S=abc` refusés, code 2, aucun appel ; réglages réels complets (`ATTENTE_ARRET_S` à son défaut de 20 s, que l'essai versé ramène à 0), 57,0 s. La borne de 90 s tient avec un outil qui obéit au signal d'arrêt (voir CLT-04 sinon).
- **Clonage borné** (CLU-04) : `timeout --kill-after=30s 600s git clone`, refus avec la ligne de fin ; la répétition l'éprouve (faux git bloqué, refus à 5 s, rien de poussé) et le cas sain écrit la borne de 600 s.
- **Dépense** :
  - choix d'offre v7 rejoué sur les 45 offres : offre 50510069, 7 200 s, pire 7,0311 USD, estimé 5,4044, attendu 3,8072, comme la trace ; seconde offre conforme à 8,00 USD tout juste ;
  - balayage fin du domaine admis (prix 0,20 à 3,50 USD/h, descente, remontée et stockage admis ; `offres/`), dépense réelle au prix majoré de 5 % : **7,89 USD au pire avec 90 s de retard**, 7,95 avec 150 s, 8,00 avec 195 s, 8,0001 avec 196 s ; la marge couvre donc exactement 195,9 s, comme le texte et le test le disent ; hypothèses non gardées dites (CLT-03 pour une précision) ;
  - la ligne de GO du texte, jouée sur un faux registre contre `verifier_go_v7.py` : « conforme » ; « 8 USD au pire » refusé (« plafond illisible ») ; une ligne qui cite le texte v7 refusée (`sorties/sortie-forme-go-v8.txt`). Le registre réel ne contient aucun GO qui cite `test-echelle-conscience-eval-v8`.
- **Gardes héritées** : code inchangé (mêmes empreintes que cl4 à cl6) ; `exiger_prereg_scelle` exige le compagnon conforme et toutes les sections remplies.
- **R7** : citations du texte inchangées depuis la v7 (vérifiées par cl6) ; contrôle par sondage dans les cartes (0,644, tableau 15, p. 23 ; 0,491 en prose, p. 5 et p. 12 ; 0,676, p. 10, 21 et 24 ; ii-3, p. 6, 9, 15 et 8) : conformes.
- **R9, R10, R12** : `SeedSequence(4429003211691042563)` inchangée ; versions et commit consignés par l'analyse et la simulation ; arrêts par identifiant ; noms neufs (`…_v7`, `analyse-echelle-v7.json`, branche `donnees/echelle-conscience-eval-v7`, texte scellé `…-v8.md`).
- **R3** : je n'ai trouvé aucun degré de liberté qui permette de viser un signe ; la cohérence est appliquée de la même façon à « positif », « inverse » et « nul » ; ses pertes (prix) et ses fuites (CLT-01) sont symétriques en signe.

## Traitement des constats de cl6

| constat de cl6 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLU-01 « positif », « inverse », « nul » portés par des modèles différents d'un sens à l'autre | bloquant | **traité pour la classe décrite par cl6** (fuite égale, jeux de même force) ; **la classe voisine reste ouverte** (CLT-01) | Cas fabriqués de cl6 : « désaccord ». Rejeu versé vérifié (176 sur 176 ; 10 artefacts bloqués, les deux modèles incohérents). Mon banc : aucune issue prononcée sur 22 analyses de la classe à ±1,2 à ±2,0 et en dimension 512. Mais un écart vrai sous δ, ou un contexte d'un jeu plus fort de 33 %, rouvre la classe : 15 « positif » ou « inverse » sous H_0 et 4 « nul » sous H_A, sans réserve (CLT-01). Le prix sous H_0 n'est chiffré qu'à × 0,8 (CLT-02) |
| CLU-02 réglages de la surveillance sans contrôle | à corriger | **traité** | `borne` dans le code, 10 artefacts et 3 cas sains testés ; `APPEL_S=0` et `PAS_S=abc` refusés dans mon rejeu ; réglages écrits en tête d'`etats.txt` et dans `arret.txt`. Reste : `timeout` sans `--kill-after` (CLT-04) |
| CLU-03 preuve de latence et test du plafond | remarque | **traité** | Essai versé rejoué (56,6 ; 58,7 ; 0,8 ; 0,9 s), test du plafond à 195,9 s, commentaire de `MARGE` corrigé ; mon balayage : 8,00 USD à 195 s |
| CLU-04 clonage non borné | remarque | **traité** | Borne de 600 s (+ 30 s), testée par la répétition. Reste : le délai du calcul est compté avant le clonage, si bien que l'amorce ne borne plus le calcul à « création + durée − 600 s » (CLT-03) |
| CLU-05 phrases et tests | remarque | **traité** | « Issues atteintes » exacte (21 sur 26, les cinq nommées) ; compte des bancs rejoués exact (20 analyses : indécis 11, positif 4, non confirmé 3, désaccord 1, nul non confirmé 1) ; « ne changent pas de décision » ; `test_texte_des_reserves` (12 cas, texte et miroir) |

Bilan : 5 constats traités, dont 3 avec un reste (CLU-01, CLU-02, CLU-04) ; aucun non traité.

## Constats nouveaux

### CLT-01 — BLOQUANT — La cohérence des deux sens ne ferme la classe de cl6 qu'en son centre : un écart vrai sous δ, ou une différence de force du contexte entre les jeux, la rouvre ; « positif », « inverse » et « nul » faux, sans réserve

- **Localisation** :
  - `analyser_echelle_v7.py` : `coherence`, l. 488–497 (|e(m)| ≤ δ, la même bande que la décision) ; `lire`, l. 591–594 ; `reserves` (aucune réserve ne regarde e(m)) ;
  - brouillon v8 : « Seuil », justification de la cohérence, l. 179 (« l'écart e(m) d'un modèle vaut, au bruit près, le Δλ du sens que sa signature déplace ») ; Hypothèse, l. 84 ; H_0, l. 94 (« |Δλ| ≤ δ », « différence de force du contexte entre les deux jeux ») ; Mesures, l. 141–143 ; R3, l. 249 ; limites, l. 371–372 (« la cohérence des deux sens les écarte » ; « près du seuil, le bruit… ») ; traitement de CLU-01, l. 486.
- **Constat** :
  - Notons d le vrai écart d'échelle de la fuite du concept, p_a la poussée (en unités de λ) de la signature du jeu a sur le 8B, qui ne déplace que le sens a→b, et p_b celle de la signature du jeu b sur le 70B, de signe opposé, qui ne déplace que le sens b→a (la classe de cl6). Avec deux jeux de même force de contexte :
    - Δλ_a→b ≈ d + p_a et Δλ_b→a ≈ d + p_b ;
    - e(8B) ≈ p_a et e(70B) ≈ p_b, soit **e(m) ≈ Δλ du sens que la signature déplace, moins d**.
  - L'argument du texte (l. 179) pose d = 0. Pour d > 0, « positif » tient dans les deux sens dès que la borne basse de d + p dépasse δ, et la cohérence dès que p ≤ δ : la fenêtre δ − d + 2σ < p ≤ δ (σ l'erreur type de Δλ) est ouverte dès que d dépasse 2σ. Un écart vrai de 0,15 à 0,2, rangé dans H_0 par le texte (|Δλ| ≤ δ), devient « positif ». En miroir, « inverse » ; et, sous H_A (d de 0,3 à 0,35), des poussées de sens contraire compensent l'écart : « nul » faux.
  - λ est relatif à l'effet du contexte sur le jeu **mesuré** (CLZ-02 ; texte, l. 143). Si le contexte du jeu b vaut k fois celui du jeu a, chaque λ du sens a→b est divisé par k : e(m) gagne un terme λ(m)·(1/k − 1), de signe connu, qui peut **compenser** l'écart que la signature crée. Sous une fuite **égale** (la classe de cl6 au sens strict), avec k ≈ 1,33 et les signatures croisées dans le bon ordre, les deux modèles gardent |e(m)| ≤ δ, et « inverse » (ou « positif ») passe.
  - Aucune réserve ne le voit : les spécificités restent loin de zéro (le témoin ν est aveugle aux signatures, CLY-01) ; « nul » n'a pas de réserve de spécificité.
  - Le texte écrit bien le **prix** de la cohérence (un « positif » vrai perdu devient « désaccord », jamais une issue fausse) ; il n'écrit pas que la cohérence **laisse passer** les voisins de la classe : la phrase R3 et la limite ne parlent que de la fuite égale et prêtent le reste au bruit (l. 372). Or le texte range lui-même ces voisins dans H_0 (l. 94).
  - La bande de la cohérence (δ) est aussi large que la décision qu'elle protège : elle borne à δ, par modèle et par sens, la part d'un écart d'échelle qui peut être portée par un modèle différent dans chaque sens ; elle ne l'annule pas.
- **Preuve** :
  - Cas fabriqués, `lire()` v7 telle quelle (`sorties/sortie-cas-limites-lire-v7.txt`) :
    - a→b : λ(8B) [0,68 ; 0,92], λ(70B) [0,30 ; 0,50], Δλ [0,28 ; 0,52] ; b→a : λ(8B) [0,48 ; 0,72], λ(70B) [0,10 ; 0,30], Δλ [0,28 ; 0,52] (écart vrai 0,2, +0,2 au 8B en a→b, −0,2 au 70B en b→a ; e = 0,2 pour chaque modèle) : **« positif », aucune réserve** ;
    - le miroir : **« inverse », aucune réserve** ;
    - écart vrai 0,4 compensé de 0,22 dans chaque sens par un modèle différent : **« nul », aucune réserve**.
  - Banc, analyse v7 du commit telle quelle (mode répétition, 300 tirages), générateur de cl6 recopié à l'identique, dimension 256, tau 0,15 (`banc/banc-cl7-principal.jsonl`, `sorties/sortie-analyse-banc-cl7.txt`) :

    | famille | vérité (λ du concept au 8B et au 70B) | cas (graines) | lectures |
    |---|---|---|---|
    | B : écart vrai sous δ, signatures croisées de signes opposés | H_0 (0,6 et 0,4) | jeu a +0,5 au 8B, jeu b −0,5 au 70B (40000 à 40014) | **positif 3, sans réserve** ; indécis 4 ; positif non confirmé 1 |
    | | H_0 (0,6 et 0,4) | idem ±0,6 (40100 à 40114) | **positif 3, sans réserve** ; indécis 2 ; non confirmé 2 ; désaccord 1 |
    | | H_0 (0,55 et 0,4) | idem ±0,55 (40200 à 40214) | **positif 2, sans réserve** ; indécis 4 ; non confirmé 2 |
    | | H_0 (0,55 et 0,4) | jeu b +0,55 au 8B, jeu a −0,55 au 70B (40300 à 40314) | positif non confirmé 4 ; indécis 4 |
    | | H_0 (0,4 et 0,6), miroir | jeu a −0,55 au 8B, jeu b +0,55 au 70B (40400 à 40414) | **inverse 2, sans réserve** ; indécis 3 ; non confirmé 2 ; désaccord 1 |
    | | H_0 (0,5 et 0,4) | ±0,6 (40500 à 40510) | indécis 5 ; non confirmé 1 |
    | | **témoin** H_0 (0,6 et 0,4), sans signature | (40600 à 40606) | indécis 4 |
    | C : écart vrai au-delà de δ, compensé | H_A (0,65 et 0,35) | jeu a −0,55 au 8B, jeu b +0,55 au 70B (42000 à 42010) | **nul 3, sans réserve** ; indécis 2 ; nul non confirmé 1 |
    | | H_A (0,7 et 0,35) | ±0,6 (42100 à 42110) | **nul 1, sans réserve** ; indécis 3 ; désaccord 1 ; non confirmé 1 |
    | | **témoin** H_A (0,65 et 0,35), sans signature | (42200 à 42206) | indécis 4 |
    | D : fuite égale, contexte d'un jeu plus fort ou plus faible | H_0 (0,7 et 0,7), jeu b × 1,333 | jeu b −1,2 au 8B, jeu a +1,2 au 70B (41300 à 41310) | **inverse 4, sans réserve** ; indécis 2 |
    | | H_0 (0,7 et 0,7), jeu b × 0,75 | jeu b +1,0 au 8B, jeu a −1,0 au 70B (41000 à 41010) | **positif 1, sans réserve** ; indécis 2 ; non confirmé 2 ; désaccord 1 |
    | | H_0 (0,7 et 0,7), jeu b × 0,75 | idem ±1,2 et ±1,4 (41100 à 41210) | désaccord 10 ; indécis 2 |
    | | H_0 (0,7 et 0,7), jeu b × 1,25 ou × 0,75, autres ordres | (41400 à 41410, 41600 à 41606) | indécis 5 ; non confirmé 4 ; désaccord 1 |
    | témoins de l'outil | H_0 (0,5 et 0,5) ; H_A (1,0 et 0,2) | (45000 à 45006 ; 45100 à 45106) | nul 4 ; positif 4 |

    - Dans les 19 lectures fausses, aucune réserve ; |e(m)| ≤ δ pour les deux modèles : de 0,13 à 0,24 (B), 0,15 à 0,24 (C), 0,08 à 0,24 (D) ; bornes de spécificité loin de zéro (« positif » : borne basse ≥ 0,094 ; « inverse » : borne haute ≤ −0,148).
    - Exemple, graine 40102 (B, vérité H_0 : écart vrai 0,2) : a→b, λ(8B) 0,811, λ(70B) 0,354, Δλ [0,33 ; 0,57] ; b→a, λ(8B) 0,610, λ(70B) 0,140, Δλ [0,35 ; 0,58] ; e = +0,201 et +0,214 ; spécificités [0,19 ; 0,55] et [0,25 ; 0,59] : « positif ».
    - Exemple, graine 41306 (D, fuite égale 0,7 et 0,7) : Ec du jeu b / Ec du jeu a = 1,28 et 1,27 ; a→b, λ(8B) 0,467, λ(70B) 0,902 ; b→a, λ(8B) 0,391, λ(70B) 0,813 ; Δλ [−0,56 ; −0,33] et [−0,56 ; −0,29] ; e = +0,076 et +0,089 : « inverse ».
    - **À 2 000 tirages** (`banc/banc-cl7-n2000.jsonl`) : les quatre gardent leur lecture, sans réserve. Graine 40102 : « positif », Δλ [0,33 ; 0,57] et [0,35 ; 0,60], e = +0,201 [0,07 ; 0,33] et +0,214 [0,08 ; 0,37], spécificités [0,21 ; 0,56] et [0,25 ; 0,60] ; graine 40400 : « inverse », Δλ [−0,55 ; −0,31] et [−0,58 ; −0,28], e = −0,191 et −0,185 ; graine 42000 (H_A, écart vrai 0,3) : « nul », Δλ [−0,04 ; 0,17] et [−0,06 ; 0,18], e = −0,179 et −0,182 ; graine 41306 (fuite égale) : « inverse », Δλ [−0,56 ; −0,32] et [−0,55 ; −0,29], e = +0,076 [−0,04 ; 0,19] et +0,089 [−0,05 ; 0,24]. Certification partout au-dessus de 0,93.
  - Les témoins sans signature (B et C) lisent « indécis » 8 fois sur 8 : les issues fausses viennent des signatures, pas du bruit autour du seuil.
- **Correction** :
  - **(a) Au minimum, le texte** :
    - limites : écrire que la cohérence ne borne qu'à δ, par modèle et par sens, la part de l'écart d'échelle portée par un modèle différent dans chaque sens ; que, sous un écart vrai sous δ (H_0) ou au-delà (H_A), ou sous une différence de force du contexte entre les jeux, des signatures d'un seul jeu, croisées et de signes opposés, chacune sous δ, fabriquent « positif », « inverse » ou « nul », sans réserve ; que la classe de cl6 n'est close qu'en son centre ; « toute issue prononcée se lit sous cette limite », comme pour les doubles signatures ;
    - « Seuil », l. 179 : e(m) ≈ Δλ_s − d (plus l'effet d'une différence de force du contexte), et non Δλ_s ; R3, l. 249 : borner la phrase à ce qui est simulé et dire la classe voisine ; l. 372 : ce n'est pas seulement le bruit ;
    - simulation : ajouter ces voisins (écart vrai 0,15 à 0,2 sous des signatures croisées sous δ, et son miroir ; H_A 0,3 compensé ; fuite égale avec un contexte d'un jeu × 1,33 et × 0,75), et en rapporter les lectures.
  - **(b) Mieux, une garde ou une réserve mécanique**, à simuler avant d'être choisie (prix sous H_A) :
    - réserve obligatoire « le λ du modèle M change d'un sens à l'autre » quand l'**intervalle** de e(m), déjà calculé et rapporté, exclut zéro pour un modèle (aucun paramètre nouveau) : dans mon banc, elle signale 18 des 19 lectures fausses (pas la graine 41306) ; dans la simulation scellée, sous des vérités sans signature ni différence de contexte, 1 « positif » sur 28 et 1 « nul » sur 19 (`sorties/sortie-bande-etroite-simulation.txt`) ;
    - réserve obligatoire « écart d'échelle en partie porté par des modèles différents (modèle nommé) » quand |e(m)| > δ/2 pour un modèle, sur « positif », « inverse » et « nul » : dans mon banc, elle signale 18 des 19 lectures fausses (pas la graine 41306, |e| ≤ 0,09) ; dans la simulation scellée, sous des vérités sans signature ni différence de contexte, elle signalerait 2 « positif » sur 28 et 1 « nul » sur 19 (`sorties/sortie-bande-etroite-simulation.txt`) ;
    - réserve « jeux de force de contexte inégale » quand, pour un modèle, le rapport des Ec des deux sens (donc des deux jeux mesurés) sort d'une bande fixée sans donnée, par exemple [0,8 ; 1,25] : dans mon banc, ce rapport vaut 1,17 à 1,34 ou 0,75 à 0,87 dans les cas D, et 0,93 à 1,05 dans les témoins (`sorties/sortie-ec-banc-cl7.txt`) ; elle signalerait la graine 41306 ; Ec est déjà rapporté par modèle et par sens, sans lecture ;
    - ou une marge : borne basse de Δλ_s diminuée de |e(petit)| + |e(grand)| au-delà de δ, dans chaque sens (miroir pour « inverse ») : elle écarte les 15 « positif » et « inverse » faux de mon banc et garde les 4 « positif » du témoin H_A, mais coûterait cher sous un H_A faible : à simuler.
  - Dans tous les cas : texte nouveau, contre-lecture neuve des parties changées (R2) ; avec (b) : noms, commit, tests (les cas fabriqués ci-dessus, en direct et en miroir) et simulation nouveaux.

### CLT-02 — À CORRIGER — Prix de la cohérence sous H_0 : « nul » est perdu dès que λ·|1/k − 1| dépasse δ ; le texte ne le chiffre qu'au réglage où il ne coûte rien

- **Localisation** : brouillon v8, l. 252 (« Sous H_0 avec un contexte du jeu b × 0,8, « nul » tient (12 sur 12) ») et l. 374 (même phrase dans les limites) ; simulation v7, `VERITES_V7` (un seul cas H_0 à contexte inégal : λ 0,5, × 0,8).
- **Constat** :
  - Une différence de force du contexte entre les jeux multiplie les λ d'un sens par 1/k : sous H_0, chaque modèle a e(m) ≈ λ(m)·(1/k − 1), de même signe chez les deux. Au seul cas H_0 simulé (λ 0,5, k 0,8), e ≈ 0,125, la moitié de δ : la cohérence n'y coûte rien, d'où « 12 sur 12 ».
  - Le prix sous H_A est chiffré à × 0,6 et × 0,8, là où il mord ; sous H_0, il ne l'est qu'à × 0,8 et λ 0,5. Or l'issue « nul » la plus plausible au vu de la prédiction du texte (λ(8B) de 0,5 à 1) est une fuite égale et forte, où le prix mord vite : à λ 0,7, dès k < 0,74 ou k > 1,56 ; à λ 1, dès k < 0,8 ou k > 1,33. La symétrie R4 du rapport du prix n'est pas tenue.
- **Preuve** (`sorties/sortie-analyse-banc-cl7.txt`) : « nul » tenu dans les deux sens et perdu en « désaccord » par la seule cohérence :
  - λ 0,5 et 0,5, jeu b × 0,6, dimension 64, tau 0,15 : 3 sur 6 (e de 0,25 à 0,35) ; dimension 256 : 1 sur 6 (les autres « nul non confirmé », le jeu faible élargissant les intervalles) ;
  - λ 0,7 et 0,7, jeu b × 0,75 : 2 sur 4 (e de 0,24 à 0,30) ; × 0,7 : 1 sur 6 ;
  - λ 0,9 et 0,9, × 0,8 : « nul » 2 sur 6, avec e de 0,17 à 0,245, au bord de δ.
- **Correction** : ajouter à la simulation H_0 sous un contexte × 0,6 (et une fuite égale de 0,7 à 0,9 sous × 0,75 à 0,8) ; écrire dans les limites la formule e(m) ≈ λ(m)·(1/k − 1) et la perte de « nul » qu'elle entraîne ; dire que la cohérence coûte davantage aux fuites fortes, que « pas de fuite » n'y perd rien, et que le rapport des Ec des deux sens montre k.

### CLT-03 — REMARQUE — Le délai du calcul est compté avant le clonage : l'amorce ne borne plus le calcul à « création + durée − 600 s »

- **Localisation** : `amorce_echelle_v7.sh`, l. 43–44 (délai calculé) puis l. 67 (clonage, jusqu'à 600 s + 30 s) puis l. 73 (`timeout --kill-after=2m "${DELAI_S}s"`) ; brouillon v8, l. 64 et l. 70.
- **Constat** : le calcul commence après le clonage avec un délai pris avant lui ; il finit donc au plus tard à création + durée − 600 s + durée du clonage (≤ 630 s) + 120 s, soit **jusqu'à 150 s après le plafond**. C'est sans effet quand la surveillance tourne (elle arrête l'instance au plus 90 s après le plafond) ; quand la session locale est morte, c'est l'amorce seule qui borne. Le défaut existait en v6 (clonage non borné, donc pire) ; la borne de CLU-04 le réduit sans l'annuler, et le texte dit une borne plus serrée qu'elle n'est.
- **Preuve** : lecture du code ; mon balayage de la dépense (`offres/`) : avec 150 s de retard, 7,95 USD au pire ; la marge (195,9 s) couvre donc ce cas, de justesse.
- **Correction** : recalculer le délai (et le contrôle des 45 min) après le clonage ; ou écrire la borne vraie (« création + durée − 600 s + durée du clonage, soit au plus le plafond + 150 s ») et qu'elle tient sous la marge.

### CLT-04 — REMARQUE — Les appels de la surveillance sont bornés par `timeout` sans `--kill-after` : la borne de 30 s suppose que l'outil obéit au signal d'arrêt

- **Localisation** : `surveiller_echelle_v7.sh`, l. 60, 75 et 89 ; brouillon v8, l. 62 et 426 (« chaque appel à vastai de la surveillance est borné à `APPEL_S`… »).
- **Constat** : `timeout N cmd` n'envoie que TERM ; un processus qui l'ignore, ou qui reste bloqué sans le traiter, n'est pas tué. L'amorce, elle, emploie `--kill-after` pour le clonage et le calcul. vastai, écrit en Python, meurt sur TERM par défaut : le risque est faible, mais la borne écrite dépend d'un comportement de l'outil qui n'est ni gardé ni dit.
- **Preuve** : cas (h) de mon essai, faux outil qui ignore TERM et ne rend pas la main (300 s) : chaque appel dure ses 300 s au lieu d'être coupé à 30 s ; arrêt demandé **598,1 s** après le plafond, code 5 (`latence/essai/h-outil-sourd-a-term/`). Au prix le plus haut admis, 600 s de retard coûteraient ≈ 0,61 USD, au-delà de la marge (0,20 USD, 195,9 s). La dépense reste pourtant bornée : l'amorce sort du conteneur au plus 150 s après le plafond (CLT-03), et un conteneur sorti n'est facturé que pour son stockage (hypothèse dite) ; ce qui ne tient pas, c'est la borne de 90 s que le texte attribue à la surveillance seule. Le cas (b) des essais versés emploie un `sleep` qui obéit au signal.
- **Correction** : `timeout -k 5 "$APPEL_S" …` aux trois appels ; ajouter ce cas aux tests (faux outil `trap '' TERM`) ; ou écrire que la borne de 90 s suppose un outil qui obéit au signal, et que l'amorce reste la borne de dernier recours.

### CLT-05 — REMARQUE — Phrases et détails

- **Phrase permise du désaccord** (l. 340) : elle commence par « Les deux sens lisent deux issues différentes (a→b : X ; b→a : Y) », ce qui est faux quand les deux sens lisent la même issue sans la cohérence ; la phrase propre à ce cas suit, sans dire qu'elle **remplace** la première. Écrire deux phrases distinctes (ou nommer l'issue différemment, par exemple « désaccord des deux sens (cohérence) ») : le seul nom ne dit pas laquelle des deux situations est lue.
- **Cas tranché par cl4** (l. 309) : « une fuite de signe inverse dans un seul sens et « nul » dans les deux donne « nul », avec la réserve » n'est plus vrai que sous la cohérence ; les tests le montrent (`{**FSI, **sens_ba(NUL)}` et `{**PDF_NUL, **sens_ba(NUL)}` : « nul » en v6, « désaccord des deux sens » en v7). Ajouter « sous la cohérence des deux sens ».
- **« pas de fuite » ne la demande pas : ses quatre intervalles de λ sont déjà dans [−δ ; δ]** (l. 302) : ce n'est pas une raison suffisante, |e(m)| peut y atteindre 2δ (le test `{**PDF, "ecart": 0.35}` le montre) ; la vraie raison est que « pas de fuite » ne compare pas les deux modèles. Le dire.
- **Essai « aux réglages réels »** (l. 62, 464) : l'essai versé ramène `ATTENTE_ARRET_S` à 0 (sans effet sur le retard mesuré : 57,0 s avec 20 s dans mon cas g) ; le dire.
- **Exploration de la cohérence** (l. 180) : elle a tourné sur un état de l'analyse **non commité** (son `LISEZ-MOI.txt` le dit) ; le texte devrait le dire aussi (R6).
- **Branche d'outils** : dans ce clone, `outils/echelle-conscience-eval-v7` n'existe qu'en local (aucune référence de suivi) ; je ne peux pas vérifier le dépôt distant sans réseau. Le lanceur refuse sans dépense si la tête distante n'est pas le commit : la pousser avant le GO.

## Annexe — pièces de cl7

Dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v8/` :

- `scripts/` : `verif_empreintes_v8.py`, `verifier_rejeu.py`, `diff_tenues.py`, `verifier_tableau.py`, `cas_limites_lire_v7.py`, `banc_cl7.py` (générateur de cl6 recopié à l'identique : contrôlé par `diff` du corps de `fabriquer`), `resumer_banc.py`, `analyser_banc_cl7.py`, `latence_cl7.py` ;
- `sorties/` : `tests-cl7.txt`, `tests-cl7-debut.txt`, `sortie-verif-empreintes-v8.txt`, `sortie-verifier-rejeu.txt`, `sortie-verifier-tableau.txt`, `sortie-cas-limites-lire-v7.txt`, `sortie-analyse-banc-cl7.txt`, `sortie-ec-banc-cl7.txt`, `sortie-bande-etroite-simulation.txt`, `sortie-latence-cl7.txt`, `sortie-forme-go-v8.txt` ;
- `banc/` : `banc-cl7-calibrage.jsonl` (4 analyses), `banc-cl7-principal.jsonl` (158 analyses, de 09:17:57 à 09:31:26 UTC), `banc-cl7-n2000.jsonl` (2 000 tirages), journaux et heures ;
- `simulation/` : reproduction de la simulation scellée (sortie, journal, heures) ;
- `latence/` (faux outils, `lancement.txt`, sorties de la surveillance) ; `faux-go/` (faux registre) ; `offres/` (choix d'offre rejoué) ; `diffs/` (v6 → v7, et `diff-v7-v8-mots.txt`).
