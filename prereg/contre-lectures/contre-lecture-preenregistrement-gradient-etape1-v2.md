# Seconde contre-lecture (R2) — préenregistrement « gradient conçu par l'essaim », étape 1 (sondes) — v2

- Relecteur neuf : sous-agent de contre-lecture R2 n° 2 ; n'a écrit ni le brouillon v1, ni la v2, ni le code, ni la
  première contre-lecture. Date (UTC) : 2026-10-24, 19:32 → 21:xx (lue par `date -u`).
- Texte relu : `gradient-etape1-sondes-v2.md`
  empreinte SHA-256 **`6ae4a8b367ccf6ac9de69e7c792971b8a1b3bab283ad49c549a95094dc8b1507`** (compagnon vérifié : OK).
- Première contre-lecture relue : `contre-lecture-preenregistrement-gradient-etape1-v1.md` `2efeb8db…` (compagnon OK) ;
  brouillon v1 `2b6e5dcb…` (OK).
- Code lu au commit cité (`49f1a16`, pièces) : `entrainement.py`, `bac_a_sable.py`, `boucle.py`, `cli.py`,
  `serveur.py`, `archive.py`, `contrat.py`, `taches.py`, `analyse_gradient.py`, `analyse.py`, `banque.py`,
  `appels.py`, `tests/test_noyau.py`, `collisionneur_v2.py`, `extraire_activations_v2.py`.
- Empreintes citées par la v2, vérifiées et **concordantes** : `analyse_gradient.py` `7a782eb6…`, `analyse.py`
  `1cef7c0f…`, collisionneur `213b52ef…` (= `EMPREINTE_COLLISIONNEUR_V25`, donc la garde de conformité du mode réel
  ne refusera pas), `puissance-v1.json` `eaf4ea5d…`, MISSION `bd2c6a15…`, note `6b415104…`, banque `f1387a20…`,
  manifeste traits-16384 `034d8460…`, EMPREINTES traits `add13e09…`, script d'extraction `8286f4e7…`, gabarit et
  validateur du dépôt (OK). Toutes les empreintes compagnons des pièces : OK.

## VERDICT : **scellable après corrections**

Deux **bloquantes**, de pur texte (le code et les tests se tiennent) :

