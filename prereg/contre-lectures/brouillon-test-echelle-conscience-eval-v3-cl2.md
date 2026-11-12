# Contre-lecture R2 du préenregistrement « fuite du format et échelle, Llama-3.1 8B contre 70B » (brouillon v3) — cl2

- **Rôle** : sous-agent neuf, deuxième contre-lecteur au sens de R2. Je n'ai écrit ni le brouillon v3, ni le texte v2, ni le code, ni les tests, ni la contre-lecture n° 1 (cl1).
- **Date** : 27 octobre 2026. Lecture commencée à 00:18:26 UTC, rapport écrit à partir de 00:48:07 UTC (`date -u`).
- **Empreintes (sha256)** :

  | pièce | sha256 |
  |---|---|
  | `prereg/brouillon-test-echelle-conscience-eval-v3.md` (texte relu ; conforme à son compagnon, inchangé entre le début et la fin de ma lecture) | `62221ab3865c0e33a3c59e41f66695206815bce4fa8dd2a031097c4b42f81667` |
  | `echelle-v2/scripts/analyser_echelle_v2.py` (conforme au tableau du texte et à son compagnon) | `d8534a94cd7dc920fcde22514a55fa8ade5fbe9f99356ee98340848b9abae746` |
  | `prereg/test-echelle-conscience-eval-v2.md` | `67ad73b5e403d3b9d8bc9bb14c4d31c73d08956b782a84f9cdf388cc49fde90f` |
  | `prereg/contre-lectures/test-echelle-conscience-eval-v2-cl1.md` | `70afa51997f66f882f79686765c9b1fdded6f0016007b626355b975abd9e673a` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md` | `134040bd9a126dce4592aa3b357375f0209f987610d3be21a6848f647eaf59b4` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v2.md` | `fe1e93c1efe7c9117c9f0b22711912394c5b40d0180b904bf61e324cf0943d3a` |
  | `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v3.md` | `9d03d3b212ca43d3eb905413f95f808ef2bc90376b284804a9ed1dbd28ddc3de` |

