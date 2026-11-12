# Contre-lecture du script de puissance de la garde δ — v3

Contre-lecteur neuf (règle R2). Je n'ai écrit ni le script, ni le rapport, ni les contre-lectures précédentes.
29 octobre 2026, de 04:58 à 05:18 UTC (`date -u`). Processeur seul, aucun réseau, aucune dépense. Rien n'a été écrit
dans l'arbre v41 ni dans `source/`.

## Verdict

**Utilisable après corrections.**

- Le cœur est juste. La fiche simulée est celle de `pari_apparie.evaluer` (v41), longueurs de garde et de contraste
  différentes comprises : 1 000 fiches, écart maximal 7,1·10⁻¹⁵, aucun instant d'arrêt différent. Le « prolongement par
  la dernière valeur » est exactement ce que fait le pôle.
- Les chiffres du rapport se reproduisent à l'identique (même graine). À graine neuve, ils tiennent (voir Q3).
- Un point empêche de citer la lecture « effet d'unité » au préenregistrement (GD3-01, majeur). L'effet d'unité du
  script déplace l'espérance de A (écrêtage à 0) : à τ = 0,01 et σ = 0,05, E[f_A] passe de 0,010 à 0,025. La chute de
  la garde (0,89 → 0,014) est un biais de 0,015, pas le lien garde-contraste de GD2-02. À espérance tenue, le même effet
  donne 0,86, et le lien garde-contraste change la fiche de moins de 0,01.
- Pour le fichier réel, le script n'est pas encore prêt (GD3-02, moyen). Il exige le même ensemble d'unités pour la
  garde et le contraste, et interdit toute colonne d'identifiant. La spécification v2 (et le pôle) donnent deux
  ensembles différents : unités à épisode honnête, unités à épisode saboté.
- Restent des replis silencieux d'options (GD3-03) et des points mineurs.

Sources relues. `sha256sum -c` donne « OK » pour les sept fichiers de `source/` (script `7b636c1e…`, sortie
`bed0050d…`, effet d'unité `5d22b2bd…`, indépendants `dfeff845…`, rapport `e45d64ce…`, journal `e3b0c442…`
(vide), manifeste `c64e4ac8…`). Pôle : `pole/pari_apparie.py` `ec6c2cf6…`, conforme à
`EMPREINTES-orchestrateur-pole-v7-v41.txt`. Copies conformes dans `cl/outils/copie_script/` et `cl/outils/copie_pole/`.
Environnement : Python 3.13.17 (auteur : 3.13.18), numpy 2.5.3.

## Réponses aux sept questions

### 1. GD2-01 à GD2-11

Voir la table plus bas. 5 corrigés (GD2-01 en grande partie, 04, 06, 07, 08), 6 en partie (GD2-02, 03, 05, 09, 10,
11). Aucun ignoré.

### 2. La fiche simulée est-elle celle du pôle ? (démontré, `verif_fiche_pole.py`)

Oui. 1 000 essais. Chaque essai tire g et v par la loi du script, puis calcule la fiche deux fois : par `processus` du
script (minimum, première atteinte de m/α), et par `evaluer({B_j: v_j}, {B_j: g_j}, δ, α, m)` du pôle.
- 800 essais synthétiques : partagé ou indépendants, effet d'unité 0 ; 0,05 ; 0,2, K ∈ {3 ; 10}, τ ∈ {0 ; 0,01 ;
  0,10}, biais ∈ {0 ; 0,025}, k = 1 à 3, δ ∈ {0,05 ; 0,10 ; 0,20}, m ∈ {1 ; 8}, α ∈ {0,05 ; 0,01} ;
- 200 essais sur loi réelle (fichiers fabriqués, écarts −1 et +1 compris), brute ou recentrée ;
- 495 essais avec n_garde ≠ n (dans les deux sens).

Résultats : écart maximal sur la trajectoire du minimum 7,1·10⁻¹⁵ ; même longueur de trajectoire partout ; 0 instant
d'arrêt différent ; 0 seuil différent ; 243 fiches promues, dont 114 à longueurs différentes.

Le pôle (`evaluer`, l. 210-222) lit `traj[min(t, n − 1)]` et `g[min(t, len(g) − 1)]` jusqu'à `max(n, len(g))` : chaque
processus garde sa dernière valeur. `prolonger` du script fait la même chose. GD2-08 est corrigé côté calcul.

