# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v4) — cl3

- **Rôle** : sous-agent neuf, troisième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v4, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 (cl1) et n° 2 (cl2).
- **Date** : 27 octobre 2026. Lecture commencée à 01:52:05 UTC, rapport écrit à partir de 02:18:23 UTC (`date -u`).
- **Empreintes (sha256)** :

  | pièce | sha256 |
  |---|---|
  | `prereg/brouillon-test-echelle-conscience-eval-v4.md` (texte relu ; conforme à son compagnon, inchangé du début à la fin de ma lecture) | `8c0d19dc65d2e0bf2b51f248077a8bea861b266c7da9df081a6fc8d7d646f523` |
  | `echelle-v3/scripts/analyser_echelle_v3.py` (conforme au tableau du texte, à son compagnon et à l'objet du commit) | `e65a916bb5d45b9fb0673190eb3ca5ad5771de356b29c77ba17af0576773653d` |
  | `prereg/brouillon-test-echelle-conscience-eval-v3.md` | `62221ab3865c0e33a3c59e41f66695206815bce4fa8dd2a031097c4b42f81667` |
  | `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v3-cl2.md` | `9b476cf4b64a521f97cc7368ca60723e41390557291570fc6c08f30369b04803` |
  | `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md` | `70afa51997f66f882f79686765c9b1fdded6f0016007b626355b975abd9e673a` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md` | `134040bd9a126dce4592aa3b357375f0209f987610d3be21a6848f647eaf59b4` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v2.md` | `fe1e93c1efe7c9117c9f0b22711912394c5b40d0180b904bf61e324cf0943d3a` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v3.md` | `9d03d3b212ca43d3eb905413f95f808ef2bc90376b284804a9ed1dbd28ddc3de` |

- **Code relu** dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` :
  - branche `outils/echelle-conscience-eval-v3`, tête `c08a5b21df42aa10f7c7351173ccb75ed5a101ca` : c'est le commit attendu, et la branche distante locale pointe au même endroit ; arbre propre avant et après mes essais ;
  - les 27 empreintes complètes du brouillon (18 outils, 9 traces) concordent avec les fichiers et avec leurs compagnons ; pour les 18 outils, aussi avec les objets du commit (`scripts/verif_empreintes.py`, sortie `sortie-verif-empreintes.txt`) ;
  - la v2 (`echelle-v2/`) a servi aux comparaisons : `diff` de neuf fichiers de `scripts/` et des tests d'offre, et rejeu de CLY-01 et CLY-02 avec `analyser_echelle_v2.py` tel quel.
- **Lu en entier** :
  - le brouillon v4, le brouillon v3, cl2 et cl1 ;
  - les douze fichiers nouveaux de `echelle-v3/scripts/`, les quatre fichiers de tests, `.gitignore`, `construction-echelle-v2.json` ; `construire_echelle_v2.py` et `echelle-v2.json` sont identiques à l'octet à ceux de `echelle-v2/`, les outils du brouillon v3 (`cmp`) ; les stimuli ne sont lus que par Python ;
  - les traces citées : accès, offre de référence, gabarits, contrôles lexicaux, sortie des tests, répétition de l'instance (résumé, commit, empreintes, quatre journaux sur sept), atteignabilité ; `offres-relues-reference-v1.json` par Python ;
  - les passages des cartes v1 à v3 que le texte cite.
- **Non lus**, hors de ma liste comme pour cl2 : `src/controle_ia/prereg.py` et `.claude/hooks/garde_calcul.py`. Les gardes héritées du lanceur restent donc non relues par une contre-lecture.
- **Interdits respectés** :
  - aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt (seules des listes de dossiers nommés) ;
  - aucun réseau, aucune commande vastai, aucun lancement, aucune poussée, aucun commit ; rien de modifié hors de mon bac à sable.
  - Aucun `__pycache__` créé par mes essais (`-B` et `PYTHONDONTWRITEBYTECODE=1`). Les deux dossiers `__pycache__` présents dans l'arbre relu datent de 01:11:56 et 01:15:53 UTC, avant ma lecture ; `.gitignore` les ignore ; je ne les ai pas touchés.
- **Essais** (scripts jetables et sorties dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v4/`) :
  - tests du commit : `80 passed in 210.21s`, avec le modèle minuscule local (`tests-cl3.txt`) ;
  - simulation d'atteignabilité rejouée avec le script scellé et ses graines (`reproduction-atteignabilite/`) ;
  - trace lexicale rejouée (`lexique-reproduit/`) ; choix d'offre rejoué sur la trace de 43 offres (`offres/`) ;
  - dépense réelle au pire balayée sur tout le domaine admis (`scripts/pire_tolerance.py`) ;
  - `etat_scripts()` réel (et non remplacé par un faux) essayé sur un clone jetable du commit, puis supprimé (`sortie-etat-scripts.txt`) ;
  - refus de l'amorce (`sortie-amorce-essais.txt`) ; comportement de `timeout` sur un groupe de processus ;
  - `scripts/banc_v4.py` : 30 analyses synthétiques à vérité connue, analyse v3 **telle quelle** (mode `--repetition`, 300 tirages au lieu de 2 000, d = 64) ; générateur repris du test v3, étendu (signature de signe libre, signature du jeu b, force du contexte par jeu) ;
  - `scripts/rejouer_cly01_cly02.py` : mêmes activations analysées par la v2 puis par la v3 (16 analyses) ;
  - `scripts/details_h1_tau08.py` : les quatre analyses « H1 ; tau 0,8 » de la simulation, avec le détail du sens b→a.

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLZ-01** : la correction de CLY-01 n'exige le contrôle symétrique que pour « positif » et « inverse ». La même signature des cadrages a, de signe négatif, fabrique une « fuite de signe inverse » (4 sur 4 dans le banc) et peut masquer un écart d'échelle vrai en « nul » ou en « pas de fuite ». Ces trois lectures se prononcent sur le sens a→b seul, sans réserve, alors que le sens b→a les contredit. C'est l'asymétrie que R4 interdit, et le texte range lui-même ces effets dans H_0.

Corrections à faire avant le scellement :

- CLZ-01 (bloquant) ;
- CLZ-02 à CLZ-04 (à corriger) : phrase de « non confirmé », tolérance de 5 % sur le prix relu, gardes nouvelles non éprouvées (R5).

CLZ-01 et CLZ-02 touchent `lire()` ; CLZ-03 et CLZ-04 touchent le choix d'offre, le lanceur, l'amorce et la répétition. Il faut donc, comme après cl2 :

- des noms nouveaux (R12), un commit et des empreintes nouveaux ;
- les tests, la simulation et la répétition rejoués ;
- un texte nouveau, et une contre-lecture neuve des parties changées (R2).

Les remarques CLZ-05 à CLZ-11 sont à reprendre au passage.

**Ce qui tient** :

- **Empreintes et commit** : 27 sur 27 ; tête de branche = commit attendu ; stimuli et constructeur identiques à l'octet à ceux de `echelle-v2/`.
- **Tests** : 80 passent, comme la trace.
- **Simulation** : reproduite **à l'octet près** (`8d90b2e7…`) ; 17 cases sur 17 ; mêmes empreintes d'analyse, de simulation et de stimuli, même commit, mêmes versions. Le tableau du texte la transcrit fidèlement.
- **Trace lexicale** : reproduite à l'octet près ; sac de mots 0,5717 ; « how » 4 contre 0 (a), « on » 0 contre 5 (b).
- **Choix d'offre** : sur la trace des 43 offres, l'offre de référence est retenue, avec un pire de 6,6889 USD (le texte : 6,69).
- **Contrôle symétrique**, construit comme cl2 le demandait :
  - mêmes tirages pour les deux modèles et les deux sens (`un_tirage`) ;
  - centrage par moitié et ajustement croisé dans chaque sens ;
  - certification à directions fixes propres à chaque sens (`fixes[s]`) ;
  - témoin sur les paires du jeu d'apprentissage du sens (b pour b→a), orthogonalisé ;
  - tirage des paires conditionné pour les deux jeux, rejets comptés par jeu.
  - Une signature propre au jeu b ne fabrique pas de « positif », puisque le sens a→b décide (banc « sig_b_pos » : « indécis » 3 sur 3, λ_b→a seul gonflé). Voir CLZ-08 pour les deux signatures ensemble.
- **Concordance du texte et du code** :
  - ordre de `lire()`, conditions P(s) et I(s), inégalités strictes ou larges, réserves ;
  - `SEUILS`, `ATTENDUS`, profondeurs, `NUMPY_ATTENDU`, `SANS_INTERVALLE` (CLY-07) ;
  - choix de couche : aire arrondie au millième, puis d', puis la plus basse ; sur le pli S, sens a→b ;
  - graines, rejets, mode décisif, garde de délestage, amorce, surveillance, lanceur (24 h, durée transmise, prix relu) ;
  - liste d'arrêt conforme au code, ligne à ligne, aux manques de test près (CLZ-04).
- **Mode décisif** : `etat_scripts()` réel sur un clone du commit. Arbre propre : vrai ; avec un `__pycache__` : vrai (ignoré) ; avec un fichier non suivi dans `echelle-v3/` ou un script modifié : faux.
- **Amorce** : elle refuse `DUREE_MAX_S` absente, 4 499, 7 201 et « abc », et accepte 4 500 (délai 3 900 s). `timeout` tue bien tout le groupe de processus : essai de 2 s, code 124, aucun processus restant.
- **R3** : aucune issue n'est visée. Aucun « positif » ni « inverse » dans les 28 analyses de la simulation sous H_0, sans fuite et sous signature a, ni dans mes cas sans concept à signature d'un seul jeu (« sig_a_neg », « sig_b_pos »). Limite : CLZ-08.
- **R7** :
  - Nguyen et al. : carte v2, l. 20 et 24 ; Xiong et al. : carte v3, l. 55 et 81 à 84 ; chiffres et pages conformes (voir cependant CLZ-07) ;
  - les citations inchangées depuis le v3 concordent par sondage : carte v1, l. 114, 205, 289, 358 et 359 ; carte v3, l. 14 et 179.
- **R9, R10, R12** :
  - `SeedSequence`, versions et commit consignés par l'analyse et par la simulation ;
  - arrêts par identifiant dans le lanceur et la surveillance ; `timeout` n'agit que sur ses propres processus, jamais par motif ;
  - noms neufs partout : `…_v3`, `analyse-echelle-v3.json`, branche `donnees/echelle-conscience-eval-v3`. Le nom du texte scellé, `test-echelle-conscience-eval-v4.md`, est encore libre dans `prereg/`.

## Traitement des constats de cl2

| constat de cl2 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLY-01 signature du jeu a | bloquant | **partiellement** | Contrôle b→a calculé comme demandé et exigé pour « positif » et « inverse ». Rejoué sur les mêmes activations (signature a de +2 au 8B, aucun concept) : la v2 lit « positif » sans réserve 4 fois sur 4, la v3 « positif non confirmé » 4 fois sur 4 ; λ_a→b(8B) de 0,87 à 0,94, λ_b→a(8B) de −0,38 à 0,06. Simulation : 4 sur 4. Mais le contrôle ne couvre pas « fuite de signe inverse », « pas de fuite » ni « nul » (CLZ-01), et la phrase de « non confirmé » dit plus que la lecture (CLZ-02) |
| CLY-02 biais de ν | à corriger | **traité** | Orthogonalisation l. 291, au point et dans chaque tirage ; test présent et passant. Rejoué, forces de paires inégales (0,5) : ν(8B) de 0,57 à 0,91 en v2, de 0,06 à 0,12 en v3 (b→a : 0,05 à 0,11) ; borne basse de la spécificité de 0,06 à 0,18 en v2, de 0,41 à 0,56 en v3. Banc « HA_kappa » : ν ≤ 0,10, aucune fausse réserve |
| CLY-03 plafond non garanti | à corriger | **partiellement** | (a) surveillance sans `DUREE_MAX_S` : refus, testé. (b) 24 h de stockage comptées ; destruction au plan et à la liste d'arrêt ; au prix de l'offre, le pire tient sous 8 USD par construction (balayage du domaine : 7,88 USD au plus, latence comprise). (c) amorce bornée, refus vérifiés, hypothèse de facturation dite. Mais la tolérance de 5 % du prix relu casse la garantie (CLZ-03), les gardes nouvelles ne sont pas éprouvées (CLZ-04), et la borne de l'amorce court depuis son départ, pas depuis la création (CLZ-05) |
| CLY-04 atteignabilité | à corriger | **traité** | Simulation étendue, scellée, reproduite à l'octet. Phrases réécrites et conformes, sauf « 32 analyses » au lieu de 28 (CLZ-06). tau 1,2 non simulé : la réécriture des phrases suffit |
| CLY-05 sac de mots sans trace | à corriger | **traité** | 0,5717 dans la trace lexicale, reproduite à l'octet |
| CLY-06 intégrité du run | remarque | **traité** | Commit, arbre propre (`.gitignore` des caches), numpy 2.4.6 ; tests par substitution ; `etat_scripts()` réel conforme sur un clone |
| CLY-07 intervalles de λ_a et du transfert | remarque | **traité** | Points seuls (`SANS_INTERVALLE`) |
| CLY-08 saturation de L\* | remarque | **traité** | d' au second rang ; réserve « profondeur ». Celle-ci n'est jamais calculée sur quatre couches dans les essais (CLZ-11) |
| CLY-09 hypothèses et formulation | remarque | **traité** | H_A sur les quatre conditions, dans les deux sens ; « vers son pôle » |
| CLY-10 indices contraires | remarque | **traité** | Cités ; chiffres et pages conformes. La circularité de Xiong et al. est omise (CLZ-07) |
| CLY-11 aires à 1,00 | remarque | **traité** | A_ctx_fixe exclue de R4. Le même raisonnement vaut pour A_conf quand λ est petit (CLZ-09) |
| CLY-12 résidus lexicaux | remarque | **traité** | Garde des lemmes unilatéraux contre les gabarits ; mots courts comptés et cités dans les limites. Le contrôle de `MOTS_ETAT` sur un seul rendu fictif reste tel quel, sans effet selon cl2 |
| CLY-13 contrôles avant le GO | remarque | **traité** | Gabarits et dernier jeton : trace conforme. Elle ne consigne pas les versions, mais celles du venv local sont celles de l'instance (transformers 5.18.0, tokenizers 0.23.2). Garde de délestage. Prix relu, qui ouvre CLZ-03 et CLZ-04 |
| CLY-14 sous-gardes | remarque | **partiellement** | Une sous-garde par test, plafond absent, conditions de « positif » refusées une à une : faits. Le compagnon de script faux sur l'instance n'est toujours pas éprouvé (CLZ-04) |
| CLY-15 détails | remarque | **traité** | Les six points : heure, écarts au v1, versions et commit de la simulation, rejets du sac, conditionnement dans « Intervalles », « / \|Ec\| » |

Bilan : 12 constats traités, 3 partiellement (CLY-01, CLY-03, CLY-14), aucun non traité.

## Constats nouveaux

### CLZ-01 — BLOQUANT — Le contrôle symétrique n'est exigé que pour « positif » et « inverse » : la signature des cadrages a, de signe négatif, fabrique une « fuite de signe inverse » et peut masquer un effet vrai en « nul » ou « pas de fuite »

- **Localisation** :
  - `analyser_echelle_v3.py`, `lire()` : l. 408–409 (fuite de signe inverse, λ a→b seul) et l. 437–442 (pas de fuite, nul, a→b seul) ;
  - brouillon v4 : critères 3, 7 et 8 (l. 191–192 et 201–204) ; H_0 (l. 63) ; « Mesures » (l. 109–110).
- **Constat** :
  - Le texte pose lui-même qu'une poussée du format sur la signature propre aux cadrages a « ne se retrouve pas dans le sens b→a ». Il range dans H_0 « une fuite qui ne se retrouve que dans un sens ». La correction n'applique pourtant le contrôle qu'à « positif » et « inverse ».
  - Le signe de cette poussée est arbitraire. CLY-01 le notait : elle peut aussi « fabriquer un “inverse” ou masquer un effet vrai ». De signe négatif, elle tire λ_a→b vers le bas :
    - sans fuite du concept, elle donne « fuite de signe inverse ». La phrase permise affirme alors que « le gabarit de banc d'essai déplace la lecture vers le pôle “usage réel” », ce qui est faux ;
    - avec une fuite vraie et un écart d'échelle vrai, elle peut ramener λ_a→b(8B) ou Δλ_a→b dans la bande d'équivalence. On lit alors « nul » (« l'écart d'échelle […] est inférieur à δ ») ou « pas de fuite », alors que le sens b→a montre l'écart.
  - Ces trois lectures ne regardent pas le sens b→a, et aucune réserve ne le signale. Un résultat nul ou négatif s'y prononce donc plus facilement qu'un positif, sous le même artefact : c'est l'asymétrie que R4 interdit.
- **Preuve** (`scripts/banc_v4.py`, analyse v3 telle quelle, 300 tirages ; détail en annexe et dans `banc/banc.jsonl`) :
  - **« sig_a_neg »** : signature a de −2 au 8B, soit la norme du cas qui sert au test et à la simulation du v4 avec le signe opposé ; aucun concept ; tau 0,4.
    - Résultat : **« fuite de signe inverse » 4 sur 4**. λ_a→b(8B) va de −0,49 à −0,94 (bornes hautes de −0,25 à −0,65).
    - Dans le sens b→a, λ(8B) vaut [0,33 ; 0,62], [0,27 ; 0,74], [−0,20 ; 0,32] et [0,17 ; 0,54] : aucune fuite négative.
  - **« masque_HA_fort_t015 »** : H_A vraie (λ du concept 1,0 et 0,2), signature a de −2 au 8B, tau 0,15.
    - Résultat : « positif » 3, **« nul » 1**.
    - Dans ce cas, Δλ_a→b vaut [−0,08 ; 0,22] et Δλ_b→a [0,30 ; 0,59].
  - **« masque_pasdefuite_t015 »** : fuite de 0,6 au 8B et de 0 au 70B, signature a de −1,4 au 8B, tau 0,15.
    - Résultat : « positif » 3, **« pas de fuite » 1**.
    - Dans ce cas, λ_a→b(8B) vaut [−0,01 ; 0,19] et λ_b→a(8B) [0,27 ; 0,48].
  - **« masque_HA_fort »**, au tau 0,4 : « indécis » 4 sur 4, alors que Δλ_b→a vaut [0,50 ; 1,16], [1,11 ; 1,88], [1,14 ; 2,01] et [0,37 ; 0,81].
  - Ni la simulation du v4 ni les tests ne contiennent de signature de signe négatif : seul le sens qui gonfle « positif » est éprouvé.
- **Correction** :
  - Lire « fuite de signe inverse », « pas de fuite » et « nul » dans les deux sens, comme « positif » et « inverse ». Par exemple :
    - « fuite de signe inverse » : borne haute de λ_b→a < −δ pour le même modèle, avec la certification b→a ;
    - « pas de fuite » : les quatre intervalles de λ dans [−δ ; δ] ;
    - « nul » : les deux intervalles de Δλ dans [−δ ; δ].
    - Sinon, « … non confirmé (sens b→a) », avec une phrase propre, ou « indécis ».
  - À défaut : une réserve obligatoire et symétrique, « désaccord des deux sens », sur toute lecture prononcée sur a→b seul.
  - Ajouter à la simulation et aux tests une signature de signe négatif, au 8B et au 70B, et un cas de masquage. Réécrire les phrases d'atteignabilité en conséquence : « nul » et « pas de fuite » deviendront plus rares sous H_0, et c'est le prix honnête de la symétrie.

### CLZ-02 — À CORRIGER — « Positif non confirmé (sens b→a) » : la phrase permise affirme une absence que la lecture n'établit pas, et l'impute à la signature

- **Localisation** : brouillon v4, critère 5 (l. 198–199) et son miroir au critère 6 (l. 200) ; `lire()`, l. 429–436.
- **Constat** :
  - L'issue tombe dès que P(b→a) est faux ou que la certification b→a manque. Elle confond trois situations :
    - (i) l'effet est absent dans le sens b→a, ce qui signe la signature des cadrages a ;
    - (ii) l'effet y est, mais la borne basse de Δλ_b→a ne dépasse pas δ : c'est un manque de puissance ;
    - (iii) la direction apprise sur b ne lit pas le contexte sur a : le sens b→a ne dit rien.
  - De plus, λ est relatif à l'effet du contexte sur le jeu **mesuré**. Pour une fuite pure du concept, λ_a→b ≈ α/κ_b et λ_b→a ≈ α/κ_a, où κ est la force du cadrage du jeu. Une différence de force entre les deux jeux suffit donc à séparer les deux sens, sans aucune signature.
  - « L'effet n'apparaît que lorsque la direction est apprise sur le jeu a » est faux en (ii) et en (iii). « Il peut tenir à la signature de ces cadrages » ne nomme qu'une cause sur trois.
- **Preuve** :
  - Dans la simulation du v4 elle-même, case « H1 (1,0 et 0,2) ; tau 0,8 », graine 3072 (rejouée, `banc/details-h1-tau08.txt`) : fuite pure du concept, aucune signature, lue « positif non confirmé ».
    - Sens b→a : Δλ dans [0,195 ; 1,25] ; λ(8B) dans [0,60 ; 1,52] ; λ(70B) dans [0,14 ; 0,53] ; certifications 0,85 et 0,81.
    - Seule manque la borne basse de Δλ_b→a (0,195 ≤ δ) : l'effet « apparaît » bien dans le sens b→a.
  - Banc « HA_kappa » (fuites de 1,0 et 0,1, forces de paires inégales de 0,5), graine 9402 : « positif non confirmé », parce que la certification b→a du 70B vaut 0,517. Il n'y a aucune signature.
- **Correction** :
  - Distinguer « non confirmé : contredit » (par exemple, borne haute de Δλ_b→a ≤ δ, ou de λ_b→a(8B) ≤ δ) de « non confirmé : non concluant » (intervalle large, ou certification b→a manquante). Ou bien écrire une seule phrase qui dit ce que la lecture établit, par exemple :
    - « L'effet n'est confirmé que dans le sens a→b ; dans le sens b→a, [condition manquante]. Il peut tenir à la signature des cadrages a, à une différence de force entre les deux jeux ou au manque de puissance ; ce n'est pas un résultat d'échelle établi. »
  - Rapporter la condition qui manque. Faire de même en miroir pour « inverse non confirmé ».

### CLZ-03 — À CORRIGER — La tolérance de 5 % sur le prix relu laisse la dépense dépasser le plafond « au pire et tout compris »

- **Localisation** :
  - `lancer_echelle_v3.sh`, l. 155–172 ; l. 168 : `float(r) <= 1.05 * o` ;
  - `choisir_offre_v3.py`, l. 51–56 : la durée et le pire sont calculés au prix de l'offre ;
  - brouillon v4, l. 36, 40 et 242.
- **Constat** :
  - La durée plafonnée est calculée pour que le pire tienne sous 8 USD **au prix de l'offre**. Le lanceur accepte ensuite une instance dont le prix relu dépasse l'offre de 5 % au plus. Toute la location, et sans doute le stockage, se paie alors à ce prix.
  - La marge de 0,20 USD sert déjà la latence de la surveillance (environ 0,08 USD selon cl2).
- **Preuve** (`scripts/pire_tolerance.py` : `choisir_offre_v3.evaluer` balayé sur le domaine admis, latence de 80 s comptée ; `sortie-pire-tolerance.txt`) :
  - au prix de l'offre, la dépense réelle maximale vaut 7,88 USD : le plafond tient ;
  - au prix relu plus 5 %, elle atteint **8,27 USD** : offre à 3,50 USD/h, descente nulle, stockage 0,08 USD/h, durée 6 048 s ;
  - sur une offre réelle de la trace `offres-relues-reference-v1.json` (37942441 : 2,9281 USD/h, pire calculé 8,00 USD, durée 7 028 s), elle atteint 8,15 à 8,24 USD.
- **Correction** :
  - calculer la durée plafonnée et le pire au prix majoré de la tolérance (1,05 × dph_total, stockage compris) ;
  - ou n'accepter qu'un prix relu égal à l'offre, à l'arrondi près ;
  - tester les deux bords (voir CLZ-04). Sinon, écrire « au pire ≈ 8,3 USD » et le demander dans le devis.

### CLZ-04 — À CORRIGER — R5 : les gardes d'arrêt nouvelles ne sont pas éprouvées

- **Localisation** : `lancer_echelle_v3.sh`, l. 155–172 ; `amorce_echelle_v3.sh`, l. 21–24 et 42–44 ; `repeter_instance_v3.sh` ; brouillon v4, l. 246, 253 et 290.
- **Constat** :
  - **Prix relu** : c'est une garde nouvelle de la liste d'arrêt, sans cas sain ni artefact. Le texte le dit (« nouvelle et non répétée »), mais R5 est gelée, et le dire ne suffit pas.
    - Après un prix non conforme, l'arrêt de l'instance n'est pas relu ; seul le code 4 demande une vérification à la main. La surveillance, elle, relit l'état et rend 6.
  - **Délai de l'amorce atteint** : il figure à la liste d'arrêt, mais aucun cas ne l'éprouve. `DUREE_MAX_S` hors de [4 500 ; 7 200] non plus : seule « absente » est répétée.
  - CLY-14 demandait un artefact « compagnon de script faux sur l'instance » : il manque toujours à la répétition.
- **Preuve** :
  - `RESUME.txt` compte dix lignes, sans aucun de ces cas ; les tests n'en contiennent pas davantage.
  - À la main, dans mon bac à sable, les refus de l'amorce sont bons : `DUREE_MAX_S` absente, 4 499, 7 201 et « abc » sont refusées, 4 500 est accepté. `timeout` tue bien tout le groupe de processus. Ces essais ne remplacent pas une garde testée dans le dépôt.
- **Correction** :
  - extraire la comparaison du prix dans une fonction testée : prix égal, +4 %, +6 %, illisible ;
  - relire l'état après l'arrêt, et rendre un code distinct si l'arrêt n'est pas relu ;
  - ajouter une variable réservée aux essais qui raccourcit le délai de l'amorce, comme `PAS_S` pour la surveillance, et un cas de répétition : délai atteint, rien de plus n'est poussé, code 124 consigné ;
  - ajouter les cas 4 499 et 7 201, et l'artefact « compagnon de script faux ».

### CLZ-05 — REMARQUE — Ce que la borne de l'amorce et le devis supposent

- Le délai de l'amorce court depuis son départ, pas depuis la création : `CREATION` est pris avant `vastai create` (lanceur, l. 131). Le démarrage du conteneur s'y ajoute.
  - La borne « durée moins 600 s » ne tient que si ce démarrage, plus les 2 min de `--kill-after`, reste sous 600 s, soit environ 8 min de démarrage.
  - Le dire, ou passer l'heure de création à l'instance et y caler le délai.
- Si la session locale meurt, l'arrêt et la destruction attendent la session suivante. Les 24 h de stockage comptées supposent qu'elle vienne dans les 24 h : le dire.
- La remontée des résultats (environ 0,3 Go) n'est pas comptée : c'est négligeable, mais à dire.
- À la durée minimale admise (4 500 s), le délai est de 3 900 s. Au débit minimal du filtre (`inet_down>=700`, en Mb/s), les 141 Go du 70B demandent à eux seuls environ 27 min.
  - Aux offres chères, le risque d'un « 8B seul » payé n'est pas nul. Le dire, ou relever le débit minimal.

### CLZ-06 — REMARQUE — Chiffres et renvois (R6)

- « Sous H_0, sans fuite et sous la signature du jeu a (32 analyses) » (l. 160) : la trace en compte 28 (12 + 12 + 4), et je retrouve 28. Zéro « positif » ou « inverse » : exact.
- « Au pire ≈ 6,69 USD ; attendu ≈ 4 USD » (l. 44) : la trace citée, `offre-reference-v1.txt`, porte 5,2306 et 3,9292 (avec 3 h de stockage).
  - 6,69 se retrouve avec le code v3 sur `offres-relues-reference-v1.json` (6,6889), une trace que le v4 ne cite plus.
  - Pour cette offre, le code v3 estime 5,39 USD, 24 h de stockage comprises, et non 4 : l'« attendu » suppose une destruction rapide. Le dire, et citer une trace qui porte ces nombres.
- Le rapport de construction `stimuli/construction-echelle-v2.json` (`401f75fb…`) n'est plus au tableau des empreintes. Or « aucune question reprise de H-M1 », les lemmes disjoints, la même personne et la même négation en dépendent. Le remettre au tableau.
- Écart 6 : le « 0,98 » n'a pas de source dans les pièces citées. 0,585 vient de cl1 et 0,572 de la trace lexicale.

### CLZ-07 — REMARQUE — Xiong et al. : la circularité manque, et deux pages (R7, R8)

- Les chiffres et les pages cités concordent avec la carte v3 (l. 81–84) : 0,056 → 0,073 ; 14,8 % → 26,4 % ; 15,1 % pour le témoin ; p. 4 et 5 ; figures 4 et 18.
- Mais la carte v3 souligne deux choses que le texte omet :
  - la réécriture est choisie parmi sept pour maximiser la sonde même qui sert de mesure (p. 3) ;
  - le témoin aléatoire n'est pas choisi de la même façon (carte v3, l. 72, 81 et 201).
  - Citer la hausse sans cette réserve en surestime le poids comme indice contraire. Une demi-phrase suffit.
- « Change d'un même geste le format, le style, la personne et la longueur » : la carte v3 le place p. 3 et p. 11 à 13 (l. 15 et 79), et non p. 4 et 5.

### CLZ-08 — REMARQUE — Portée du contrôle symétrique

- « Une fuite du concept, elle, se retrouve dans les deux sens » est juste ; la réciproque ne l'est pas. Une poussée du format alignée sur les signatures **des deux** jeux passe les deux sens.
- Banc « sig_ab_pos » (signatures a et b de +2 au 8B, aucun concept) : **« positif » 4 sur 4**, dont trois avec la réserve « fuite non spécifique » et un sans.
- Le cas suppose une coïncidence : deux particularités indépendantes poussées ensemble par le format. Il suffit de le dire dans les limites.

### CLZ-09 — REMARQUE — R4 : A_conf à 1,00 n'est pas suspect quand λ est petit

- Le long de ĉ, l'écart des cellules en conflit vaut Ec × (1 − λ). Si le contexte sature l'aire (CLY-11) et que λ est proche de 0, A_conf et A_conf_T1 valent 1,00 sans rien de suspect.
- C'est la prédiction même de l'auteur pour le 70B (λ ≈ 0 à 0,3). L'exemple de R4 déclencherait donc audit et réserve sur une issue attendue.
- Le restreindre, par exemple « A_conf à 1,00 avec λ ≥ 0,5 », ou l'écarter comme A_ctx_fixe.

### CLZ-10 — REMARQUE — Phrases, commande et petits écarts du texte

- « Inverse » et « inverse non confirmé » n'ont pas de phrase écrite (« en miroir », l. 200). CLX-15 demandait une phrase par issue : les écrire.
- Étape 5 du plan (l. 179) : `--commit-attendu <commit de ce texte>`. Le commit attendu est celui des outils (`c08a5b21…`), et non celui qui portera le texte scellé. Écrire la valeur.
- « ≈ 1 tirage sur 7 776 » (l. 123) vaut par jeu : avec deux jeux conditionnés, c'est environ 2 sur 7 776.

### CLZ-11 — REMARQUE — Petits manques de tests et de gardes

- La réserve « profondeur » n'est jamais calculée sur quatre couches. Toutes les données synthétiques (tests et simulation) en ont deux, si bien que `len(par_prof) == 4` est faux (l. 548). Seul `lire()` est testé, avec un drapeau fabriqué. Ajouter un test d'intégration à quatre couches.
- `verifier_repartition(None)` passe en silence (mesure, l. 76–77). Avec au moins une carte et `device_map="auto"`, une carte des couches absente devrait arrêter (R5 : aucun repli silencieux).
- La surveillance accepte toute valeur ≤ 7 200 s (l. 19), alors que son en-tête annonce 4 500 à 7 200 et que l'amorce vérifie l'intervalle. Elle ne vérifie pas non plus que la valeur est celle que le lanceur a écrite dans `lancement.txt`.
- La surveillance rend 0 dès que la ligne « AMORCE … fin, code » paraît, que l'amorce ait fini par 0, par 1 ou par le délai (124). Seul le journal porte ce code ; le reprendre dans `arret.txt` ou dans le code de sortie.
- Tests de `lire()` : « positif » a ses conditions refusées une à une ; « inverse » n'en a qu'une (Δλ_b→a). Ajouter les refus en miroir (R4 appliqué aux tests).

## Annexe — banc synthétique (analyse v3 telle quelle, 300 tirages, d = 64)

Générateur : x = contenu + s_f·F + s_c·κ·C + cadrage + bruit, avec F = α·C + F⊥ + signature_a·sig_a + signature_b·sig_b ; |C| = 4 ; les signatures sont normées à |C| et multipliées par le facteur indiqué.

| cas (graines) | vérité (8B ; 70B) | lectures | remarque |
|---|---|---|---|
| rejeu CLY-01 (9500 à 9506) | signature a de +2 au 8B, aucun concept, tau 0,4 | v2 : positif 4, sans réserve ; v3 : positif non confirmé 4 | λ_b→a(8B) de −0,38 à 0,06 |
| rejeu CLY-02 (9500 à 9506) | fuite spécifique (1,0 ; 0,1), forces de paires inégales (0,5), tau 0,15 | v2 et v3 : positif 3, certification asymétrique (grand) 1 | ν(8B) de 0,57–0,91 à 0,06–0,12 |
| sig_a_neg (9100 à 9106) | signature a de −2 au 8B, aucun concept, tau 0,4 | **fuite de signe inverse 4** | CLZ-01 |
| masque_HA (9100 à 9106) | (1,0 ; 0,2) et signature a de −0,9 au 8B, tau 0,4 | positif 3 (dont 1 avec réserve), indécis 1 | — |
| masque_HA_fort (9200 à 9206) | (1,0 ; 0,2) et signature a de −2 au 8B, tau 0,4 | indécis 4 | Δλ_b→a > δ dans les quatre |
| masque_HA_fort_t015 (9300 à 9306) | idem, tau 0,15 | positif 3, **nul 1** | CLZ-01 |
| masque_pasdefuite_t015 (9300 à 9306) | (0,6 ; 0) et signature a de −1,4 au 8B, tau 0,15 | positif 3, **pas de fuite 1** | CLZ-01 |
| sig_ab_pos (9200 à 9206) | signatures a et b de +2 au 8B, aucun concept, tau 0,4 | **positif 4** (3 avec réserve) | CLZ-08 |
| sig_b_pos (9400 à 9404) | signature b de +2 au 8B, aucun concept, tau 0,4 | indécis 3 | λ_b→a(8B) de 0,6 à 1,1 ; a→b propre |
| HA_kappa (9400 à 9404) | (1,0 ; 0,1), forces de paires inégales (0,5), tau 0,4 | positif 1 ; positif non confirmé 1 (certification b→a du 70B : 0,517) ; certification asymétrique (petit) 1 | CLZ-02 ; ν ≤ 0,10 |
| simulation du v4, H1 ; tau 0,8 (3066 à 3072) | (1,0 ; 0,2) | positif 3 ; positif non confirmé 1 (Δλ_b→a [0,195 ; 1,25]) | CLZ-02 |
| reproduction de la simulation du v4 | 68 analyses, mêmes graines | identique à l'octet (`8d90b2e7…`) | 17 cases sur 17 |

- En dimension 64, deux directions indépendantes ne sont pas orthogonales : leur cosinus vaut environ 1/8. D'où des λ_b→a(8B) non nuls sous une signature a pure (de −0,38 à 0,49 aux points).
- Le mécanisme de CLZ-01, la projection de la poussée sur la part de ĉ_a propre au jeu a, ne dépend pas de la dimension.
- Au passage, « certification asymétrique (petit seulement) » est atteinte dans ce banc (HA_kappa, graine 9404), alors que la simulation du v4 ne l'atteint pas.

Pièces, dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v4/` :

- `scripts/` : `verif_empreintes.py`, `banc_v4.py`, `rejouer_cly01_cly02.py`, `details_h1_tau08.py`, `comparer_atteignabilite.py`, `pire_tolerance.py`, `essai_etat_scripts.py` ;
- `banc/` : `banc.jsonl`, `rejeu-cly01-cly02.jsonl`, `details-h1-tau08.txt`, journaux ;
- `reproduction-atteignabilite/` (sortie et `comparaison.txt`), `lexique-reproduit/`, `offres/` ;
- `tests-cl3.txt`, `sortie-verif-empreintes.txt`, `sortie-pire-tolerance.txt`, `sortie-etat-scripts.txt`, `sortie-amorce-essais.txt`.