1. **CE2-01** — la section « Métrique » nomme la lignée Gemini auto-écrite **`gemini-4-argon`** ; le noyau la forme
   **`gemini-argon`** (`gemini-4-argon` est l'identifiant de *modèle*, pas de lignée). Comme l'unité d'analyse est gelée
   avec ce nom, la lecture de H-G1 appliquée telle quelle coupe les deux répliques de cette lignée → 2 paires sur 6
   coupées (> 25 %) → verdict mécanique « non concluant : invalidé », quel que soit le résultat réel. **Rejoué.**
2. **CE2-02** — la commande du bras B_r dit « `--depuis <A_r>` … **tout le reste identique** », donc en gardant les deux
   `--organisme-impose`. Exécutée telle quelle, elle est **refusée** par le noyau (`SystemExit : --depuis : la lignée
   'enveloppe-essaim-gemini-v3' est aussi donnée par --organisme-impose`). Le plan n'est pas exécutable mot pour mot ;
   il faut retirer les deux `--organisme-impose` de B_r (comme le fait le test `test_bras_apparie_adaptatif…`), ce que
   le texte ne dit pas. **Rejoué.**

Hors ces deux corrections de texte, les vingt remarques CE-01 à CE-20 sont réellement traitées, dans le texte **et** le
code (vérifié ; 74 tests du noyau passent, dont les gardes neuves ; l'analyse de H-G1 est correcte et sa puissance se
rejoue à l'identique). Après ces corrections et une courte re-vérification (les deux portent sur des identifiants et une
ligne de commande gelés), la v2 est scellable.

**Validateur du dépôt** : rejoué sur une copie (bouchons de scellement inoffensifs) — la seule chose relevée est
« contre-lecture 2 sans ses deux empreintes (brouillon relu et rapport) ». L'entrée 1 porte bien ses deux empreintes
(`2b6e5dcb…` et `2efeb8db…`). Au scellement, inscrire dans l'entrée 2 l'empreinte du texte relu (`6ae4a8b3…`) et celle
du présent rapport (compagnon `.sha256`), plus l'entropie E : **le validateur sera alors muet.** Confirmé.

Décompte : **2 bloquantes, 1 majeure, 4 mineures, 2 de forme.**

---

## Corrections

### Bloquantes

**CE2-01 — bloquante — mauvais identifiant de lignée dans la section gelée « Métrique » (unité d'analyse).**
Fichier : `gradient-etape1-sondes-v2.md`, l. 72-73 (« ℓ ∈ {claude-fable-5-1, claude-opus-5-5, **gemini-4-argon**} »).
Défaut : le noyau forme le nom de lignée par `espece.lower().replace("_","-")` (`contrat.ESPECES_DISPONIBLES`,
`boucle.amorcer`) ; `GEMINI_ARGON` → **`gemini-argon`**. `gemini-4-argon` est l'`id` de modèle
(`collisionneur_v2.MODELES["C"]["id"]`). La lecture gelée (Plan, point 6) appelle
`paires_h_g1(..., [trois lignées auto-écrites], ...)` ; les seuls noms écrits sont ceux de « Métrique ». Avec
`gemini-4-argon`, `generations_valides` ne trouve aucune génération → les deux paires `gemini-4-argon@r0/r1` sont
« coupées » → 2/6 = 0,33 > `PART_INVALIDE_MAX` (0,25) → `etat["invalide"]` vrai → `lecture_h_g1` rend « non concluant :
plus d'une paire sur quatre coupée ou invalidée ». Les deux lignées Claude (`claude-fable-5-1`, `claude-opus-5-5`) sont,
elles, correctes.
Preuve (rejouée, deux répliques simulées appariées, `travail/sortie-noms-lignees.txt`) :
```
lignées formées par le noyau : ['claude-fable-5-1', 'claude-opus-5-5', 'gemini-argon']
noms du texte (Métrique) : 4 paires, coupées ['gemini-4-argon@r0','gemini-4-argon@r1'], invalide True
                           -> « non concluant : plus d'une paire sur quatre coupée ou invalidée »
noms du noyau            : 6 paires, coupées [], invalide False -> « non concluant ; aucune relance… »
```
Correction : remplacer `gemini-4-argon` par `gemini-argon` à la section « Métrique » (et partout où la lignée
auto-écrite Gemini est nommée). Ne pas confondre avec les deux lignées imposées (`gemini-organisme-v3`,
`enveloppe-essaim-gemini-v3`), dont les noms, eux, sont justes (ce sont les `NOM` de `--organisme-impose`).

**CE2-02 — bloquante — la commande du bras B_r, « tout le reste identique », est refusée par le noyau.**
Fichiers : `gradient-etape1-sondes-v2.md`, l. 119-120 (B_r : « `--depuis <A_r>` … tout le reste identique ») ;
`cli._imposes_et_especes` (l. 59-66 : `--depuis` injecte les g000 archivés dans `imposes` et **lève `SystemExit` si un
nom est déjà un `--organisme-impose`**).
Défaut : A_r passe `--organisme-impose gemini-organisme-v3=…` et `--organisme-impose enveloppe-essaim-gemini-v3=…`.
B_r = `--depuis A_r` récupère **toutes** les lignées g000 de A_r (dont ces deux imposées) ; « tout le reste identique »
les redonne par `--organisme-impose` → conflit de nom → refus **avant tout appel**. Le plan gelé doit être exécutable
tel quel (R1) ; il ne l'est pas.
Preuve (rejouée, `travail/sortie-bras-b-commande.txt`) :
```
A_1 (avec gradient, deux imposées) : code 0 ; lignées g000 : [enveloppe-essaim-gemini-v3, gemini-argon, gemini-organisme-v3]
B_1 tel quel (avec --organisme-impose) : REFUS -> --depuis : la lignée 'enveloppe-essaim-gemini-v3' est aussi donnée par --organisme-impose
B_1 sans --organisme-impose : code 0 ; lignées : [enveloppe-essaim-gemini-v3, gemini-argon, gemini-organisme-v3] (mêmes g000, --depuis les réimpose seul)
```
Correction : écrire explicitement la commande B_r **sans** les deux `--organisme-impose` (les lignées imposées
reviennent par `--depuis`, avec les mêmes empreintes d'arbre, le manifeste de B le confirme) ; garder
`--entrainements-max 0 --plafond-total 225 --depuis <A_r> --taches <banque> --graine <graine_r>` et le reste. Préciser
que « tout le reste identique » exclut `--organisme-impose` (et, au besoin, que `--traits` peut rester : avec
`--entrainements-max 0`, `traits.disponibles` est faux, vérifié).

### Majeure

**CE2-03 — majeure — « toutes choses égales par ailleurs » surévalue le contrôle du bras apparié : trois choses restent
différentes et le texte n'en nomme aucune.**
Fichiers : `gradient-etape1-sondes-v2.md`, l. 38-42 (H-G1 : « mêmes organismes g000, même banque, même graine d'ordre,
mêmes budgets… ») ; `boucle.boucler` (l. 546-551 : `graine_ronde` permute `actives`, liste **ordonnée par insertion**
dans `self.lignees`), `boucle.executer_generation` (l. 433 : `usd_max` d'une génération = `min(usd_max,
plafond_restant)`).
Défaut : les graines par lignée (`graine(lignee, g, usage)`) utilisent `sorted(self.lignees).index(lignee)` : elles sont
donc **identiques** entre les deux bras (vérifié : `ordre_train/ordre_test/organisme` de `gemini-argon` g0 identiques en
A et B). En revanche :
1. **l'ordre des lignées dans une ronde diffère entre A et B.** A insère [auto-écrites, puis imposées] ; B (`--depuis`)
   insère toutes les lignées comme imposées, dans l'ordre de l'index d'archive de A — donc un ordre de base différent, à
   quoi la même permutation de ronde donne un ordre concret différent. Rejoué (`travail/sortie-noms-lignees.txt` et
   l'essai `bras_b_commande`) : ronde 1 de A = [enveloppe, gemini-organisme-v3, gemini-argon] ; ronde 1 de B =
   [gemini-argon, gemini-organisme-v3, enveloppe]. Comme `plafond_total` est partagé et consommé dans l'ordre de ronde,
   une lignée servie plus tard voit un `usd_max` effectif plus petit : asymétrie possible entre bras si le plafond de
   course mord.
2. **les appels de modèle sont non déterministes** (pas de température, mais pas déterministes) : même à g0 (même code),
   les réponses sur le test final diffèrent d'un bras à l'autre ; c'est inhérent et le bootstrap par paire est censé
   l'absorber, mais le texte ne le dit pas.
3. **les successeurs g1, g2 sont réécrits** par l'organisme selon ce qu'il a lu (c'est le traitement, mais c'est une
   différence entre bras au-delà du seul « entraînement »).
Portée : limitée (lignées indépendantes par défaut — pas `--memoire-partagee` — et plafond de course généreux : attendu
150-400 USD pour 990 USD de bornes), mais réelle et non divulguée, ce qui heurte la symétrie R4 affichée.
Correction : ajouter une phrase à H-G1 (ou au Plan) nommant ce qui reste différent entre bras (ordre de ronde effectif,
non-déterminisme des appels, réécriture des successeurs) et désignant le bootstrap à deux niveaux par paire comme
l'absorbeur du bruit de paire ; au besoin, dire que `plafond_total` est dimensionné pour ne pas mordre (c'est le cas :
B_r 225 < attendu, A_r 270).

### Mineures

**CE2-04 — mineure — la branche « modèle non conforme (formes, pickle) » de `_lire_resultat` n'a pas d'essai sur
artefact (R5).**
Fichiers : `gradient-etape1-sondes-v2.md`, l. 184 (ligne d'arrêt « résultat d'entraînement ou modèle non conforme …
garde (`_lire_resultat`) ; **même essai d'isolation** ») ; `entrainement._lire_resultat` (l. 213-228 :
`allow_pickle=False`, contrôle des formes et de la finitude) ; `tests/test_noyau.py`.
Défaut : le cas sain et l'artefact « perte qui lève » (→ `ECHEC_ENTRAINEMENT`) sont testés
(`test_entraineur_sonde…`), mais **aucun test ne fabrique un `modele.npz` malformé** (mauvaises formes, ou objet Python
à charger) ; l'« essai d'isolation » cité (`test_entraineur_isole…`) produit un modèle **valide**. La branche
réécriture-de-forme du garde n'est donc pas couverte sain+artefact comme l'exige R5. (Recherche rejouée : « aucun test
ne produit un modele.npz malformé ».)
Correction : soit ajouter un petit essai d'artefact (un `resultat.json` OK avec un `modele.npz` aux mauvaises formes →
`ECHEC_ENTRAINEMENT`, modèle non servi), soit corriger la ligne d'arrêt pour ne citer que ce qui est réellement testé
(la branche « perte qui lève / `resultat.json` illisible »).

**CE2-05 — mineure — le mécanisme de l'en-tête d'espace de travail (clés) n'est exercé par aucun test et dépend du SDK.**
Fichiers : `gradient-etape1-sondes-v2.md`, l. 120-124 (« en-tête d'espace de travail par `ANTHROPIC_CUSTOM_HEADERS` …
`ANTHROPIC_BASE_URL` absente ») ; `collisionneur_v2.appeler_anthropic` (l. 388 : `anthropic.Anthropic(max_retries=4)`,
**sans** `default_headers`).
Défaut : le client Anthropic est construit sans en-tête explicite ; l'attribution à l'espace de travail repose
entièrement sur la lecture, par le SDK, de la variable d'environnement `ANTHROPIC_CUSTOM_HEADERS`, et sur le retrait de
`ANTHROPIC_BASE_URL`. Rien dans le code ni les tests ne le vérifie (et ce n'est pas vérifiable ici, sans réseau ni
clé). Ce n'est pas un défaut de code, mais une dépendance opérationnelle non éprouvée, portée par un run décisif payant.
Correction : soit un contrôle avant lancement (le lanceur affiche/trace, sans la valeur, que l'en-tête est bien pris en
compte et que `ANTHROPIC_BASE_URL` est absente), soit une note disant que ce point est vérifié par la répétition
mécanique (Plan, point 8) et par l'inspection des journaux d'appels (qui portent le modèle servi), avant les courses
décisives.

**CE2-06 — mineure — `revision_resolue = None` : l'identité du modèle tient au seul argument `--revision`, non à une
empreinte résolue.**
Fichiers : `gradient-etape1-sondes-v2.md`, l. 104-105 ; manifeste traits-16384 (`config_modele.revision_resolue: None`,
vérifié) ; `extraire_activations_v2.py` (garde l. « révision résolue ≠ demandée » qui **laisse passer `None`**).
Défaut : sous transformers 5.18.0, `_commit_hash` n'est plus posé, donc le manifeste n'enregistre pas l'empreinte de
commit effectivement servie ; la reproductibilité du modèle repose sur le fait que `from_pretrained(revision=
0e9e39f2…)` honore la révision. La v2 le **divulgue** (bon au regard de R7/R8) et R-360 note « à corriger en v3 ».
Portée : faible pour le scellement — les traits sont déjà extraits et **scellés par leurs empreintes** (vérifiées), donc
l'artefact servi est figé quoi qu'il arrive. Correction : rien d'obligatoire avant scellement ; garder la divulgation
telle quelle. (Non bloquant : noté pour la trace.)

**CE2-07 — mineure — le script des sondes témoins (H-G2) n'existe pas encore ; c'est un engagement, pas une pièce.**
Fichier : `gradient-etape1-sondes-v2.md`, l. 138-143 (« script … écrit et scellé (addendum) avant d'être lancé »).
Défaut : H-G2 est descriptive (sans seuil), et la v2 promet un addendum scellé et contre-lu avant lancement. L'engagement
est conforme à R1 pour une analyse descriptive post-course, mais le préenregistrement ne porte pas encore l'empreinte de
ce script : à ne pas oublier au moment de lancer les témoins (il n'entre pas dans la décision de H-G1).
Correction : aucune avant scellement ; rappeler dans l'addendum que l'empreinte du script témoin y est inscrite.

### Forme

**CE2-08 — forme — section « Contre-lecture », entrée 2 sans ses deux empreintes (attendu avant scellement).**
Fichier : `gradient-etape1-sondes-v2.md`, l. 223-224. C'est l'unique chose que le validateur relève (rejoué). Inscrire,
au scellement : empreinte du texte relu `6ae4a8b3…`, empreinte du présent rapport (compagnon `.sha256`), entropie E.

**CE2-09 — forme — « Δ d'une paire au-dessus de +0,40 ou au-dessous de −0,40 » (audit R4) : vérifier que la condition
est bien calculée sur les Δ par paire renvoyés.**
Fichier : `gradient-etape1-sondes-v2.md`, l. 162-165 ; `analyse_gradient.difference_h_g1` renvoie `par_paire`
(Δ par paire) ; `lecture_h_g1` lit `resultat["audit"]`, **posé par l'appelant**. Le texte dit « l'appelant passe
`audit` » (Plan, point 6 : `lecture_h_g1` avec `audit` et `invalide`). Rien à corriger dans le code ; s'assurer, au
rapport d'analyse, que le calcul de `audit` couvre bien les trois déclencheurs (score de famille > 0,95 ou < 0,30 ;
sonde témoin > 0,95 ; |Δ paire| > 0,40) — ils ne sont pas codés dans une fonction unique, c'est l'analyste qui les
applique. Mentionner où, pour qu'un sous-agent neuf (R13) puisse les rejouer.

---

## Suivi des vingt remarques de la première contre-lecture (CE-01 à CE-20)

| remarque (v1) | état | vérification |
|---|---|---|
| CE-01 validateur / 8 sections | **traité** | les 8 sections canoniques présentes ; validateur muet sauf empreintes d'entrée 2 (rejoué) |
| CE-02 entraîneur non isolé | **traité** (code) | `Entraineur(uid, isoler_reseau, espace)` ; `boucle._entraineur` met l'uid en root, **lève `Arret` en réel sans isolation** (rejoué) ; `test_entraineur_isole_ne_lit_pas_les_fichiers_du_noyau` passe (sain : fichier 0600 non lu — perte de Brier ; artefact : sans isolation, lu = 42,0) ; `test_organisme_fuite…` passe ; aucun processus uid≥60000 ne survit (vérifié) |
| CE-03 bootstrap par tâche | **traité** | `analyse_gradient.difference_h_g1` à deux niveaux, unité = paire ; contrôle positif `verifier_sur_simulation_h_g1` ; ma simulation adverse (tâches partagées, effets hétérogènes) : « confirmé » sous effet nul ≤ 2 % — sous le seuil de 5 % |
| CE-04 vues non codées | **traité** (code) | `normaliser_vues`, `spec["vue"]`, `cli.charger_traits` multi-vue ; `test_vues_choisies…`, `test_charger_traits…`, `test_noyau_sert_les_vues…` passent |
| CE-05 table + règle | **traité** | table du texte = `lecture_h_g1` (lu ligne à ligne) ; « confirmé » = borne basse > 0 **et** Δ ≥ +0,10 ; `test_analyse_h_g1…` couvre chaque ligne |
| CE-06 appariement | **traité en partie** | mécanisme bon (`--depuis` sans `--gel`, même banque exigée ; `test_bras_apparie_adaptatif…`), **mais la commande B_r du texte est non exécutable** → CE2-02 |
| CE-07 budget | **traité** | 10×120+300 = 1 500 ≤ 2 400 ; garde `Arret CE-07` (rejouée) ; `_entraineur` passe bien `delai_s` ; `test_budget_incoherent…` |
| CE-08 lignées | **traité en partie** | `gemini-organisme-v3` + `enveloppe-essaim-gemini-v3` imposées, hors H-G1 ; **mais le nom de la lignée Gemini auto-écrite est faux** → CE2-01 |
| CE-09 troncature | **traité** | `traits-16384` servi, `n_tronquees` = 0, max 12 407 jetons (manifeste vérifié) ; v2 du script consigne chaque troncature (`traits-2048` : 44 consignées) |
| CE-10 révision / manifeste | **traité** | révision `0e9e39f2…` ; versions, carte, durée, commit au manifeste ; limite `revision_resolue=None` divulguée → CE2-06 |
| CE-11 empreintes | **traité** | banque, traits, script, code, collisionneur, analyse — toutes inscrites et **vérifiées concordantes** |
| CE-12 liste d'arrêt | **traité en partie** | chaque ligne nomme garde+essai ou vérification humaine ; **une branche de `_lire_resultat` sans essai d'artefact** → CE2-04 |
| CE-13 « à confirmer » | **traité** | R-344, 18:39 (décisions de Lazar, extrait des registres) ; réserve retirée |
| CE-14 métrique | **traité** | H-G1 sur le test final seul ; H-G2/H-G3 sans seuil (le nom de lignée fautif vit dans cette section → CE2-01) |
| CE-15 graine de la sonde | **traité** | « choix de l'organisme, journalisé par `sha256_spec`, distinct des graines expérimentales » (Plan, point 5) |
| CE-16 sonde « longueur seule » | **traité** | retirée ; référence de surface `reference_traits_texte` (0,69 / 0,50, dites non auditées) |
| CE-17 sondes témoins | **traité** | descriptives, après la course, script scellé en addendum avant lancement → engagement, rappel CE2-07 |
| CE-18 titres | **traité** | intitulés canoniques |
| CE-19 empreintes de la section | **traité** (entrée 1) | entrée 1 porte `2b6e5dcb…` et `2efeb8db…` ; entrée 2 au scellement → CE2-08 |
| CE-20 devis | **traité** | GO-2026-10-24-05 sans devis (R-355) ; annexe informative, non opposable |

Bilan : **20/20 réellement traitées**, avec deux traitements dont le *texte* a introduit une erreur localisée (le nom de
lignée Gemini, CE2-01, dans l'héritage de CE-14 ; la commande B_r, CE2-02, dans l'héritage de CE-06) et deux traitements
seulement partiels en R5/trace (CE-12 → CE2-04 ; disclosure CE2-05).

---

## Réponses aux sept points à examiner

**1. CE-01 à CE-20 traités réellement (texte et code) ?** Oui, tous (table ci-dessus), le code à l'appui : 74 tests du
noyau passent (les 4 échecs sont des tests qui exigent les organismes de la relève ou la banque réelle, hors pièces,
comme annoncé — voir « ce que je n'ai pas pu vérifier »). Deux héritages portent une erreur de *texte* (CE2-01, CE2-02),
deux sont partiels côté R5/trace (CE2-04, CE2-05).

**2. Isolation de l'entraîneur — reste-t-il un chemin où l'objectif de l'organisme lit une vérité du test final ou écrit
dans la zone du noyau ? Le test prouve-t-il ce qu'il dit ?** Au niveau de la conception, non. En réel (root obligatoire :
`cli.lancer` + `Noyau.__init__`), `boucle._entraineur` fixe un `uid` d'entraîneur distinct
(`bac_a_sable.uid_entraineur`) et `isoler_reseau`. `Entraineur.entrainer` écrit, dans un dossier neuf de `espace`
(`entrainements/<prefixe>`) **appartenant à cet utilisateur** : seulement `donnees.npz` (X et y des **seules** tâches
d'entraînement demandées — `valider` refuse tout identifiant de test, `verites_train` ne contient que `train`),
`spec.json`, et `programme.py` **rechownné à root 0644** (l'utilisateur ne peut pas le modifier). Le sous-processus passe
par `_commande_isolee` → `unshare --mount --pid --fork --kill-child --mount-proc` + `-n` + `abaisser.py` (setgid/setuid,
vérifié). La zone du noyau (`travail`, banque 0600 root, `juge/`) n'est ni lisible ni accessible. Le modèle validé est
recopié par le noyau (`_lire_resultat`, `allow_pickle=False`, formes et finitude contrôlées) dans sa zone ; `predire` ne
rend que des probabilités, **jamais une vérité**. Les canaux de retour (`courbe_perte`, `perte_finale_entrainement`,
`exactitude_entrainement`) ne portent que l'entraînement (tâches `train`), pas le test final. Le test
`test_entraineur_isole_ne_lit_pas_les_fichiers_du_noyau` prouve bien les deux côtés (R5) : **rejoué**, il passe — le cas
sain (fichier 0600 du noyau non lu, l'objectif retombe sur la perte de Brier, courbe < 1,0) et l'**artefact** (le **même**
objectif, sans isolation, lit le fichier : courbe = 42,0, « la fuite est vue quand elle existe »). La branche réelle
sans root de `_entraineur` (`elif self.reel: raise Arret(...CE-02)`) est **défensive et inatteignable** (Noyau refuse
déjà le réel hors root), ce que la ligne d'arrêt dit honnêtement (« non atteignable en root »).

**3. Bras apparié — les deux bras ne diffèrent-ils que par l'entraînement ?** Non entièrement : les **graines par
lignée** sont identiques (vérifié), mais l'**ordre de ronde effectif** diffère, les **appels de modèle** sont non
déterministes, et les **successeurs** sont réécrits (c'est le traitement). Le texte n'en nomme aucun → **CE2-03**
(majeure, portée bornée). Et la commande B_r telle qu'écrite est **refusée** → **CE2-02** (bloquante).

**4. Analyse de H-G1.** Statistique correcte : unité = paire (ℓ, r), Δ = score(test final, A) − score(test final, B) à
la dernière génération valide commune (`paires_h_g1`), bootstrap à deux niveaux par strate (famille, vérité), mêmes
tâches pour les deux bras d'une paire (`difference_h_g1`), 2 000 tirages, graine `SeedSequence` consignée. **Table du
texte = `lecture_h_g1`** (lu ligne par ligne : audit → invalide → aucune paire → confirmé [bas>0 et Δ≥+0,10] → réfuté
[haut<+0,10, avec « plus petit que prédit » si bas>0] → non concluant). Contrôle positif présent
(`verifier_sur_simulation_h_g1` : +0,20 → « confirmé » et couvre ; nul → jamais « confirmé »). **Puissance rejouée à
l'identique** (200 jeux, 400 tirages, `SeedSequence(20261025)`, `travail/sortie-puissance-rejouee.txt`) : six paires,
nul → confirmé 0 % / réfuté 46,5 % / non concl. 53,5 % ; +0,10 → 44 % / 1,5 % / 54,5 % ; +0,20 → 98,5 % ; neuf paires
+0,10 → 49,5 %. **Tous identiques à `puissance-v1.json`.** La puissance modeste (44 %) est dite avant la course (R3/R8) :
honnête. Ma simulation adverse (les six paires partagent les 60 mêmes tâches, effets de tâche hétérogènes communs) montre
que le bootstrap du code est **légèrement anticonservateur** (couverture d'IC ≈ 92 % contre 95 % nominal) quand les
tâches portent de forts effets communs, mais le taux de « confirmé » sous effet nul **reste ≤ 2 %** : la cible de H-G1
(« confirmé à tort ≤ 5 % ») tient. Pas de défaut statistique bloquant.

**5. Plan d'exécution.** La commande **A_r** est exécutable telle quelle (toutes les options existent : `--reel --go
--registre-go --taches --traits --sortie --generations --graine --appels-max --usd-par-generation --temps-max
--recherches-max --entrainements-max --pas-max --delai-entrainement --parallele-max --relances-max --isoler-reseau
--plafond-total --organisme-impose` ×2 ; aucune n'est refusée). La commande **B_r** ne l'est **pas** (CE2-02). La garde
de GO lit bien le type « calcul » dans l'extrait du registre (rejoué : GO-2026-10-24-05 « calcul » accepté ; mais la
garde cherche le mot « calcul » **dans la ligne**, pas la colonne — GO-2026-10-24-04, de type « décision », serait aussi
accepté s'il était passé, car sa ligne contient le mot « calcul » ailleurs : non exploité ici puisque le GO cité est le
05, mais à savoir). Budgets cohérents (garde CE-07 rejouée). Clés : dépendance SDK non éprouvée (CE2-05). La garde
`--depuis` « même banque » agit (rejoué : banque identique → passe ; banque modifiée → refus code 6). La répétition
mécanique (point 8) est bien préalable et exclue de l'analyse.

**6. Liste d'arrêt — chaque garde existe-t-elle, avec essai sain et artefact (R5) ?** Oui pour l'essentiel, vérifié au
code et en rejouant : GO/collisionneur (constructeur `Noyau`, empreinte collisionneur = attendue), non-root / réseau
(rejoué : refus distincts), **entraîneur sans isolation en réel** (rejoué : `Arret` CE-02), **traits altérés/compagnon/
banque/vue/non fini/factice** (`test_charger_traits…`, 7 artefacts), **budget incohérent** (rejoué), **bras sur une
autre banque** (rejoué), **spec qui désigne une tâche de test / objectif refusé / plafond** (`test_entraineur_sonde…`),
**plafond dollars au pire cas** (`test_appels_paralleles…`), **modèle non conforme** (`test_modele_non_conforme…`),
**fichier STOP** (`test_fichier_stop…`), **plus d'une paire sur quatre coupée** (`test_paires_h_g1…`), **vue d'archive
sans juge/journal/modele** (vérifié dans la vue : rien). **Exception** : la branche « modèle non conforme (formes/
pickle) » de `_lire_resultat` n'a pas d'essai d'artefact → **CE2-04**.

**7. Reste (R1–R14, R3, R4, R9, chiffres, provenance).** **R1** : les 8 sections pleines, pièces et empreintes gelées
(sauf les deux empreintes d'entrée 2, au scellement) ; aucun chiffre non vérifié trouvé (la puissance et les comptes de
banque se rejouent/concordent ; la référence de surface 0,69/0,50 est dite non auditée ; l'annexe de dépense est dite
non opposable). **R2** : la v2 est bien contre-lue deux fois ; ce rapport est la seconde. **R3** : « run décisif exigé »
(R-344) et la puissance modeste divulguée — compatible, aucun run ne vise un signe (bras sans gradient apparié,
réfutation définie). **R4** : audit de symétrie prévu, bilatéral (> 0,95 **ou** < 0,30, |Δ| > 0,40) ; sa condition est
posée par l'analyste, pas par une fonction unique → CE2-09. **R9** : graines expérimentales par `SeedSequence`
(`boucle.graine/graine_ronde`), entropie E au scellement, graine de sonde = choix de l'organisme (dit) ; manifeste
d'extraction portant versions/carte/commit (revision_resolue None, divulgué). **R5/R10–R14** : gardes testées (ci-dessus)
; versionnage respecté ; verdict de porte R13 réservé à un sous-agent neuf. **Provenance des décisions de Lazar** :
R-344 (18:39, « ok »/« oui »), R-351 (clés `RR_*`), R-355 (GO-2026-10-24-05 « calcul », sans devis), R-356 (« execute
les R1 R2 ») — toutes concordent entre `decisions-lazar-2026-10-24-v1.md`, `messages-lazar-session-2026-10-24-v1.md` et
`extrait-registres-v2.md` (empreintes des extraits vérifiées). GO-2026-10-24-05 est bien de type « calcul », échéance
2026-11-30, sans plafond fixé par Lazar — conforme à la hiérarchie de décision (dépense de calcul = nœud tranché par
Lazar).

---

## Ce que j'ai rejoué

Tout sous `env -i PATH=/usr/bin:/bin HOME=<travail>`, `python3 -B` (interpréteur `.venv` du dépôt), sur des copies ;
les suites qui lancent des sous-processus isolés tournées dans un espace de noms de montage avec `/var/tmp` lié au
scratchpad ; aucune écriture dans les pièces ni le dépôt ; aucun appel réseau ; aucune évasion ; root dans le conteneur,
aucun processus laissé (vérifié : `pgrep -u 60000…61002` vide), `/var/tmp/essaim-m3` nettoyé.

1. **Empreintes** : toutes les pièces (compagnons OK) ; empreintes citées par la v2 (analyse, collisionneur, traits,
   banque, MISSION, note, puissance, validateur, gabarit) **concordantes**. Texte relu = `6ae4a8b3…`.
2. **Validateur du dépôt** (`controle_ia.prereg`, bouchons de scellement) : une seule plainte — « contre-lecture 2 sans
   ses deux empreintes » ; entrée 1 porte bien ses deux empreintes. `travail/sortie-validateur-v2.txt`.
3. **Suite du noyau** (78 tests) : 74 passent, 4 échouent par manque des organismes de la relève / de la banque réelle
   (`gemini-v2`, `banque/traces-sabotage-lot1-…`, `reference_traits_texte`) — attendu, non compté (consigne).
   `travail/sortie-pytest-complet.txt`.
4. **Gardes du mode réel** (constructions sans appel, clés factices) : chaque refus et son message
   (`travail/sortie-gardes-masquees.txt`, `sortie-garde-go-type.txt`, `sortie-garde-depuis.txt`) — dont la garde CE-02
   de l'entraîneur, la garde CE-07 du budget, la garde « même banque » de `--depuis`, la garde GO-type.
5. **Commande B_r telle qu'écrite** : refus `--depuis`/`--organisme-impose` reproduit ; B_r sans `--organisme-impose`
   passe et réimpose les mêmes g000 (`travail/sortie-bras-b-commande.txt`).
6. **Noms de lignées** : le noyau forme `gemini-argon` ; `gemini-4-argon` coupe les deux paires → invalide
   (`travail/sortie-noms-lignees.txt`).
7. **Puissance de H-G1** : rejouée aux paramètres cités → **identique** à `puissance-v1.json`
   (`travail/sortie-puissance-rejouee.txt`) ; contrôle positif conforme.
8. **Simulation adverse (tâches partagées)** : bootstrap du code vs bootstrap croisé, sous effets de tâche hétérogènes ;
   « confirmé » sous nul ≤ 2 %, couverture d'IC ≈ 92 % (code) vs 97 % (croisé) (`travail/sortie-taches-partagees.txt`).

## Ce que je n'ai pas pu vérifier

- **Le modèle réel et les traits eux-mêmes** : pas de carte, pas de Llama-3.1-8B, pas de jeton (et interdit) ; seuls les
  manifestes et empreintes des traits ont été lus. L'honneur de `--revision` par `from_pretrained`, le placement exact
  du texte dans le gabarit de dialogue et l'équivalence « 7 000 car. ≈ 2 048 jetons » ne sont pas mesurés (la v2 dit
  n'avoir servi que `traits-16384`, sans troncature : ce risque ne porte pas sur les traits servis).
- **La banque elle-même** : seuls les comptes agrégés (`resume-banque-confrontation-v1.md`) et la documentation ; pas les
  textes ni les vérités. Je n'ai pas rejoué la référence de surface 0,69 / 0,50 (dite non auditée) ni l'équilibre fin.
- **Les courses réelles** : aucune (nœud de dépense ; interdit). Le comportement des organismes réels, leur usage de
  `entrainer`/`predire`, le nombre d'appels et la non-détermination ne sont pas observés — c'est l'objet du run décisif.
- **Les deux lignées imposées (code)** : seule leur documentation est fournie (empreintes d'arbre `3e6fe2e9…`,
  `bceb1332…` annoncées, non recalculables ici faute du `organisme/`) ; je n'ai pas vérifié si elles appellent
  `entrainer` (le texte dit qu'elles ne le font pas et les met hors de H-G1 : cohérent).
- **Les deux tests exigeant les organismes de la relève de Gemini** : non rejoués (aucun dans les pièces ; consigne) —
  non compté comme défaut.
- **La dépendance SDK de l'en-tête d'espace de travail** (CE2-05) : non vérifiable sans réseau ni clé.
- **La simulation adverse (point 8)** repose sur un modèle de variance du relecteur (non opposable, R7) : elle établit
  la direction (bootstrap du code un peu anticonservateur sous forts effets de tâche partagés, mais « confirmé » sous
  nul ≤ 2 %), pas un chiffre opposable.