Deux limites, hors du calcul :
- « Sujet partagé = structure du pôle » repose sur `engagement_apparie.evaluer`, que la contre-lecture v2 a lu. Je ne
  l'ai pas relu (consigne : rien d'autre que `pari_apparie.py`).
- Dans le pôle, l'unité t de la garde et l'unité t du contraste sont le t-ième honnête et le t-ième saboté dans l'ordre
  secret : ce ne sont pas forcément la même unité. Le script synthétique les aligne (même u pour les deux sous l'effet
  d'unité). C'est une hypothèse de modèle, sans effet quand l'effet d'unité est nul.

### 3. Reproduction (démontré, `comparer_sorties.py`, `verif_rapport.py`)

**Même graine** (commandes du manifeste, avec `--repetitions 4000`) : les trois sorties sont identiques champ par champ,
hors `commit`, `etat_du_script` et `environnement` (5 953, 1 193 et 233 champs, 0 différence).

**Graine neuve 918273645** (mêmes commandes) :
- 1 310 parts diffèrent, d'au plus 0,033 (cellule K = 3, τ = 0,01, biais 0,0125, k = 3, seuil 20) ;
- tableau principal (160 unités, seuil 160) : chaque case à 0,02 près. Exemples : K = 10, τ = 0,01, δ = 0,05, fiche
  k = 3 0,749 contre 0,738 ; K = 3, τ = 0,01, fiche k = 3 0,069 contre 0,069 ; K = 3, τ = 0,10, fiche k = 3 0,006 contre
  0,008 ;
- indépendants contre partagé (k = 3, δ = 0,05) : 0,66 / 0,08 / 0,013 / 0,0003 contre 0,75 / 0,20 / 0,07 / 0,007 ;
- effet d'unité : garde 0,89 → 0,008, fiche 0,75 → 0,002 ; δ = 0,10 : 0,95 → 0,94 ;
- biais : 0,89 → 0,03 → 0,00 ; 400 unités : 1,00 → 1,00 → 0,95 ; K = 3, τ = 0,10, δ = 0,10 : 0,95 → 0,82 → 0,59 ;
- seuil 20 : 1,00 / 0,83 / 0,46 / 0,13 et 0,40 / 0,30 / 0,07 / 0,03 ;
- artefacts : frontière ≤ 0,004 au seuil 160 (borne 0,00625), ≤ 0,028 au seuil 20 (borne 0,05) ; tricheur ≤ 0,0005 ;
- n₈₀ : 53 sur 144 changent, d'au plus 3,8 % ; tous les 53 sortent du `pas_de_la_dichotomie` de l'auteur, ce qui est
  attendu (le champ ne se dit plus intervalle) ; la note « ≈ 6 % » est prudente.

**Rapport contre sorties** (`verif_rapport_auteur.json`). Tous les chiffres du § 2 sont dans les sorties de l'auteur,
à l'arrondi près : tableau des huit lois, 64 et 400 unités, indépendants, effet d'unité, biais, n₈₀ (24 plages),
seuil 20, artefacts, 216 cellules, 672 s. Une plage est inexacte : « contrastes seuls 0,08 à 0,12 » (sortie : 0,068 à
0,124). Phrases non soutenues :
- l'attribution de l'effet d'unité à la dépendance (§ 2, lectures 3 et 4 : GD3-01) ;
- « ce qui limite dépend de K » et « à K = 3 le contraste limite plus » (lecture 2 : GD3-06) ;
- « δ = 0,10 y résiste sous la loi favorable seulement (K = 10) » (lecture 3 : GD3-06) ;
- au § 1, « GD2-10 … corrigé » alors qu'un refus reste brut (GD3-05), et « un fichier par comparateur » sans
  identifiant d'unité (GD3-02).

### 4. Le modèle « effet d'unité sur A » (démontré, `verif_effet_unite.py`)

Défini dans le code ainsi : un décalage u ~ N(0, σ) par unité, ajouté à la probabilité d'alerte de A sur les honnêtes
**et** sur les sabotés de la même unité, puis écrêté à [0 ; 1]. Commun aux k comparateurs en mode partagé. Bien défini,
mais **pas à espérance tenue**. E[clip(p + u, 0, 1)] vaut, à σ = 0,05 :

| p | 0 | 0,01 | 0,06 | 0,10 | 0,50 |
|---|---|---|---|---|---|
| E[clip(p + u)] | 0,0200 | 0,0253 | 0,0628 | 0,1004 | 0,5000 |
| décalage | +0,020 | **+0,015** | +0,003 | +0,0004 | 0 |

À τ = 0,01, la cellule « honnête » a donc E[g] = +0,015 : c'est un biais de 0,0125 à 0,025, déjà rapporté à part.

Décomposition (4 000 répétitions, 160 unités, seuil 160, σ = 0,05) :
- A : sans effet ;
- B : effet du script ;
- C : sans effet, biais égal au décalage de B ;
- D : effet à espérance tenue (p′ tel que E[clip(p′ + u)] = p), même u pour honnêtes et sabotés ;
- E : comme D, u des sabotés tiré à part (aucun lien garde-contraste).

| loi, δ, k | garde seule A / B / C / D / E | fiche A / B / C / D / E |
|---|---|---|
| K = 10, τ = 0,01, δ = 0,05, k = 1 | 0,89 / **0,010** / **0,006** / 0,86 / 0,86 | 0,87 / 0,009 / 0,006 / 0,84 / 0,84 |
| K = 10, τ = 0,01, δ = 0,05, k = 3 | 0,89 / 0,013 / 0,004 / 0,86 / 0,86 | 0,73 / **0,002** / 0,000 / **0,68** / **0,69** |
| K = 3, τ = 0,01, δ = 0,05, k = 3 | 0,66 / 0,046 / 0,046 / 0,65 / 0,66 | 0,079 / 0,001 / 0,002 / 0,067 / 0,065 |
| K = 10, τ = 0,10, δ = 0,05, k = 3 | 0,43 / 0,40 / 0,44 / 0,42 / 0,41 | 0,18 / 0,17 / 0,18 / 0,19 / 0,19 |
| K = 3, τ = 0,10, δ = 0,10, k = 3 | 0,94 / 0,93 / 0,94 / 0,93 / 0,93 | 0,14 / 0,14 / 0,14 / 0,14 / 0,14 |

Lecture :
- À τ = 0,01, B ≈ C : toute la chute vient du déplacement de l'espérance (biais), pas de la dépendance.
- À espérance tenue (D), l'effet coûte 0,02 à 0,05 sur la fiche, par la variance accrue de f_A.
- Le lien garde-contraste (D contre E) change la fiche d'au plus 0,01 dans les 16 cas, dans un sens ou dans l'autre.
  Le sens annoncé par GD2-02 (minimum plus sévère) n'apparaît pas à σ = 0,05 : l'effet est trop petit devant le bruit
  binomial. La contre-lecture v2 l'avait trouvé avec un modèle plus fort (a = 0,08 honnêtes, b = 0,20 sabotés).
- La phrase du rapport « C'est le second effet de GD2-02 ; dans le sens inverse du partage, et plus fort que lui à
  δ = 0,05 » est donc fausse (GD3-01). La lecture 4 (« dans l'autre sens (effet d'unité) ») aussi.
