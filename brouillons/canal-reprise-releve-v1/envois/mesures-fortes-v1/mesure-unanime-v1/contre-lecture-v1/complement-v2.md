# Contre-lecture (R2), complément — v2 du préenregistrement « mesure unanime » et de son script, changements seuls

- Contre-lecteur : le même sous-agent Opus 5.5 que pour la v1 (auteur ni du texte ni du script).
- Début : 2026-10-27 23:32:40 UTC (`date -u`). Fin : dernière ligne du document.
- Synthétique seulement ; `scores-p3.npz` ni ouvert ni lu ; aucun fichier du dépôt modifié ; aucun commit.

## Verdict

**À corriger en v3.** Liste : (a) le bras M4 mélange un élargissement d'échelle et la dépendance. Il est confirmé par
construction, maximum compris, et la première ligne de lecture en tire « A(a)3 fondée », ce qu'il ne montre pas.
(b) La plage de M3 « [0,02 ; 0,08] » n'est pas alignée entre le tableau et le Seuil, n'a pas de zone intermédiaire, et
peut bloquer toute la lecture à tort. (c) La table de M2 bis est à refaire avec le code v2, et sa réfutation « ≤ 0 » doit
dépendre de r₀. (d) Les gardes d'empreinte et d'effectifs sont facultatives et non testées. (e) Quelques formulations de
lecture (première et deuxième lignes). Le reste est fermé.

## Empreintes lues

| fichier | empreinte |
|---|---|
| `preenregistrement-mesure-unanime-v2.md` (disque) | `e6369f43ac5481ac55832db74a9f44130908c4ce9b39442d942a02962b610c51` (attendue : conforme) |
| `analyse_fausses_alertes_v2.py` | `d8ded1e0a76a55742878c72a429f8487c560b5ef7b7d285aaf99152bd098c6fe` (conforme ; identique dans le commit `ffd5968c`) |
| `sortie-synthetique-essai-v2.json` | `954d0b8d0a1c31c22c79d12ab174e59f3bbc3340e699ca2f78effbf39f118015` (conforme) |
| `contre-lecture-v1/rapport-contre-lecture-mesure-unanime-v1.md` (copie versée) | `5d47ae52…` : identique à mon rendu |

Le préenregistrement v2 du commit `ffd5968c` (`2d80508f…`) diffère de celui du disque (`e6369f43…`). La version scellée
devra être committée à son tour.

Mes vérifications (dossier de ce complément, compagnons `.sha256`) : `verif3_v2_v1.py` → `sortie-verif3-v2-v1.json`
(graine `SeedSequence(20261027234000)`, enfants (0,) à (3,)) ; `verif4_table_m2_v2_v1.py` →
`sortie-verif4-table-m2-v2-v1.json` (graine `SeedSequence(20261027234500)`). Les deux importent le script v2 sans le
modifier.

## (1) Fermeture des constats

| constat | état | raison |
|---|---|---|
| CM-1 | **à moitié** | M3 devient un contrôle ; A(a)1 et A(a)3 sont tranchées ; le bras M4 est ajouté, mais il est confondu avec un changement d'échelle et porte un verdict (voir (2) et (6)). |
| CM-2 | fermé, avec une réserve | M2 principal = Ville au-dessus de α à τ = 2 ; r₀ mesuré ; ligne « M2 ter ». Réserve : la table de M2 bis vient de ma simulation v1 (12 sondes, 4 tirages, 20 épisodes de normalisation, effets par sonde). Refaite avec le code v2 (8 sondes, 4 tirages) : +0,147 (r₀ = 0), +0,139 (0,2), +0,071 (0,5), **−0,009 (0,8)**. L'écart à la v1 atteint 0,05 à r₀ = 0,2, plus que la tolérance de ± 0,03. À r₀ élevé, la différence peut être nulle ou négative alors que Ville est déjà à 0,16 à τ = 0. Ville à τ = 2 atteint 0,15 à 0,17 : le « plafond 0,16 » est juste à la limite. |
| CM-3 | **à moitié** | Finitude, scores constants et K sont codés et testés. L'empreinte et les effectifs sont codés mais **facultatifs** : les arguments valent `None` par défaut et le contrôle est sauté en silence si on les omet. Ils ne sont pas testés, pas plus que E < 44. La commande du texte écrit `968414fc…` tronqué : copiée telle quelle, elle arrête le run (l'erreur est sûre, mais il faudrait une version nouvelle). |
| CM-4 | fermé | `cal_idx` est trié par `rang[e]`, donc dans l'ordre de la permutation (vérifié, partie L : la normalisation prend les positions 0 à 16 de la permutation, un sous-ensemble tiré au hasard, indépendant de l'ordre des identifiants). |
| CM-5 | **à moitié** | K = 39 et un niveau exact de 0,05 si E = 60, E ≥ 44 : dit et codé. Mais si E vaut 44 à 59, le niveau n'est plus 0,05 (E = 50 : K = 30, niveau 1/31 = 0,032 ; E = 55 : environ 0,028), et la plage de M3 reste fixe. `seuils_K` est toujours jeté (`al, _ = …`) : K par pli n'est pas consigné. |
| CM-6 | fermé | Le verdict placebo ne porte que sur les statistiques conformes ; pour M1 et M2, l'écart est seulement rapporté. |
| CM-7 | fermé | Un vecteur `effets[τ][tirage]` commun à toutes les sondes, multiplié par τ·σ_sonde. |
| CM-8 | fermé | L'intervalle est dit conditionnel aux calibrages. |
| CM-9 | **à moitié** | Le commit `ffd5968c` contient bien le script (empreinte vérifiée) ; la source de P8 est dite. Mais l'empreinte de `bases/sequentiel.py` manque (R6). La commande garde `--commit <commit du scellement>`. |
| CM-10 | **à moitié** | Lignes M2 ter, M4, M3 et placebo ajoutées. Manquent « M1 non concluant » et une zone intermédiaire de M3. La conséquence pour G1 et H2 n'est toujours pas écrite « proposée à Lazar ». Le « contrôle 19 du pari » est cité sans source. |
| CM-11 | à moitié (mineur) | Rapport versé. La docstring du script dit encore « σ_cal » et « Lancement : analyse_fausses_alertes_v1.py ». Rien n'est dit sur le balayage qui enjambe une action invalide, ni sur les sondes corrélées dans « part des sondes ». |

