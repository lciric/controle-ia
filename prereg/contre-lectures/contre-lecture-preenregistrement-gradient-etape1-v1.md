# Contre-lecture (R2) — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes) — v1

- Relecteur neuf : lignée de contre-lecture R2 (ni auteur du brouillon, ni auteur du code). Date (UTC) : 2026-10-24, 19:02.
- Brouillon relu : `essaim-m3-refonte-v1/prereg/brouillon-gradient-etape1-sondes-v1.md`
  empreinte SHA-256 `2b6e5dcb81dc081e20431a092f982ef373960d1317e4c407528cadf5a5ae6f7c` (compagnon vérifié : OK).
- Note du programme citée par le brouillon : `notes/programme-apprentissage-gradient-essaim-v1.md`,
  empreinte `6b4151049ff9…` (annoncée `6b415104…` dans le brouillon : concorde, vérifiée).
- Code lu : branche `outils/essaim-m3-gradient-v1-travail` (contenu des pièces), surtout
  `essaim_m3/noyau/entrainement.py` (`b1020769…`), `serveur.py`, `boucle.py`, `cli.py`, `contrat.py`,
  `bac_a_sable.py`, `taches.py`, `banque.py`, `analyse.py`, `scripts/extraire_activations_v1.py`, `tests/test_noyau.py`.

## VERDICT : **non scellable en l'état**

Deux raisons dirimantes immédiates et trois gaps bloquants :

1. **Le validateur du dépôt refuse le fichier** (rejoué, voir CE-01) : les titres de sections ne sont pas ceux que
   `controle_ia.prereg` exige. Sceller est matériellement impossible maintenant.
2. **L'entraîneur qui exécute l'objectif écrit par l'organisme n'est pas étanche** (CE-02) : en réel il tourne dans le
   processus **root** du noyau, sans abaissement de privilèges, sans isolation réseau, et le garde-fou (expression
   régulière + espace `{"np": np}`) n'est pas une frontière. Les vérités de toutes les parts (dont le test final) sont
   lisibles par ce sous-processus, et la courbe de perte rendue à l'organisme est un canal de retour.
3. Le plan d'analyse de H-G1 sous-estime l'incertitude (bootstrap « par tâche » seul : CE-03), la table de lecture
   gelée manque et la règle de décision est contradictoire (CE-05), et le mécanisme central « vues servies à
   l'organisme » n'est pas codé (CE-04).

Le brouillon redevient **scellable après corrections** une fois CE-01 à CE-05 traités (dont deux exigent du **code**,
pas seulement du texte) et le fichier re-contre-lu. Je recommande une deuxième contre-lecture R2 après correction,
parce que les corrections touchent le fond (étanchéité, statistique, mécanisme).

Décompte : **5 bloquantes, 7 majeures, 5 mineures, 3 de forme**.

---

## Corrections

### Bloquantes

