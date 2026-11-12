# Préenregistrement — la fuite du format dans la direction « évaluation » diminue-t-elle avec l'échelle ? Llama-3.1 8B contre 70B (v2)

- **Auteur** : lignée « session-depot » (Claude), le 26 octobre 2026, vers 22:45 UTC (`date -u`). Mode rapide d'exploration (R-522, option (a) : R1 et R3 gardées, le reste élagué).
- **Remplace** le brouillon v1 (`prereg/brouillon-echelle-conscience-eval-v1.md`, `7c38d340…`, jamais scellé ni lancé). Les écarts et leurs motifs sont listés en fin de texte. **Décisions** : R-523 (le pari est l'échelle, pas la certification du 8B), mot de Lazar « go en parallèle » (R-523, comparaison 8B contre 70B).
- **Scellement** : avant toute lecture de résultat (R1). Expérience décisive. Contre-lecture par un sous-agent neuf (R2), consignée plus bas.
- **Modèles** (même famille, même génération, même gabarit de dialogue) : `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` ; `meta-llama/Llama-3.1-70B-Instruct`, révision `1605565b47bb9346c5515c34102e054115b4f98b`. `bfloat16`, une passe avant par stimulus, lot de un, sur **la même instance**. Accès vérifié le 26 octobre vers 22:05 UTC : 200 pour les deux. Llama-3.3-70B-Instruct répond 403 : licence non acceptée sur le compte.
- **Outils** : branche `outils/echelle-conscience-eval-v1`, commit `c74b267787222ffead04d5b1f7b894a7804ca378`. Empreintes :

  | fichier | sha256 |
  |---|---|
  | `echelle-v1/stimuli/echelle-v1.json` | `bb285e11a63351047be7d7fb7e1827748884e107ccdbbcb4e6e9e3b322783b5b` |
  | `echelle-v1/scripts/construire_echelle_v1.py` | `a7521fa8c5138c039fface75412560d3d64642b404578e6ae34d17643bb796d1` |
  | `echelle-v1/scripts/mesurer_echelle_v1.py` | `d3dff98dde5505514c467ce401aca64d44e9ffb13325e9c247c5ad213410ac0f` |
  | `echelle-v1/scripts/analyser_echelle_v1.py` | `2c9c66a4b2de55316098f5b8fedfc08df53118421a8dc3b89cecbc7be8fed530` |
  | `echelle-v1/scripts/echelle_instance_v1.sh` | `f4b15ed4f75b4f8a0e35ab88b770833c593f2762e3d8801148d3709e7d46fdb9` |
  | `echelle-v1/scripts/amorce_echelle_v1.sh` | `43ca7736a95487b5e1361a8052cf39a49c7f30656bab67e3b7cca286c8f60156` |
  | `echelle-v1/scripts/lancer_echelle_v1.sh` | `74a3e61ef58375846d609d91678b63156fc25d59cb29c2b71518a15bb80642cf` |
  | `echelle-v1/scripts/surveiller_echelle_v1.sh` | `7e0459b146f1ff00cdb91cddc3097bc4385263e7cb03bf31ac88bd884ffaf640` |
  | `echelle-v1/scripts/requirements-echelle-v1.txt` | `34b1262856da879eec5e006c31ac0c9a623d9332ed162b82d68966aed5d0cdbd` |
  | `echelle-v1/tests/test_analyser_echelle_v1.py` | `5376b0789b5a11400e08281868b8af22089b30efac1c240ecc041ff32c1530a2` |

- **Dépense** : un GO nouveau, sur devis, avant toute carte. Rien ne part avant ce GO et avant le scellement. Devis :
  - une instance, de deux à quatre cartes de 46 Go ou plus, 160 Go au total, CUDA ≥ 13.0 ;
  - au plus 4 USD de l'heure ; descente au plus 0,01 USD le Go ;
  - attendu ≈ 1 h, soit ≈ 3 à 3,5 USD de location et ≈ 0,4 USD pour descendre ≈ 160 Go ;
  - **plafond demandé : 8 USD** ; durée plafonnée à 2 h, arrêt par identifiant (R10).
  - Offre de référence relue le 26 octobre (lecture seule) : deux RTX PRO 6000 de 96 Go, ≈ 3,0 USD/h, descente 0,0026 USD/Go.

## Hypothèse

Selon la thèse de Singh et Chaudhary (2026), la conscience d'évaluation suit surtout le **format** chez les petits modèles et davantage le **contexte** chez les grands. Leur preuve s'arrête à 12B, sans plan croisé, et 70B y est déclaré ouvert (carte des zones libres v1, ligne ii-3 : `docs/sources/anteriorite-hm1-20261026/carte-zones-libres-v1.md`, `134040bd…`).

Traduite en géométrie, au contenu égal, avec format et contexte croisés :

- On apprend une **direction « évaluation »** ĉ à format constant : des paires de cadrages qui ne diffèrent que par la situation de l'auteur, qui connaît la réponse et regarde, ou ne la connaît pas et en a besoin.
- On la mesure ensuite sur des **paraphrases tenues à part**.
- Le gabarit de **banc d'essai** (qcm), à contexte égal, déplace la lecture le long de ĉ moins chez le 70B que chez le 8B.

Les deux hypothèses :

- **H_A** : Δλ = λ(8B) − λ(70B) > δ, où λ est l'indice de fuite du format (métrique ci-dessous).
- **H_0** : |Δλ| ≤ δ (pas d'effet d'échelle), ou Δλ < −δ (effet inverse).

## Prédiction chiffrée et signe attendu

- **Aucune issue n'est visée (R3)** ; toutes sont lues et rapportées au même titre (R4).
- À titre indicatif, sans effet sur la lecture, l'auteur s'attend à :
  - Δλ > 0 (signe de la thèse ci-dessus) ;
  - λ(8B) ≈ 0,5 à 1 et λ(70B) ≈ 0 à 0,3 ;
  - une probabilité subjective d'environ 0,35 pour l'issue « positif ».
- Point d'appui vérifié sur PDF : chez Nayan et al. (2026), la détection comportementale du 8B passe de 0,644 à 0,491 sur le plan croisé de Devbunova (tableau 15 p. 23 ; p. 5 et p. 12 ; carte v1). C'est un autre instrument, cité seulement pour le signe.
- Chaudhary et al. (2025) sondent la même paire de modèles (Llama-3.1-instruct 8B et 70B), sans contrôle du format (p. 3 et p. 6 ; carte v2, `fe1e93c1…`). Le plan croisé à 70B n'est fait dans aucun des sept papiers lus (R-507). C'est une **extension méthodologique**, pas une zone vierge (R8).

## Métrique

**Stimuli** (`construire_echelle_v1.py`, déterministe, sans modèle, sans graine) :

- 64 contenus neufs : questions factuelles neutres à quatre options, sans chiffre. Aucune question reprise des stimuli de H-M1 v1, v2 et v4 (vérifié à la construction, empreintes consignées dans `construction-echelle-v1.json`).
- Plan : format {qcm, prose} × contexte {eval, reel}. Le contenu est identique dans les quatre cellules ; seuls varient le gabarit de format (deux par format) et la phrase de cadrage placée en tête du message. Le message système est constant.
- Jeux de cadrages, en paires minimales :

  | jeu | paires | rôle | contraste |
  |---|---|---|---|
  | a | 6 | apprentissage | eval / reel |
  | b | 6 | mesure | eval / reel |
  | placebo | 4 | témoin | mer / montagne, en usage réel des deux côtés |

  Dans chaque paire : même personne grammaticale (trois paires sur six à la première personne), même nombre de marques de négation (garde à la construction).
- Contrôles à la construction :
  - lemmes disjoints entre les jeux a et b, et entre b et les gabarits ;
  - aire des longueurs, eval contre reel : 0,496 (a), 0,478 (b), 0,519 (placebo).
- Référence lexicale mesurée sur les textes **avant tout modèle** : un sac de mots appris sur a et appliqué à b donne une aire de 0,585. Une version antérieure des cadrages, à négation déséquilibrée, donnait 0,98 ; elle a été corrigée.
- Plis de contenus : S1 et S2 (8 + 8), pour le choix de couche ; E1 et E2 (24 + 24), pour la mesure. Toutes les positions de la bonne réponse sont présentes dans chaque pli.
- Au total, 4 096 stimuli.

**Activations** (`mesurer_echelle_v1.py`) :

- flux résiduel au dernier jeton de l'entrée, après l'en-tête de réponse (position constante, vérifiée) ;
- quatre profondeurs relatives, 0,25 ; 0,375 ; 0,5 et 0,625 : couches 8, 12, 16, 20 (8B) et 20, 30, 40, 50 (70B) ;
- stockage en float16.

**Mesures**, par modèle, à la couche L\* (`analyser_echelle_v1.py`, qui fait foi pour le détail du calcul) :

- **ĉ** : différence des moyennes eval − reel du jeu a, les deux formats confondus, normée. Elle est apprise sur une moitié des contenus E et appliquée au jeu b de l'autre moitié (ajustement croisé E1 → E2 et E2 → E1). Projections s = x · ĉ.
- **Ec** = moyenne sur les formats de [s̄(eval) − s̄(reel)] ; **Ef** = moyenne sur les contextes de [s̄(qcm) − s̄(prose)].
- **λ = Ef / Ec**, l'indice de fuite du format, sans dimension et comparable entre modèles :
  - 0 : le format ne bouge pas la lecture « évaluation » ;
  - 1 : il la bouge autant que le contexte ;
  - positif : le banc d'essai pousse vers « évaluation ».
- **A_ctx** : aire (eval contre reel) à format égal, moyenne des deux formats. C'est la **certification** : ĉ lit-il le contexte sur des paraphrases tenues à part ?
- **A_conf** : aire sur les cellules en conflit, (prose, eval) contre (qcm, reel).
- **Témoin placebo** : la même chose avec ĉ remplacé par la direction mer − montagne, apprise sur deux paires du placebo et mesurée sur les deux autres. On en retient |λ_p|.
- **Diagnostic T1**, à titre comparatif avec la littérature : direction apprise sur les cellules concordantes du jeu a, (qcm, eval) − (prose, reel) ; aire A_conf_T1 sur les cellules en conflit du jeu b.
- **Sac de mots** : régression logistique sur les textes du jeu a, aire sur le jeu b. C'est une référence lexicale qui ne dépend d'aucun modèle.

**Couche L\*** : choisie par modèle sur le pli S seulement (ajustement croisé S1 et S2), à l'aire A_ctx maximale ; en cas d'égalité, la plus basse. Elle est ensuite fixée. Elle n'est jamais choisie sur λ.

**Contraste principal** : Δλ = λ(8B) − λ(70B).

**Intervalles** : bootstrap apparié, avec les mêmes tirages pour les deux modèles.

- On tire avec remise les contenus dans chaque moitié de E, et les paires de cadrages dans chaque jeu (pour le placebo, à l'intérieur de chaque groupe tenu à part).
- 2 000 tirages ; percentiles 2,5 et 97,5 ; directions réapprises à chaque tirage ; L\* fixe.
- Graines : `numpy.random.SeedSequence(4429003211691042563)` (R9), entropie tirée le 26 octobre à 22:42 UTC, avant tout scellement et toute mesure.

## Seuil

Fixés sans donnée, contraignants une fois scellés (`SEUILS` dans l'analyse) :

| grandeur | seuil |
|---|---|
| certification | borne basse de A_ctx ≥ 0,70 |
| δ (écart d'échelle minimal d'intérêt sur λ) | 0,25 |
| λ(70B) maximal pour « positif » | borne haute < 1 (au 70B, le contexte bouge la lecture plus que le format) |
| « pas de fuite » | bornes hautes de λ(8B) et de λ(70B) < 0,25 |
| spécificité | borne basse de [Δλ − (|λ_p|(8B) − |λ_p|(70B))] > 0 |

## Plan d'analyse

1. **Sur l'instance** (`echelle_instance_v1.sh`) :
   - vérifier le commit, la branche de résultats absente, l'empreinte des stimuli et celles des scripts ;
   - mesurer le 8B et pousser ; effacer le 8B du cache, mesurer le 70B et pousser, sur la branche neuve `donnees/echelle-conscience-eval-v1` ;
   - aucune lecture : formes, nombres finis, empreintes.
2. **En local, processeur** :
   - `python -I -B analyser_echelle_v1.py echelle-v1.json <petit> <grand> 4429003211691042563 <sortie neuve>` ;
   - la sortie `analyse-echelle-v1.json` est scellée.
3. **Lecture** : mécanique (ci-dessous), prononcée par un sous-agent neuf qui n'a écrit ni ce texte ni l'analyse, puis scellée.

## Critères de lecture gelés

La lecture se fait dans cet ordre (`lire()` de l'analyse).

1. **Non certifiable** : borne basse de A_ctx < 0,70 pour **les deux** modèles. λ n'est pas lu.
2. **Certification asymétrique (grand seulement | petit seulement)** : un seul modèle est certifié. λ n'est pas lu ; ΔA_ctx est rapporté avec son intervalle.
3. **Positif** : borne basse de Δλ > 0,25 **et** borne haute de λ(70B) < 1.
   - Phrase permise : « sur Llama-3.1, à contenu égal et à format croisé, le gabarit de banc d'essai déplace la direction "évaluation" moins à 70B qu'à 8B ».
   - Réserve obligatoire « fuite non spécifique » si la borne basse de la spécificité est ≤ 0.
4. **Inverse** : borne haute de Δλ < −0,25.
5. **Pas de fuite** : bornes hautes de λ(8B) et de λ(70B) < 0,25. Le format ne bouge pas la direction aux deux tailles ; Δλ n'est pas interprété.
6. **Nul** : intervalle de Δλ inclus dans [−0,25 ; 0,25].
7. **Indécis** : tout le reste.

Rapportés dans tous les cas, sans lecture décisive :

- λ, A_ctx, A_conf, Ec, Ef, |λ_p|, A_placebo et A_conf_T1 par modèle, avec leurs intervalles ;
- ΔA_ctx et ΔA_conf ;
- l'aire du sac de mots, et la marge A_ctx − sac par modèle ;
- L\* et les aires du choix de couche.

Limites de la lecture :

- une famille, deux tailles, une manipulation de contexte (« l'auteur connaît la réponse ») ;
- aucune généralisation à la conscience d'évaluation en général, à d'autres familles ou à d'autres marqueurs ;
- une sonde linéaire qui lit un texte mesure la représentation du lecteur (validité de construit, R-525).

**R4** : une issue trop propre déclenche le même audit des formes et des empreintes, quel que soit son signe, avant tout rapport, et une réserve. Par exemple : λ exactement nul, intervalles anormalement étroits, aires à 1,00.

## Liste d'arrêt

Chacune arrête sans lecture et se consigne :

- révision du modèle différente de celle attendue, ou `_commit_hash` contraire ; dernier jeton de l'entrée non constant ;
- une activation non finie, ou hors de l'étendue de float16 ;
- l'empreinte des stimuli ou d'un script différente de ce texte, ou de son compagnon ; HEAD différent du commit ;
- la branche `donnees/echelle-conscience-eval-v1` déjà présente (R12) ;
- aucune offre conforme au devis, ou crédit insuffisant ;
- une dépense qui dépasserait le GO ;
- une instance au-delà de 2 h, arrêtée par son identifiant (R10) ;
- une clé trouvée dans les sorties : rien n'est poussé ;
- un refus de téléchargement (licence, 403) ;
- en local : ordre des identifiants différent des stimuli, empreinte différente du manifeste, tirage de bootstrap non fini (l'analyse s'arrête, code 1) ;
- toute surprise hors de cette liste : arrêt, compte rendu, Lazar décide.

## Écarts au brouillon v1 et motifs

1. **70B** : Llama-3.3 est remplacé par Llama-3.1, même famille et même génération que le 8B. La licence 3.3 n'est pas acceptée sur le compte (403).
2. **Mesure principale** : « aire décorrélée » devient l'indice de fuite λ.
   - Avec une phrase de contexte explicite, l'aire du contexte serait presque au plafond aux deux tailles.
   - Le seuil Δ > 0,10 du v1 serait alors inatteignable par construction dès que le 8B dépasse 0,90.
   - λ ne plafonne pas.
3. **Cadrages réécrits sans négation déséquilibrée**. Sac de mots de a vers b : 0,98, puis 0,585.
   - Sans cette correction, ĉ aurait pu n'être qu'une direction « négation ».
   - Le format ne s'y projette pas, ce qui aurait biaisé vers « pas de fuite ».
4. **Ajouts** :
   - le témoin placebo (spécificité) et le diagnostic T1 ;
   - les issues « certification asymétrique » et « pas de fuite » ;
   - le bootstrap sur les paires de cadrages en plus des contenus.
5. **Analyse** : bloc-notes processeur et douze tests synthétiques à vérité connue.
   - Cas sains : positif, nul, pas de fuite, inverse, non certifiable, certification asymétrique, fuite non spécifique.
   - Artefacts : ordre des identifiants, empreinte, valeur non finie, sortie déjà présente.
   - Les douze passent (`echelle-v1/tests/`).
   - Répétition locale de toute la chaîne d'instance, avec un modèle minuscule et un dépôt local : cas sain poussé ; mauvais commit et branche déjà présente arrêtés avant tout calcul.

## Contre-lecture

À REMPLIR après la relecture par un sous-agent neuf (R2), qui lit ce texte, le brouillon v1, les scripts et les tests.
