# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v9) — cl8

- **Rôle** : sous-agent neuf, huitième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v9, ni les versions précédentes, ni le code, ni les tests, ni les contre-lectures n° 1 à 7.
- **Consigne** : `docs/notes/echelle-conscience-eval/v8/consigne-contre-lecture-cl8.md` (`435b4263a9dc0fd943ac9612a1b083e172c607efce202eec6f98b0837c168717`), conforme à son compagnon ; suivie à la lettre.
- **Heure** (`date -u`) : 27 octobre 2026 ; lecture commencée à 11:38:25 UTC ; rapport achevé à 12:18 UTC.

## Empreintes des pièces lues (sha256)

| pièce | sha256 |
|---|---|
| `prereg/brouillon-test-echelle-conscience-eval-v9.md` (texte relu ; conforme à son compagnon au début, 11:38, et à la fin, 12:12, de ma lecture) | `27026f1a25e2ab2c19d5bdd0a829aef8d2b99ce36c9480c15c4155d18ce7e0f9` |
| `prereg/brouillon-test-echelle-conscience-eval-v8.md` | `a6dcd579d9ff2d16e51412347ba8b6fe291c668f520577f38eed2f0460636717` |
| `prereg/contre-lectures/brouillon-test-echelle-conscience-eval-v8-cl7.md` | `0093def46360e36d96c44e4bfc961a024db8d1069a1a7fdf9a6ca3671a09a8d6` |
| contre-lectures n° 1 à 6 (`…-v2-cl1.md`, `…-v3-cl2.md` à `…-v7-cl6.md`) | `70afa519…`, `9b476cf4…`, `a2f330f0…`, `5728de4c…`, `4ea69784…`, `3d7a60fc…` (conformes à leurs compagnons) |
| les 20 outils du tableau du texte (`echelle-v8/…`) | les 20 empreintes concordent avec le fichier, le compagnon et l'objet du commit `9ccc383…` |
| les 51 traces du tableau « Traces » | toutes conformes au fichier et à leur compagnon |
| les 29 empreintes abrégées du corps du texte | toutes conformes, chacune rapprochée du chemin qui la précède (dont les trois cartes, hors tableau) |
| `src/controle_ia/prereg.py`, `scellement.py`, `.claude/hooks/garde_calcul.py` | `3b2e3ee5…`, `93beeb1c…`, `84512d4a…` (inchangés depuis cl4 à cl7) |
| `registres/go.md` (en-tête et lignes « calcul » lues ; modifié à 10:31 UTC, avant ma lecture ; aucune ligne ne cite `test-echelle-conscience-eval-v9`) | `0d0a198dc868d80ed5ce3d58171157de0283f45ad61d12d3c902db1d371375fa` |
| cartes `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `-v2.md`, `-v3.md` | `134040bd…`, `fe1e93c1…`, `9d03d3b2…` (conformes) |
| générateur de cl7 importé tel quel (`…/v8/contre-lecture-cl7/scripts/banc_cl7.py`) | `856c0aa9897f7faa…` |

## Ce qui a été lu et essayé

- **Code** : arbre de travail `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/wt-echelle-v1/`, branche `outils/echelle-conscience-eval-v8`, tête `9ccc383c02a08e58928368b23471f4c438e06cda` (le commit attendu, daté 10:46:37 UTC) ; arbre propre avant et après mes essais (seuls les `__pycache__` ignorés de `echelle-v7/`, datés de 07:59 à 10:44 UTC, avant ma lecture) ; index inchangé (10:47 UTC) ; tous mes appels git en lecture, avec `GIT_OPTIONAL_LOCKS=0`.
  - Lu en entier : `analyser_echelle_v8.py`, `amorce_echelle_v8.sh`, `surveiller_echelle_v8.sh`, `simuler_atteignabilite_v8.py`, les différences v7 → v8 de chaque test ; lus en partie : le lanceur (gardes, création), `choisir_offre_v8.py` (calcul).
  - Différences v7 → v8, noms de version normalisés : la mesure, le script d'instance, le contrôle du prix, le contrôle du GO, le contrôle lexical, le choix d'offre et le lanceur ne changent que par leurs commentaires ; stimuli et rapport de construction identiques à l'octet à `echelle-v7/` ; l'analyse change par `rapport_Ec`, `rapport_hors_bande`, les deux réserves et le nom du désaccord né de la cohérence ; l'amorce par `delai()` appelée avant et après le clonage ; la surveillance par `timeout -k 5` aux trois appels.
  - Les stimuli n'ont été lus que par Python.
- **Texte** : brouillons v9 et v8 en entier, et leur différence mot à mot (`sorties/diff-v8-v9-mots.txt`) ; cl7 en entier ; constats de cl1 à cl6, CLU-01 de cl6 en entier ; traces nouvelles de `v8/` (exploration de la bande, rejeu du banc de cl7, simulation, tableau, comptes, latence, répétition, lexique, offre de référence, tests) ; passages des cartes cités (contrôle par sondage : 0,644 tableau 15 p. 23 ; 0,491 p. 5 et 12 ; 0,676 p. 10, 21 et 24 ; ii-3 p. 6, 9, 15 et 8 ; « LLaMA-3.1-instruct (8B, 70B) » p. 3 ; Nguyen p. 6 et figure 7 p. 8 ; Xiong 0,056 → 0,073, 14,8 % → 26,4 %, 15,1 %, carte v3 l. 15, 79, 81–84 : conformes).
- **Gardes héritées** : `exiger_prereg_scelle` et `problemes` ; `problemes()` sur le brouillon v9 ne relève que « section vide ou à remplir : Contre-lecture », comme attendu ; `prereg/test-echelle-conscience-eval-v9.md` est absent (nom libre).
- **Essais** (scripts et sorties dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9/`, avec `TMPDIR`, `HF_HOME` et `--basetemp` dedans, `-B`, `PYTHONDONTWRITEBYTECODE=1`, fils de calcul à un, bornes de durée explicites) :
  - tests du commit avec le modèle minuscule local : **401 passed in 498,22 s** (`sorties/tests-cl8.txt`, de 11:39:26 à 11:47:46 UTC ; la trace versée dit 498,57 s) ; collecte : 299, 89, 8 et 5 par fichier ; `test_lire` 109, `test_lire_miroir` 109, `test_texte_des_reserves` 16, `test_go` 11, artefacts d'offre 11 : ceux du tableau R5 ;
  - contrôle de toutes les empreintes citées (`scripts/verif_outils.py`, `verif_traces.py`, `verif_abregees.py`) ;
  - tableau de la simulation reconstruit par un script à moi depuis la sortie scellée, comptes et audit recalculés, 386 analyses communes comparées à la simulation v7 (`verif_tableau.py`, `verif_comptes.py`, `verif_v7_v8.py`) ;
  - **reproduction de 42 des 84 analyses nouvelles de la simulation scellée** avec le script du commit (`reproduire_sim_v8.py`) : 42 sur 42 identiques (lecture, réserves, e(m), son intervalle, rapport des Ec) ;
  - cas fabriqués de cl7 rejoués contre `lire()` v8, avec des intervalles de e(m) et des rapports des Ec choisis (`cas_fabriques_v8.py`) ;
  - **rejeu versé du banc de cl7 vérifié et non cru** (`verifier_rejeu_cl7.py`), et trois analyses du banc refaites par moi (graines 41306, 40006, 43202 ; `refaire_banc_cl7.py`) : identiques au rejeu versé ;
  - **trois bancs nouveaux** (analyse v8 du commit telle quelle, mode répétition, 300 tirages) :
    - banc Q, 60 analyses : rapport des Ec sous une fuite égale (0,7) et un contexte du jeu b × 1 ; 1,15 ; 1,25 ; 1,333 ; 0,75, aux tau 0,15 et 0,4 en dimension 256, 0,4 et 0,8 en dimension 64 (générateur de la simulation scellée importé tel quel ; `banc_cl8.py`) ;
    - banc BDC, 186 analyses : voisins de la classe de cl6 à des amplitudes, dimensions et rapports de contexte que la simulation ne joue pas (même générateur) ;
    - banc Z, 62 analyses, plus une confirmation à 2 000 tirages : générateur de la simulation recopié, plus une composante commune aux cadrages « eval » de toutes les paires d'un seul jeu (`banc_cl8_commun.py`) ; contrôle : sans cette composante, il rend à l'octet les activations de la simulation (2 graines sur 2) ;
  - choix d'offre rejoué sur les 45 offres versées, et dépense réelle au pire avec 105 s de retard.