- **Code relu** dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/wt-echelle-v1/` :
  - branche `outils/echelle-conscience-eval-v2`, tête `495b8bd5bd5d888088324c8a787760a3685baa2c` (le commit attendu ; la branche de suivi locale pointe au même endroit), arbre propre avant mes essais ;
  - les 17 empreintes du tableau d'outils concordent avec les fichiers et avec leurs compagnons `.sha256`, et les 8 empreintes du tableau « Traces » aussi : vérifiées une à une par script (`scripts/verif_empreintes.py`) ;
  - la v1 (`echelle-v1/`) a servi à vérifier le traitement des constats de cl1.
- **Lu en entier** : le brouillon v3, cl1, le texte v2, les onze fichiers de `scripts/`, les quatre fichiers de tests, `construction-echelle-v2.json`, les traces citées (accès ; offre de référence ; offres relues, 43 offres, par extraits : `dph_total` − `dph_base` = `storage_total_cost` pour chacune ; répétition de l'instance : résumé, journaux, empreintes ; sortie des tests ; atteignabilité), et les passages des cartes v1 à v3 que le texte cite. `echelle-v2.json` seulement par extraits en Python.
- **Interdits respectés** :
  - aucun fichier interdit ouvert ni haché ; aucune recherche récursive dans le dépôt ;
  - aucun réseau, aucune commande vastai, aucun lancement, aucune poussée, aucun commit, rien de modifié ;
  - non lus, car hors de ma liste : `.claude/hooks/garde_calcul.py` et `src/controle_ia/prereg.py` (gardes du lanceur que le texte dit héritées de H-M1 v3), et le brouillon v1 (les écarts sont vérifiés contre le v2 seulement).
- **Essais** (scripts jetables et sorties dans `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/contre-lecture-echelle-v3/`) :
  - tests du commit : `60 passed in 130.30s`, avec le modèle minuscule local (`tests-cl2.txt`) ;
  - `scripts/banc.py` appelle `analyser_echelle_v2.py` **tel quel** (mode `--repetition`, 300 tirages au lieu de 2 000) sur des activations synthétiques à vérité connue (d = 64). Environ 140 analyses, détail en annexe, plus les 96 de la reproduction ;
  - reproduction de la simulation d'atteignabilité avec le script scellé et ses graines (`reproduction-atteignabilite/`) ;
  - vérifications sur les textes, sans modèle : sac de mots, longueurs, lemmes, mots courts (`scripts/verif_stimuli.py`) ;
  - les `__pycache__` que mes essais ont créés dans l'arbre relu sont retirés.

## Verdict

**Scellable après corrections.** Un défaut bloque le scellement en l'état :

- **CLY-01** : λ mesure la poussée du format le long de ĉ entier, y compris la part de ĉ propre aux cadrages du jeu a, qui ne passe pas aux paraphrases b. Le témoin ν est aveugle à cette part en espérance, par construction, et la décomposition ne la distingue pas. Une fuite non spécifique y fabrique un « positif » sans réserve : 5 sur 5 dans le banc.

Corrections à faire avant le scellement :

- CLY-01 (bloquant) ;
- CLY-02 à CLY-05 (à corriger).

CLY-01 et CLY-02 touchent l'analyse. Il faut donc :

- un nom nouveau (R12), par exemple `analyser_echelle_v3.py`, un commit et des empreintes nouveaux ;
- rejouer la simulation et les tests ;
- un texte nouveau, et une contre-lecture neuve des parties changées (R2).

Les trois bloquants de cl1 sont levés : j'ai rejoué leurs preuves sur la v2. Les lectures fausses ont disparu, l'invariance par translation tient et les gabarits de prose sont neutres.

**Ce qui tient** :

- **Concordance du texte et du code** :
  - ordre de `lire()`, inégalités strictes ou larges conformes au texte ;
  - `SEUILS` (0,70 ; 0,25 ; 1,0) ;
  - `ATTENDUS` : modèles, révisions (conformes à la trace d'accès), couches 8, 12, 16, 20 et 20, 30, 40, 50, dimensions 4 096 et 8 192 ;
  - plis par blocs : E1 = blocs 1, 3, 6, 9, 11, 14 ; E2 = blocs 2, 5, 7, 10, 13, 15 ; S1 = blocs 0 et 8 ; S2 = blocs 4 et 12. Chaque pli a les positions A à D en nombre égal ;
  - 3 072 stimuli ;
  - contrôles de construction : lemmes a/b et b/gabarits disjoints, trois paires sur six à la première personne par jeu, négation syntaxique équilibrée ;
  - graines par `SeedSequence` ; versions et commit consignés dans la sortie.
- **Chiffres reproduits** :
  - aires des longueurs : 0,4966 (a) et 0,4823 (b) ;
  - sac de mots : 0,5717 avec centrage par moitié (0,5701 sans) ;
  - offre de référence (unités de Vast) :
    - `dph_total` = `dph_base` + stockage, soit 2,1333 + 0,0694 = 2,2028 USD/h ;
    - `gpu_ram` en Mo (46 068 pour une A40) ;
    - descente en USD/Go (0,0026) ;
    - dépense au pire : 2 h × 2,2028 + 160 × 0,0026 + 3 × 0,0694 + 0,20 = 5,2306 USD, comme la trace ;
  - l'arrondi par défaut de la durée garantit pire ≤ plafond par construction. La latence de la surveillance (au plus 60 s, plus 20 s d'attente de l'arrêt) coûte environ 0,08 USD au prix maximal ; la marge de 0,20 USD la couvre.
- **Tirage conditionné des paires du jeu a** :
  - la masse exclue vaut 6/6⁶ = 1/7 776 par tirage ; P(au moins un rejet sur 2 000) = 0,227, comme le texte ;
  - le biais est négligeable ; les rejets de la boucle principale sont comptés et consignés.
- **Témoin ν et fuite purement spécifique** : aucune fausse réserve sur 47 lectures « positif » ou « inverse », issues de 53 analyses (T1, T2, T3, K1 à K6, W10). Voir cependant CLY-02 pour le biais de ν.
- **Scripts d'instance et de lancement** :
  - recherche de clé au début de `pousser`, chemins d'échec compris ;
  - code de `ls-remote` distingué (0, 2, autre) au lancement et sur l'instance ;
  - HEAD égal au commit ; empreinte des stimuli vérifiée ;
  - `allow_patterns` exclut `original/`, si bien que la descente reste d'environ 157 Go, cohérente avec 160 Go ;
  - arrêt par identifiant (R10) ; noms neufs partout (R12).
- **R7** : chaque chiffre et chaque page cités concordent avec les cartes. Sources : carte v1 l. 114, 289, 358 et 359 ; carte v2 l. 57, 66 et 161 ; carte v3 § 0. Voir aussi CLY-10.
- **R3** :
  - aucune issue n'est visée ;
  - les conditions de « positif » et d'« inverse » sont en miroir, avec une réserve symétrique ;
  - la « fuite de signe inverse » est testée pour chacun des deux modèles ;
  - à Δλ vrai nul, 66 analyses : aucun « positif » ni « inverse ». Ce sont la reproduction (48) et H1 à H3 (18).

## Traitement des constats de cl1

| constat | gravité (cl1) | état | preuve ou réserve |
|---|---|---|---|
| CLX-01 λ signé | bloquant | **traité** | `lire()` l. 403–413. Reproduit sur la v2 : λ vrais (−1 ; −1), (0 ; −0,6) et (−0,6 ; 0) donnent tous trois « fuite de signe inverse » ; 3 tests |
| CLX-02 aires sans centrage | bloquant | **traité** | `centrer()` appliqué à ĉ, à la décomposition, à T1, à la direction fixe, au témoin et au sac de mots. Reproduit : translations de norme 60, 600 et 3 000, même lecture, écart maximal 0,0012 aux points et 0,0017 aux bornes |
| CLX-03 prose porteuse de contexte | bloquant | **traité** | Gabarits « …? Is it …? » et « Among …, …? » ; liste `MOTS_ETAT`. Le stimulus `ech-04-a-0-eval-prose` est devenu neutre. Contrôles rejoués (longueurs, lemmes, sac de mots 0,572). Reste la remarque CLY-12 |
| CLX-04 placebo inopérant | à corriger | **partiellement** | Placebo retiré, témoin par permutation, réserve symétrique, test : faits. Mais ν est aveugle à la part de ĉ propre au jeu a (CLY-01) et capte une part de la fuite spécifique quand la force des paires varie (CLY-02) |
| CLX-05 plis par parité | à corriger | **traité** | Blocs de quatre, garde à la construction, test |
| CLX-06 identité des dossiers | à corriger | **traité** | `charger_modele` et gabarit comparés avant tout calcul ; `--repetition` explicite ; 13 tests de gardes d'identité et d'intégrité (cas sain et artefacts). Sous-gardes non testées une à une : CLY-14 |
| CLX-07 devis incohérent | à corriger | **partiellement** | Dépense au pire calculée et testée. Mais le plafond de durée de la surveillance retombe sur 7 200 s si la variable manque, et les 3 h de stockage avant destruction ne sont pas gardées (CLY-03) |
| CLX-08 clé sur les chemins d'échec | à corriger | **traité** | `cle_dans_sorties` au début de `pousser` ; cas répété : clé dans les journaux, rien n'est poussé, la branche reste absente |
| CLX-09 manifeste de l'analyse | à corriger | **traité** | Python, numpy, commit, propreté consignés. Consignés, pas gardés : CLY-06 |
| CLX-10 gardes non testées | à corriger | **traité** | 60 tests, que je relance avec succès ; répétition scriptée conforme (sept cas, neuf lignes de résumé) ; `test_nul_strict` strict. Petits manques : CLY-14 |
| CLX-11 biais de A_ctx | à corriger | **traité** | A_ctx_fixe à directions fixes ; égalité au point testée. Effet observé : borne basse plus haute de 0,05 à 0,18 que celle de A_ctx réapprise (T3, H1) |
| CLX-12 atteignabilité | à corriger | **partiellement** | Simulation scellée et reproduite. Mais deux phrases dépassent ce qu'elle montre (CLY-04) |
| CLX-13 liste d'arrêt | à corriger | **traité** | Les six manques de cl1 y sont, conformes au code. Lacunes de dépense : CLY-03 |
| CLX-14 citations | à corriger | **traité** | 0,644 (tableau 15, p. 23) ; 0,491 en prose (p. 5 et 12) ; 0,676 pour le même modèle (p. 10, 21 et 24) ; « LLaMA-3.1-instruct (8B, 70B) » p. 3, sans identifiant exact ; « sept papiers » (carte v3) ; pages de Singh et Chaudhary : toutes conformes aux cartes |
| CLX-15 phrase permise | à corriger | **traité** | Phrase relative, décomposition, une phrase par issue. Formulation : CLY-09 |
| CLX-16 validité de construit | remarque | **traité** | Portée dans les limites |
| CLX-17 portée lexicale | remarque | **traité** | Définition énoncée, limite dite. Asymétries résiduelles chiffrées : CLY-12 |
| CLX-18 couche L\* | remarque | **traité** | λ et Δλ aux quatre profondeurs, en points. Point neuf, les égalités à saturation : CLY-08 |
| CLX-19 écarts incomplets | remarque | **traité** | Écarts 3 à 5 ajoutés. Ceux du v2 non repris : CLY-15 |
| CLX-20 traces non citées | remarque | **traité** | 8 traces, chemins et empreintes vérifiés |
| CLX-21 détails de code | remarque | **traité** | `ids.json` comparé au manifeste ; « jeton constant » ; Ec par format |

Bilan : 18 constats traités, 3 partiellement (CLX-04, CLX-07, CLX-12), aucun non traité.

## Le témoin ν, en bref

Question posée : est-il sensé, biaisé, déclenchable ?

- **Sensé, à moitié** :
  - il mesure la poussée du format le long des contrastes entre groupes de paires du jeu a, où le contexte s'annule ;
  - il ne regarde pas la moyenne des particularités, c'est-à-dire la part de ĉ propre au jeu a. C'est la voie de confusion la plus directe (CLY-01).
- **Normalisation par Ec et valeur absolue** :
  - la normalisation est cohérente avec λ ;
  - la valeur absolue se justifie, puisque le signe de d_σ est arbitraire. Son plancher de bruit est faible : ν de 0,04 à 0,16 sans fuite générique.
- **Biaisé** : vers le haut, dès que la force du cadrage varie d'une paire à l'autre, car d_σ hérite alors d'une composante ĉ (CLY-02). Le biais pèse sur le modèle au λ le plus grand, donc sur « positif » comme sur « inverse ».
- **Comparaison Δλ − Δν** : elle oppose un λ signé à un ν positif. C'est voulu, car une fuite générique a un signe quelconque le long de ĉ. Elle devient correcte une fois d_σ orthogonalisée.
- **Déclenchable** :
  - oui : T7 donne « inverse » avec réserve (1 sur 5) ;
  - mais une fuite générique forte sur les contrastes élargit d'abord l'intervalle de λ, et la lecture tombe le plus souvent en « indécis » ou en « fuite de signe inverse ». Sur 23 analyses (T4, T5, T6, G1), aucun faux « positif » ; le seul « positif » (T5) porte une fuite spécifique vraie ;
  - la réserve ne joue donc qu'à la marge. Le danger réel est l'angle mort de CLY-01, pas un défaut de sensibilité sur les contrastes.

## Constats nouveaux

### CLY-01 — BLOQUANT — λ compte la poussée du format sur la part de ĉ propre au jeu a ; ni ν ni la décomposition ne la voient : un « positif » sans réserve sous une fuite non spécifique

- **Localisation** :
  - `analyser_echelle_v2.py`, `mesures_couche`, l. 261–289 : ĉ est appris sur le jeu a ; Ef et Ec sont mesurés sur le jeu b ;
  - même fonction, l. 274–283, et `PARTITIONS`, l. 75–76 : d_σ = contraste entre deux groupes de trois paires ;
  - texte, « Mesures » (ĉ, témoin ν, décomposition) et critères 4 et 5.
- **Constat** :
  - ĉ ∝ moyenne des différences de paires du jeu a, soit concept + **signature propre aux cadrages a**. Cette signature est la moyenne des particularités des six paires : mots, style, polarité propres au jeu a.
  - Ec, mesuré sur b, ne contient que la part qui transfère. Ef, mesuré le long de ĉ entier, contient en plus toute poussée du format sur la signature a. Une telle poussée gonfle donc λ sans toucher le concept que les paraphrases b ancrent.
  - Le témoin ne la voit pas. Chaque d_σ est un contraste entre groupes de paires (Σσ = 0), donc orthogonal en espérance à la moyenne des particularités, c'est-à-dire à la signature. Il n'en capte qu'un reste fortuit (ν de 0,14 à 0,32 dans G3, contre 0,09 à 0,16 sous une fuite spécifique).
  - La décomposition ne la voit pas non plus. λ_a, le rapport de transfert et Ec par format dépendent de la composition de ĉ, pas de la direction de la poussée.
  - Le bootstrap ne la capte pas : c'est une composante systématique, pas une variabilité entre paires.
  - Elle est plausiblement plus forte chez le 8B, plus lexical, donc alignée sur le signe de la thèse (esprit de R3). Elle peut aussi fabriquer un « inverse » ou masquer un effet vrai.
- **Preuve** (`banc.py`, analyse inchangée ; annexe) :
  - **G3**. Au 8B, le format pousse seulement le long de la signature a, avec une norme de 2 fois l'effet du contexte ; aucune fuite sur le concept, aux deux tailles.
    - Résultat : **« positif » 5 sur 5, sans réserve** ;
    - λ(8B) de 0,66 à 1,29 ; borne basse de la spécificité de 0,11 à 0,89 ; ν(8B) de 0,14 à 0,32.
  - **G2**, à demi-intensité : « positif » sans réserve 3 sur 5.
  - **Décomposition identique** à celle d'une fuite purement spécifique, aux mêmes graines (`exp_decomposition.py`) :
    - transfert 0,728 et 0,843 dans les deux cas ;
    - λ_a de 0,74 et 0,83 (spécifique), contre 0,91 et 0,75 (signature).
  - Le test `test_temoin_de_permutation_sensible` tire des signes au hasard pour sa fuite générique. Il éprouve donc des contrastes, que ν voit par construction, et non la moyenne, qui est l'angle mort.
  - **Le contrôle symétrique discrimine** (`exp_lambda_ba.py`) : λ(b→a), direction apprise sur le jeu b d'une moitié, mesurée sur le jeu a de l'autre.

    | cas | λ(a→b) / λ(b→a) |
    |---|---|
    | fuite spécifique (T1, T2) | 1,05/0,97 ; 1,01/1,03 ; 0,99/0,99 ; 1,06/0,97 ; 1,05/0,92 ; 1,01/1,09 ; 0,98/1,00 ; 1,11/0,99 |
    | signature a (G3) | 1,29/0,25 ; 0,92/−0,19 ; 0,75/−0,27 ; 1,03/−0,06 |
    | aucune fuite | écarts ≤ 0,07 |

- **Correction** :
  - Calculer λ(b→a) de la même manière : ajustement croisé, centrage par moitié, mêmes tirages du bootstrap ; ainsi que Δλ(b→a). Les rapporter.
  - Puis, au choix :
    - (i) exiger les conditions de « positif » (ou d'« inverse ») pour les deux sens, a→b et b→a, avec la certification correspondante (aire sur le jeu a de la direction apprise sur b) ;
    - (ii) garder a→b décisif et ajouter une réserve obligatoire et symétrique, « signature des cadrages », si l'intervalle de Δλ(b→a) ne remplit pas la même condition. Pour « positif », c'est une borne basse > δ, avec la condition de signe sur λ(b→a) du 8B.
  - Ajouter le cas G3 à la simulation d'atteignabilité et un test (R5).
  - Une garde de construction bon marché : les lemmes présents d'un seul côté d'une paire du jeu a doivent être disjoints de ceux des gabarits. C'est vrai aujourd'hui, mais non gardé : voir CLY-12.

### CLY-02 — À CORRIGER — ν capte une part d'une fuite purement spécifique quand la force du contexte varie d'une paire à l'autre

- **Localisation** : `mesures_couche`, l. 274–283 ; texte, « Témoin de spécificité ν ».
- **Constat** :
  - Si D_j = κ_j·C + particularités, avec κ_j la force du cadrage de la paire j, alors d_σ contient (κ̄_groupe1 − κ̄_groupe0)·C. Avec six cadrages réels, il faut s'attendre à des forces inégales.
  - Pour une fuite purement spécifique, ν vaut alors environ |λ| × |cos(d_σ, ĉ)|. La spécificité Δλ − Δν est rognée en proportion du λ de chaque modèle.
  - La réserve « fuite non spécifique » se rapproche donc à tort de son seuil, pour le modèle au λ le plus grand. C'est vrai pour « positif » comme pour « inverse ».
  - Le |·| ajoute un plancher de bruit propre à chaque modèle. Il est faible ici : ν de 0,04 à 0,16 sans fuite générique.
- **Preuve** (annexe ; `exp_nu_orth.py`) :
  - **K1 et K2**, κ_j = 1 + 0,3·N(0, 1), fuite purement spécifique, λ vrai 1,0 : ν(8B) de 0,17 à 0,53, contre 0,06 à 0,14 sans hétérogénéité (T1) ; |cos(d_σ, ĉ)| moyen de 0,17 à 0,49.
  - **K5 et K6**, hétérogénéité 0,5 : ν(8B) jusqu'à 0,71.
  - Borne basse de la spécificité jusqu'à −0,03 et −0,02 dans deux analyses (K3, K6), lues « indécis » ou « certification asymétrique ».
  - Aucune fausse réserve sur les 47 lectures « positif » ou « inverse » de ces 53 analyses à fuite spécifique, mais la marge fond d'autant.
  - **d_σ orthogonalisées par rapport à ĉ** : ν⊥ de 0,04 à 0,09 sur les mêmes données. La sensibilité reste intacte sur une fuite générique : T4 donne ν de 1,06 à 1,51 et ν⊥ de 0,99 à 1,50.
- **Correction** :
  - Remplacer d_σ par normer(d_σ − (d_σ·ĉ) ĉ) avant la projection, au point et dans chaque tirage. C'est une ligne de code.
  - Ajouter un test : fuite spécifique avec des forces de paires inégales, sans réserve.

### CLY-03 — À CORRIGER — Plafond de 8 USD « au pire et tout compris » : deux hypothèses non gardées

- **Localisation** :
  - `surveiller_echelle_v2.sh`, l. 16 : `DUREE_MAX_S=${DUREE_MAX_S:-7200}` ;
  - `lancer_echelle_v2.sh`, l. 130–131 : la commande de surveillance n'est qu'écrite dans `lancement.txt`, et la destruction se fait « après vérification », à la main ;
  - `choisir_offre_v2.py`, l. 19 : `STOCKAGE_APRES_H = 3.0` ;
  - texte, « Dépense » et liste d'arrêt.
- **Constat** :
  - **(a) Repli silencieux (R5).** Si la session lance la surveillance sans la variable, le plafond retombe sur 7 200 s, même quand le lanceur a raccourci la durée.
    - Exemple, offre admise à 3,50 USD/h, descente 0,005 USD/Go et stockage 0,15 USD/h : plafond calculé de 6 737 s, pire = 8,00 USD. Avec 7 200 s, la dépense réelle atteint environ 8,33 USD.
    - Au bord du domaine admis (stockage 0,85 USD/h, plafond de 4 577 s) : environ 10,4 USD.
    - Le test `plafond > 2 h refusé` existe, mais aucun ne couvre la variable absente.
  - **(b) Destruction non gardée.** Les 3 h de stockage entre l'arrêt et la destruction sont un engagement manuel : ni garde, ni ligne de la liste d'arrêt. Chaque heure de plus coûte `storage_total_cost`.
    - Pour l'offre de référence (pire 5,23 USD), il reste une quarantaine d'heures de marge.
    - Pour une offre admise à un pire de 8,00 USD, toute heure au-delà de 3 h dépasse le plafond.
  - **(c) Surveillance vivante.** La garantie suppose que la surveillance locale vive jusqu'à l'arrêt. Côté instance, la fin de l'amorce termine le conteneur, mais rien ne demande l'arrêt de l'instance (l'instance n'a pas de clé Vast, à juste titre). Ce que Vast facture dans cet état n'est pas dit dans le texte.
- **Correction** :
  - Refuser l'absence de `DUREE_MAX_S` et de `CREATION`, ou bien faire écrire par le lanceur un fichier que la surveillance lit. Ajouter un test.
  - Inscrire la destruction par identifiant dans le plan et dans la liste d'arrêt (« instance non détruite 3 h après l'arrêt : destruction par identifiant, consignée »), ou élargir `STOCKAGE_APRES_H`, par exemple à 24 h.
  - Dire (c) dans le texte.

### CLY-04 — À CORRIGER — Atteignabilité : deux phrases dépassent la simulation citée

- **Localisation** : texte, « Atteignabilité » (« Ce tableau montre que chaque issue est atteignable ») ; critère 8 (« Sous H_0 avec une hétérogénéité forte des cadrages, c'est l'issue attendue (simulation ci-dessus) ») ; « R3 tenue ».
- **Constat** :
  - **Le tableau lui-même est reproduit à l'identique** avec le script scellé et ses graines : 16 cases sur 16 (`reproduction-atteignabilite/`, `scripts/comparer_atteignabilite.py`).
  - Il ne montre que quatre issues : « nul », « indécis », « pas de fuite », « positif ».
  - Sous H_0, à tau 0,4, le cas le plus hétérogène simulé, il donne « nul » 9 fois sur 12 et « indécis » 3 fois sur 12 : « indécis » n'y est pas l'issue attendue.
  - Les autres issues sont bien atteignables, mais pas dans ce tableau. Dans mon banc :
    - « fuite de signe inverse » : reproduction de CLX-01 ;
    - « inverse », avec et sans réserve : T7, K4 ;
    - « non certifiable » : C1, H3 ;
    - « certification asymétrique » dans les deux sens : C2, C3, K5, H3.
  - Mon extension sous H_0 :
    - à tau 0,8, « indécis » 12 sur 12, avec ou sans interaction ;
    - à tau 1,2, la certification échoue dans 5 analyses sur 6.
  - « 0 sur 24 : R3 tenue » parle en fait d'étalonnage. On peut écrire 0 sur 48 en comptant les lignes « pas de fuite », où Δλ est nul aussi.
- **Correction** :
  - Étendre et sceller la simulation : tau 0,8 et 1,2, inverse, signe inverse, contexte faible, et le cas G3 de CLY-01.
  - Ou bien réécrire les deux phrases. Par exemple : « quatre issues sont atteintes dans ce tableau, les autres dans [trace] » ; « “indécis” devient majoritaire sous H_0 quand l'hétérogénéité croît ».

### CLY-05 — À CORRIGER — R6 : le chiffre du sac de mots (0,572) ne renvoie à aucun chemin ni empreinte

- **Localisation** : texte, « Mesures », sac de mots.
- **Constat** : `construction-echelle-v2.json` ne contient pas cette valeur, et aucune trace ne la porte. R6 est une règle gelée.
- **Preuve** : je la reproduis avec les fonctions de l'analyse sur les stimuli :
  - 0,5717 avec centrage par moitié ;
  - 0,5701 sans centrage ;
  - moyennes des scores bruts par moitié : −0,389 et −0,099.
- **Correction** : verser la valeur dans le rapport de construction ou dans une trace empreintée, et la citer.

### CLY-06 — REMARQUE — L'intégrité du run d'analyse est consignée, pas gardée

- Rien n'arrête l'analyse décisive si :
  - l'empreinte de son propre script diffère de `d8534a94…` ;
  - le commit n'est pas `495b8bd…` ou l'arbre n'est pas propre ;
  - numpy n'est pas en version 2.4.6 (les suites aléatoires en dépendent) ;
  - la sortie est marquée « répétition ».
- Le sous-agent du verdict devra donc tout vérifier à la main. Proposer une ligne de la liste d'arrêt ou une garde.
- Détail : lancer les tests dans l'arbre crée des `__pycache__` non suivis, et rend `arbre_scripts_propre` faux.

### CLY-07 — REMARQUE — Intervalles de λ_a et du rapport de transfert biaisés

- Dans chaque tirage, les mêmes poids de paires du jeu a servent à apprendre ĉ et à mesurer le jeu a de l'autre moitié. Les paires tirées en double sont favorisées des deux côtés : Ec(a) est gonflé, λ_a et le transfert sont dégonflés.
- Le point se trouve en haut de son intervalle : λ_a 0,738 dans [0,519 ; 0,746], et 0,833 dans [0,584 ; 0,850].
- Ces grandeurs sont rapportées sans lecture. Donner seulement les points, ou découpler les poids (tirer les paires de mesure à part).

### CLY-08 — REMARQUE — Choix de L\* : à saturation, la règle d'égalité décide

- À contexte explicite, une aire de 1,00 à plusieurs couches est plausible, surtout au 70B. La règle « la plus basse » choisit alors la plus basse des couches saturées, faute d'information, et les deux modèles peuvent finir à des profondeurs relatives différentes pour cette seule raison.
- Proposer un critère second qui ne sature pas, par exemple l'écart des moyennes rapporté à l'écart-type, sur le pli S. Ou, au minimum, une réserve si le Δλ à profondeur appariée contredit le signe du Δλ décisif.

### CLY-09 — REMARQUE — Hypothèses et formulations

- H_A et H_0 ne recouvrent pas l'espace et ne suivent pas les critères :
  - λ(8B) dans ]0 ; δ] avec Δλ > δ n'est ni H_A ni H_0 ;
  - λ(70B) ≥ 1 avec Δλ > δ relève de H_A, mais la lecture est « indécis ».
  - Aligner H_A sur les quatre conditions du critère 4.
- « déplace la direction "évaluation" vers "évaluation" » (critère 4, repris aux critères 5 et 6) : écrire plutôt « déplace la lecture le long de la direction "évaluation", vers son pôle "évaluation" ».

### CLY-10 — REMARQUE — Indices contraires à 70B non cités (R4, R8)

- La carte v2 note qu'à 70B (Llama-3.3), les erreurs de la sonde de Nguyen et al. suivent qualitativement le format (p. 6 ; figure 7, p. 8 ; carte v2, l. 24–27).
- La carte v3 note que Xiong et al. déplacent le score de cette sonde en réécrivant les items (format et style mêlés).
- Ces indices vont contre la prédiction indicative λ(70B) ≈ 0 à 0,3 et contre la thèse de Singh et Chaudhary. Les citer avec les « points d'appui », par symétrie.

### CLY-11 — REMARQUE — L'exemple « aires à 1,00 » de R4 se déclenchera probablement sur la certification

- L'écart 2 annonce une aire du contexte presque au plafond. Préciser quelles aires sont visées (A_conf, A_conf_T1), ou annoncer que A_ctx_fixe peut valoir 1,00 sans réserve.

### CLY-12 — REMARQUE — Résidus lexicaux non gardés

- « answer » est commun au jeu a (quatre paires, des deux côtés) et au gabarit qcm 1. C'est symétrique, donc sans effet de premier ordre, mais aucune garde ne couvre a ∩ gabarits.
- Mots courts asymétriques :
  - jeu a : « how » 4/0, « see » 3/0, « me » 0/2 ; « you » 1/0 dans la paire 2 (deuxième personne déséquilibrée) ;
  - jeu b : « on » 0/5, « to » 2/6, « now » 2/0, « for » 0/2, « gap » 0/2.
- `MOTS_ETAT` est vérifié par sous-chaîne sur un seul rendu fictif. Les contenus 51 (« needle ») et 53 (« known ») contiennent des mots de la liste, constants entre cellules donc sans effet.

### CLY-13 — REMARQUE — Contrôles à faire avant le GO, sans dépense

- Rendre le premier stimulus avec les deux jeux de jetons (le tokenizer seul, aux deux révisions), et vérifier sur processeur que le texte rendu et le dernier jeton sont identiques. Sinon, la garde de l'analyse arrêterait tout après la dépense.
- `device_map="auto"` peut délester silencieusement des couches sur le processeur ou le disque. Ajouter une garde : aucune entrée « cpu » ni « disk » dans `hf_device_map`.
- Relire le `dph_total` de l'instance créée et le comparer à l'offre choisie.

### CLY-14 — REMARQUE — Tests : sous-gardes non éprouvées une à une (R5)

- Non éprouvées une à une :
  - révision, couches et dimension (seul « modèle » déclenche le test des dossiers inversés) ;
  - dernier jeton différent entre modèles (seul `rendu_premier` est altéré) ;
  - compagnon de script faux sur l'instance ;
  - `DUREE_MAX_S` absente ;
  - « positif » refusé par borne basse de λ(8B) ≤ δ, ou de λ(70B) ≤ −δ.

### CLY-15 — REMARQUE — Détails du texte

- L'en-tête dit « vers 23:55 UTC », mais les traces citées datent de 00:10 et 00:15.
- Les écarts 3 à 5 du v2 (négation réécrite, ajouts, tests) ne sont plus listés comme écarts au brouillon v1.
- La sortie d'atteignabilité ne consigne ni versions ni commit (R9).
- Les rejets du tirage du sac de mots ne sont pas comptés.
- La section « Intervalles » ne dit pas le conditionnement du tirage des paires du jeu a ; il n'apparaît qu'en fin de texte.
- Le texte écrit « / Ec » pour ν, le code divise par |Ec|. C'est sans effet dès que la certification passe.

## Annexe — banc synthétique (analyse inchangée, 300 tirages, d = 64)

| cas | vérité (8B ; 70B) | lectures |
|---|---|---|
| CLX-01 (a), (b), (c) | λ (−1 ; −1), (0 ; −0,6), (−0,6 ; 0) | fuite de signe inverse ×3 |
| contrôle | λ (0,6 ; −0,2) | indécis |
| CLX-02 | λ (0,6 ; 0,2), translation 0, 60, 600, 3 000 | positif ×4, mêmes valeurs à 0,002 près |
| T1, T2 | spécifique (1,0 ; 0,1), tau 0,15 et 0,4 | positif 10/10, sans réserve |
| T3 | idem, bruit du 8B ×3 | positif 4, certification asymétrique (grand) 1 |
| T4 | générique sur contrastes de paires au 8B, λ concept 0 | indécis 3, fuite de signe inverse 2 |
| T5 | spécifique + générique (contrastes) au 8B | indécis 4, positif 1 (sans réserve) |
| T6 | idem aux deux | indécis 5 |
| T7 | inverse spécifique + générique au 70B | indécis 4, inverse avec réserve 1 |
| T8 | générique orthogonal au 8B | pas de fuite 4, indécis 1 |
| G1 | générique sur contrastes, tau 0,25 | indécis 6, fuite de signe inverse 2 |
| **G2, G3** | **signature moyenne du jeu a au 8B, λ concept 0** | **positif 3/5 et 5/5, sans réserve** |
| H1, H2 | H_0 (0,5 ; 0,5), tau 0,8, ± interaction | indécis 12/12 |
| H3 | H_0, tau 1,2 | non certifiable 3, certification asymétrique 2, indécis 1 |
| C1, C2, C3 | contexte faible aux deux, au 8B, limite au 8B | non certifiable 2 ; certification asymétrique (grand) 2 et 4 |
| K1 à K6 | spécifique, force des paires inégale (0,3 à 0,5) | positif 21, indécis 3, inverse 6, certification asymétrique (petit) 2 ; ν(8B) jusqu'à 0,71 |
| W9, W10 | spécifique (0,6 ; 0,2), bruit du 8B ×3 ou égal | indécis 6 ; positif 6 |
| reproduction | simulation scellée, mêmes graines | identique au tableau du texte : 16 cases sur 16, même empreinte d'analyse et de stimuli |

Pièces du banc, dans `scripts/` :

- `banc.py` : générateur et appel de l'analyse ;
- `exp_bloquants.py`, `exp_temoin.py`, `exp_complements.py` : scénarios ;
- `exp_lambda_ba.py`, `exp_nu_orth.py`, `exp_decomposition.py` : contrôles au point ;
- `verif_stimuli.py`, `verif_empreintes.py`, `comparer_atteignabilite.py` : vérifications.

Sorties dans `sortie-*.txt` et `tests-cl2.txt`. Graines du générateur : 101 et 102 (CLX-01), 201 et 202 (CLX-02), 5000 + 10k (T), 7000 + 10k (G, H, C, K, W) ; entropie de l'analyse 12345.