## (2) Le bras M4

- **Codage : correct.** Avec `calibrage_sans_effet=True`, on a `Xcal = X`. La normalisation (μ₀, σ) et les seuils conformes
  sont calculés sur `Xcal`, le quantile par action sur `Xcal[cal_idx]`. L'évaluation se fait sur `Xe = X + τ·σ·u` :
  conformes et Ville sur `Zev = (Xe − μ₀)/σ`, par action sur `Xe`. Aucune fuite.
- **La prédiction est atteinte, mais pour une autre raison que celle annoncée.** À τ = 2, l'effet ajoute à chaque épisode
  évalué un décalage d'écart type 2σ. La variance marginale par action est multipliée par 5 par rapport au calibrage.
  Toute méthode calibrée sur la loi d'origine échoue, que la statistique soit sensible à la dépendance ou non.
  Résultats simulés (partie J, 8 sondes, 4 tirages) :

  | | max conforme | sommes conformes | par action | Ville |
  |---|---|---|---|---|
  | bras codé, r₀ = 0,2 | 0,240 | 0,280 à 0,293 | 0,279 | 0,289 |
  | bras codé, r₀ = 0,8 | 0,240 | 0,222 à 0,242 | 0,238 | 0,315 |
  | variance marginale constante, r₀ = 0,2 | **0,013** | 0,069 à 0,125 | — | — |
  | variance marginale constante, r₀ = 0,8 | 0,038 | 0,051 à 0,054 | — | — |

  La sortie v2 de l'auteur dit la même chose : max conforme 0,23, sommes 0,25 à 0,26, par action 0,27, Ville 0,25.
  « Médiane ≥ 0,15 » sera donc tenue sur presque n'importe quelles données, et « ≤ 0,08 » ne peut pas arriver. Le bras ne
  teste pas A(a)3, c'est-à-dire la dépendance que le calibrage n'a pas vue : à variance marginale constante, le maximum
  reste sous α et les sommes ne montent que si r₀ est faible.
- **Correction** :
  - faire de M4 le bras à variance marginale constante, en évaluation : m + (x − m + τ·σ·u)/√(1 + τ²) ;
  - prédiction conditionnelle à r₀ : sommes ≈ 0,07 à 0,13 à r₀ ≈ 0,2, ≈ α à r₀ ≈ 0,8 ; maximum ≤ α ;
  - garder le bras actuel comme descriptif « dérive d'échelle et de dépendance », sans verdict ;
  - préciser « chacune des cinq statistiques de somme » ou « leur médiane » : le texte est ambigu.

## (3) Corrélation intraclasse `correlation_intra_episode`

Juste. C'est l'analyse de variance à un facteur : CM_inter = SC_inter/(k − 1), CM_intra = SC_intra/(N − k), et le n₀ de
Searle (N − Σnᵢ²/N)/(k − 1). L'estimateur ICC(1) = (CM_inter − CM_intra)/(CM_inter + (n₀ − 1)·CM_intra) est sans biais
visible sur des longueurs de 5 à 10 (partie K, 300 jeux, 60 épisodes) :