- Les artefacts (R5) sous effet d'unité ne sont plus à la frontière : à τ = 0,01, la cellule « frontière » a
  E[g] = δ + 0,003. Le contrôle reste prudent, mais ce n'est plus un test de la frontière. Près de 1 (τ = 0,9,
  σ = 0,5, accepté), l'écrêtage baisse l'espérance et la « frontière » sortirait du nul.

### 5. Entrées (démontré, `verif_entrees.py` : 96 essais : 50 fichiers de garde, 13 passages en contraste ou combinés, 33 réglages ; 73 refus nommés, 1 erreur brute, 22 acceptations)

Refus nommés (code 1, message « refus : … ») :
- CSV : virgule décimale sur une colonne (« 2 champs pour 1 ») et sur `fA,fB` (« 4 champs pour 2 ») ; en-tête
  `ecart,note` à virgule décimale (le trou de GD2-05 est fermé) ; `ecart,fA,fB` ; `Ecart` ; `fA;fB` ; tabulation ;
  `rA,rB` en garde ; colonne `unite` ; guillemets `"0,1"` ; ligne vide au milieu ou à la fin ; ligne d'espaces ; champ
  vide ; `True`/`False` ; `nan` ; `inf` ; pourcentages ; fraction 1,5 ; fichier vide ; en-tête seul ; Latin-1 ;