- **Interdits respectés** : aucun fichier interdit ouvert, lu ou haché (la liste du dossier `prereg/` a montré le nom de `P3-consignes-v1.md` ; il n'a été ni ouvert ni haché) ; aucune recherche récursive dans le dépôt ; aucun réseau ; aucune commande vastai ; aucun lancement ; aucune écriture git ; rien de modifié hors de mon bac à sable (vérifié à 12:12 UTC : brouillon v9 conforme à son compagnon ; aucun fichier de `prereg/` ni de `docs/notes/echelle-conscience-eval/` plus récent que mon départ ; arbre de travail propre, rien de plus récent que mon départ) ; aucune clé ni aucun jeton cherché, affiché ou écrit.

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLS-01** : la réserve « jeux de force de contexte inégale » repose sur le rapport q des Ec des deux sens, que le texte dit estimer k, le rapport des forces de contexte des deux jeux. Or q mêle k et la **pureté** des deux directions apprises : une composante propre aux cadrages d'un seul jeu (une asymétrie lexicale, comme celles que la trace lexicale compte : « how » 4 contre 0 dans a, « on » 0 contre 5 dans b) le fausse dans les deux sens. Sur activations synthétiques :
  - à contextes égaux, q vaut 0,81 à 0,84 (composante dans a) ou 1,19 à 1,26 (dans b) : la réserve se déclenche à tort sur chaque issue prononcée ;
  - sous un contexte du jeu b plus fort de 25 % ou de 40 %, q vaut 0,95 à 1,04 : la réserve se tait ;
  - la famille D de cl7 (fuite égale, contexte d'un jeu plus fort, signatures croisées), que le texte dit signalée, rend alors **« inverse » sous H_0 sans aucune réserve** : 2 fois sur 18, et la lecture tient à 2 000 tirages.
  - Le texte écrit au contraire que seuls « un écart de force de contexte sous 15 % et des signatures assez petites » ne sont signalés par rien.

Corrections à faire avant le scellement :

- CLS-01 (bloquant) : au minimum, le texte (ce que q mesure ; ce que la réserve dit ; la limite ; la phrase R3 ; la justification de 1,15) ; mieux, ajouter ce cas à la simulation. Pistes plus bas.
- CLS-02 et CLS-03 (à corriger) : chiffrer ce qui passe encore sans réserve à petite amplitude ; dire le vrai prix des réserves et le sens d'une issue réservée au regard de H_0.
- CLS-04 et CLS-05 (remarques) : à reprendre au passage.

Sur la question posée par la consigne (une réserve suffit-elle, ou faut-il une garde ?) : **une réserve est recevable** au regard de R3 et de R4, pourvu que le texte dise exactement ce qu'elle voit et ce qu'elle ne voit pas.

- R4 prescrit lui-même la réserve comme réponse au soupçon (« trop beau = réserve ») ; les deux réserves sont mécaniques, sans paramètre tiré des mesures, et appliquées de la même façon à « positif », « inverse » et « nul ».
- Aucune ne permet de viser un signe (R3).
- Une garde ne fermerait pas mieux le reste : sous la composante commune de CLS-01, e(m) est près de zéro et q près de 1, si bien qu'aucune garde fondée sur ces deux grandeurs ne verrait l'artefact. Dans le modèle linéaire de la simulation, les Ec rapportés ne séparent pas k de la pureté sans supposer les deux jeux également purs (annexe A). Seul un troisième jeu de cadrages tenu à part le permettrait, comme pour les doubles signatures.
- Ce qui ne va pas, c'est donc ce que le texte attribue à la réserve, pas le choix de la réserve.

## Ce qui tient

- **Empreintes et commit** : 20 outils sur 20 (fichier, compagnon, objet du commit), 51 traces sur 51, 29 empreintes abrégées sur 29 ; tête de branche = commit attendu ; arbre propre ; nom scellé libre ; `problemes()` ne relève que la section « Contre-lecture ».
- **Tests** : 401 passent chez moi en 498,2 s ; les décomptes du tableau R5 concordent avec la collecte.
- **Concordance du texte et du code**, pour les parties changées :
  - « λ change d'un sens à l'autre » : `b > 0 or h < 0` sur l'intervalle de e(m), exclusion stricte, zéro compris dans l'intervalle = pas de réserve (l. 607–610), comme le tableau « Seuil » et les tests (bornes 0 et 0,001) ;
  - « jeux de force de contexte inégale » : `max(q, 1/q) > 1,15`, inégalité stricte, symétrique en logarithme (à q = 1/1,15 exactement, `1/q` vaut 1,15 en virgule flottante : pas de réserve, comme à 1,15) ; q non défini si un Ec ≤ 0 (l. 585–587, 611–614, 761–765) ;
  - les deux réserves ne visent que « positif », « inverse » et « nul » ; ni la fuite de signe inverse, ni « pas de fuite », ni une issue non confirmée, ni un désaccord ne les portent (tests, et mes cas fabriqués) ;
  - « désaccord des deux sens (cohérence) » si une issue au moins est tenue dans les deux sens sans la cohérence, sinon « désaccord des deux sens » (l. 647) ;
  - le reste de la lecture (cinq étapes, inégalités, cohérence, combinaison, réserves anciennes, mode décisif, `SEUILS` hors la borne nouvelle, commandes, liste d'arrêt) est inchangé depuis la v7, que cl7 a trouvée conforme ligne à ligne.
- **Cas fabriqués de cl7, rejoués contre `lire()` v8** (`sorties/sortie-cas-fabriques-v8.txt`) : « positif », « inverse » et « nul », avec un intervalle de e(m) de ± 0,10, portent chacun les deux réserves « λ change ». Mais voir CLS-02 : avec un intervalle de ± 0,21, que le bootstrap donne couramment au tau 0,4, « positif » et « inverse » n'en portent aucune.
- **Rejeu du banc de cl7, vérifié** (`sorties/sortie-verifier-rejeu-cl7.txt`) :
  - les 162 lignes rejouées sont celles du banc (même scénario, même graine, même lecture v7) ;
  - intervalles de λ et e(m) identiques (écart maximal 0,0) ; 30 lectures changent, de nom seulement ;
  - les 19 lectures fausses du banc principal (« positif » 9, « inverse » 6, « nul » 4) portent toutes au moins une réserve v8 (« λ change » 18, « contexte inégal » 5), les 4 à 2 000 tirages aussi ;
  - mes trois analyses refaites sont identiques au rejeu versé.
- **Simulation** :
  - tableau du texte (69 lignes) identique à ma reconstruction depuis la sortie scellée ;
  - comptes et audit exacts : 22 noms sur 27 ; R3 : 36, 42 (dont 30 nouvelles), 32, 24, 144 et 6 analyses ; 11 lectures fausses de la classe voisine, toutes réservées (« λ change » 10, « contexte inégal » 3) ; 3 fausses alertes sur 51 (rapports 1,178 et 1,23, aux tau 0,4 et 0,8) ; 30 réserves ajoutées aux analyses communes, dont le détail du texte est exact ;
  - les 386 analyses communes avec la v7 lisent la même issue (64 renommées seulement), e(m) identiques ;
  - 42 analyses nouvelles reproduites à l'identique.
- **CLT-02** : seuils de perte de « nul » exacts (k < λ/(λ + δ) ou k > λ/(λ − δ) : 0,67 et 2 ; 0,74 et 1,56 ; 0,8 et 1,33) ; comptes de la simulation exacts ; « pas de fuite » n'y perd rien.
- **CLT-03** : `delai()` est appelée avant et après le clonage, et le calcul part du délai recalculé (l. 50–59, 81–84 de l'amorce) ; le calcul finit au plus tard à création + durée − 600 s + 2 min, soit 480 s avant le plafond. La répétition l'éprouve : ligne « délai recalculé après le clonage » dans le cas sain ; refus après un clonage lent ; ligne de fin ; rien de poussé (`RESUME.txt`, 35 lignes conformes).
- **CLT-04** : `timeout -k 5 "$APPEL_S"` aux trois appels de la surveillance (l. 67, 82, 96). Au pire, l'arrêt est demandé deux appels de 35 s après le plafond, et l'appel d'arrêt dure au plus 35 s : 105 s. Le test « outil sourd » passe ; l'essai versé (g) donne 68,4 s.
- **Dépense** :
  - le calcul du choix d'offre est inchangé (seuls les commentaires changent) ;
  - offre de référence rejouée sur les 45 offres versées : 50510069, 7 200 s, pire 7,0311 USD, comme la trace ;
  - à la pire offre admise (3,50 USD/h majoré de 5 %), la dépense réelle avec 105 s de retard vaut 7,907 USD, sous 8 ; la marge couvre 195,9 s ;
  - les hypothèses non gardées sont dites : facturation d'une instance sortie, session morte, prix absent, arrêt effectif en quelques secondes. Le conteneur sort à la fin de l'amorce (`--entrypoint bash … bash /root/amorce.sh`), ce qui rend la borne de l'amorce effective.
- **R7, R9, R10, R12** :
  - citations inchangées et conformes par sondage ;
  - `SeedSequence(4429003211691042563)` inchangée ;
  - commit et versions consignés par l'analyse et la simulation ;
  - arrêts par identifiant ;
  - noms neufs (`…_v8`, `analyse-echelle-v8.json`, texte scellé `…-v9.md`).

## Traitement des constats de cl7

| constat de cl7 | gravité | état | preuve ou réserve |
|---|---|---|---|
| CLT-01 la cohérence ne ferme la classe de cl6 qu'en son centre | bloquant | **partiellement traité** | Les familles B, C et D de cl7, aux amplitudes de cl7 et de la simulation, portent toutes une réserve : rejeu vérifié (19 sur 19), simulation (11 sur 11), et mon banc (19 des 21 « positif » et « inverse » des familles B). Restent deux trous : à petite amplitude, des issues fausses passent sans réserve (CLS-02) ; et la réserve « contexte inégal » se fausse ou se tait sous une composante propre à un jeu, si bien que la famille D passe sans réserve à un contexte plus fort de 40 % (CLS-01). Le texte et la formule de e(m) sont justes ; la limite et la phrase R3 disent trop (CLS-01, CLS-02) |
| CLT-02 prix sous H_0 chiffré au seul réglage sans coût | à corriger | **traité** | Cinq cas H_0 à contextes inégaux ajoutés (30 analyses), formule et seuils écrits dans les limites, comptes vérifiés ; « pas de fuite » n'y perd rien |
| CLT-03 délai compté avant le clonage | remarque | **traité** | Code, répétition (cas sain, clonage lent) ; texte l. 64, 70, 300, 445 conforme |
| CLT-04 appels sans KILL | remarque | **traité** | Code, test, essai (g) ; borne de 105 s écrite ; dépense réelle au pire 7,907 USD |
| CLT-05 phrases et détails | remarque | **traité, deux restes mineurs** | Désaccord nommé à part, avec sa phrase ; cas de cl4 sous la cohérence ; raison de « pas de fuite » ; `ATTENTE_ARRET_S` dit, cas (h) ; code non commité dit. Restes : la phrase du désaccord dit « lisent » au lieu de « tiennent » ; la branche d'outils n'a toujours aucune référence distante dans ce clone (CLS-05) |

Bilan : 5 constats traités, dont CLT-01 en partie seulement.

## Constats nouveaux

### CLS-01 — BLOQUANT — Le rapport des Ec n'estime pas la force relative des contextes : une composante propre aux cadrages d'un jeu le fausse dans les deux sens, et la famille D de cl7 rend alors « inverse » sous H_0 sans aucune réserve

- **Localisation** :
  - `analyser_echelle_v8.py` : l. 39–40 (« il estime k ») ; l. 761–765 (q = Ec_a→b / Ec_b→a) ; l. 585–587 et 611–614 (réserve) ; l. 572–573 (texte de la réserve : « jeux de force de contexte inégale … »).
  - Brouillon v9 :
    - l. 8 ; l. 143–145 (« il estime k ») ; l. 176 ; l. 185 (« Pourquoi 1,15 ») ;
    - l. 271 (R3 : « « jeux de force de contexte inégale » 3 fois (les 3 à contextes inégaux) ») ;
    - l. 349 (la réserve « dit que λ et la cohérence ne se comparent plus ») ;
    - l. 405 (limite : « un écart de force de contexte sous 15 % et des signatures assez petites … ne sont signalés par rien ») ;
    - l. 408 (« le rapport des Ec des deux sens … l'estime ») ;
    - l. 520 (traitement de CLT-01).
- **Constat** :
  - Dans le modèle linéaire de la simulation, notons u le contexte commun (le concept), s_a et s_b la part du contraste « eval − reel » propre aux cadrages de chaque jeu, et k la force du contexte du jeu b relativement à celle du jeu a. La direction apprise sur a est ĉ_a ∝ u + s_a. Il vient :
    - Ec_a→b = k|u|²/|u + s_a| et Ec_b→a = k|u|²/|k·u + s_b| ;
    - d'où **q = |k·u + s_b| / |u + s_a|**, alors que λ ne dépend pas de s (il s'y simplifie) : λ_a→b = α/k, λ_b→a = α, et e(m) = α(1/k − 1).
  - q ne vaut donc k que si les deux directions apprises sont également pures. Le « tirage vers 1 » que le texte constate (l. 145, 185) en est un effet ; il dépend de l'hétérogénéité des cadrages, et la bande 1,15 a été réglée au seul tau 0,15 en dimension 256, trois graines par réglage, où cette pureté est presque égale entre les jeux.
  - Une **composante commune aux cadrages d'un seul jeu** rend les puretés inégales sans ajouter de bruit au bootstrap des paires. Par exemple, un mot ou un tour présent dans les cadrages « eval » de presque toutes les paires d'un jeu et absent de l'autre. C'est le cas que la trace lexicale du texte compte : « how » 4 contre 0 dans a, « on » 0 contre 5 dans b (l. 127). Alors :
    - à k = 1, q s'écarte de 1 : **fausse alerte** sur chaque issue prononcée, avec une phrase qui affirme à tort des « jeux de force de contexte inégale » ;
    - à k ≠ 1, q peut revenir près de 1 : **silence**, et le terme α(1/k − 1) de e(m) reste entier.
  - La famille D de cl7 exploite précisément ce terme : sous une fuite égale, il compense l'écart que créent des signatures croisées, si bien que e(m) reste près de zéro (pas de réserve « λ change ») ; seule la réserve « contexte inégal » la voyait dans la graine 41306 de cl7, et surtout elle dans la graine 1012 des tests. Dès que q est ramené dans la bande, rien ne la voit plus.
  - Le texte présente ce cas comme signalé (R3, l. 271 ; limite, l. 405), et ne concède que les écarts de contexte « sous 15 % » avec des signatures « assez petites ». Ce n'est pas le bruit qui cache ici l'artefact, mais un biais de q.
- **Preuve** (banc Z : `scripts/banc_cl8_commun.py`, `sorties/banc-cl8-Z.jsonl`, `banc-cl8-Z2.jsonl`, `banc-cl8-Z-n2000.jsonl`, résumés `sorties/resume-banc-cl8-Z*.txt`) :
  - Réglage commun : générateur de la simulation recopié, identique à l'octet sans la composante (contrôle, 2 sur 2) ; dimension 256, tau 0,15, 300 tirages ; composante commune de norme 3 ou 4, celle du contexte valant 4.
  - Rapport des Ec, fuite égale (H_0) :

    | réglage | q (petit / grand), par analyse | réserve « contexte inégal » |
    |---|---|---|
    | contextes égaux, composante dans a (norme 3) | 0,82/0,82 ; 0,84/0,82 ; 0,82/0,83 ; 0,82/0,81 | sur les 3 « nul » prononcés : **fausse alerte 3 fois sur 3** |
    | contextes égaux, composante dans b (norme 3) | 1,21/1,20 ; 1,19/1,23 ; 1,21/1,19 ; 1,26/1,20 | « nul » 4 : **fausse alerte 4 fois sur 4** |
    | contexte du jeu b × 1,25, composante dans a (norme 3) | 1,00/0,98 ; 0,99/0,99 ; 0,99/1,04 ; 0,97/0,96 | « nul » 4 : **aucune** (seule « λ change », e de −0,11 à −0,17) |
    | contexte du jeu b × 1,4, fuite 1,0, composante dans a (norme 4) | 1,02/0,95 ; 0,97/0,97 ; 1,03/1,04 ; 0,99/1,02 | aucune (lu « désaccord (cohérence) », e de −0,24 à −0,41) |

  - **Famille D sous la composante** : H_0, fuite égale 1,0 et 1,0 ; contexte du jeu b × 1,4 ; composante dans a, norme 4 ; signature du jeu b −1,6 au petit, du jeu a +0,55 au grand. Sur 18 analyses : « inverse » 6, dont **2 sans aucune réserve** (graines 145008 et 145118) et 4 avec « λ change » ; indécis 7 ; non confirmés 4 ; désaccord 1. Le rapport des Ec y reste de 0,95 à 1,05.
  - **Graine 145008 à 2 000 tirages** (taille du bootstrap décisif) : « inverse », **aucune réserve** ; la réserve « fuite non spécifique » ne se déclenche pas non plus.

    | grandeur | a→b | b→a |
    |---|---|---|
    | λ (petit ; grand) | 0,55 ; 1,12 | 0,58 ; 1,01 |
    | intervalle de Δλ | [−0,75 ; −0,40] | [−0,59 ; −0,29] |
    | intervalle de la spécificité | [−0,78 ; −0,28] | [−0,65 ; −0,22] |
    | certification (borne basse, petit / grand, à 300 tirages) | 0,964 / 0,946 | 0,955 / 0,941 |

    - Cohérence tenue : e(petit) = −0,025 [−0,152 ; 0,112] et e(grand) = 0,105 [−0,022 ; 0,241] ;
    - q = 0,998 [0,905 ; 1,099] et 1,014 [0,911 ; 1,121].
  - Le miroir (« positif ») sur 18 analyses rend « positif » 4 fois, toutes avec « λ change » : rien n'y fabrique de « positif » sans réserve à ces graines, mais la construction est symétrique en signe.
  - Avec le générateur scellé lui-même (banc Q, 60 analyses, `sorties/resume-banc-cl8-Q.txt`, `sortie-Q-bande.txt`), l'hétérogénéité des cadrages brouille déjà q :
    - au tau 0,8 en dimension 64, à contextes égaux, les 3 analyses ont un modèle hors bande (q 0,80 à 1,10) ; dans la simulation scellée, au même réglage, 8 des 24 valeurs de q à contextes égaux sont hors bande (`sorties/sortie-largeurs-simulation.txt`) ;
    - au tau 0,4 en dimension 256, sous × 1,333, 1 analyse sur 3 n'a aucun modèle hors bande (1,11/1,08).
  - Annexe A : dans ce modèle, Ec_a→b × Ec_app,a→b = Ec_b→a × Ec_app,b→a = k|u|², quels que soient s_a et s_b. Les Ec rapportés, rapport de transfert compris, ne séparent donc pas k de la pureté sans supposer les deux jeux également purs.
- **Correction** :
  - **Au minimum, le texte** (scellable sans nouveau commit) :
    - l. 143–145, 408 : q estime k **seulement si les deux directions apprises ont la même pureté** ; une composante propre aux cadrages d'un jeu (asymétrie lexicale, trace l. 127) le biaise dans un sens ou dans l'autre ;
    - l. 185 : la bande 1,15 a été réglée au tau 0,15, en dimension 256, sur trois graines par réglage, où cette pureté est égale ; elle ne garantit rien ailleurs ;
    - l. 349 : la réserve dit que **le rapport des Ec des deux sens sort de la bande** (force du contexte, ou composition des deux jeux, inégale), et non que les jeux ont une force de contexte inégale ; le texte du code, s'il n'est pas changé, se lit ainsi (à écrire) ;
    - l. 405 : la classe voisine peut passer **sans aucune réserve** même sous un écart de contexte de 25 à 40 %, quand une composante propre à un jeu ramène q près de 1 ; chiffres ci-dessus ;
    - l. 271 : borner la phrase R3 au générateur de la simulation ;
    - l. 184 : la fausse alerte de « contexte inégal » n'est pas rare sous de tels jeux.
  - **Mieux** : ajouter ce cas à la simulation (une composante commune d'un jeu, à k = 1 et à k ≠ 1, avec et sans signatures croisées) et en rapporter les lectures ; ou verser mon banc comme trace. Une garde ne fermerait pas ce trou (e(m) et q sont tous deux près de leur valeur neutre) : seul un troisième jeu tenu à part le permettrait. Si le texte de la réserve change dans le code : noms, commit, tests nouveaux (R12).
  - Dans tous les cas : texte nouveau et contre-lecture neuve des parties changées (R2).

### CLS-02 — À CORRIGER — À petite amplitude, des voisins de la classe de cl6 fabriquent encore « positif » et « inverse » sans aucune réserve ; la phrase R3 dit trop

- **Localisation** : brouillon v9, l. 270–272 (R3 : « seules les doubles signatures chez un même modèle fabriquent encore « positif » ou « inverse » sans réserve de la v8 ») ; l. 405 (« à des amplitudes que le bruit cache ») ; l. 183–184.
- **Constat** :
  - La réserve « λ change » ne voit e(m) que si son intervalle exclut zéro. Or cet intervalle est large : demi-largeur médiane 0,14 au tau 0,15 en dimension 256, 0,21 au tau 0,4 en dimension 64, 0,36 au tau 0,4 en dimension 256, dans la simulation scellée (`sorties/sortie-largeurs-simulation.txt`).
  - Des signatures croisées assez petites pour garder e(m) sous cette demi-largeur, mais assez grandes pour pousser un écart vrai proche de δ au-delà du seuil dans les deux sens, passent sans réserve.
  - Le texte le concède en termes généraux (l. 405), mais sa phrase R3 (l. 272) se lit comme générale, et la simulation ne joue que des amplitudes où la réserve se déclenche (± 0,55 et ± 0,6 en dimension 256).
  - Les cas fabriqués le montrent aussi : ceux de cl7, avec un intervalle de e(m) de ± 0,21, rendent « positif » et « inverse » sans aucune réserve (`sorties/sortie-cas-fabriques-v8.txt`).
- **Preuve** (banc BDC, générateur scellé, `sorties/banc-cl8-BDC.jsonl`, `sorties/sortie-banc-cl8-BDC-sans-reserve.txt`) :
  - Familles B, 15 cas et 90 analyses, dimension 64 et 256 : 21 « positif » ou « inverse » prononcés sous H_0, 19 avec « λ change », **2 sans aucune réserve** :
    - graine 81002 : H_0, λ 0,6 et 0,4, jeu a +0,3 au 8B, jeu b −0,3 au 70B (chacune ≈ 0,1 en λ), dimension 256 ; « positif » ; Δλ [0,26 ; 0,54] et [0,27 ; 0,49] ; e = 0,070 [−0,072 ; 0,216] et 0,068 [−0,034 ; 0,170] ; q 1,03 et 1,03 ;
    - graine 102000 : H_0, λ 0,4 et 0,64, jeu a −0,4 au 8B, jeu b +0,4 au 70B ; « inverse » ; e = −0,096 [−0,208 ; 0,021] et −0,131 [−0,305 ; 0,015].
  - Témoins sans signature au même écart vrai (simulation et cl7) : aucun « positif » sur 10.
  - Les familles D au tau 0,4 et 0,8, et à k = 1,12, ne prononcent rien (84 analyses, indécis ou non confirmés) ; la famille C en dimension 64 non plus (12 analyses).
- **Correction** : borner la phrase R3 à ce qui est simulé ; dans la limite, chiffrer le reste (ces deux cas, et la demi-largeur de l'intervalle de e(m) selon le réglage) et dire qu'un écart vrai juste sous δ, poussé par des signatures d'environ 0,1 en λ chacune, peut être lu « positif » ou « inverse » sans réserve. Ajouter à la simulation au moins une amplitude où la réserve ne se déclenche pas (± 0,3 en dimension 256).

### CLS-03 — À CORRIGER — Le prix des réserves n'est compté que sous des vérités sans signature ; une issue réservée ne sépare pas H_A de la part de H_0 que le texte nomme

- **Localisation** : brouillon v9, l. 94 (H_0 : « ou chez des modèles différents d'un sens à l'autre, en tout ou en partie ») ; l. 184 (« une réserve ne coûte qu'une phrase de plus quand elle se déclenche à tort ») ; l. 276 (« prix des réserves ») ; l. 366 (phrase de « positif ») ; l. 348.
- **Constat** :
  - La réserve « λ change » se déclenche à juste titre dès qu'une signature d'un seul jeu touche un modèle, **y compris sous H_A**. Dans la simulation, les 3 « positif » vrais prononcés sous H_A avec une telle signature la portent tous (« H_A, jeu a −1 au 8B, dimension 256 » : 1 sur 1 ; « fuite masquée » : 2 sur 2). Or la trace lexicale compte des asymétries propres à chaque jeu : des signatures sont plausibles dans les données réelles. Une issue prononcée réelle portera donc probablement la réserve, sous H_A comme sous la classe voisine, et elle ne les distingue pas.
  - Le prix de la réserve n'est donc pas « une phrase de plus » : sous des signatures réalistes, il est la perte du pouvoir de trancher entre H_A et cette part de H_0. Le texte ne chiffre que les fausses alertes sous des vérités sans signature et à contextes égaux (3 sur 51), et ne dit pas non plus le taux de fausse alerte de « contexte inégal » sous des cadrages hétérogènes (tau 0,8, dimension 64 : 8 valeurs de q sur 24 hors bande dans la simulation scellée ; voir aussi CLS-01).
  - H_0 inclut « chez des modèles différents d'un sens à l'autre, en tout ou en partie » (l. 94), alors que « positif » est prononcé avec une réserve qui dit exactement que cela peut tenir « en partie » (l. 348). La phrase de « positif » (l. 366) reste celle d'un effet établi.
- **Correction** :
  - écrire le prix des réserves sous H_A avec une signature d'un seul jeu (3 sur 3 dans la simulation), et la fausse alerte de « contexte inégal » selon l'hétérogénéité ;
  - accorder H_0 et la lecture : soit H_0 dit « en partie, au-delà de δ pour un modèle » (ce que la cohérence borne), soit le texte écrit qu'une issue qui porte la réserve « λ change » n'écarte pas cette part de H_0, et la phrase de l'issue le dit avec elle.

### CLS-04 — REMARQUE — Une affirmation non chiffrée justifie le choix de la réserve

- **Localisation** : brouillon v9, l. 184 (« une marge sur Δλ, envisagée par cl7, demanderait une simulation de plus et perdrait les H_A faibles »).
- **Constat** : la perte sous les H_A faibles n'est ni simulée ni sourcée ; cl7 la donnait comme « à simuler ». Le choix de la réserve se défend sans elle (voir le verdict : une garde ne fermerait pas le trou de CLS-01) ; tel quel, c'est un chiffre de fait sans trace (R6).
- **Correction** : écrire « coûterait sans doute sous les H_A faibles (non simulé) », ou retirer l'argument.

### CLS-05 — REMARQUE — Petits écarts du texte

- **Rejeu du banc de cl7** (l. 284) : « seules les 2 « nul » sous un contexte × 0,8 portent une réserve de la v8 (« contexte inégal », à juste titre) ». Les deux portent aussi « λ change » pour les deux modèles (graines 43202 et 43206 ; mon analyse refaite de 43202 le confirme). Écrire « les deux réserves ».
- **Phrase du désaccord (cohérence)** (l. 373) : « Les deux sens lisent X ». Quand un sens tient aussi une issue d'une étape antérieure (cas tenu {fuite de signe inverse (petit), nul} contre {nul}, testé), sa lecture rapportée est cette autre issue. Écrire « Les deux sens tiennent X ».
- **Branche d'outils** : `outils/echelle-conscience-eval-v8` n'a, dans ce clone, aucune référence distante (comme la v7 relevée par cl7). Le lanceur refuse sans dépense si la tête distante n'est pas le commit : la pousser avant le GO, comme le texte le dit.

## Annexe A — ce que mesure le rapport des Ec

Modèle de la simulation : contraste « eval − reel » du jeu a = u + s_a ; du jeu b = k·u + s_b ; s_a et s_b orthogonaux à u et entre eux ; poussée du format le long du concept = α·u ; on néglige le bruit.

- ĉ_a = (u + s_a)/|u + s_a| ; ĉ_b = (k·u + s_b)/|k·u + s_b|.
- Ec_a→b = ĉ_a·(k·u + s_b) = k|u|²/|u + s_a| ; Ec_b→a = ĉ_b·(u + s_a) = k|u|²/|k·u + s_b|.
- Ef_a→b = α|u|²/|u + s_a| ; Ef_b→a = α·k|u|²/|k·u + s_b|. D'où λ_a→b = α/k et λ_b→a = α.
- q = Ec_a→b / Ec_b→a = |k·u + s_b| / |u + s_a| = √((k²|u|² + |s_b|²)/(|u|² + |s_a|²)).
- Sur le jeu d'apprentissage : Ec_app,a→b = |u + s_a| et Ec_app,b→a = |k·u + s_b|. D'où Ec_a→b × Ec_app,a→b = Ec_b→a × Ec_app,b→a = k|u|², sans information sur k.
- À s_a = s_b = s : q = √((k² + r)/(1 + r)), avec r = |s|²/|u|². La réserve se déclenche (q > 1,15) dès que k > √(1,3225 + 0,3225·r) : 1,17 à r = 0,12 (tau 0,15, dimension 256, le réglage de l'essai), 1,26 à r = 0,85, 1,40 à r = 2.

## Annexe B — pièces de cl8

Dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lecture-echelle-v9/` :

- `scripts/` (sha256) :
  - `banc_cl8.py` `06a9c43e…`, `banc_cl8_commun.py` `20835d6e…`, `confirmer_n2000.py` `d00467a2…` ;
  - `cas_fabriques_v8.py` `76fdb9d4…`, `refaire_banc_cl7.py` `fada15cc…`, `reproduire_sim_v8.py` `063c3575…`, `verifier_rejeu_cl7.py` `e9752684…` ;
  - `verif_outils.py`, `verif_traces.py`, `verif_abregees.py`, `verif_tableau.py`, `verif_comptes.py`, `verif_v7_v8.py`, `largeurs.py`, `resumer_banc_cl8.py`.
- `sorties/` (sha256) :
  - tests : `tests-cl8.txt` `392686d2…` et ses heures ;
  - bancs : `banc-cl8-Q.jsonl` `25474156…`, `banc-cl8-BDC.jsonl` `bdeed2af…`, `banc-cl8-Z.jsonl` `a0b9a67b…`, `banc-cl8-Z2.jsonl` `29e8e777…`, `banc-cl8-Z-n2000.jsonl` `98553074…`, leurs heures et résumés ;
  - reproduction de la simulation : `sortie-reproduire-sim-v8.txt` `dd4d4d1a…`, `sortie-reproduire-sim-v8-suite.txt` `208827c7…` ;
  - cas fabriqués et banc de cl7 : `sortie-cas-fabriques-v8.txt` `21a200a6…`, `sortie-verifier-rejeu-cl7.txt` `8021ac53…`, `sortie-refaire-banc-cl7.txt` `1f2fa8fa…` ;
  - vérifications des empreintes, du tableau et des comptes : `sortie-verif-*.txt`, `sortie-largeurs-simulation.txt`, `sortie-Q-bande.txt` ;
  - différence du texte : `diff-v8-v9-mots.txt`.
- `offres/` : choix d'offre rejoué (offre, journal, offres relues).