| r₀ vrai | 0 | 0,2 | 0,5 | 0,8 |
|---|---|---|---|---|
| moyenne estimée | 0,001 | 0,193 | 0,496 | 0,797 |
| écart type | 0,027 | 0,049 | 0,054 | 0,035 |

Deux réserves mineures :
- Le repli « 0,0 » quand le dénominateur est ≤ 0 n'arrive que pour des scores constants, que `un_passage` arrête ensuite.
  À dire, ou remplacer par une erreur.
- La borne basse naturelle de l'estimateur est −1/(n₀ − 1), pas −1 ; c'est sans effet.

## (4) Partage normalisation / seuils

Conforme. `cal_idx = sorted(setdiff1d(...), key=rang)` suit l'ordre de la permutation. La normalisation prend les 15
premiers épisodes de calibrage dans cet ordre, soit les positions 0 à 16 de la permutation selon le pli (partie L).
Elle reste presque fixe d'un pli à l'autre, mais c'est un sous-ensemble tiré par la graine, sans lien avec les
identifiants : l'échangeabilité entre seuils et évaluation tient.

## (5) `--test-gardes`

Lancé (`/opt/venv-essaim-sim-v1/bin/python -I -B analyse_fausses_alertes_v2.py --test-gardes`). Le cas sain passe, et
chacun des trois artefacts déclenche la bonne garde, avec le bon message :
- NaN sur une action valide : `masque[e_ok, 0]` est vrai, la garde de finitude se déclenche ;
- scores constants : σ = 0 sur la normalisation ;
- K trop petit : E = 30, K = 12, rang 13.

Les quatre cas sont probants. Ce qui n'est pas testé :
- les gardes d'empreinte, d'effectifs et de E < 44 (dans `charger_reel` et `main`) ;
- le cas sain en mode `calibrage_sans_effet`.

Par ailleurs, `test_gardes` tire sa graine par `default_rng(1)` et non par `SeedSequence` (R9, mineur).

## (6) Lectures qui laissent passer un résultat faux

1. **M4 « confirmé », d'où « A(a)3 fondée : le conforme ne protège que de la dépendance que son calibrage a vue »**
   (première ligne de lecture). Ce serait une conclusion causale fausse, confirmée par construction par l'élargissement
   d'échelle (voir (2)). C'est le défaut principal de la v2.
2. **M2 principal est vrai par construction.** Une corrélation injectée ≥ 0,8 donne 0,10 à 0,17 pour tout r₀. Le
   « confirmé » ne dit rien des scores de P3 ; seul M2 ter, à τ = 0, en dit quelque chose. La première ligne doit dire
   « sous un effet épisode injecté (τ = 2) », et réserver « sur P3 » à M2 ter.
3. **Faux échec de M3, qui bloque toute la lecture.** Sous le nul avec K = 39, une sonde seule a P(taux > 0,08) ≈ 0,055 à
   0,075 et P(taux > 0,10) ≤ 0,005 (partie I, 200 jeux). Les sondes réelles sont corrélées entre elles (mêmes épisodes,
   mêmes concepts sur trois couches) : sur 24 cellules, une médiane au-dessus de 0,08 est donc plausible sans aucun
   défaut. Le Seuil la déclare alors « non tenu », et la lecture dit « rien d'autre n'est lu ». À l'inverse, si E < 60,
   le niveau tombe vers 0,03 et une médiane de 1/E < 0,02 sort de la plage par le bas. En outre, le tableau des
   prédictions met l'audit hors de [0 ; 0,10] et le Seuil hors de [0,005 ; 0,10], avec « tenu » sur [0,02 ; 0,08] : rien
   n'est fixé entre les deux. Correction : « tenu » si toutes les médianes sont ≤ 0,10 ; « fragile, rapporté, lecture
   continue » entre 0,08 et 0,10 ou sous 0,02 ; audit au-delà ; plage exprimée par rapport au niveau du manifeste.
4. **Deuxième ligne de lecture.** « Ville tient sur ces scores » est déduit d'un M2 « non concluant ». Écrire plutôt :
   « pas de dépassement établi ».
5. **M2 bis.** La réfutation « ≤ 0 » est fausse à r₀ élevé : à r₀ = 0,8, −0,009 est attendu alors que le mécanisme est
   présent. Supprimer cette réfutation quand r₀ ≥ 0,5, et refaire la table avec le code v2 et au moins 20 tirages, gelée
   avec son chemin et son empreinte.

Fin : 2026-10-27 23:37:28 UTC (`date -u`).