**CE-01 — bloquante — le préenregistrement ne passe pas le validateur `sceller_prereg`.**
Fichier : `prereg/brouillon-gradient-etape1-sondes-v1.md`, titres de sections (l. 17, 35, 44, 60, 66, 80).
Défaut : `controle_ia.prereg.SECTIONS` exige huit sections de niveau 2 aux titres exacts *Hypothèse ; Prédiction
chiffrée et signe attendu ; Métrique ; Seuil ; Plan d'analyse ; Critères de lecture gelés ; Liste d'arrêt ;
Contre-lecture*. Le brouillon a « Hypothèses », « Métriques et seuils », « Plan », « Liste d'arrêt », « Devis… », «
Contre-lecture » — il manque donc **six** sections nommées et il n'y a **pas** de « Critères de lecture gelés ».
Preuve (rejoué, environnement vide, sur une **copie**) :
```
sections trouvées : ['Hypothèses', 'Métriques et seuils', 'Plan', "Liste d'arrêt",
                     'Devis (ordre de grandeur, à confirmer avant GO)', 'Contre-lecture']
PROBLEME : section absente : Hypothèse
PROBLEME : section absente : Prédiction chiffrée et signe attendu
PROBLEME : section absente : Métrique
PROBLEME : section absente : Seuil
PROBLEME : section absente : Plan d'analyse
PROBLEME : section absente : Critères de lecture gelés
PROBLEME : section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport)
REFUS : GardeArret
```
(prereg.py relu empreinte `3b2e3ee5…`, identique à la pièce). C'est exactement le piège signalé dans la consigne
(« des titres de sections renumérotés le faisaient refuser »).
Correction : reprendre les huit titres canoniques du gabarit `gabarit-preregistrement-v1.md`, chacun non vide, et y
répartir le contenu actuel (le « Devis » peut rester en section libre après « Contre-lecture », le validateur ne
l'interdit pas, mais « Seuil » et « Critères de lecture gelés » doivent devenir des sections pleines).

**CE-02 — bloquante — l'exécuteur de l'objectif écrit par l'organisme n'est pas isolé (point 1).**
Fichiers : `essaim_m3/noyau/entrainement.py` l. 73-145 (`PROGRAMME_ENTRAINEMENT`, `exec(compile(spec["objectif"], …),
env)` l. 84 avec `env = {"np": np}` l. 83 ; filtre l. 211), l. 148-157 (`_limites` : RLIMIT seulement, **aucun**
setuid/setgid/unshare), l. 255-258 (`subprocess.run([python, "-I","-B","-s","programme.py"], env=env,
preexec_fn=_limites(...))`) ; `essaim_m3/noyau/boucle.py` l. 261-272 (`_entraineur` crée l'`Entraineur` **sans passer
d'uid**) et l. 383-384 (il est servi dans le fil du serveur, c.-à-d. le processus du noyau) ; `cli.py` l. 106
(mode réel : `os.geteuid() == 0` exigé ⇒ le noyau est **root**).
Défaut : en réel, le sous-processus qui exécute `perte(p, y)` tourne **en root**, dans `travail/noyau/modeles/…` (zone
0700 du noyau), **sans** l'abaissement d'uid ni l'`unshare --mount --pid -n` que `bac_a_sable.executer` applique à
l'organisme. Le seul rempart est (a) une expression régulière sur le **texte source** de l'objectif
(`\b(import|open|exec|eval|__import__|os\.|sys\.|subprocess|socket)\b`) et (b) l'espace d'exécution `{"np": np}`.
Ni l'un ni l'autre n'est une frontière :
- `exec(code, {"np": np})` reçoit automatiquement `__builtins__` complet (vérifié : `exec("x=1", g)` ⇒ `"__builtins__"
  in g` vaut `True`). Toutes les primitives (`open`, `__import__`, parcours de classes) restent donc joignables par
  des tournures qui ne contiennent aucun des mots filtrés (le filtre est purement lexical) ; je **ne** fournis pas de
  chaîne d'évasion.
- même en restant dans `numpy`, `np.load` / `np.fromfile` / `np.save` lisent et écrivent des fichiers et ne sont pas
  filtrés.
Conséquence : le code (écrit par un modèle, donc non fiable) peut lire `racine/banque.json` (0600 root, **toutes** les
vérités, test final compris), le dossier `juge/`, les autres lignées, et renvoyer de l'information à l'organisme par
les valeurs qu'il contrôle (`courbe_perte`, `perte_finale_entrainement`, `exactitude_entrainement`). C'est la question
même du point 1 (« par quels canaux peut-il rendre de l'information ? le filtre suffit-il ? ») : **non**.
Preuve (observation du lancement réel, sans exploit) :
```
lancement du sous-processus d'entraînement : commande ["python","-I","-B","-s","programme.py"],
  options [cwd, env, preexec_fn, stderr, stdout, timeout], user=None, group=None,
  preexec_fn=_limites.<locals>.applique, env=[HOME,LANG,LC_ALL,OMP_NUM_THREADS,OPENBLAS_NUM_THREADS,PATH]
identité du processus du noyau : uid 0 ; capacités : {root:True, utilisateur:True, reseau:True, espaces_noms:True}
commande d'un ORGANISME (comparaison) : ["unshare","--mount","--pid","--fork","--kill-child","--mount-proc","-n","--",
  "python","-I","-B","-s","abaisser.py","60001","60001","python","-I","-B","-s","-u","lanceur.py"]
```
On voit que l'organisme passe par `unshare` + `abaisser.py` (setuid), l'entraîneur non.
Correction : faire tourner le sous-processus d'entraînement sous **le même régime que l'organisme** — abaissement vers
l'uid non privilégié de la lignée, `unshare --mount --pid --fork --kill-child -n`, session neuve — et dans un dossier
qui ne contient **que** `donnees.npz` (traits + vérités des seules tâches d'entraînement demandées) et `spec.json`,
rien du noyau. Réutiliser `bac_a_sable._commande_isolee` / `_changer_proprietaire`. Tant que l'objectif s'exécute dans
la zone de confiance du noyau, aucun filtre d'expression régulière ne rend l'étape 1 étanche.

**CE-03 — bloquante — le bootstrap de H-G1 « par tâche » seul sous-estime l'incertitude (points 3 et R3).**
Fichier : brouillon l. 22-26 (« bootstrap par tâche, 2 000 tirages », « réfutée si la borne supérieure ≤ 0 »).
Défaut : l'unité qui varie d'un bras à l'autre est la **lignée-course** (organisme écrit par une espèce à chaque
amorçage, appels stochastiques), pas la tâche. Un intervalle qui ne rééchantillonne que les tâches (les mêmes pour
toutes les lignées) traite les lignées comme fixes et déclare « confirmé » bien plus souvent que le taux affiché.
Le code d'analyse de la confrontation `essaim_m3/analyse.py` fait, lui, un **bootstrap à deux niveaux** (lignées-graines
puis tâches, l. 11-14, 73-86) — mais il est écrit pour H-E1 (adaptatif contre gelé) et le brouillon ne le cite pas.
Preuve (simulation du relecteur, **non opposable**, R7 ; script
`travail/scripts-relecteur/simuler_plan_h_g1.py`, `SeedSequence(20261024)`, 300 répétitions, test final de la banque :
conscience 18+18, délégation 12+12 ; variance de course σ=0,5 en logit) — taux de « confirmé » (borne basse > 0) sous
effet **nul** :

| unités (lignées) | σ course | A = tâches seules (brouillon) | B = deux niveaux (analyse.py) |
|---|---|---|---|
| 4 | 0,0 | 0,047 | 0,010 |
| 4 | 0,5 | **0,190** | 0,057 |
| 5 | 0,5 | **0,160** | 0,037 |
| 20 | 0,5 | **0,157** | 0,023 |

Dès qu'il y a de la variabilité entre courses, le bootstrap « par tâche » du brouillon confirme à tort ~16-19 % du
temps au lieu de 5 % ; le deux-niveaux reste ≤ 6 %. (Même script : sous un vrai gain de +0,10 par génération, la
puissance tombe aussi, surtout à 4-5 unités — voir CE-07 sur le nombre d'unités.)
Correction : adopter le bootstrap **à deux niveaux** (unités rééchantillonnées, puis tâches stratifiées par famille et
classe, mêmes tâches pour les deux bras d'une paire), fixer l'unité d'analyse (lignée-course), écrire le code
d'analyse propre à H-G1 (ou adapter `analyse.difference_h_e1`) et le passer au **contrôle positif** comme
`verifier_sur_simulation` (CR-18, `analyse.py` l. 148-186) avant le scellement.

**CE-04 — bloquante — les « vues servies à l'organisme » ne sont pas codées (points 2 et 5).**
Fichiers : brouillon l. 50-51 (« le noyau sert plusieurs vues (`spec["vue"]`, à coder) ; l'organisme choisit ») ;
`cli.py` l. 121-125 (`--traits` charge **un seul** `.npz` → un seul dict `id→vecteur`) ; `entrainement.py` (l'`Entraineur`
a un unique `self.traits`) ; `serveur.py` l. 114-121 (`entrainer`/`predire` ne lisent aucune clé « vue ») ;
`scripts/extraire_activations_v1.py` l. 126-130 (écrit **un fichier par vue** `traits-couche{c}-{agg}.npz`).
Défaut : le script produit 5 couches × 2 agrégations = **10** fichiers, mais le noyau n'en charge qu'un et ne sait pas
servir plusieurs vues ; `spec["vue"]` n'est lu nulle part (vérifié : aucune occurrence hors `archive_vue`). Le cœur du
plan — « l'organisme conçoit la couche et l'agrégation, le noyau sert plusieurs vues, l'organisme choisit » — n'existe
pas. R1 interdit de sceller un plan dont le mécanisme central est « à coder ».
Correction : avant le scellement, coder le service multi-vues (le noyau charge les 10 fichiers, expose la liste dans
`contexte["traits"]`, `entrainer`/`predire` prennent `spec["vue"]`, refus si vue inconnue), le tester (cas sain +
artefact R5), puis **geler dans le préenregistrement la liste exacte des vues** et leurs empreintes. Sinon, réduire
explicitement l'étape 1 à **une** vue fixée d'avance (p. ex. couche 16, dernier jeton) et retirer tout le langage «
l'organisme choisit la vue » — mais cela change l'hypothèse (nœud).

**CE-05 — bloquante — pas de « Critères de lecture gelés » et règle de décision de H-G1 incomplète/contradictoire (R1).**
Fichier : brouillon l. 22-26 (H-G1), l. 35-42 (métriques et seuils).
Défaut : R1 exige une table « issue observée → verdict (confirmé / réfuté / non concluant) » gelée d'avance ; elle est
absente (et le validateur réclame la section, CE-01). La règle énoncée est en outre incohérente : « signe attendu
positif ; ordre de grandeur ≥ +0,10 ; réfutée si la borne **supérieure** ≤ 0 ; non concluante si l'intervalle couvre
0 » ne dit **jamais** ce qui vaut « confirmé », et le seuil +0,10 n'entre dans aucune décision. Tel quel, un effet
réel mais petit (p. ex. +0,04, intervalle [0,01 ; 0,07]) n'est ni confirmé, ni réfuté, ni « couvrant 0 » : trou.
Correction : écrire la table gelée, sur le modèle de `analyse.lecture_h_e1` (l. 92-106) : *confirmé* si borne basse >
0 **et** différence ≥ +0,10 ; *réfuté* si borne haute < +0,10 (effet prédit exclu), en distinguant « effet positif
plus petit que prédit » ; *non concluant* sinon, **sans relance sans nouveau préenregistrement**. Fixer aussi le
traitement d'une lignée coupée/invalidée (combien invalident la lecture).

### Majeures

**CE-06 — majeure — l'appariement « même organisme » des deux bras n'est ni décrit ni proprement outillé (point 3).**
Fichiers : brouillon l. 22-24, l. 52-55 ; `cli.py` l. 53-64 (`--depuis` **exige** `--gel`), `boucle.py` l. 349-373,
445-446 (`--gel` vide l'historique et l'archive vue).
Défaut : H-G1 veut « la même lignée » avec et sans gradient. Sans `--depuis`, chaque bras ré-amorce (appels de modèle
réels, sans température, donc **non déterministes**) : les organismes g0 diffèrent, ce n'est pas « le même ». Avec
`--depuis` on fige bien les mêmes g0, mais `--depuis` force `--gel`, qui supprime **aussi** l'historique et la mémoire
entre générations : le bras « sans gradient » diffère alors du bras « avec gradient » par **deux** choses à la fois
(pas de gradient *et* pas de mémoire), ce qui confond H-G1 et contredit H-G3 (« apprentissage de la conception entre
générations »). « Même graine » (l. 24) ne rend pas l'amorçage déterministe : la graine ne pilote que l'ordre des
tâches, pas la réponse des modèles.
Correction : décider et écrire la procédure d'appariement. Option propre : un drapeau qui relance les **mêmes** g0
(comme `--depuis`) en ne changeant **que** `entrainements_max` (donc `traits.disponibles`), **sans** vider l'historique.
À coder et tester (R5) avant le scellement ; sinon requalifier H-G1 en comparaison entre lignées non appariées et
revoir la puissance en conséquence.

**CE-07 — majeure — budget par génération incohérent : il tronque l'expérience (point 4).**
Fichiers : brouillon l. 54 (« 900 s », « 10 entraînements de ≤ 5 000 pas, 120 s chacun ») ; `entrainement.py` l. 34
(`DELAI_S_DEFAUT = 120`), `boucle.py` l. 270 (`_entraineur` ne passe pas `delai_s` → 120 s par entraînement) ;
`serveur.py` l. 114-117 (l'entraînement est servi **synchrone** dans le fil du serveur : l'appel client de l'organisme
bloque jusqu'à la fin).
Défaut : 10 entraînements × jusqu'à 120 s = **1 200 s** d'entraînement possible, mais la paroi du bac à sable de
l'organisme est `temps_max_s = 900 s`. L'organisme ne peut pas dépenser son budget d'entraînements dans sa paroi, et
le temps d'entraînement est en concurrence avec le temps des appels d'espèces. Lazar accepte le coût du calcul quel
qu'il soit (message du 24 octobre, 18:22-18:30 UTC, `messages-lazar-session-2026-10-24-v1.md`) : un budget qui coupe
l'expérience est un défaut, pas une économie.
Ordre de grandeur mesuré de l'entraîneur à d = 4 096, 80 tâches, 5 000 pas (script
`travail/scripts-relecteur/chronometrer_entraineur.py`, non opposable) : linéaire ≈ 5 s ; une couche cache 16 ≈ 8 s ;
cache 256 ≈ **50 s**. Le gradient par différences finies coûte ~2·lot évaluations de `perte` par pas (l. 114-120),
donc une perte lourde ou un gros `cache` peut atteindre les 120 s.
Correction : rendre `temps_max_s` cohérent avec `entrainements_max × delai` (ou servir l'entraînement hors de la paroi
de l'organisme, ou compter le temps d'entraînement à part), et fixer ces bornes dans le préenregistrement après calcul
du pire cas. Côté appels (prix transcrits, non opposables R7) : lire une fois les 120 tâches de test coûte ≈ 0,8-2 USD
par lignée selon l'espèce ; sous la réservation au **pire cas** (`cout_pire_cas`, `appels.py` l. 135-141) avec
`max_tokens` par défaut 4 096 (`serveur.py` l. 21), un lot de 8 tâches réserve ≈ 0,3-0,7 USD, soit ~7 à 36 lots « en
vol » simultanés sous 5 USD : la borne pratique est le nombre d'appels (60) et le temps, pas les 5 USD.

**CE-08 — majeure — périmètre des lignées : version périmée et lignée manquante (point 5).**
Fichiers : brouillon l. 52-53 ; `lignees-imposees/gemini-organisme-v3-LISEZMOI-v1.md`,
`enveloppe-essaim-gemini-v3-LISEZMOI-v3.md` ; `decisions-lazar-2026-10-24-v1.md` l. 23-24 (« étape 1 toutes les
lignées » : « oui ») ; `notes/comparaison-conception-trois-organismes-v1.md` l. 118-123 (cinq lignées).
Défaut : le brouillon prévoit « les trois auto-écrites + `gemini-organisme-v2` si livré » = 4. Or (a) une **v3** de
l'organisme écrit par Gemini existe (`gemini-organisme-v3`, correction C-11 des étiquettes ; la v2 était invalide sous
la règle du noyau) ; (b) la **lignée d'enveloppe de l'essaim de Gemini** (`enveloppe-essaim-gemini-v3`) est une
cinquième lignée candidate ; (c) Lazar a dit « étape 1 **toutes** les lignées ». Le brouillon cite donc une version
périmée et omet une lignée.
Correction : lister explicitement les lignées de l'étape 1 (trois auto-écrites + `gemini-organisme-v3` +
`enveloppe-essaim-gemini-v3`), fixer leurs chemins, familles déclarées et empreintes d'arbre, ou justifier toute
exclusion comme nœud soumis à Lazar. Attention : ces deux lignées imposées « ignoreront sans doute `entrainer` » (elles
n'ont pas été écrites pour le contrat v3) — à dire, et à décider si elles comptent dans H-G1 (appariable seulement si
elles appellent `entrainer`).

**CE-09 — majeure — l'extraction tronque par la tête et jette la queue que la banque avait gardée ; troncatures mal consignées (point 2).**
Fichier : `scripts/extraire_activations_v1.py` l. 106-111 (`texte_tok = tok(texte)[: max(16, max_jetons - len(prefixe)
- 64)]` garde le **début** et coupe la **fin**), l. 116-123 (`debut_texte = min(len(prefixe), T-1)` ; « moyenne » =
`h[debut_texte:].mean(0)`), l. 118 (`jetons_par_tache` = nombre total de jetons seulement).
Défaut : la banque scellée borne déjà chaque texte à 20 000 caractères en gardant **15 000 au début + 5 000 à la fin**
(`banque/LISEZMOI-v3.md` l. 30-34), justement parce qu'un indice peut être en fin de texte. L'extraction à 2 048
jetons re-tronque ensuite **par la queue**, supprimant ces 5 000 derniers caractères préservés. D'après
`resume-banque-confrontation-v1.md`, ~14-18 items « conscience-évaluation » par part dépassent 7 000 caractères (≈ 2 048
jetons) : ils seront tronqués, et l'agrégation « moyenne » ne portera que sur la tête. De plus le manifeste n'enregistre
**ni** le nombre de jetons d'origine **ni** un drapeau « tronqué » par tâche : on ne peut pas savoir après coup quelles
tâches ont perdu leur fin (le point 2 demande « enregistrement des troncatures »).
Correction : décider la politique de troncature (tête+queue comme la banque, ou tête seule assumée) et la **fixer dans
le préenregistrement** ; consigner dans le manifeste, par tâche, la longueur d'origine, le nombre de jetons et un
drapeau de troncature (et, pour « moyenne », les positions réellement couvertes). Monter `--max-jetons` si Lazar
accepte le coût (CE-07) pour éviter de couper les items longs.

**CE-10 — majeure — révision du modèle non figée ; manifeste d'extraction incomplet pour R9.**
Fichier : `scripts/extraire_activations_v1.py` l. 63 (`--revision default=None`), l. 93-94
(`from_pretrained(revision=args.revision)`), l. 75-79 (manifeste) ; brouillon l. 48 (« révision fixée dans le
manifeste »).
Défaut : le défaut `None` vaut « branche `main` » du dépôt du modèle — cible mobile. Le brouillon affirme « révision
fixée » mais ne donne **aucune valeur** et le code enregistrerait `null`. Le manifeste d'extraction n'inscrit ni les
versions de `numpy`/`torch`/`transformers`, ni le commit du code, ni de graine (R9 demande « versions, graines,
commit » ; la banque, elle, fige bien la révision du **jeu de données** `5d724f12…`). L'extraction est déterministe,
mais la reproductibilité du modèle n'est pas garantie.
Correction : fixer une révision de modèle explicite (empreinte de commit Hugging Face) dans le préenregistrement et la
passer au script ; refuser `--revision None` ; ajouter au manifeste les versions des bibliothèques, le commit du code
et le type de nombre effectif.

**CE-11 — majeure — empreintes et commit porteurs laissés en blanc dans le brouillon (R1, R6).**
Fichier : brouillon l. 9-13 (« commit fixé au scellement », « la banque (nom et empreinte fixés au scellement) », «
les traits extraits (manifeste, empreintes) »).
Défaut : R1/R6 veulent la métrique, le seuil, le plan et **toutes** les pièces gelés avec leurs empreintes avant la
lecture. Le brouillon laisse à remplir : commit du code, nom + empreinte de la banque (`banque-confrontation-v1.json` =
`f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`, déjà connue — à inscrire), empreinte du fichier de
traits et de son manifeste (qui n'existe pas encore : l'extraction doit précéder le scellement, ou le préenregistrement
geler la **procédure** d'extraction et son script, empreinte `e85313d8…`, à défaut du produit).
Correction : avant le scellement, renseigner le commit, l'empreinte de la banque, et soit l'empreinte des traits (si
l'extraction est faite avant), soit l'empreinte du script d'extraction + les paramètres gelés (vues, max-jetons,
révision) avec la règle « le préenregistrement est amendé d'un addendum scellé portant l'empreinte des traits dès
qu'ils sont produits, avant toute lecture ».

**CE-12 — majeure — la liste d'arrêt mêle gardes automatiques et invalidations manuelles, non testées comme l'exige R5 (point 3).**
Fichier : brouillon l. 60-64 ; `entrainement.py` l. 187-229 (validation → `REFUSE`), l. 281-299 (`predire` rend une
liste `absents`, **sans** invalider) ; `tests/test_noyau.py` l. 733-763 (la vue ne contient ni
`journal-entrainements.jsonl` ni `modele.npz` : testé).
Défaut : certaines entrées sont des gardes codées et testées (spec qui désigne une tâche de test → `REFUSE`, testé l.
709 ; absence de traits en réel → `Arret`, testé l. 765-774 `test_gradient_en_reel_exige_des_traits`), d'autres sont
des invalidations **manuelles** sans garde (« fuite des vérités : fichier `donnees.npz` hors du dossier du noyau »,
« `archive_vue` contenant `juge/` ») et une est molle : « traits absents pour une tâche » est, à la prédiction, une
simple liste `absents`, pas une invalidation. R5 veut chaque garde testée sur un cas sain **et** un artefact, et aucun
repli silencieux.
Correction : pour chaque ligne de la liste d'arrêt, dire si c'est une garde automatique (et pointer son test sain +
artefact) ou une vérification humaine post-run (et comment elle est faite) ; transformer « traits absents » en
condition explicite (refus d'entraîner, et invalidation de la lecture si une tâche de test n'a pas de trait) et
l'ajouter aux tests.

### Mineures

**CE-13 — mineure — « à confirmer par Lazar » est périmé.**
Fichier : brouillon l. 14-15 (« run décisif exigé … à confirmer par Lazar (§ 0 de la note) »).
Défaut : Lazar a déjà confirmé la lecture « run décisif exigé » le 24 octobre à 18:39 (« ok »), transcrit dans
`decisions-lazar-2026-10-24-v1.md` l. 24 et `extrait-registres-v1.md` R-344 (3). La réserve n'a plus lieu d'être.
Correction : remplacer par la citation de la décision (R-344, 18:39) et retirer « à confirmer ».

**CE-14 — mineure — section « Métriques et seuils » mélange H-G1 (avec seuil) et H-G2/H-G3 (descriptives) ; unité ambiguë.**
Fichier : brouillon l. 37-42.
Défaut : « exactitude équilibrée par famille, moyenne (dev rendu, final témoin) » laisse croire que H-G1 se lit sur une
moyenne dev+final, alors que H-G1 parle du « test final caché ». Le mélange seuil/descriptif dans une même section
brouille ce qui est gelé.
Correction : après CE-01, mettre dans « Métrique » la définition unique de la statistique de H-G1 (différence de
l'exactitude équilibrée **sur le test final**, par famille puis moyenne, l'unité étant la lignée-course), et renvoyer
H-G2/H-G3 (descriptives) à un paragraphe clairement « sans seuil ».

**CE-15 — mineure — la graine d'entraînement est choisie par l'organisme (R9).**
Fichier : `entrainement.py` l. 82 (`default_rng(int(algo.get("graine", 0)))`).
Défaut : la graine de la descente de gradient vient de la spec de l'organisme (défaut 0), elle n'est pas dérivée par
`SeedSequence` du manifeste de run ; elle est tracée seulement via l'empreinte de la spec (l. 275). C'est défendable
(c'est un paramètre de conception de l'organisme) mais à dire explicitement dans le plan pour ne pas laisser croire à
une dérivation R9.
Correction : noter dans le plan que la graine du modèle est un choix de l'organisme, journalisé par `sha256_spec`, et
distinct des graines expérimentales (ordres de tâches), elles dérivées par `SeedSequence` (`boucle.py` l. 138-144).

**CE-16 — mineure — la sonde témoin « longueur seule » (audit R4) n'est pas outillée.**
Fichier : brouillon l. 41-42 (« une sonde témoin “longueur seule” est rapportée »).
Défaut : aucune pièce ne produit cette sonde. La banque a bien une référence de **traits de surface du texte**
(`banque.py` l. 231-255, `reference_traits_texte`, testée l. 1015), mais pas une sonde « longueur seule » sur les
activations.
Correction : soit renvoyer explicitement à `reference_traits_texte` comme référence de surface (et retirer « longueur
seule »), soit coder et tester la sonde « longueur seule » avant le scellement.

**CE-17 — mineure — les « deux sondes témoins que le noyau entraîne lui-même » (H-G2) n'ont pas de chemin de code.**
Fichier : brouillon l. 27-30, 56 ; `entrainement.py` (l'`Entraineur` est par lignée) ; `boucle.py` l. 261-272.
Défaut : H-G2 prévoit des sondes témoins entraînées par le noyau **hors lignées** (Brier et score logarithmique borné,
1 000 pas, etc.), mais rien dans le noyau ne les entraîne en dehors du service aux organismes.
Correction : coder un petit pilote témoin (réutilisant `Entraineur` avec des specs gelées) et le tester, ou requalifier
H-G2 en analyse descriptive post-run exécutée par un script d'analyse scellé.

### Forme

**CE-18 — forme — titres de sections (découle de CE-01).** Reprendre exactement les huit intitulés du gabarit ; ne pas
réordonner ni fusionner les sections exigées.

**CE-19 — forme — section « Contre-lecture » sans ses deux empreintes.**
Fichier : brouillon l. 80-85. Le validateur exige, dans « Contre-lecture », l'empreinte du **brouillon relu** et celle
du **rapport** de contre-lecture (`prereg.py` l. 48-56). La section actuelle n'en porte aucune.
Correction : y inscrire l'empreinte du brouillon (`2b6e5dcb…`) et celle du présent rapport (voir compagnon `.sha256`),
avec le traitement accepté/refusé de chaque CE.

**CE-20 — forme — le « Devis » entre en tension avec le GO sans devis de Lazar.**
Fichier : brouillon l. 66-78 ; `messages-lazar-session-2026-10-24-v1.md` l. 5-6 (« j'accepte le cout du calcul
quelquil soit lance le j'ai pas besoin du devis pour cette etape »).
Défaut : le brouillon présente un devis « ≈ 70 USD (plafond demandé 90) » comme s'il conditionnait le GO, alors que
Lazar a donné le GO de calcul de l'étape 1 **sans devis**. Le devis reste utile comme information, mais ne doit pas se
présenter comme la porte de dépense.
Correction : garder le devis en annexe informative (R7 : non opposable) et dire que le GO de calcul de l'étape 1 est
acquis sans devis (message du 24 octobre), l'identifiant de GO « calcul » à inscrire dans `registres/go.md` restant la
condition que vérifie la garde (`boucle.py` l. 107-113 : extrait du registre + type « calcul »).

---

## Réponses aux six points à examiner

**1. Étanchéité de l'entraîneur.** Insuffisante — c'est **CE-02** (bloquante). Qui exécute l'objectif : le noyau, en
**root** en mode réel (`cli.py` l. 106), dans un sous-processus `python -I -B -s` **sans** abaissement d'uid ni
`unshare` (contrairement à l'organisme), dans sa propre zone 0700. Ce qu'il peut lire : tout ce que root lit, dont
`banque.json` (vérités de train/test/**test final**), le `juge/`, les autres lignées. Canaux de retour vers
l'organisme : `courbe_perte`, `perte_finale_entrainement`, `exactitude_entrainement` (valeurs calculées par le code de
l'organisme), et `predire` (probabilités sur toute tâche). Le filtre par expression régulière **ne suffit pas** : il
est lexical, `__builtins__` est présent dans l'espace d'exécution (vérifié de façon inoffensive), et `np.load` /
`np.fromfile` / `np.save` ne sont pas filtrés. Je n'ai **pas** écrit de voie d'évasion ; la démonstration est au niveau
de la conception (observation du lancement réel du sous-processus, sans privilèges abaissés ni réseau coupé).

**2. Extraction des traits.** Troncature : le script coupe par la **tête-conservée/queue-jetée** (l. 106-111) et
supprime les 5 000 derniers caractères que la banque gardait exprès → **CE-09**. Agrégations : « dernier » = dernier
jeton (y compris l'invite de génération) ; « moyenne » = de la fin du préfixe système à la fin (`debut_texte`), donc
sur le texte tronqué seulement. Révision : `--revision None` par défaut, cible mobile → **CE-10**. Troncatures non
consignées par tâche → CE-09/CE-10. Lecture des seules clés `id` et `texte` : **oui**, conforme (`charger_taches`
l. 46-55, « jamais la vérité » l. 51 ; vérifié). Formes/noms vs `cli.py` : le script écrit **un `.npz` par vue** (10
fichiers), `cli.py --traits` n'en charge **qu'un** et ne gère pas plusieurs vues → **CE-04**.

**3. Plan d'analyse de H-G1.** Appariement « même organisme » : non outillé proprement (`--depuis` force `--gel` qui
vide aussi l'historique) → **CE-06**. Unité d'analyse et puissance : l'unité devrait être la lignée-course ; le
brouillon ne fixe ni le nombre de courses/graines ni la puissance ; avec 4-5 unités et une seule graine, la puissance
est faible (simulation CE-03). Bootstrap par tâche : **sous-estime l'incertitude** → **CE-03** (le deux-niveaux de
`analyse.py` existe mais n'est pas cité). Une seule comparaison principale : annoncée (l. 39) — bien. Critères de
lecture gelés : **absents** et règle contradictoire → **CE-05**. Liste d'arrêt testée sain+artefact : partiellement
seulement → **CE-12**.

**4. Budgets par génération.** Incohérence bloquant l'expérience : `temps_max_s = 900 s` < 10 × 120 s d'entraînement →
**CE-07**. Réservation au pire cas (`cout_pire_cas`, `appels.py` l. 135-141, `max_tokens` défaut 4 096) : sous 5 USD,
~7 à 36 lots « en vol » selon l'espèce (prix transcrits, non opposables) ; la borne réelle est le nombre d'appels
(60) et le temps, pas les dollars. Combien d'appels tiennent : lire une fois les 120 tâches de test ≈ 0,8-2 USD par
lignée — largement sous 5 USD, mais 60 appels/génération est serré si l'organisme veut lots + recherches +
entraînements dans 900 s. Lazar accepte le coût (message du 24 octobre) : les bornes doivent être dimensionnées pour
**ne pas** tronquer, pas pour économiser.

**5. Lignées.** « Toutes les lignées » (Lazar, 18:39) = 3 auto-écrites + `gemini-organisme-v3` +
`enveloppe-essaim-gemini-v3` ; le brouillon cite `gemini-organisme-v2` (périmé) et omet l'enveloppe → **CE-08**.
Banque et empreinte à fixer (`f1387a20…`, connue) → **CE-11**. « À coder » avant le scellement : le service multi-vues
`spec["vue"]` → **CE-04** ; l'appariement des bras → **CE-06** ; les sondes témoins → **CE-16/CE-17**.

**6. Reste (R1-R14).** R1 : sections et pièces incomplètes → CE-01, CE-05, CE-11. R2 : la section Contre-lecture doit
porter les deux empreintes → CE-19 (le présent rapport exécute R2). R3 : « run décisif exigé » est une lecture
acceptée par Lazar (R-344 (3)) et compatible avec R3 ; mais un plan dont le taux d'erreur réel dépasse l'annoncé
(CE-03) heurte l'esprit de R3 — à corriger. R4 : l'audit de symétrie est prévu (l. 40-42) mais la sonde témoin
« longueur seule » n'existe pas → CE-16 ; bien pensé de prévoir l'audit si une sonde dépasse 0,95 **ou** tombe sous
0,30 (symétrie). R6 : empreintes manquantes → CE-11. R9 : graines expérimentales par `SeedSequence` (`boucle.py`
l. 138-144) — bien ; mais la graine d'entraînement est choisie par l'organisme (CE-15) et le manifeste d'extraction
manque versions/commit (CE-10). R10 : sans objet ici (pas de lancement d'instance dans le préenregistrement lui-même).
R12/R13 : versionnage respecté ; le verdict de porte R13 viendra d'un sous-agent neuf si l'étape sert de porte.
Provenance des décisions de Lazar : les messages cités (18:22, 18:23) concordent avec `decisions-lazar-2026-10-24-v1.md`
(l. 22-23) et `messages-lazar-session-2026-10-24-v1.md` ; le GO de calcul sans devis est bien dans les messages du
24 octobre (CE-20). Aucun chiffre non vérifié trouvé dans le brouillon **sauf** les ordres de grandeur du devis, qui se
disent eux-mêmes non opposables.

---

## Ce que j'ai rejoué (commandes, résultats)

Tout dans un environnement vide (`env -i PATH=/usr/bin:/bin HOME=<travail>`), `python3 -B`, sur des **copies** ; aucune
écriture dans les pièces ni dans le dépôt ; aucun appel réseau ; aucun exploit.

1. **Empreintes.** Vérifié les compagnons `.sha256` des pièces (tous OK sauf le fichier de banque, volontairement
   absent) ; brouillon = `2b6e5dcb…` (concorde avec l'empreinte attendue) ; note = `6b415104…` (concorde) ; `prereg.py`
   copié = `3b2e3ee5…` identique à la pièce. Le code diffère des listes `EMPREINTES-*.txt` pour les fichiers attendus
   (noyau modifié pour le gradient) ; les 38 fichiers présents de `EMPREINTES-gradient-v1.txt` qui pouvaient être lus
   sont OK, les manques sont les organismes et données retirés exprès.
2. **Validateur** (`controle_ia.prereg` rejoué avec des bouchons `gardes`/`scellement` inoffensifs) : **REFUS**
   (`GardeArret`), six sections exigées absentes + Contre-lecture sans empreintes (sortie dans CE-01). C'est la preuve
   de CE-01.
3. **Tests de l'entraîneur** rejoués à l'identique (source extraite par `ast` de `tests/test_noyau.py`) :
   `test_entraineur_sonde_sain_et_artefacts` **PASSE** (1,0 s), `test_entraineur_une_couche_et_perte_logarithmique`
   **PASSE** (1,2 s). Avec un bouchon de collisionneur (interface seule, prix transcrits) et un bouchon `pytest` :
   `test_boucle_organisme_sonde_apprend_sous_le_noyau` **PASSE**, `test_gradient_en_reel_exige_des_traits` **PASSE**,
   `test_organisme_fuite_…` **PASSE** (root disponible), `test_metrique_qui_lit_la_banque_est_non_calculee` **PASSE**,
   `test_bras_gele_apparie_…` **PASSE**, `test_analyse_controle_positif_et_lecture` **PASSE**. Le code livré se tient ;
   les défauts sont de conception/plan, pas des régressions de test.
4. **Lancement de l'entraîneur observé** (enveloppe de `subprocess.run`) : commande `python -I -B -s programme.py`,
   `user=None`, `preexec_fn=_limites` (RLIMIT seulement), **pas** d'`unshare`, à comparer à la commande d'un organisme
   (`unshare … abaisser.py <uid>`). Processus noyau : uid 0. Preuve de CE-02 (sans exploit). Vérifié aussi, de façon
   inoffensive, que `exec(code, {"np": np})` reçoit `__builtins__`.
5. **Durée de l'entraîneur** à d = 4 096, 80 tâches, 5 000 pas : linéaire ≈ 5 s ; une couche cache 16 ≈ 8 s ; cache
   256 ≈ 50 s. Appuie CE-07.
6. **Simulation du plan H-G1** (`simuler_plan_h_g1.py`, `SeedSequence(20261024)`, 300 répétitions) : taux de « confirmé »
   sous effet nul — bootstrap par tâche 0,16-0,19 contre deux-niveaux 0,02-0,06 dès qu'il y a de la variance de course.
   Preuve de CE-03 (non opposable, R7).
7. **Ordres de grandeur de budget** (`budget_ordre_de_grandeur.py`, prix transcrits non opposables) : chiffres repris
   dans CE-07 et au point 4.

Scripts et sorties du relecteur : `…/scratchpad/r2-etape1-v1/travail/scripts-relecteur/` et fichiers `sortie-*.txt`.

## Ce que je n'ai pas pu vérifier

- **Le modèle réel.** Pas de GPU, pas de Llama-3.1-8B, pas de jeton (et interdit) : le script d'extraction n'a été lu
  que statiquement ; les longueurs de jetons réelles, la position exacte du texte dans le gabarit de dialogue et le
  comportement de `apply_chat_template` ne sont pas mesurés. L'équivalence « 7 000 caractères ≈ 2 048 jetons » du
  résumé de banque n'est pas mesurée (le résumé le dit aussi).
- **La banque elle-même.** Seuls les comptes agrégés et la documentation sont fournis (pas les textes ni les vérités) :
  je n'ai pas pu vérifier les longueurs par tâche, l'équilibre fin, ni rejouer la référence de surface (0,69 / 0,50).
  J'ai pris `resume-banque-confrontation-v1.md` et `banque/LISEZMOI-v3.md` pour argent comptant.
- **Le collisionneur v2.5** (absent des pièces) : j'ai utilisé un bouchon d'interface avec des prix **transcrits** du
  brouillon de confrontation v3 (non opposables, R7) ; les vrais prix, `cout_pire_cas` et `modele_conforme` ne sont pas
  vérifiés. Tout chiffre de coût est un ordre de grandeur.
- **Les tests dépendant d'organismes retirés** (relève de Gemini, données) : non rejoués, comme annoncé par la
  consigne ; ce n'est pas un défaut du code.
- **Les organismes imposés v3** (`gemini-organisme-v3`, `enveloppe-essaim-gemini-v3`) : seule la documentation est
  fournie ; je n'ai pas lu leur code (hors périmètre des pièces) et n'ai pas vérifié s'ils appellent `entrainer`.
- **La simulation de puissance** repose sur un modèle du relecteur (variance de course en logit, base 0,65) dont les
  paramètres sont des hypothèses dites, non calibrées sur des données réelles : elle établit la **direction** du
  problème (bootstrap par tâche trop optimiste), pas des chiffres opposables.