- effectif faux (5 lus, 180 attendus) ; `--effectif-attendu` absent avec un fichier ;
- JSON : booléen, `null`, chaîne, `NaN`, `Infinity`, `1e400`, liste imbriquée, clé `signe`, clé `unites`, liste en
  racine, longueurs différentes, |écart| > 1, fraction négative, `rA/rB` en garde, imbrication profonde (RecursionError
  nommée) ;
- contraste : `fA,fB` refusé, rA = 1,5 refusé (CSV et JSON), longueur 6 contre 5, un contraste pour deux gardes ;
- réglages : α ∈ {NaN, 0, 1}, δ ∈ {0,6 ; 0 ; NaN}, τ + 2δ > 1, τ + biais > 1, biais < 0 ou NaN, effet 0,6 ou NaN,
  graine −1, répétitions 50 ou 200 000, `--tailles ""`, `"5,"`, 20 001, `--tailles-garde` mal apparié ou 0, K = 0,
  m = 0, `--K-sabotes` mal apparié, comparateurs 0 ou 65, écart de contraste 0 ou 0,6.

Erreur brute (non nommée) :
- entier JSON de 401 chiffres → `OverflowError: int too large to convert to float` (GD2-10 resté ouvert).

Acceptés sans rien dire (GD3-03, GD3-05) :
- `--ecarts-contraste` sans `--ecarts` : le fichier est ignoré, la sortie est toute synthétique ;
- `--effectif-attendu` sans fichier : ignoré ;
- `--comparateurs 1,2,3` avec deux fichiers : k forcé à 2, aussi pour les lois synthétiques ;
- garde réelle sans fichier de contraste : contraste synthétique de secours, sans mention dans `lois` ni dans la cellule ;
- le même fichier de contraste donné deux fois (deux comparateurs identiques) ;
- clé JSON doublée : la dernière l'emporte ;
- `0.0_5` lu 0,05 (`float` de Python admet le souligné) ;
- marque d'ordre des octets, en-tête entouré d'espaces, fins de ligne CRLF, `+0.1`, extension `.JSON` : acceptés, sans
  danger.

### 6. Prêt pour le fichier d'écarts réels ? (démontré, `verif_reechantillonnage.py`, essais réels)

En partie. Ce qui tient :
- un fichier par comparateur ; unités entières rééchantillonnées : pour chaque tirage et chaque instant, les k gardes et
  les k contrastes viennent de la même ligne, et le fichier j sert au comparateur j (démontré, trois couples n, n_garde) ;
- en-têtes exacts, `fA,fB` et `rA,rB` contrôlés dans [0 ; 1], effectif obligatoire, clés JSON exactes ;
- bloc brut sans champ d'artefact (démontré sur un passage réel à deux comparateurs) ;
- empreinte de chaque fichier lu en sortie.

Écarts à la spécification v2 :
1. **Ensembles d'unités** (GD3-02). La spécification met dans la garde les unités à au moins un épisode honnête, dans le
   contraste les unités à au moins un épisode saboté. Le script exige la même longueur et un seul effectif pour les
   deux, et lit la ligne i de la garde et la ligne i du contraste comme la même unité.
2. **Identifiant d'unité** (GD3-02). La spécification (point 9) demande une colonne d'identifiant. Le script la refuse
   (CSV `unite,fA,fB`, clé JSON `unites`). L'appariement entre fichiers repose sur l'ordre des lignes, sans contrôle.
3. **Métadonnées** : la spécification demande banque, partie, τ, strate, cellules, seuils, m_honnetes par unité, signe,
   commit. Le script les refuse dans le fichier (clés exactes) et n'a pas d'option pour les recopier en sortie. Elles
   restent à joindre à part.
4. **Biais « moyenne + 2 erreurs types »** : non calculé ; l'utilisateur doit le passer à la main dans `--biais`.
5. **Rôle des fichiers** : `fichiers_observes` mêle gardes et contrastes dans une liste, sans champ « rôle ».
6. **Contraste de secours** : sans fichier de contraste, la fiche « réelle » utilise un contraste synthétique, sans le
   dire (GD3-03).

### 7. Ce que disent les chiffres v3 (sans trancher)

Sous les lois synthétiques du script, sujet partagé, biais 0 sauf mention :
- **δ = 0,05** : la garde passe à 160 unités sous la loi la plus favorable (0,89 à k = 1), mais tombe à 0,03 avec un
  biais honnête de 0,0125, et à 0,46 dès τ = 0,10 ; il faut environ 160 à 530 unités pour 80 % des k gardes à biais 0,
  et 350 à 2 400 à biais 0,025.
- **δ = 0,10** : la garde passe à 160 unités sous toutes les lois à biais 0 (0,95 à 1,00 à k = 1), résiste au biais
  0,025 sauf à K = 3 et τ = 0,10 (0,59) ; n₈₀ ≈ 80 à 145 ; mais elle laisse passer un sujet qui alerte presque 10 points
  de plus que le comparateur sur les honnêtes.
- **Seuil 160 (borne basse e-BH) contre 20 (borne haute)** : l'écart est grand à 160 unités et δ = 0,05 (fiche k = 3 :
  0,74 contre 1,00 ; 0,07 contre 0,45 à K = 3) ; la vraie retenue e-BH est entre les deux et n'est pas simulée.
- **Nombre d'unités** : à 64, la fiche ne passe pas à la borne basse (≤ 0,011), contrastes seuls compris ; à 160, elle
  dépend de K et de τ (0,74 à 0,01 à k = 3, δ = 0,05) ; à 400, elle passe à K = 10 (1,00) et partiellement à K = 3
  (0,50 à 0,95). À K = 3, c'est le contraste de dix points qui limite à τ = 0,01, la garde à τ = 0,10 et δ = 0,05.

Ces phrases valent pour la loi synthétique seulement. Le modèle de dépendance change la fiche jusqu'à un facteur 5
(partage) ; l'effet d'unité tel que codé est un biais déguisé (GD3-01).

## Constats

### GD3-01 — majeur — L'« effet d'unité sur A » est surtout un biais d'espérance ; la lecture du rapport l'attribue à la dépendance

**Preuve (démontré, question 4).**
- `tirer` ajoute u ~ N(0, σ) à la probabilité de A, puis écrête à [0 ; 1] (l. 213-217). À p = 0,01 et σ = 0,05,
  E[clip(p + u)] = 0,0253 : le sujet A alerte 2,5 fois plus sur les honnêtes. E[g] = +0,015.
- Sans effet d'unité, un biais de 0,0153 donne la même garde (0,006 contre 0,010 ; fiche k = 3 : 0,000 contre 0,002).
- À espérance tenue, le même effet donne une garde à 0,86 (au lieu de 0,89) et une fiche k = 3 à 0,68 (au lieu de 0,73).
- Le lien garde-contraste (même u pour honnêtes et sabotés) change la fiche d'au plus 0,01 sur 16 cas.
- Le rapport (§ 2) écrit : « C'est le second effet de GD2-02 ; dans le sens inverse du partage, et plus fort que lui
  à δ = 0,05 ». Lecture 3 range « effet d'unité 0,05 (→ 0,014) » à côté du biais comme s'il s'agissait d'une autre
  fragilité. Lecture 4 : « dans l'autre sens (effet d'unité) ». Ces trois phrases ne sont pas soutenues.
- L'en-tête du script et le rapport disent « décalage gaussien … écrêté », sans dire que l'écrêtage change l'espérance.

**Correction.**
- Tenir l'espérance : p′ tel que E[clip(p′ + u)] = p (fonction fermée, voir `esp_clip` et `p_tenu` de
  `verif_effet_unite.py`), ou un effet sur l'échelle logit recentré. Refuser les réglages où p′ sortirait de [−1 ; 1].
- Écrire en sortie E[f_A], E[r_A] effectifs de chaque loi.
- Rapporter l'effet d'unité séparément du biais, avec la décomposition A–E ; donner une amplitude où le lien
  garde-contraste est visible (σ plus grand, ou K plus grand), ou dire qu'il est négligeable aux réglages essayés.
- Réécrire § 2 (« effet d'unité »), lectures 3 et 4.

### GD3-02 — moyen — Fichiers réels : un seul ensemble d'unités pour la garde et le contraste, sans identifiant

**Preuve (à la lecture et démontré).**
- `LoiReelle.__init__` refuse des longueurs différentes ; `--effectif-attendu` est unique ; `tirer` lit la ligne i de
  la garde et la ligne i du contraste comme la même unité (démontré : même ligne sur min(n, n_garde)).
- La spécification v2 (points 2 et « contraste ») et le pôle (`ecarts_faux_positifs` sur les unités à épisodes
  honnêtes, `contrastes` sur les unités à épisodes sabotés, selon la v2) donnent deux ensembles. Une banque avec 180
  unités à honnêtes et 150 à sabotés est refusée, ou forcée à l'intersection, ce qui change la loi de la garde.
- Colonne `unite` en CSV et clé `unites` en JSON : refusées. Deux fichiers de garde peuvent porter des unités dans des
  ordres différents sans que rien ne le voie.

**Correction.**
- Identifiant d'unité obligatoire dans chaque fichier ; contrôle « même liste, même ordre » entre comparateurs d'un même
  rôle.
- Ensembles propres à la garde et au contraste, joints par identifiant. Rééchantillonner l'unité dans l'union ; une unité
  apporte un incrément de garde si elle a des honnêtes, de contraste si elle a des sabotés. Effectifs séparés
  (`--effectif-garde`, `--effectif-contraste`).
- Plus simple : un seul fichier large par unité (`unite, fA_1, fB_1, rA_1, rB_1, …`, case vide admise et nommée).
- À défaut, écrire dans la spécification : « n'utiliser que les unités qui portent honnêtes et sabotés », et chiffrer
  la part des unités écartées.

### GD3-03 — moyen — Replis silencieux d'options (règle R5 : aucun repli silencieux)

**Preuve (démontré, `verif_entrees.py`, code 0 dans chaque cas).**
- `--ecarts-contraste` sans `--ecarts` : ignoré ; sortie toute synthétique (seul le statut le laisse deviner).
- Garde réelle sans contraste : la fiche des lois `reelle_*` prend un contraste synthétique (K[0], τ[0]) ; ni `lois` ni
  la cellule ne le disent.
- `--comparateurs 1,2,3` avec deux fichiers : k forcé à 2 partout, y compris pour les lois synthétiques ; `reglages`
  garde « 1,2,3 ».
- `--effectif-attendu` sans fichier : ignoré.

**Correction.** Refuser les trois premiers cas, ou écrire en sortie `contraste: "synthétique de secours (K, τ)"` et
`k_force_par_les_fichiers`. Refuser `--effectif-attendu` sans fichier.

### GD3-04 — mineur — Traçabilité : état git faux hors dépôt ; commit du manifeste différent de la sortie principale

**Preuve (démontré).**
- Hors dépôt git : `commit: null`, `etat_du_script: "commité, non modifié"`. Fichier ignoré par `.gitignore` dans un
  dépôt : même message, alors que le script n'est pas suivi (`sorties/essai_git/`). La cause : sortie vide de
  `git status` lue comme « propre », sans regarder le code de retour.
- Sortie principale : `commit` `e07b4cda…` ; sorties « effet d'unité » et « indépendants » : `12e765e8…`. Le
  manifeste n'écrit que `12e765e8` comme « commit au lancement ».

**Correction.** Tester le code de retour de `git rev-parse` et `git status` ; utiliser `git ls-files --error-unmatch`
pour « suivi ou non » ; écrire « hors dépôt » ou « non suivi (ignoré) ». Mettre au manifeste le commit de chaque
sortie.

### GD3-05 — mineur — Entrées : un refus brut, deux acceptations douteuses

**Preuve (démontré).**
- Entier JSON de 401 chiffres → `OverflowError` brute (`_fini` appelle `math.isfinite` sans rattraper). Le rapport
  dit GD2-10 corrigé.
- Clé JSON doublée : la dernière valeur l'emporte, sans trace.
- `0.0_5` lu 0,05.

**Correction.** Rattraper `OverflowError` dans `_fini` (comme le pôle, `pari_apparie._fini`) ; `json.loads` avec
`object_pairs_hook` qui refuse les doublons ; refuser `_` dans les champs CSV.

### GD3-06 — mineur — Trois lectures du rapport inexactes

**Preuve (démontré, `verif_rapport_auteur.json`).**
- Lecture 2 : « ce qui limite dépend de K … à K = 3 le contraste limite plus que la garde ». À K = 3, τ = 0,10,
  δ = 0,05, k = 3 : gardes 0,05, contrastes 0,19. La garde limite. Cela dépend de K **et** de τ. De même, à K = 10,
  τ = 0,10 : gardes 0,20 contre contrastes 0,95 (pas « du même ordre »).
- Lecture 3 : « δ = 0,10 y résiste sous la loi favorable seulement (K = 10) ». À K = 3, τ = 0,01, 160 unités, la garde
  vaut 1,00 / 1,00 / 0,99 aux biais 0 / 0,0125 / 0,025. Seule la loi K = 3, τ = 0,10 la fait tomber (0,59).
- § 2 : « contrastes seuls 0,08 à 0,12 à k = 1 » à 64 unités : la sortie donne 0,068 à 0,124.

**Correction.** Écrire « dépend de K et de τ » avec les deux cas ; « δ = 0,10 résiste sauf à K = 3, τ = 0,10 » ;
« 0,07 à 0,12 ».

### GD3-07 — mineur — Lecture des seuils écrite en dur ; e-BH non simulé

**Preuve (à la lecture et démontré).**
- La chaîne `lecture_des_seuils` dit « 20 (m = 1) » quel que soit `--alpha` ou `--m`. Avec `--alpha 0.01`, les seuils
  sont 800 et 100, la chaîne dit toujours 20. Si `--m` ne contient pas 1, il n'y a pas de borne haute du tout.
- La retenue e-BH sur la valeur finale reste citée (0,32 au cas de GD2-03), non simulée. C'est dit au § 4 du rapport.

**Correction.** Construire la chaîne à partir des seuils réels (« 1/α_c = … : borne haute ») ; exiger m = 1 dans la
liste, ou écrire « pas de borne haute ».

### GD3-08 — mineur — Sortie réelle : rôle des fichiers absent, doublon accepté, métadonnées impossibles à joindre

**Preuve (démontré, `essai_reel_deux_comparateurs.json`).**
- `fichiers_observes` liste gardes puis contrastes, sans champ « rôle » ni « comparateur ».
- Le même fichier de contraste passé pour deux comparateurs est accepté sans avertissement.
- Les métadonnées que la spécification v2 demande de joindre (banque, partie, τ, strate, cellules, seuils, signe,
  commit) ne peuvent ni entrer dans le fichier (clés exactes) ni passer par une option.

**Correction.** Ajouter `role` et `comparateur` à chaque fichier observé ; avertir (ou refuser) deux fichiers de même
empreinte ; accepter un fichier de métadonnées à part (`--metadonnees`), recopié en sortie avec son empreinte.

## Table GD2-01 à GD2-11

| constat v2 | état en v3 | preuve |
|---|---|---|
| GD2-01 lecture 2 fausse | **corrigé en grande partie** | ligne K = 3 à k = 3 au tableau (chiffres exacts) ; « garde comprise » ; 64 unités juste. Restent les lectures 2 et 3 inexactes (GD3-06) |
| GD2-02 comparateurs indépendants | **en partie** | sujet partagé par défaut, `--comparateurs-independants` : chiffres retrouvés (0,65 contre 0,74…). Rééchantillonnage par unité entière démontré. L'effet d'unité est un biais déguisé (GD3-01) |
| GD2-03 seuils | **en partie** | « borne basse / borne haute, lâche » en sortie ; `--alpha` en option et en sortie ; seuil = m/α identique au pôle. Chaîne écrite en dur, e-BH non simulé (GD3-07) |
| GD2-04 bloc brut | **corrigé** | `reelle_brute` sans `frontiere_part` ni `tricheur_part` (démontré, passage réel à deux comparateurs) |
| GD2-05 CSV | **corrigé pour la garde, en partie pour l'ensemble** | `ecart,note` à virgule, `ecart,fA,fB`, effectif faux, effectif absent : refusés (démontré). L'effectif est unique pour garde et contraste (GD3-02) |
| GD2-06 troncature | **corrigé** | τ + 2δ > 1 et τ + biais > 1 refusés (τ = 0,95, δ = 0,05 ; δ = 0,5, τ = 0,01 ; τ = 0,89, biais 0,2). L'écrêtage de l'effet d'unité n'est pas couvert (GD3-01) |
| GD2-07 n₈₀ | **corrigé** | « ≈ », `pas_de_la_dichotomie`, note. À graine neuve, 53 n₈₀ sur 144 changent, d'au plus 3,8 %, sous la note « ≈ 6 % » |
| GD2-08 longueurs | **corrigé** | `--tailles-garde` ; prolongement identique au pôle à 7,1·10⁻¹⁵ sur 495 fiches à longueurs différentes |
| GD2-09 fichiers | **en partie** | `rA,rB`, [0 ; 1] en contraste, un fichier par comparateur, clés en trop refusées (démontré). Pas d'identifiant d'unité, refus de toute métadonnée, clé doublée acceptée (GD3-02, GD3-05) |
| GD2-10 refus | **en partie** | graine négative, listes mal formées, bornes de répétitions et tailles, marque d'ordre des octets, JSON profond : nommés. Entier JSON de 401 chiffres : `OverflowError` brute (GD3-05). Le produit répétitions × tailles n'est pas borné (100 000 × 20 000 × 4 mises ≈ 64 Go, à la lecture, non exécuté) |
| GD2-11 traçabilité | **en partie** | `commit` et `etat_du_script` en sortie. Faux hors dépôt et pour un fichier ignoré ; commit du manifeste ≠ commit de la sortie principale (GD3-04) |

## Non vérifié

- « Sujet partagé = structure du pôle » : repris de la contre-lecture v2 (`engagement_apparie.evaluer`), non relu.
- L'ordre relatif des unités honnêtes et sabotées dans le pôle (alignement par rang) : lu dans la docstring de
  `evaluer` seulement.
- La loi réelle : aucun fichier d'écarts réels fourni.
- Les commits `e07b4cda…` et `12e765e8…` : pas de dépôt ici.
- Python 3.13.18 : j'ai la 3.13.17 ; sorties identiques hors environnement.
- Le journal vide : cohérent avec le code (le script n'écrit rien sur l'erreur standard quand il réussit). Il ne prouve
  donc rien de plus que le code de sortie. Il ne contient ni commandes ni heures ; le manifeste les donne, abrégées
  par « … ».
- Le dépassement mémoire à 100 000 répétitions × 20 000 unités : non exécuté.

## Fichiers produits (sous `…/relecture-garde-delta-v3/cl/`)

| fichier | rôle |
|---|---|
| `outils/copie_script/sim_garde_v3.py` | copie conforme du script (`7b636c1e…`) |
| `outils/copie_pole/pari_apparie.py` | copie conforme du pôle v41 (`ec6c2cf6…`) |
| `outils/verif_fiche_pole.py` → `sorties/verif_fiche_pole.json` | Q2 : 1 000 fiches contre `evaluer` |
| `outils/verif_effet_unite.py` → `sorties/verif_effet_unite.json` | Q4 : espérances, décomposition A–E |
| `outils/verif_entrees.py` → `sorties/verif_entrees.json`, `sorties/essais_entrees/` | Q5 |
| `outils/verif_reechantillonnage.py` → `sorties/verif_reechantillonnage.json` | Q6 : unités entières |
| `sorties/essai_reel_deux_comparateurs.json` | Q6, GD2-04 : passage réel à deux comparateurs |
| `sorties/essai_git/` | GD3-04 : fichier ignoré lu « commité » |
| `outils/lancer_repro.sh` → `sorties/repro-*.json`, `sorties/neuve-*.json` | Q3 : même graine, graine 918273645 |
| `outils/comparer_sorties.py` → `sorties/comparaison-*.json` | Q3 : comparaison champ par champ |
| `outils/verif_rapport.py` → `sorties/verif_rapport_auteur.json`, `sorties/verif_rapport_neuve.json` | Q3, Q6 : chiffres du rapport |

Empreintes : `cl/EMPREINTES-contre-lecture-garde-delta-v3.txt`. Les fichiers `.err` sont tous vides.
